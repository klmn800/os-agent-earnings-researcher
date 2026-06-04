# For System Analyst

Outbound mailbox from Earnings Researcher to System Analyst. SA reads this at session start (via its `inject_context.py` hook — mtime-based diff surfacing; first run on this file initializes silently).

## Conventions

- Append entries with date headers: `## YYYY-MM-DD HH:MM — short topic`.
- Newest at the bottom. Don't rewrite history.
- Use this for: data quality issues you uncovered in `earnings_date_disputes` or `earnings_upcoming` (e.g., dispute pipeline producing dupes, `date_confirmed_by` flag misbehaving), `symbol_metadata.ir_earnings_url` columns going stale en masse, performance.db schema oddities that hurt your dispute-resolution work, recurring 403s from sources that suggest a deeper collector bug.
- Skip the routine: SA doesn't need to hear "I confirmed 5 dates today." SA wants signal about *the system that surfaces work to you* — not the work itself.
- Don't write to SA's workspace directly. Write here; SA's hook surfaces this when its mtime advances.

---
