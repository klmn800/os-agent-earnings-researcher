# Earnings Researcher — STATUS

> Lightweight dashboard for Ben. Maintained by the Earnings Researcher during its
> weekly maintenance session (`PROMPT_SUNDAY.md`). Glance here for current
> state without reading the full research log.

**Last updated:** 2026-09-27 (weekly maintenance)

---

## Needs attention this week (09-28 → 10-02)

1. **REXR — check Monday 09-28.** The stored 10-14 is probably wrong (advance PR overdue since 09-20);
   10-22's PR is due by 09-28. Monday has **no unconfirmed row inside the 14-day horizon**, so a session
   runs only if a dispute flags. REXR/AMX/WIT have flagged every day since 09-22, so it probably will. If
   Tuesday's hook shows a missed-session warning, REXR is the row that slipped.
2. **The 10-13 → 10-17 cohort hits the horizon: 25 unconfirmed rows from 09-29 to 10-03** (JPM, WFC, JNJ,
   UNH, DPZ, then BAC, MS, ABT, ASML, FAST, STT, then the 10-15 banks + TSM, …). Their advance PRs are
   almost certainly already out. Front-load: clear the 10-13/10-14 names as early as possible.
3. **AMX feed: re-cache the IR URL with `pageSize=100`** (the cached one returns 2014 events first;
   that's why 09-25 saw nothing). A DB write, so it waits for a weekday session.
4. **HDB / IBN are dated Saturday 10-17.** They need Ben's D−1-amc vs D-bmo rule (`notes_for_ben.md`,
   policy question 2) before they surface ~10-03.

## Open Carry-Overs

| Symbol | DB row | Why open | Next check |
|--------|--------|----------|------------|
| REXR | 10-14 amc (date **probably wrong**) | Advance PR overdue for 10-14; 4th-Thursday cadence ⇒ **10-22** expected | **09-28**, 09-29 |
| AMX | 10-13 amc (finnhub 10-20) | No 3Q26 event in the company feed as of 09-24; Q3 is always Tuesday amc, 10-13 fits | **09-29**, 10-06 |
| ACI | 10-13 bmo (date unlocked) | FQ2 arithmetic says **10-20** (38d after quarter-end, 2 obs); advance PR due 09-29 / 10-06 | **09-30**, 10-07 |
| FNB | 10-15 amc (date unlocked) | Scheduling PR due ~09-29 (16d lead, 1 obs) | **09-30**, 10-01 |
| SNA | 10-15 bmo (date **probably 7d early**) | 53-week fiscal 2025 ⇒ **10-22**; the webcast PR settles it (10-01 vs 10-08) | **10-02**, 10-09 |
| WIT | 10-15 bmo (finnhub 10-13) | Thursday cadence fits 10-15; advance ~9d lead | **10-06**, 10-07 |

Each carry-over row in `memory/research_log.md` now has a **"How to read"** column with the working
channel and its known traps.

**Confirmed-but-upcoming:** 25 rows, 09-28 → 10-20, all re-verified against the DB today (ledger in the
research-log header). Weakest: LW 10-06 (no first-party fetch). Inferred times: CAG, DAL (bmo, from the
call time).

---

## Last Week's Calibration (09-21 → 09-25)

| Metric | Value |
|--------|-------|
| Sessions | **4 of 5** (09-22 → 09-25; 09-21 didn't run under the old dispute gate). First Sonnet session: 09-25 |
| Unique symbols surfaced | 21 |
| Dates confirmed on a company source | **15 (71%)**: UEC, CCL, MU, ACN, STZ, C, PGR, SYF, FHN, PEP, ERIC, JBHT, RF, TFC, DAL |
| Time-only (date left open on purpose) | 3: ACI, FNB, SNA |
| Held | 3: AMX, REXR, WIT |
| Wrong stored values corrected | **UEC** date +5d and time; **ACN** amc → bmo; **STZ** bmo → amc. Plus 9 `Unknown` times filled |
| Wrong writes | 0 |
| finnhub dissents that were right | **0 of 4 resolved** (JBHT, PGR, SYF, FHN). 3 still pending (AMX, REXR, WIT) |

**Skip judgment:** no gated symbol reported or moved inside its skip. **Leads with a stable channel held to
the day** (ACN 16d, UEC 7d, CCL within a day). **Both 1-observation leads borrowed from another fiscal
quarter undershot** (PEP 35 → 44d, MU 28 → 35d), so their windows opened a week before the table said and
PEP's PR sat unread for 30 days. No harm (both DB dates were right), but the cost was lead time. Rule
added to `feedback_window_gating_and_noop.md`: start reading a 1-obs row at ~1.5× the lead. n=2, so it's
a working rule, not a law. The CCL miss (PR 09-15, check scheduled 09-16, never ran) was the dispute
gate, now fixed.

**Drift:** the 09-25 session made two bad reads (AMX feed, REXR list) that it logged as absences, and skipped
its bookkeeping. Part of the AMX cause was a stale memory note of mine. Fixed today; details in
`notes_for_ben.md`. One session, so no conclusion about the model yet.

---

## Maintenance Bookkeeping (09-27)

- **Archived:** sessions 09-08 → 09-11 (216 lines) → summer archive, verbatim, integrity-checked.
  Active log **679 → 519 lines** (incl. today's entry). Header rebuilt from the DB (6 carry-overs, window watch, 25-row ledger
  sorted by date; CTAS/GIS/PAYX/DRI pruned as reported).
- **Cadence table:** RF, TFC added (first-time names 09-25 never wrote); DAL closed out; AMX row's URL
  fixed; REXR row flags the 09-25 bad read.
- **Memory:** `reference_q4_event_feed.md` corrected (it said `sortDirection=desc` works; it doesn't).
  Window-gating note: spawn fix verified in code + residual gap + the lead-table score. `MEMORY.md`
  lines updated.
- **`notes_for_ben.md`:** spawn-gate item → archive (resolved); re-seeding item condensed (9/10 fixed);
  SNA item now also covers REXR; new Sonnet-session item; HDB/IBN added to policy Q2.
- **Inbox** clean, **outbox** ≤ 128 lines, no rotation.
- Committed the uncommitted 09-25 session along with today's work.
