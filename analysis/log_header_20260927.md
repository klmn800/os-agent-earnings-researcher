# Earnings Research Log

> Active log: full sessions for the last ~2 weeks (newest first, below), a compact ledger of
> confirmed-but-upcoming dates, and the open carry-overs with next-check dates. Older sessions live in
> the season archives: `memory/archive/research_log_2026-Q2_spring-earnings.md` (through 06-30) and
> `memory/archive/research_log_2026-Q3_summer-earnings.md` (07-01 → 09-11, plus the summer's full
> confirmation ledger and carry-over table as appendices). Maintenance notes at the very bottom.
> Per-symbol cadence/lead-times live in `memory/reference_company_cadence.md` — **grep it by symbol
> (`^| SYM `); don't read it whole (~190 KB).**

## Open Carry-Overs — unresolved, with next-check dates

Symbols held because no company-issued source exists *yet*, plus rows whose stored date is doubted.
Next-check ≈ **advance-PR due date + 1** (most advance PRs publish after the ~07:15 session starts —
see the standing rules in `reference_company_cadence.md`). Rebuilt from the DB on 2026-09-27.
**Each row's "How to read" column is the working channel and its known traps. Use it verbatim; don't
rediscover it.** (On 09-25 two reads went wrong because the fix lived only in an older session note.)

| Symbol | DB row | Status | How to read | Next check |
|--------|--------|--------|-------------|------------|
| **REXR** | 10-14 `amc` (time set 09-23; date unlocked, **probably wrong**) | No Q3 advance as of the last *good* read (09-24: list current to the 09-17 portfolio-sale PR). Leads 24–35d (3 obs) ⇒ a 10-14 release's PR was due by 09-20: overdue. 2026 quarters are 4th-Thursday amc (04-23, 07-23) → **10-22** expected, PR due 09-17 → 09-28. ⚠ The 09-25 read reported the list "ends 03-19". That contradicts 09-24, so it was a bad view, **not an absence**. | WebFetch `ir.rexfordindustrial.com/news-events/press-releases`. **First check that the newest item is ≥ 09-17**; if it isn't, the view is stale, so try the stocktitan spine `stocktitan.net/news/REXR/` (`--compressed`). PR publishes ~16:05 ET, so a morning read sees prior-day PRs. Title: *"Announces Dates for Third Quarter 2026 Earnings Release…"* | **09-28**, then 09-29. No PR by 09-29 ⇒ 10-22 is also doubtful; widen to the spine + EDGAR |
| **AMX** | 10-13 `amc` (finnhub 10-20) | No 3Q26 event as of 09-24 (the 09-25 read saw only 2014–2018 events, which is the feed quirk below, **not an absence**). Q3 is Tuesday amc every year (10-17 / 10-15 / 10-14); 10-13 fits the trend, 10-20 is the +7d artifact shape. | curl the Event.svc feed with a browser UA, **`pageSize=100`** (the cached URL still says `pageSize=25` and `sortDirection` is ignored, so a verbatim read returns 2014 first). Page with `pageNumber` until empty, dedupe by `EventId`, sort by `StartDate` in Python, open as utf-8. **Monday: re-cache the URL with `pageSize=100`.** | **09-29**, then 10-06 |
| **ACI** | 10-13 `bmo` (time via `--time-only` 09-22; date unlocked) | FQ2 ends 09-12; the last two FQ2s reported 38d after quarter-end ⇒ **10-20**. 10-13 would be the shortest FQ2 on record. Advance PR (BusinessWire, 14d lead) due ~09-29 for 10-13 / ~10-06 for 10-20. | stocktitan spine `ACI` (BW deep links 403). Title: *"Albertsons Companies Announces Second Quarter Fiscal 2026 Earnings Release and Conference Call Date."* | **09-30**, then 10-07 |
| **FNB** | 10-15 `amc` (time via `--time-only` 09-24; date unlocked) | Q2's scheduling PR came 06-30 15:30 ET for 07-16 (16d, 1 obs) ⇒ Q3's due ~09-29 for 10-15. 3rd-Thursday amc fits. | stocktitan spine `FNB` or `fnb-online.com` newsroom (cached). Title: *"F.N.B. Corporation Schedules Third Quarter 2026 Earnings Report and Conference Call."* | **09-30**, then 10-01 |
| **SNA** | 10-15 `bmo` (time via `--time-only` 09-24; date unlocked, **probably 7d early**) | 53-week fiscal 2025 shifted every 2026 quarter a week later; Q3 ends 10-03, +19d ⇒ **Thu 10-22**. Dispute row left `unresolved` on purpose. | stocktitan spine `SNA`. Title: *"Snap-on Incorporated to Webcast 2026 Third Quarter Results Conference Call"* (BusinessWire, 14d lead). Due **10-01** if 10-15, **10-08** if 10-22. `investors.snapon.com` is NXDOMAIN. | **10-02** (silent ⇒ 10-15 is dead), then 10-09 |
| **WIT** | 10-15 `bmo` (finnhub 10-13) | Q2 has been a Thursday since 2024 (10-17, 10-16) ⇒ **10-15** fits; finnhub's Tuesday doesn't. Advance ~9d lead (1 obs) ⇒ due ~10-06. | wipro.com/newsroom list is JS-only; search the title *"Wipro Limited to announce results for the second quarter ended September 30, 2026"* or read the BusinessWire copy via stocktitan `WIT`. **No IR URL cached**: cache the PR page when found. | **10-06**, then 10-07 |

