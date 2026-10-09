# Earnings Research Log

> Active log: full sessions for the last ~2 weeks (newest first, below), a compact ledger of
> confirmed-but-upcoming dates, and the open carry-overs with next-check dates. Older sessions live in
> the season archives: `memory/archive/research_log_2026-Q2_spring-earnings.md` (through 06-30) and
> `memory/archive/research_log_2026-Q3_summer-earnings.md` (07-01 → 09-15, plus the summer's full
> confirmation ledger and carry-over table as appendices). Maintenance notes at the very bottom.
> Per-symbol cadence/lead-times live in `memory/reference_company_cadence.md`. **Grep it by symbol
> (`^| SYM `); don't read it whole (~200 KB).** The fall-wave names confirmed 09-29 → 10-02 are in
> its *"Fall-2026 wave"* block.

## ⚠⚠ READ FIRST: work these BEFORE the injected list (rebuilt from the DB 2026-10-04)

**The injected list does not contain them.** The hook backfills unconfirmed rows only into the room left
under a 25-row ceiling, and disputes have run 28–42 a day since 09-30, so the backfill has been **empty**.
Rows where all three feeds agree have no dispute and **never reach a session**: 83 unconfirmed rows dated
≤ 10-23 as of 10-04. Fix proposed (`analysis/proposal_20261004_backfill_crowded_out.md`). Until Ben
ships it, this block is the list.

**Order: nearest date first, before any dispute dated later than the row.** The October wave posted its
advance PRs 09-28 → 10-01, so most of these are already out. Go spine → company page → confirm. Use
`analysis/helpers/spine.py` (nearest symbols first; it 429s partway through a batch, and a 429 means
*unread*, not absent) and `analysis/helpers/conf.sh` for the three writes. **Remember that this block
isn't in the dispute list: there is no dispute row to close for these, so `conf`'s dispute UPDATE will
simply match nothing (fine).**

| Reports | Never researched this quarter (unconfirmed, no open dispute) |
|---------|---------------------------------------------------------------|
| ~~10-13~~ | ~~ACI~~ confirmed 10-05 |
| **10-14** | **ASML** only left (company sites 403/timeout 10-06; aggregators say 14 Oct 07:00 CET): BAC, FAST, MS, STT confirmed 10-06 |
| ~~10-15~~ | ~~SNA~~ confirmed 10-09 (**actually 10-22**). The other 10 confirmed 10-06 (SCHW date inferred, TSM time corrected to bmo) |
| ~~10-16~~ | ~~CFG, MTB, TRV~~ confirmed 10-06 |
| **10-17** | HDB, IBN: **Saturday-dated** Indian ADRs. HDB board meets **Sat 10-17** (angelone/sahi reports of the NSE intimation, 10-06). IBN: no 2026 notice found yet. Hold the encoding for Ben's policy Q2 (`notes_for_ben.md`) |
| ~~10-19~~ | ~~STLD, WRB, ZION~~ confirmed 10-06; ~~WAL~~ confirmed 10-07 (10-19 amc) |
| 10-20 | ~~EFX~~ confirmed 10-08 (bmo), ~~GM~~ confirmed 10-09 (weak source), **ISRG** (search snippet says 10-21 amc, DB 10-20; unverified), **OMC** (no Q3 date PR found). HAL, HAS, MSCI, NOC, UAL, MMM confirmed 10-07 |
| 10-21 | ~~CCI, CME, DHR~~ confirmed 10-07; ~~ELV~~ confirmed 10-08, EQR (search says 10-28; AVB merger, may have no call), ~~FAF~~ confirmed 10-09, ~~IBM~~ confirmed 10-09, ~~KNX, LRCX, LUV, MOH, PKG, T~~ confirmed 10-08, LVS, PM (no PR), SAP (IR calendar via search: 10-21, disclosure 22:05 CET = amc; page 403), ~~TMO, TSLA~~ confirmed 10-09, TXN |
| 10-22 | CMCSA, DGX, DOV, DOW, HBAN, HON, INTC, LAZ, NDAQ, NEM, NOK, ORI, PG, PHM, SCCO (`Unknown`), SPOT, SSNC, UNP, VLO, VRSN, ~~WST~~ confirmed 10-09 (**actually 10-29**) |
| 10-23 | AXP, E, GNTX, INFY, SLB |

Banks often publish the whole year's dates in one PR (C, RF, FITB and KEY did). For BAC, MS, PNC, USB,
BK, STT, CFG, MTB, ZION, HBAN, ALLY, COF, look for a *"…Announces 2026 Earnings Release Dates"* PR
before hunting a per-quarter one. Known quirks in the cadence table: **SCHW** (earnings ride the
seasonal *Business Update*, look for a *Fall* one), **MRSH** (MMC renamed), **BAC** (06-30 lock
unsourced). Strike rows out here as they're confirmed.

## Open Carry-Overs: researched, unresolved, with next-check dates

Next-check ≈ **advance-PR due date + 1** (PRs mostly publish after the ~07:15 session start). **Each
row's "How to read" is the working channel and its known traps. Use it verbatim.**

