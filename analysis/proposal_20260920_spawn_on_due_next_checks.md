# Proposal (2026-09-20 Sunday maintenance): don't let a zero-dispute morning cancel the session

**Status: IMPLEMENTED 2026-09-24 (A + C; B skipped).** Ben's dev session: `ei_lite_refresh.py` spawns on
`disputes or unconfirmed rows due within 14d` (`_count_due_unconfirmed`), `launcher.py` mirrors the gate
(`get_due_unconfirmed`, horizon/ceiling imported from the hook), and `hooks/inject_context.py` emits a
missed-session line (`missed_session_warning`) in both the daily and Sunday blocks. B was skipped because a
next-checks file the agent maintains can go stale the same way. Original text follows unchanged.

~~**Status: PROPOSED** — for a dev session. I don't implement orchestrator/launcher changes; flagged in
`notes_for_ben.md` → Open (top item) and `STATUS.md`.~~

## What happened

No daily session ran on **09-16, 09-17 or 09-18** (no transcript, no log block, no dispute rows). The
orchestrator ran normally each morning; its lite refresh logged:

| Day | Unconfirmed rows in the 21-day scope | Disputes flagged | Agent spawned |
|-----|--------------------------------------|------------------|---------------|
| 09-15 | 6 | 1 (JEF) | yes |
| 09-16 | 5 (1 date updated) | 0 | **no** |
| 09-17 | 7 | 0 | **no** |
| 09-18 | 7 | 0 | **no** |

Two independent gates both require a dispute:

1. `strategies/earnings_intel/ei_lite_refresh.py:339` — `if disputes and spawn_agent: _spawn_earnings_researcher(...)`
2. `agents/earnings_researcher/launcher.py` daily mode — `if not all_disputes: print("No unresolved earnings date disputes for today. Nothing to do."); return`

But the session has a second job that doesn't depend on disputes: the hook's **unconfirmed backfill**
(`hooks/inject_context.py`, `HORIZON_DAYS = 14`) and my **logged next-check dates**. Those only ever ran
because some other symbol's dispute happened to fire the launcher that day. This week nothing did.

## What it cost (known so far)

- **UEC** — reports **09-24**, unconfirmed, stored `amc` believed wrong (`bmo` expected). Next-check was
  09-17 (the day its 7d-lead advance PR was due). Never ran.
- **CCL** — next-check 09-16. Never ran. The feed moved its date 09-28 → 09-29 in the meantime, unsourced.
- **MU** (09-30) and **ACN** (10-01, stored time contradicts every observed quarter) entered the 14-day
  horizon on 09-16/09-17 and were never surfaced.
- No wrong write resulted — the cost is lost lead time on four rows, one of them 4 days from its event.

This gets more likely, not less, between seasons: the dispute count is thinnest exactly when the
remaining rows are the off-cycle names (Aug/Sep fiscal quarter-ends) that need the advance-PR watch.

## Suggested change (smallest first)

**A. Spawn on "disputes OR unconfirmed rows inside the hook's horizon."** In `ei_lite_refresh.py`, the
refresh already has the unconfirmed set in hand (`Scope: N unconfirmed symbols within 21 days`). Spawn
when `disputes` is non-empty **or** any unconfirmed row has `earnings_date <= today + 14`. Mirror the
same condition in `launcher.py`'s early-exit so the two gates agree. Window-gating
(`memory/feedback_window_gating_and_noop.md`) already makes a nothing-actionable session cheap — a
handful of cadence greps and a logged no-op.

**B. (Tighter, more work.) Spawn only when something is *due*.** Have the Sunday session write a small
machine-readable `next_checks.json` (`{"UEC": "2026-09-17", ...}`) next to `STATUS.md`; the launcher
spawns if `disputes` or any entry is `<= today`. Avoids sessions on days when every unconfirmed row is
gated, at the price of a file I have to keep accurate. I'd start with A and only move to B if the
no-op sessions turn out to be a nuisance.

**C. Independent of A/B — make the miss visible.** One line in the hook when the newest
`## Session:` header in `research_log.md` is more than one trading day old:
`⚠ Last logged session YYYY-MM-DD — N trading day(s) had no session; check missed next-check dates.`
Same family as the `STATUS.md` staleness tripwire in `proposal_20260913_…`.

## Side note found while reading the launcher

`launcher.py` daily mode writes `.session_mode = 'daily'` **before** its dispute check, which is good:
it means a zero-dispute run still clears Sunday's `weekend` marker. But if nothing invokes the launcher
at all on a zero-dispute day (gate 1), the marker stays `weekend`, and a `claude` session opened by
hand in the workspace would get the maintenance block instead of the backfill. Read from the code, not
tested.
