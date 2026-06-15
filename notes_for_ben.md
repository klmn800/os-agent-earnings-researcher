# Notes for Ben

Issues, questions, and findings from the Earnings Date Researcher agent.
Open items first; long-resolved notes condensed into **Resolved** at the bottom.

---

## Open

### Minor: stray mailbox duplicates in `memory/` (safe to delete)
`memory/` contains three misplaced copies of outbox mailboxes — `for_market_analyst.md`, `for_system_analyst.md`, `for_trading_advisor.md`. These belong in `outbox/` (where the canonical, peer-readable copies live). Two are byte-identical to the `outbox/` versions; `for_system_analyst.md` is a **truncated 13-line subset** of the canonical 65-line outbox copy. They're not in `MEMORY.md` and carry no unique content. Looks like a 06-04-restore artifact. I tried to delete them this session but the operation was denied by the permission layer — flagging so you can remove them (or let me, if you re-allow): `rm memory/for_{market_analyst,system_analyst,trading_advisor}.md`.

### Proposal: move window-gating into `hooks/inject_context.py` (dev session)
Now that `memory/reference_company_cadence.md` exists (and is well-populated — 51 rows / ~55 tickers after the 06-14 maintenance), the hook could stop surfacing symbols before their advance-PR window opens (`window_opens = earnings_date − lead_time − buffer`) — killing the late-week 0-confirm churn at the source instead of me skipping by hand each morning. Written up in **`analysis/window_gating_in_inject_context_hook.md`** with the mechanic + 3 decisions for you (where lead-time data lives, suppress vs. footer, default lead time). Not urgent; for whenever you next do a dev session on the hook.

---

## Resolved

- **2026-06-14 — Injected dispute-list under-reported the DB → FIXED, note retired.** Saga ran 05-29 → 06-11: the `<dispute-list>` the hook injected diverged from `earnings_date_disputes` in *both* directions (real disputes JBL/KMX/KR on 05-29 and GIS/NKE on 06-11 were never injected; "unconfirmed calendar rows" that have no dispute row *were* injected). Root cause, fixed in your **06-11 dev session**: a `db_date <= today+14d` horizon gate on the disputes query hid disputes whose *stored* date was >14d out (the stored date is the value under dispute). Gate removed from the disputes query, kept on the unconfirmed-backfill query; injected list now split into "DISPUTES" vs "UNCONFIRMED CALENDAR ROWS" sub-headers. No recurrence on 06-12. I've dropped the defensive every-session cross-check (keeping a glance at the table as cheap insurance).

- **2026-06-14 — UEC chronic-wrong date: closed.** The impossible `2026-05-28` date that fired false earnings-window signals for 8+ sessions self-corrected to `2026-06-09 bmo` (feeds `conflict=0`) by 06-05, and **UEC reported 06-09 as predicted**. No manual DB intervention was ever needed; the resolver caught up on its own. Cadence entry in `reference_company_cadence.md` documents the no-advance-PR-for-Q3 pattern.

- **2026-06-14 — `earnings_date_disputes`-absent-on-Sunday: closed, did not recur.** On Sunday 06-07 the table didn't exist in `performance.db`; on weekdays 06-11/06-12 it was present and my UPDATEs persisted; **this Sunday 06-14 it is present again** (with the 06-11/06-12 rows). So the 06-07 absence was a one-off, not a Sunday-suppression behavior. Nothing actionable.

- **2026-06-14 — Weekend/Sunday maintenance proposal: marked IMPLEMENTED.** Everything `analysis/weekend_cleanup_proposal.md` proposed now exists and runs: `PROMPT_SUNDAY.md`, `STATUS.md`, `memory/archive/`, and the `<maintenance-session>` hook injection. Archive granularity landed as quarterly-by-earnings-season (not monthly) and is working well. Marked the proposal file's header IMPLEMENTED; flag me if you'd rather revisit any of it.

- **2026-06-14 — Workspace restore (~06-04) log/archive loss: closed (awareness only).** The git restore (`43c4af6` / `9cb08f1`) truncated `memory/archive/research_log_2026-Q2_spring-earnings.md` (849 lines → 524 bytes, lost most spring detail) and the active log (lost the 06-01→06-05 session entries). **Databases were untouched** (`data/*.db` aren't git-tracked). The operational ledgers (header tables, cadence) survived, so weekday work was never impaired. Truncation markers are now in the archive so the gap is explained, not mysterious. *If the transcript-restore tooling can preserve full file contents next time, that'd avoid the truncation — but no action needed otherwise.*

- **2026-06-07 — Maintenance day wiring confirmed correct.** The prior note flagged the 05-28 maintenance session firing on a Thursday. The 06-07 and 06-14 sessions both fired correctly on **Sunday**. The off-day 05-28 run was a one-off; weekly cadence is on Sunday.

- **2026-05-28 — Stray `inbox/` research artifacts cleared.** Moved all pre-staged SEC files (orcl/uec/cnm/gme `*_filings.json` / `*_search.json` / `*.html` + the 0-byte `jef_8k.htm`) from `inbox/` root into `inbox/processed/`. Inbox root is clean.

- **2026-05-27 — SEC.gov reachable via curl (now in memory).** `WebFetch` 403s on sec.gov, but `Bash` + `curl` with a UA (`klmn800alerts@gmail.com`) gets 8-Ks, the submissions JSON, and EDGAR full-text search. Promoted to `memory/reference_sec_via_curl.md`; SEC 8-K bodies are now a first-class confirmation source.
