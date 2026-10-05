# Proposal (2026-10-04): disputes crowd the unconfirmed backfill out entirely

> **Status 2026-10-05: options A and D implemented** (Ben's call; interactive session).
> `hooks/inject_context.py` `build_research_queue()` (merged, date-sorted, `TOTAL_CEILING` 25 → 40,
> overflow listed), `launcher.py` sizes the session from the same function, and `PROMPT_TEMPLATE`
> gained Step 0a (read the log header) and a bookkeeping step. B is superseded by A; C (inject
> next-checks directly) remains open.

**For:** Ben, a dev session. **Severity:** high during earnings season; it is happening now.
**Files:** `hooks/inject_context.py` (backfill block, ~line 376), `launcher.py` (`TOTAL_CEILING` sizing, ~line 295).

## What happened (09-28 → 10-02)

The hook injects disputes first, then backfills unconfirmed `earnings_upcoming` rows due ≤14d **only into
the room left under `TOTAL_CEILING = 25`**:

```python
if limit == 0 and len(disputes) < TOTAL_CEILING:
    remaining = TOTAL_CEILING - len(disputes)
```

Disputes per morning last week: **6, 16, 28, 42, 34**. Backfill was 19 → 9 → **0 → 0 → 0**.

The rows that never surfaced are exactly the ones a dispute generator can't see: **all three sources agree,
so there is no dispute, but no company source has been read either.** As of tonight (DB 10-04):

| Date | Unconfirmed, never researched this quarter |
|------|---------------------------------------------|
| 10-13 | ACI (date doubted: 10-20 likely), AMX |
| 10-14 | ASML, BAC, FAST, MS, STT |
| 10-15 | AA, BK, MAN, MRSH, PLD, PNC, SCHW, TSM, USB, **SNA (date doubted: 10-22 likely)** |
| 10-16 | CFG, MTB, TRV |
| 10-17 | HDB, IBN (Saturday-dated, policy Q2 open) |

That's 24 rows reporting in 9 to 13 days. Meanwhile the sessions spent their capacity on disputed rows
dated 10-19 → 11-02. **ACI's 09-30 next-check and SNA's 10-02 next-check never ran**: both rows have
`confirmed_agent` or quiet dispute rows, so they reach a session only via backfill.

The 09-27 maintenance note said overflow "slips a day rather than vanishing". That was wrong. Disputes are
uncapped (with no `--limit`), so the ceiling only ever shrinks the backfill. On a heavy day it goes to zero,
and the dispute count stays high the whole season.

## Why it matters

Agreement among three feeds is weaker evidence than it looks. This quarter's scored cases have all three
wrong together on REXR, LMT and DOC, and SNA is probably a fourth (DB and finnhub agree on 10-15; the
fiscal-calendar arithmetic says 10-22). An undisputed row isn't a confirmed row.

## Options (my preference first)

**A. Merge by earnings date, not by kind.** Build one list of disputes plus unconfirmed rows due ≤14d,
dedupe by symbol, sort by `earnings_date` ascending, and cap the total if a cap is wanted. The nearest
deadline wins whatever its kind. Today that would put the 10-13 → 10-17 rows ahead of the 10-27 disputes.

**B. Reserve a backfill floor.** Keep disputes first but always add the nearest `N` unconfirmed rows
(e.g. `N = 10`) whatever the dispute count. It's a smaller code change than A, but the ordering problem
stays.

**C. Inject the carry-over next-checks.** Parse the "Next check" column of the research-log header, or
better, a small `next_checks` table, and always inject rows whose next-check ≤ today. This closes the
residual gap from the 09-20 proposal too (a next-check on a row >14d out with no dispute). It's
complementary to A or B, not a replacement.

**Session capacity is not the constraint.** The Sonnet sessions handled 34–42 symbols a morning and
confirmed 8–10. The binding cost is reads on rows whose PR doesn't exist yet. A date-ordered list puts
the reads where PRs are most likely to exist.

**D. Give the daily prompt the two lines it's missing** (`launcher.py` `PROMPT_TEMPLATE`). Right now it
never mentions the research-log header, the carry-over table or the cadence table, and it tells the
session to sort `unconfirmed` **last**. The 09-28 → 10-02 sessions did exactly what it says. Suggested
additions:
1. *"Before the injected list, read the header of `memory/research_log.md` (down to `# Research Sessions`):
   carry-overs whose Next check ≤ today and any 'read first' block are part of today's list."*
2. *"Before finishing: for each first-time name you confirmed, add a row to
   `memory/reference_company_cadence.md` (PR date → release date = lead, time, the source that worked),
   and update the carry-over / ledger rows you touched in the log header."*
And with option A, drop the "`unconfirmed` last" sort rule.

Last week's sessions confirmed 36 dates and wrote **zero** cadence rows. Tonight I added 30 new rows from the session
logs and updated 4 (the other 2 already had rows). Lead times are the input to window-gating, so that gap compounds every quarter.

## Stopgap until then (no code)

The Monday header in `memory/research_log.md` lists the never-researched cohort as a **"read these first,
whatever the injected list says"** block, and STATUS.md says the same. That depends on the session reading
the header, which nothing in the daily prompt asks for (see D), so it's a stopgap, not a fix. A one-line
edit to `launcher.py` (D.1) would make it reliable. The orchestrator spawns sessions with that file, so
the edit is Ben's to make.
