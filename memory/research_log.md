# Earnings Research Log

> Active log: full sessions for the last ~2 weeks (newest first, below), a compact ledger of
> confirmed-but-upcoming dates, and the open carry-overs with next-check dates. Older sessions live in
> the season archives: `memory/archive/research_log_2026-Q2_spring-earnings.md` (through 06-30) and
> `memory/archive/research_log_2026-Q3_summer-earnings.md` (07-01 → 09-25, **closed**, plus the summer's ledger
> and carry-over table as appendices) and `memory/archive/research_log_2026-Q4_fall-earnings.md` (from 09-28: the
> sessions that researched the fall wave, plus pruned ledger rows verbatim in its Appendix A). Maintenance notes at the very bottom.
> Per-symbol cadence/lead-times live in `memory/reference_company_cadence.md`. **Grep it by symbol
> (`^| SYM `); don't read it whole (~220 KB).**

## Still unconfirmed (rebuilt 2026-10-19 after the session)

Kept as a checklist so nothing falls off between sessions (the hook injects one date-sorted queue,
ceiling 40). 21 rows closed 10-19; what's left is waiting on a company PR or Ben's policy call. **Nearest date first.**

| Reports | Unconfirmed (`?` = time Unknown) | Notes |
|---------|-----------------------------------|-------|
| 10-17 | HDB, IBN | Saturday-dated Indian ADRs. Held for Ben's policy Q2 (`notes_for_ben.md`). HDB board meeting was Sat 10-17 per the 09-22 exchange filing (secondary coverage); IBN: no notice found |
| 10-20 | ISRG | No PR found 1 day out (last PR 09-08). Search shows only calendar estimates (10-20/10-21) |
| 10-22 | DOW, IRDM?, SCCO? | |
| 10-23 | INFY | 10-23 per news coverage of the board filing (not primary); **time likely bmo** (results ~3:45pm IST = 06:15 ET), DB says amc |
| 10-27 | CNC, GLW, PCAR, PYPL, ST, UPS | No PR yet (calendar estimates only). 21 of the 10-27 batch closed today |
| 10-28..11-05 | DVA, EBAY?, BMRN, MKTX, ROKU, CC?, COKE?, SW?, DTE, WHR, OSK | No PR yet. MKTX: under ICE acquisition, see cadence row |

## Open Carry-Overs: researched, unresolved, with next-check dates

