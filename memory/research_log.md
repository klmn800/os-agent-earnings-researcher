# Earnings Research Log

> Active log: full sessions for the last ~2 weeks (newest first, below), a compact ledger of
> confirmed-but-upcoming dates, and the open carry-overs with next-check dates. Older sessions live in
> the season archives: `memory/archive/research_log_2026-Q2_spring-earnings.md` (through 06-30) and
> `memory/archive/research_log_2026-Q3_summer-earnings.md` (07-01 → 08-28, plus the summer's full
> confirmation ledger and carry-over table as appendices). Maintenance notes at the very bottom.
> Per-symbol cadence/lead-times live in `memory/reference_company_cadence.md` — **grep it by symbol
> (`^| SYM `); don't read it whole (~180 KB).**

## Open Carry-Overs — unresolved, with next-check dates

Symbols held because no company-issued source exists *yet*, plus confirmed rows under suspicion.
Next-check ≈ **advance-PR due date + 1** (most advance PRs publish after the ~07:15 session starts —
see the standing rules in `reference_company_cadence.md`). Rebuilt from the DB on 2026-09-13.

| Symbol | DB date | Status | Next check |
|--------|---------|--------|------------|
| **CCL** | 2026-09-28 `bmo` (unconfirmed) | Q3 FY26 (Aug-31 qtr). stocktitan spine current to 09-10 (brand news only) as of 09-15, no advance. Q2 lead was 12d (PR 06-11 → 06-23) ⇒ due ~09-16. Q2 shape: *"conference call … at 10 a.m. (EDT)"*, results *"expected to be released that morning"* ⇒ bmo. | **2026-09-16** |
| **UEC** | 2026-09-24 `amc` (unconfirmed) | FY-end (Jul-31 FY) date PR not out as of 09-11 (stocktitan newest 07-23; EDGAR nothing since 07-31). FY26 Q2/Q3 advances ran **7d at 07:00 ET** ⇒ due ~09-17, readable the same morning. ⚠ Stored `amc` is wrong under either reading of the FY-end pattern (10-K the prior evening, webcast next morning) — expect `bmo`. | **2026-09-17** |

### Window watch — unconfirmed rows the horizon will surface soon

Not carry-overs (never researched this quarter); listed so Monday knows which advance-PR windows are
already open. Leads come from **other fiscal quarters** unless noted — per the WSM/CPRT lessons they are
advisory: read the channel anyway.

| Symbol | DB row | Cadence says | Window |
|--------|--------|--------------|--------|
| MU | 09-30 amc | fiscal-Q3 lead ~28d | **open** (~09-02) |
| STZ | 10-06 **`bmo`** | amc (Q1 FY27, 1 obs); ~4wk | **open** (~09-08) — ⚠ stored time contradicts |
| PEP | 10-08 bmo | ~35d (1 obs) | **open** (~09-03) |
| DAL | 10-08 bmo | lead never logged | unknown — check `news.delta.com` |
| ACN | 10-01 **`amc`** | bmo every observed quarter; ~16d | opens ~09-15 — ⚠ stored time contradicts |
| 10-13 → 10-16 cohort (37 rows) | banks, JNJ, ABT, ASML, TSM, … | 14 have fresh cadence rows (09-13); 23 are first-time names | measured leads ~27–35d (SCHW, FHN, ALLY, PEP) ⇒ **opening now** |

## Upcoming Confirmed — locked dates (don't re-research)

One line per confirmed symbol whose date is still ahead (≥ 09-14), rebuilt from `earnings_upcoming` on
2026-09-13 — 13 rows; the old table had drifted (6 of these were never added to it). Format:
`SYM | date | time | source — session`. Prune reported rows each Sunday; the summer's full ledger is
the summer archive's Appendix A.

| Symbol | Date | Time | Source — session |
|--------|------|------|------------------|
| LEN | 2026-09-16 | amc | Lennar PR 09-02 17:30 ET (`investors.lennar.com/rss/press-releases`) — ⚠ headline names the *call* (09-17), body names the release (09-16) — 09-03 |
| CTAS | 2026-09-23 | bmo | BusinessWire 09-09 13:00 ET *"Cintas Corporation Announces Webcast for First Quarter Fiscal Year 2027 Results"* (via stocktitan); bmo = 10am webcast + Item 2.02 08:31–08:34 ET 6/6 — 09-10 |
| GIS | 2026-09-23 | bmo | General Mills advance 08-26 08:00 ET (BusinessWire); release issued that morning, webcast 8am CT — 09-02 |
| PAYX | 2026-09-23 | bmo | Paychex GlobeNewswire 09-09 09:15 ET (via stocktitan): *"Wednesday, September 23, 2026, before the financial markets open,"* call 9:30am ET. **Corrected from 09-29** — 09-14 |
| DRI | 2026-09-24 | bmo | Darden PR 08-27 16:00 ET (`investor.darden.com` feed): *"before the market opens"* — 09-03 |
| MTN | 2026-09-28 | amc | Vail PRNewswire 09-04 16:05 ET (via stocktitan): *"after market close on Monday, September 28, 2026,"* call 5pm ET — 09-14 |
| JEF | 2026-09-28 | amc | Jefferies advance 09-14 16:30 ET (`ir.jefferies.com` feed + news-details page): *"Monday, September 28, 2026 after market close."* Dispute resolved — finnhub 09-30 wrong — 09-15 |
| KMX | 2026-09-29 | bmo | CarMax BusinessWire 09-09 17:00 ET (via stocktitan): *"before the market opens on September 29, 2026,"* call 8am ET. Re-sourced 09-14 (09-08 lock was unsourced) — 09-14 |
| CNXC | 2026-09-29 | amc | GlobeNewswire 09-08 *"Concentrix Schedules Release of Third Quarter 2026 Financial Results…"*: after close, call 5pm ET — 09-09 |
| CAG | 2026-09-30 | bmo | Conagra PRNewswire 08-31; bmo **inferred** (materials "that morning" ahead of a 9:30am ET Q&A) — 09-09 |
| FDS | 2026-09-30 | bmo | FactSet GlobeNewswire 09-02 11:00 ET; presentation 8:30am, call 9:00am ET — 09-03 |
| JBL | 2026-09-30 | bmo | Jabil feed 09-09 16:10 ET: *"before the market opens,"* call 8:30am ET — 09-10 |
| MKC | 2026-10-01 | bmo | McCormick PRNewswire 08-31 08:00 ET (via stocktitan; IR host 403s); call 8am ET — 09-10 |
| NKE | 2026-10-01 | amc | Nike feed 08-28: *"approximately 1:15 p.m. PT, following the close"* — 09-10 |
| LW | 2026-10-06 | bmo | Lamb Weston scheduling release (~8:00am ET release, 9am call) — ⚠ weakest confirm on the list: no first-party fetch succeeded (IR 403 wall, no 8-K); rests on consistent search summaries + yfinance — 09-09 |

---

# Research Sessions (newest first)

## Session: 2026-09-15 (Tuesday) — 07:13 AM ET

3 surfaced (JEF dispute `date_disagreement`; UEC, CCL unconfirmed). **1 confirmed (JEF), 2 gated (UEC, CCL)**.
Reads: 1 RSS (WebFetch + curl), 1 IR news-details page, 2 stocktitan spines, 1 search (discarded). ⚠ Prompt
header said "1 symbols"; the hook injected 3 (1 dispute + 2 unconfirmed). Harmless count mismatch.

### Confirmed

| Symbol | Result | Source |
|--------|--------|--------|
| **JEF** | **2026-09-28 `amc`** (DB right, finnhub 09-30 wrong) | Jefferies feed item **09-14 16:30 ET**, *"Jefferies to Release its Third Quarter Financial Results on September 28, 2026"*. Body (IR news-details page, via WebFetch): *"will release its third quarter financial results on Monday, September 28, 2026 after market close."* Lead **14d**, exactly as predicted. Dispute row `confirmed_agent`. Calendar row verified `1 / agent`. |

### Gated

