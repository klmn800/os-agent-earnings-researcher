---
name: dispute-snapshot-db-date-is-frozen
description: The db_date in the injected dispute list is frozen at detection time; the live calendar moves underneath it, so a snapshot-vs-final delta is NOT a measure of the correction you made
metadata:
  type: reference
---

`earnings_date_disputes.db_date` is written **when the dispute is detected** and is never refreshed. The live calendar that `earnings_confirm.py` reads keeps moving as the feeds converge. **The two routinely disagree by the time the session runs**, and the injected `<dispute-list>` shows only the frozen value.

Found 2026-08-06, where all three date corrections had already happened on their own:

| Symbol | snapshot `db_date` | live calendar before the write | confirmed |
|--------|--------------------|-------------------------------|-----------|
| FLO | 2026-08-14 | **already 2026-08-20** | 2026-08-20 |
| WOLF | 2026-08-27 | **already 2026-08-19** | 2026-08-19 |
| SJM | 2026-08-27 | **already 2026-08-26** | 2026-08-26 |

In every case the calendar had **already adopted yfinance's date**, and yfinance was right — consistent with [[cadence-364d-weekday-aligned-corroborator]]'s "yfinance dissent ⇒ DB is the suspect side."

## Why it matters

1. **Do not report a snapshot-vs-final delta as a save.** "The DB was wrong by 8 days" was true when the dispute was *detected*, not when the session ran. What the session actually adds in these cases is an **authoritative lock** — `date_confirmed_by='agent'` plus a company URL — on a date that was otherwise resting on an unverified feed. That is real value, but it is a different claim, and overstating it is the kind of thing Ben would have to catch.
2. **The `DaysOut` and `Δ` columns in the session opener can be stale on arrival**, since they are computed off the snapshot.
3. **`earnings_confirm.py`'s `(was: …)` line is the live value** — it is the cheapest way to see the real prior state. Read it rather than assuming the snapshot.

## The rule

Before characterising any correction, check the live row (`earnings_confirm.py --symbol SYM`, or the `(was: …)` output of the write itself). Distinguish three outcomes explicitly:

- **Corrected** — the live calendar was wrong and my write changed it (2026-08-06: only **SJM**, `amc` → `bmo`).
- **Locked** — the live calendar already had the right date from a feed; my write supplied the company source and set `date_confirmed`.
- **Unchanged** — already confirmed, nothing to do.

⚠ Note the asymmetry that made SJM the only real correction that day: the feeds converge on **dates**, but nothing upstream fixes **bmo/amc**. Timing regressions (SJM `amc`→`bmo`, and the FLO / AMCR regime-flip warnings) are the failures only this job catches.

Related: [[company-earnings-cadence]], [[cadence-364d-weekday-aligned-corroborator]], [[confirmed-row-diverged-signal]], [[window-gating-and-noop-sessions]].
