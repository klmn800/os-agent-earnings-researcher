# Earnings Research Log

> Active log: full sessions for the last ~2 weeks (newest first, below), a compact ledger of
> confirmed-but-upcoming dates, and the open carry-overs with next-check dates. Older sessions live in
> the season archives: `memory/archive/research_log_2026-Q2_spring-earnings.md` (through 06-30) and
> `memory/archive/research_log_2026-Q3_summer-earnings.md` (07-01 → 09-25, **closed**, plus the summer's ledger
> and carry-over table as appendices) and `memory/archive/research_log_2026-Q4_fall-earnings.md` (from 09-28: the
> sessions that researched the fall wave, plus pruned ledger rows verbatim in its Appendix A). Maintenance notes at the very bottom.
> Per-symbol cadence/lead-times live in `memory/reference_company_cadence.md`. **Grep it by symbol
> (`^| SYM `); don't read it whole (~220 KB).**

## ⚠ READ FIRST (2026-10-25): weekday sessions are not launching

Ben's **Simple Mode trial started 2026-10-20** (`docs/simple_mode/README.md`, commits 30719c6 → 7b45809). Simple Mode skips
orchestrator Phase 1, and Phase 1 is where the Earnings Intelligence step spawns this agent. It also skips the Friday 5.3 Earnings
Refresh. So **no weekday session ran 10-20 → 10-23**, and none will while the trial runs. This is deliberate on Ben's side, not an
outage. The last confirm in `earnings_upcoming` is 2026-10-19 07:42. Only the Sunday maintenance session still fires.
If a weekday session does run, start with the open rows below, nearest date first, and drop the past-dated ones (see their rows).

## Still unconfirmed (rebuilt 2026-10-25 from `earnings_upcoming`, `date_confirmed = 0`)

| Reports | Unconfirmed (`?` = time Unknown) | Notes |
|---------|-----------------------------------|-------|
| **past** 10-17 → 10-23 | HDB, IBN (10-17), ISRG (10-20), DOW, IRDM?, SCCO? (10-22), INFY (10-23) | Already reported, never confirmed. Nothing to trade ahead of, so **don't research them** unless Ben asks for a backfill. Under Ben's 10-19 rule HDB/IBN would be **10-19 bmo** (the DB still says 10-17) |
| 10-26 | BMRN | Finnhub said 11-03. No PR as of 10-19 |
| 10-27 | CNC, GLW, PCAR, PYPL | No company PR as of 10-19 (calendar estimates only) |
| 10-28 / 10-29 | COKE?, DVA, EBAY?, SW?, WHR?, OSK | No PR as of 10-19. DVA overdue against its Q3'25 lead |
| 11-03 | ITUB | Ben's 6-K-cluster test: log the predicted date **before** it reports, then score it. Not done (no session ran) |
| 11-05 | CC?, DTE, MKTX, ROKU | MKTX is under ICE acquisition; a date may never come |

## Open Carry-Overs: researched, unresolved, with next-check dates

Every next-check date in the 10-19 table (10-19 → 10-21) **passed with no session**. Reset to "first weekday session".
The "How to read" column is still the working channel; use it verbatim.
Spine = `analysis/helpers/spine.py` (paces itself to stocktitan's 10-per-300s limit; run big lists with `run_in_background`;
**no Monitor on it**, read the output once at the end).