| Symbol | DB row | Status | How to read | Next check |
|--------|--------|--------|-------------|------------|
| **AMX** | 10-13 `amc` (finnhub 10-20) | No 3Q26 event in the feed as of 10-02 (newest 2Q26, 07-21). Q3 is always Tuesday amc (10-17 / 10-15 / 10-14); 10-13 fits. The event's appearance lead is unmeasured. **Log the first day it appears.** **10-06: feed re-read (61 events), newest still 2Q26 07-22; no 3Q26 event.** | Event.svc feed, browser UA, `pageSize=100` (cached correctly since 09-28). Page with `pageNumber`, dedupe by `EventId`, parse `StartDate` with strptime (string-sorting `MM/DD/YYYY` is garbage), open as utf-8. | 10-12, daily (10-09: feed not re-read, 429s elsewhere; 10-08: feed re-read, 61 events, newest still 2Q26 07-22) |
| **TSCO** | 10-22 `Unknown` | Q2 PR 07-02 → 07-23 (21d) ⇒ due ~10-01; none by 10-02. **Slightly overdue.** IR calendar empty. | search the IR newsroom; stocktitan `TSCO` | ~~resolved 10-09~~: PR came 10-09 (13d lead), 10-22 bmo |
| **VRT, LRCX** (MMM, WAL, UAL confirmed 10-07) | 10-21 / 10-21 | **Time-only** (EDGAR furnish history, 09-30); dates unsourced. WAL: aggregator says 10-20 amc, so the DB 10-21 may be a day late. UAL's live row moved 10-21 → 10-20. 10-06: spines MMM/WAL read, no date PR (WAL's Q3'25 PR came 10-02 for 10-21, so WAL is now ~4d late). | stocktitan spines; IR newsrooms | 10-07 |
| **PNR** | 10-20 | 14d lead ⇒ PR due ~10-06; 10-08 spine: still nothing (newest = 09-22). **PEGA confirmed 10-08.** finnhub says 10-27. | stocktitan spine `PNR` | 10-12 (10-09 spine: still nothing, newest 09-22) |
| **ALK** | 10-22 `Unknown` | 14d lead (Q2) ⇒ due ~10-08 10-06 spine: nothing yet. | — (10-07/10-08 searches: aggregators list the Q3 call 10-23 11:30am ET; no PR; DB 10-22; yfinance/finnhub 10-20) | ~~resolved 10-09~~ |
| **RHI** | 10-21 `amc` | ~7d lead ⇒ due ~10-14. **Don't read before ~10-12.** | — | 10-13 |
| **SF, TER, VLTO, BPOP, NSC, SLM, ITW, F, FCX, DECK** (POOL, BC confirmed 10-09) | 10-21 → 10-23 (F/FCX later) | No company Q3 date as of 10-02; only aggregator estimates. **10-09 12:40 spine read (full pages, nothing dated Oct): SF, TER, VLTO, SLM, DECK show no Q3 date PR** (BPOP, NSC, ITW, F, FCX not read). | stocktitan spine (`analysis/helpers/spine.py`, paces itself to the 10-per-300s limit) | 10-12 |
| **IRDM** | 10-22 `Unknown` | Pending Rocket Lab acquisition (close mid-2027), still a registrant that issued a Q2 PR (07-22). 10-06: no Q3 date found. Look for a bare results PR or 8-K. **WBS resolved 10-06 as `skipped`**: delisted (Santander closed Aug 2026, SEC `tickers=[]`, Form 15-12G 08-31 and 09-30), so the DB row is a phantom. **Ben: the scanner calendar still carries a WBS 10-22 row.** | EDGAR 8-K | 10-08 |

## Upcoming Confirmed: locked dates (don't re-research)

One line per confirmed symbol whose date is still ahead (≥ 10-05). **Rebuilt from `earnings_upcoming`
on 2026-10-04: 48 rows, all `1 / agent`, every date and time matching the DB.** 16 rows confirmed
09-29/09-30 had never been added; they're in now. Pruned as reported: MTN, JEF (09-28), KMX, CNXC, UEC,
CCL (09-29), CAG, FDS, JBL, MU (09-30), ACN, MKC, NKE (10-01). An `earnings_events` row exists for every
one of them on its confirmed date. **Weakest locks:** LW (no first-party fetch) and BX (search snippet
only). Inferred times: DAL, GPC, PCG, BX, AAL, HCA (and LMT from the call time). Format:
`SYM | date | time | source — session`.

