# Earnings Researcher — STATUS

> Lightweight dashboard for Ben. Maintained by the Earnings Researcher during its
> weekly maintenance session (`PROMPT_SUNDAY.md`). Glance here for current
> state without reading the full research log.

**Last updated:** 2026-11-01 (Sunday maintenance)

---

## Needs attention

1. **Weekday research is off under Simple Mode** (default since 10-28), and `earnings_upcoming` is frozen at 10-19.
   **Question in `notes_for_ben.md`:** keep it off, or launch me on my own? I recommend off unless something uses this calendar.
2. **Audit #4: 41/42 right.** The miss is JBLU (logged 10-27 bmo, really 10-26 amc).
3. **Next-Sunday audit?** Question open in `notes_for_ben.md`. The pool would be only 5 rows, so I'd stop here.

## Open Carry-Overs

| Symbol | DB row | Why open | Next check |
|--------|--------|----------|------------|
| ITUB | 11-03 amc | Prediction logged: release 11-03 after B3 close, 6-K cluster 11-04. Not confirmed | score 11-08 |
| BMRN | 10-26 amc | No Q3 report on EDGAR by 11-01; DB date looks wrong | score 11-08 |
| CC, DTE, MKTX, ROKU | 11-05 | No PR as of 10-19; MKTX under ICE acquisition | first session |

**Unresearched:** 249 unconfirmed rows 11-02 → 11-06. 172 past-dated rows parked.
**Confirmed-but-upcoming:** 5 rows (DOC, KHC, NVST, KMB, MAT), **5/5 match the DB** (checked 11-01).

---

## Last Week's Calibration (10-26 → 10-30)

| Metric | Value |
|--------|-------|
| Sessions | **0 of 5** (Simple Mode) |
| Dates confirmed | **0** |
| Wrong writes found | **1** (JBLU, confirmed 10-14) |
| Overdue-PR doubts | **4 right / 4 wrong** (DVA was right) |

**Skip judgment:** of the carry-overs that reported, CNC, GLW, PCAR, EBAY, SW and OSK held on date. PYPL held on date; its time
looks wrong. DVA came 1d late, as doubted. WHR came 2d early, with no doubt logged.

**Unresearched rows, EDGAR filing-date screen:** 6 of 146 dates wrong (about 4%), 5 sessions wrong. Coarse, not an audit.

### Source audit #4: 10-26 → 10-30 confirms (n = 42, all checked against EDGAR or dated releases)

| Source type | n | date right | time right |
|---|---|---|---|
| Company IR / newsroom page | 7 | 7 | 7 |
| PR read as a copy | 12 | 12 | 12 |
| Search summary (of company text) | 10 | 10 | 10 |
| Time inferred, date sourced | 13 | 12 | 12 |

Report: `analysis/source_audit_20261101.md`. Earlier audits: #1 (September, 49/50), #2 (summer weak types), #3 (October, 44/44).

---

## Maintenance Bookkeeping (11-01)

- **Archived:** sessions 10-12 → 10-16, the 10-11 maintenance entry, and 75 ledger rows → fall archive.
- **Memory:** JBLU rewritten; rule 6 addendum; rows DVA, WHR, DAR, CUBE, PYPL group, RRC, PII, ITUB. MEMORY.md pointers resolve.
- **notes_for_ben:** audit #3 archived; Simple Mode, audit #4 and ITUB rewritten.
- **Inbox** root clean. **Outbox** ≤ 128 lines, no rotation.
