# Earnings Researcher — STATUS

> Lightweight dashboard for Ben. Maintained by the Earnings Researcher during its
> weekly maintenance session (`PROMPT_SUNDAY.md`). Glance here for current
> state without reading the full research log.

**Last updated:** 2026-11-15 (Sunday maintenance; the window stayed open and the work finished 11-18)

---

## Needs attention

1. **Weekday research is still off (4th week).** You said on 11-09 it should run. Simple Mode still skips 1.2 Earnings
   Intelligence (my spawn) and the Friday 5.3 refresh. The orchestrator logged "skipping Phase 1" every weekday through 11-18,
   and `earnings_upcoming` hasn't been written since 10-19. **The stored dates are getting worse:** 7 of 22 comparable rows for
   11-09 → 11-13 were wrong on EDGAR (about 32%, after 12% and 4%). Restore order in `notes_for_ben.md`: refresh the calendar first, then the spawn.
2. **Audit #6 closed the October census:** every October-wave confirm has been checked once. 1 miss (JBLU), 1 unverifiable (C).
   The next-audit question is open in `notes_for_ben.md`. The pool is now empty until weekday confirms resume.
3. **QRVO** has no CIK in SEC's ticker list (row dated 11-09). Check for a rename or merger before anyone researches it.

## Open Carry-Overs

| Symbol | DB row | Why open | Next check |
|--------|--------|----------|------------|
| ITUB | next quarter | 11-03 prediction hit, but it rests on a weekday pattern. Hold until a company date is read | Q4 wave (early Feb) |

**Unresearched:** 104 unconfirmed rows ahead (11-16 → 2027-01-11, 49 due by 11-27), all on dates from the 10-19 feed.
460 past-dated rows parked.
**Confirmed-but-upcoming:** none.

---

## Last Week's Calibration (11-09 → 11-13)

| Metric | Value |
|--------|-------|
| Sessions | **0 of 5** (Simple Mode) |
| Dates confirmed | **0** |
| Confirmed rows that came due | 0 (none were left) |
| Carry-over skips scored | 0 due (ITUB's next check is February) |

**Unresearched rows, EDGAR screen (11-09 → 11-13, 39 rows):** 22 comparable. **15 dates right, 7 wrong** (PINS −11, GRAL −7,
PTC −7, SARO −5, CELH −4, FIVN −4, LUNR +2). 17 had no comparable 8-K (mostly foreign filers). CTVA and TTEK looked wrong but
were next-morning 8-K filers. `edgar_screen.py` now catches that case. Coarse screen, not an audit.

### Source audit #6 (n = 40 by subagent + 47 by EDGAR screen; the whole remaining October pool)

| Source type | n | date right | time right | unverifiable |
|---|---|---|---|---|
| Company IR / newsroom page | 17 (census) | 17 | 17 | 0 |
| PR read as a copy | 23 | 23 | 23 | 0 |
| PR copy, EDGAR screen only | 47 | 47 | no contradiction | — |

October wave, audits #3 → #6: all 214 ledger rows checked, **1 miss (JBLU), 1 unverifiable (C)**. Report: `analysis/source_audit_20261115.md`.

---

## Maintenance Bookkeeping (11-15)

- **Archived:** 10-25 maintenance entry → fall archive. Ledger still empty.
- **Memory:** cadence notes on NOV, STLD, TER, BK, WIT, CB, CZR, CELH; new rows CTVA, TTEK, PINS, GRAL, PTC, SARO, FIVN, LUNR.
- **Tool:** `analysis/edgar_screen.py` reads the Item 2.02 date sentence and re-dates next-morning filers.
- **notes_for_ben:** audit #5 → archive, #6 + question added; weekday item updated.
- **Inbox** root clean. **Outbox** ≤ 128 lines, no rotation. **MEMORY.md** pointers resolve.
