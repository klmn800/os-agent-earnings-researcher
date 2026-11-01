# Earnings Research Log

> Active log: full sessions for the last ~2 weeks (newest first, below), a compact ledger of
> confirmed-but-upcoming dates, and the open carry-overs with next-check dates. Older sessions live in
> the season archives: `memory/archive/research_log_2026-Q2_spring-earnings.md` (through 06-30) and
> `memory/archive/research_log_2026-Q3_summer-earnings.md` (07-01 → 09-25, **closed**, plus the summer's ledger
> and carry-over table as appendices) and `memory/archive/research_log_2026-Q4_fall-earnings.md` (from 09-28: the
> sessions that researched the fall wave, plus pruned ledger rows verbatim in its Appendix A). Maintenance notes at the very bottom.
> Per-symbol cadence/lead-times live in `memory/reference_company_cadence.md`. **Grep it by symbol
> (`^| SYM `); don't read it whole (~220 KB).**

## ⚠ READ FIRST (updated 2026-11-01): no weekday sessions, and that is now permanent unless Ben changes it

Ben made **Simple Mode the default on 2026-10-28** (`docs/simple_mode/README.md`), after the 10-20 → 10-27 trial. It skips
orchestrator Phase 1, which is where this agent gets spawned, and the Friday 5.3 Earnings Refresh. So **no weekday session has
run since 10-19**, and `earnings_upcoming` has not been written since 10-19 (last confirm 07:42, last `updated_at` 07:22).
Earnings Signals is also disabled. Only this Sunday session fires. Whether I should run on my own is an open question in
`notes_for_ben.md`. If a weekday session does run, start with the rows below and ignore anything past-dated.

## Still unconfirmed (rebuilt 2026-11-01 from `earnings_upcoming`, `date_confirmed = 0`)

- **Past-dated, parked:** 172 rows dated 10-17 → 10-30. Nothing to trade ahead of, so don't research them unless Ben asks for a
  backfill. EDGAR screen of all 172: see the 11-01 maintenance entry.
- **Ahead, 11-02 → 11-06:** 249 rows, none researched. Named carry-overs are below.

## Open Carry-Overs: researched, unresolved, with next-check dates

| Symbol | DB row | Status at 11-01 | How to read | Next check |
|--------|--------|-----------------|-------------|------------|
| **ITUB** | 11-03 amc | **Prediction logged 11-01, before the report: release Tue 11-03 after the B3 close, 6-K cluster from Wed 11-04.** Not confirmed. See the 11-01 entry | EDGAR 6-K list | score **11-08** |
| BMRN | 10-26 amc | No Q3 Item 2.02 on EDGAR by 11-01 (only the 10-06 off-cycle one). DB date looks wrong; finnhub said 11-03 | EDGAR | score 11-08 |
| CC, DTE, MKTX, ROKU | 11-05 | No PR as of 10-19. MKTX under ICE acquisition | spine; search | first session |
| WBS | — | Skipped (delisted). Ben's item | — | — |

Spine = `analysis/helpers/spine.py` (paces itself to stocktitan's 10-per-300s limit; run big lists with `run_in_background`;
**no Monitor on it**, read the output once at the end).

## Upcoming Confirmed: locked dates (don't re-research)

One line per confirmed symbol whose date is still ahead (≥ 11-02). Pruned 11-01: the 75 rows dated 10-26 → 10-30, moved verbatim
to the fall archive's Appendix A (source audit #4 drew from them; JBLU's row there carries the correction).
Format: `SYM | date | time | source — session`.

| Symbol | Date | Time | Source — session |
|--------|------|------|------------------|
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

# Maintenance History

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
