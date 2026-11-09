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