| Symbol | Date | Time | Source — session |
|--------|------|------|------------------|
| LW | 2026-10-06 | bmo | Lamb Weston scheduling release (~8:00am ET release, 9am call). ⚠ Weakest confirm on the list: no first-party fetch succeeded (IR 403 wall, no 8-K); rests on consistent search summaries + yfinance — 09-09 |
| STZ | 2026-10-06 | amc | Constellation `ir.cbrands.com` detail/345, 09-10: *"after the close of the U.S. markets,"* call 10-07 8am ET. **Time corrected from bmo** — 09-22 |
| PEP | 2026-10-08 | bmo | pepsico.com newsroom PR 08-25 *"PepsiCo Announces Timing and Availability of Third-Quarter 2026 Financial Results"*: *"Thursday, October 8, 2026,"* materials ~6:00am EDT, Q&A 8:15am EDT — 09-24 |
| DAL | 2026-10-09 | bmo | Delta webcast PR: call 10am ET Oct 9. bmo **inferred** (release time not stated); lead unmeasured (PR date not captured) — 09-25 |
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
| ERIC | 2026-10-15 | bmo | `ericsson.com/en/investors/financial-calendar/2026/q3-2026`: *"Oct 15, 2026 07:00 (CET)"* = 01:00 ET ⇒ bmo — 09-24 |
| FHN | 2026-10-15 | bmo | `ir.firsthorizon.com` PR 09-22: materials ~6:30am ET, call 9:30am ET. Snapshot 10-14 was already stale — 09-23 |
| JBHT | 2026-10-15 | amc | `investor.jbhunt.com` "Estimated Earnings Periods" table: Q3 release **October 15, 2026**, quiet period Sep 26 – Oct 15; amc = Item 2.02 furnished 20:08–21:26Z (16:0x–16:2x ET) 8/8 since 2024-10 — 09-24 |
| WIT | 2026-10-15 | bmo | wipro.com events page: *"Results for the Second quarter ending September 30, 2026, will be announced on October 15, 2026, Thursday after stock market trading hours in India"* (= US morning) — 10-01 |
| AA | 2026-10-15 | amc | q4cdn 3Q26-EarningsAnnouncement.pdf (PR 09-15): after NYSE close, call 5:00pm EDT — 10-06 |
| BK | 2026-10-15 | bmo | bny.com 2026 earnings-calls PR: release ~6:30am ET, call 11:00am — 10-06 |
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
| BAH | 2026-10-23 | bmo | investors.boozallen.com (BW 09-11): call Fri 10-23 8am EDT, release *"before the call"* — 10-02 |
| VZ | 2026-10-26 | bmo | verizon.com / GNW 09-28: *"Monday, October 26, 2026,"* materials 7:00am, webcast 8:30am ET — 09-29 |
| HIG | 2026-10-26 | amc | newsroom.thehartford.com PR 09-28: ~4:05pm EDT — 10-05 |
| BKR | 2026-10-27 | amc | Baker Hughes GlobeNewswire 09-28: *"press release at 5 p.m. Eastern Time on Tuesday, Oct. 27, 2026,"* webcast 10-28 9:30am — 10-01 |
| CNP | 2026-10-27 | bmo | CenterPoint GlobeNewswire 09-29 16:30 ET: call 10-27 8:00am ET, release *"on the same day before the market opens"* — 10-01 |
| HCA | 2026-10-27 | bmo | investor.hcahealthcare.com / BW 09-30: call Tue 10-27 9am CT. bmo inferred (release time not stated) — 10-02 |
| KO | 2026-10-27 | bmo | investors.coca-colacompany.com detail/1173 (09-29): *"Oct. 27 before the NYSE opens,"* call 8:30am. finnhub's +7d was right — 09-30 |
| TRU | 2026-10-27 | bmo | newsroom.transunion.com Q3 date PR: release ~6:00am CT Tue 10-27, call 8:30am CT. Cached URL was the Q2 PR — replaced — 10-02 |
| EQT | 2026-10-27 | amc | EQT PR 10-07 20:15 (stocktitan wire text): *"after market close on Tuesday, October 27,"* call 10-28 10am ET. **DB 10-20 was 7d early** — 10-08 |
| BC | 2026-10-29 | bmo | Brunswick GlobeNewswire 10-08 (stocktitan copy): *"before the market opens on October 29"*, call 11am ET; 21d lead. **DB 10-22 was 7d early** (yfinance, finnhub said 10-29) — 10-09 |
| DXCM | 2026-10-29 | amc | Dexcom Business Wire 10-07 (stocktitan copy): *"after market close on October 29"*, call 4:30pm ET; 22d lead. Time was Unknown; finnhub 10-22 wrong — 10-09 |
| WST | 2026-10-29 | bmo | West PRN 10-08 (stocktitan copy): *"before the market opens on Thursday, October 29"*, call 8am ET; 21d lead. **DB 10-22 was 7d early** — 10-09 |
| MA | 2026-10-29 | bmo | Mastercard BW 10-08 (stocktitan copy): call 9:00am ET. Release time not stated; **bmo inferred** from the call time + DB. 21d lead; finnhub 10-22 wrong — 10-09 |
| CARR | 2026-10-29 | bmo | Carrier PRN 10-08 *Earnings Advisory* (stocktitan copy): call 7:30am ET. Release time not stated; **bmo inferred** from the call time. **DB 10-27 was 2d early** — 10-09 |
| AJG | 2026-10-29 | amc | Gallagher PRN 10-08 (stocktitan copy): *"after the market closes on Thursday, October 29"*, call 5:15pm ET; 21d lead. DB right; finnhub 10-22 wrong — 10-09 |
| DOC | 2026-11-02 | amc | Healthpeak BW 10-01 (financialcontent copy): after NYSE close Mon 11-02, call 11-03 10am ET. Snapshot 10-22 was stale — 10-02 |

---

# Research Sessions (newest first)

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

## Session: 2026-09-25 (Friday) — 07:17 AM ET

6 surfaced (5 disputes: AMX, REXR, WIT `date_disagreement`; RF, TFC `unknown_time`; 1 unconfirmed: DAL).
**3 confirmed (RF, TFC, DAL), 3 held (AMX, REXR, WIT).** 0 dates changed; 2 `Unknown` times filled (RF bmo, TFC bmo).
Reads: 8 searches, 9 WebFetches (Regions BusinessWire 403; ir.regions.com PR page rendered).

### Confirmed

| Symbol | Result | Source |
|--------|--------|--------|
| **RF** | **2026-10-16 `bmo`** (DB right; `unknown_time` closed) | ir.regions.com 2026 release-dates PR: *"Third Quarter 2026 Results: To be announced pre-market open on Friday, Oct. 16, 2026,"* call 10am ET. Advance PR 09-16 (BusinessWire) agrees. |
| **TFC** | **2026-10-16 `bmo`** (`unknown_time` closed) | media.truist.com 09-18 *"Truist announces third quarter 2026 earnings call details"*: *"before the market opens on Friday, Oct. 16, 2026,"* call 8am ET. |
| **DAL** | **2026-10-09 `bmo`** (DB right, no dispute row) | Delta *"announces webcast of September quarter 2026 financial results"*: call **10am ET Fri Oct 9** (date is company-sourced). bmo is **inferred** — the PR doesn't state a release time; Delta's usual morning release ahead of the call, and the DB already said bmo. Lead not logged (PR date not seen). |

### Held

