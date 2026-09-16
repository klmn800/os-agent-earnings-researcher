# Proposal (2026-09-13 Sunday maintenance): two small hook changes + one prompt line

**Status: PROPOSED** — for a dev session. I don't implement hook or prompt changes; flagged in
`notes_for_ben.md` → Proposals.

## 1. Sort `confirmed_row_diverged` first in the injected dispute list

`hooks/inject_context.py` orders disputes with
`PRIORITY = {'date_disagreement': 0, 'both': 1, 'unknown_time': 2}`. `confirmed_row_diverged` has no
entry and falls through to `9`, i.e. **last**. With no `.session_limit` every row is injected anyway, so
today this only changes order; under a limit, the drift flags are the first rows cut.

Why it matters: a drift flag is the **only** way a wrong *confirmed* date resurfaces — a locked row is
suppressed from the normal stream. Record so far:
- **07-17:** four wrong agent-locks from the 06-30/07-02 batch (RTX, LMT, CLF, EQT; −4 to −7d), all
  flagged with yfinance on the right, earlier date.
- **09-11:** PAYX — yfinance 09-23 against a 09-29 locked on 09-08 without a same-quarter source. The
  09-11 session log does not mention it. Whether it was injected and overlooked or inserted after the
  07:16 session ran, I can't tell: `earnings_date_disputes` has no created-at column.

Suggested change: `'confirmed_row_diverged': -1`, and render the line with the confirmed date, the
diverging feed's date and the **signed delta**, so the "yfinance ≥3d earlier ⇒ probable wrong date"
rule (`memory/reference_confirmed_row_diverged_signal.md`) is visible without a lookup.

## 2. `STATUS.md` staleness tripwire

The hook already knows today's date. If `STATUS.md`'s `**Last updated:**` stamp is more than ~10 days
old, append one line to the injected context:
`⚠ STATUS.md last updated YYYY-MM-DD (N days ago) — the Sunday maintenance may not be running.`
The 06-21 → 09-13 gap (12 weeks; active log grew to 3,351 lines / 478 KB, read at every startup) would
have surfaced in early July instead of being noticed by a daily session on 08-26.

## 3. Prompt: state the time-only rule in the daily workflow

`CLAUDE.md` step 5 and the `launcher.py` template show only the full confirm command. Add one line:

> If only the **time** is company-sourced, do **not** use `earnings_confirm.py` — it sets
> `date_confirmed=1` and locks the date. Use
> `direct_db_query.py --db E:/options_scanner/data/datalake.db --write --sql "UPDATE earnings_upcoming SET earnings_time='bmo' WHERE symbol='SYM'"`.

That sentence is the whole 09-08 KMX/PAYX error. (Same edit is a good moment to fix the template's
missing `--write` on steps 6–7 — see `notes_for_ben.md` → Tool fixes.)