Next-check ≈ **advance-PR due date + 1** (PRs mostly publish after the ~07:15 session start). **Each
row's "How to read" is the working channel and its known traps. Use it verbatim.**
Spine = `analysis/helpers/spine.py` (paces itself to stocktitan's 10-per-300s limit since 10-09; run big lists with `run_in_background`). Its output lists only date-keyword headlines, so no lines = no new PR. **Don't attach a Monitor to it: each event re-injects the whole dispute list.** Read the output file once at the end; a stocktitan article page via WebFetch gives the PR text.

| Symbol | DB row | Status | How to read | Next check |
|--------|--------|--------|-------------|------------|
| ISRG | 10-20 `amc` | Spine + search 10-19: nothing (last PR 09-08). ISRG IR 403s WebFetch. **No PR 1 day out is suspect** (Q3'25 call was 10-21 4:30pm EDT) | spine; search | 10-20 |
| **SCCO** | 10-22 | **Stocktitan listing 404s on every try (5th day).** Search 10-19: nothing. Q3'25 call notice was posted the day before (10-28 for 10-29), so no PR is expected before ~10-21 | search; southerncoppercorp.com | 10-21 |
| DOW | 10-22 | Spine 10-19: only the 10-15 dividend PR (Q3'25 call was 10-23 8am). Search found only a TipRanks "confirmed" label (it copies Dover's 10-22) | spine; 8-K | 10-20 |
| WHR, DTE, OSK | 10-28/29 | Not scanned 10-19 (not due). WHR Q3'25 notice was 10-20 for 10-27 | spine | 10-20 |
| DVA | 10-28 | Search 10-19 nothing. Q3'25 notice was 10-13 for 10-29 (now 6 days overdue) | spine; investors.davita.com | 10-20 |
| MKTX, EBAY | 10-28..11-05 | Search 10-19 nothing. MKTX Q3'25 PR was 10-16; **MKTX is under ICE acquisition, so the date may not come**. EBAY has no date (Q2 was 08-05) | spine | 10-20 |
| CNC, GLW | 10-27 | Spine + search 10-19: no Q3 date PR (calendar estimates only: CNC 10-27 8:30am per AJ Bell, GLW 10-28) | spine; search | 10-20 |
| PCAR, PYPL, ST, UPS | 10-27 | Search 10-19: no company PR (PCAR/PYPL/UPS: calendars say 10-27 bmo; ST: Q3'25 notice was 10-14 for 10-28 amc, now overdue) | spine; search | 10-20 |
| **INFY** | 10-23 `amc` | News coverage (upstox/kotakneo/angelone) cites the board filing: meeting 10-22/23, results Fri 10-23. Q2 FY27 times unconfirmed; Q1 FY27 pattern: results ~3:45pm IST (= bmo ET). infosys.com 403s | NSE/BSE filing or infosys.com event page | 10-20 |
| BMRN | 10-26 | Search 10-19 nothing (Q3'25 notice was 10-22 for 10-27). Finnhub says 11-03 | spine | 10-21 |
| **IRDM** | 10-22 `Unknown` | Spine + search 10-19: nothing. **Q2 PR said no conference calls** (pending Rocket Lab deal), so no date PR may ever come; Q3'25 notice was 10-02 for 10-23 | EDGAR 8-K; spine | 10-20 |
| ROKU, CC, COKE, SW | 10-28..11-05 | Search 10-19 nothing (COKE Q2 notice was 07-22 for 08-05; CC Q2 07-23 for 08-04; SW Q2 reported 07-29) | spine; search | 10-21 |
| WBS | — | **Skipped (delisted)**, but the scanner calendar may still carry it. Ben's item | — | — |

## Upcoming Confirmed: locked dates (don't re-research)

One line per confirmed symbol whose date is still ahead (≥ 10-19). **Checked mechanically against
`earnings_upcoming` on 2026-10-18: 160 of 160 rows ↔ DB, 0 date/time mismatches, 0 DB-confirmed rows missing here.**
Pruned 10-18: the 31 rows dated 10-13 → 10-16 (C, DPZ, JNJ, JPM, … TRV), moved verbatim to the fall archive's Appendix A,
which is the pool for the 10-25 source audit. ⚠ **BK still has no `earnings_upcoming` row** (its 10-15 confirm is in that
appendix only; flagged for Ben). **Weakest locks still ahead:** MSCI and GM (10-20, search summaries; GM bmo inferred),
CME (10-21, search summary), ELV and MOH (10-21, biopharmawatch copies), BX (10-22, search snippet of a 403'd page).
Inferred times are marked in each row. Format: `SYM | date | time | source — session`.

| Symbol | Date | Time | Source — session |
|--------|------|------|------------------|
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
| AMX | 2026-10-20 | amc | company 3Q26 call-invitation PDF (q4cdn; text via search summary): release 10-20 after US close, call 10-21 9am Mexico City. Event.svc feed still has no 3Q26 event — 10-19 |
| SPCX | 2026-10-20 | amc | ir.spacex.com PR 10-16: *after market close on Tuesday, October 20, 2026*, webcast 4:30pm ET; 4d lead. **Time was Unknown**; calendars (11-03/11-05) wrong — 10-19 |
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
| RHI | 2026-10-22 | amc | Robert Half PR 10-15 (roberthalf.com press-releases/2026-10-15): ~4:05pm ET, call 5pm. **DB 10-21 was 1d early**; 7d lead — 10-16 |
| WDC | 2026-10-22 | amc | WD PR 10-08 (stocktitan page): *after the market closes*, call 4:30pm ET — 10-13 |
| OMC | 2026-10-22 | amc | Omnicom PR 10-16 (placera copy): *after the NYSE close*, call 4:30pm ET; 6d lead. DB right; finnhub 10-20 wrong — 10-19 |
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
| ARE | 2026-10-26 | amc | Alexandria PRN 08-25 (finviz copy): *after the market closes on Monday, October 26*, call 10-27 2pm ET; 62d lead. **Time was Unknown** — 10-19 |
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
| ITW | 2026-10-27 | bmo | ITW GNW 10-15 (stocktitan page): 7:00am CDT, webcast 9:00am CDT; 12d lead — 10-16 |
| BA | 2026-10-27 | bmo | Boeing PRN 09-30 (stocktitan page): call 10:30am ET; bmo **inferred** (release time not stated) — 10-16 |
| ECL | 2026-10-27 | bmo | Ecolab PR 09-22 (stocktitan page): before the open, webcast 1pm ET — 10-16 |
| HLT | 2026-10-27 | bmo | Hilton PR 09-30 (stocktitan page): before the open, call 9am ET — 10-16 |
| IQV | 2026-10-27 | bmo | IQVIA PR 09-29 (stocktitan page): before the open, call 9am ET — 10-16 |
| JCI | 2026-10-27 | bmo | Johnson Controls PRN 10-01 (stocktitan page): call 8:30am ET; bmo **inferred**. **Time corrected from amc** — 10-16 |
| HOOD | 2026-10-27 | amc | Robinhood GNW 10-01 (stocktitan page): after close, call 5pm ET — 10-16 |
| NXPI | 2026-10-27 | amc | NXP PR 10-06 (stocktitan page): after the Nasdaq close, call 4:30pm EDT — 10-16 |
| ENPH | 2026-10-27 | amc | Enphase GNW 10-06 (stocktitan page): call 4:30pm ET; amc **inferred** from the call time — 10-16 |
| FFIV | 2026-10-27 | amc | F5 BW 10-06/08 (stocktitan page): following the close, call 4:30pm ET — 10-16 |
| FE | 2026-10-27 | amc | FirstEnergy PRN 10-02 (stocktitan page): after close, call 10-28 9am EDT — 10-16 |
| EXR | 2026-10-27 | amc | Extra Space PRN 10-02 (stocktitan page): after close, call 10-28 1pm ET — 10-16 |
| CZR | 2026-10-27 | amc | Caesars PR 10-02 (stocktitan page): after close, no call — 10-16 |
| BXP | 2026-10-27 | amc | BXP BW 09-29 (stocktitan page): after NYSE close, call 10-28 10am ET — 10-16 |
| NOV | 2026-10-27 | amc | NOV PR 09-16 (stocktitan page): after close, call 10-28 10am CT — 10-16 |
| SHW | 2026-10-27 | bmo | Sherwin-Williams PR 10-01 (search summary of finviz copy): *prior to market open*, call 10am ET — 10-19 |
| SOFI | 2026-10-27 | bmo | SoFi PR 09-29 (q4cdn PDF via search): results ~7am ET, call 8am ET — 10-19 |
| SPGI | 2026-10-27 | bmo | S&P Global PR 09-29 (press.spglobal.com): ~7:15am ET, call 8:30am — 10-19 |
| XYL | 2026-10-27 | bmo | Xylem PR 09-29 (finviz copy): 6:55am ET, call 9am — 10-19 |
| RGEN | 2026-10-27 | bmo | Repligen PR 10-13 (finviz copy): *before the market opens*, call 8am ET; 14d lead — 10-19 |
| FCX | 2026-10-27 | bmo | Freeport Q3 operational-update PR 10-02 (stocktitan page): *before the market opens on Tuesday, October 27*, call 10am ET — 10-19 |
| RCL | 2026-10-27 | bmo | Royal Caribbean PR ~10-08 (search summary of finviz copy): call 10am ET; bmo **inferred** (release time not stated) — 10-19 |
| OKE | 2026-10-27 | amc | ONEOK PR 10-05 (search summary of finviz copy): *after the market closes on Oct. 27*, call 10-28 11am ET — 10-19 |
| PPG | 2026-10-27 | amc | PPG BW 09-28 (search): after markets close, call 10-28 8am ET — 10-19 |
| RRC | 2026-10-27 | amc | Range PR 10-06 (search summary of finviz copy): after the NYSE close, call 10-28 9am ET — 10-19 |
| STAG | 2026-10-27 | amc | STAG PR 10-01 (search summary of finviz copy): after close, call 10-28 10am ET — 10-19 |
| STX | 2026-10-27 | amc | Seagate BW 10-13 (search summary of finviz copy): after close, call 5pm ET; 14d lead — 10-19 |
| UHS | 2026-10-27 | amc | UHS PR 10-09 *date and time change* (search summary of finviz copy): after close 10-27, call 10-28 8am ET. Original 10-05 PR said 10-26 — 10-19 |
| V | 2026-10-27 | amc | Visa PR 10-08 (investor.visa.com via search): results after close, webcast 5pm ET — 10-19 |
| WM | 2026-10-27 | amc | WM BW 09-24 (search): after the close, call 10-28 10am ET — 10-19 |
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
| GILD | 2026-10-29 | amc | Gilead PR 10-15 (stocktitan page): after close, webcast 4:30pm ET; 14d lead. Time was Unknown; finnhub 10-22 wrong — 10-16 |
| MDLZ | 2026-10-29 | amc | Mondelēz GNW 10-15 (stocktitan page): 4:05pm ET, call 5pm; 14d lead. finnhub 11-03 wrong — 10-16 |
| EXEL | 2026-10-29 | amc | Exelixis PR 10-15 (stocktitan page): after close, call 5pm ET; 14d lead. finnhub 11-03 wrong — 10-16 |
| GD | 2026-10-30 | bmo | GD PR 10-09 (stocktitan PRN copy): call Fri 10-30 9am EDT; bmo **inferred** from call time — 10-12 |
| XOM | 2026-10-30 | bmo | investor.exxonmobil.com detail/1212 (PR 10-16): release 5:30am CT, call 8:30am CT; 14d lead. **Time was Unknown** — 10-19 |
| NVT | 2026-10-30 | bmo | nVent GNW 10-16 (quiverquant copy): call 9:00am ET; bmo **inferred** (release time not stated). **Time was Unknown** — 10-19 |
| DOC | 2026-11-02 | amc | Healthpeak BW 10-01 (financialcontent copy): after NYSE close Mon 11-02, call 11-03 10am ET. Snapshot 10-22 was stale — 10-02 |
| KHC | 2026-11-04 | bmo | Kraft Heinz BW 10-12 (finviz copy): before the open, Q&A 9am ET. DB right; finnhub 10-27 wrong — 10-15 |
| NVST | 2026-11-04 | amc | Envista PRN 10-06 (finviz copy): call 2pm PT / 5pm ET; amc **inferred** from the call time — 10-15 |
| MAT | 2026-11-05 | amc | Mattel PR 10-15 (stocktitan page): ~4:05pm ET, webcast 5pm; 21d lead. **DB 10-29 was 7d early** — 10-16 |
| KMB | 2026-11-05 | bmo | Kimberly-Clark 8-K ex99.1 10-15 (sec.gov): *final Q3 results Thursday Nov 5*, ~6:30am ET, Q&A 8am. **DB 11-03 was 2d early** — 10-15 |

---

# Research Sessions (newest first)

## Session: 2026-10-19 (Monday) — 07:21 AM ET

40-row queue (15 disputes + 25 unconfirmed). **21 confirmed:** OMC (10-22 amc), SPCX (10-20, time Unknown → amc), AMX (10-20 amc), XOM (10-30, Unknown → bmo), NVT (10-30, Unknown → bmo, inferred), ARE (10-26, Unknown → amc), and 15 of the 10-27 batch: OKE, PPG, RRC, STAG, STX, UHS, V, WM amc; FCX, RCL, RGEN, SHW, SOFI, SPGI, XYL bmo.
Method: one background spine over all 40 (SCCO 404'd a 5th time) plus ~35 WebSearches, one per name, read through finviz/stocktitan/placera copies and the company's own pages (ir.spacex.com, investor.exxonmobil.com, press.spglobal.com, investor.visa.com). The spine found nothing the searches missed.
Date corrections: none. Every confirmed date matched the DB; finnhub was wrong for OMC (10-20). UHS moved its release 10-26 → 10-27 on 10-09 (the first PR is still what some calendars show).
Time inferences: NVT bmo (call 9am only), RCL bmo (call 10am only). AMX: 3Q26 call-invitation PDF is on the company's q4cdn (release 10-20 after close, call 10-21), but the Event.svc feed still has no 3Q26 event, and WebFetch can't read the PDF, so the text came from a search summary of it.
Not resolved: ISRG, DOW, SCCO, IRDM, INFY, CNC, GLW, PCAR, PYPL, ST, UPS (no company PR found), DVA, EBAY, BMRN, MKTX, ROKU, CC, COKE, SW (no PR). INFY: still only news coverage of the board filing. MKTX: under ICE acquisition, don't expect a date. HDB/IBN held for Ben's policy Q2. WHR, DTE, OSK not scanned (next check 10-20).
Process note: `earnings_confirm.py` prints "date unchanged, time unchanged" for rows the DB already had right; that is still a fresh `agent` confirmation. `direct_db_query.py --write` prints "No results returned" on success.

## Session: 2026-10-16 (Friday) — 07:21 AM ET

40-row queue (16 disputes + 24 unconfirmed). **20 confirmed:** RHI (10-21 → **10-22 amc**), GILD (time Unknown → amc), ITW (10-27 bmo), MDLZ and EXEL (10-29 amc), MAT (**10-29 → 11-05 amc**), and 14 of the 10-27 batch: BA, ECL, HLT, IQV, JCI (**amc → bmo**, inferred) bmo; HOOD, NXPI, ENPH, FFIV, FE, EXR, CZR, BXP, NOV amc.
Method: one spine run over 33 symbols (~20 min, background, redirected to /tmp/spine_out.txt), then WebFetch of each stocktitan article page. RHI came from the IR financial-news page (title/date only) plus the dated press-release URL for the body. WebSearch found nothing for DOW, ISRG, OMC, DVA, XOM, NVT, EBAY, INFY, MKTX, CNC, FCX, GLW.
Date corrections: RHI DB 10-21 → 10-22; MAT DB 10-29 → 11-05 (yfinance right, finnhub wrong).
Time inferences: BA bmo (call 10:30am only), JCI bmo (call 8:30am only), ENPH amc (call 4:30pm).
Not resolved: see carry-overs and the unconfirmed table. AMX feed still has no 3Q26 event. HDB/IBN held for Ben's policy Q2. DTE, WHR, OSK, SCCO not scanned this session (spine was not run on them).
Process note: a PreToolUse hook blocks writing .py files, so bookkeeping edits were done with Edit/sed/append on the markdown files.

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

---

# Maintenance History

## Weekly Maintenance — 2026-10-18 (Sunday)

**Archived.** Sessions 09-28 → 10-02 and the 09-27 maintenance entry → new `archive/research_log_2026-Q4_fall-earnings.md`
(fall season). 09-28 → 09-30 are calendar-Q3 days but researched the fall wave, so they went there. I corrected the summer
archive header, which had claimed every calendar-Q3 session. The 31 ledger rows dated 10-13 → 10-16 were pruned, moved
verbatim to the fall archive's Appendix A (the 10-25 audit pool). Active log 787 → ~565 lines, keeping 10-05 → 10-16 in full.

**Ledger check (mechanical, vs `earnings_upcoming`):** 160 of 160 future rows match on date and time, and 0 DB-confirmed rows
≥ 10-19 are missing from the ledger. BK still has no calendar row. OMC's unconfirmed row moved 10-20 → 10-22 since Friday, with no source.

**Source audit #2 (back in time):** 58 summer writes, a census of three weak types; blind subagents; all 12 mismatches re-checked
by me on EDGAR. Report: `analysis/source_audit_20261018.md`.
- Feed/cadence locks (06-30, n=12): **dates 6/12**, times 12/12. New misses: **SNA** (+7), **WAL** (+5, never flagged).
- SEC filing-history times (07-15, n=29): **times 28/29** (UGI: next-morning 8-K filer). Unsourced dates 27/29 (PPL +8, FLY +7).
- Call-time-only inferences (n=12): **times 9/12**. AMTM and UUUU released the evening before a morning call (date −1 too);
  CNP flipped a correct bmo to amc.
- Home-market clocks (n=5): 5/5.

**Promoted.** Cadence rule 6 (a morning call doesn't date the release). New rows: PPL, FLY, UGI, AMTM, UUUU. Rewritten: WAL.
Annotated: CNP, CLF, RTX. SEC timing note: next-morning filers + the 28/29 score. MEMORY.md lines updated; all 21 pointers resolve.

**Calibration, week 10-12 → 10-16.** 5/5 sessions, **80 confirms** (14 / 19 / 12 / 15 / 20) from 200 queue rows (40%).
Date corrections: PNR +7, MAT +7, KMB +2, RHI +1, PII +1, FLS +1. Times: NEM bmo → amc, JCI amc → bmo; DECK, CDNS, GILD Unknown → amc.
- **Calls that held:** TER (finnhub's 10-27 over DB 10-21: right), PNR (overdue PR ⇒ doubt DB 10-20: right, 10-27),
  KMI and RHI (~7d lead ⇒ PR ~10-14/15: right, though RHI's date was 10-22 not the DB's 10-21).
- **Calls that didn't:** "overdue PR" for GILD and MDLZ, whose stored dates held. Overdue-PR doubts now stand at 3 right
  (EQT, WAL, PNR) and 3 wrong (TSCO, GILD, MDLZ), so an overdue PR is a reason to look, not evidence the date is wrong.
- **Rule-6 exposure in last week's writes:** BA (bmo, 10:30am call only) and JCI (bmo, 8:30am call only). Both are safe:
  EDGAR shows same-morning releases (BA 07:30–07:40, JCI 06:57–07:02) on the release day for 5 straight quarters.
  ENPH (4:30pm call ⇒ amc) and NVST (5pm) are afternoon calls, so the rule doesn't apply.
- **Pending:** AMX (still no 3Q26 event as of 10-16), ISRG (10-20), OMC (now 10-22), SCCO, HDB/IBN (now past-dated, Ben's rule).

**Hygiene.** notes_for_ben: audit #1 item archived, replaced by audit #2 + the next-Sunday question; HDB/IBN marked overdue; BK still
open. `rm` of the two 10-15 temp drafts (`memory/mid_tmp.md`, `sess_tmp.md`) was denied, so they're listed for Ben with the
`for_*.md` strays. Inbox root clean. Outbox ≤ 128 lines, no rotation. **STATUS.md** rewritten.

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