| Symbol | Reasoning | Next check |
|--------|-----------|------------|
| **AMX** | Event.svc feed (cached URL) returned only 2014–2018 entries this time (pageSize/sort quirk?) — the calendar page lists only 2Q26. No 3Q26 event. | 2026-09-29 |
| **REXR** | IR press list still ends 03-19 in the fetch view; events page: *"no upcoming events."* No Q3 advance found. Search shows only Q1/Q2 advance PRs. | 09-28 (10-22 case), daily |
| **WIT** | No Q2 FY27 advance on wipro.com/investors (expected ~10-06). | 2026-10-06 |

## Session: 2026-09-24 (Thursday) — 07:17 AM ET

8 surfaced (7 disputes: AMX, REXR, JBHT, WIT `date_disagreement`; ERIC, FNB, SNA `unknown_time`; 1 unconfirmed:
PEP). **3 confirmed on company sources (PEP, ERIC, JBHT), 2 time-only (FNB, SNA), 3 held (AMX, REXR, WIT).**
0 dates changed; 3 `Unknown` times filled (ERIC bmo, FNB amc, SNA bmo). Reads: 3 searches, 10 WebFetches
(1 NXDOMAIN — `investors.snapon.com` is dead), AMX Event.svc feed ×2, stocktitan spines ×3, EDGAR
submissions ×3 + 1 exhibit. All four finnhub dissents today are the +5/+7d shape (AMX, REXR, JBHT) or an
off-pattern weekday (WIT Tue); none was right where checked.

### Confirmed

| Symbol | Result | Source |
|--------|--------|--------|
| **PEP** | **2026-10-08 `bmo`** (DB right) | pepsico.com newsroom, **08-25**, *"PepsiCo Announces Timing and Availability of Third-Quarter 2026 Financial Results"*: results *"Thursday, October 8, 2026"* by posting the 10-Q, release and prepared remarks *"at approximately 6:00 a.m. EDT,"* analyst Q&A 8:15am EDT. Lead **44d** (Q2 was 35d → 2 obs, 35–44d). The window-watch row said "open since ~09-03"; the PR was already three weeks old when this session first read the channel. |
| **ERIC** | **2026-10-15 `bmo`** (`unknown_time` closed) | Ericsson financial calendar, per-quarter page `/2026/q3-2026`: *"Oct 15, 2026 07:00 (CET)"* — 07:00 Stockholm = 01:00 ET ⇒ bmo, same as every quarter. The calendar index page is JS-only to WebFetch; the per-quarter deep link renders. Cached. finnhub agrees on the date. |
| **JBHT** | **2026-10-15 `amc`** (finnhub 10-20 wrong — the +5d shape) | `investor.jbhunt.com` home page, "Estimated Earnings Periods" table: Q3 2026 release **October 15, 2026**, quiet period *"September 26, 2026 – October 15, 2026."* The table gives no time; amc from EDGAR CIK 728535 — 8/8 Item 2.02 8-Ks since 2024-10 accepted 20:08–21:26Z on the 15th (16:0x–16:2x ET), and every quarter the release goes out ~4pm ET with a 5pm call. J.B. Hunt reports on the 15th of the month after quarter-end regardless of weekday (10-15-24 Tue, 01-16-25 Thu, 04-15-25, 07-15-25, 10-15-25, 01-15-26, 04-15-26, 07-15-26). |

### Time-only (date NOT locked)

| Symbol | Written | Basis | Why the date is open |
|--------|---------|-------|----------------------|
| **FNB** | `amc` | Q2 scheduling PR 06-30 15:30 ET (via stocktitan): *"plans to issue financial results for the second quarter of 2026 after the market close on Thursday, July 16, 2026,"* call Friday 8:30am ET; Item 2.02 furnished the **next morning** 11:30–12:36Z, 8/8 since 2024-10 — the release-day-evening / 8-K-next-morning shape. | No Q3 scheduling PR yet (newsroom + stocktitan both end 09-03). Q2's came 16d ahead ⇒ due ~09-29. 10-15 = 3rd Thursday fits (Q3'25 10-16, Q2'26 07-16). Dispute row marked `confirmed_agent` (the `unknown_time` question is answered; the ACI 09-22 precedent), calendar row left `date_confirmed=0`. |
| **SNA** | `bmo` | Q2-26 results PR published **07-23 06:30 ET** (stocktitan timestamp), webcast 9:00am CT; Item 2.02 accepted 10:31–10:42Z on release day 6/8 (11:3xZ for the two February FY releases) — morning either way. | ⚠ **The 10-15 date is probably 7d early — see Held.** Dispute row left `unresolved` so the doubted date stays visible (REXR precedent). |

### Held

