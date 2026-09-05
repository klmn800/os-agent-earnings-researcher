---
name: sec-8k-acceptance-time-as-timing-source
description: Derive bmo/amc from the ET clock time a company furnishes its 8-K Item 2.02 — resolves unknown_time in bulk with no web calls, with hard-won rules about which times are trustworthy
metadata:
  type: reference
---

`https://data.sec.gov/submissions/CIK<10-digit>.json` → `filings.recent` has parallel arrays including **`acceptanceDateTime`** and **`items`**. For 8-Ks whose `items` contain **`2.02`** (Results of Operations), the furnish time in ET tells you whether the company released **bmo** or **amc**. It's the company's own filing, so it's a primary source, which makes it the highest-leverage tool against an `unknown_time` backlog. Fetch via `urllib`/curl with the project UA (see [[reference-sec-via-curl]]); ~0.1s sleep between CIKs.

## ⚠⚠ DO NOT timezone-convert `acceptanceDateTime` — the field's timezone is inconsistent

It is suffixed `Z`, but **the `Z` is a lie for a large subset of filings**. Proven 2026-07-31 against EDGAR's own ET-rendered `Accepted` field:

| Filing | `acceptanceDateTime` | true ET (`Accepted`) | field was |
|--------|----------------------|----------------------|-----------|
| ROST 2026-05-21 | `16:02:44Z` | 16:02:44 | **ET** |
| RDW 2026-05-06 | `16:32:17Z` | 16:32:17 | **ET** |
| BJ 2026-05-22 | `07:27:34Z` | 07:27:34 | **ET** |
| CSCO 2026-05-13 | `20:06:53Z` | 16:06:53 | UTC |
| TECH 2026-05-06 | `10:30:36Z` | 06:30:36 | UTC |
| TOL 2026-05-19 | `20:42:45Z` | 16:42:45 | UTC |
| **CHD 2026-05-01** | `11:08:26Z` | 07:08:26 | UTC |
| **CHD 2026-07-31** | `07:04:30Z` | 07:04:30 | **ET** |

**It is not per-filer** — CHD flipped between its own consecutive quarters, so you cannot calibrate once per CIK and reuse it. Applying a blanket UTC→ET conversion silently turns ET-stamped **amc** filers into midday "ambiguous" (ROST 16:02→12:02, RDW 16:32→12:32) and **bmo** filers into implausible pre-dawn times (BJ 07:27→03:27) — i.e. it destroys exactly the classification the technique exists to make, and it does so *quietly*, producing values that still look like plausible clock times.

**Authoritative source for the ET furnish time:**
`https://www.sec.gov/Archives/edgar/data/<cik>/<accession-no-dashes>/<accession-with-dashes>-index.htm` → the `Accepted</div> <div class="info">YYYY-MM-DD HH:MM:SS</div>` field, which EDGAR always renders in ET. Costs one extra HTTP call per filing; that is the price of the technique being correct. Regex:
`r'Accepted</div> <div class="info">([^<]+)</div>'` after collapsing whitespace.

**Local CIK lookup:** SEC's full ticker→CIK map was delivered to the inbox 2026-07-30 and now lives at **`inbox/processed/company_tickers_20260731.json`** (~10.4k tickers, `{"0": {"cik_str":…, "ticker":…, "title":…}, …}`). Build `{ticker: cik}` from it instead of hitting the network per symbol — and note that **a ticker missing from this map means "renamed or delisted, go check `submissions/CIK….json` for the current `tickers` array"**, not "delisted" (see [[IAC ticker is now PPLI (People Inc.)]]).

**Cheap sanity heuristic when you can't spare the extra calls:** real earnings furnishes cluster at 06:00–09:30 and 16:00–16:50 ET. If a blanket conversion moves a whole filer into 10:00–15:00, suspect the conversion, not the filer.

## Classification rules — do not loosen these

Used 2026-07-15 to resolve **29 `unknown_time` symbols** out of a 69-symbol backlog in one pass.

