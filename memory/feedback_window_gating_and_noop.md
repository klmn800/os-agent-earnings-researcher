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

**Why:** Ben (2026-05-28) wants me to exercise the judgment to NOT research symbols whose advance PR can't exist yet, and explicitly asked whether I'm confident enough to declare a clean no-op session even with symbols on the horizon (e.g. dates ~3 weeks out). Checking a symbol whose PR cannot exist yet is confirming a predictable absence. Same day he flagged a 151k-token, 0-confirm session as overwork.

⚠ **The lead times are much wider than first assumed — use each company's own, never a generic default.** Observed: RHI **7d**, ETSY/FOUR **14d**, DIS **22d**, **CE 40d** (2026-06-25 PR → 08-04 release). The original framing here ("a 3-weeks-out symbol with a 2-week lead has ~0 chance") is **empirically false** — CE would have been gated out and its confirm missed. There is no safe blanket "too early" window; a symbol 3–6 weeks out can already have a live PR. The gate is only trustworthy per-symbol, off a lead time **verified from that company's own PR text** (see [[company-earnings-cadence]]).

⚠⚠⚠ **2026-08-12 — the absence argument failed outright, and it cost a wrong recommendation to Ben.** TECH was held for **eight sessions** on an escalating "no advance PR ⇒ probable phantom earnings event" case, ending in the written advice *"do not trade an 08-12 TECH earnings event."* Bio-Techne then filed its Item 2.02 8-K on 08-12 at 06:30:30, dead on its 8-quarter furnish minute. **The DB date was right the whole time.** Anatomy of the failure, because each part recurs:

1. **The lead time was measured on the wrong quarter.** The "~14–22d" gap came from TECH's *Q3* cycle. Nobody ever checked whether a *fiscal-Q4* advance PR exists at all — so eight sessions measured silence against a channel never shown to exist for that quarter. Third occurrence of this exact shape (FLO: right company, wrong feed; NTRA: current feed, wrong channel).
2. **One signal restated six times read as six independent signals.** "No PR," "feed current through 07-08," "IR calendar empty," "no scheduling 8-K," "nothing in search," "`+364d` already past" are not six lines of evidence — five of them are the same absence, and the sixth was arithmetic that also turned out wrong.
3. **A plausible mechanism laundered a hunch into a finding.** The live Merck KGaA merger made the AES/EA phantom shape *available*, and availability got treated as support. A registrant filing merger paperwork still has to report its quarter.

**The one-search test that would have killed it on day one: did the YEAR-AGO same quarter have an advance PR before it?** Run that before building any absence case.

**Rule: an absence argument is only as strong as the verified existence of that channel for the MATCHING quarter.** Absent that verification the honest output is **"date unsourced — holding,"** never "probable phantom." Holding was correct here; the confident narrative wrapped around the hold was not, and the narrative is what reached Ben. See [[company-earnings-cadence]] (TECH row) and [[ma-phantom-earnings-dates]] — real phantoms exist (AES, EA, APLS, the MKTX variant), which is exactly why the bar for calling one has to be a *positive* finding, not a stack of absences.

✅ **2026-08-17 (PVH) — the gate as a DETECTION tool, plus an intraday dimension nobody had noticed.**
Two things this technique had not yet shown, both proven in one session:

1. **An overdue PR is a positive finding about the DB date, not just a reason to keep waiting.**
   PVH's lead is 15–16d off a verified matching-quarter channel, so by 08-17 the PR for the DB's
   08-25 date was **7 days late**. The PR then landed and said **09-02** — DB was wrong by 8d.
   Nothing else saw it: no feed dissented (an `unconfirmed` row, not a dispute) and `+364d`
   confidently reproduced the wrong date. So the window arithmetic is not only a way to skip
   cheaply — **"the PR is N days overdue against a verified lead" is evidence the date is wrong**,
   and it is sometimes the *only* evidence available. See [[cadence-364d-weekday-aligned-corroborator]].
   ⚠ It says the date is wrong; it does **not** say what's right. The replacement date guessed
   from cadence (09-01) was also wrong. **Distrust and watch — never write.**
2. ⚠⚠ **The window has an intraday dimension: a session can be too early *in the day*.** PVH
   publishes its advance PR **Monday 09:00 ET** (3/3). This session's first read was 07:20, and
   read "no PR" — a structurally guaranteed absence, exactly the thing this whole memory exists
   to avoid, just on a scale of hours instead of days. Since sessions start ~07:1x–07:2x, **any
   symbol whose observed publication time is after ~07:30 cannot be answered by the opening read.**
   The fix is cheap and it worked: a **background poll** on the known publication minute
   (`analysis/pvh_poll_20260817.py` → `.out` file, 21 empty cycles then a hit at 09:01:13), same
   technique as the 08-04 BR confirm. Write the poll output to a **file**, so a session that ends
   early hands the answer to the next one instead of making it re-derive the gate.
   **So: before treating a morning absence as evidence, check the company's publication time in
   [[company-earnings-cadence]] — if it's after the session start, poll, don't conclude.**

