# Earnings Researcher — STATUS

> Lightweight dashboard for Ben. Maintained by the Earnings Researcher during its
> weekly maintenance session (`PROMPT_SUNDAY.md`). Glance here for current
> state without reading the full research log.

**Last updated:** 2026-10-25 (Sunday maintenance)

---

## Needs attention

1. **Weekday sessions are off under Simple Mode** (trial since 10-20; Phase 1 is skipped, and Phase 1 is what spawns me). No
   session ran 10-20 → 10-23. The last DB confirm was 10-19 07:42. I'm assuming it's intended. **Question for you in
   `notes_for_ben.md`:** keep it off, or launch me on my own?
2. **ITUB 6-K test (11-03)** needs a run before 11-02. With no weekday sessions, it slips unless I do it Sunday 11-01.
3. **Audit #3 done: 44/44 right.** Next-Sunday audit? Question open in `notes_for_ben.md`.

## Open Carry-Overs

All 10-19 next-checks passed with no session, so each one is now "first session that runs".

| Symbol | DB row | Why open | Next check |
|--------|--------|----------|------------|
| BMRN | 10-26 amc | No PR (finnhub 11-03) | first session |
| CNC, GLW, PCAR, PYPL | 10-27 | No company PR as of 10-19 | first session |
| COKE, DVA, EBAY, SW, WHR | 10-28 | No PR; DVA overdue against its Q3'25 lead | first session |
| OSK | 10-29 bmo | No PR | first session |
| ITUB | 11-03 amc | 6-K-cluster test: predict, don't confirm, then score | before 11-02 |
| CC, DTE, MKTX, ROKU | 11-05 | No PR; MKTX under ICE acquisition | first session |
| *parked (past)* | HDB, IBN, ISRG, DOW, IRDM, SCCO, INFY | Reported with no session running. EDGAR: IRDM and SCCO came **10-20**, 2d before their DB rows | only if asked |

**Confirmed-but-upcoming:** 80 rows (10-26 → 11-05). **80/80 match the DB** (checked 10-25). Inferred times still ahead:
NVT (10-30 bmo, 9am call only) and RCL (10-27 bmo, 10am call only).

---

## Last Week's Calibration (10-19 → 10-23)

| Metric | Value |
|--------|-------|
| Sessions | **1 of 5** (10-19; Simple Mode from 10-20) |
| Dates confirmed | **23** of a 40-row queue (58%) |
| Stored dates corrected | none |
| Times filled | SPCX, ARE Unknown → amc; XOM, NVT Unknown → bmo |
| Wrong writes found | 0 (audit #3, 44 of the October writes) |

**Skip judgment:** of the parked rows that reported unseen, ISRG and DOW held their DB dates. IRDM (no call, no PR) and SCCO
(DB had the call date) both came 2 days early, on 10-20. Overdue-PR doubts now stand at **3 right / 4 wrong** (ISRG's
doubt was wrong), so an overdue PR means look again, nothing more.

### Source audit #3: October confirms, stratified random sample (n = 44, all checked against EDGAR or dated releases)

| Source type | n | date right | time right |
|---|---|---|---|
| Company IR / newsroom page | 10 | 10 | 10 |
| PR read as a copy | 10 | 10 | 10 |
| Search summary (of company text) | 11 | 11 | 11 |
| Time inferred, date sourced | 13 | 13 | 13 |

Report: `analysis/source_audit_20261025.md`. Earlier audits: #1 (10-11, September, 49/50) and #2 (10-18, summer weak types,
feed/cadence locks 6/12 dates, call-time inferences 9/12 times).

---

## Maintenance Bookkeeping (10-25)

- **Archived:** sessions 10-05 → 10-09 and the 10-04 maintenance entry → fall archive; the 103 ledger rows dated 10-19 →
  10-23 → its Appendix A. Active log 600 → ~330 lines.
- **Memory:** cadence rows SCCO, IRDM, ISRG, DOW, INFY, SCHW, PCG/DHR (evening-before 8-K filers). MEMORY.md: all
  pointers resolve.
- **notes_for_ben:** audit #2 and the daily-queue item archived; Simple Mode question and audit #3 added; SCHW closed.
- **Inbox** root clean. **Outbox** ≤ 128 lines, no rotation.
