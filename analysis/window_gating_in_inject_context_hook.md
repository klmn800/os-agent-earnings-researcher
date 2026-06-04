# Proposal: Move window-gating into `hooks/inject_context.py`

**Author:** Earnings Researcher agent
**Date:** 2026-05-28
**For:** Ben → dev session to implement
**Status:** proposal / awaiting decisions

---

## Goal

Stop surfacing earnings symbols in the daily `<dispute-list>` *before their advance-PR window has opened*, so the agent doesn't burn a session "skipping" symbols whose authoritative source can't exist yet.

## Why now

This wasn't feasible until today — it needs per-symbol lead times, which didn't exist as data until this maintenance session created `memory/reference_company_cadence.md`. It directly attacks the drift flagged in this week's calibration: the 05-27 and 05-28 sessions were 0-confirm because *every* surfaced symbol was an early-to-mid-June reporter whose "to Announce"/"Sets the Date" PR hadn't dropped. The agent already knows to skip these by judgment (`memory/feedback_window_gating_and_noop.md`), but it still has to spend the session doing so. Gating upstream in the hook removes the churn entirely.

## The mechanic

For each candidate symbol the hook would otherwise surface:

```
window_opens = earnings_date − lead_time − buffer
```

- `lead_time` = that company's historical advance-PR → release gap (from the cadence table; ~14d default if unknown).
- `buffer` = small (2–3d) so an early PR isn't missed.
- If `today < window_opens` → **don't surface it as actionable**; instead emit a one-line `outside window, next-check YYYY-MM-DD` so it's auditable, not silently dropped.

Guardrails (carry over from `feedback_window_gating_and_noop.md`):
- Still run the cheap **batched EDGAR FTS tripwire** across all surfaced CIKs each session — nearly free, catches the rare early announcement even when every symbol is "outside window."
- **Bypass the gate** for `date_disagreement` or a moved yfinance/finnhub date — something may have shifted, worth a look.
- UEC-class symbols (no advance PR for the quarter) have effectively zero lead time → gate on the expected 10-Q-drop date instead.

## Decisions for Ben

1. **Where should lead-time data live for the hook to read?** Options: (a) parse `reference_company_cadence.md` directly — human-friendly but markdown parsing is fragile; (b) promote lead times to a structured sidecar (e.g. `memory/cadence.json` the agent maintains alongside the table) — robust to parse but duplicates data; (c) a column in `symbol_metadata`. *My lean: (b), generated from the table, so the table stays the human-readable source of truth.*
2. **Suppress vs. down-rank.** Hard-hide outside-window symbols, or still list them under a collapsed "outside window" footer? *My lean: footer — keeps it auditable and lets me override.*
3. **Default lead time** for symbols not yet in the cadence table. *My lean: 14d (typical "to Announce" lead).*

## Related
- `memory/feedback_window_gating_and_noop.md` — the agent-judgment version of this; the hook change is the upstream automation of it.
- `memory/reference_company_cadence.md` — the lead-time data source.
- `analysis/weekend_cleanup_proposal.md` — the cadence table was proposed there as "doubles as the data for window-gating."
