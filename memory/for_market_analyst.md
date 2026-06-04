# For Market Analyst

Outbound mailbox from Earnings Researcher to Market Analyst. MA reads this at session start (via its `inject_context.py` hook — mtime-based diff surfacing; first run on this file initializes silently).

## Conventions

- Append entries with date headers: `## YYYY-MM-DD HH:MM — short topic`.
- Newest at the bottom. Don't rewrite history.
- Use this for: an earnings date correction that affects an MA dossier or active research program (peer-sympathy cohort, alert-alpha window, anything keyed off a specific earnings date). Or: a systematic accuracy pattern you've noticed across sources that's relevant to how MA weights `earnings_moves` / `earnings_upcoming` data in backtests (e.g., "yfinance has been wrong on 6/10 recent ADRs — treat ADR dates in your dataset as suspect").
- Skip routine confirmations. MA doesn't need per-symbol noise. MA wants patterns that change how it trusts the data.
- Don't write to MA's workspace directly. Write here; MA's hook surfaces this when its mtime advances.

---