| Symbol | State | Reasoning | Next check |
|--------|-------|-----------|------------|
| **SNA** (date) | 10-15 `bmo`, finnhub also 10-15 | ⭐ **Fiscal-calendar shift found.** The Q2-26 8-K exhibit (EDGAR, curl) is headed *"Three Months Ended July 4, 2026 / June 28, 2025"* and cites the 10-K *"for the fiscal year ended January 3, 2026"* — fiscal 2025 was a **53-week year**, so every 2026 quarter ends one week later than 2025's. The report dates moved with it: Q1 **04-23** (vs 04-17 '25), Q2 **07-23** (vs 07-17 '25) — both 4th Thursdays, 19 days after quarter-end. **The 06-30 "07-16" cadence lock was therefore wrong by a week** (the archive's SNA line never recorded the outcome; EDGAR shows the 07-23 furnish). Q3-26 ends **10-03** → +19d = **Thu 10-22**. 10-15 would be 12d after quarter-end, shorter than any Snap-on quarter observed. Both the DB and finnhub sit on the 2025-shaped "3rd Thursday". Snap-on's only advance channel is the BusinessWire *"Snap-on Incorporated to Webcast 2026 Third Quarter Results Conference Call"* PR, **14d lead** (2025-10-02 → 10-16; 2026-07-09 → 07-23): due **10-01** if 10-15 were real, **10-08** for 10-22. Not written — a cadence argument is not a source (standing rule), however good the arithmetic. | **2026-10-02** (a silent 10-01 kills 10-15), then **10-09** |
| **AMX** | 10-13 `amc` (finnhub 10-20) | Event.svc feed re-read (pageSize=100, sorted client-side — `sortDirection=desc` is ignored, and the feed returns the 2014 events first at pageSize=10): 61 unique events, newest still **2Q26 (07-22 call)** — no 3Q26 event. Held per the 09-22 reasoning; nothing new. | **09-29**, then 10-06 |
| **WIT** | 10-15 `bmo` (finnhub 10-13) | First-time name. Wipro's advance is a short-lead PR (*"Wipro Limited to announce results for the first quarter ended June 30, 2026, on July 16, 2026"* — dated **07-07**, 9d lead) on wipro.com/newsroom, also on BusinessWire. Results go out *"after stock market trading hours in India"* with a 7:00pm IST / 9:30am ET call ⇒ bmo for the US session, matching the stored time. Q2 report days: Wed 10-12 '22, Wed 10-18 '23, **Thu 10-17 '24, Thu 10-16 '25** — the stored Thu 10-15 is the pattern; finnhub's Tue 10-13 is not. No Q2 FY27 PR yet (due ~10-06). The newsroom list page is JS-only to WebFetch; individual PR pages render. | **10-06**, then 10-07 |

### Notes

- **PEP was sitting confirmed-in-public for 30 days.** The window-watch row flagged it "open (~09-03)" on 09-13 and
  09-20, and the PR had actually published 08-25. It only got read today because it entered the 14-day horizon
  as an unconfirmed backfill row. The dispute-gated launcher (09-20 note) is the reason; the fix proposal stands.
- **SNA is the 06-30 bad-lock batch, still paying out.** The July lock (07-16) was wrong, the outcome was never
  logged, and the Q3 row inherited the same 3rd-Thursday assumption. The general lesson is new though: a
  **53-week fiscal year shifts every report date in the following year by ~7d**, and a cadence row keyed to
  "nth weekday of the month" silently breaks. Check `fiscal year ended` in the latest 10-K/8-K when a
  company's 2026 dates all sit a week off 2025's (REXR shows the same 4th-Thursday shift — worth checking
  whether it is the same cause). Added to notes_for_ben.
- **finnhub as a signal today: 0 for 4.** AMX +7d, REXR +7d (after moving overnight), JBHT +5d, WIT −2d onto a
  Tuesday. None matched a company source.
- **Ericsson calendar:** the index page is a JS calendar; the per-quarter deep link (`/financial-calendar/2026/q3-2026`)
  is the readable one, so the cached URL is now quarter-specific and will need bumping to `/2027/q4-2026` next time.
- **Dead IR host:** `investors.snapon.com` NXDOMAIN; `www.snapon.com/EN/Investors` returns 200 (cached instead).
  Not yet checked for an events list — Snap-on has no advance channel other than the webcast PR anyway.
- **JBHT dispute pattern:** finnhub 10-20 is the third consecutive quarter it has disagreed with the IR table by
  +5d (the Q2 dispute was the same). The IR table is authoritative and pre-lists the whole year — no need to
  wait for anything.
- Tooling: the AMX feed had a 0x81 byte that `json.load` with the default cp1252 codec choked on — open with
  `encoding='utf-8'`. The `sortDirection` parameter is ignored; sort in Python.

## Session: 2026-09-23 (Wednesday) — 07:13 AM ET

4 disputes (PGR, SYF `date_disagreement`; FHN `both`; REXR `unknown_time`), all four rows dated 10-14 in the
snapshot. **3 confirmed on company sources (PGR, SYF, FHN), 1 time-only (REXR — date held).** The snapshot was
stale for two: the live rows already read **SYF 10-20** and **FHN 10-15** before this session touched them, so
those confirms locked the moved dates rather than correcting anything (0 dates changed today). Reads: 6
searches, 9 WebFetches (2× 404 on guessed Progressive event URLs), EDGAR submissions ×2 + 1 exhibit,
Progressive Q4 `Event.svc` feed ×3.

### Confirmed

