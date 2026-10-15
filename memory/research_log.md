# Earnings Research Log

> Active log: full sessions for the last ~2 weeks (newest first, below), a compact ledger of
> confirmed-but-upcoming dates, and the open carry-overs with next-check dates. Older sessions live in
> the season archives: `memory/archive/research_log_2026-Q2_spring-earnings.md` (through 06-30) and
> `memory/archive/research_log_2026-Q3_summer-earnings.md` (07-01 → 09-25, **closed**: every calendar-Q3
> session is there, plus the summer's ledger and carry-over table as appendices). Fall sessions
> (from 10-01) will roll into `research_log_2026-Q4_fall-earnings.md`. Maintenance notes at the very bottom.
> Per-symbol cadence/lead-times live in `memory/reference_company_cadence.md`. **Grep it by symbol
> (`^| SYM `); don't read it whole (~220 KB).**

## Still unconfirmed (rebuilt 2026-10-15 after the session)

Kept as a checklist so nothing falls off between sessions (the hook injects one date-sorted queue,
ceiling 40). 15 rows closed 10-15; what's left is waiting on a company PR or Ben's policy call. **Nearest date first.**

| Reports | Unconfirmed (`?` = time Unknown) | Notes |
|---------|-----------------------------------|-------|
| 10-17 | HDB, IBN | Saturday-dated Indian ADRs. Held for Ben's policy Q2 (`notes_for_ben.md`). HDB board meeting is Sat 10-17 per the 09-22 exchange filing (secondary coverage); IBN: no notice found |
| 10-20 | AMX, ISRG, OMC | |
| 10-21 | RHI | |
| 10-22 | DOW, IRDM?, SCCO? | |
| 10-23 | INFY, ITW | INFY: 10-23 per news coverage of the board filing (not primary); **time likely bmo** (results ~3:45pm IST = 06:15 ET), DB says amc. ITW: aggregator says 10-27 (unsourced) |
| 10-26 | ARE?, BMRN | |
| 10-27/29 | EXEL, EBAY?, GILD, WHR, DTE, OSK, DVA, NVT?, XOM?, MKTX, MAT, MDLZ | MKTX/MAT/MDLZ newly in the queue; no PR yet |

## Open Carry-Overs: researched, unresolved, with next-check dates

Next-check ≈ **advance-PR due date + 1** (PRs mostly publish after the ~07:15 session start). **Each
row's "How to read" is the working channel and its known traps. Use it verbatim.**
Spine = `analysis/helpers/spine.py` (paces itself to stocktitan's 10-per-300s limit since 10-09; run big lists with `run_in_background`). Its output lists only date-keyword headlines, so no lines = no new PR. **Don't attach a Monitor to it: each event re-injects the whole dispute list.** Read the output file once at the end; a stocktitan article page via WebFetch gives the PR text.

| Symbol | DB row | Status | How to read | Next check |
|--------|--------|--------|-------------|------------|
| **AMX** | **10-20** `amc` | Feed re-read 10-15: still no 3Q26 event (newest 2Q26 07-22; the 3Q25 event was dated 10-15-2025 for 10-14 amc). Q3 is always a Tuesday amc; 10-20 is a Tuesday too. **Log the first day the event appears** | Event.svc feed, browser UA, `pageSize=100`. Page with `pageNumber`, dedupe by `EventId`, parse `StartDate` with strptime (string-sorting `MM/DD/YYYY` is garbage), open as utf-8 | 10-16, daily |
| ISRG, OMC | 10-20 | Spine 10-15: nothing (ISRG last 09-08, OMC 09-09). ISRG IR 403s WebFetch. **No PR 5 days out is suspect** | spine; search | 10-16 |
| **RHI** | 10-21 `amc` | Spine + search + IR page 10-15: newest item is the Q2 notice (07-16). About 7d lead | spine; roberthalf.com investor-center financial-news (WebFetch works) | 10-16 |
| **SCCO** | 10-22 | **Stocktitan listing 404s on every try (4th day: 10-12 → 10-15): use search.** Search 10-15: nothing. Q3'25 call notice was posted the day before (10-28 for 10-29), so no PR is expected before ~10-21 | search; southerncoppercorp.com | 10-21 |
| DOW | 10-22 | Spine 10-15: nothing (Q3'25 call was 10-23 8am) | spine; 8-K | 10-16 |
| GILD | 10-29 | Spine + search 10-15 nothing. GILD's Q3'25 date PR was 10-09 (21d lead), so one is overdue | spine; gilead.com news | 10-16 |
| WHR, DTE, OSK | 10-28/29 | Spine 10-15 nothing. WHR Q3'25 notice was 10-20 for 10-27 | spine | 10-20 |
| DVA, ITW, NVT, XOM | 10-23..30 | Spine 10-15 nothing. DVA Q3'25 notice was 10-13 for 10-29 (now overdue). XOM IR page shows no Q3 event yet | spine | 10-16 |
| EXEL, EBAY | 10-27..11-04 | Spine + search 10-15 nothing. EXEL Q3'25 was 10-21 for 11-04; EBAY has no date (Q2 was 08-05) | spine | 10-16 |
| MKTX, MAT, MDLZ | 10-28..11-05 | Spine 10-15 nothing. MKTX Q3'25 PR was 10-16 for 11-07; MDLZ Q3'25 PR was 10-09 for 10-28 (overdue); MAT Q3'25 notice date not logged | spine | 10-16 |
| **INFY** | 10-23 `amc` | News coverage (upstox/kotakneo) cites the mid-Sept board filing: results Fri 10-23. Q2 FY27 times unconfirmed; the Q2 FY26 filing had results at 3:45pm IST (= bmo ET). infosys.com events page 403s | NSE/BSE filing or infosys.com event page | 10-16 |
| BMRN, ARE | 10-26 | Spine 10-15 nothing | spine | 10-16 |
| **IRDM** | 10-22 `Unknown` | Spine + search 10-15: nothing. **Q2 PR said no conference calls** (pending Rocket Lab deal), so no date PR may ever come; Q3'25 notice was 10-02 for 10-23 | EDGAR 8-K; spine | 10-16 |
| WBS | — | **Skipped (delisted)**, but the scanner calendar may still carry it. Ben's item | — | — |

## Upcoming Confirmed: locked dates (don't re-research)

One line per confirmed symbol whose date is still ahead (≥ 10-12). **Checked mechanically against
`earnings_upcoming` on 2026-10-11: 109 of 110 DB rows ↔ ledger, 0 date/time mismatches.** Pruned as reported: LW, STZ
(10-06), PEP (10-08), DAL (10-09), all four now **verified against their 8-Ks** in the 10-11 source audit.
⚠ **BK has no `earnings_upcoming` row at all** (last `earnings_date_sources` snapshot 10-02, `no_data`), so the
10-06 confirm below is in this ledger only. Flagged for Ben. **Weakest locks still ahead:** BX (search snippet
of a 403'd page), GM (search summary; bmo inferred), CME and MSCI (search summaries), SCHW (date inferred
from the Business Update). Inferred times are marked in each row. Format: `SYM | date | time | source — session`.

| Symbol | Date | Time | Source — session |
|--------|------|------|------------------|
| C | 2026-10-13 | bmo | Citi 2025 calendar PR (citigroup.com): *"3Q26 – Tuesday, October 13, 2026,"* release ~8am ET, webcast ~11am ET — 09-22 |
| DPZ | 2026-10-13 | bmo | Domino's PR 09-10 16:05 ET (stocktitan wire text; ir.dominos.com timed out): results 6:05am, webcast 8:30am ET — 09-29 |
| JNJ | 2026-10-13 | bmo | investor.jnj.com PR 08-31: release ~6:45am, call 8:30am ET Tue 10-13 — 09-29 |
| JPM | 2026-10-13 | bmo | jpmorganchase.com/ir PR 09-17: results ~7:00am, call 8:30am ET — 09-29 |
| UNH | 2026-10-13 | bmo | unitedhealthgroup.com PR 09-15: results before open, call 8:00am ET — 09-29 |
| WFC | 2026-10-13 | bmo | newsroom.wf.com *"Wells Fargo Updates 2026 Earnings Release Date Information"*: results ~7:00am, call 10am ET — 09-29 |
| ACI | 2026-10-13 | bmo | Albertsons PR 09-29, 14d lead (stocktitan wire text) — 10-05 |
| PGR | 2026-10-14 | bmo | Progressive August results release (8-K 7.01, 09-18): *"We plan to release September results on Wednesday, October 14, 2026, before the market opens"* — 09-23 |
| BAC | 2026-10-14 | bmo | BAC PR 09-30 (stocktitan wire text): release ~6:45am ET, call 8:30am. Closes the unsourced 06-30 lock question for Q3 — 10-06 |
| MS | 2026-10-14 | bmo | morganstanley.com/about-us-ir third-quarter-2026 call page (curl 200): release ~7:30am ET, call 9:30am — 10-06 |
| STT | 2026-10-14 | bmo | State Street PR 09-23 (stocktitan wire text): release ~7:30am ET, call 11:00am — 10-06 |
| FAST | 2026-10-14 | bmo | Fastenal PR 09-28 (stocktitan wire text): call Wed 10-14 9:00am CT. bmo **inferred** (release time not stated; DB bmo) — 10-06 |
| ASML | 2026-10-14 | bmo | ASML FY2025 20-F financial calendar (via search): Q3 results 10-14; bmo **inferred** from the usual 07:00 CET release — 10-12 |
| ERIC | 2026-10-15 | bmo | `ericsson.com/en/investors/financial-calendar/2026/q3-2026`: *"Oct 15, 2026 07:00 (CET)"* = 01:00 ET ⇒ bmo — 09-24 |
| FHN | 2026-10-15 | bmo | `ir.firsthorizon.com` PR 09-22: materials ~6:30am ET, call 9:30am ET. Snapshot 10-14 was already stale — 09-23 |
| JBHT | 2026-10-15 | amc | `investor.jbhunt.com` "Estimated Earnings Periods" table: Q3 release **October 15, 2026**, quiet period Sep 26 – Oct 15; amc = Item 2.02 furnished 20:08–21:26Z (16:0x–16:2x ET) 8/8 since 2024-10 — 09-24 |
| WIT | 2026-10-15 | bmo | wipro.com events page: *"Results for the Second quarter ending September 30, 2026, will be announced on October 15, 2026, Thursday after stock market trading hours in India"* (= US morning) — 10-01 |
| AA | 2026-10-15 | amc | q4cdn 3Q26-EarningsAnnouncement.pdf (PR 09-15): after NYSE close, call 5:00pm EDT — 10-06 |
| BK | 2026-10-15 | bmo | bny.com 2026 earnings-calls PR: release ~6:30am ET, call 11:00am — 10-06. ⚠ **No `earnings_upcoming` row exists** (dropped after 10-02); see notes_for_ben |
| MAN | 2026-10-15 | bmo | investor.manpowergroup.com *Announce 3rd Quarter 2026 Earnings Results*: before the open — 10-06 |
| MRSH | 2026-10-15 | bmo | marsh.com PR 09-17: before the open, call 8:30am EDT — 10-06 |
| PLD | 2026-10-15 | bmo | Prologis PR 09-03 (finviz copy): call 9am PT/12pm ET. bmo **inferred** (release time not stated; DB bmo) — 10-06 |
| PNC | 2026-10-15 | bmo | PNC PR 09-03 (stocktitan wire text): release ~6:30am ET, call 10:00am — 10-06 |
| SCHW | 2026-10-15 | bmo | ⚠ **Inferred**: Schwab *Fall Business Update* PR 09-17 (Thu 10-15 8:30am ET); it doesn't mention earnings. Earnings rode the update in 3/3 (Q3'25, Q1'26, Q2'26) — 10-06 |
| TSM | 2026-10-15 | bmo | investor.tsmc.com: call Thu 10-15 14:00 Taiwan = 02:00 ET, so results precede the US open. **Time corrected from amc** — 10-06 |
| USB | 2026-10-15 | bmo | q4cdn USB PR (10-01): before the open, call 8am CT — 10-06 |
| RF | 2026-10-16 | bmo | ir.regions.com 2026 release-dates PR: *"pre-market open on Friday, Oct. 16, 2026,"* call 10am ET — 09-25 |
| TFC | 2026-10-16 | bmo | media.truist.com 09-18: *"before the market opens on Friday, Oct. 16, 2026,"* call 8am ET — 09-25 |
| CFG | 2026-10-16 | bmo | CFG PR (finviz copy): call 9:00am ET — 10-06 |
| MTB | 2026-10-16 | bmo | M&T PR 09-18 (finviz copy): before the open Fri 10-16, call 8:00am ET — 10-06 |
| TRV | 2026-10-16 | bmo | investor.travelers.com *Schedules Conference Call … Q3 2026*: release before the 9:00am ET call — 10-06 |
| AGNC | 2026-10-19 | amc | AGNC PR 09-30 20:01Z (via stocktitan): *"after market close on October 19, 2026,"* call 10-20 8:30am ET — 10-01 |
| CCK | 2026-10-19 | amc | crowncork.com/news 09-22 PR: *"after the close of trading on the New York Stock Exchange on Monday, October 19, 2026,"* call Tue 10-20 9am EDT — 09-28 |
| CLF | 2026-10-19 | bmo | clevelandcliffs.com detail/703 (10-01): before open, call 8:30am ET. **Time corrected from amc** — 10-02 |
| FITB | 2026-10-19 | bmo | ir.53.com event page: results ~6:30am ET, call 9:00am ET, per the 2026/2027 annual dates PR — 09-28 |
| FNB | 2026-10-19 | amc | fnb-online.com PR 09-29: *"after the market close on Monday, October 19, 2026,"* call 10-20 8:30am. **Date corrected from 10-15** — 09-30 |
| STLD | 2026-10-19 | amc | Steel Dynamics Q3 guidance PR (finviz copy): after the close, call 10-20 11:00am ET. Cached IR URL was the Q2 PR — replaced — 10-06 |
| WRB | 2026-10-19 | amc | q4cdn WRB PR: after the close, call 5:00pm ET — 10-06 |
| ZION | 2026-10-19 | amc | Zions *2026 Earnings Release Dates* PR: call 5:30pm ET — 10-06 |
| WAL | 2026-10-19 | amc | Western Alliance PR 10-06 (stocktitan wire text): *"after the market closes on Monday, October 19, 2026,"* call 10-20 12:00pm ET — 10-07 |
| UAL | 2026-10-20 | amc | United webcast PR 09-30 (stocktitan wire text): *"after market close on Tuesday, October 20,"* call 10-21 10:30am ET — 10-07 |
| MMM | 2026-10-20 | bmo | 3M *Upcoming Investor Event* PR 10-06 (stocktitan): call Tue 10-20 8am CT. Release time not stated; **bmo inferred** from call time + DB — 10-07 |
| HAS | 2026-10-20 | bmo | Hasbro BW PR 09-29 (finviz copy): *"before the market open on Tuesday, October 20, 2026,"* call 8:30am ET — 10-07 |
| NOC | 2026-10-20 | bmo | Northrop date PR (finviz copy): *"prior to the market opening"*, webcast 9:30am ET — 10-07 |
| MSCI | 2026-10-20 | bmo | MSCI BW PR 09-24 (search summary of financialcontent copy): pre-market, call 11:00am ET — 10-07 |
| HAL | 2026-10-20 | bmo | Halliburton BW PR 09-15 (finviz copy): call 8:00am CT. bmo **inferred** (release before the call, time not stated) — 10-07 |
| ADC | 2026-10-20 | amc | Agree BusinessWire 09-30 16:05 ET (financialcontent copy): *"after the market closes on Tuesday, October 20, 2026,"* call 10-21 9am — 10-01 |
| GPC | 2026-10-20 | bmo | genpt.com PR 09-29: call 8:30am ET; bmo **inferred** (Item 2.02 6/6 at 07:2x ET) — 09-30 |
| KEY | 2026-10-20 | bmo | investor.key.com 2026 call-dates PR: *"Tuesday, October 20th, 2026 at 8 a.m. ET,"* results before open — 09-29 |
| NLY | 2026-10-20 | amc | Annaly BW 09-29 (financialcontent copy): *"after the market close on Tuesday, October 20, 2026,"* call 10-21 9am — 09-30 |
| RTX | 2026-10-20 | bmo | rtx.com PR 09-29: *"Tuesday, October 20, prior to the stock market opening,"* call 8:30am — 09-30 |
| SYF | 2026-10-20 | bmo | `investors.synchrony.com` detail/588: release ~6:00am ET, call 8:00am ET. Snapshot 10-14 was already stale — 09-23 |
| ALLY | 2026-10-20 | bmo | Ally PR 09-17 (finviz copy): ~7:30am ET, call 9:00am — 10-06 |
| CB | 2026-10-20 | amc | Chubb PR (finviz copy): release after the close, call Wed 10-21 8:30am — 10-06 |
| COF | 2026-10-20 | amc | Capital One PR 09-24 (stocktitan wire text): ~4:05pm ET, call 5:00pm — 10-06 |
| EWBC | 2026-10-20 | amc | investor.eastwestbank.com dates PR (03-30): after the close, call 5pm ET — 10-06 |
| GE | 2026-10-20 | bmo | geaerospace.com 3rd Quarter 2026 webcast page: Tue 10-20 7:30am EDT. bmo from the call time — 10-06 |
| EFX | 2026-10-20 | bmo | Equifax PR 10-06 (stocktitan wire text): release 6:30am ET, call 8:30am. **Time corrected from amc**; lead 14d — 10-08 |
| PEGA | 2026-10-20 | amc | Pega PR 10-07 (stocktitan wire text): *"after market close"*, call 10-21 8:00am EDT; lead 13d — 10-08 |
| ALK | 2026-10-20 | amc | Alaska webcast PR 10-07 (stocktitan): after close, call 10-21 11:30am ET. **Time was Unknown**; 13d lead — 10-09 |
| GM | 2026-10-20 | bmo | ⚠ Weak: GM Q2'26 call notice per search summary (page timed out); bmo inferred from Q1 pattern — 10-09 |
| ABT | 2026-10-21 | bmo | abbott.mediaroom.com 09-30: *"Wednesday, Oct. 21, before the market opens,"* call 9am ET — 10-01 |
| CSX | 2026-10-21 | amc | GlobeNewswire 09-21: *"after the market close on Wednesday, Oct. 21, 2026,"* call 4:30pm ET — 09-30 |
| MCO | 2026-10-21 | bmo | Moody's BW 09-30 07:00 ET (financialcontent copy): *"before the start of NYSE trading on Wednesday, October 21, 2026,"* call 9am — 09-30 |
| WH | 2026-10-21 | amc | investor.wyndhamhotels.com detail/430 (09-23): ~4:30pm ET 10-21, call 10-22 8:30am — 09-30 |
| CCI | 2026-10-21 | amc | Crown Castle PR (finviz copy): *"after the market closes on Wednesday, October 21, 2026,"* call 4:45pm ET — 10-07 |
| CME | 2026-10-21 | bmo | cmegroup.com PR 09-04 (search summary; page timed out on WebFetch): release 6:00am CT, call 7:30am CT — 10-07 |
| DHR | 2026-10-21 | bmo | Danaher PR (finviz copy): materials posted 6:00am ET, call 8:00am ET — 10-07 |
| TXN | 2026-10-21 | amc | TI PR 10-01 (PRNewswire via stocktitan): call 3:30pm CT — 10-05 |
| T | 2026-10-21 | bmo | AT&T PR 08-27 (finviz copy): *"before the New York Stock Exchange opens,"* call 8:30am ET — 10-08 |
| ELV | 2026-10-21 | bmo | Elevance PR 10-05 (biopharmawatch copy; ir.elevancehealth.com not fetched): 6:00am EDT, call 8:30am — 10-08 |
| LUV | 2026-10-21 | amc | Southwest PR 10-01 (finviz copy): after close, call 10-22 10am ET — 10-08 |
| LRCX | 2026-10-21 | amc | Lam PR 09-30 (finviz copy): call 2pm PT/5pm ET. amc **inferred** from call time + Item 2.02 history — 10-08 |
| MOH | 2026-10-21 | amc | Molina PR 09-02 (biopharmawatch copy): after close, call 10-22 8am ET — 10-08 |
| PKG | 2026-10-21 | amc | PCA BW 09-17 (finviz copy): after close, call 10-22 9am ET — 10-08 |
| KNX | 2026-10-21 | amc | Knight-Swift BW 10-01 (finviz copy): after close, call 5:30pm ET. **DB 10-21 was right** (search had said 10-22 from Earnings Whispers) — 10-08 |
| IBM | 2026-10-21 | amc | IBM PR 10-07 (finviz copy): call 5:00pm ET; amc inferred from call time — 10-09 |
| TMO | 2026-10-21 | bmo | TMO BW 09-28 (finviz copy): *before the market opens*, call 7am ET — 10-09 |
| TSLA | 2026-10-21 | amc | Tesla deliveries PR 10-02 (financialcontent): *after market close*, webcast 4:30pm CT — 10-09 |
| FAF | 2026-10-21 | amc | First American PR 10-07 (stocktitan wire text): 14d lead. A search summary had said no Q3 PR existed; the spine found it — 10-09 |
| ROL | 2026-10-21 | amc | Rollins PRN 10-07 (stocktitan copy): *"after the market closes on October 21"*, call 10-22 8:30am ET. DB right; finnhub 10-28 wrong — 10-09 |
| NEE | 2026-10-21 | bmo | NextEra *Announces Date for Release of Third-Quarter 2026* PR (stocktitan wire text); PR date not captured — 10-09 |
| GL | 2026-10-21 | amc | Globe Life *Announces Third Quarter 2026 Earnings Release and Conference Call* PR (stocktitan wire text); PR date not captured — 10-09 |
| QS | 2026-10-21 | amc | QuantumScape *Announces Timing of Third Quarter 2026 Business Update* PR (stocktitan wire text); PR date not captured — 10-09 |
| SAP | 2026-10-21 | amc | sap.com/investors events page (via search): disclosure 22:05 CEST = 16:05 ET — 10-12 |
| META | 2026-10-21 | amc | Meta PRN 10-12 (stocktitan page): *"after market close on Wednesday, October 21st"*, call 4:30pm ET; 9d lead. DB/yfinance right, finnhub 10-28 wrong — 10-13 |
| KMI | 2026-10-21 | amc | Kinder Morgan PR 10-14 (stocktitan page): *after market close*, webcast 4:30pm ET; 7d lead — 10-15 |
| LVS | 2026-10-21 | amc | Sands PR 10-14 (stocktitan page): after close, call ~1:30pm PT; 7d lead — 10-15 |
| PM | 2026-10-21 | bmo | PMI PR 10-14 (stocktitan page): release ~7:00am ET, webcast 9am; 7d lead — 10-15 |
| SF | 2026-10-21 | bmo | Stifel GNW 10-14 (stocktitan page): before the open, call 9:30am ET; 7d lead. Finnhub 10-28 wrong — 10-15 |
| SLM | 2026-10-22 | amc | Sallie Mae PR 10-13 (stocktitan page): after close, call 5:30pm ET; 9d lead. DB right, finnhub 10-28 wrong — 10-14 |
| AAL | 2026-10-22 | bmo | GlobeNewswire 10-01: call 10-22 7:30am CT. Release time not stated; **bmo inferred** from the call time — 10-02 |
| ARGX | 2026-10-22 | bmo | argenx HY release 07-23 financial calendar: *"October 22, 2026: Third Quarter 2026 Financial Results and Business Update"*; its releases go out 07:00 CET ⇒ bmo — 10-01 |
| BX | 2026-10-22 | bmo | blackstone.com *"Third-Quarter 2026 Investor Call"* (search snippet; page 403s WebFetch): call 10-22 9:00am ET. bmo inferred (BX releases ahead of its call) — 10-01 |
| BYD | 2026-10-22 | amc | Boyd investors.boydgaming.com PR 10-01: results shortly after 4:00pm ET, call 5:00pm ET — 10-02 |
| CBRE | 2026-10-22 | bmo | ir.cbre.com detail/269 (09-28): *"approximately 6:55 a.m. Eastern time on Thursday, October 22, 2026,"* call 8:30am — 10-01 |
| LMT | 2026-10-22 | bmo | investors.lockheedmartin.com 3Q26 PR: call Thu 10-22 8:30am ET. Live row was already 10-22 (snapshot 10-20 stale); bmo from call time — 10-02 |
| PCG | 2026-10-22 | bmo | investor.pgecorp.com PR 09-24: call 10-22 11:00am ET. Release time not stated; **bmo inferred** from Item 2.02 acceptance pattern (8/8 quarters 00:13–01:57 on the release-day date, e.g. Q2 2026-07-23 00:21) — 10-01 |
| REXR | 2026-10-22 | amc | ir.rexfordindustrial.com detail/380, PR 09-28 16:05 ET: *"after the market closes on Thursday, October 22, 2026,"* call 10-23 11am. All 3 feeds were wrong — 09-29 |
| NSC | 2026-10-22 | bmo | NSC PR 10-02 (Yahoo copy): call 10am ET. bmo **inferred** — 10-05 |
| SNA | 2026-10-22 | bmo | Snap-on webcast PR 10-08 (stocktitan): release before open, call 10am ET. **DB 10-15 was 7d early**; 14d lead — 10-09 |
| POOL | 2026-10-22 | bmo | Pool GlobeNewswire 10-08 (stocktitan copy): *"before the market opens on October 22"*, call 11am ET; 14d lead. Time was Unknown; finnhub 10-15 wrong — 10-09 |
| TSCO | 2026-10-22 | bmo | Tractor Supply Business Wire 10-09 (stocktitan copy): *"before the market opens on Thursday, October 22"*, call 10am ET; 13d lead. Time was Unknown — 10-09 |
| BPOP | 2026-10-22 | bmo | Popular BW 10-01 (stocktitan copy): *before the market opens*, call 11am ET — 10-12 |
| DGX | 2026-10-22 | bmo | Quest PR 09-22 (stocktitan): *before the market opens*, call 8:30am ET — 10-12 |
| DOV | 2026-10-22 | bmo | Dover PRN 09-16 (stocktitan): ~7:00am ET, call 9:30am — 10-12 |
| HBAN | 2026-10-22 | bmo | Huntington PR 09-30 (stocktitan): *prior to the market opening*, call 9am ET — 10-12 |
| HON | 2026-10-22 | bmo | Honeywell PR 09-24 (stocktitan): *before the opening of the Nasdaq Stock Market*, call 8:30am — 10-12 |
| LAZ | 2026-10-22 | bmo | Lazard PR 10-01 (stocktitan): *Thursday morning*, call 8am ET; bmo **inferred** — 10-12 |
| NDAQ | 2026-10-22 | bmo | Nasdaq GNW 10-01 (stocktitan): ~7:00am ET, call 8am — 10-12 |
| NEM | 2026-10-22 | amc | Newmont PR 09-24 (stocktitan): *after North American markets close*, call 5:30pm EDT. **Time corrected from bmo** — 10-12 |
| ORI | 2026-10-22 | bmo | Old Republic PR 10-08 (stocktitan): call 8:30am ET; bmo **inferred** (release time not stated) — 10-12 |
| PG | 2026-10-22 | bmo | P&G PR 09-24 (stocktitan): 8:30am ET webcast; bmo **inferred** — 10-12 |
| RNG | 2026-10-22 | amc | RingCentral PRN 10-08 (stocktitan): *after market close*, call 5pm ET — 10-12 |
| CMCSA | 2026-10-22 | bmo | Comcast BW PR 09-15 (search result): release *earlier that morning*, call 8:30am ET — 10-13 |
| DECK | 2026-10-22 | amc | Deckers PR 10-12 16:05 (stocktitan page): call ~4:30pm ET; amc **inferred** from call time. **Time was Unknown** — 10-13 |
| NOK | 2026-10-22 | bmo | Nokia financial-calendar PR 2025-12-01 (search): Q3 report 22 Oct; bmo **inferred** (~08:00 EEST release) — 10-13 |
| PHM | 2026-10-22 | bmo | PulteGroup PR 08-27 (finviz/barchart copy via search): before the market opens, call 8:30am ET — 10-13 |
| SPOT | 2026-10-22 | bmo | Spotify PR 09-24 (stocktitan page): *before market open*, Q&A 8:00am ET — 10-13 |
| SSNC | 2026-10-22 | amc | SS&C PR 10-06 (stocktitan page): *after the close*, call 5:00pm ET — 10-13 |
| UNP | 2026-10-22 | bmo | Union Pacific PR 09-24 (stocktitan page): release 7:45am ET, call 8:45am — 10-13 |
| VLO | 2026-10-22 | bmo | Valero PR 09-08 (stocktitan page): release *the morning before* the 10am ET call; bmo **inferred** (Q1/Q2 releases 06:30) — 10-13 |
| VRSN | 2026-10-22 | amc | Verisign PR 10-01 (stocktitan page): ~4:05pm ET, call 4:30pm — 10-13 |
| WDC | 2026-10-22 | amc | WD PR 10-08 (stocktitan page): *after the market closes*, call 4:30pm ET — 10-13 |
| SLB | 2026-10-23 | bmo | SLB BW 09-28 (stocktitan page): release 7:00am ET, call 9:30am; 25d lead — 10-14 |
| BAH | 2026-10-23 | bmo | investors.boozallen.com (BW 09-11): call Fri 10-23 8am EDT, release *"before the call"* — 10-02 |
| AXP | 2026-10-23 | bmo | Amex webcast PR 09-23 (stocktitan page): release ~7:00am ET, call 8:30am — 10-13 |
| E | 2026-10-23 | bmo | Eni 2026 financial calendar (search): board 10-22, results + call 10-23; bmo **inferred** (Italian site: before Milan open) — 10-13 |
| GNTX | 2026-10-23 | bmo | Gentex PR 10-01 (stocktitan page): *before the market opens*, call 9:30am ET — 10-13 |
| RITM | 2026-10-23 | bmo | Rithm PR 10-12 (stocktitan page): *before the market opens*, call 8am ET. DB 10-29 and finnhub 11-03 wrong, yfinance right — 10-13 |
| NUE | 2026-10-26 | amc | Nucor guidance PR 09-17 (q4cdn): *"after the markets close on Monday, October 26"*, call 10-27 10am ET — 10-14 |
| PSA | 2026-10-26 | amc | Public Storage PR 10-05 (stocktitan page): *after the market close*, call 10-27 12pm ET — 10-14 |
| WELL | 2026-10-26 | amc | Welltower PR 09-23 (stocktitan page): after NYSE close, call 10-27 9am ET — 10-14 |
| VZ | 2026-10-26 | bmo | verizon.com / GNW 09-28: *"Monday, October 26, 2026,"* materials 7:00am, webcast 8:30am ET — 09-29 |
| HIG | 2026-10-26 | amc | newsroom.thehartford.com PR 09-28: ~4:05pm EDT — 10-05 |
| BRO | 2026-10-26 | amc | Brown & Brown PR 10-01 (stocktitan page): *after market close*, call 10-27 8am ET — 10-13 |
| CDNS | 2026-10-26 | amc | Cadence PR 10-05 (stocktitan page): webcast 2pm PT / 5pm ET; amc **inferred**. **Time was Unknown** — 10-13 |
| CINF | 2026-10-26 | amc | Cincinnati Financial PRN 10-07 (stocktitan page): *after the close*, call 10-27 11am ET — 10-13 |
| PII | 2026-10-27 | bmo | Polaris PR 10-06 (stocktitan page): call 9am ET; bmo **inferred** (release time not stated). **DB 10-26 was 1d early** — 10-14 |
| PNR | 2026-10-27 | bmo | Pentair PR 10-14 06:50 ET (stocktitan page): *before the opening of the NYSE*, call 9am ET; 13d lead. **DB 10-20 was 7d early**; finnhub right — 10-14 |
| TER | 2026-10-27 | amc | Teradyne PR 10-13 16:30 ET (stocktitan page): ~4:30pm ET, call 10-28 8:30am. **DB 10-21 was 6d early** — 10-14 |
| HUBB | 2026-10-27 | bmo | Hubbell GNW 10-13 (stocktitan page): *prior to the opening of the market*, call 10am ET. DB right; finnhub 11-03 wrong — 10-14 |
| JBLU | 2026-10-27 | bmo | JetBlue BW 10-13 (stocktitan page): call 10am ET; bmo **inferred** (release time not stated). DB right; finnhub 11-03 wrong — 10-14 |
| BKR | 2026-10-27 | amc | Baker Hughes GlobeNewswire 09-28: *"press release at 5 p.m. Eastern Time on Tuesday, Oct. 27, 2026,"* webcast 10-28 9:30am — 10-01 |
| CNP | 2026-10-27 | bmo | CenterPoint GlobeNewswire 09-29 16:30 ET: call 10-27 8:00am ET, release *"on the same day before the market opens"* — 10-01 |
| HCA | 2026-10-27 | bmo | investor.hcahealthcare.com / BW 09-30: call Tue 10-27 9am CT. bmo inferred (release time not stated) — 10-02 |
| KO | 2026-10-27 | bmo | investors.coca-colacompany.com detail/1173 (09-29): *"Oct. 27 before the NYSE opens,"* call 8:30am. finnhub's +7d was right — 09-30 |
| TRU | 2026-10-27 | bmo | newsroom.transunion.com Q3 date PR: release ~6:00am CT Tue 10-27, call 8:30am CT. Cached URL was the Q2 PR — replaced — 10-02 |
| EQT | 2026-10-27 | amc | EQT PR 10-07 20:15 (stocktitan wire text): *"after market close on Tuesday, October 27,"* call 10-28 10am ET. **DB 10-20 was 7d early** — 10-08 |
| ACGL | 2026-10-27 | amc | Arch BW 09-28 (finviz copy): *after the close*, call 10-28 10am ET — 10-15 |
| AMT | 2026-10-27 | bmo | American Tower BW 09-29 (finviz copy): release 7:00am ET, call 8:30am. Time was Unknown — 10-15 |
| CSGP | 2026-10-27 | amc | CoStar BW 10-01 (finviz copy): *following the market close*, call 5pm EDT. Time was Unknown — 10-15 |
| EXE | 2026-10-27 | amc | Expand Energy PR 10-14 (stocktitan page): after close, call 10-28 9am EDT; 13d lead. Finnhub 11-03 wrong — 10-15 |
| MRP | 2026-10-27 | bmo | Millrose PR 10-06/07 (stocktitan page): *before the market opens*, call 10am ET. Time was Unknown — 10-15 |
| NVS | 2026-10-27 | bmo | novartis.com events page (Oct 27, no time shown). ⚠ bmo **inferred** (usual ~07:00 CET release) — 10-15 |
| VTR | 2026-10-27 | amc | Ventas BW 09-25 (finviz copy): after NYSE close, call 10-28 10am ET. Time was Unknown — 10-15 |
| VRT | 2026-10-28 | bmo | Vertiv PR 10-14 (stocktitan page): before market open, call 11am ET. **DB 10-21 was 7d early** — 10-15 |
| FLS | 2026-10-28 | amc | Flowserve BW 10-13 (stocktitan page): after close, call 10-29 8:30am ET. DB 10-27 was 1d early — 10-14 |
| ATI | 2026-10-29 | bmo | ATI PR 10-13 (stocktitan page): release 6:30am CT, call 7:30am CT. DB 10-27 was 2d early; finnhub 11-03 wrong — 10-14 |
| BC | 2026-10-29 | bmo | Brunswick GlobeNewswire 10-08 (stocktitan copy): *"before the market opens on October 29"*, call 11am ET; 21d lead. **DB 10-22 was 7d early** (yfinance, finnhub said 10-29) — 10-09 |
| DXCM | 2026-10-29 | amc | Dexcom Business Wire 10-07 (stocktitan copy): *"after market close on October 29"*, call 4:30pm ET; 22d lead. Time was Unknown; finnhub 10-22 wrong — 10-09 |
| WST | 2026-10-29 | bmo | West PRN 10-08 (stocktitan copy): *"before the market opens on Thursday, October 29"*, call 8am ET; 21d lead. **DB 10-22 was 7d early** — 10-09 |
| MA | 2026-10-29 | bmo | Mastercard BW 10-08 (stocktitan copy): call 9:00am ET. Release time not stated; **bmo inferred** from the call time + DB. 21d lead; finnhub 10-22 wrong — 10-09 |
| CARR | 2026-10-29 | bmo | Carrier PRN 10-08 *Earnings Advisory* (stocktitan copy): call 7:30am ET. Release time not stated; **bmo inferred** from the call time. **DB 10-27 was 2d early** — 10-09 |
| VLTO | 2026-10-29 | amc | Veralto PR 10-12 (stocktitan page): *after market close on Thursday, October 29*, call 10-30 7:30am ET. **DB 10-21 was 8d early** — 10-13 |
| AJG | 2026-10-29 | amc | Gallagher PRN 10-08 (stocktitan copy): *"after the market closes on Thursday, October 29"*, call 5:15pm ET; 21d lead. DB right; finnhub 10-22 wrong — 10-09 |
| GD | 2026-10-30 | bmo | GD PR 10-09 (stocktitan PRN copy): call Fri 10-30 9am EDT; bmo **inferred** from call time — 10-12 |
| DOC | 2026-11-02 | amc | Healthpeak BW 10-01 (financialcontent copy): after NYSE close Mon 11-02, call 11-03 10am ET. Snapshot 10-22 was stale — 10-02 |
| KHC | 2026-11-04 | bmo | Kraft Heinz BW 10-12 (finviz copy): before the open, Q&A 9am ET. DB right; finnhub 10-27 wrong — 10-15 |
| NVST | 2026-11-04 | amc | Envista PRN 10-06 (finviz copy): call 2pm PT / 5pm ET; amc **inferred** from the call time — 10-15 |
| KMB | 2026-11-05 | bmo | Kimberly-Clark 8-K ex99.1 10-15 (sec.gov): *final Q3 results Thursday Nov 5*, ~6:30am ET, Q&A 8am. **DB 11-03 was 2d early** — 10-15 |

---

# Research Sessions (newest first)

## Session: 2026-10-15 (Thursday) — 07:21 AM ET

40-row queue (30 disputes + 10 unconfirmed). **15 confirmed:** KMI, LVS, PM, SF (10-21); ACGL, AMT, CSGP, EXE, MRP, NVS, VTR (10-27); VRT (10-28); KHC, NVST (11-04); KMB (**11-03 → 11-05**).
Method: one spine run over all 40 (~23 min, background; SCCO 404 again) found 6 new PRs (SF, VRT, LVS, PM, EXE, MRP) plus KMI; KHC, KMB, NVST, AMT, CSGP, VTR, ACGL came from WebSearch, read through finviz/stocktitan/sec.gov copies. AMX feed: still no 3Q26 event.
Date corrections: KMB DB 11-03 → 11-05 (8-K ex99.1: final Q3 results, in the 10-15 prelim-results PR). VRT: live row was already 10-28 (dispute row stale).
Time inferences: NVS bmo (no time on the events page), NVST amc (call 5pm ET). INFY not confirmed: 10-23 only from news coverage, time probably bmo while DB says amc.
Not resolved: see carry-overs. HDB/IBN held (HDB board meeting Sat 10-17 per secondary coverage).
Process note: with a redirected background spine, the task output file only says "done"; read the redirect target.

## Session: 2026-10-14 (Wednesday) — 07:20 AM ET

40-row queue (31 disputes + 9 unconfirmed, shrinking as rows closed). **12 confirmed:** PNR (10-20 → **10-27 bmo**), TER (10-27 amc), SLM, SLB, NUE, PII (10-26 → **10-27**), PSA, WELL, ATI, FLS (10-27 → **10-28**), HUBB, JBLU.
Method: two spine runs (23 + 15 symbols, SCCO 404'd a third time), WebFetch of the stocktitan article per hit, plus ~20 WebSearches for names the spine showed nothing for. PNR's PR landed 06:50 ET today, so the spine caught it in the morning. AMX Event.svc feed: still no 3Q26 event.
Date corrections: PNR DB 10-20 → 10-27 (finnhub right); PII 10-26 → 10-27; FLS 10-27 → 10-28.
Not resolved (no PR yet; see carry-overs): IRDM, WHR, AMX, ISRG, OMC, KMI, RHI, SF, VRT, LVS, PM, DTE, OSK, GILD, SCCO, DOW, DVA, ITW, NVT, XOM, INFY, BMRN, ARE, EXE, EXEL, EBAY. HDB/IBN held for Ben's policy question. IRDM may hold no call at all.

## Session: 2026-10-13 (Tuesday) — 07:19 AM ET

40-row queue (21 disputes + 19 unconfirmed). **19 confirmed:** META (10-21 amc), VLTO (10-29 amc), DECK and CDNS (time Unknown → amc), SPOT, SSNC, UNP, VLO, VRSN, WDC, CMCSA, NOK, PHM, E, AXP, RITM, GNTX, BRO, CINF.
No date changed in the DB: the calendar had already moved META to 10-21 and VLTO to 10-29 before the session. The gain was source verification plus the two Unknown times.
Method: one spine run over 36 queue symbols (~20 min; SCCO's listing 404'd), then WebFetch of the stocktitan article page per hit, and WebSearch for CMCSA/NOK/PHM/E, which found PRs the spine had not.
Not resolved: see the carry-over table (PNR, AMX, ISRG, OMC, RHI, SF, TER, VRT, LVS, PM, DOW, IRDM, SCCO, SLM, KMI, GILD, WHR, DTE, OSK, DVA, ITW, NVT, XOM, INFY, SLB; HDB/IBN held).
Process note: a Monitor on the spine output re-injected the full dispute list on every event (about 8 copies). Use one end-of-run read instead; noted in the carry-over header.

## Session: 2026-10-12 (Monday) — 07:18 AM ET

40-row queue (15 disputes + 25 unconfirmed). **14 confirmed:** ASML (20-F calendar, bmo inferred), GD, SAP (sap.com IR calendar), and BPOP, DGX, DOV, HBAN, HON, LAZ, NDAQ, NEM, ORI, PG, RNG from the 40-symbol spine run (stocktitan wire copies). **NEM time corrected bmo → amc.** Mid-session spine finished with SCCO UNREAD (stocktitan 404, not an absence); re-run. Spine found **no Q3 date PR** for: IRDM, WHR, PNR, AMX, ISRG, OMC, KMI, RHI, SF, TER, VLTO, VRT, LVS, PM, DTE, OSK, SLM, GILD, DECK, CMCSA, DOW, NOK, PHM, and nothing yet for HDB/IBN (held for Ben's policy Q2). Searches: ISRG third-party dates disagree (10-19/20/21); IRDM likely holds **no call** (pending Rocket Lab deal), no Q3 date yet; KMI aggregator says 10-22 amc (unsourced; Q2 notice came 07-15 for 07-22, ~7d lead ⇒ due ~10-15); TER Q3'25 notice was 14d ahead (10-15 → 10-28) ⇒ Q3'26 notice due ~10-13 and finnhub's 10-27 looks likelier than DB 10-21. Not researched (time): SCCO retry, SPOT, SSNC and the rest beyond the 40.
Carry-overs next check: TER/KMI/RHI/PNR/AMX/IRDM/ISRG/OMC/SF/VLTO/VRT/LVS/PM/DTE/OSK/SLM/GILD/DECK/WHR/CMCSA/DOW/NOK/PHM **10-13** (spine again), SCCO **10-12 retry**.

## Session: 2026-10-09 (Friday) — 07:21 AM ET

40-row queue (25 disputes + 15 unconfirmed). **19 confirmed** (SNA, ALK, IBM, TMO, TSLA, GM, FAF, NEE, GL, QS, then ROL, POOL, TSCO, BC, DXCM, WST, MA, CARR, AJG after the stocktitan rate-limit experiment let the spine read 30 symbols cleanly), WBS still skipped (delisted).
Spine ran 8 symbols clean in the morning, then 429'd on the next batch of 9, so FAF/PM/NEE/LVS/EQR/SAP got searches only. FAF, NEE, GL and QS were
confirmed from stocktitan article pages (WebFetch kept working while the curl listing pages were blocked).
A search summary had wrongly said FAF had no Q3 PR; the PR was dated 10-07. I then measured stocktitan's limit (10 requests per fixed 300 s window;
`analysis/stocktitan_ratelimit_test_plan.md`) and rewrote `spine.py` to pace itself. Its first real use read **30 symbols in 15 min with no 429**,
which turned up Q3 date PRs for ROL, POOL, TSCO, BC, DXCM, WST, MA, CARR and AJG (all confirmed above from the article pages).
**Date corrections this session:** BC DB 10-22 → **10-29**; WST DB 10-22 → **10-29**; CARR DB 10-27 → **10-29**; SNA DB 10-15 → 10-22.

| Symbol | Result | Source |
|--------|--------|--------|
| SNA | **10-22 bmo** (DB 10-15, finnhub/yf 10-22 were right) | webcast PR 10-08 (stocktitan), 14d lead |
| ALK | 10-20 **amc** (time was Unknown) | webcast PR 10-07 (stocktitan), 13d lead |
| IBM | 10-21 amc | finviz copy of PR 10-07, call 5pm ET |
| TMO | 10-21 bmo | finviz copy of BW 09-28 |
| TSLA | 10-21 amc | 10-02 deliveries PR (financialcontent copy) |
| GM | 10-20 bmo | ⚠ weak: search summary of GM's Q2 call notice; investor.gm.com timed out |
| FAF | 10-21 amc (DB right) | PR 10-07 (stocktitan article page), 14d lead |
| NEE | 10-21 bmo | date-release PR (stocktitan article page) |
| GL | 10-21 amc | earnings release and call PR (stocktitan article page) |
| QS | 10-21 amc | timing-of-business-update PR (stocktitan article page) |
| ROL | 10-21 amc (DB right; finnhub 10-28 wrong) | PRN 10-07, stocktitan copy, 14d lead |
| POOL | 10-22 bmo (time was Unknown; finnhub 10-15 wrong) | GlobeNewswire 10-08, stocktitan copy, 14d lead |
| TSCO | 10-22 bmo (time was Unknown) | Business Wire 10-09, stocktitan copy, 13d lead |
| BC | **10-29 bmo** (DB 10-22 was 7d early) | GlobeNewswire 10-08, stocktitan copy, 21d lead |
| DXCM | 10-29 amc (time was Unknown; finnhub 10-22 wrong) | Business Wire 10-07, stocktitan copy, 22d lead |
| WST | **10-29 bmo** (DB 10-22 was 7d early) | PRN 10-08, stocktitan copy, 21d lead |
| MA | 10-29 bmo (**bmo inferred** from the 9am call) | Business Wire 10-08, stocktitan copy |
| CARR | **10-29 bmo** (DB 10-27; **bmo inferred** from the 7:30am call) | PRN 10-08 earnings advisory, stocktitan copy |
| AJG | 10-29 amc (DB right; finnhub 10-22 wrong) | PRN 10-08, stocktitan copy, 21d lead |

Held (no company Q3 date found): PNR (spine 10-09 12:40: nothing since 09-22), ISRG (spine: nothing since 09-08), OMC (spine: nothing since 09-09), LVS, PM, SAP, EQR, KMI, SF, TER, VLTO, VRT (spine 10-09: no Q3 date PR for any of these), GD, OSK, DTE, SLM, GILD, SCCO, DECK, IRDM, WHR (spine 10-09: nothing dated October), ASML, HDB/IBN (Saturday-dated, Ben's policy), AMX, RHI (not before 10-12).
Not worked: INTC, BPOP, CMCSA, DGX, DOV (never spined this session), NSC, ITW, F, FCX.

Next checks: 10-12 for everything above (spine paces itself now: nine symbols per five minutes, so run big lists with `run_in_background`).

## Session: 2026-10-08 (Thursday) — 07:21 AM ET

40-row queue, 18 disputes + 22 unconfirmed. **10 confirmed** (EQT, PEGA, EFX, T, ELV, LUV, LRCX, MOH, PKG, KNX), **1 skipped (WBS, delisted)**, rest held.
Spine ran clean for 6 symbols, then 429'd after 8 total. Searches + finviz/biopharmawatch/stocktitan copies covered the rest.

| Symbol | Result | Source |
|--------|--------|--------|
| EQT | **10-27 amc** (DB had 10-20; live row already 10-27) | PR 10-07 (stocktitan), 20d lead |
| PEGA | 10-20 amc | PR 10-07 (stocktitan), 13d lead |
| EFX | 10-20 **bmo (was amc)** | PR 10-06 (stocktitan): 6:30am ET |
| T | 10-21 bmo | finviz copy of 08-27 PR |
| ELV, MOH | 10-21 bmo / amc | biopharmawatch copies of company PRs (company pages not fetched) |
| LUV, LRCX, PKG, KNX | 10-21 amc | finviz copies; LRCX amc inferred from 5pm ET call |

Held:
- **SNA, PNR, ISRG, OMC, GM, IBM, PM**: no Q3 date PR. GM's Q1/Q2 releases say 10-20 (company-stated) but the call-details PR isn't out, so time and page unread (WebFetch timed out). IBM IR lists 10-21 as *preliminary*.
- **SAP**: IR calendar via search says 10-21 22:05 CET (amc); the page 403s. **FAF**: search says 10-21 amc from prior releases, no Q3 PR. **EQR**: search 10-28, may have no call.
- **KMI, NEE, ALK, GL, QS, SF, TER, VLTO, VRT, ROL, RHI, POOL, WHR, IRDM, LVS**: no company Q3 date found (spine 429 for most; searches show aggregators only). **ASML**: aggregators 14 Oct 07:00 CET, no company page. **AMX**: feed re-read, no 3Q26 event. **HDB, IBN**: Saturday-dated, held for Ben's policy Q.
- **WBS**: skipped again (delisted).

Next checks: 10-09 (SNA, PNR, AMX, ALK, IBM, OMC, ISRG, GM), 10-12 onward for the 10-21/22 disputes once their ~7–14d PRs land.

## Session: 2026-10-07 (Wednesday) — 07:17 AM ET

40-row queue, 17 disputes + 23 unconfirmed. **10 confirmed** (WAL, UAL, MMM, HAS, NOC, MSCI, HAL, CCI, CME, DHR), none skipped, 30 held.
Stocktitan spine ran clean for 8 symbols, then 429'd the whole second batch (15 symbols, all UNREAD, not absences). Article pages 403 curl but WebFetch reads them. Searches plus finviz/stocktitan copies covered the rest.

| Symbol | Result | Source |
|--------|--------|--------|
| WAL | 10-19 amc | WAL PR 10-06 (stocktitan via WebFetch) |
| UAL | 10-20 amc | webcast PR 09-30 (stocktitan via WebFetch) |
| MMM | 10-20 bmo (inferred) | 3M investor-event PR 10-06: call 8am CT |
| HAS, NOC, MSCI | 10-20 bmo | finviz/BW copies |
| HAL | 10-20 bmo (inferred) | BW 09-15 finviz copy, call 8am CT |
| CCI | 10-21 amc | finviz copy of CCI PR |
| CME | 10-21 bmo | cmegroup.com PR (search summary) |
| DHR | 10-21 bmo | finviz copy of DHR PR |

Held:
- **GM, ISRG, EFX, OMC**: no Q3 date PR fetched. ISRG search snippet said 10-21 amc (DB 10-20). EFX Q2 results were 6:30am ET, so DB `amc` is suspect.
- **FAF, KNX, EQR, ELV, IBM**: search summaries only (FAF 10-21 amc matches DB; KNX 10-22 vs DB 10-21; EQR 10-28; ELV aggregator). No fetchable company source.
- **SF**: search says 10-22 (DB 10-21, finnhub 10-28); Q3 PDF 404s. **ALK**: aggregator 10-23. **POOL**: aggregator 10-21. **ASML**: aggregators 10-14, no company page read.
- **KMI, QS, TER, VLTO, VRT, GL, WHR, EQT, PNR, PEGA, SNA, IRDM, HDB, IBN, AMX**: no company date found. SNA still has no webcast PR.

## Session: 2026-10-06 (Tuesday) — 07:16 AM ET

40-row queue, 10 disputes + 30 unconfirmed. **27 confirmed** (list below), **1 skipped (WBS, delisted)**, rest held.
Stocktitan spine 429'd after ~5 symbols again; company-wire text + first-party pages + search then covered the rest.

| Symbol | Result | Source |
|--------|--------|--------|
| BAC, MS, STT, FAST | 10-14 bmo | wire text (BAC/STT/FAST), morganstanley.com (MS). FAST bmo inferred |
| PNC, USB, BK, MAN, MRSH, AA, PLD | 10-15 (AA amc, rest bmo) | PNC wire text, USB/AA q4cdn PDFs (read with pdftotext), bny.com, investor.manpowergroup.com, marsh.com, finviz copy (PLD, bmo inferred) |
| SCHW | 10-15 bmo, **date inferred** | Fall Business Update PR (does not mention earnings); same-day pattern 3/3 |
| TSM | 10-15 **bmo (was amc)** | investor.tsmc.com: call 14:00 Taiwan = 02:00 ET |
| CFG, MTB, TRV | 10-16 bmo | finviz copies of BW PRs (CFG, MTB), investor.travelers.com |
| STLD, WRB, ZION | 10-19 amc | finviz copy / q4cdn PDF |
| ALLY, CB, COF, EWBC, GE | 10-20 (ALLY, GE bmo; CB, COF, EWBC amc) | finviz/wire copies, investor.eastwestbank.com, geaerospace.com webcast page |
| WBS | **skipped** | delisted: SEC `tickers=[]`, Form 15-12G 08-31 and 09-30, Santander closed Aug 2026 |

Held:
- **ASML** (10-14): asml.com and investor.asml.com 403/timeout; only a search snippet (14 Oct 07:00 CET). Try the 6-K or the Q3 release itself.
- **SNA**: no Q3 webcast PR, so 10-15 is dead. Expect 10-22; PR due ~10-08. Dispute row left `unresolved`.
- **AMX**: no 3Q26 event in the feed (61 events, newest 2Q26).
- **HDB**: board meets Sat 10-17 (search reports of the NSE intimation). **IBN**: no notice found. Both held for Ben's policy Q2.
- **EFX**: Q3 date PR not out (Q2 one was 07-07). **GM**: no Q3 event page. Aggregators only for both.
- **EQT, MMM, PNR, PEGA, WAL, ALK, POOL, IRDM**: spines read, no company date PR. WAL is ~4d late against last year's PR timing.
- Time-wasters: stocktitan 429s GE/GM; `morganstanley.com` WebFetch ECONNRESET but curl works.

## Session: 2026-10-05 (Monday) — 07:15 AM ET

32 disputes + READ FIRST block. **4 confirmed (ACI, TXN, HIG, NSC); the rest held (no company Q3 date out yet).**
Stocktitan spine hit 429 after the first 10 symbols (SNA ACI EQT TSCO MMM PNR PEGA GL QS SF read OK;
TER VLTO VRT WAL NSC SLM ITW CINF HIG UHS **unread**, not absent).

| Symbol | Result | Source |
|--------|--------|--------|
| ACI | **10-13 bmo confirmed** (call 8:30am EDT; PR 09-29, 14d lead; was 6d overdue by my 10-02 reckoning, not overdue: PR existed) | stocktitan wire text of the Albertsons PR |
| TXN | **10-21 amc confirmed** (call Wed 10-21 3:30pm CT; PR 10-01 via PRNewswire) | stocktitan wire text; investor.ti.com timed out |
| HIG | **10-26 amc confirmed** (~4:05pm EDT release, webcast 10-27 9am; PR 09-28) | newsroom.thehartford.com |
| NSC | **10-22 confirmed** (call 10am ET Thu; PR 10-02). ⚠ bmo is **inferred**: PR says results "in advance of the call", no release time | Yahoo copy of the PR (dateline 10-02) |

Held / no change:
- **AMX**: Event.svc feed read 10-05, newest event still 2Q26 (07-21). **No 3Q26 event as of 10-05.** DB 10-13 still unsourced.
- **MMM**: investors.3m.com events page says "no upcoming events", no Q3 call listed (aggregators say 10-20).
- **SNA**: spine shows newest keyword hit is the Q2 webcast PR (07-09); **no ~10-01 webcast PR ⇒ 10-15 is dead**, 10-22 PR due ~10-08.
- **EQT, TSCO, PNR, PEGA, GL, QS, SF**: spine read, no Q3 date PR yet. EQT/TSCO now 4d overdue vs the Q2 lead.
- **ITW**: IR Q3 event slug 404; aggregator says 10-27 bmo ("confirmed" label, but unsourced). DB 10-23 unverified.
- **CINF, UHS, TER, VLTO, VRT, WAL, SLM, ALK, IRDM, POOL, SCCO, WBS, BC, DECK, ARE, LEG, VFC, RHI**: no company source found (aggregators only); spine 429 for most.
- **CDNS**: aggregators say 10-26 amc; Q2 webcast PR was 07-06 (3w lead) so Q3's is due ~10-05/06. Recheck.
- ⚠ **VRT**: investors.vertiv.com news is a JS shell for WebFetch; WAL news page likewise. Use spine/EDGAR.

Next checks: 10-06 (spine for the 429'd names, CDNS, EQT, TSCO), 10-07 (PNR, PEGA, IRDM, WBS), 10-08 (SNA).

## Session: 2026-10-02 (Friday) — 07:18 AM ET

34 surfaced (24 `date_disagreement`, 6 `both`, 4 `unknown_time`). **8 confirmed on company sources (CLF, LMT, AAL, BYD, TRU, HCA, BAH, DOC); 26 held.**
Stored dates changed: **none** — all 8 already matched the live calendar (stale snapshot again). Time gains: CLF amc→bmo (corrected), AAL/BAH/DOC Unknown→set.
Process slip: DOC's `research_url` was first written with a guessed BusinessWire path (not from any result); replaced the same minute with the financialcontent copy that search returned. Never construct a URL.

### Held (no company-issued Q3 source yet)

| Symbol | Why | Next check |
|--------|-----|------------|
| **AMX** | feed (pageSize=100) still has no 3Q26 event; newest is 2Q26 07-21 | 10-05 |
| **EQT, MMM, PNR, PEGA, GL, QS, RHI, SF, TER, VLTO** | stocktitan spine (10-02): no Q3 advance PR (only dividend PRs); search = aggregator estimates (MMM "10-20 9am" is marketbeat only) | 10-05 |
| **VRT, WAL, BPOP, F, FCX, NSC, SLM, ITW** | spine hit HTTP 429 (VRT onward); search shows only estimates (WAL "10-20 amc/10-21 call" and FCX 10-22 are aggregator) | 10-05, spine first |
| **ALK, POOL, WBS, IRDM** | IR pages show no Q3 date; IRDM/WBS have no calls (pending deals) so look for a PR only | 10-05 |
| **BC** | no Q3 date PR; Q2 reported **07-30**, so DB 10-22 is doubtful (likely later) | 10-05 |
| **DECK, TSCO** | IR calendar empty / no Q3 PR; marketbeat 10-22 only. TSCO Q2 PR came ~3wk ahead (07-02 for 07-23) so due now | 10-05 |


## Session: 2026-10-01 (Thursday) — 07:19 AM ET

42 surfaced (36 `date_disagreement`/`both`, 6+ `unknown_time`/`unconfirmed`). **10 confirmed on company sources (ABT, ADC, WIT, AGNC, BX, BKR, CNP, CBRE, ARGX, PCG); 32 held.**
Stored dates changed: **none** — every confirmed date already matched the live calendar (stale snapshot again); CBRE/ARGX/PCG were time-only gains (Unknown → bmo).

### Confirmed

| Symbol | Result | Source |
|--------|--------|--------|
| **ABT** | 2026-10-21 `bmo` (DB 10-14 snapshot stale; finnhub+yfinance right) | abbott.mediaroom.com 09-30: *"Wednesday, Oct. 21, before the market opens,"* call 9am ET. |
| **ADC** | 2026-10-20 `amc` (finnhub 10-27 wrong) | Agree BusinessWire 09-30 16:05 ET: *"after the market closes on Tuesday, October 20, 2026,"* call 10-21 9am. |
| **WIT** | 2026-10-15 `bmo` (finnhub 10-13 wrong) | wipro.com/investors/events page: results *"October 15, 2026, Thursday after stock market trading hours in India"* (≈ US morning). |
| **AGNC** | 2026-10-19 `amc` (finnhub 10-26 wrong) | AGNC PR 09-30 (via stocktitan): *"after market close on October 19, 2026,"* call 10-20 8:30am ET. investors.agnc.com timed out on WebFetch. |
| **BX** | 2026-10-22 `bmo` (finnhub 10-15 wrong); bmo inferred | blackstone.com *"Blackstone Announces Third-Quarter 2026 Investor Call"*: call 10-22 9:00am ET. ⚠ page 403s WebFetch/curl — read via search snippet only; stocktitan spine had no such PR. |
| **BKR** | 2026-10-27 `amc` (yfinance right, finnhub 10-21 wrong) | GlobeNewswire 09-28 (marketscreener copy): *"press release at 5 p.m. Eastern Time on Tuesday, Oct. 27, 2026,"* webcast 10-28 9:30am. Cached URL was the Q2 PR — replaced with the Q3 event page. |
| **CNP** | 2026-10-27 `bmo` (yfinance+finnhub right) | GlobeNewswire 09-29: call 10-27 8am ET, *"released on the same day before the market opens."* |
| **CBRE** | 2026-10-22 `bmo` | ir.cbre.com detail/269 (09-28): *"approximately 6:55 a.m. Eastern time on Thursday, October 22, 2026,"* call 8:30am. Cached URL (detail/267) was the Q2 PR — replaced. |
| **ARGX** | 2026-10-22 `bmo` | argenx HY release (07-23) "Expected financial calendar": *"October 22, 2026: Third Quarter 2026 Financial Results and Business Update."* Time: argenx releases 07:00 CET ⇒ bmo. |
| **PCG** | 2026-10-22 `bmo` (time inferred) | investor.pgecorp.com PR 09-24: call 10-22 11:00am ET; release time not stated. EDGAR acceptance times 8/8 quarters 00:1x–01:57 on the release-day date ⇒ overnight/pre-market. |

### Held (no company source yet)

| Symbol | Why | Next check |
|--------|-----|------------|
| **LMT, PNR, EQT, CLF, GL, QS, RHI** | stocktitan spine (read 10-01) shows no Q3 advance PR; search finds only aggregator estimates. | 10-02 |
| **TER, VLTO, VRT, PEGA, MMM, BPOP, BYD, SF** | stocktitan 429'd the whole batch — spine unread; WebSearch finds nothing company-issued (TER/VRT hits were marketscreener-style estimates). | 10-02 (spine) |
| **AMX** | Event.svc (pageSize=100) newest event still 2Q26 (07-21 amc); no 3Q26. | 10-06 |
| **F, FCX, NSC, SLM, TRU, KBR, WAL** | no company Q3 date; only aggregator "estimated" dates (FCX 10-22, WAL 10-20). | 10-06 |
| **ALK** | No webcast PR yet (Q2's came ~07-08 for 07-22); Investor Day 09-29 only. | 10-06 |
| **POOL, WBS** | No Q3 PR. WBS: no call (pending Santander merger); Q2 was after close 07-21. | 10-06 |
| **AAL, DECK, BC, DOC, TSCO** | No company PR (DECK IR calendar: *"no upcoming events"*; DOC Q3-25 advance was 09-25-2025 so due any day). AAL/DECK 10-22 appear only on marketbeat. | 10-02 |
| **IRDM** | Calls suspended (pending Rocket Lab acquisition); no Q3 date. | 10-06 |

### Notes
- stocktitan JSON-LD now serialises without spaces (`"headline":"..."`) — the old regex in `reference_stocktitan_jsonld_discovery.md` needs `\s*`. It 429'd after 9 fetches at 9s spacing; the second batch got 429 on all 8 even after a pause.
- WebFetch on blackstone.com 403s; on investors.agnc.com times out.
- Helper at `inbox/fetch/conf.sh` (confirm + IR URL + dispute update in one call).
- direct_db_query writes print nothing; verified via SELECT.

## Session: 2026-09-30 (Wednesday) — 07:14 AM ET

28 surfaced (all disputes: 20 `date_disagreement`, 4 `both`, 4 `unknown_time`). **8 confirmed on company sources (FNB, KO, RTX, MCO, NLY, GPC, CSX, WH; GPC time inferred), 5 time-only (MMM, VRT, WAL, LRCX, UAL), 15 held incl. LRCX/UAL dates.**
Stored dates changed: FNB 10-15→**10-19** (company PR; yfinance was right, finnhub 10-15 wrong). Others matched the live calendar already (stale snapshot again).

### Confirmed

| Symbol | Result | Source |
|--------|--------|--------|
| **FNB** | **2026-10-19 `amc`** (DB 10-15 was wrong; Q2 lead was 16d, this one 20d) | fnb-online.com PR **09-29**: *"after the market close on Monday, October 19, 2026,"* call Tue 10-20 8:30am ET. |
| **KO** | 2026-10-27 `bmo` (finnhub+yfinance right, DB 10-20 doubt resolved) | investors.coca-colacompany.com detail/1173, PR 09-29 10:00 EDT: *"release third quarter 2026 financial results Oct. 27 before the NYSE opens,"* call 8:30am. Cached URL was the Q2 PR — replaced. |
| **RTX** | 2026-10-20 `bmo` (finnhub 10-27 wrong) | rtx.com PR 09-29: *"Tuesday, October 20, prior to the stock market opening,"* call 8:30am. |
| **MCO** | 2026-10-21 `bmo` (finnhub 10-27 wrong) | Business Wire 09-30 07:00 ET (read via financialcontent copy): *"before the start of NYSE trading on Wednesday, October 21, 2026,"* call 9:00am. ⚠ `ir.moodys.com` news-details URL returned the Q4-25 release when fetched — stale cache, don't use. |
| **NLY** | 2026-10-20 `amc` (yfinance right, finnhub 10-28 wrong) | Business Wire 09-29 (financialcontent copy; businesswire.com 403s WebFetch): *"after the market close on Tuesday, October 20, 2026,"* call Wed 10-21 9:00am. |
| **GPC** | 2026-10-20 (finnhub 10-15 wrong); time **`bmo` inferred** | genpt.com PR 09-29 states date + call 8:30am ET but NOT bmo/amc. bmo from SEC Item 2.02 pattern: 6/6 quarters furnished 11:21–12:09Z (07:2x ET). |
| **CSX** | 2026-10-21 `amc` | GlobeNewswire 09-21: *"after the market close on Wednesday, Oct. 21, 2026,"* call 4:30pm ET. |
| **WH** | 2026-10-21 `amc` | investor.wyndhamhotels.com detail/430, PR 09-23: *"Wednesday, October 21, 2026 at approximately 4:30 p.m. ET,"* call 10-22 8:30am. |

### Time-only (date NOT locked) — from SEC Item 2.02 acceptance times, all 6–7 quarters consistent (times UTC `Z`)
MMM `bmo` (10:33–11:34Z) · VRT `bmo` (10:00–11:00Z) · WAL `amc` (20:08–20:26Z) · LRCX `amc` (20:07–20:09Z) · UAL `amc` (20:00Z). Dispute rows closed `confirmed_agent` only for LRCX and UAL (`unknown_time`); MMM/VRT/WAL left `unresolved` since their dates are still disputed.

### Held

| Symbol | Why | Next check |
|--------|-----|------------|
| **AMX** | Event.svc feed (pageSize=100, strptime) newest still 2Q26 (07-22 call); no 3Q26. | 10-06 |
| **WIT** | No advance PR (due ~10-06). | 10-06 |
| **LMT** | Only aggregators say 10-27; no company PR (Q2 PR was 07-01, Q1 04-01 ⇒ Q3 due ~10-01). news.lockheedmartin.com slug guess 404. investors.lockheedmartin.com 403 to curl. | 10-01 |
| **PNR, EQT, CLF** | No Q3 advance found (PNR Q1 PR 04-14 for 04-28 ⇒ ~2wk lead; EQT/CLF due ~10-01). | 10-01 |
| **ADC** | Q3 PRs historically ~10-01/10-04; none yet. | 10-01 |
| **PEGA, AGNC, GL, QS, RHI, SF, TER, VLTO** | No company Q3 date found by search. (SF Q2 PR came 07-15; RHI Q2 PR 07-16 ⇒ ~1 week lead; VLTO Q2 PR 07-13.) | 10-06 |
| **MMM, VRT, WAL** | Dates undated by company (VRT/RHI aggregator 10-28). | 10-07 |
| **LRCX, UAL** dates | Time locked; date 10-21 unsourced (UAL aggregator 10-20). | 10-07 |

### Notes
- **stocktitan needs the fuller UA** (`Chrome/126.0 Safari/537.36` + Accept + Accept-Language); the shorter `Chrome/120` string got 403 across the board. It then rate-limited (429 → "Too Many Requests" page, 200 status with a 2.5KB body) after ~3 fetches, so no spine data was obtained today; WebSearch surfaced the company PRs instead.
- WebSearch's "confirmed" labels from TipRanks/Nasdaq aggregators (LMT, UAL) were not used.
- direct_db_query writes print nothing; verified via SELECT.

## Session: 2026-09-29 (Tuesday) — 07:14 AM ET

22 surfaced (16 disputes, 6 unconfirmed). **8 confirmed on company sources (REXR, VZ, KEY, JNJ, JPM, UNH, WFC, DPZ), 14 held.**
0 stored dates changed (snapshot was stale for REXR 10-14→10-22 and VZ 10-20→10-26; live rows already had them). 2 `Unknown` times filled (VZ, KEY bmo).

### Confirmed

| Symbol | Result | Source |
|--------|--------|--------|
| **REXR** | **2026-10-22 `amc`** (the 4th-Thursday reading was right; finnhub 10-21 / yf 10-22) | ir.rexfordindustrial.com detail/380, PR **09-28 16:05 ET**: *"release third quarter 2026 financial results after the market closes on Thursday, October 22, 2026,"* call Fri 10-23 11am ET. Lead 24d. Dispute closed. |
| **VZ** | **2026-10-26 `bmo`** (yfinance was right; finnhub 10-20 wrong) | Verizon GlobeNewswire/verizon.com **09-28**: *"Monday, October 26, 2026,"* materials 7:00am ET, webcast 8:30am. Dispute closed. |
| **KEY** | **2026-10-20 `bmo`** | investor.key.com 2026 call-dates PR: *"Third quarter 2026 – Tuesday, October 20th, 2026 at 8 a.m. ET,"* results before market open. |
| **JNJ** | 2026-10-13 `bmo` | investor.jnj.com PR 08-31: call 8:30am ET Tue 10-13; release ~6:45am. |
| **JPM** | 2026-10-13 `bmo` | jpmorganchase.com/ir PR 09-17: call 8:30am ET, results ~7:00am. |
| **UNH** | 2026-10-13 `bmo` | unitedhealthgroup.com PR 09-15: results before open, call 8:00am ET. |
| **WFC** | 2026-10-13 `bmo` | newsroom.wf.com *"Wells Fargo Updates 2026 Earnings Release Date Information"*: results ~7:00am ET, call 10am. |
| **DPZ** | 2026-10-13 `bmo` | Domino's PR 09-10 16:05 ET (read via stocktitan wire text; ir.dominos.com timed out): webcast 8:30am ET, results 6:05am. |

### Held

| Symbol | Why | Next check |
|--------|-----|------------|
| **AMX** | Event.svc feed (pageSize=100, parsed with strptime — string-sorting `MM/DD/YYYY` gives garbage) newest still 2Q26; no 3Q26 event. | 10-06 |
| **WIT** | No advance PR yet (due ~10-06). | 10-06 |
| **ACI** | stocktitan newest 09-17, no FQ2 advance. 10-20 still the doubt. | 09-30, 10-07 |
| **KO** | No Q3 timing PR (spine newest 09-25). ⚠ **Q2-26 reported Tue 07-28** — DB 10-20 looks early; finnhub 10-27 may be right this time. Q1/Q2 timing PRs came ~3 weeks ahead. | 09-30 |
| **CLF, EQT** | No Q3 advance (Q2 PRs came 07-02 for 07-23 / 07-21, 19–21d lead ⇒ due ~10-01). DB 10-20 unsourced; bad-batch names (see confirmed_row_diverged). | 10-01 |
| **RTX, LMT, PNR** | No Q3 date found. Q2-26 was Thu 07-23 (RTX, LMT), Tue 07-28 (PNR) — DB 10-20 doubtful. | 10-01 |
| **ADC, PEGA, AGNC** | No Q3 advance found (ADC PRs ~10-01; Q2 was 07-30, so 10-20 doubtful; PEGA Q2 07-21 advance 07-07; AGNC IR/EDGAR silent). | 10-01 |
| **MMM, GPC** | No Q3 date/time yet. GPC Q3'25 advance was 09-30 → due 09-30/10-01. | 10-01 |

### Notes
- Stale snapshot again: REXR and VZ live rows were already right; locks, not corrections.
- WebSearch for KO/RTX/LMT/PNR returned only estimates or Q2 data — not used.
- `direct_db_query` writes print "No results returned"; verified via SELECT that they landed.

## Session: 2026-09-28 (Monday) — 07:14 AM ET

6 surfaced (3 disputes: AMX, REXR, WIT `date_disagreement`; 3 disputes: AGNC, CCK, FITB `unknown_time`).
**2 confirmed on company sources (CCK, FITB), 1 time-only (AGNC), 3 held (AMX, REXR, WIT).** 0 dates changed;
1 `Unknown` time filled via historical pattern (AGNC amc), 2 unknown times filled + dates re-confirmed (CCK amc,
FITB bmo). Also fixed a standing bug: AMX's cached IR URL used the broken `pageSize=25` feed param (returns
only 2014–2018 events) — re-cached with `pageSize=100` per the 09-22/09-25 cadence notes.
Reads: 6 searches, 11 WebFetches (2 AGNC investors.agnc.com timeouts, fell back to SEC EDGAR 8-K exhibits).

### Confirmed

| Symbol | Resolution | Evidence |
|--------|-----------|----------|
| **CCK** | **2026-10-19 `amc`** (date + time both company-sourced; dispute closed) | crowncork.com/news 09-22 PR *"CROWN HOLDINGS SCHEDULES THIRD QUARTER 2026 EARNINGS CONFERENCE CALL"*: *"release its earnings for the third quarter ended September 30, 2026, after the close of trading on the New York Stock Exchange on Monday, October 19, 2026,"* call Tue 10-20 9:00am EDT. Cached dispute URL (crowncork.com "Schedules Second Quarter 2026...") was stale — replaced with the Q3 PR. |
| **FITB** | **2026-10-19 `bmo`** (date + time both company-sourced; dispute closed) | ir.53.com event-details page for the 3Q26 call (Oct 19, 2026, 9:00am ET); the 2026/2027 annual-dates PR states results are available ~6:30am ET ahead of the call ⇒ bmo. No cached IR URL existed before today — now cached. |
| **AGNC** | **`amc` written via `--time-only`; 2026-10-19 date NOT locked** | No company 8-K/PR found for 3Q26 specifically (SEC EDGAR CIK 1423689 newest 8-K is the 07-20 Q2 release). Time rests on a clean 3/4-year pattern instead: 3Q22, 3Q23, 3Q25 press releases all state *"after market close"* (3Q24's 8-K is silent on timing but same release-day shape); all four years released on the **3rd Monday after quarter-end** (10-24 '22, 10-23 '23, 10-21 '24, 10-20 '25), and 2026-10-19 continues that exactly. Confident enough on time to close the `unknown_time` question; not confident enough on date to lock it without a same-quarter source — matches the FNB/SNA/REXR/ACI precedent of `--time-only` + dispute row `confirmed_agent`, calendar row left unconfirmed. |

### Held

| Symbol | Why held | Next check |
|--------|----------|------------|
| **AMX** | No 3Q26 event yet on the (now-fixed) Event.svc feed — newest is 2Q26 (07-21 amc). DB's 10-13 continues the Tuesday-amc 17→15→14 trend; finnhub's 10-20 is the known +7d artifact shape for this name. | 09-29, then 10-06 |
| **REXR** | No Q3 advance PR (press-releases list checked fresh, events-webcasts page explicitly says no upcoming events). Shortest-lead due date (09-20) is now 8+ days overdue; the 4th-Thursday-2026 cadence guess (10-22) is unconfirmed and its own PR due date (09-28) also just passed. | 09-29, then 09-30 |
| **WIT** | No board-meeting advance PR yet; per the cadence file the 9d-lead pattern puts one due ~10-06, so its absence today isn't informative. Cadence-predicted 10-15 `bmo` matches the DB row exactly; finnhub's 10-13 doesn't fit the Thursday-since-2024 pattern. | 10-06, then 10-07 |

### Notes

- `reference_company_cadence.md` already had detailed prior work on all six symbols (AMX, REXR, WIT held from
  09-22 → 09-25; CCK/FITB/AGNC were first-time names) — checked it before re-researching from scratch, which
  saved a redundant pass on the three held names and confirmed today's holds are consistent with the standing
  reasoning rather than new information.
- AGNC's `investors.agnc.com` news-release detail page timed out on WebFetch twice; SEC EDGAR 8-K exhibits
  (which render reliably) were used instead for the historical timing evidence.
- New cadence rows written for CCK, FITB, AGNC in `reference_company_cadence.md`.

# Maintenance History

## Weekly Maintenance — 2026-10-11 (Sunday)

Fifth weekly pass in a row (Task Scheduler, Opus). No mailbox notices. All five weekday sessions ran
(10-05 → 10-09) and each was committed. 10-09 also had an interactive afternoon with Ben (stocktitan rate-limit
experiment → paced `spine.py`).

**⭐ First source-accuracy audit (new step 7).** Census of **every agent confirm dated 09-01 → 10-09 (n = 50)**,
checked by 5 subagents (10 each, alphabetical, blind to source type) against the Item 2.02 8-K / Ex-99.1 on
EDGAR (ET `Accepted` from the index page). Both mismatches re-read by me. **Dates 49/50, times 49/50,
0 unverifiable.** By type: IR direct 38 (1 date miss DELL, 1 time miss GME), PR copy 11/11, search summary 1/1,
aggregator 0, feed agreement 0; time-inferred overlay 11 with 1 miss (GME). n is too small to rank types, and
the weak types are October dates (next week). **DELL** 09-03 → actually **09-01**: its events page pre-listed
09-03 when read 21d ahead, the date then moved, and the cadence row said not to look again. **GME** amc → actually
**bmo 09:02**: the time was inferred from 2.02 history across a financing quarter, the same shape as its known outlier.
Cadence rows fixed, SEC note extended (GWRE `items` omits 2.02; after-17:30 acceptances get the next-day filingDate).
`analysis/source_audit_20261011.md`. The question for Ben is in `notes_for_ben.md`.

**Archived.** Sessions **09-22 → 09-25** and the **09-20 maintenance entry** → summer archive, verbatim, checked
(`analysis/maintenance_archive_20261011.py`). **The summer archive is now closed** (07-01 → 09-25). Fall sessions
(10-01 on) start a `…2026-Q4_fall-earnings.md` file once they age out. Active log 863 → 668 lines, including the new header and this entry.

**Header rebuilt from the DB.** READ FIRST block **retired** (the hook merges the queue since 10-06), replaced by a
compact "still unconfirmed through 10-23" checklist: **46 rows** (ASML 10-14 first). Carry-overs rebuilt:
SNA, ACI, EQT, TSCO, ALK, the time-only five, and most of the 10-02 held set resolved and dropped. AMX's live row
moved **10-13 → 10-20**. PNR now ~3 business days overdue. Ledger: LW, STZ, PEP, DAL pruned (all four verified
by the audit). **109/110 DB rows ↔ ledger, 0 mismatches.** BK is the odd one: confirmed 10-06 but **no
`earnings_upcoming` row exists** (flagged for Ben). WBS's phantom row is gone, correctly.

**Promoted.** Cadence: outcomes for **ACI** (prediction wrong), **DELL**, **GME**; rows backfilled for **TXN, HIG,
NSC** (10-05 ran on the old prompt). Every 10-06 → 10-09 first-time name already had its row, so **proposal D works**.

**Calibration: week of 10-05 (5 of 5 sessions).**
- **Volume:** **70 dates confirmed** (4 / 27 / 10 / 10 / 19). Stored dates corrected: SNA 10-15 → **10-22**,
  EQT 10-20 → **10-27**, BC and WST 10-22 → **10-29**, CARR 10-27 → **10-29**, WAL 10-21 → **10-19**.
  Times corrected: EFX amc → **bmo**, TSM amc → **bmo**. Unknown → set: ALK, POOL, TSCO, DXCM. **0 wrong writes found
  this week** (the audit's two misses date from August).
- **Skip/doubt calls from 10-04, scored:** **SNA right** (53-week arithmetic ⇒ 10-22; the PR came on the predicted day,
  10-08). **ACI wrong**: the stored 10-13 was right. I predicted 10-20 from a 38-days-after-quarter-end pattern (n=2),
  and "overdue" was a read failure (the PR existed from 09-29). Quarter-end offset now joins weekday pattern as
  *not evidence*. **Overdue-PR doubts: 2 right (EQT +7d, WAL −2d), 1 wrong (TSCO: the date held, the PR just came 8d
  late at a 13d lead vs Q2's 21d), 1 pending (PNR).** So an overdue PR is real evidence, but a ~1-week overdue on a
  1-obs lead isn't enough to doubt a date.
- **Leads:** multi-obs leads held to the day (SNA 14 ×3, ACI 14 ×2, EQT 20). One-obs leads: **TSCO ran short for
  the first time** (21 → 13d). The tally is now 4 long, 1 short, so a single observation is noisy in both directions.
- **The new queue (A + D), first four runs:** 40 rows a morning, mixed by date. The 83 invisible rows are down to 46.
  Bookkeeping is happening without me. But disputes went **32 → 112 a morning**, so the overflow is growing. Flagged
  with numbers for Ben.
- **Drift (mine):** (1) 10-04's STATUS told Ben "SNA and ACI are both probably wrong". Half right, and the wrong
  half rested on n=2 arithmetic, the same class as the weekday-pattern doubts I'd demoted that same day. I generalized
  the demotion too narrowly. (2) The DELL cadence note *told future sessions not to re-check* a provisional date. Advice
  to skip a check should name the condition that ends it.

**Housekeeping.** `notes_for_ben.md`: crowd-out, SNA/ACI and Sonnet items → archive (resolved/superseded); new items:
audit + question, BK, queue pressure; HDB/IBN now 6 days out. MEMORY.md: all pointers resolve; two lines updated.
Outbox ≤ 128 lines, no rotation. Inbox root clean. **STATUS.md** rewritten.

## Weekly Maintenance — 2026-10-04 (Sunday)

Fourth weekly pass in a row (Task Scheduler, Opus). No mailbox notices. All five weekday sessions ran
(09-28 → 10-02, all Sonnet) and each was logged and committed.

**⚠⚠ Main finding: 83 unconfirmed rows dated ≤ 10-23 are invisible to the daily sessions.** The hook
backfills unconfirmed rows only into `25 − disputes` slots. Disputes ran 28 / 42 / 34 from 09-30, so the
backfill was zero, and every row where the three feeds agree (no dispute) never surfaced. That covers the
whole 10-14 → 10-17 cohort the 09-27 header told the sessions to front-load (BAC, MS, TSM, PNC, SCHW,
…), the ACI (09-30) and SNA (10-02) next-checks, and most of the 10-19 → 10-23 wave (TSLA, IBM, INTC, T,
PG, GE, GM, …). **Second cause:** the daily prompt (`launcher.py` `PROMPT_TEMPLATE`) never mentions the
log header, the carry-overs or the cadence table, and it sorts `unconfirmed` last, so the header's
front-load instruction had no way in. **My 09-27 note was wrong:** I wrote that overflow "slips a day
rather than vanishing" without reading how the ceiling applies. Corrected in
`feedback_window_gating_and_noop.md`. Proposal (A: merge by date, B: backfill floor, C: inject
next-checks, D: two prompt lines): `analysis/proposal_20261004_backfill_crowded_out.md`. It's at the top
of `notes_for_ben.md`. Stopgap: the header's new **READ FIRST** block lists all 83, nearest first.

**Archived.** Sessions **09-14, 09-15** and the **09-13 maintenance entry** were moved verbatim into the
summer archive ahead of the appendices (header range → 07-01 → 09-15). Script:
`analysis/maintenance_archive_20261004.py` (asserts every moved line landed; git is the backup).
Active log 705 → 667 lines (with the larger header and this entry). Sessions 09-22 → 10-02 kept.

**Header rebuilt from the DB.** READ FIRST block (83 invisible rows by date). Carry-overs rebuilt:
REXR, FNB and WIT resolved and dropped; SNA and ACI marked **10-05 FIRST** (their checks were missed);
AMX daily; EQT and TSCO added as *slightly overdue* (PR due ~10-01 at their Q2 leads); the time-only
five and the 10-02 held set each got a next-check. **Ledger: 48 rows rebuilt from `earnings_upcoming`,
0 mismatches.** It had been missing all 16 confirms from 09-29/09-30, and 10-01/10-02 lines had been
appended unsorted. Pruned 13 reported rows, each with an `earnings_events` row on its confirmed date.

**Promoted.**
- `reference_company_cadence.md`: **30 new rows** for names first confirmed 09-29 → 10-02 (the sessions
  wrote none after 09-28), plus time-only and held names with known leads. Outcomes written into FNB,
  REXR, WIT and AGNC. A *wave-level* paragraph (advance PRs bunched 09-28 → 10-01 at 18–29d). A scored
  feed-dissent table (below).
- `reference_stocktitan_jsonld_discovery.md`: the 09-30 UA change (Chrome/120 → 403), the JSON-LD
  losing its spaces (the old regex silently matches zero), and the 200-status 429 page.
- Helpers promoted to `analysis/helpers/`: `spine.py` (flags *unread* vs *empty*) and `conf.sh`. The
  10-01 copy in `inbox/fetch/` **hard-coded `trade_date='2026-10-01'`**, so reused on another day its
  dispute UPDATE would have matched nothing.

**Calibration — week of 09-28 (5 of 5 sessions).**
- **Volume:** 60 unique disputed symbols + 5 backfilled. **36 dates confirmed on company sources**,
  6 time-only (AGNC later dated), 26 disputes still open at Friday's close. **0 wrong writes found.**
  Stored values corrected: FNB date 10-15 → **10-19**, CLF amc → **bmo**. Every other confirm locked a
  date the live row already had (stale snapshot again).
- **Skip judgment on last week's carry-overs:** **REXR right** (10-22 predicted from 4th-Thursday +
  overdue PR; the PR came on the predicted day and was read the next morning). **WIT right** on date.
  **FNB: right to hold, wrong guess.** The PR came on the predicted due day, but the date was Monday
  10-19, not my 3rd-Thursday 10-15. **ACI, SNA: untested** (their checks never ran). **AMX: still
  pending.** Prior-quarter-weekday doubts went **2 for 4** (KO, LMT right; ADC, RTX wrong), so a weekday
  pattern isn't evidence against a stored date. Only an overdue PR is. Noted in the window-gating file.
- **Leads:** one-observation leads undershot again (FNB 16 → 20d, WIT 9 → ≥14d); **4 of 4** now ran
  long, none short. The 1.5× read-window rule stands. Multi-obs leads held (REXR 24d, CLF 18 vs 19d).
- **Feed dissents (21 company-resolved date disputes):** yfinance-vs-DB **7/7 yfinance**. finnhub-only
  **9/12 artifact, 2/12 right** (KO +7d, TRU +5d, both textbook "artifact" shapes that were real).
  **All three feeds wrong on 3/21** (REXR, LMT, DOC). The DB's first-snapshot date was right on only
  9/21. Table in the cadence file.
- **The Sonnet sessions, scored on the points I set on 09-27 (n=5):** reads are better than 09-25. AMX
  was read correctly every day, and 429'd spines were logged as *unread*, not absent. Throughput was
  strong: 8–10 confirms a morning on 22–42 surfaced. Sourcing slips: **DOC's `research_url` was first
  written with a constructed BusinessWire URL** (self-caught within the minute), and **BX was confirmed
  from a search snippet** of a 403'd company page (flagged as weak in the ledger). **Bookkeeping didn't
  happen:** no cadence rows after 09-28, no carry-over updates, and ledger lines missed for two days.
  But nothing in their prompt asks for any of it. The Opus sessions did it from habit. **So this is a
  prompt gap, not a model verdict:** the sessions did what the template says, competently. Proposal D
  adds the two missing lines.
- **Drift (mine):** a confident claim about the hook ("slips a day") written without reading the code
  path it described. Same class as the TECH absence argument: I asserted a mechanism I hadn't checked.
  Today I read the code before writing the proposal.

**Housekeeping.** `notes_for_ben.md`: new top item (crowd-out); SNA/REXR item → SNA only (REXR resolved
as predicted → archive); Sonnet item → this week's scoring; HDB/IBN policy question now **live**
(10-17 rows are in the READ FIRST block). Outbox ≤ 128 lines, no rotation. Inbox root clean.
`inbox/fetch/` added to `.gitignore` (fetch blobs are transient; ~5 MB already tracked stays as is).
**STATUS.md** rewritten.

## Weekly Maintenance — 2026-09-27 (Sunday)

Third weekly pass in a row (Task Scheduler, 18:00, Opus). No mailbox notices. Found the 09-25 session
logged but **uncommitted**, with its header and cadence bookkeeping undone. Finished and committed both.

**Archived.** Sessions **09-08 (stub), 09-09, 09-10, 09-11** (216 lines) moved verbatim into the summer
archive ahead of the appendices; archive header range → 07-01 → 09-11. Script
`analysis/maintenance_archive_20260927.py` (backs up both files, asserts every moved non-blank line
landed; passed). Active log keeps 09-14 → 09-25. The 09-13 maintenance entry stays one more week.

**Header rebuilt from the DB.** Carry-overs: REXR, AMX, ACI, FNB, SNA, WIT, each with a new **"How to
read"** column that records the working channel and its known traps, so a session doesn't have to find
them in an older note. The ⚠⚠ "no session ran 09-16 → 09-18" banner is removed (fixed 09-24). Window
watch replaced with the **25 unconfirmed 10-13 → 10-17 rows** by horizon-entry day, plus the Monday caveat
(no unconfirmed row ≤ 10-12 ⇒ Monday spawns only on a dispute). Ledger: CTAS, GIS, PAYX, DRI pruned
(reported), sorted by date, **25 rows checked mechanically against `earnings_upcoming`: 0 mismatches.**

**Promoted / corrected.**
- `reference_q4_event_feed.md` — ⚠ **it was wrong**: it said `sortDirection=desc` works. 09-24 had found
  the feed ignores it and returns oldest first, but that correction only reached a session note and the
  AMX cadence row. The 09-25 read then used the cached URL (`pageSize=25`) verbatim, got 2014–2018, and
  logged "quirk?". Fixed the note, its MEMORY.md line, and the URL inside the AMX cadence row. The cached
  `symbol_metadata` URL still needs `pageSize=100`, which is a weekday DB write (STATUS item 3).
- `reference_company_cadence.md` — **RF** and **TFC** rows added (first-time names confirmed 09-25, never
  written); **DAL** closed out (10-09 bmo, feed move was right; PR date still uncaptured); **REXR** row
  flags the 09-25 bad read ("list ends 03-19" contradicts 09-24's "current to 09-17").
- `feedback_window_gating_and_noop.md` — spawn fix **verified in code** (`ei_lite_refresh.py:375–377`,
  `launcher.py:get_due_unconfirmed`, `inject_context.py:missed_session_warning`) + the residual gap (a
  next-check on a row >14d out with no dispute still spawns nothing) + the 25-row cap (nearest first, so
  overflow slips a day, not lost) + this week's lead-table score (below).
- `MEMORY.md` — Q4-feed and window-gating lines updated; all 21 pointers resolve (the 3 unindexed `for_*.md` are the known stray mailbox duplicates).

**`notes_for_ben.md`:** spawn-gate item → archive verbatim (new "Moved at the 2026-09-27 maintenance"
section) and a Resolved line saying it **hasn't been exercised yet** (every morning since 09-22 had
disputes). Re-seeding item condensed (9 of 10 rows fixed, MDT left, class still open). SNA item widened
to REXR ("two stored dates I believe are wrong"). New item on the first Sonnet session. HDB/IBN (Saturday
10-17) added to policy question 2.

**Inbox/outbox.** Inbox root clean. Outbox unchanged, largest file 128 lines, so no rotation.

**Calibration — week of 09-21 (4 of 5 sessions: 09-22 → 09-25; 09-21 didn't run under the old gate).**
- 21 unique symbols. **15 dates confirmed on company sources (71%)**, 3 time-only with dates held on
  purpose (ACI, FNB, SNA), 3 held (AMX, REXR, WIT). **0 wrong writes.** Stored values corrected: UEC
  date +5d and time, ACN time, STZ time; 9 `Unknown` times filled.
- **Skip judgment:** nothing gated reported or moved inside its skip. UEC's 09-17 check would correctly
  have found nothing (PR 09-22, exact 7d lead to the *true* date). CCL's 09-16 check would have found the
  09-15 PR, so that miss was machinery, not judgment.
- **Lead table:** stable-channel leads held to the day (ACN 16d, UEC 7d, CCL within 1d). **Both 1-obs
  leads borrowed from another fiscal quarter undershot**: PEP 35 → 44d, MU 28 → 35d. Their windows opened
  7–9 days early, and PEP's PR sat 30 days unread. No wrong date resulted (DB right both times). New
  working rule, n=2: start reading 1-obs rows at ~1.5× the lead.
- **finnhub:** 0 of 4 resolved dissents right (JBHT +5d, PGR +19d, SYF −7d, FHN +6d); yfinance right on
  SYF and FHN. The pattern holds.
- **Drift:** (1) **Lessons stranded in session notes.** The AMX sort fix is the second case after MTN/PEP
  (09-14 "read open windows the day they open" was not applied 09-15). A correction that lives only in a
  session block is invisible three days later. Rule for myself: when a session finds a channel quirk, it
  updates the memory note or the carry-over row's "How to read" cell **the same day**. (2) **09-25
  (first Sonnet session):** two bad reads logged as absences, and no bookkeeping. One session isn't a
  sample; I'll score 09-28 → 10-02 on the same points.

**STATUS.md** rewritten.
