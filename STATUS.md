# Earnings Researcher — STATUS

> Lightweight dashboard for Ben. Maintained by the Earnings Researcher during its
> weekly maintenance session (`PROMPT_SUNDAY.md`). Glance here for current
> state without reading the full research log.

**Last updated:** 2026-10-18 (weekly maintenance)

---

## Needs attention this week (10-19 → 10-23)

1. **❓ Ben: another source audit next Sunday (10-25)?** It would cover the October dates that have passed by then
   (GM, MSCI, CME, ELV, MOH, BX, SCHW, ASML …). This week's results are below; the question is in `notes_for_ben.md`.
2. **⚠ Ben: HDB / IBN are past-dated.** Both are still unconfirmed at Saturday 10-17. Either rule moves the date (10-16 amc
   or 10-19 bmo); I'm holding for your policy Q2 answer.
3. **⚠ Ben: BK still has no `earnings_upcoming` row** (BNY reported 10-15; my confirm is in the archive only).
4. **Monday's first reads:** AMX (10-20, still no 3Q26 event in its feed), ISRG (10-20, no PR 4 days out), OMC (row moved to
   10-22 with no source), DOW / IRDM / SCCO (10-22), INFY (10-23, time probably bmo, DB says amc).
5. **Possible prompt tweak (Ben's call):** a PR that gives only a *morning call time* doesn't date the release. Details in
   `notes_for_ben.md` → audit #2.

## Open Carry-Overs

| Symbol | DB row | Why open | Next check |
|--------|--------|----------|------------|
| AMX | 10-20 amc | No 3Q26 event in the Q4 feed (read daily) | 10-19 |
| ISRG | 10-20 amc | No Q3 date PR; IR 403s | 10-19 |
| OMC | **10-22** amc (moved from 10-20, unsourced) | No Q3 date PR | 10-19 |
| DOW, IRDM, SCCO | 10-22 | No PR; IRDM may hold no call (Rocket Lab deal); SCCO's stocktitan listing 404s, use search | 10-19 (SCCO 10-21) |
| INFY | 10-23 amc | Date from news coverage of the board filing only; time likely bmo | 10-19 |
| BMRN, ARE | 10-26 | No PR | 10-19 |
| CNC, FCX, GLW | 10-27 | No Q3 date PR | 10-19 |
| DVA, NVT, XOM, MKTX, EBAY | 10-28 → 11-05 | No PR (DVA overdue vs Q3'25 lead) | 10-19 |
| WHR, DTE, OSK | 10-28/29 | No PR; WHR's Q3'25 notice came 10-20 | 10-20 |
| HDB, IBN | Sat 10-17 (past) | Policy call (Ben) | on Ben's answer |

**Confirmed-but-upcoming:** 160 rows (10-19 → Nov), **160/160 match the DB, 0 mismatches** (checked 10-18). Weakest still
ahead: MSCI, GM (10-20, search summaries), CME (10-21), ELV, MOH (10-21, biopharmawatch copies), BX (10-22, search snippet).

---

## Last Week's Calibration (10-12 → 10-16)

| Metric | Value |
|--------|-------|
| Sessions | **5 of 5** |
| Dates confirmed | **80** (14 / 19 / 12 / 15 / 20), 40% of the 200 queue rows |
| Stored dates corrected | PNR +7d, MAT +7d, KMB +2d, RHI +1d, PII +1d, FLS +1d |
| Times corrected / filled | NEM bmo → amc, JCI amc → bmo; DECK, CDNS, GILD Unknown → amc |
| Wrong writes found this week | 0 among last week's writes. The audit found 12 old summer misses (below) |

**Skip/doubt judgment:** TER, PNR, KMI and RHI predictions held. "Overdue PR" doubts on GILD and MDLZ were wrong (dates
held). Running tally **3 right / 3 wrong**, so an overdue PR means look again, not that the date is wrong.
**Rule-6 check on last week:** BA and JCI were timed from a morning call alone. Both are safe: EDGAR shows same-morning releases for 5 straight quarters.

### Source audit #2: summer writes on weak sources (n = 58, census, all mismatches re-checked)

| Source type | n | date right | time right |
|---|---|---|---|
| Feed agreement + cadence lock | 12 | **6** | 12 |
| Time from SEC filing history | 29 | 27 (unsourced) | 28 |
| Time inferred from call time | 12 | 10 | **9** |
| Time from home-market clock | 5 | 5 | 5 |

Report: `analysis/source_audit_20261018.md`. (Audit #1, 10-11: September's company-sourced confirms, dates 49/50, times 49/50.)

---

## Maintenance Bookkeeping (10-18)

- **Archived:** sessions 09-28 → 10-02 + the 09-27 maintenance entry → new **fall archive**; 31 reported ledger rows → its
  Appendix A. Active log 787 → ~565 lines.
- **Memory:** cadence rule 6; rows PPL, FLY, UGI, AMTM, UUUU added, WAL rewritten, CNP/CLF/RTX annotated; SEC timing note
  extended; MEMORY.md pointers all resolve.
- **notes_for_ben:** audit #1 archived, audit #2 + question added; HDB/IBN, BK, SCHW updated. `rm` of two temp drafts denied
  (listed for Ben).
- **Inbox** root clean. **Outbox** ≤ 128 lines, no rotation.
