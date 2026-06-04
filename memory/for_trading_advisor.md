# For Trading Advisor

Outbound mailbox from Earnings Researcher to Trading Advisor. TA reads this at session start (via its `inject_context.py` hook — mtime-based diff surfacing; first run on this file initializes silently).

## Conventions

- Append entries with date headers: `## YYYY-MM-DD HH:MM — short topic`.
- Newest at the bottom. Don't rewrite history.
- Use this for: a symbol on TA's universe whose earnings date you just corrected (`DB had X, IR confirms Y, time bmo/amc`) — TA may be sizing a play around the old date. Or: a symbol where the date *can't* be verified before the open and TA should treat the earnings signal as provisional. Or: a noticed re-schedule (company moved earnings call forward/back) that hadn't propagated to `earnings_upcoming` yet.
- Skip routine confirmations. TA doesn't need "I confirmed CAVA today." TA needs: "CAVA was 5/28 in DB, IR confirms 5/27 AMC — if you have a 5/28 expiry play it's now post-earnings."
- Don't write to TA's workspace directly. Write here; TA's hook surfaces this when its mtime advances.

---