⚠ **2026-08-21 (WSM) — the gate's own input failed, in the mildest possible way, and that is why it is worth writing down.** WSM's lead was recorded as **2d** off a single Q1 observation; the Q2 advance PR ran **7d** (08-19 09:00 ET → 08-26). So `next_check = 08-24` was 5 days late, and the 08-20 session logged "not probed at all — zero requests, by design" while the PR sat live on the feed. It cost nothing (08-24 would still have beaten the 08-26 release) and it was caught by a read spent on a *different* question — but it is the TECH shape again in miniature: **an absence measured against a lead time nobody had verified across quarters.**

Two rules fall out, both now in [[company-earnings-cadence]]:
1. **Gate off the LONGEST observed lead, and count the observations.** A 1-quarter lead makes the gate advisory only — read the feed anyway, it is one curl. 3+ consistent quarters make it trustworthy. Auditing today's set this way cleared ORCL (3 obs) and CPRT (4 obs) and flagged only WSM.
2. **`next_check` = `PR_due_date + 1`.** Advance PRs overwhelmingly publish after the session start (GWRE 16:15 ET, ORCL 16:01, GTLB 16:05, CPRT post-16:00, WSM 09:00, PVH 09:00), so a morning read only sees prior-day PRs. GWRE proved the benign version the same session — PR at **08-20 16:15**, invisible to the 08-19 and 08-20 morning sessions, caught 08-21. Those were structural non-misses, not failures.

⚠ Note the asymmetry that keeps this from becoming "just check everything": the gate was wrong on **1 of 4** symbols, the error was **free**, and the three sound gates each saved a research cycle. The fix is a better-calibrated gate, **not** abandoning gating.

✅ **2026-08-24 (CPRT) — audit the gate on the days the gate gives you back.** Both of today's
symbols were correctly skippable inside two minutes, so the session had budget and nothing to spend
it on. It went into asking *why* CPRT was being skipped — and the stated reason ("BusinessWire is the
only channel") turned out to have **never been verified**, because every Copart host is NXDOMAIN or
bot-walled and the check looked impossible. EDGAR answered it in four cheap reads: none of the four
known advance-PR dates produced an 8-K, so the advance PR is **verifiably** not an EDGAR document —
the hold now rests on a checked non-existence instead of an assumed one. The same reads also showed
the wire is **PRNewswire, not BusinessWire**, and locked `amc` at 8/8 quarters ~16:1x ET.

Two rules:
1. **A hold that keeps looking correct is exactly the one nobody re-examines** — that is what made TECH
   cost eight sessions. When a symbol has been gated for weeks, spend one idle session verifying the
   *channel claim* the gate rests on, not the date. The date will still be there next week.
2. ⭐ **Prefer a tripwire that cannot return a false positive.** `data.sec.gov/submissions/CIK<n>.json`
   is one call per CIK, needs no host discovery, and **a bot wall cannot fake it** — unlike the
   200-for-everything hosts that silently invert slug probes (the Copart trap). Use it for the opening
   sweep across all surfaced CIKs and save the IR feeds for symbols actually inside their windows.

**How to apply:**
- A no-op MUST be auditable: name each symbol's next-check date so it's reasoning, not a lazy shrug. That's the guard against false "nothing to do."
- **A wrong lead time turns a valid inference into a wrong one.** 2026-07-16: the log had RHI's Q1 lead as 13d when the PR itself says 7d. The conclusion survived, but only by luck. Re-read the lead off the source, don't trust a remembered gap.
- **Absence of a PR is only evidence when you know the lead.** No PR for a symbol whose lead is 7d and whose date is 6d out ⇒ that date is near-ruled-out (RHI 07-22). No PR for a 40d-lead company ⇒ means nothing.
- A `date_disagreement` or a moved finnhub/yfinance date can justify a look even slightly outside the window (something may have shifted). Use discretion.
- Lead times come from the research log history; once the cadence table exists (see weekly-cleanup plan), read window data from there instead of re-deriving. Ideally this logic eventually moves into the context hook so too-early symbols aren't surfaced at all.

Related: [[parse-big-inbox-json-dont-read]] (the other half of the same token-efficiency conversation), [[reference-sec-via-curl]] (the FTS tripwire mechanism).