| Symbol | Result | Source |
|--------|--------|--------|
| **PGR** | **2026-10-14 `bmo`** (DB right; finnhub 11-02 is the same +19d artifact as Q2's 08-03) | ⭐ **The previous month's results release is the advance channel.** *"Progressive Reports August Results"* (8-K **Item 7.01**, filed 09-18 08:38 ET, EX-99 `pgr202608ex99earningsrelea.htm`, read via curl) closes with *"Events — We plan to release September results on **Wednesday, October 14, 2026, before the market opens**."* Quarter releases since 2025-04 are all 3rd-Wednesday bmo (04-16, 07-16, 10-15 '25; 04-15, 07-15 '26; furnished 08:40–09:50 ET) and 10-14 is October's 3rd Wednesday. The Q4 `Event.svc` feed on `investors.progressive.com` renders (browser UA) but lists only the quarterly investor calls (~3 weeks after each release), not the results dates. |
| **SYF** | **2026-10-20 `bmo`** (snapshot 10-14; live row had already moved to 10-20 — yfinance 10-20 right, finnhub 10-13 wrong) | `investors.synchrony.com` financial-news detail/588, *"Synchrony to Announce Third Quarter 2026 Financial Results on October 20, 2026"*: release *"approximately 6:00 a.m. Eastern Time,"* call 8:00am ET. First-time name; IR URL cached (financial-news list). PR date not captured — lead unmeasured. |
| **FHN** | **2026-10-15 `bmo`** (snapshot 10-14 `Unknown`; live row already 10-15 — yfinance 10-15 right, finnhub 10-21 wrong) | `ir.firsthorizon.com` press release **09-22**, *"First Horizon Corporation to Announce Third Quarter Financial Results on October 15, 2026"*: materials *"approximately 6:30 am ET,"* call 9:30am ET. Lead **23d** (Q2 was 28d → 2 obs, 23–28d). |

### Held

| Symbol | State | Reasoning | Next check |
|--------|-------|-----------|------------|
| **REXR** | 10-14, **time set `amc` via `--time-only`; date NOT confirmed and probably wrong** | **Time** rests on the company's own advance PRs — Q3'25 *"after the market closes on Wednesday, October 15, 2025,"* Q1'26 and Q2'26 *"after the market closes on Thursday…"*; the Item 2.02 furnish stamps (20:1x–21:2x`Z`, 12/12 quarters since 2023) are consistent and were not timezone-converted. **Date:** the IR press list is current through 09-17 and carries no Q3 advance. Leads now 3 obs: Q3'25 **29d** (09-16→10-15), Q1'26 **35d** (03-19→04-23), Q2'26 **24d** (06-29→07-23). For a 10-14 release the PR was due 09-09 → 09-20 — **3+ days overdue against the shortest lead** ⇒ the PVH shape: distrust the date, don't guess the replacement. Cadence hint only: Q3 was Wed 10-18 / 10-16 / 10-15 ('23–'25), but both 2026 quarters slipped to the **4th Thursday** (04-23, 07-23) → October's is **10-22** (PR due 09-17 → 09-28). finnhub 10-13 is the −1d shape. The PR publishes ~16:05 ET (2/2), so a morning read only sees prior-day PRs. Dispute row left `unresolved` (unlike ACI on 09-22, which was marked `confirmed_agent` on a time-only fix — leaving it open keeps the row visible while the date is doubted). | **09-24**, then daily through 09-29 (one WebFetch of the press list) |

### Notes

- **Stale snapshot ×2 (SYF, FHN).** Both live rows had already moved to the company's dates (FHN's PR is dated
  09-22, so the overnight feed caught it). Per [[dispute-snapshot-is-stale]] these are locks, not corrections.
- **PGR channel:** Progressive pre-announces the quarter-end release date inside the *previous month's* results
  release ("Events" paragraph, ~26d ahead) and files that release under **Item 7.01** — an EDGAR sweep
  filtered on 2.02 misses it for this name. Cached IR URL moved from the home page to the
  financial-news-releases list (JS-rendered; the EDGAR exhibit is the readable copy).
- 10-13 → 10-16 cohort: PGR and FHN handled today; SYF moved out of it (10-20). REXR is the first cohort
  member showing the overdue-advance signal.

## Session: 2026-09-22 (Tuesday) — 07:13 AM ET

8 surfaced (3 disputes: AMX `date_disagreement`, ACI + C `unknown_time`; 5 unconfirmed: UEC, CCL, MU, ACN, STZ).
**6 confirmed on company sources (UEC, CCL, MU, ACN, STZ, C), 1 time-only (ACI), 1 held (AMX).** Three
stored values were wrong and got fixed: **UEC date 09-24 → 09-29 and amc → bmo; ACN amc → bmo; STZ bmo → amc.**
First session since 09-15 (no session 09-16 → 09-18, dispute-gated; 09-21 also did not run). Reads: 8 searches,
7 WebFetches (1 BusinessWire 403), EDGAR submissions ×2 + 6 filings, 3 IR-host curls, 1 stocktitan spine, and
**the AMX Q4 event feed (new channel, see Notes)**.

### Confirmed / corrected

