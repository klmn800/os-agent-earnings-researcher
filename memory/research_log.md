# Earnings Research Log

> Active log: full sessions for the last ~2 weeks (newest first, below), a compact ledger of
> confirmed-but-upcoming dates, and the open carry-overs with next-check dates. Older sessions live in
> the season archives: `memory/archive/research_log_2026-Q2_spring-earnings.md` (through 06-30) and
> `memory/archive/research_log_2026-Q3_summer-earnings.md` (07-01 → 09-25, **closed**, plus the summer's ledger
> and carry-over table as appendices) and `memory/archive/research_log_2026-Q4_fall-earnings.md` (from 09-28: the
> sessions that researched the fall wave, plus pruned ledger rows verbatim in its Appendix A). Maintenance notes at the very bottom.
> Per-symbol cadence/lead-times live in `memory/reference_company_cadence.md`. **Grep it by symbol
> (`^| SYM `); don't read it whole (~220 KB).**

## ⚠ READ FIRST (updated 2026-11-15): no weekday sessions since 10-19, and the calendar is still frozen

Ben confirmed on 11-09 that weekday sessions **should** run (`memory/project_weekday_research_expected.md`). Simple Mode
turned them off by accident: it skips orchestrator Phase 1 (1.2 Earnings Intelligence, which spawns me) and the Friday 5.3
Earnings Refresh. As of 11-18 the orchestrator still logs "Simple Mode - skipping Phase 1" daily, and `earnings_upcoming`
was last written 10-19 07:22. Restore steps are in `notes_for_ben.md`. **When a weekday session does run:** the frozen rows
are badly stale. In the 11-15 EDGAR screen, 7 of 22 comparable dates for 11-09 → 11-13 were wrong (about 32%, up from 12%
and 4% in the two weeks before). Treat every unconfirmed date as an estimate and check EDGAR first. `edgar_screen.py` now
reads the Item 2.02 sentence, so next-morning filers no longer show up as false misses.

## Still unconfirmed (rebuilt 2026-11-15 from `earnings_upcoming`, `date_confirmed = 0`)

- **Past-dated, parked:** 460 rows dated 10-17 → 11-13. Don't research them unless Ben asks for a backfill. EDGAR screens:
  10-17 → 10-30 (11-01 entry), 11-02 → 11-06 (11-08 entry), 11-09 → 11-13 (11-15 entry).
- **Ahead:** 104 rows, 11-16 → 2027-01-11 (49 of them due by 11-27), none researched. Their dates come from a feed last refreshed 10-19.

## Open Carry-Overs: researched, unresolved, with next-check dates

All six named carry-overs reported and were scored 11-08 (see that entry): ITUB's prediction hit; DTE held; BMRN (+7 vs DB),
CC (−3), MKTX (−13) and ROKU (−3) didn't. **ROKU was acquired by Fox (closed 11-06)**, so any later ROKU row is a phantom.

| Symbol | DB row | Status at 11-15 (unchanged since 11-08) | How to read | Next check |
|--------|--------|-----------------|-------------|------------|
| ITUB | next quarter | Weekday pattern 4/4 (release Tue/Wed early in month 2), still not a source. Hold until a company date is read | EDGAR 6-K list | Q4 wave (early Feb) |
| WBS | — | Skipped (delisted). Ben's item | — | — |

Spine = `analysis/helpers/spine.py` (paces itself to stocktitan's 10-per-300s limit; run big lists with `run_in_background`;
**no Monitor on it**, read the output once at the end).

## Upcoming Confirmed: locked dates (don't re-research)

**Empty.** No confirmed row is dated ≥ 11-09. The last five (DOC, KHC, NVST, MAT, KMB, 11-02 → 11-05) were pruned 11-08 to the
fall archive's Appendix A; source audit #5 found all five right. Format when rows return: `SYM | date | time | source — session`.

---

# Research Sessions (newest first)

_No weekday sessions since 10-19 (Simple Mode). The 10-19 session is in the fall archive._

# Maintenance History

## Weekly Maintenance — 2026-11-15 (Sunday; the window stayed open and the work finished 11-18)

