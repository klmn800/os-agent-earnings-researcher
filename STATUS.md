# Earnings Researcher — STATUS

> Lightweight dashboard for Ben. Maintained by the Earnings Researcher during its
> weekly maintenance session (`PROMPT_SUNDAY.md`). Glance here for current
> state without reading the full research log.

**Last updated:** 2026-10-11 (weekly maintenance)

---

## Needs attention this week (10-12 → 10-16)

1. **Next Sunday (10-18): source audit #2 goes back in time** (Ben, 10-11). It covers the 29 times set on 07-14 with
   the unreliable UTC→ET conversion, the 10 convergence locks from 06-30, and ~10 summer inferred times. 10-25 then audits
   the weak October confirms. Plan: `analysis/source_audit_20261011.md` → "Next runs".
2. **⚠ Ben: BK has no `earnings_upcoming` row.** It was confirmed 10-15 bmo on 10-06, but the row is gone (last
   snapshot 10-02). If that wasn't deliberate, the scanner will miss BNY's 10-15 print.
3. **ASML reports Wed 10-14 and has no company-sourced read.** Monday's first item.
4. **HDB / IBN (Saturday 10-17)** still need Ben's D−1-amc vs D-bmo rule (`notes_for_ben.md`, policy Q2).
5. **PNR (10-20)** is ~3 business days past its 14d-lead PR, and finnhub says 10-27. **AMX**'s live row moved to
   10-20 with still no 3Q26 feed event. Both are read Monday.
6. **Queue pressure:** disputes rose 32 → 112 a morning against the 40-row ceiling (nearest first). Fine this
   week; by ~10-19 the overflow will reach near-dated rows. Ben: numbers in `notes_for_ben.md`.

## Open Carry-Overs

| Symbol | DB row | Why open | Next check |
|--------|--------|----------|------------|
| ASML | 10-14 bmo | Aggregators only (company sites 403/timeout) | **10-12 first** |
| AMX | 10-20 amc | No 3Q26 event in the Q4 feed yet; the event's lead is unmeasured | 10-12, daily |
| PNR | 10-20 | PR ~3 business days overdue at the 14d lead; finnhub 10-27 | 10-12 |
| ISRG, OMC | 10-20 | No Q3 date PR (ISRG snippet says 10-21 amc) | 10-12 |
| RHI | 10-21 amc | ~7d lead ⇒ PR due ~10-14 | 10-13 |
| SF, TER, VLTO, VRT, SLM, DECK | 10-21 / 10-22 | No Q3 date PR as of 10-09 | 10-12 |
| LVS, PM, SAP | 10-21 | No PR (SAP calendar 403s; says 10-21 22:05 CET) | 10-12 |
| BPOP, ITW, F, FCX, IRDM | 10-22 → later | Not read 10-09; IRDM pending acquisition | 10-12 |
| HDB, IBN | Sat 10-17 | Policy call (Ben) | on Ben's answer |

Plus **~26 never-researched 10-22/10-23 rows** (CMCSA, PG, HON, UNP, AXP, SLB, …), all in the research-log
header checklist. The hook queue now surfaces them on its own.

**Confirmed-but-upcoming:** 110 rows in the DB (10-13 → 11-02), 109 matching the ledger with 0 date/time
mismatches, plus BK (ledger only, item 2). Weakest: **BX** (search snippet), **GM, CME, MSCI** (search summaries),
**SCHW** (date inferred from the Business Update).

---

## Last Week's Calibration (10-05 → 10-09)

| Metric | Value |
|--------|-------|
| Sessions | **5 of 5** |
| Dates confirmed | **70** (4 / 27 / 10 / 10 / 19) |
| Stored dates corrected | SNA +7d, EQT +7d, BC +7d, WST +7d, CARR +2d, WAL −2d |
| Times corrected / filled | EFX, TSM amc → bmo; ALK, POOL, TSCO, DXCM Unknown → set |
| Wrong writes found this week | 0 |
| **Source audit (all 50 confirms dated 09-01 → 10-09)** | **Dates 49/50, times 49/50, 0 unverifiable.** Misses: DELL (pre-listed date moved −2d), GME (inferred amc, was 9:00 AM) |

**Skip/doubt judgment:** **SNA right** (53-week arithmetic ⇒ 10-22). **ACI wrong**: the stored 10-13 held, and my
quarter-end-offset prediction (10-20) was n=2 arithmetic, now demoted. **Overdue-PR doubts went 2 right (EQT, WAL),
1 wrong (TSCO, whose date held after the PR came 8d late), 1 pending (PNR).**
**Leads:** multi-observation leads held to the day (SNA, ACI, EQT). One-observation leads are noisy both ways:
TSCO ran short (21 → 13d), the first short one after 4 long.
**Queue (A + D):** both are working. The invisible-row backlog fell 83 → 46, and sessions now write their own cadence rows
(the only gap was 10-05, which ran on the old prompt).

---

## Maintenance Bookkeeping (10-11)

- **Audit:** `analysis/source_audit_20261011.md` (5 subagents, both mismatches re-checked on EDGAR by me).
- **Archived:** sessions 09-22 → 09-25 + the 09-20 maintenance entry → summer archive (now closed, 07-01 → 09-25).
  Active log 863 → 668 lines.
- **Header rebuilt from the DB:** READ FIRST block retired (the hook merges the queue now); new 46-row "still unconfirmed
  ≤ 10-23" checklist; carry-overs rebuilt; ledger pruned (LW, STZ, PEP, DAL) and checked against the DB.
- **Memory:** cadence outcomes for ACI, DELL, GME; rows for TXN, HIG, NSC; SEC timing note extended (2 EDGAR quirks);
  MEMORY.md pointers all resolve.
- **notes_for_ben:** 3 resolved items archived; 3 new (audit question, BK, queue pressure).
- **Inbox** root clean. **Outbox** ≤ 128 lines, no rotation.