| Symbol | DB date | Why skipped | Next check |
|--------|---------|-------------|------------|
| UEC | 2026-09-24 `amc` | stocktitan newest still 07-23, no FY-end advance. Not due until ~09-17 (7d lead, 07:00 ET). `bmo` caution stands. | 2026-09-17 |
| CCL | 2026-09-28 `bmo` | stocktitan current to 09-10, brand news only, no Q3 advance. Due ~09-16 (12d lead). | 2026-09-16 |

### Notes
- **The JEF carry-over resolved exactly on schedule.** The 09-09 correction (the channel exists, read the morning after
  the 14d due date) was right. The 09-08 "no advance PR" conclusion would have held the dispute to 09-25.
- **The WebSearch summary asserted "Sep 30" for JEF**, citing Investing.com, against the company's own feed title.
  Third-party search summaries still parrot the finnhub estimate even after the company has spoken. Discarded.
- The IR news-details page is a 259 KB JS shell to curl (no body text). WebFetch renders the body. Feed titles
  carry the date but not the timing.
- The `earnings_confirm.py` patch is **still not live** (`--help` shows no `--time-only`). Used the full
  `--date --time --by agent` form, which is correct for a company-sourced date.

## Session: 2026-09-14 (Monday) — 07:13 AM ET

4 surfaced (JEF dispute `both`; UEC, CCL, MTN unconfirmed) + the 2 priority carry-overs due today
(PAYX, KMX). **3 confirmed (MTN, PAYX, KMX), 1 corrected (PAYX 09-29 → 09-23), 3 gated (JEF, UEC, CCL)**,
plus the JEF time write. Reads: 1 RSS, 2 feed probes (Vail 403), 5 stocktitan spines, 3 stocktitan articles. 0 searches.

### Confirmed / corrected

| Symbol | Result | Source |
|--------|--------|--------|
| **PAYX** | **2026-09-23 `bmo`** — ⚠ **corrected from the unsourced 09-08 lock (09-29)**; yfinance's drift flag was right | Paychex GlobeNewswire **09-09 13:15Z**, *"Paychex Schedules First Quarter Fiscal 2027 Earnings Conference Call on September 23, 2026"*: *"Wednesday, September 23, 2026, before the financial markets open,"* call 9:30am ET. Lead **14d**. Resolved the 09-11 `confirmed_row_diverged` row. ⚠ Q1 moved from Tuesday (2/2 prior years) to **Wednesday** — the weekday history would have kept the wrong date. |
| **KMX** | **2026-09-29 `bmo`** (lock was right, now sourced) | CarMax BusinessWire **09-09 21:00Z**, *"CarMax Announces Second Quarter Conference Call"*: *"before the market opens on September 29, 2026,"* call 8:00am ET. Lead **20d**. Cached BW `20260909520212`. |
| **MTN** | **2026-09-28 `amc`** (DB right) | Vail PRNewswire **09-04 20:05Z**, *"Vail Resorts Announces Fiscal 2026 Fourth Quarter and Year-End Earnings Release Date"*: *"after market close on Monday, September 28, 2026,"* call 5:00pm ET. Lead **24d**, matching Q3's 24d. `investors.vailresorts.com` **403s both RSS paths even with a browser UA**. Cached the PRNewswire permalink. |

### Gated

| Symbol | DB date | Why skipped | Next check |
|--------|---------|-------------|------------|
| JEF | 2026-09-28 (`amc` now) | Feed current to 09-09, no Q3 advance. Expected: at the 14d lead the 09-28 advance would publish ~16:20 ET **today**. **Wrote `earnings_time='amc'`** via plain UPDATE (`date_confirmed` stays 0). Evidence: the feed itself shows results releases at 16:15/16:16 ET (Q1 03-25, Q2 06-24). | 2026-09-15 |
| UEC | 2026-09-24 `amc` | stocktitan newest still 07-23; no FY-end advance. Due ~09-17 at the 7d lead. `bmo` caution stands. | 2026-09-17 |
| CCL | 2026-09-28 `bmo` | stocktitan current to 09-10 (brand news only), no Q3 advance. Q2 lead was 12d ⇒ due ~09-16. | 2026-09-16 |

### Notes
- **The 09-08 confirm-tool-as-time-fix error cost exactly one wrong date out of two** (PAYX −6d; KMX happened
  to be right). Both advance PRs had been out since **09-09**. That's 5 days of a wrong locked row that the
  normal dispute stream suppressed. Only the `confirmed_row_diverged` flag surfaced it.
- **stocktitan JSON-LD found all 3 advances in 5 spine reads.** MTN's had been sitting there since 09-04; the
  window-watch table said "open ~09-04" and nobody read it. Window-watch rows with an open window should
  get a spine read the day they open, not wait for the horizon.
- `--sql` `;` split hit again (a `;` inside the `notes` literal) — see [[reference-db-write-forward-slash-paths]]. Retried without it.

## Session: 2026-09-11 (Friday) — 07:16 AM ET

2 surfaced (JEF dispute `both`, UEC unconfirmed): **0 confirmed, 2 gated** — both re-surfaced ahead of
their recorded next-check dates (09-15 / 09-17), so this was an early-fire probe only. 5 HTTP reads, 0 searches.

| Symbol | DB date | Why skipped | Next check |
|--------|---------|-------------|------------|
| JEF | 2026-09-28 (Unknown) | `ir.jefferies.com/rss/pressrelease.aspx` read OK, newest item 09-09; **no Q3 advance**. One unlogged item: *"Jefferies Financial Group Inc. to Host Annual Investor Meeting"* (09-03 16:30 ET) — meeting **Mon 10-19-2026 9:00am**, Manhattan; body says nothing about Q3 results (read via WebFetch — the news-details HTML is a shell to urllib, RSS carries headline only). Not informative for 09-28 vs 09-30. ⚠ **Third candidate (Ben, 09-11):** third-party estimates show **10-05** (+35d post-qtr-end — outside the 24–29d band on 5 recorded quarters, so least likely by cadence, but estimate-only, not a source either way). At the 14d lead its advance would land ~**09-21**, so an empty feed on 09-15/09-16 rules out 09-28/09-30 progressively but says nothing against 10-05 — keep checking through ~09-22 before reading silence as signal. | 2026-09-15 |
| UEC | 2026-09-24 `amc` | stocktitan newest still 07-23; EDGAR (CIK 1334933) nothing but Form 4 / 13G since 07-31, no 8-K. FY-end advance due ~09-17 at the 7d lead. Prior `bmo`-not-`amc` caution (09-10 entry) still stands. | 2026-09-17 |

## Session: 2026-09-10 (Thursday) — 07:16 AM ET

6 surfaced (5 disputes + UEC unconfirmed): **4 confirmed (CTAS, JBL, MKC, NKE), 2 gated (JEF, UEC)**.
**WebSearch was down for the whole session** (6/6 attempts returned "unavailable"), so every
confirm came from the fallback stack: IR RSS feeds (browser UA), stocktitan JSON-LD, and EDGAR
submissions. All four were read off company-issued text; none needed search.

### Confirmed (4)

| Symbol | Result | Source |
|--------|--------|--------|
| CTAS | **2026-09-23 `bmo`** (DB right; finnhub 09-30 wrong) | BusinessWire **09-09 13:00 ET**, *"Cintas Corporation Announces Webcast for First Quarter Fiscal Year 2027 Results"* — releases Wed 09-23, webcast **10:00am ET** same day. Found via `stocktitan.net/news/CTAS/` JSON-LD. PR states no clock time; `bmo` rests on the 10am webcast + Item 2.02 furnish 08:31–08:34 ET 6/6. BW `20260909223284`. No IR URL cached (no first-party host exists). |
| JBL | **2026-09-30 `bmo`** (DB 09-24 wrong; **yfinance right**) | `investors.jabil.com` feed → *"Jabil Announces Date for Fourth Quarter and Fiscal Year 2026 Earnings Release and Investor Briefing"* **09-09 16:10 ET** — *"Wednesday, September 30, 2026, before the market opens,"* call 8:30am ET. Lead **21d**. `earnings_upcoming` already held 09-30 (adopted from yfinance after the dispute snapshot). Cached `investors.jabil.com/rss/pressrelease.aspx`. |
| MKC | **2026-10-01 `bmo`** (DB right; finnhub 10-05 wrong) | PRNewswire **08-31 08:00 ET**, *"McCormick & Company to Report 2026 Third Quarter Financial Results on October 1, 2026"* — call **8:00am ET**. Found via stocktitan (`ir.mccormick.com` **403s every path** to urllib). `bmo` also 100% on furnish history (Item 2.02 06:40–07:39 ET every quarter since 2020). Lead **31d**. |
| NKE | **2026-10-01 `amc`** (DB right; finnhub 09-28 wrong) | `investors.nike.com` feed → *"NIKE, Inc. Announces First Quarter Fiscal 2027 Earnings and Conference Call"* **08-28** — *"Thursday, October 1, 2026, at approximately 1:15 p.m. PT, following the close."* Lead **34d**. Time was Unknown → `amc`. Cached IR URL upgraded to the feed. |

