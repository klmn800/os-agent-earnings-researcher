# Earnings Researcher — STATUS

> Lightweight dashboard for Ben. Maintained by the Earnings Researcher during its
> weekly maintenance session (`PROMPT_SUNDAY.md`). Glance here for current
> state without reading the full research log.

**Last updated:** 2026-06-14 (weekly maintenance)

---

## Open Carry-Overs

Symbols still unresolved, with current status and the date to re-check (derived from
each company's announcement window — see `memory/reference_company_cadence.md`).
Both are next-check **Monday 06-15**.

| Symbol | Reason still open | Current status (feeds @ 06-12) | Next-check |
|--------|-------------------|--------------------------------|------------|
| JEF | Jefferies Q2 FY26 — no advance businesswire PR yet | Feeds split: DB **06-24 amc** / finnhub 07-01 (`conflict=1`). Cadence favors DB (Q1 released 25d post-quarter-end → ~06-25; finnhub's 31d is atypical). | 2026-06-15 |
| FDX | FedEx Corp — no company advance PR yet | Feeds have **converged on 06-23 amc** (stored=yf=finnhub, `conflict=0`) — corroborates the third-party date but is NOT a company source. FDXF spinco reports 06-25 (don't conflate). | 2026-06-15 |

**Confirmed-but-upcoming (locked; don't re-research):** JBL 06-17 bmo, KMX 06-17 bmo,
ACN 06-18 bmo, KR 06-18 bmo, CCL 06-23 bmo, MU 06-24 amc, PAYX 06-24 bmo, DRI 06-25 bmo,
MKC 06-25 bmo, CNXC 06-29 amc, NKE 06-30 amc, GIS 07-01 bmo.

`earnings_date_disputes` is present and current this Sunday (06-11/06-12 rows persisted) —
the 06-07 Sunday-absence did not recur.

---

## Last Week's Calibration

Window: 2026-06-08 → 06-14.

| Metric | Value |
|--------|-------|
| Symbols confirmed | **14** (13 on 06-11, 1 on 06-12) |
| Skips that later proved to be missed confirmable dates | **0** |
| Last Sunday's 4 carry-overs | All resolved correctly: ORCL/GME/UEC reported 06-09/10 (as feed dates predicted); JBL's advance PR dropped → confirmed 06-17 on 06-11. |
| This week's skips | CCL skipped 06-11 → confirmable 06-12 when PR dropped (clean 1-day-early skip). JEF still split (correctly held). FDX feeds converged but no company PR (correctly held, not locked). |

**Read:** skip judgment stays well-calibrated. The feed-convergence rule held up cleanly —
FDX's feeds agreeing on 06-23 is corroboration, not a company confirmation, so it stays a
carry-over rather than a lock. 06-11 was high-yield (13/16), the opposite of the late-May
0-confirm churn. Standing lever is unchanged: minimize too-early cycles (the window-gating
hook proposal addresses this at the source).

---

## Maintenance Bookkeeping

- **Archived:** 05-28 (truncated stub) + 05-29 (5-confirm) sessions rolled to `memory/archive/research_log_2026-Q2_spring-earnings.md`; active log now ~150 lines.
- **Cadence table:** **+14 symbols** from the 06-11/06-12 confirm wave (ACN, CCL, CNXC, DRI, FDX, GIS, JBL, JEF, KMX, KR, MKC, MU, NKE, PAYX) with lead times, BMO/AMC, and DB-vs-finnhub error notes — now 51 rows (~55 tickers). This is the data behind window-gating.
- **`notes_for_ben.md`:** pruned to one open item (window-gating hook proposal); 5 items moved to Resolved (dispute-list fix, UEC, Sunday-table-absence, restore, weekend-maintenance proposal marked implemented).
- **Inbox:** root clean (README + processed/ only). **Outbox:** all files ≤ 65 lines — no rotation.
- **MEMORY.md:** index pointers verified; no new files this session (cadence already indexed).
