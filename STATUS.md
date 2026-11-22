# Earnings Researcher — STATUS

> Lightweight dashboard for Ben. Maintained by the Earnings Researcher during its
> weekly maintenance session (`PROMPT_SUNDAY.md`). Glance here for current
> state without reading the full research log.

**Last updated:** 2026-11-22 (Sunday maintenance)

---

## Needs attention

1. **Weekday research is still off (5th week). The fix waits on you registering the `\!Earnings Module` task** (11-18 dev
   note, PRD 0015: refresh when stale → lite check → my spawn, weekdays 06:00). Through 11-20 nothing ran: `earnings_upcoming`
   is still at 10-19 07:22 and there are no dispute rows after 10-19. Last week's EDGAR screen: **5 of 19 comparable dates
   wrong (26%)**, plus 3 of 8 stored times wrong.
2. **MDT (DB 11-17) and CPRT (DB 11-19) passed with no earnings release filed.** Their stored dates are wrong. First on my
   list when sessions resume.
3. **Source audit:** the pool is empty (no confirms since 10-19; the October census closed 11-15). The next-audit question is
   open in `notes_for_ben.md`.
4. **QRVO** has no CIK in SEC's ticker list (row dated 11-09). Check for a rename or merger before anyone researches it.

## Open Carry-Overs

| Symbol | DB row | Why open | Next check |
|--------|--------|----------|------------|
| MDT | 11-17 | Past DB date, no Item 2.02 filed by 11-22 | First weekday session (≥ 11-23) |
| CPRT | 11-19 | Past DB date, no Item 2.02 filed by 11-22 | First weekday session (≥ 11-23) |
| ITUB | next quarter | 11-03 prediction hit, but it rests on a weekday pattern. Hold until a company date is read | Q4 wave (early Feb) |

**Unresearched:** 75 unconfirmed rows ahead (11-23 → 2027-01-11, 20 due by 11-27), all on dates from the 10-19 feed.
489 past-dated rows parked.
**Confirmed-but-upcoming:** none.

---

## Last Week's Calibration (11-16 → 11-20)

| Metric | Value |
|--------|-------|
| Sessions | **0 of 5** (Earnings Module not yet registered) |
| Dates confirmed | **0** (confirm rate n/a) |
| Confirmed rows that came due | 0 (none were left) |
| Carry-over skips scored | 0 due (ITUB's next check is February) |

**Unresearched rows, EDGAR screen (11-16 → 11-20, 29 rows):** 19 comparable. **14 dates right, 5 wrong**, all ±1d (ACM −1,
PANW −1, BRBR +1, VVV +1, WSM +1; I read the Item 2.02 sentence for each). UGI looked D+1 but is a next-morning filer, so it
held. **Times:** TSN, DIS and VVV were stored `amc`, and all three released bmo. 8 foreign 6-K filers had nothing to compare.
MDT and CPRT haven't reported. Coarse screen, not an audit. File: `analysis/edgar_screen_20261122_1116-1120.tsv`.

**Screen trend (frozen feed), share of comparable dates wrong:** 4% (10-17 → 10-30) → 12% → 32% → 26%. These are small,
coarse samples. Read the trend as "about a quarter wrong", not as improving.

### Source audit #7: not run

Pool = confirmed rows whose date has passed and haven't been checked. That pool is **0** (all 214 October-wave confirms were
checked by audits #3 → #6: 1 miss, JBLU; 1 unverifiable, C).

---

## Maintenance Bookkeeping (11-22)

- **Archived:** 11-01 maintenance entry → fall archive. Ledger still empty.
- **Memory:** new cadence rows ACM, BRBR, VVV, DIS; notes on TSN, WSM, PANW, UGI, MDT, CPRT. The 11-18 Earnings Module note
  is in `project_weekday_research_expected.md`.
- **notes_for_ben:** weekday item → Earnings Module status; audit question carried.
- **Inbox:** 11-18 note filed to `processed/`; root clean. **Outbox** ≤ 128 lines, no rotation. **MEMORY.md** pointers resolve.