**Still Simple Mode: 0 weekday sessions, 0 confirms, no dispute rows since 10-19.** The orchestrator skipped Phase 1 on every
weekday 11-09 → 11-13 and again 11-16 → 11-18. `earnings_upcoming` is still at 10-19 07:22. Ben's 11-09 answer (weekday
research should run) is recorded; the restore is his to make.

**Archived.** The 10-25 maintenance entry → fall archive (header updated). No sessions or ledger rows to move; the ledger is
still empty. Active log ~132 lines. Header rebuilt: 460 past-dated unconfirmed rows parked, 104 ahead (11-16 → 01-11).

**Skip calibration: EDGAR screen of the 39 unresearched rows dated 11-09 → 11-13** (`analysis/edgar_screen_20261115_1109-1113.tsv`).
22 had a comparable Item 2.02 8-K. 17 had none: mostly foreign filers (B, PBR, SE, FNV, LEGN, BN, EC, JD, NU, SMFG, MFG, MUFG)
plus CNH, OGN, OKLO and TECH (10-Q/A only); QRVO has no CIK.
- **Date: 15 of 22 right, 7 wrong (about 32%).** PINS −11, GRAL −7, PTC −7, SARO −5, CELH −4, FIVN −4, LUNR +2. These are
  filing dates only; I didn't read the datelines. LUNR could also be a next-morning filer for 11-11.
- CTVA and TTEK flagged D+1 / session at first. Both are **next-morning filers**: the Item 2.02 sentence says 11-11, the DB
  date, so they are right.
- **Times:** 8 of the 15 matched rows were `Unknown` (CEG, FERG, LINE, RBA, RKLB, TTWO, FLY, CSCO); none contradicted a stored bmo/amc.
- **Reading:** the drift keeps climbing (4% → 12% → 32%) as more of the 10-19 feed's estimates come due. Coarse screen, same
  caveats as before. The 49 rows due by 11-27 will be worse, not better.
- **QRVO with no CIK** needs a rename or merger check before anyone researches it. Not done today (weekday work).

**Source audit #6: closes the October census.** Pool = every passed confirm no earlier audit checked: 87 rows (copy 70,
IR 17). Drew IR as a census plus 23 copy rows (seed 20261115) for 5 blind subagents, then screened the other 47 on EDGAR
(`analysis/edgar_screen_confirmed.py`). **Subagents: 40/40 right on date and time, 0 unverifiable, 0 mismatches. Screen:
47/47 dates.** STLD and TER flagged and were next-morning filers (Item 2.02 sentence read). **All 214 October-wave ledger
rows have now been checked once. One miss (JBLU), one unverifiable time (C).** Report: `analysis/source_audit_20261115.md`.
Nothing is left to draw until weekday confirms resume.

**Promoted.** Cadence: next-morning-filer notes on NOV, STLD, TER; new rows CTVA, TTEK (next-morning filers), PINS, GRAL,
PTC, SARO, FIVN, LUNR (Q3 dates from the screen); CELH annotated (Q3 4d earlier than DB); BK = EDGAR ticker BNY; WIT 6-K
~5 days late; CB 8-K at 17:24; CZR pending Fertitta deal (phantom pre-flight). **Tool:** `edgar_screen.py` now reads the
Item 2.02 date sentence on any date mismatch and re-dates next-morning filers. Tested on 11-11: CTVA and TTEK re-dated,
GRAL and PTC kept as misses.
**Hygiene.** notes_for_ben: audit #5 → archive, #6 + the next-audit question; weekday item updated (32%, still off 11-18).
Outbox ≤ 128 lines, no rotation. Inbox root clean (scratch in `inbox/fetch/`). MEMORY.md: pointers resolve, cadence line
updated. **STATUS.md** rewritten.

**Drift (mine):** (1) I ran the two screens chained in one background job. When the window paused, I thought it had died
and started a second copy, so both wrote the same files. The output checks out clean (no duplicate or malformed rows), but I
can't prove the two never overlapped. Next time: one job per file, and wait for the completion notice. (2) In the
draft audit report I wrote a "±2" approximate totals table and named SCHW as the extra row without checking. I replaced both
with exact sums from the reports before committing. (3) Last week I said I'd skip this audit. I ran it anyway, because it
closes the census for less than the cost of one more sample. Now the pool is empty, so the skip recommendation holds for real.

## Weekly Maintenance — 2026-11-08 (Sunday)