### Window watch — unconfirmed rows the horizon will surface soon

Not carry-overs (never researched this quarter). **Monday 09-28 caveat:** no unconfirmed row falls in the
14-day horizon until **09-29** (every row ≤ 10-12 is confirmed), so Monday's session spawns only if a
dispute flags. AMX/REXR/WIT have flagged every day 09-22 → 09-25, so it probably will. From 09-29 the cohort
below guarantees a spawn every day.

| Enters horizon | Unconfirmed rows (DB 09-27) | Note |
|----------------|-----------------------------|------|
| 09-29 | **10-13:** DPZ, JNJ, JPM, UNH, WFC | Measured cohort leads ~23–35d ⇒ these PRs are **almost certainly already out**. Spine-read them the first session that runs; don't wait for the horizon (MTN 09-14 and PEP 09-24 lessons). |
| 09-30 | **10-14:** ABT, ASML, BAC, FAST, MS, STT | same |
| 10-01 | **10-15:** AA, BK, MAN, MRSH, PLD, PNC, SCHW, TSM, USB | same |
| 10-02 → 10-03 | **10-16:** CFG, MTB, TRV · **10-17:** HDB, IBN | HDB/IBN are Saturday-dated Indian ADRs: check the D−1 amc / D bmo encoding (open policy question 2 in `notes_for_ben.md`) |

25 rows over four days, on top of the carry-overs. The 10-19 → 10-22 wave (~90 rows) follows directly
behind. Front-load: the more of the 10-13/10-14 names a session clears early, the lighter 09-29 → 10-02 get.

## Upcoming Confirmed — locked dates (don't re-research)

One line per confirmed symbol whose date is still ahead (≥ 09-28), re-verified row by row against
`earnings_upcoming` on 2026-09-27: 25 rows, all `1 / agent`, every date and time matching the DB.
Pruned today as reported: CTAS, GIS, PAYX (09-23), DRI (09-24). Sorted by date. Format:
`SYM | date | time | source — session`. Prune reported rows each Sunday; the summer's full ledger is the
summer archive's Appendix A.

