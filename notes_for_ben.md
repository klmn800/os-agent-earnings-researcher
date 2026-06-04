# Notes for Ben

Issues, questions, and findings from the Earnings Date Researcher agent.
Open items first; long-resolved notes condensed into **Resolved** at the bottom.

---

## Open

### ⚠ Injected dispute-list under-reported the DB (3 disputes silently dropped) — 2026-05-29
The `<dispute-list>` the hook injected this morning named **5** symbols (ORCL, GME, CNM, ADBE, LEN), but `earnings_date_disputes` for `trade_date=2026-05-29` actually had **7 rows**: CNM, GME, **JBL, KMX, KR**, LEN, ORCL. The session prompt header also said "7 symbols."
- **JBL, KMX, KR were never in the injected list** — yet they were real, unresolved `date_disagreement`/`unknown_time` rows. If I'd trusted only the injection, all three would have gone unresearched. I caught it because I read the dispute table directly to update resolutions, and confirmed KMX (06-17, **time correction amc→bmo**) and KR (06-18 bmo); JBL has no advance PR yet so it's carried over.
- Conversely, **ADBE was injected but is *not* in the dispute table** (it came in as "unconfirmed-but-undisputed"). So the injected set isn't simply a subset of the dispute table either — the two lists are assembled from different sources and have diverged.
- **Suggest** checking `hooks/inject_context.py` (or whatever builds the daily `<dispute-list>`) against the `earnings_date_disputes` query — looks like the injection is filtering/capping rows (maybe a LIMIT, a join that drops symbols, or a separate query than the resolver uses). For now I'm defensively cross-checking the dispute table every session, but the injection is the thing the hook surfaces and it shouldn't silently omit open disputes.

### UEC — DB date is wrong and self-triggering (recurring, 8+ sessions)
`earnings_upcoming` has UEC at **2026-05-28** (was "tomorrow," now repeatedly "today"), `time=Unknown`. It is certainly wrong and will keep firing false earnings-window signals until cleared:
- UEC files its **Q3 10-Q with no advance PR** (~6 weeks after the Apr-30 quarter-end → realistic window early-to-mid June; FY25 Q3 10-Q was 2025-06-02). EDGAR full-text search = 0 earnings 8-Ks; the IR events page lists nothing past Q2 (Mar 10).
- Neither yfinance nor finnhub can pick it up (no advance PR to scrape). finnhub's 06-16 is more plausible but still unconfirmed.
- I can't authoritatively replace the date, so I've left it unresolved. **Suggest** clearing/pushing it forward manually, or letting the daily resolver catch the actual 10-Q when it drops (~next-check 2026-06-04). Cadence now captured in `memory/reference_company_cadence.md`.

### Weekend/Sunday maintenance session — looks implemented; OK to close the proposal?
`analysis/weekend_cleanup_proposal.md` is still marked "awaiting decisions," but everything it proposed now exists and I'm running it today: `PROMPT_SUNDAY.md`, `STATUS.md`, `memory/archive/`, and the `<maintenance-session>` hook injection. Archive granularity landed as **quarterly-by-earnings-season** (not the monthly I'd leaned toward) — that's working well; this run produced `research_log_2026-Q2_spring-earnings.md`. If you agree it's done, I'll mark the proposal **implemented** next session.

### Proposal: move window-gating into `hooks/inject_context.py` (dev session)
Now that `memory/reference_company_cadence.md` exists, the hook could stop surfacing symbols before their advance-PR window opens (`window_opens = earnings_date − lead_time − buffer`) — killing the late-week 0-confirm churn at the source instead of me skipping by hand each morning. Written up in **`analysis/window_gating_in_inject_context_hook.md`** with the mechanic + 3 decisions for you (where lead-time data lives, suppress vs. footer, default lead time). Not urgent; for whenever you next do a dev session on the hook.

### Minor: this maintenance session ran on a **Thursday**, not Sunday
The SessionStart hook + `<maintenance-session>` block both date today as **Thursday 2026-05-28**, while `PROMPT_SUNDAY.md` is written as a Sunday session. Not a problem — I followed the maintenance prompt — but flagging in case the scheduled task fired off-day or the date wiring is off. (2026-05-28 is genuinely a Thursday.)

---

## Resolved

- **2026-05-28 — Stray `inbox/` research artifacts cleared.** Moved all 10 pre-staged SEC files (orcl/uec/cnm/gme `*_filings.json` / `*_search.json` / `*.html`) from `inbox/` root into `inbox/processed/`. Inbox root is clean; the hook no longer flags them.
- **2026-05-27 — SEC.gov reachable via curl (now in memory).** `WebFetch` 403s on sec.gov, but `Bash` + `curl` with a UA (`klmn800alerts@gmail.com`) gets 8-Ks, the submissions JSON, and EDGAR full-text search. Promoted to `memory/reference_sec_via_curl.md`; SEC 8-K bodies are now a first-class confirmation source. No action needed.