**Still Simple Mode: 0 weekday sessions, 0 confirms this week.** `earnings_upcoming` last written 10-19 07:22. No answer yet
from Ben on the weekday question or the next-audit question.

**Archived.** The 10-19 session (the last weekday session) and the 10-18 maintenance entry → fall archive. The last 5 ledger rows
(DOC, KHC, NVST, MAT, KMB, 11-02 → 11-05) → its Appendix A. The ledger is now empty. Active log 181 → ~140 lines. Header rebuilt
from `earnings_upcoming`: 421 past-dated unconfirmed rows parked, 143 ahead (11-09 → 01-11), all on 10-19 feed dates.

**Carry-overs scored (EDGAR index pages, ET Accepted times):**
- **ITUB: prediction hit.** Release datelined *São Paulo, November 3, 2026* (board approved the financials 11-03 15:00 local);
  first cluster 6-K Wed 11-04 07:00 ET. As written beforehand, that tests a weekday pattern, not a source. Keep it held.
- **DTE held** (11-05 bmo, 06:53). **BMRN** 11-02 amc (16:07; DB 10-26 was 7d early, finnhub 11-03 1d late). **CC** 11-02 amc
  (16:33; DB 11-05 Unknown). **MKTX** 10-23 bmo (06:30; DB 11-05, 13d late, under the pending ICE deal). **ROKU** 11-02 amc
  (16:09; DB 11-05), and **acquired by Fox, merger closed 11-06**.
- Overdue-PR doubts: none were logged for these six, so the tally stays 4 right / 4 wrong.

**Skip calibration: EDGAR screen of all 249 unresearched rows dated 11-02 → 11-06** (new reusable `analysis/edgar_screen.py`;
output `analysis/edgar_screen_20261108_1102-1106.tsv`). 221 had a Q3 Item 2.02 8-K, 27 had none (mostly foreign filers), 1 no CIK.
- **Date: 194 of 221 agree (88%), 27 wrong (12%)**, up from 6 of 146 (about 4%) the week before. Big misses: MKTX −13, CART −7,
  RKT −7, DASH −6, DV −6, KVUE −6, BMRN +7; ±1–3d for the rest. I read the Ex-99.1 datelines for DASH, CART, RKT, DV, KVUE, GPN,
  LYV, BRKR and FOX, and each is a real Q3 release on the EDGAR date. CG (17:47 8-K) and SRE (10:53 8-K) are ambiguous filing-
  time cases; I haven't classed them either way.
- **Session:** 16 rows had a stored bmo/amc contradicted by the 8-K time (FOX/FOXA, ON, WMB, YUMC, COR, EMR, APD, BDX, ROK, U,
  XRAY, BEN, plus DASH, CART, DKNG with a date miss). 75 matched rows had `Unknown` time.
- **Reading:** the drift is what a frozen feed does as stale estimates come due. The same caveat as last week applies: it's a filing-
  date screen, coarse on timing, and next-morning or late filers can hide in it.

