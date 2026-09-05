---
name: ma-phantom-earnings-dates
description: A dispute can be unresolvable because the earnings EVENT doesn't exist — delisted tickers and pending-take-private companies that stopped issuing releases; two cheap SEC tells catch both
metadata:
  type: reference
---

Every technique in this workspace assumes the question is *"which date is right?"*. Sometimes there is no right answer, because the company has no earnings event to schedule — while both feeds still carry confident dates. Check for this **before** spending research on a symbol, and never write a date for one.

**This note exists to turn a recurring per-symbol diagnosis into a bulk screen.** AES, APLS and IAC were each worked out individually on 07-27 and escalated in `notes_for_ben.md`; they then re-appeared on 07-28 and again on **07-29**, consuming 3 of 32 slots (9%) for a third straight session. The diagnoses were right — the problem is that nothing *screens* for the class, so each session re-derives them one at a time. Both tells below fall out of the SEC sweep already run for [[sec-8k-acceptance-time-as-timing-source]], so screening the whole dispute list costs nothing extra.

## The two tells, both free

Both come out of `https://data.sec.gov/submissions/CIK<10>.json`, which you already fetch for [[sec-8k-acceptance-time-as-timing-source]].

1. **`tickers` is `[]`** in the submissions JSON, and/or the symbol is **absent from `company_tickers.json`** ⇒ **delisted**. This is what exposed **APLS**: Biogen's tender offer closed **2026-05-14**, Nasdaq halted trading, Form 25 filed — APLS had **not traded for 10 weeks**, yet DB carried 07-30 and finnhub 07-29. (Note `company_tickers.json` is the same file you use for CIK lookup, so a `NO_CIK` result in a sweep is *itself* the signal — don't dismiss it as a mapping gap.)
2. **A gap in Item 2.02 8-Ks while 10-K/10-Q filings continue** ⇒ the company **still reports, but has stopped holding earnings events**. This is the subtle one, and no ticker check finds it. **AES** was still listed and its take-private had *not* closed (GIP/EQT, holder-approved 06-26) — but it had filed **no Item 2.02 since 2025-11-04**, and both the 10-K (2026-03-02) and Q1 10-Q (2026-05-05) went out with **no release and no call**. Two consecutive quarters of results-without-an-event ⇒ no Q2 event either. DB said it reported *the next day*.

**Rule: ≥2 consecutive quarters where a periodic report was filed but no Item 2.02 accompanied it ⇒ treat as no-event and skip.** One quarter is not enough (a company can file the 8-K late or under different items).

## ⚠ 2026-08-03 — the screen works, but the *handling* has a hole

Running the two tells across all 25 symbols cost nothing and re-caught **AES** immediately, with the evidence now stronger: still no Item 2.02 since **2025-11-04**, and **three** consecutive periodic reports filed with no event (10-K 2026-03-02, Q1 10-Q 2026-05-05, and the Q2 report now due). `tickers=['AES']`, take-private still not closed. The diagnosis is settled; **stop re-deriving it**.

**The hole: AES arrived as an *unconfirmed calendar row*, not a dispute row.** There is no `earnings_date_disputes` row for it, so the documented handling — resolve `skipped` with the reasoning in `research_url` — **has nothing to write to**. `earnings_confirm.py` is the only writable path for that class, and using it would stamp a date on a no-event symbol, which is the one thing this note forbids. So the correct action is **write nothing at all and escalate**, which means the finding survives only in the log and `notes_for_ben.md` and the row will resurface every session.

Worse, this time **the phantom date was *today*** (DB 2026-08-03), i.e. the scanner believed AES reported that session. The unconfirmed-row class is where a phantom is most dangerous and least catchable.

**Rule: run the screen against the whole injected list, disputes *and* unconfirmed rows.** A symbol moving from the dispute table to the unconfirmed table is not a resolution — it just removes the only field you could have recorded the finding in.

## 2026-08-04 — EA: the screen catches a phantom the *day of*, and tell #2 needs one refinement

Second phantom in three sessions, same shape as AES, same handling hole: **an unconfirmed calendar row dated the session it surfaced.** **EA (Electronic Arts)** filed its **Q1 FY27 10-Q on 2026-08-03 at 20:08 ET with no Item 2.02, no press release and no call** — results went straight into the 10-Q the prior evening. The 07-30 8-K (item 8.01) confirms the cause: *"as of July 30, 2026, all regulatory approvals required to complete the Merger have been obtained"* — the $55B PIF/Silver Lake/Affinity take-private is cleared to close. EA had **already** dropped its Q3 FY26 call. DB said `2026-08-04 amc`. Wrote nothing; escalated.

**⚠ Refinement to the ≥2-quarter rule — do not apply the ±4d window mechanically.** The raw screen flagged EA's **10-K of 2026-05-11** as eventless, which is *wrong*: EA's Q4 FY26 Item 2.02 was filed **2026-05-05**, six days earlier — outside the ±4d window but plainly the same event. Widen the window to **±10 days for 10-K/20-F** (annual reports routinely trail the release by a week or more) or the screen manufactures false positives on exactly the healthy filers. EA's *real* signal was the **Q1 FY27 10-Q with no 2.02 at any distance**, plus the two corroborators below.

