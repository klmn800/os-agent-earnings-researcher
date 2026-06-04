---
name: window-gating-and-noop-sessions
description: Gate research by each symbol's announcement window; be willing to confidently declare a no-op session backed by logged next-check dates
metadata:
  type: feedback
---

Don't reflexively research every surfaced symbol. Gate by the **announcement window**: `window_opens = earnings_date − company_lead_time − small_buffer`, where `lead_time` is that company's historical gap between its advance "to announce"/"Sets the Date" PR and the actual release.

- **Inside the window:** do the cheap check (~1 targeted search + 1 EDGAR FTS per symbol).
- **Outside / too far out:** skip with a one-line logged rationale and a computed **next-check date** — no web calls.
- **Always-on tripwire:** one batched EDGAR FTS sweep across all surfaced CIKs is nearly free and catches the rare early announcement. If it's empty AND every symbol is outside its window, it's correct to end the session: *"nothing actionable today, next check <date>, done."*

**Why:** Ben (2026-05-28) wants me to exercise the judgment to NOT research symbols whose advance PR can't exist yet, and explicitly asked whether I'm confident enough to declare a clean no-op session even with symbols on the horizon (e.g. dates ~3 weeks out). A 3-weeks-out symbol with a 2-week lead time has ~0 chance of an authoritative source today — checking it is confirming a predictable absence. Same day he flagged a 151k-token, 0-confirm session as overwork.

**How to apply:**
- A no-op MUST be auditable: name each symbol's next-check date so it's reasoning, not a lazy shrug. That's the guard against false "nothing to do."
- A `date_disagreement` or a moved finnhub/yfinance date can justify a look even slightly outside the window (something may have shifted). Use discretion.
- Lead times come from the research log history; once the cadence table exists (see weekly-cleanup plan), read window data from there instead of re-deriving. Ideally this logic eventually moves into the context hook so too-early symbols aren't surfaced at all.

Related: [[parse-big-inbox-json-dont-read]] (the other half of the same token-efficiency conversation), [[reference-sec-via-curl]] (the FTS tripwire mechanism).