| Symbol | DB row | Status at 10-19 | How to read | Next check |
|--------|--------|-----------------|-------------|------------|
| BMRN | 10-26 amc | No PR (Q3'25 notice was 10-22 for 10-27) | spine | first session |
| CNC, GLW | 10-27 bmo | No Q3 date PR (calendars: CNC 10-27 8:30am, GLW 10-28) | spine; search | first session |
| PCAR, PYPL | 10-27 | No company PR (calendars 10-27 bmo) | spine; search | first session |
| WHR, DTE, OSK | 10-28 → 11-05 | Not scanned 10-19. WHR Q3'25 notice was 10-20 for 10-27 | spine | first session |
| DVA | 10-28 amc | No PR; Q3'25 notice was 10-13 for 10-29 (overdue since 10-14) | spine; investors.davita.com | first session |
| MKTX, EBAY | 10-28 → 11-05 | No PR. **MKTX under ICE acquisition**; EBAY has no date (Q2 was 08-05) | spine | first session |
| ROKU, CC, COKE, SW | 10-28 → 11-05 | No PR (COKE Q2 notice 07-22 for 08-05; CC Q2 07-23 for 08-04; SW Q2 reported 07-29) | spine; search | first session |
| **ITUB** | 11-03 amc | **Ben 10-19: test the 6-K cluster first.** Predict from the SEC 6-K filing cluster, *don't confirm*; score after the report | EDGAR 6-K list; itau.com.br 403s | before 11-02 |
| *past, parked* | HDB, IBN, ISRG, DOW, IRDM, SCCO, INFY | Reported while no session ran. Parked; see the table above | — | only if Ben asks |
| WBS | — | Skipped (delisted). Ben's item | — | — |

## Upcoming Confirmed: locked dates (don't re-research)

One line per confirmed symbol whose date is still ahead (≥ 10-26). **Checked mechanically against
`earnings_upcoming` on 2026-10-25: 80 of 80 rows ↔ DB, 0 date/time mismatches, 0 DB-confirmed rows missing here.**
Pruned 10-25: the 103 rows dated 10-19 → 10-23, moved verbatim to the fall archive's Appendix A (source audit #3 drew from
them and the 10-13 → 10-16 rows). BK's missing calendar row: Ben said skip (10-19), don't re-flag.
Inferred times are marked in each row. Format: `SYM | date | time | source — session`.

| Symbol | Date | Time | Source — session |
|--------|------|------|------------------|
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
| ST | 2026-10-27 | amc | Sensata BW 10-14 (stocktitan page): at or about 4:05pm ET, call 5pm ET; 13d lead — 10-19 |
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
| UPS | 2026-10-27 | bmo | UPS BW 10-13 (stocktitan page): ~6:00am ET, call 8:30am; 14d lead — 10-19 |
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

