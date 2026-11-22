---
name: project-weekday-research-expected
description: Ben wants the earnings researcher running on weekdays; the 10-20 → 11-06 gap was an accidental side effect of Simple Mode, not a decision
metadata:
  type: project
---

On 2026-11-09 Ben said the earnings agent was supposed to keep running on weekdays and that turning it off was an accident.
The cause: Simple Mode (default since 2026-10-28, `\!main.py (Simple Mode)` task) skips step 1.2 Earnings Intelligence, which
is what spawns this agent, and the Friday 5.3 Earnings Refresh. So `earnings_upcoming` froze at 2026-10-19.

**Why:** I had spent three Sundays (10-25, 11-01, 11-08) recommending "leave weekday research off". That recommendation was
built on the wrong premise that Ben had chosen this.

**How to apply:** don't treat a weekday gap as intended. If weekday sessions stop again, flag it as a probable outage at the
top of STATUS.md. Research only after the calendar refresh has run, or I'll be confirming against stale rows. Related:
[[feedback-window-gating-and-noop]].

**2026-11-18 (dev session, inbox note):** the fix is PRD 0015, the Earnings Module (`tasks/0015-prd-earnings-module.md`
in the parent repo). Phase 1 = a separate `\!Earnings Module` task, weekdays 06:00, in either mode: (a) full calendar refresh
when the last good one is >6 days old (so the first run refreshes before I research), (b) lite yfinance/Finnhub re-check of
rows due ≤21d that writes today's disputes, (c) my spawn, same gate, ≤1/day. Live once Ben registers the task. The poller
(Phase 3) will only write **candidates** I approve or reject; fetchers live in my workspace; Sunday is unchanged.
**Score the 10-20 → first-run gap as an outage, never as a skip pattern.** As of 11-22 it hadn't run (`earnings_upcoming`
still 10-19 07:22, no dispute rows after 10-19).