| Symbol | Date | Time | Source — session |
|--------|------|------|------------------|
| MTN | 2026-09-28 | amc | Vail PRNewswire 09-04 16:05 ET (via stocktitan): *"after market close on Monday, September 28, 2026,"* call 5pm ET — 09-14 |
| JEF | 2026-09-28 | amc | Jefferies advance 09-14 16:30 ET (`ir.jefferies.com` feed + news-details page): *"Monday, September 28, 2026 after market close."* Dispute resolved — finnhub 09-30 wrong — 09-15 |
| KMX | 2026-09-29 | bmo | CarMax BusinessWire 09-09 17:00 ET (via stocktitan): *"before the market opens on September 29, 2026,"* call 8am ET. Re-sourced 09-14 (09-08 lock was unsourced) — 09-14 |
| CNXC | 2026-09-29 | amc | GlobeNewswire 09-08 *"Concentrix Schedules Release of Third Quarter 2026 Financial Results…"*: after close, call 5pm ET — 09-09 |
| UEC | 2026-09-29 | bmo | UEC advance 09-22 07:00 ET (via stocktitan) + `uraniumenergy.com/invest/events-and-webcasts` (webcast 8am PDT): *"before the markets open on Tuesday, September 29, 2026"*. **Corrected from 09-24 amc** — 09-22 |
| CCL | 2026-09-29 | bmo | Carnival PR Newswire 09-15 11:56 ET (via stocktitan): call 10am EDT, results *"released that morning"* — 09-22 |
| CAG | 2026-09-30 | bmo | Conagra PRNewswire 08-31; bmo **inferred** (materials "that morning" ahead of a 9:30am ET Q&A) — 09-09 |
| FDS | 2026-09-30 | bmo | FactSet GlobeNewswire 09-02 11:00 ET; presentation 8:30am, call 9:00am ET — 09-03 |
| JBL | 2026-09-30 | bmo | Jabil feed 09-09 16:10 ET: *"before the market opens,"* call 8:30am ET — 09-10 |
| MU | 2026-09-30 | amc | Micron IR PR 08-26: call 2:30pm MT = 4:30pm ET — 09-22 |
| ACN | 2026-10-01 | bmo | Accenture newsroom 09-15: call 8:00am EDT, *"release will be issued before the call"*. **Time corrected from amc** — 09-22 |
| MKC | 2026-10-01 | bmo | McCormick PRNewswire 08-31 08:00 ET (via stocktitan; IR host 403s); call 8am ET — 09-10 |
| NKE | 2026-10-01 | amc | Nike feed 08-28: *"approximately 1:15 p.m. PT, following the close"* — 09-10 |
| LW | 2026-10-06 | bmo | Lamb Weston scheduling release (~8:00am ET release, 9am call). ⚠ Weakest confirm on the list: no first-party fetch succeeded (IR 403 wall, no 8-K); rests on consistent search summaries + yfinance — 09-09 |
| STZ | 2026-10-06 | amc | Constellation `ir.cbrands.com` detail/345, 09-10: *"after the close of the U.S. markets,"* call 10-07 8am ET. **Time corrected from bmo** — 09-22 |
| PEP | 2026-10-08 | bmo | pepsico.com newsroom PR 08-25 *"PepsiCo Announces Timing and Availability of Third-Quarter 2026 Financial Results"*: *"Thursday, October 8, 2026,"* materials ~6:00am EDT, Q&A 8:15am EDT — 09-24 |
| DAL | 2026-10-09 | bmo | Delta webcast PR: call 10am ET Oct 9. bmo **inferred** (release time not stated); lead unmeasured (PR date not captured) — 09-25 |
| C | 2026-10-13 | bmo | Citi 2025 calendar PR (citigroup.com): *"3Q26 – Tuesday, October 13, 2026,"* release ~8am ET, webcast ~11am ET — 09-22 |
| PGR | 2026-10-14 | bmo | Progressive August results release (8-K 7.01, 09-18): *"We plan to release September results on Wednesday, October 14, 2026, before the market opens"* — 09-23 |
| ERIC | 2026-10-15 | bmo | `ericsson.com/en/investors/financial-calendar/2026/q3-2026`: *"Oct 15, 2026 07:00 (CET)"* = 01:00 ET ⇒ bmo — 09-24 |
| FHN | 2026-10-15 | bmo | `ir.firsthorizon.com` PR 09-22: materials ~6:30am ET, call 9:30am ET. Snapshot 10-14 was already stale — 09-23 |
| JBHT | 2026-10-15 | amc | `investor.jbhunt.com` "Estimated Earnings Periods" table: Q3 release **October 15, 2026**, quiet period Sep 26 – Oct 15; amc = Item 2.02 furnished 20:08–21:26Z (16:0x–16:2x ET) 8/8 since 2024-10 — 09-24 |
| RF | 2026-10-16 | bmo | ir.regions.com 2026 release-dates PR: *"pre-market open on Friday, Oct. 16, 2026,"* call 10am ET — 09-25 |
| TFC | 2026-10-16 | bmo | media.truist.com 09-18: *"before the market opens on Friday, Oct. 16, 2026,"* call 8am ET — 09-25 |
| SYF | 2026-10-20 | bmo | `investors.synchrony.com` detail/588: release ~6:00am ET, call 8:00am ET. Snapshot 10-14 was already stale — 09-23 |