**Source audit #5** (5 new + earlier un-drawn rows, pool 129, n = 42, 5 blind subagents): **42/42 dates right, 41/42 times right,
0 wrong, 1 unverifiable** (C: 8-K at 10:09 ET can't prove the ~8am release). IR 12, copy 22, inferred 8 (census). Edge cases FNB
(next-morning filer), PKG (18:07 filer, release 10-21), ERIC (late 6-K, 03:00 ET webcast) all called right. Report:
`analysis/source_audit_20261108.md`. Audits #3 → #5: 129 of 130 October confirms right.

**Promoted.** Cadence: BMRN, MKTX, ITUB annotated; new rows CC, DTE, ROKU; C ("8-K doesn't time the release").
`reference_ma_phantom_earnings.md`: ROKU (closed into Fox) and MKTX (early twice under a pending deal).
**Hygiene.** notes_for_ben: weekday item updated with the 12% screen; audit #4 → archive, replaced by #5 + the next-audit
question; ITUB → Resolved; phantoms + ROKU. Outbox ≤ 128 lines, no rotation. Inbox root clean. MEMORY.md: every pointer
resolves, nothing unindexed. **STATUS.md** rewritten.

**Drift (mine):** (1) On 10-19 I told myself MKTX was "under ICE acquisition, don't expect a date". It reported 13 days before the
DB, the same early-under-a-deal shape it showed in Q2. My own phantom memory already said so. (2) Last week I recommended against
another audit with only 5 rows in the pool. The prompt still asked, so I widened it per its own rule. It found nothing new, which
is the diminishing return I'd predicted. I'm saying so in the note rather than either skipping it or overselling it.

## Weekly Maintenance — 2026-11-01 (Sunday)

**Simple Mode is now permanent (10-28), so there were 0 weekday sessions and 0 confirms this week.** `earnings_upcoming` hasn't
been written since 10-19. Header rewritten to say so.

**Archived.** Sessions 10-12 → 10-16 and the 10-11 maintenance entry → fall archive. The 75 ledger rows dated 10-26 → 10-30 →
its Appendix A, with JBLU's row annotated. Active log 327 → ~180 lines. **Ledger check:** 5 of 5 future rows match the DB
(DOC, KHC, NVST, KMB, MAT), 0 missing.

**Source audit #4 (10-26 → 10-30):** 42 rows from a pool of 75, 5 blind subagents, **41/42 right on date and time, 0
unverifiable.** IR 7/7, copy 12/12, search summary 10/10, inferred 12/13. Report: `analysis/source_audit_20261101.md`.
- **Miss: JBLU**, 10-27 bmo → actually **10-26 amc** (8-K accepted 16:15:21, I re-read it). It came from a 10am call with a
  silent PR. Its 5 prior quarters were all same-morning, so even the prior-quarter check would have agreed with the wrong answer.
  Cadence row and rule 6 updated. NVT and RCL, flagged 10-25, both held.

**ITUB 6-K test: prediction written here before the report (Sun 11-01 evening; latest 6-K is 10-26, a Neospace material fact).**
Predicted **release Tue 11-03 after the B3 close, first 6-K of the cluster Wed 11-04.** No DB write, not confirmed. Basis: Q3'25
released Tue 11-04-25, Q4'25 Wed 02-04-26, Q2'26 Tue 08-04-26 (Ex-99.1 datelines); the cluster began the next day each time.
Q1'26's cluster began 05-06; I didn't read that dateline. **Finding before the score:** the cluster follows the release, so it
can't date one in advance. What I'm really testing is a weekday pattern, which isn't evidence by my own rules, so even a hit
proves little. Done on a Sunday because no other session runs before 11-03; it was a few EDGAR reads and a log entry.

**Skip calibration: EDGAR screen of all 172 unconfirmed past-dated rows (10-17 → 10-30), filing date vs DB.** 145 had a Q3
Item 2.02 8-K, BMRN has none yet, 26 have none to compare (mostly foreign filers, plus COKE and WLK).
- **Date:** 139 agree. 6 of 146 are wrong: IRDM −2, SCCO −2 (release 10-20), WHR −2, DAR −1, DVA +1, BMRN (no report by 11-01,
  DB 10-26). CUBE +1 is ambiguous (07:23 next morning; may be a next-morning filer, as RRC turned out to be).
- **Session:** 5 DB `amc` rows have a morning 8-K on the date (PYPL, TEL, CTSH, LHX, CHRW). 33 of the matched rows were `Unknown`.
- **Caveat:** a filing-date screen, not an audit. It's coarse on timing, and I read only index pages for the flagged rows.
  Rows that are off in the same way as RRC or CUBE can hide here. Rough rate: about 4% of unresearched dates wrong.
- **Named carry-overs:** CNC, GLW, PCAR, EBAY, SW, OSK held on date. PYPL held on date, wrong on time. **DVA's overdue-PR doubt
  was right** (DB 10-28 → 10-29), so doubts stand at **4 right / 4 wrong**. WHR moved −2 with no doubt logged. BMRN pending.

**Promoted.** Cadence: JBLU rewritten; rule 6 addendum; new rows DVA, WHR, DAR, CUBE, PYPL group, RRC, PII, ITUB.
**Hygiene.** notes_for_ben: audit #3 archived; Simple Mode item rewritten; audit #4 and ITUB updated. Outbox ≤ 128 lines, no
rotation. Inbox root clean. MEMORY.md: pointers resolve, cadence line updated. **STATUS.md** rewritten.

**Drift (mine):** the 10-25 note said next week's audit pool would be ~45 rows. It was 75.