- **bmo** = furnish **< 09:30 ET** (LINE legitimately furnishes 02:00–03:06 ET; still bmo — don't impose an early-morning floor).
- **amc** = **16:00–16:50 ET only**.
- **17:00–22:00 = AMBIGUOUS, never amc.** These are *late administrative filings for a morning release*. KBR furnishes 19:47–21:00 and LDOS 17:55–20:29 — **both actually report bmo**. A naive "≥16:00 ⇒ amc" rule wrote both wrong. Discard the symbol instead.
- Require **≥3 usable** (non-ambiguous) observations.

## ⚠ Recency beats majority — timing regime changes are real and recent

Companies **move** between bmo and amc, and a majority-vote over 8 quarters returns the *stale* answer:

| Symbol | Change | Evidence |
|--------|--------|----------|
| **ET** (Energy Transfer) | amc → **bmo** in 2026 | last 2 qtrs 07:36/07:41; older 6 at ~16:20 |
| **PODD** (Insulet) | amc → **bmo** in 2025 | 4 recent at ~07:05; 4 older at ~16:03 |
| **VFC**, **CPRI** | amc → **bmo** | 6 recent bmo, 2 oldest amc |
| **DIS** (Disney) | amc → **bmo** (~2023) | 8 straight qtrs ~06:42 — legacy "DIS = amc" prior is simply wrong now |

**Rule: the most recent 4 usable observations must be unanimous.** If they split, the symbol is mid-regime-change — it needs a company source, not a pattern (that's ET's status as of 07-15).

### ⚠⚠ Unanimity does NOT protect the quarter the change happens in — diff the advance PR (2026-08-07)

**AAON** furnishes its Item 2.02 at **07:00–07:18 true-ET, 6/6 quarters** — recent-4 unanimous, no ambiguity, the cleanest `bmo` signature this technique produces. It was **wrong by a session**: AAON's own Q2-FY26 PR says the call is **5:00 p.m. EDT** and "**The results will be released after market close.**"

The catch came from **diffing the advance PR's timing sentence against the prior quarter's**, and the diff is unmistakable:

| Quarter | PR call time | PR release sentence |
|---|---|---|
| Q2 FY25 (PR 2025-07-24) | 9:00 a.m. EDT | "released **earlier that morning**" |
| Q1 FY26 (PR 2026-04-23) | 9:00 a.m. EDT | "released **earlier that morning**" |
| **Q2 FY26 (PR 2026-07-23)** | **5:00 p.m. EDT** | "released **after market close**" |

Both fields moved together ⇒ deliberate change, not boilerplate drift.

**The rule this adds:** recency-beats-majority only catches a regime change *after* it appears in the filing history — it is structurally blind to the first quarter of the change, and in that quarter it answers with full confidence. **The advance PR carries the new regime one quarter earlier than any filing can.** So when a company issues an advance PR, read its timing sentence **even when the furnish history is unanimous**, and read the *previous* quarter's sentence too — the signal is the diff, not the sentence. Where the PR and the filing history disagree, the PR wins; it describes the quarter you are actually pricing.

Corollary for the bulk sweep: a unanimous furnish history is grounds to write a time only for symbols with **no advance PR channel at all** (see [[ir-rss-feeds-beat-spa-pages]] for who those are). Everyone else gets the PR read first.

## Live validation 2026-08-03 — both hard rules held against company sources

Two symbols on the same day tested the two rules most likely to be "loosened" out of impatience. Both rules were right and loosening either would have produced a whole-session directional error.

- **The ambiguous band is real, and it extends through midday.** **AME** (AMETEK) furnishes its Item 2.02 at **10:56–14:05 ET** — no cluster anywhere near the 06:00–09:30 or 16:00–16:50 bands. AMETEK's own PR: *"will issue its second quarter 2026 earnings release **before the market opens** on Tuesday, August 4, 2026,"* call 8:30am ET. So a **midday furnish means the 8-K is a late administrative filing for a morning release** — exactly the KBR/LDOS shape, just shifted earlier. Generalise the rule: **anything outside 06:00–09:30 and 16:00–16:50 is ambiguous, in both directions.** Never read midday as amc *or* as dmh.
- **Recency-beats-majority was right, but only a company source could prove it.** **ON** (onsemi) shows 16:05/16:10 for its last two quarters against 08:05 for the three before — a live bmo→**amc** flip, and the recent-4 were *not* unanimous, so the rule correctly refused to answer. onsemi's PR put the call at **5:00pm ET on Aug 3 "following the release"** ⇒ amc. The flip was real. Add ON to the regime-change table above.

**New contamination case:** **APO** (Apollo) furnishes an Item 2.02 on roughly the **1st of every month at ~16:30 ET** — those are **NAV/alternative-net-investment-income filings, not earnings**. Its actual earnings 2.02s sit at **06:31 ET (bmo)**. Screening on "most recent 2.02" would have returned amc and been wrong by a session. Same family as the ETSY debt-8-K case below, but far more frequent — a monthly cadence of decoys.

## ⚠ Other contamination

- **Not every Item 2.02 is an earnings release.** ETSY's 2026-02-18 8-K (items `1.01,2.02,7.01,9.01`, 16:11 ET — a debt announcement) polluted its otherwise-perfect 07:0x bmo cadence. Combined-item 8-Ks are the usual culprit.
- **Foreign private issuers file 6-K, which has no `items` field** ⇒ the *item-code* screen is blind to them: KB, BBVA, ING, AU, BEPC, CCJ, SMFG, MUFG, CCEP, YPF, NVO, RIO, SN, MFG, BP, JD, SE, NU, XP, SQM, XPEV, DNN. Use their own IR calendars per [[company-earnings-cadence]] — **but read the next section first, the blindness is only partial.**

## ✅ 6-K filers are not actually blind — screen `primaryDocDescription` (2026-08-04)

`filings.recent` carries a **`primaryDocDescription`** array alongside `form` and `items`. It is free text the filer supplies, and foreign issuers routinely put the filing's *identity* in it — which recovers most of what the missing `items` field costs.

**BP** was confirmed on 08-04 from nothing else: its 6-K that morning was described **`"2Q26 BP PLC SEA"`** (SEA = Stock Exchange Announcement, i.e. the results release), dated *04 August 2026*, accepted **06:37 ET**. BP has **no usable IR feed at all** — `www.bp.com/rss`, `/rss/news-releases.xml`, `/feed` and three more paths all 404, and `/investors` is an SPA — so without this field the symbol was unresearchable. The same pass showed BP's other two 6-Ks that week described `"TOTAL VOTING RIGHTS"` and `"BATCH FILING"`, i.e. **the field discriminates cleanly between the results filing and the routine noise** that makes 6-K streams so hard to read.

**How to use it:** in the bulk sweep, for `form == "6-K"`, match `primaryDocDescription` against something like `results|earnings|interim|half.?year|SEA|[1-4]Q\d\d|Q[1-4]`, and treat a hit the same way you treat an Item 2.02 — the acceptance time then gives bmo/amc under the *same* classification rules and the *same* never-timezone-convert caveat. Verify by fetching the document, as with any 2.02.

⚠ Two limits: the field is **filer-supplied and unstandardised** (BP uses `SEA`; CCEP's results 6-K on the same day was not distinctively labelled and had to come off its IR feed), and it is **absent or generic** for plenty of filers. So this narrows the blind spot rather than closing it — try it before falling back to the IR calendar, not instead of.

## Validation (do this before trusting a batch)

Cross-check derived verdicts against symbols where the DB **already** has a known bmo/amc: 2026-07-15 → **31 agree / 7 disagree**, and **all 7 disagreements were DB errors, not method errors** — independently proven on **DIS** (Disney's own PR: "release results before the opening of regular trading") and **FOX** (its own PR: "Results will be released at approximately 8:00 a.m. ET"). DB time errors found this way: **DIS, FOX, FOXA, TECH, DKNG, SYY** are bmo (DB said amc); **WMB** is amc (DB said bmo).

## Companion check — cadence-verify the DATE before confirming

The technique gives **time**, not date. `earnings_confirm.py --time X` (no `--date`) leaves `earnings_date` alone **but still stamps `date_confirmed=1`**, which suppresses the symbol from future dispute lists. So before writing, sanity-check each DB date against the **same quarter's year-ago 8-K**, weekday-aligned (`year_ago + 364d`); flag |diff| > 4d. On 2026-07-15 that flagged 8 of 37 (ADT +7, ARE +14, DOC +12, HST +7, MRK +7, **MSI −7**, PSN −7, SNDK −8) → wrote the time, then reset `date_confirmed=0` so they keep surfacing. **MSI is the cautionary tale**: DB 07-30 vs actual Q2 filings 2025-08-07 / 2024-08-01, and **no feed challenged it** — it would have been silently locked to a wrong date.

Related: [[reference-sec-via-curl]], [[company-earnings-cadence]], [[window-gating-and-noop-sessions]], [[feedback-direct-db-query]].
