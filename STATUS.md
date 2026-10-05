# Earnings Researcher — STATUS

> Lightweight dashboard for Ben. Maintained by the Earnings Researcher during its
> weekly maintenance session (`PROMPT_SUNDAY.md`). Glance here for current
> state without reading the full research log.

**Last updated:** 2026-10-04 (weekly maintenance)

---

## Needs attention this week (10-05 → 10-09)

1. **🚨 83 unconfirmed rows dated ≤ 10-23 can't reach a daily session.** Disputes (28–42 a day) fill the
   hook's 25-row ceiling, so the unconfirmed backfill is empty. Rows where all feeds agree never surface:
   BAC, MS, TSM, PNC, SCHW (10-14/15), TSLA, IBM, INTC, GE, GM, T, PG (10-20 → 10-22), and more.
   **Ben:** `analysis/proposal_20261004_backfill_crowded_out.md` (A/B fix the hook; D is two prompt lines).
   **Monday-me:** work the READ FIRST block at the top of `memory/research_log.md`, nearest date first,
   before the injected list.
2. **SNA and ACI first thing Monday.** Both stored dates are probably wrong (SNA 10-15 → 10-22, ACI 10-13
   → 10-20) and both checks were missed last week. ACI reports in 8 days if the DB is right.
3. **AMX (10-13) still has no 3Q26 event** in its feed as of 10-02. Read daily. If it's still absent
   ~10-08, say so in notes_for_ben.
4. **HDB / IBN (Saturday 10-17)** need Ben's D−1-amc vs D-bmo rule (`notes_for_ben.md`, policy Q2). Read
   the dates and hold the write.
5. **Slightly overdue advance PRs: EQT (10-20), TSCO (10-22).** Their Q2 leads put the PR at ~10-01, and
   none had appeared by 10-02. Read Monday. If still absent, the stored date is suspect.

## Open Carry-Overs

| Symbol | DB row | Why open | Next check |
|--------|--------|----------|------------|
| SNA | 10-15 bmo (date **probably 7d early**) | 53-week FY2025 ⇒ Q3 ends 10-03 ⇒ **10-22**. Webcast PR ~10-01 ⇒ 10-15 real; none ⇒ 10-22 | **10-05**, 10-09 |
| ACI | 10-13 bmo (date unlocked) | FQ2 arithmetic says **10-20**; 10-13's advance would be overdue | **10-05**, 10-07 |
| AMX | 10-13 amc (finnhub 10-20) | No 3Q26 feed event yet; Tuesday-amc cadence fits 10-13 | 10-05, daily |
| EQT, TSCO | 10-20 / 10-22 | Advance slightly overdue at Q2 lead | 10-05 |
| MMM, VRT, WAL, LRCX, UAL | 10-20 / 10-21 | Time sourced (EDGAR), date not | 10-05 |
| PNR, PEGA · ALK · RHI | 10-20 · 10-22 · 10-21 | 14d · 14d · 7d leads | 10-07 · 10-09 · 10-13 |
| 14 more (GL, QS, SF, TER, VLTO, BPOP, NSC, SLM, ITW, F, FCX, POOL, DECK, BC) | 10-21 → 10-23+ | No company date as of 10-02 | 10-05 |
| IRDM, WBS | 10-22 | Pending acquisitions, no calls (phantom screen) | 10-07 |

Each row's channel and known traps are in the "How to read" column of the research-log header.

**Confirmed-but-upcoming:** 48 rows, 10-06 → 11-02, re-verified against the DB today (0 mismatches).
Weakest: **LW 10-06** (no first-party fetch) and **BX 10-22** (search snippet of a 403'd page).

---

## Last Week's Calibration (09-28 → 10-02)

| Metric | Value |
|--------|-------|
| Sessions | **5 of 5** (all Sonnet) |
| Symbols worked | 60 disputed + 5 backfilled (and **83 undisputed rows never surfaced**) |
| Dates confirmed on a company source | **36** (2 / 8 / 8 / 10 / 8 a day) |
| Time-only (date left open on purpose) | 6: AGNC (later dated), MMM, VRT, WAL, LRCX, UAL |
| Stored values corrected | FNB date 10-15 → **10-19**, CLF amc → **bmo** |
| Wrong writes | 0 found |
| Feed dissents (21 resolved) | yfinance-vs-DB: **yfinance 7/7**. finnhub-only: artifact 9/12, **right 2/12** (KO, TRU). All three wrong: 3/21 |

**Skip judgment:** REXR was called right (10-22, read the morning after its PR). WIT was right. For FNB,
holding was right but the guessed date wasn't (Monday 10-19, not 3rd-Thursday 10-15). ACI and SNA went
**untested** because their checks never ran. Doubts based only on the prior quarter's weekday went
2-for-4, so they're no longer treated as evidence. Only an overdue PR is.
**Leads:** one-observation leads ran long again (FNB 16 → 20d, WIT 9 → ≥14d), now 4 of 4, so the 1.5×
read-window rule stays. October-wave PRs bunched 09-28 → 10-01.

**Sonnet sessions:** research is solid and fast, and the 09-25 bad-read pattern didn't recur. They did
no cadence or header upkeep, but the daily prompt never asks for it (proposal D). Two sourcing slips:
a constructed URL on DOC, fixed at once, and a snippet-only BX confirm, flagged.

---

## Maintenance Bookkeeping (10-04)

- **Archived:** sessions 09-14, 09-15 + the 09-13 maintenance entry → summer archive, verbatim, checked.
  Active log 705 → 667 lines, including the new header block and today's entry.
- **Header rebuilt from the DB:** READ FIRST block (83 rows), carry-overs rebuilt, ledger 48 rows (16
  had been missing).
- **Cadence table:** 30 new rows (fall-wave names), 4 outcomes, wave-level lead pattern, scored
  feed-dissent table.
- **Memory:** window-gating note corrected (the "slips a day" claim) and this week's lead score added;
  stocktitan note updated (new UA, regex, 429 shape). Helpers promoted to `analysis/helpers/` (the old
  `conf.sh` had a hard-coded date).
- **notes_for_ben:** new 🚨 top item; SNA item refreshed (REXR resolved → archive); Sonnet item scored.
- **Inbox** root clean; `inbox/fetch/` now git-ignored. **Outbox** ≤ 128 lines, no rotation.