40-row queue (15 disputes + 25 unconfirmed). **23 confirmed:** ST (10-27 amc) and UPS (10-27 bmo) came from the spine after the searches missed them. OMC (10-22 amc), SPCX (10-20, time Unknown → amc), AMX (10-20 amc), XOM (10-30, Unknown → bmo), NVT (10-30, Unknown → bmo, inferred), ARE (10-26, Unknown → amc), and 17 of the 10-27 batch (ST, UPS added): OKE, PPG, RRC, STAG, STX, UHS, V, WM amc; FCX, RCL, RGEN, SHW, SOFI, SPGI, XYL bmo.
Method: one background spine over all 40 (SCCO 404'd a 5th time) plus ~35 WebSearches, one per name, read through finviz/stocktitan/placera copies and the company's own pages (ir.spacex.com, investor.exxonmobil.com, press.spglobal.com, investor.visa.com). The spine caught ST and UPS, which the searches missed; it found nothing else new.
Date corrections: none. Every confirmed date matched the DB; finnhub was wrong for OMC (10-20). UHS moved its release 10-26 → 10-27 on 10-09 (the first PR is still what some calendars show).
Time inferences: NVT bmo (call 9am only), RCL bmo (call 10am only). AMX: 3Q26 call-invitation PDF is on the company's q4cdn (release 10-20 after close, call 10-21), but the Event.svc feed still has no 3Q26 event, and WebFetch can't read the PDF, so the text came from a search summary of it.
Not resolved: ISRG, DOW, SCCO, IRDM, INFY, CNC, GLW, PCAR, PYPL (no company PR found), DVA, EBAY, BMRN, MKTX, ROKU, CC, COKE, SW (no PR). INFY: still only news coverage of the board filing. MKTX: under ICE acquisition, don't expect a date. HDB/IBN held for Ben's policy Q2. WHR, DTE, OSK not scanned (next check 10-20).
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

# Maintenance History

## Weekly Maintenance — 2026-10-25 (Sunday)

**Weekday sessions stopped after 10-19.** Ben's Simple Mode trial began 10-20. It skips orchestrator Phase 1, which is where
the Earnings Intelligence step spawns me, and it skips the Friday 5.3 Earnings Refresh. The orchestrator logs for 10-20 →
10-23 show "Simple Mode - skipping Phase 1". The last DB confirm was 10-19 07:42. This was deliberate on Ben's side, not an
outage. I put a READ FIRST block in the header and raised it in `notes_for_ben.md` as a question.

**Archived.** Sessions 10-05 → 10-09 and the 10-04 maintenance entry went to the fall archive (chronological; header
updated). The 103 ledger rows dated 10-19 → 10-23 went verbatim to its Appendix A. The active log went from 600 to ~290
lines, keeping 10-12 → 10-19 in full. Header rebuilt from `earnings_upcoming`: the past-dated unconfirmed rows (HDB, IBN,
ISRG, DOW, IRDM, SCCO, INFY) are parked, and every other next-check is reset to "first session".

**Ledger check (mechanical):** 80 of 80 future rows (10-26 → 11-05) match the DB on date and time. 0 DB-confirmed rows
are missing from the ledger.

**Source audit #3 (October, forward):** 134-row pool, 43 drawn by stratified random sampling plus SCHW, 5 blind subagents.
Report: `analysis/source_audit_20261025.md`.
- **44 of 44 match on date and time, 0 unverifiable.** IR direct 10/10, PR copy 10/10, search summary 11/11, inferred time
  13/13. Aggregator and feed-agreement sources: n = 0 in the pool (policy since July).
- In the summer, call-time inferences were 9/12. In October they were 13/13. That probably reflects rule 6, but it isn't
  tested; October was mostly large caps with fixed habits. Small n for each type, so I'm not generalizing.
- New evidence rule (in the cadence table): an **evening-before 8-K** (PCG 21:04, DHR 17:43, accepted after 17:30) carries
  the next day's EDGAR filing date and a same-morning release, so it is D bmo, not D−1 amc. **SCHW files at ~16:17 every
  quarter**, so its 8-K never times the release.

**Calibration, week 10-19 → 10-23.** **1 of 5 sessions** (10-19 only; Simple Mode). **23 confirms** from a 40-row queue (58%).
No date corrections. Times: SPCX, ARE Unknown → amc; XOM, NVT Unknown → bmo (NVT inferred).
- **Parked rows that reported unseen** (EDGAR): ISRG 10-20 amc and DOW 10-22 bmo held. **IRDM reported 10-20 bmo** (DB 10-22,
  2d late; no call, so no advance PR, as noted). **SCCO released 10-20** (DB 10-22 was the call date). INFY's date held; my
  bmo time call is still unverified (the 6-K landed 11:45 ET).
- **Overdue-PR doubts: 3 right, 4 wrong** (ISRG's "no PR 1 day out" doubt was wrong). It stays a reason to look, not evidence.
- Rule-6 exposure in the 10-19 writes: NVT (9am call) and RCL (10am call) were bmo from the call time alone. Both dates are
  still ahead (10-27/10-30). If a session runs before then, check their prior-quarter 8-K times.

**Promoted.** Cadence rows SCCO (release = call − 2d), IRDM (no-call quarters: EDGAR only), ISRG, DOW, INFY, SCHW (late 8-K
filer; update-day inference 4/4), and PCG/DHR (evening-before filers). The SCHW Q3 row is marked as held.

**Hygiene.** notes_for_ben: audit #2 and the 10-11 queue item archived; audit #3, Simple Mode and the next-audit question
added; SCHW minor item closed. Outbox ≤ 128 lines, no rotation. Inbox root clean (`inbox/fetch/` holds 240-odd scratch
downloads, which is harmless). MEMORY.md: every pointer resolves and nothing is unindexed. **STATUS.md** rewritten.

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
