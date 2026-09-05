# Earnings Researcher — STATUS

> Lightweight dashboard for Ben. Maintained by the Earnings Researcher during its
> weekly maintenance session (`PROMPT_SUNDAY.md`). Glance here for current
> state without reading the full research log.

**Last updated:** 2026-06-21 (weekly maintenance)

---

## Open Carry-Overs

**None.** All carry-overs cleared on 06-18 (FDX → 06-23 amc; JEF → 06-24 amc). No symbols
are open going into the week of 06-22 — the late-June reporting cluster is fully confirmed
and locked below.

**Confirmed-but-upcoming (locked; don't re-research):** FDX 06-23 amc, CCL 06-23 bmo,
MU 06-24 amc, PAYX 06-24 bmo, JEF 06-24 amc, DRI 06-25 bmo, MKC 06-25 bmo, CNXC 06-29 amc,
NKE 06-30 amc, STZ 06-30 amc, GIS 07-01 bmo, FDS 07-01 bmo.

After this cluster reports, the calendar quiets until the mid-July Q2 wave begins.

---

## Last Week's Calibration

Window: 2026-06-15 → 06-21. Only two weekday sessions (06-15, 06-18).

| Metric | Value |
|--------|-------|
| Symbols confirmed | **4** (all on 06-18: JEF, STZ, FDS, FDX) |
| Skips that later proved to be missed confirmable dates | **0** |
| 06-15 skips (JEF, FDX) | Both correctly held as carry-overs (no company source yet) → **both confirmed 06-18 at the predicted dates.** |

**Read:** a clean week-long validation of skip judgment. JEF's Business Wire advance dropped
06-16 — ~8d before the 06-24 release, dead-on the cadence table's ~10d lead — and resolved
the dispute in DB's favor over finnhub's atypical 07-01. FDX confirmed 06-23 amc once a
company source was available. The feed-convergence rule held both times: I did not lock on
converging feeds, only on the company source. **The one friction point was tooling, not
judgment** — FDX has no machine-readable source, so Ben had to paste the rendered IR page
(flagged as a recurring gap in `notes_for_ben.md`). 06-15 was a 0-confirm session but the
correct kind: 2 carry-overs checked at their next-check date, verified not-yet-out, held.
Standing lever unchanged: push window-gating into the hook to remove even the cheap hand-skips.

---

## Maintenance Bookkeeping

- **Archived:** the **06-11** session (13-confirm late-June wave) rolled to
  `memory/archive/research_log_2026-Q2_spring-earnings.md`; the 06-07 maintenance note also
  rolled off. Active log back to ~140 lines.
- **Cadence table:** **+2 symbols** — STZ (Constellation, fiscal Q1, ~4wk lead, amc w/ bmo→amc
  correction) and FDS (FactSet, fiscal Q3, ~4wk lead, 9am ET = bmo). Rewrote the FDX row
  (browser-render-only, no scrapeable source; next call Q1 FY27 = 2026-10-28) and strengthened
  JEF (Business-Wire ~10d lead + cadence-over-finnhub call both vindicated). Now ~53 rows.
- **`notes_for_ben.md`:** +1 open item — the **FDX browser-render-only tooling gap** (recurs
  every quarter; suggested finding the IR events JSON endpoint). Window-gating-hook proposal
  still open. Stray `memory/for_*.md` duplicates: `rm` denied again — still needs Ben.
- **Inbox:** root clean (README + processed/ only). **Outbox:** all files ≤ 65 lines — no rotation.
- **MEMORY.md:** index pointers verified; no new files this session (STZ/FDS folded into the
  existing cadence table).
