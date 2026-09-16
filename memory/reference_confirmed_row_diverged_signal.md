---
name: confirmed-row-diverged-drift-signal
description: The `confirmed_row_diverged` dispute flag with yfinance EARLIER than a stale agent-confirmed date is a high-value wrong-date signal — prioritize it
metadata:
  type: reference
---

`earnings_date_disputes.dispute_reason = 'confirmed_row_diverged'` is the drift-detection output (Proposal 021, `ei_collector.py`): a row with `date_confirmed=1` whose stored date now disagrees with a live feed. These are **not** in the normal dispute stream's mental model (they're already "confirmed"), so they're easy to under-weight — **don't**. On 2026-07-17 they were the single highest-value catch of the session.

## The signal that means "the confirmed date is WRONG"

**A `confirmed_row_diverged` row where yfinance is ~4–7 days EARLIER than the agent-confirmed date ⇒ the confirmed date is very likely stale/wrong.** yfinance had the right date; the confirm was bad.

2026-07-17: an entire **06-30/07-02 agent-confirm batch** was systematically late — RTX 07-28→**07-23** (−5d), LMT 07-28→**07-23** (−5d), CLF 07-27→**07-23** (−4d), EQT 07-28→**07-21** (−7d). All four corrected against the company's own advance PR; all four had yfinance sitting on the correct earlier date, flagged by the drift detector. RTX/LMT/CLF cluster and historically report ~July 22–23, so 27–28 was implausible on cadence too.

## Triage rules

- **yfinance EARLIER than confirmed by ≥3d** → treat as probable wrong-date; verify against the company advance PR now (high impact — these are `date_confirmed=1` so they're suppressed from the normal list and won't self-heal except through this flag).
- **yfinance LATER than confirmed** → usually the *opposite*: yfinance is carrying a stale/estimated later date while the earlier confirmed date is correct from a PR. Checked ENTG/PPL/FLY on 07-17 (yfinance +5/+8/+7d later) — left alone. Verify only if the confirmed date also looks off vs history.
- **±1–2d divergence** → feed noise (VLTO/AEE on 07-17). Ignore.
- Only `date_confirmed_by='agent'` rows are revisable. **Never touch `date_confirmed_by='ben'`** (critical rule) — log disagreement instead.

## Why agent-confirms go stale-late

Likely an earlier session locked a date from an aggregator/estimate or a superseded PR, then the company issued (or moved to) an earlier date. The lock (`date_confirmed=1`) then *prevented* the feed from correcting it — the drift flag is the only escape hatch. Corollary: when locking a date, prefer the company advance PR over any feed/aggregator, and if only an estimate is available, keep `date_confirmed=0`.

## Live case — PAYX, raised 2026-09-11, open at the 09-13 maintenance

Confirmed **2026-09-29 bmo** by agent on 09-08 with **no same-quarter source** (a time fix run through
`earnings_confirm.py`, which locks the date as a side effect — see [[feedback-earnings-confirm-bare-symbol-trap]]).
yfinance now **2026-09-23 (−6d)**. That is the ≥3d-earlier rule above ⇒ **priority verify**. Paychex's Q1
was Tuesday-bmo in 2024 (10-01) and 2025 (09-30); 09-23 would be a Wednesday, so cadence mildly favours
the stored date — which is exactly the kind of prior that lost on RTX/LMT/CLF/EQT. Only the Q1 FY27
advance PR settles it. **Second-order lesson:** both recorded batches of bad agent-locks (06-30 cadence
locks, 09-08 time fixes) had the same root — a date locked without a company source — and the drift
flag caught both. Locking is the error; the flag is the safety net, not the plan.

Related: [[sec-8k-acceptance-time-as-timing-source]] (companion year-ago+364d date sanity-check), [[company-earnings-cadence]], [[window-gating-and-noop-sessions]], [[feedback-direct-db-query]].
