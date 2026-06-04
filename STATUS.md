# Earnings Researcher — STATUS

> Lightweight dashboard for Ben. Maintained by the Earnings Researcher during its
> weekly maintenance session (`PROMPT_SUNDAY.md`). Glance here for current
> state without reading the full research log.

**Last updated:** 2026-05-28 (weekly maintenance)

---

## Open Carry-Overs

Symbols still unresolved, with current status and the date to re-check (derived from
each company's announcement window — see `memory/reference_company_cadence.md`).

| Symbol | Reason still open | Current status | Next-check date |
|--------|-------------------|----------------|-----------------|
| CNM | No Q1 FY26 schedule PR yet | DB 06-09 unk; PR overdue (last-yr 05-23→06-10 bmo); yf+finnhub 06-10 | 2026-06-01 |
| ADBE | No Q2 FY26 "to Announce" PR | DB 06-11 amc; pattern-consistent (Q2 = 2nd/3rd Thu of June); PR ~now | 2026-06-01 |
| ORCL | No Q4 FY26 "Sets the Date" PR/8-K | DB 06-10 amc; PR historically ~Jun 3; finnhub 06-16 aggregator-only | 2026-06-03 |
| UEC | **DB date wrong (=today)**; no advance PR for Q3 | DB 05-28 unk — impossible; Q3 10-Q drops ~early-mid June; flagged to Ben | 2026-06-04 |
| GME | No Q1 FY26 8-K/PR; minimal advance notice | DB 06-09 unk; reports ~06-09/10 AMC; finnhub 06-08 | 2026-06-05 |

**Horizon** (surfaced before, outside window — don't research yet): LEN 06-15, JBL 06-16, KMX 06-17, ACN 06-18, DRI 06-18. Re-check ~06-08+.

---

## Last Week's Calibration

Window: 2026-05-21 → 05-28 (5 sessions).

| Metric | Value |
|--------|-------|
| Sessions run | 5 (05-21, 05-22, 05-26, 05-27, 05-28) |
| Symbols confirmed | 9 |
| Symbols skipped (logged next-check) | 16 |
| Confirm rate | 9/25 ≈ 36% |
| Skips that later confirmed on the predicted date | GWRE + TTC (skipped 05-20/21 → both confirmed 05-22 at predicted 06-04). No skip proved to be a missed confirmable date. |
| Open skips awaiting validation | 5 (CNM, ADBE, ORCL, UEC, GME) — next-checks early June |
| Notes / drift to watch | Late-week sessions (05-27, 05-28) were 0-confirm — every symbol a pre-PR June reporter. These should become clean **no-ops** via window-gating + the new cadence table, not full research passes. (Recall the 151k-token/0-confirm 05-28 session that prompted window-gating.) |

**Read:** skip judgment is well-calibrated — the "wait for the company PR" discipline keeps paying off (GWRE/TTC/WSM all confirmed at/near predicted dates; the M +7d move was caught by *not* confirming a stale feed date). The improvement lever is fewer wasted cycles on too-early symbols, not better accuracy.

---

## Maintenance Bookkeeping

- **Active `research_log.md` size:** 390 lines (was 1,157 before this roll).
- **Archive files:** `memory/archive/research_log_2026-Q2_spring-earnings.md` (849 lines, covers 2026-04-23 → 05-13).
- **Last archive roll:** 2026-05-28.
- **New this session:** `memory/reference_company_cadence.md` (cadence/lead-time table behind window-gating).