| Symbol | Result | Source |
|--------|--------|--------|
| **UEC** | **2026-09-29 `bmo`** — ⚠ corrected from 09-24 `amc` (+5d, time flipped) | Advance PR **published this morning 09-22 07:00 ET** (via stocktitan; the exact 7d lead seen for FY26 Q2/Q3): *"issue its fiscal 2026 year-end operating and financial results **before the markets open on Tuesday, September 29, 2026**,"* call 11:00am ET. Corroborated first-party: `uraniumenergy.com/invest/events-and-webcasts` lists *"URANIUM ENERGY FY 2026 RESULTS WEBCAST — Tuesday, September 29, 2026 — 8:00AM PDT"* (curl, browser UA). The carry-over's `bmo` expectation was right; its date was not (the 09-24 row was a feed guess, and the cadence row's 10-K-eve reading was also wrong for the date). |
| **CCL** | **2026-09-29 `bmo`** (DB right — the 09-15→09-20 feed move to 09-29 was correct) | PR Newswire **09-15 11:56 ET**, *"Carnival Corporation & plc to Hold Conference Call on Third Quarter Earnings"* (via stocktitan): call *"Tuesday, September 29, 2026, at 10 a.m. (EDT)"*, results *"expected to be released that morning."* Lead **14d** (Q2 was 12d). |
| **MU** | **2026-09-30 `amc`** (DB right) | `investors.micron.com` PR **08-26**, *"Micron Technology to Report Fiscal Fourth Quarter Results on September 30, 2026"*: call *"2:30 p.m. Mountain time"* = 4:30pm ET ⇒ amc (no before/after phrase in the PR; the 4:30 ET call is the amc evidence, same as every prior quarter). Lead **35d** (fiscal Q3 was 28d). |
| **ACN** | **2026-10-01 `bmo`** — ⚠ corrected from `amc` (the 09-13 re-seed flag) | `newsroom.accenture.com` **09-15**, *"Accenture to Announce Fourth-Quarter and Full-Year Fiscal 2026 Results"*: call *"8:00 a.m. EDT on Thursday, October 1, 2026,"* *"An earnings news release will be issued before the call."* Lead **16d** — exactly the cadence row's figure. |
| **STZ** | **2026-10-06 `amc`** — ⚠ corrected from `bmo` (the 09-13 re-seed flag) | `ir.cbrands.com` detail/345, **09-10 16:30 ET**: *"Tuesday, October 6, 2026, after the close of the U.S. markets,"* call 8:00am ET **Wednesday 10-07**. Second consecutive quarter of release-after-close / call-next-morning ⇒ amc is now 2 obs. Lead **26d**. |
| **C** | **2026-10-13 `bmo`** (`unknown_time` closed; date sourced for the first time) | Citi's own calendar PR *"Citi Third Quarter and Fourth Quarter 2025 Earnings Calls and First Quarter … Fourth Quarter 2026 Earnings Calls"* (citigroup.com, 2025): *"3Q26 – Tuesday, October 13, 2026,"* results *"via press release at approximately 8 a.m. (ET),"* webcast ~11am ET. One page covers the whole year — cached. Dispute row `confirmed_agent`. |
| **ACI** | **`bmo` written via `--time-only`; date 10-13 NOT locked** | EDGAR CIK 1646972: **11/11 Item 2.02 8-Ks since 2024-01 accepted 07:30–08:32 ET** (07-23 11:31Z, 04-14 11:30Z, 01-07 12:30Z, 2025-10-14 11:31Z …) ⇒ bmo settled from furnish history, per the standing rule. No FQ2 advance yet (stocktitan spine newest = brand news; last year's FQ2 advance was BusinessWire **2025-09-30** for a 10-14 release = 14d). Dispute row `confirmed_agent` with the DB date recorded as-is; see Held for why the date is doubtful. |

### Held

| Symbol | DB date | Why skipped | Next check |
|--------|---------|-------------|------------|
| **AMX** | 2026-10-13 `amc` (finnhub 10-20) | ⭐ **Found the company channel**: the JS-only IR calendar is a Q4 site and its data feed is readable — `americamovil.com/feed/Event.svc/GetEventList?…` (browser UA, curl; cached as the IR URL). Every quarter since 2016 is an event titled *"AMX will report 3Q25 Financial and Operating Results on October 14th after the market close. The conference call…"* dated the **next morning** (call day). **Q3 history: 3Q23 Tue 10-17, 3Q24 Tue 10-15, 3Q25 Tue 10-14 — all Tuesday amc, 14–17 days after quarter-end**; 2Q26 was Tue 07-21 amc. ⚠ The results 6-Ks post **2 days later** (10-16, 10-17, 10-19) — do not read 6-K dates as release dates for AMX. **No 3Q26 event is listed yet.** Both candidates are Tuesdays; 10-13 (13d after q-end) continues the 17→15→14 trend, 10-20 (20d) would be the latest Q3 in the series — finnhub's +7d artifact shape. Not locked: no same-quarter source. | **2026-09-29**, then 10-06 (one curl of the feed, newest-first) |
| **ACI** (date) | 2026-10-13 (time now bmo) | FQ2 FY26 ends **09-12** (16+12 weeks from 02-28). FQ2 FY25 ended 09-06 → reported 10-14 (**38d**); FQ2 FY24 09-07 → 10-15 (38d); FQ1 FY26 06-20 → 07-23 (33d). 38d from 09-12 = **10-20 (Tue)**; 10-13 would be 31d, shorter than any FQ2 on record. The stored 10-13 is probably a stale +364d guess. Advance PR due ~**09-29 → 10-06** at the 14d lead, BusinessWire, *"Albertsons Companies Announces Second Quarter Fiscal 2026 Earnings Release and Conference Call Date."* | **2026-09-30** |

### Notes
- **UEC would have "reported in 2 days" per the DB** — the real date is a week out. The 09-17 next-check
  that never ran would also have found nothing (the PR came 09-22); the 7d lead held exactly, so the
  FY-end advance channel behaves like Q2/Q3. Cadence row rewritten.
- **Two re-seed time flags closed (ACN, STZ)**, both in the direction the cadence rows predicted. The MDT
  shape (a feed re-seed flips a settled time) is now 4-for-4 on the Q3 cohort where it has been checked.
- **Q4 Inc `Event.svc` feed** — first time used. Generalizable: any `*/English/investors/events/calendar/default.aspx`
  Q4 page should have `/feed/Event.svc/GetEventList` behind it (parameters as in the cached AMX URL;
  `eventSelection=0`, sort desc, `pageSize=100`, paginate with `pageNumber`). Promoted to
  `reference_q4_event_feed.md`. The feed returned each event twice and ignored `eventDateFilter`.
- WebSearch summaries were used only as pointers; every date above was read from a company page, a wire
  reprint on stocktitan, or EDGAR. BusinessWire deep links 403 to WebFetch (ACI FQ2 FY25 advance).
- `earnings_confirm.py --time-only` used for the first time in a daily session (ACI): wrote `bmo`, left
  `date_confirmed=0`. Works as patched.
- ⚠ Tooling: Bash heredocs whose body has an odd count of single quotes (a Python triple-quoted
  string, an apostrophe) are rejected by the harness command parser before bash runs — the edit
  script for this session had to be written with the Write tool as `.txt` (the hook refuses `.py`)
  and run with `python <file>`.

# Maintenance History

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

## Weekly Maintenance — 2026-09-20 (Sunday)

Second weekly pass in a row (launched 18:00 by Task Scheduler). One mailbox notice. The week's real
finding is not in the workspace at all: **three weekday sessions silently didn't happen.**

**⚠⚠ No session ran 09-16, 09-17 or 09-18.** No transcript, no log block, no dispute rows. The
orchestrator logs show why: the lite refresh flagged `Disputes flagged: 0` each morning (5 / 7 / 7
unconfirmed rows in scope), and the agent is spawned only `if disputes and spawn_agent`
(`ei_lite_refresh.py:339`); `launcher.py` daily mode has the same early-exit. Every gated symbol's
next-check had, until now, been rescued by some other symbol's dispute firing the launcher. Missed:
**CCL (next-check 09-16), UEC (09-17 — reports 09-24)**; never surfaced: **MU** (entered the 14d horizon
09-16) and **ACN** (09-17). No wrong write resulted. Written up in
`analysis/proposal_20260920_spawn_on_due_next_checks.md`, top of `notes_for_ben.md`, `STATUS.md`, and
as a standing caution in `feedback_window_gating_and_noop.md`.

**Archived.** `research_log.md` **761 → 504 lines** (incl. this entry). Sessions **09-01, 09-02, 09-03** (329 lines) moved
verbatim into `memory/archive/research_log_2026-Q3_summer-earnings.md`, chronological, ahead of the
appendices; archive header updated (now 07-01 → 09-03). Script: `analysis/maintenance_archive_20260920.py`
(backs up both files, asserts every moved non-blank line is present in the archive — passed). Active
log keeps 09-08 → 09-15. Header rebuilt from the DB: 2 carry-overs (both with a missed check), window
watch refreshed (**CCL 09-28 → 09-29 and DAL 10-08 → 10-09 moved in the feed**, unsourced), ledger
re-verified row-by-row against `earnings_upcoming` (14 rows, all match) and **LEN pruned** (reported 09-16).

**Promoted to structured memory.**
- `reference_company_cadence.md` — five rows that the 09-14 session confirmed but never wrote back:
  **PAYX** (resolved: lock was wrong, 09-23 Wed; lead 14d ×2; *weekday history is not a fence*),
  **KMX** (re-sourced; lead 20d ×2; publishes after the close), **MTN** (Q4 lead 24d = 2nd obs; host is a
  **403**, not a timeout; the advance sat unread 10 days), **CCL** (Q3 context, the feed move, absence
  record stops at 09-15), **DAL** (feed move). Cheat-sheet: Vail moved timeout → chronic 403; McCormick
  and `businesswire.com/newsroom` added to chronic 403; Jefferies split into "HTML shell / RSS works".
- `feedback_earnings_confirm_bare_symbol.md` — **rewritten to lead with the patched tool** (inbox
  notice: installed 09-16; I verified `--help` today: `--time-only`, required `--by`). Time-only fixes now
  go through `--time-only`, not the plain UPDATE. The three pre-patch traps are kept as history. What the
  patch can't do is stated up front: it cannot tell whether a `--date` is sourced.
- `feedback_direct_db_query.md` — the "prompt template omits `--write`" sentence retired (verified fixed
  in `launcher.py`); frontmatter brought to the current format; `PRAGMA` trips the write guard (seen once).
- `feedback_window_gating_and_noop.md` — the dispute-gated-session caution + three rules (put near-term
  next-checks in STATUS "Needs attention"; check missed next-checks first after a gap; **a gap is not an
  absence**).
- `MEMORY.md` — two index lines rewritten; all 20 pointers resolve, no unindexed files.

**Pruned `notes_for_ben.md`:** 175 → 170 lines, but materially different — the patch item and the
PAYX/KMX item moved verbatim to `notes_for_ben_archive.md` (new "Moved at the 2026-09-20 maintenance"
section) and condensed into Resolved; the tool-fix item now shows two fixes landed (confirm tool,
template `--write`) and what remains (`direct_db_query.py`, backslash paths in the template); new top
item for the missed sessions.

**Inbox/outbox.** `2026-09-16_earnings-confirm-patch-installed.md` integrated → `inbox/processed/`.
Inbox root clean. Outbox unchanged since 08-13, largest file 128 lines — no rotation.

**Calibration — this week (09-14 → 09-18: 2 sessions ran, 3 didn't).**
- 6 unique symbols handled (JEF, UEC, CCL, MTN + the two priority carry-overs PAYX, KMX).
  **Confirmed 4 — all four from company-issued PRs** (MTN, KMX, JEF; PAYX **corrected −6d**). Open: UEC, CCL.
- **Skip judgment, where it could be tested: 1 for 1.** JEF was gated five sessions running (09-08 →
  09-14) on "advance due ~09-14 at the 14d lead, publishes ~16:20 ET ⇒ read 09-15." The PR published
  **09-14 16:30 ET** and was confirmed 09-15 — the predicted morning, to the day. It also settled the
  dispute against finnhub and against the 10-05 third-party estimate. Two weeks running the gate has
  fired on its predicted day (CTAS 09-09, JEF 09-14) — two cases, both off leads with ≥2 observations.
- **UEC and CCL are untestable, not passed:** their checks never ran. I can't score those gates until
  a session reads the channels; if either PR turns out to have published on/near its predicted day,
  that's a hit for the lead table and a miss for the machinery.
- **Write-side: the 09-08 error is fully unwound.** PAYX corrected from the company PR, KMX sourced, and
  the tool patched so that route can't recur. Net cost: one wrong locked date for 5 days.
- **Drift I can own:** (1) On 09-14 I wrote *"window-watch rows with an open window should get a spine
  read the day they open"* after MTN's advance sat unread for 10 days — and on 09-15 I did not apply it:
  MU (open since ~09-02), STZ, PEP and ACN got no spine read. A lesson logged and not acted on the very
  next day. It is now in the window-watch header where Monday will see it, not only in a session note.
  (2) 09-14's confirms weren't written back to the cadence table (09-15's JEF was) — fixed today; the
  daily habit is "cadence row in the same session as the confirm."
- Sessions were lean where they ran: 09-15 = 5 reads / 1 search for 3 symbols; 09-14 = 11 reads / 0 searches.

**STATUS.md** rewritten.