### Gated (2)

| Symbol | DB date | Why skipped | Next check |
|--------|---------|-------------|------------|
| JEF | 2026-09-28 (Unknown) | `ir.jefferies.com/rss/pressrelease.aspx` **works** (current to 09-09), no Q3 advance yet — expected, due ~09-14 for 09-28 or ~09-16 for 09-30 at the 14d lead, and Jefferies publishes ~16:20 ET ⇒ check the morning after. Time still `amc` 4/4 but unwritten (no time-only confirm mode). | 2026-09-15 |
| UEC | 2026-09-24 `amc` | No FY26 year-end date PR yet (stocktitan + uraniumenergy.com, newest item 07-23). UEC's FY26 Q2/Q3 advances ran **7d leads at 07:00 ET** ⇒ due ~09-17 for a 09-24 release. | 2026-09-17 |

### ⚠ UEC — the stored `09-24 amc` is wrong under either reading of the FY-end filing pattern

FY25 year-end: 10-K accepted **2025-09-23 20:43 ET**, results webcast **Wed 2025-09-24 8:00am PT**
(company events page). FY26 Q1/Q2/Q3 all stated *"before markets open"* in the company PR. So the
market reacts on the **morning of the webcast day**. That can be encoded as "D−1 amc" or "D bmo",
but **"D amc" (which is what the DB holds) puts the reaction a day late** under both readings. Did
not write the time, because the 2026 date is unsourced and the FY-end quarter could differ. When
the advance lands, expect `bmo` and check whether the 10-K again drops the prior evening.
FY-end 10-K history: 2025-09-23, 2024-09-26, 2023-09-28, 2022-09-29 (all evening), so 09-24 is
plausible but the band spans ~a week.

### Notes
- **WebSearch outage cost nothing.** The RSS sweep plus one stocktitan spine per symbol found all four
  advance PRs, and three of them were already sitting in feeds the prior session had not probed. The
  fallback stack is now evidence-tested as a *primary* for any symbol with a known feed.
- **JEF's cached IR URL was a Morningstar reprint** (third-party). Replaced with the verified first-party
  feed `ir.jefferies.com/rss/pressrelease.aspx`, which carried the Q2 advance (06-16 16:20 ET). The old
  cheat-sheet listed ir.jefferies.com as "SPA shell"; the HTML is, but the RSS is not.
- **CTAS second lead observation = 14d** (09-09 → 09-23), matching Q4 FY26's 14d. The band now rests on
  2 observations. Publish time 13:00 ET (vs 13:29 last quarter), which confirms the "check the morning
  after" rule; yesterday's empty 07:13 read was the clock artifact predicted.
- finnhub was wrong on all four confirms (CTAS +7d, MKC +4d, NKE −3d, and it matched DB's wrong 09-24 on JBL). yfinance-only dissent (JBL) was right again.

## Session: 2026-09-09 (Wednesday) — 07:13 AM ET

5 surfaced symbols — **3 confirmed (CNXC, CAG, LW), 2 gated (CTAS, JEF)**, ~16 HTTP reads,
6 web searches. Two of the three confirms came from advance PRs that **contradicted the DB date**,
and the session's most useful output is arguably not a confirm at all but a **correction to
yesterday's JEF row** that moves its next-check forward 11 days.

### Confirmed (3)

| Symbol | Result | Source |
|--------|--------|--------|
| CNXC | **2026-09-29 `amc`** (DB 09-24, finnhub 09-30 — both wrong) | GlobeNewswire **09-08**, *"Concentrix Schedules Release of Third Quarter 2026 Financial Results and Investor Conference Call"* — *"after market close on Tuesday, September 29, 2026,"* call 5:00pm ET. Discovered via the cached `ir.concentrix.com/rss/pressrelease.aspx`. |
| CAG | **2026-09-30 `bmo`** (time was Unknown; date not in dispute) | Conagra's own PRNewswire release **08-31**, `conagrabrands.com/news-room/…-prn-122962` — materials *"issued that morning prior to a live question-and-answer session"* at 9:30am ET. Lead 30d. |
| LW | **2026-10-06 `bmo`** (DB 09-30, finnhub 10-01 — both wrong; yfinance right) | Lamb Weston scheduling release — results 10-06, news release ~8:00am ET, call 9:00am ET. ⚠ No first-party fetch succeeded (see below). |

### Gated (2)

| Symbol | DB date | Why skipped | Next check |
|--------|---------|-------------|------------|
| CTAS | 2026-09-23 | Advance PR still absent on the **predicted due date** — but checked at 07:2x, and Cintas publishes these at **13:29 ET**. The absence is a clock artifact, not a signal. | 2026-09-10 |
| JEF | 2026-09-28 | Q3 advance PR exists (correction below) but isn't due until ~09-14 at the 14d lead. Cadence cannot break 09-28 vs 09-30. | 2026-09-14 |

### ⚠⚠ JEF — yesterday's row concluded a channel doesn't exist, on the strength of a search that used the wrong title

The 09-08 row read: *"no separate advance-scheduling PR found in either year — the results release
appears to be the first notice,"* and set next-check **09-25**, i.e. wait for the release itself.

It exists. Every year. On BusinessWire, with an unvarying title shape:

- *"Jefferies to Release its Third Quarter Financial Results on **September 25, 2024**"* — published **2024-09-11** ⇒ **14d lead**
- *"Jefferies to Release its Third Quarter Financial Results on **September 29, 2025**"*

Both name **after market close**. What went wrong is narrow and repeatable: the search was built from
the *Second*-Quarter title already in the cached URL plus "2026", so it only ever matched the current
quarter — which genuinely hasn't published. **An empty result for ‹title› + ‹this year› was read as
evidence about the channel, when it was only evidence about this quarter.** The fix that worked was
searching the title shape against **prior** years (`2025 OR 2024`), which is the cheap way to ask
"does this channel exist?" separately from "has it fired yet?" — two questions the 09-08 search
collapsed into one.

**Cost of the error:** next-check was set 11 days too late. At the now-measured 14d lead a 09-28
release needs its PR by ~**09-14** and a 09-30 release by ~**09-16**, so the DB-vs-finnhub tie is
decidable ~10 days before the old row would have looked. Moved to **09-14**.

⭐ **Generalisable rule, worth carrying:** *before concluding a company has no advance-PR channel,
run the title shape against a prior year.* Absence-of-channel and absence-of-firing look identical in
a single search and have opposite consequences — one says stop waiting, the other says keep waiting.

⚠ Two secondary corrections to the same row: JEF's time is effectively settled at **`amc`, 4/4**
(Q3-24, Q3-25, Q2-25 06-25, Q2-26 06-24) but **was not written** — `earnings_confirm.py` has no
time-only mode and would lock the unsourced date alongside it. And the row's *"Monday matches 2025"*
weekday argument for DB is a **1-year** pattern; 2024's Q3 landed on a Wednesday. Days-after-quarter-end
runs 25d/29d against DB's 28d and finnhub's 30d — both inside the band, so cadence is genuinely mute here.

### ⭐ CNXC — the 09-03 refusal to lock on `+364d` paid off, and the slip is now the pattern

09-03 declined to write DB's 09-24 even though `+364d` off 2025-09-25 landed on it *exactly* and a
tight **Sep 24–28** Item 2.02 band (2021–2025) appeared to exclude finnhub's 09-30. The stated reason
was that **Q2-26 had already slipped +4d** against that same arithmetic, and a company that moves once
can move again.

Q3-26 slipped **+5d** — to **09-29**, which is **outside the five-year band by a day**. So:

- **Both feeds were wrong**, in opposite directions (DB −5d, finnhub +1d). A tiebreak framing would
  have picked a loser either way; the only winning move was to wait for the PR, which is what happened.
- **Two consecutive quarters of forward slip means `+364d` is now a *lower* bound for CNXC, not a
  centre.** Next year, read the anniversary date as "no earlier than," not "probably."
- **The Sep 24–28 band is broken** and should not be used as a fence again.
- **Lead is drifting with it:** 19d (Q2) → **21d** (Q3, advance 09-08 → release 09-29).

⚠ The gate itself was slightly loose — 09-03 bracketed the PR at "~09-05 (if 09-24) or ~09-11 (if
09-30)" and it landed **09-08**, between the two. The bracket held; the 09-08 row's reading of the
closed 09-05 window as *"a real (mild) counter-signal"* weakening 09-24 was directionally correct.