**The two corroborators that turned one eventless quarter into a confident call** — worth reaching for, because the ≥2-quarter rule alone would have said "wait another quarter" while the phantom date was *today*:

1. **The IR feed carries no earnings PR of any kind.** EA's feed is current and full of game announcements — a live feed with zero earnings items is very different from a stale one.
2. **A prior quarter where the company demonstrably skipped the *call* while still issuing a release.** EA had no Q3 FY26 call. That is the intermediate step between "normal" and "silent," and it makes the next quarter's total silence a continuation rather than an anomaly.

**Rule: one eventless periodic report + a current-but-earnings-empty IR feed + a documented dropped call ⇒ phantom, without waiting for the second quarter.** The ≥2-quarter rule stays the default when those corroborators are absent.

## 2026-08-07 — MKTX: a third shape, where the event *moved earlier* instead of vanishing

Both cases above are absences. **MKTX is the opposite failure: the event happened, six weekdays before the date everyone had.**

MarketAxess's own advance PR (07-15) scheduled Q2 for *"Friday, August 7, 2026, before the market opens"*, call 10:00am ET — a clean, company-issued, correctly-read source, and DB matched it. Then on **2026-07-30 at 07:44 ET** MKTX filed an 8-K (items 1.01/5.02/7.01) announcing that **Intercontinental Exchange will acquire the company**, and **six minutes later, at 07:50 ET, filed the Item 2.02 with Q2 results**. Nothing has been filed since. On 08-07 the DB row pointed at an event that was already eight days in the past.

**The lesson is about the durability of a source, not its quality.** An advance scheduling PR is a statement of intent with a multi-week shelf life, and **it is never retracted** — no "we moved it up" release is ever issued, because the results PR itself is the correction. So a company source can be simultaneously authentic, correctly read, and stale. Neither tell above catches this: `tickers` is populated and Item 2.02s are flowing normally.

**Screen: for any symbol whose DB date is more than a few days out, check whether an Item 2.02 has *already* been furnished since the advance PR was published.** It costs nothing — the sweep for [[sec-8k-acceptance-time-as-timing-source]] already returns the full 2.02 history, and a 2.02 dated *after* the scheduling PR but *before* the scheduled date is unambiguous. Weight it highest for symbols inside an M&A story: pairing the deal announcement with results the same morning is a standard move, and it is precisely the moment the calendar breaks.

**Handling is the same as the absence cases and hits the same hole**: MKTX arrived as an *unconfirmed calendar row* with no dispute row to write to. Confirming 08-07 would lock a date with no event behind it; confirming 07-30 would put a past date in an upcoming-earnings table. **Write nothing, escalate.**

## Why this matters more than a wrong date

A wrong date costs a bad window. A **phantom** date invites trading an event that will never happen — the position gets held through a volatility crush that never arrives. AES was the live case: DB had it reporting the next morning.

## Handling

**Resolve `skipped`, never `confirmed_agent`, and put the reasoning in `research_url`** — that field is free text and is the only place the finding survives. Do **not** write a date, even when you know the "would-be" one. ⚠ `direct_db_query.py` **splits SQL on `;`** — a semicolon inside the note text truncates the statement and throws `unrecognized token`. Use periods.

## The neighboring case: renamed tickers

Same session, **IAC → People Incorporated, ticker `PPLI`, effective market open 2026-06-04** (CIK 1800227) — caught because **`ir.iac.com` 301-redirects to `ir.people-incorporated.com`**. Here the *date* was fine (08-03 amc, `+364d`-exact) but the **row needs renaming, not confirming**; stamping a date on a dead symbol hides the real defect. Third instance of this pattern — see [[P ticker = Pure Storage rebranded as Everpure]] and the FISV→FI note in the log. **A 301 to an unfamiliar host is a rename signal, not a URL-maintenance chore.**

## Where M&A shows up as a soft warning

An acquisition agreement alone does **not** kill the next earnings call — it's a flag to re-verify, not to skip. Live examples to watch: **TECH** (Merck KGaA, agreed 06-04) and **AMCR**. AES is the proof that the release can quietly stop *before* the deal closes, so re-check M&A names each quarter instead of trusting last quarter's cadence.

**⚠ 2026-08-04: "all regulatory approvals obtained" is the sharpest available warning.** EA's 07-30 8-K said exactly that, and its very next periodic report went out with no event. When an 8-K item 8.01 announces regulatory clearance, treat the *next* quarter's date as suspect by default — that is the point at which a company stops behaving like a going concern with public shareholders to brief. **TECH is the live test of this**: its advance PR is ~21d overdue with the Merck KGaA merger active, and as of 08-04 its DB date is the next day with no call announced. If TECH's Q4 lands inside the 10-K with no call, that is three-for-three on this pattern.

Related: [[sec-8k-acceptance-time-as-timing-source]], [[cadence-364d-weekday-aligned-corroborator]] (both silently return confident answers for a company that has stopped reporting), [[company-earnings-cadence]], [[window-gating-and-noop-sessions]], [[feedback_direct_db_query]].
