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
| **10-13** | **ACI** (carry-over below, date doubted) |
| **10-14** | ASML, BAC, FAST, MS, STT |
| **10-15** | AA, BK, MAN, MRSH, PLD, PNC, SCHW, TSM, USB, **SNA** (carry-over below, date doubted) |
| **10-16** | CFG, MTB, TRV |
| **10-17** | HDB, IBN: **Saturday-dated** Indian ADRs. Read the date; hold the encoding for Ben's policy Q2 (`notes_for_ben.md`) |
| 10-19 | STLD, WRB, ZION |
| 10-20 | ALLY, CB, COF, EFX, EWBC, GE, GM, HAL, HAS, ISRG, MSCI, NOC, OMC, UAL (time-only, date open) |
| 10-21 | CCI, CME, DHR, ELV, EQR, FAF, IBM, KNX, LRCX (time-only), LUV, LVS, MOH, PKG, PM, SAP, T, TMO, TSLA, TXN |
| 10-22 | CMCSA, DGX, DOV, DOW, HBAN, HON, INTC, LAZ, NDAQ, NEM, NOK, ORI, PG, PHM, SCCO (`Unknown`), SPOT, SSNC, UNP, VLO, VRSN, WST |
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
| **SNA** | 10-15 `bmo` (time sourced; date unlocked, **probably 7d early**) | 53-week fiscal 2025 ⇒ Q3 ends 10-03 ⇒ **Thu 10-22** expected. The webcast PR (14d lead) settles it: **a PR dated ~10-01 ⇒ 10-15 is real; none ⇒ 10-15 is dead, and the 10-22 PR is due 10-08.** ⚠ The 10-02 check **never ran** (crowded out). Dispute row left `unresolved` but it doesn't re-flag. | stocktitan spine `SNA`. Title: *"Snap-on Incorporated to Webcast 2026 Third Quarter Results Conference Call"* (BusinessWire). `investors.snapon.com` is NXDOMAIN. | **10-05 FIRST**, then 10-09 |
| **ACI** | 10-13 `bmo` (time sourced; date unlocked) | FQ2 ends 09-12; the last two FQ2s reported 38d after ⇒ **Tue 10-20**. 14d-lead advance due ~09-29 for 10-13 or ~10-06 for 10-20. ⚠ The 09-30 check **never ran** (crowded out). **Absent on 10-05 ⇒ 10-13 is 6 days overdue, so say so in notes_for_ben** (scanner exposure: 8 days out). | stocktitan spine `ACI` (BW deep links 403); `albertsonscompanies.com` news-details renders. Title: *"Albertsons Companies Announces Second Quarter Fiscal 2026 Earnings Release and Conference Call Date."* | **10-05 FIRST**, then 10-07 |
| **AMX** | 10-13 `amc` (finnhub 10-20) | No 3Q26 event in the feed as of 10-02 (newest 2Q26, 07-21). Q3 is always Tuesday amc (10-17 / 10-15 / 10-14); 10-13 fits. The event's appearance lead is unmeasured. **Log the first day it appears.** | Event.svc feed, browser UA, `pageSize=100` (cached correctly since 09-28). Page with `pageNumber`, dedupe by `EventId`, parse `StartDate` with strptime (string-sorting `MM/DD/YYYY` is garbage), open as utf-8. | **10-05**, daily |
| **EQT** | 10-20 `amc` | Q2 PR 07-02 → 07-21 (19d) ⇒ Q3 PR due ~10-01; none by 10-02. **Slightly overdue.** 06-30 bad-batch name. | stocktitan spine `EQT` | **10-05** |
| **TSCO** | 10-22 `Unknown` | Q2 PR 07-02 → 07-23 (21d) ⇒ due ~10-01; none by 10-02. **Slightly overdue.** IR calendar empty. | search the IR newsroom; stocktitan `TSCO` | **10-05** |
| **MMM, VRT, WAL, LRCX, UAL** | 10-20 / 10-21 / 10-21 / 10-21 / 10-20 | **Time-only** (EDGAR furnish history, 09-30); dates unsourced. WAL: aggregator says 10-20 amc, so the DB 10-21 may be a day late. UAL's live row moved 10-21 → 10-20. | stocktitan spines; IR newsrooms | 10-05 |
| **PNR, PEGA** | 10-20 | 14d leads (1 obs each) ⇒ PRs due ~10-06 | stocktitan spines | **10-07** |
| **ALK** | 10-22 `Unknown` | 14d lead (Q2) ⇒ due ~10-08 | — | 10-09 |
| **RHI** | 10-21 `amc` | ~7d lead ⇒ due ~10-14. **Don't read before ~10-12.** | — | 10-13 |
| **GL, QS, SF, TER, VLTO, BPOP, NSC, SLM, ITW, F, FCX, POOL, DECK, BC** | 10-21 → 10-23 (F/FCX later) | No company Q3 date as of 10-02; only aggregator estimates. VRT onward went unread on 10-02 (429). **BC:** Q2 was 07-30, so 10-22 looks early (weak signal). | stocktitan spines first | 10-05 |
| **IRDM, WBS** | 10-22 `Unknown` | Pending acquisitions (Rocket Lab / Santander), no calls. Look for a bare results PR or 8-K. Run the phantom screen. | EDGAR 8-K | 10-07 |

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