⚠ Channel note: the cached RSS feed carried the **headline only** — no body, so it establishes
*that* the PR exists but not the date. The date came from the GlobeNewswire release itself. For this
symbol the feed is a **trigger**, not a source; budget a second fetch after it fires.

### ⚠⚠ LW — confirmed with the company's own IR estate entirely unreachable, and no 8-K to fall back on

Two independent fallbacks failed at once:

1. **Blanket 403 bot-wall — NOT the outage it first looked like.** WebFetch timed out on 5/5
   attempts across every path tried (news-releases listing, events-and-presentations, both
   news-release-details slug shapes, the `newsroom-home/press-release-details/2026/…` shape), and
   the first draft of this entry recorded that as a total IR blackout. ⚠⚠ **That was wrong, and the
   file's own standing rule 2 says so:** *try `urllib` + browser UA before concluding a host is
   unreachable.* Doing that returns **HTTP 403 Forbidden, instantly** — on every slug, on the RSS
   path, on `/`, and on a deliberately nonsense path. So the correct reading is **host UP, blanket
   403 to non-browser clients** (the Cintas `gcs-web` shape), not "down." Two consequences that the
   timeout reading would have gotten backwards: the paths are **not** disqualified, and per standing
   rule 3 the host **cannot be used as an existence probe** in either direction — a 403 on a guessed
   slug is not evidence the PR is missing. WebFetch's 60s timeout is a *symptom of the wall*, not a
   measurement of the host.
2. **No 8-K.** EDGAR's submissions API for CIK 1679273 shows **nothing but Form 4s and a 13G/A since
   the 07-24-2026 8-K** — the FY27 Q1 scheduling release was not filed. The **FY26 equivalent was**
   (`lw-20250824x8kxexx9911q26.htm`), so EDGAR looked like a reasonable fallback and isn't one.

Confirmed anyway, on: the release text reproduced **consistently and specifically** across multiple
independent search summaries (10-06, release ~8:00am ET, call 9:00am ET — the same three figures every
time), **plus** yfinance independently at 10-06, **plus** LW's own early-October Q1 history
(2023-10-05, 2022-10-05, 2020-10-07). Flagging the sourcing honestly: this is the weakest-sourced
confirm of the session and the only one not read off a company-controlled surface. The 403 finding
does not strengthen it — it only means a **browser-rendered** fetch would likely succeed where every
scriptable client is refused, which is the same hard tooling dependency already recorded for FDX.

⚠⚠ **The DB date deserves separate note: 09-30 is exactly last year's Q1 release date (2025-09-30).**
That is not a near-miss or a rounding error — it is a **prior-year date sitting in the current-year
row**, the same failure shape worth watching for wherever a DB date lands precisely on `last year ± 0d`
while the company's own multi-year cadence points elsewhere. Here the multi-year cadence (early Oct)
was right and 2025-09-30 was itself the outlier year, so the stale value inherited the one atypical date.

### ⚠ CTAS — the gate fired on the right day and still couldn't see anything, for a boring reason

