# Earnings Researcher — STATUS

> Lightweight dashboard for Ben. Maintained by the Earnings Researcher during its
> weekly maintenance session (`PROMPT_SUNDAY.md`). Glance here for current
> state without reading the full research log.

**Last updated:** 2026-09-13 (weekly maintenance — the first since 06-21)

---

## Needs attention Monday (09-14)

1. **PAYX** — its agent-locked **09-29** now has a `confirmed_row_diverged` flag: yfinance says
   **09-23**. The lock was made 09-08 **without a company source** (a time fix run through the confirm
   tool). Read Paychex's Q1 FY27 advance; correct or re-confirm from it.
2. **KMX** — the same unsourced lock (09-29), no flag yet. CarMax's Q2 advance should be due now.
3. **Your call:** reset both to unconfirmed until then — statement offered in `notes_for_ben.md`.

## Open Carry-Overs

| Symbol | DB date | Why open | Next check |
|--------|---------|----------|------------|
| PAYX | 09-29 bmo (locked) | unsourced lock + drift flag (yfinance 09-23) | **09-14** |
| KMX | 09-29 bmo (locked) | unsourced lock | **09-14** |
| JEF | 09-28 Unknown | dispute: DB 09-28 / finnhub 09-30 / estimates 10-05; advance not out (14d lead, publishes ~16:20 ET) | **09-15**, then daily to ~09-22 |
| UEC | 09-24 amc | FY-end date PR due ~09-17 (7d lead, 07:00 ET); stored `amc` likely should be `bmo` | **09-17** |

**Confirmed-but-upcoming (locked; don't re-research):** LEN 09-16 amc, CTAS 09-23 bmo, GIS 09-23 bmo,
DRI 09-24 bmo, CNXC 09-29 amc, CAG 09-30 bmo, FDS 09-30 bmo, JBL 09-30 bmo, MKC 10-01 bmo,
NKE 10-01 amc, LW 10-06 bmo (weakest-sourced). *(KMX and PAYX are excluded — see above.)*

**Advance-PR windows already open (unconfirmed rows, not yet surfaced):** MU 09-30, MTN 09-28,
STZ 10-06, PEP 10-08; opening ~09-15/16: CCL 09-28, ACN 10-01. ⚠ **ACN (`amc`) and STZ (`bmo`) carry
times that contradict what was established last quarter.** The **10-13 → 10-16 cohort (37 rows —
banks, JNJ, ABT, ASML, TSM…)** starts opening this week: 14 have fresh cadence rows, 23 are first-time
names. Fall phantom watch (late Oct): AES, EA, MKTX, TECH, KVUE, WBD — run the M&A pre-flight first.

---

## Last Week's Calibration (09-08 → 09-11)

| Metric | Value |
|--------|-------|
| Sessions | 4 (09-08 wrote no log block — reconstructed from the DB) |
| Symbols surfaced | 10 disputes + 1 unconfirmed (UEC) |
| Confirmed | **9** — 7 company-sourced, **2 locked without a source (KMX, PAYX)** |
| Skips later proven to be missed confirmable dates | **0** |
| Gate that fired on its predicted day | CTAS (PR 09-09 = predicted due date, 14d lead) |

**Read:** skip judgment held. CTAS and CNXC were both held until the company spoke, and CNXC's own date
(+5d from the anniversary) proved the refusal to lock on `+364d` right. The week's real error was on the
**write** side: two dates locked as a side effect of time fixes, one now flagged by the drift detector.
JEF's advance-PR channel was also wrongly declared absent for a day (overturned 09-09).

## Twelve-Week Look (06-22 → 09-11 — no maintenance ran in between)

- **346 of 439** distinct dispute symbols confirmed (79%); confirms peaked at 80–89/week in the July wave.
- Skip-side misses were all one shape — a lead borrowed from another fiscal quarter or resting on one
  observation (TECH, WSM, ADBE, CPRT, CNM) — and all erred late enough to be caught. Rules for it are in place.
- The costly errors were **locks without a company source**: the 06-30 batch (≥4 of 10 wrong, caught
  07-17) and 09-08 KMX/PAYX. The drift flag caught both.

---

## Maintenance Bookkeeping (09-13)

- **Archived:** active log **3,351 → 702 lines** (478 KB → 56 KB). New
  `memory/archive/research_log_2026-Q3_summer-earnings.md` (sessions 07-01 → 08-28 + the summer's full
  ledger and carry-over table as appendices); late June appended to the spring archive. Two lost session
  headers repaired (07-02, 07-24), six header-embedded sessions restored as blocks, 09-08 stub reconstructed.
- **Cadence table:** +16 rows for the October kickoff cohort; CTAS / KMX / PAYX / ACN / STZ updated.
- **`notes_for_ben.md`:** 716 → 152 lines; original moved verbatim to `notes_for_ben_archive.md`.
  8 open items, 2 new (the PAYX/KMX locks; ten mis-seeded times).
- **Proposal:** `analysis/proposal_20260913_hook_diverged_priority_status_tripwire.md`.
- **Inbox** clean; **outbox** ≤ 128 lines, no rotation; **MEMORY.md** pointers verified, one line updated.
- **Scheduler:** `!Sunday Earnings Researcher` is Ready; next run 2026-09-20 18:00.
