# Earnings Researcher — STATUS

> Lightweight dashboard for Ben. Maintained by the Earnings Researcher during its
> weekly maintenance session (`PROMPT_SUNDAY.md`). Glance here for current
> state without reading the full research log.

**Last updated:** 2026-11-08 (Sunday maintenance)

---

## Needs attention

1. **The frozen calendar is drifting.** No weekday session and no 5.3 refresh since 10-19. An EDGAR screen of the 11-02 → 11-06
   rows found **27 of 221 dates wrong (about 12%)**, up from about 4% the week before, some by a week or more (MKTX −13, CART −7,
   RKT −7, DASH −6). **Question in `notes_for_ben.md`:** keep weekday research off, or launch me on my own? I'd keep it off unless
   something trades off this calendar.
2. **ROKU was acquired by Fox (closed 11-06).** Any later ROKU row is a phantom.
3. **Audit #5: 42/42 dates, 41/42 times, no misses.** Next-Sunday audit? Question open in `notes_for_ben.md`. I'd skip until
   weekday confirms exist again.

## Open Carry-Overs

| Symbol | DB row | Why open | Next check |
|--------|--------|----------|------------|
| ITUB | next quarter | 11-03 prediction hit, but it rests on a weekday pattern. Hold until a company date is read | Q4 wave (early Feb) |

All six carry-overs from 11-01 reported and were scored: ITUB hit, DTE held; BMRN, CC, MKTX, ROKU had wrong DB dates.

**Unresearched:** 143 unconfirmed rows ahead (11-09 → 2027-01-11), on dates from the 10-19 feed. 421 past-dated rows parked.
**Confirmed-but-upcoming:** none. The last 5 (DOC, KHC, NVST, MAT, KMB) passed, and all 5 were right.

---

## Last Week's Calibration (11-02 → 11-06)

| Metric | Value |
|--------|-------|
| Sessions | **0 of 5** (Simple Mode) |
| Dates confirmed | **0** |
| Confirmed rows that came due | **5, all right** (date and time) |
| Carry-over skips scored | 6: 2 held / predicted (DTE, ITUB), 4 DB dates wrong (BMRN, CC, MKTX, ROKU) |

**Unresearched rows, EDGAR filing-date screen (11-02 → 11-06):** 194 of 221 dates agree, 27 wrong; 16 sessions wrong; 75 with
no time. Coarse, not an audit. Script: `analysis/edgar_screen.py`.

### Source audit #5 (n = 42; the 5 new rows plus earlier un-drawn October rows)

| Source type | n | date right | time right | unverifiable |
|---|---|---|---|---|
| Company IR / newsroom page | 12 | 12 | 11 | 1 (C) |
| PR read as a copy | 22 | 22 | 22 | 0 |
| Time inferred, date sourced | 8 | 8 | 8 | 0 |

Report: `analysis/source_audit_20261108.md`. Audits #3 → #5: 129 of 130 October confirms right (the miss was JBLU).

---

## Maintenance Bookkeeping (11-08)

- **Archived:** the 10-19 session, the 10-18 maintenance entry, and the last 5 ledger rows → fall archive. Ledger now empty.
- **Memory:** cadence rows CC, DTE, ROKU (new); BMRN, MKTX, ITUB, C annotated. Phantom memory: ROKU, MKTX.
- **notes_for_ben:** weekday item updated; audit #4 → archive, #5 added; ITUB → Resolved; phantoms + ROKU.
- **Inbox** root clean. **Outbox** ≤ 128 lines, no rotation. **MEMORY.md** pointers resolve.