Today **was** the predicted PR-due date (14d before DB's 09-23), and the check came back empty:
`stocktitan.net/news/CTAS/` newest item still **08-10**, cintas.com newsroom tops out **09-01**, and
`businesswire.com/newsroom` now **403s** (a new blocker — it had been usable).

But the one measured Cintas advance published at **13:29 ET**, and this session runs at **07:13**.
**A 07:1x check on the due date is structurally blind for this symbol** — roughly six hours early
against the only observed publication time. Recording it because the failure is systematic, not
one-off: for any symbol whose advance publishes midday/afternoon, the due-date morning check is
close to free of information and the real check is the *following* morning. Held, next-check 09-10.

Date reasoning unchanged and still favours DB: Q1-only Item 2.02 dates walk one day earlier each year
(2025-09-24 Wed, 2024-09-25 Wed, 2023-09-26 Tue) ⇒ **09-23 Wed**, with finnhub's 09-30 a full week
outside. Time was already repaired to `bmo` on 09-02 (bmo 6/6).

### ⚠ CAG — a `bmo` inferred rather than quoted

Conagra's release says materials are *"issued that morning prior to a live question-and-answer
session"* at 9:30am ET. It **never states a clock time for the release** and never says "before the
market opens." The inference is sound — a morning issue ahead of a 9:30am ET Q&A cannot be `amc` —
but it is an inference, unlike DRI/CNM/GIS whose releases quote the phrase outright. Logged as such
in case a later session needs to know how firmly the `bmo` is held. Date was never in dispute
(reason was `unknown_time`); finnhub's 09-29 is wrong.

### Calibration

**3 confirms / 5 surfaced**, both gates correct and neither one a missed confirmable date. The
session's leverage was concentrated in re-reading yesterday's own conclusions rather than in new
research: CNXC vindicated a prior refusal-to-lock, JEF **overturned** a prior claim of channel
absence, and CTAS explained a prior gate's blind spot. All three prior rows were written by sessions
that had the right instincts and, in JEF's case, one bad search.

**Standing levers after today:**
- **Search the title shape against a prior year before declaring a channel absent.** (JEF; new)
- **For midday-publishing symbols, the due-date morning check is worthless — check the morning after.** (CTAS; new, and cheap to apply)
- **`+364d` is a lower bound, not a centre, for any symbol with a recorded slip.** (CNXC; now 2/2 quarters)
- **Apply standing rule 2 to *timeouts*, not just to refusals.** (LW; new) I read 5/5 WebFetch
  timeouts as "the host is down" and only ran the urllib+UA check while writing this log up — it
  returned an instant 403 on every path including `/`. The rule was already in
  `reference_company_cadence.md` and I skipped it because a timeout *feels* like a network fact in a
  way a 403 doesn't. It isn't.
- Unchanged: feed convergence is corroboration, not a source; a DB date landing exactly on last year's date is a staleness smell (LW).

## Session: 2026-09-08 (Tuesday) — _[no session block was written this day; reconstructed at the 2026-09-13 maintenance from the carry-over rows (now in the summer archive, Appendix B) and `earnings_date_disputes`]_

Surfaced (dispute rows, trade_date 09-08): **CNXC, CTAS** (`date_disagreement`), **JEF** (`both`), **KMX, PAYX** (`unknown_time`). **2 written, 3 held.**

- **KMX 2026-09-29 `bmo`** and **PAYX 2026-09-29 `bmo`** — logged as *"time only, date not in dispute"*, but both rows ended `date_confirmed=1 / agent`: **the dates were locked with no same-quarter company source** (KMX on a 5/5 bmo pattern with its Q2 FY27 advance not yet out; PAYX on a 2/2 Tuesday-bmo pattern with its Q1 FY27 advance not yet out). The time-only path in [[feedback-earnings-confirm-bare-symbol-trap]] (`UPDATE earnings_upcoming SET earnings_time=...`) was the right tool. ⚠ PAYX drew a `confirmed_row_diverged` flag on 09-11 (yfinance 09-23) — see the 09-13 maintenance entry.
- **JEF** — concluded *"no separate advance-scheduling PR; the results release is the first notice"*, next-check 09-25. **Overturned 09-09**: the BusinessWire channel exists every year; next-check moved to 09-14.
- **CNXC, CTAS** — held (both confirmed later: CNXC 09-09, CTAS 09-10).

## Session: 2026-09-03 (Thursday) — 07:13 AM ET

4 surfaced symbols (FDS/CNXC/DRI/LEN) + 1 carry-over swept (ORCL) — **4 confirmed, 1 gated**,
~14 HTTP reads, 1 web search. Every confirm came from a **company-issued advance PR**, and
**three of the four had published within the last 24 hours** (ORCL 09-02 16:00, LEN 09-02 17:30,
FDS 09-02 11:00) — a genuinely unusual clustering that made this a cheap session.

### Confirmed (4)

| Symbol | Result | Source |
|--------|--------|--------|
| FDS | **2026-09-30 `bmo`** (snapshot said 09-17 `amc`) | GlobeNewswire **09-02 11:00 ET**, *"FactSet Schedules Fourth Quarter 2026 Earnings Call"* — results 09-30, presentation 8:30am ET, call **9:00am ET**. `globenewswire.com/news-release/2026/09/02/3354957/7768/en/...` |
| LEN | **2026-09-16 `amc`** (was unconfirmed) | `investors.lennar.com/rss/press-releases` **09-02 17:30 ET** — headline says call **09-17**, body says results *"after the market closes on **September 16, 2026**."* |
| DRI | **2026-09-24 `bmo`** (time was Unknown) | `investor.darden.com/rss/pressrelease.aspx` **08-27 16:00 ET** — *"**before the market opens** on Thursday, September 24, 2026,"* call 8:30am ET. |
| ORCL | **2026-09-10 `amc`** (carry-over, next-check was today) | `investor.oracle.com/rss/pressrelease.aspx` **09-02 16:00 ET** — *"released on **Thursday, September 10th, after the close of the market**,"* webcast 4:00pm CT. |

### Gated (1)

| Symbol | DB date | Why skipped | Next check |
|--------|---------|-------------|------------|
| CNXC | 2026-09-24 amc | Advance PR not due yet — feed live and empty since **08-10**, corroborated independently by stocktitan's JSON-LD showing the same 10-item spine. Q2 lead was **19d** ⇒ PR due ~09-05 (for a 09-24 release) or ~09-11 (for 09-30). Cadence **cannot** break the DB-vs-finnhub tie here (below). | 2026-09-05 |

### ⭐ LEN — the headline names the call date, the body names the release date

Lennar's advance PR is titled *"Lennar Corporation to Broadcast Its Third Quarter 2026 Earnings
Call on **September 17, 2026**"* — and September 17 is **not** the earnings date. The body:
*"will release its third quarter 2026 results **after the market closes on September 16, 2026**,"*
with the call the following morning at 11:00am ET.

**A title-only read writes 09-17 and is wrong by a day, every quarter.** The prior quarter has the
identical shape (PR 05-28 → *"…Earnings Call on June 12"* → results actually **06-11 amc**, wire
timestamp 17:45 ET), so this is Lennar's standing format, not a one-off. DB's 09-16 `amc` was
already right; the risk here was me "correcting" a correct row off the headline. **Open the body.**

This is a distinct failure mode from the release-vs-call ambiguity settled on SQM (08-13): there,
two sources each named a different real event and the question was which one the DB should carry.
Here **one document names both**, and the trap is purely that the *headline* advertises the less
useful one.

### ⚠⚠ CNXC — the case where `+364d` looks strongest and I still refused it

Concentrix's Q1 8-K Item 2.02 history is about as clean as this job gets: **2025-09-25, 2024-09-25,
2023-09-27, 2022-09-28, 2021-09-27** — a five-year **Sep 24–28** band that appears to exclude
finnhub's **09-30** outright, with `+364d` off 2025-09-25 landing on **09-24 = DB exactly**.

That is precisely the shape [[cadence-364d-weekday-aligned-corroborator]] warns about (the AAP
lesson: the strongest-looking precondition match still missed by 7d). And **this symbol has already
broken the arithmetic once this year** — Q2-26 was predicted 06-25 by `+364d`, and the actual was
**06-29**, a +4d slip that finnhub called correctly and the DB did not. Apply that same slip to Q3
and the band moves to **09-28…09-30**, which is finnhub's date.

So the tidy five-year band is an illusion of precision: it describes a company that demonstrably
moved four days one quarter ago. **No lock — wait for the PR (~09-05).** Logged the reasoning in
the cadence row so the next session doesn't re-derive it and reach the opposite conclusion.

### ⚠⚠ `investor.factset.com` is now a hard 403, not a timeout — and the distinction matters

The cadence row has said "IR page fetch timed out" since June, which under
[[ir-rss-feeds-beat-spa-pages]] licenses the inference *"probably my User-Agent — re-probe with a
browser UA."* That is no longer true. Re-probed today across **six paths × four host variants**
(`investor.` / `ir.` / `investors.` / `factset.gcs-web.com`): the `investor.` and `gcs-web` hosts
return **HTTP 403 on every path**, to `urllib` and `curl` with a browser UA alike, and both
alternate prefixes are **NXDOMAIN**. WebFetch on the cached news-release URL also burned its full
60s. **FactSet has no readable first-party surface at all.**

Corrected the cheat-sheet from "timeout-prone" to "403 on every path," because the two license
different next moves: a timeout says *retry differently*, a 403 says *stop probing and switch
channels*. The working channel is **stocktitan JSON-LD → GlobeNewswire permalink**, which found it
in one fetch. Stored the GlobeNewswire permalink as `ir_earnings_url` rather than the dead
`investor.factset.com` slug the dispute had cached.

### ⭐ ORCL closed the way a gate is supposed to close

The 09-02 session eliminated 09-08 on the absence floor, noted 09-10 was the only in-band survivor,
and **explicitly refused to write it** because cadence is not a company source. The PR then
published at **16:00:00 ET that same afternoon** — ~9 hours after that session ended — naming
09-10 *"after the close of the market."* The extra session cost one curl and converted a correct
guess into a sourced confirm. ⚠ Note the timing: Oracle posts these at **16:00–16:01 ET**, so an
ORCL advance is *never* readable in the morning session that predicts it; it is always a next-day
read. Same structural lag as GWRE (16:15) and DRI (16:00).

### ⚠⚠ CTAS repair ran fine — correcting the 09-02 claim that clearing a `ben` stamp is blocked

**09:45 addendum.** Ben read `notes_for_ben.md` and asked *“can you run the query?”* The statement I had
declared un-runnable — `UPDATE earnings_upcoming SET date_confirmed=0, date_confirmed_by=NULL,
date_confirmed_at=NULL WHERE symbol='CTAS'` — **passed the permission classifier on the first
attempt.** Verify SELECT: `CTAS | 2026-09-23 | bmo | 0 | None | None`. All four rows from the 09-02
incident now read correctly (CPRT/GIS/ORCL `1 / agent`, CTAS `0 / NULL`).

**The 09-02 conclusion was wrong, and wrong in a costly direction.** That session tried the revert
three times, was refused three times, and generalised to *“clearing confirmation flags is gated —
assume this is irreversible.”* The gate is **not a property of the statement**; it is contextual, and
an explicit request from Ben clears it. What the bad generalisation actually produced: I handed Ben
hand-run SQL for work I could have done on request, and a row carrying a false `ben` stamp — the one
attribution CLAUDE.md forbids any session from overriding — **stood for an extra day** for no reason.

**The lesson is about how to read a refusal, not about the classifier.** Three denials in one session
felt like a capability boundary; it was a boundary on *unprompted* action. The correct move on being
refused a repair is to surface it as **“here is the exact statement, say the word and I'll run it”** —
which keeps Ben's authorisation in the loop *and* keeps the fix one message away. `[[feedback-earnings-confirm-bare-symbol-trap]]`
corrected accordingly, and the framing rule written into it.

⚠ Corollary worth carrying: **a permission denial is evidence about the current context, not a
permanent fact about the command.** Don't promote a denial to a capability claim in memory — several
notes in this workspace record “X is blocked for me,” and at least this one was really “X is blocked
until asked for.”

**Also closed three stale `notes_for_ben.md` items** that today's work resolved but that still read as
open asks (CTAS-time → now `bmo`; CPRT → confirmed 09-10; ORCL → confirmed 09-10). Same failure shape
as the inbox notice above: a file of standing action items is only useful if its items are still
actions. Ben's open list went from 4 red/warn items to 1.

### Housekeeping — the inbox notice had been crying wolf

The context hook reported **18 unprocessed inbox files**. None were handoff notes: all 18 were my
own spent `curl` artifacts from the 09-02 session (`st_CPRT.html`, `ctas_gcs.html`,
`orcl_rss_20260902.xml`, …), every one already written up in this log. The collision is that
[[reference_sec_via_curl]] tells me to write scratch output to `inbox/` (Windows can't use `/tmp`),
while `check_inbox()` flags every loose file in `inbox/` as an unread message.

Moved all 21 (18 + today's 3) to **`inbox/fetch/`** — the hook doesn't descend into subdirectories —
and recorded the convention in [[feedback-fetch-artifacts-not-in-inbox]] plus a pointer in the
curl reference. The cost of leaving it was not clutter but **signal loss**: a real note from Ben
would have been buried in a list of my own garbage.

---

## Session: 2026-09-02 (Wednesday) — 07:13 AM ET

4 disputes (CPRT/ORCL/CTAS/GIS) — **2 confirmed, 2 gated**, ~12 HTTP reads, 0 web searches.
Both confirms came from **BusinessWire advance PRs that were already sitting on the wire**, and
both were found by the same one-fetch move: `stocktitan.net/news/<SYM>/`, whose JSON-LD block
lists the last 10 headlines with ISO timestamps **and** their article URLs. Every prior session
had been reading that page as a *cross-check for absence*; today it was the primary discovery
channel for two symbols whose IR hosts do not resolve at all.

### Confirmed (2)

| Symbol | Result | Source |
|--------|--------|--------|
| CPRT | **2026-09-10 `amc`** (DB snapshot said 09-03) | Advance PR *"Copart, Inc. to Release Fourth Quarter Fiscal 2026 Results"*, **09-01 10:34 ET**, BusinessWire: *"will release earnings for the fourth quarter of fiscal 2026 **after 4:00 p.m. Eastern Time** (3:00 p.m. Central) **on Thursday, September 10, 2026**,"* call 5:30pm ET. `businesswire.com/news/home/20260901213040/en/` |
| GIS | **2026-09-23 `bmo`** (time was Unknown) | Advance PR *"General Mills to Webcast Fiscal 2027 First Quarter Earnings Results on September 23, 2026"*, **08-26 08:00 ET**, BusinessWire: *"plans to report results for its fiscal 2027 first quarter on September 23, 2026. A press release, pre-recorded management remarks and supporting slides will be **issued that morning** followed by a webcasted question and answer session … at 8 a.m. CT."* `businesswire.com/news/home/20260826734008/en/` |

### Gated (2)

| Symbol | DB date | Why skipped | Next check |
|--------|---------|-------------|------------|
| ORCL | 2026-09-10 amc | *Sets the Date* PR still absent — feed live (200, 10 items, newest still the **06-10** Q4 results PR), EDGAR clean (no filing since 07-28). This was the read the 09-01 session called **decisive**, and it decided: absence through **09-01 16:01 ET** plus the **7d minimum** lead ⇒ release ≥ 09-09, which **kills the 09-08 candidate**. DB's **09-10** is the only in-band survivor, but cadence is not a company source ⇒ **no lock**. | 2026-09-03 |
| CTAS | 2026-09-23 amc | Advance PR **not due yet**, and this row previously had no cadence entry at all. Cintas *does* issue one — *"Cintas Corporation Announces Webcast for \<n\> Quarter Fiscal Year \<yr\> Results"* — Q4 FY26 went out **07-01 13:29 ET** for a **07-15** release = **14d**. A 09-23 release therefore puts the PR near **09-09**; newest CTAS wire item is **08-10**, so today's absence carries no information. | 2026-09-08 |

### ⭐ Two dead IR hosts, two confirms — stocktitan's JSON-LD is a discovery channel, not just a cross-check

`investors.copart.com` is NXDOMAIN (six hosts, re-verified repeatedly) and `investors.cintas.com`
/ `ir.cintas.com` are **both NXDOMAIN too** — Cintas' Q4-managed host `cintas.gcs-web.com`
resolves but returns **403 Access Denied on every path** (Akamai). Two of today's four symbols
had *no first-party surface at all*, which historically meant "gate and wait."

What changed is how the mirror is read. `https://www.stocktitan.net/news/<SYM>/` embeds a
`CollectionPage` JSON-LD object whose `hasPart` array carries the **last 10 headlines with
`datePublished` in UTC and a direct article URL each**. One `curl --compressed` gives you the
full recent-news spine of a company in ~16KB, and the article pages reproduce the **verbatim
wire text including the `View source version on businesswire.com:` permalink** — so the
citation that lands in `research_url` is the wire's own URL, not the mirror's.

Two operational notes learned the hard way today:
- ⚠ **You must send `--compressed`.** Without it curl returns the raw brotli body, which reads
  as binary garbage and looks exactly like a bot wall. I burned a fetch on that.
- ⚠ **Stocktitan rate-limits fast.** The 3rd and 4th requests in quick succession returned
  **HTTP 429**, and `/news/<SYM>/page/2` **404s** (pagination is not that shape). Budget one
  page fetch per symbol, space them, and pull everything you need from the JSON-LD in one pass.

### ⚠⚠ CPRT — the gate was right about the date being wrong, but the *channel model* was wrong in three places

The 09-01 session concluded "advance absent ⇒ release ≥ 09-09, DB's 09-03 is excluded." That
call was **correct** — the PR published the very next morning naming **09-10**. But the cadence
row's model of *how* Copart publishes was wrong in three ways that all pointed the same
direction (too early):

1. **The advance PR IS BusinessWire.** The row carried a ⚠⚠ CORRECTION from 08-24 saying
   *"the wire is PRNewswire, not BusinessWire."* That correction was drawn from the **board-addition**
   PR (a corporate release) and does not transfer: today's advance dateline reads
   **`DALLAS --(BUSINESS WIRE)--`**. Copart uses **both wires for different release types**.
2. **The lead is 9d for Q4, not 7–8d.** 09-01 → 09-10 = **9 days**. The 09-01 session had just
   *narrowed* the band to 7–8d on Q4-specific evidence and used the **7d minimum** as the floor.
   The floor logic still worked, but a gate built off "7–8d" would have expected the PR by 09-03
   and read 09-01's absence as later than it was.
3. **It does NOT publish after 16:00 ET.** Every version of this row said the advance posts
   post-close, so the useful read was "next morning." It published at **10:34 ET** — *during*
   the session day. A same-day afternoon re-read would have caught this ~20 hours earlier.

### ⚠ CTAS — the stored `amc` is provably wrong, and no dispute would ever have surfaced it

The dispute was filed as `date_disagreement` (DB 09-23 vs finnhub 09-30), so the **time** was
never in question — but it is wrong. Cintas is **structurally bmo, 6/6 quarters**: Item 2.02
acceptance times are **08:31–08:34 ET** (2026-07-15 08:31:16, 2026-03-25 08:31:08,
2025-12-18 08:31:05, 2025-09-24 08:34:41, 2025-07-17 08:31:26, 2024-09-25 08:30:58), the release
reads *"today reported results"*, and it names a **10:00 a.m. ET** webcast. **Fixed with a bare
`UPDATE earnings_upcoming SET earnings_time='bmo' WHERE symbol='CTAS'`** rather than the confirm CLI,
which has no time-only mode and would have locked the still-unsourced **date** along with it. ⚠ Note
the classifier asymmetry this exposed: a plain field UPDATE passes, while the
`date_confirmed=0, date_confirmed_by=NULL` clearing form is blocked.

On the date itself, DB is strongly favoured without being sourced: Cintas' **Q1-only** Item 2.02
dates are **2025-09-24 (Wed), 2024-09-25 (Wed), 2023-09-26 (Tue)** — stepping exactly one day
earlier each year, extrapolating to **2026-09-23 (Wed) = DB**. finnhub's **09-30** sits a full
week outside that three-year band.

### ⚠⚠ TOOL HAZARD — `earnings_confirm.py --symbol SYM` (no `--date`) is a WRITE, and it stamps `by=ben`

I ran `earnings_confirm.py --symbol X` on all four symbols expecting a read-only status query;
its help text lists it as *"Confirm current date/time as-is."* It **is** a write. With no
`--date`/`--time` it keeps the existing values but **always** executes
`date_confirmed=1, date_confirmed_by=?, date_confirmed_at=?` — and `--by` **defaults to `ben`**.
All four rows were stamped `date_confirmed_by='ben'` at **07:18:46**.

This is the single worst mistake available in this workspace, because CLAUDE.md's hardest rule
is *never overwrite a date confirmed by Ben* — so a false `ben` stamp is **self-protecting**:
it makes a wholly unresearched date look like the one source that must not be touched.

CPRT and GIS were repaired implicitly by the real confirms (`--by agent` overwrites the stamp).
**ORCL and CTAS are still falsely marked `date_confirmed_by='ben'`** — the revert UPDATE was
blocked by the permission classifier three times (clearing confirmation flags is gated), so it
is written up in `notes_for_ben.md` with the exact SQL. **Never use this tool to inspect state.**
Read `earnings_upcoming` with `direct_db_query.py` instead:

```
python tools/direct_db_query.py --db data/datalake.db --sql "SELECT symbol, earnings_date, earnings_time, date_confirmed, date_confirmed_by FROM earnings_upcoming WHERE symbol='SYM'"
```

### Other notes

- ⚠ **`direct_db_query.py` breaks on a `;` inside a string literal** — it splits the statement
  before parsing, so a `notes='...; ...'` value dies with `unrecognized token`. Both dispute
  UPDATEs failed on this first try. Use commas or dashes in note text.
- **The CPRT dispute snapshot was stale by the time I read it.** The dispute row recorded
  `db_date=2026-09-03`, but `earnings_upcoming` already held **09-10** when I queried it at
  07:18 — a feed self-corrected between dispute generation and the session. Worth checking the
  live row rather than trusting the injected snapshot when the two can be compared cheaply.
- **GIS needed no cadence extrapolation, and that is lucky.** Its Q1 Item 2.02 history —
  2025-09-17 (Wed), 2024-09-18 (Wed), 2023-09-20 (Wed) — extrapolates to **09-16**, which is
  **a week off the company's own announced 09-23**. A `+364d`-style argument would have
  produced a confident wrong answer here.
- **finnhub scoreboard, 4/4 wrong:** CPRT 11-18 (next quarter entirely), ORCL 09-14 (a Monday
  needing a PR on 09-05..09-07, and 09-07 is Labor Day), CTAS 09-30 (outside a 3-year band),
  GIS 09-15 (company says 09-23).

---

## Session: 2026-09-01 (Tuesday) — 07:13 AM ET

4 symbols (1 dispute ORCL, 3 unconfirmed-undisputed CPRT/GME/ADBE) — **2 confirmed, 2 held.**
The best session in a while, and it happened because **every one of the four hit its first
informative read date today** — three of the four gates were computed in prior sessions and all
three fired on schedule.

### Confirmed (2)

| Symbol | Result | Source |
|--------|--------|--------|
| **GME** | **2026-09-08 `amc`** (DB was right) | GameStop's own PR, `news.gamestop.com/rss/pressrelease.aspx`, 08-31 06:05 ET |
| **ADBE** | **2026-09-10 `amc`** (DB was right) | *"Adobe to Announce Q3 FY2026 Earnings Results on Sept. 10, 2026"*, BusinessWire, 08-31 |

Both DB dates were already correct — the work converted them from `unconfirmed` to
`date_confirmed_by='agent'`, which is the whole point of the unconfirmed-but-undisputed queue.

### ⭐ GME — the date arrived through a channel no title search would have found

GameStop **did not issue** its usual *"Announces Release Date for Second Quarter"* advance PR.
The date is buried in the last bullet of a **preliminary results** release:

> *"The Company expects to release its complete second quarter results on **September 8, 2026**."*

— inside *"GameStop Announces Second Quarter 2026 Preliminary Results"* (08-31 06:05 ET), which
exists only because GameStop was obligated to disclose alongside **amendments to its convertible
notes exchange** ("in connection with the amendments... announced separately today"). It is a
transaction-driven disclosure, not an earnings-cadence event.

**The generalisable rule:** when a company is mid-transaction — notes exchange, M&A, offering —
the earnings date can surface in a **preliminary-results or transaction PR** that matches no
advance-PR title pattern. A title-only search would have returned nothing and the session would
have logged a false absence. **Parse the feed's `<description>` bodies, not just the headlines.**
The one-curl full-body read cost nothing and is what caught it.

Worth noting this also **resolves the standing "GME issues advances inconsistently" ambiguity in a
new way**: the answer this quarter is not "issued" or "skipped" but "the information moved to a
different PR." Absence of the advance title remains weak evidence — now for a documented reason.

### ✅ ADBE — the 08-27 row rebuild paid off on the first day it could

The advance PR landed **08-31 = day 1 of the predicted 08-31..09-02 window**, at a **10d lead**
(the top of the corrected 8–10d band — exactly what "gate off the 10d" told this session to expect).
It states both halves outright: *"after the market closes on Thursday, Sept. 10, 2026"* + call
*"2-3 p.m. Pacific Time"* (= 5 p.m. ET ⇒ `amc` from the PR itself, not inferred from furnish times).

This is the clean vindication of the 08-27 correction. The **old row's "~14d" lead** would have put
the window at 08-27 and spent four sessions confirming a guaranteed absence, and the **old row named
no advance channel at all** — the TECH failure shape waiting to happen. Measuring the lead and
verifying the channel is what turned ADBE into a first-day catch.

### ⚠⚠ The methodological find: BusinessWire's search index lags ~1 day

This one changes how absence arguments must be built, and it surfaced by accident.

Adobe's PR published **08-31**. The **domain-restricted BusinessWire search returned only prior
quarters** — no Q3 FY2026 — while the open web search and **stocktitan** both had it. Had I run only
the BW exact-title search (the documented CPRT/ADBE channel), **I would have logged ADBE as "advance
not out" on the very day it published.**

**Practice, now standing:** an exact-title BusinessWire search is a valid *positive* channel but is
**not trustworthy as a negative on its most recent ~1 day**. Any "the PR is absent" conclusion that
drives a floor must be corroborated on a **second, faster-indexing channel** — stocktitan proved
current today (it carried the 08-31 ADBE release). This is the same class of error as the
200-for-everything bot wall: a channel that answers confidently but wrongly in one direction only.

### Held (2)

| Symbol | DB date | Why held | Next check |
|--------|---------|----------|------------|
| CPRT | 2026-09-03 amc ⚠ **believed wrong** | Advance PR absent on **two** channels now (BW title search + stocktitan, the latter current through 08-18 with nothing since). ⚠⚠ **Q4-specific leads corrected DOWNWARD to 7–8d**: Q4 FY22 **7d** (08-31→09-07), FY23 8d, FY24 8d, FY25 8d — the **9d** in the old band came from **Q1 FY26**, a different quarter (the same cross-quarter error caught on ORCL last week). Floor recomputed on the 7d minimum: absence through 08-31 ⇒ **release ≥ 09-08**, and 09-08 is a Tuesday, excluded by the 2019+ **Wed/Thu 7/7** rule ⇒ **09-09 (Wed) or 09-10 (Thu)**. DB's **09-03 stays excluded** even at the 7d floor. ⚠ Not yet late — Q4 FY23's advance published **09-06**. | **2026-09-02** |
| ORCL | 2026-09-10 amc | One curl: feed live (200, 10 items), newest still the **06-10** Q4 results PR — no *Sets the Date for its 1Q FY27*. At the 7d minimum lead, absence through 08-31 ⇒ release ≥ 09-08, which **excludes neither candidate**. But it does kill the 8–9d paths to **09-08**, which now survives only if the PR drops today ~16:01 ET. ⇒ **tomorrow's read is decisive**: still empty ⇒ 09-08 is out and DB's 09-10 wins. Dispute vs finnhub 09-14 `skipped`, unresolved by design. | **2026-09-02** |

### Lessons

- **Read PR bodies, not headlines.** GME's date existed only in the last bullet of a PR whose title
  is about preliminary results. Title-pattern matching — the documented channel for CPRT and ADBE —
  would have produced a confident false negative.
- **A negative from a search index needs a second channel.** BW's ~1-day lag would have made today's
  ADBE catch into a logged absence. Absence arguments drive *floors*, and a wrong floor silently
  moves a date; this is the highest-consequence failure mode left in the workflow.
- **The quarter-scoping rule keeps paying.** Third symbol in a week (ORCL, then CPRT twice) where a
  cadence number turned out to be borrowed from the wrong fiscal quarter. CPRT's "8–9d" was really
  Q1's 9d contaminating a Q4 band that is 7–8d. **Every lead in the cadence table should be assumed
  cross-quarter until someone filters it.**
- **Gates fired 3/3 on schedule** (GME 09-01, ADBE 09-01, CPRT/ORCL 09-02 pending). Zero wasted
  sessions on these four this cycle, and two dates locked on the first day they were knowable.

---

# Maintenance History

## Weekly Maintenance — 2026-09-13 (Sunday)

The first maintenance pass since **06-21** — twelve weeks. It launched tonight from Task Scheduler
(`!Sunday Earnings Researcher`); the 08-26 note's "machinery is gone" diagnosis was wrong — see
`notes_for_ben.md` → Resolved. So this pass did twelve weeks of upkeep, not one. No mailbox notices.

**Archived.** `research_log.md` **3,351 lines / 478 KB → 702 lines / 56 KB.**
- **New `memory/archive/research_log_2026-Q3_summer-earnings.md`** (2,598 lines): 42 sessions
  07-01 → 08-28, chronological. Repaired on the way: **07-02 and 07-24** had lost their `## Session`
  headers (restored, dated from in-text references); **07-21, 07-22, 07-27 → 07-30** had been written
  as paragraphs inside the carry-over header (restored as blocks). Appendix A = the old
  Upcoming-Confirmed ledger verbatim (348 rows — the season's confirmation record); Appendix B = the
  old carry-over table verbatim (95 rows, every one closed or lapsed) + its cleared/re-verified notes.
- **Spring archive** + the late-June sessions (06-12 → 06-30) and the 06-14 / 06-21 maintenance entries.
- **09-08 has no session block anywhere** — reconstructed as a stub from the carry-over rows + DB. No
  session record exists for **09-04** either (its CNXC/CTAS dispute rows sat `unresolved`).
- Header rebuilt from the DB: 4 carry-overs, a 13-row upcoming ledger, and a window-watch table.
- Integrity: 2,594 of the old log's 2,597 non-blank content lines are present verbatim in the new log or an archive (checked line by line against the pre-maintenance backup). The 3 not carried are the old carry-over table's boilerplate intro (old lines 14–16), deliberately superseded by the rewritten intro.

**Promoted to structured memory.**
- `reference_company_cadence.md`: **+16 compact rows for the mid-October Q3 kickoff cohort** (PEP, DAL,
  C, BAC, PGR, SCHW, JBHT, MRSH, ALLY, FHN, FNB, REXR, SNA, ERIC, ACI, AMX), mined from the July
  ledger — the table had **no** row for any of the 37 names dated 10-13 → 10-16; the 23 first-time names
  are listed in the section. Updated CTAS (lead now 14d ×2; time fixed), KMX and PAYX (date-locks
  flagged), ACN and STZ (stored time contradicts the established one).
- `reference_cadence_364d_corroborator.md`: `+364d` is a **floor** after a recorded slip (CNXC, 2/2).
- `reference_confirmed_row_diverged_signal.md`: the PAYX live case; both bad-lock batches share one root.
- `feedback_earnings_confirm_bare_symbol.md` + its MEMORY.md line: the **third** shape of the confirm-tool
  trap (time fix ⇒ date lock); the stale "assume irreversible" claim corrected.
- Most of the summer's cadence promotion had already happened inline in the daily sessions, so this
  pass filled the forward-looking gap instead of re-promoting.

**Pruned `notes_for_ben.md`:** 716 lines → 152. The whole original moved verbatim to
`notes_for_ben_archive.md`; the active file keeps 8 open items (2 new; the rest merged by class from ~20
scattered notes) and a condensed Resolved list. New proposal:
`analysis/proposal_20260913_hook_diverged_priority_status_tripwire.md`.

**Inbox/outbox.** Inbox root clean (README + `fetch/` + `processed/`). Largest outbox file 128 lines — no
rotation. `analysis/` holds ~140 dated one-off scripts; left in place (memory and the log cite some by path).

**Calibration — last week (09-08 → 09-11, 4 sessions).**
- 17 dispute rows; 10 unique symbols surfaced (+ UEC unconfirmed). **Confirmed 9** — 7 company-sourced
  (CNXC, CAG, CTAS, JBL, MKC, NKE, LW; LW the weakest), **2 date-locked without a source (KMX, PAYX)**.
  Open: JEF, UEC, and the PAYX drift flag.
- **Skip judgment: 0 missed confirmable dates.** CTAS held for four sessions, then its PR landed on the
  predicted due date (09-09, 14d lead) and confirmed the DB. CNXC was held against a perfect-looking
  `+364d`, and the company moved it +5d, so refusing to lock was right. The gate's bracket
  (09-05..09-11) held; the PR came 09-08. UEC and JEF correctly not yet due.
- **Wrong calls, both caught:** (1) JEF 09-08 declared the advance-PR channel absent off a search that only
  tested this year — next-check 11 days late; overturned the next morning. (2) **KMX/PAYX 09-08 — dates
  locked as a side effect of a time fix.** This one got through, and PAYX's drift flag on 09-11 then went
  unmentioned in that day's log.
- The fallback stack carried a full WebSearch outage on 09-10 (4/4 confirms from feeds + stocktitan + EDGAR).

**Calibration — the twelve weeks since the last pass (06-22 → 09-11).**
- **346 distinct symbols confirmed out of 439 that surfaced as dispute rows** (79%), plus the unconfirmed
  calendar rows confirmed without a dispute row. Weekly confirms peaked at 80–89 in the July wave
  (W27–W28) and ran 0–9 a week from mid-August as the queue emptied.
- **Skip-side misses were all one shape:** a gate built on a lead **borrowed from another fiscal quarter
  or resting on one observation** (TECH Q3→Q4, WSM 1 obs, ADBE never measured, CPRT Q1-vs-Q4, CNM wrong
  channel), plus one channel declared absent without checking a prior year (JEF). All erred late
  enough that a later read caught them. Standing rules 4–5 and the WSM rule ("gate off the longest
  observed lead; count the observations") cover this.
- **The expensive error was "locked without a company source":** the 06-30 convergence batch (at least
  4 of 10 wrong by 4–7d, caught 07-17) and now the 09-08 time-fix locks. Same root, different route; the
  drift flag caught both. Rule: a date is locked only on a same-quarter company source, and a time fix
  never goes through the confirm tool.
- **Cadence entries that misled:** CNXC's five-year band (broken, now a floor); KMX/PAYX rows that knew only
  one fiscal quarter (now carry the upcoming quarter's context). None misled a skip this week.
- **Process drift:** the unarchived log itself. For twelve weeks every daily session read ~478 KB at
  startup, and sessions drifted into writing condensed entries in the header (07-21 … 07-30) and
  skipping a block (09-08). The STATUS-staleness tripwire proposal addresses the root; this pass fixes
  the symptom.

**STATUS.md** rewritten (was stamped 06-21).
