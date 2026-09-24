# Notes for Ben

Issues, questions, and findings from the Earnings Date Researcher agent.
**Open** items first, most urgent at the top — each condensed to what is still live, with a pointer
to its full history. Everything else moved **verbatim** to
[`notes_for_ben_archive.md`](notes_for_ben_archive.md) at the 2026-09-13 maintenance (headings are
unchanged there, so the pointers below are searchable); items closed since are appended there each Sunday.

---

## Open

### ⚠ SNA 10-15 is probably a week early — a 53-week fiscal year shifted every Snap-on date in 2026, and the July lock was wrong the same way — 09-24

Snap-on's fiscal 2025 ended **January 3, 2026** (53 weeks), so each 2026 quarter ends a week later than
2025's. Its Q2-26 8-K exhibit is headed "Three Months Ended July 4, 2026 / June 28, 2025", and the report
dates moved with it: Q1 04-23 (vs 04-17 '25), Q2 **07-23** (vs 07-17). The 06-30 cadence lock put Q2 at
**07-16** — wrong by 7d, and the outcome was never logged (it is not in the 07-17 bad-batch list either).
The Q3 row (10-15, finnhub agrees) carries the same 2025-shaped "3rd Thursday" assumption; the arithmetic
says **Thu 10-22** (Q3 ends 10-03, +19d as every quarter). I wrote only the time (`bmo`, sourced) and
left the date unlocked; the advance webcast PR (14d lead) will settle it 10-01 or 10-08.

Two things for you: (1) if the scanner has SNA in a 10-15 setup, treat the date as unconfirmed;
(2) the general failure — a company with a 52/53-week fiscal year moves every date after a 53-week year,
and any "nth weekday" cadence row breaks silently — is worth a one-line check in whatever seeds the
calendar (fiscal-year-end date from the latest 10-K cover). REXR's 2026 4th-Thursday shift looks like a
different cause (calendar-year REIT).

### 🚨 No research session ran 09-16, 09-17 or 09-18 — a zero-dispute morning cancels the session, and UEC reports Thursday — 09-20

The orchestrator only launches me when the lite refresh flags **≥1 dispute**
(`ei_lite_refresh.py:339`, `if disputes and spawn_agent`), and `launcher.py` has the same early-exit.
Wed–Fri it flagged **0** (with 5–7 unconfirmed rows in scope each day), so nothing ran. My logged
next-check dates and the unconfirmed backfill had only ever run because some *other* symbol's dispute
fired the launcher that day.

What slipped:
- **UEC — reports 2026-09-24, still unconfirmed, stored `amc` that I believe should be `bmo`.** Its
  check was due 09-17 (the day its advance PR was expected). Never ran.
- **CCL** — check due 09-16, never ran; the feed moved it 09-28 → 09-29 meanwhile, unsourced.
- **MU (09-30)** and **ACN (10-01, stored `amc` vs bmo every observed quarter)** entered the 14-day
  horizon and were never surfaced.

**What I need from you:** if Monday's refresh flags 0 disputes again, no session will run and UEC goes
into its event unchecked. A manual session would cover it — from the code (untested): run
`python launcher.py` once (it resets `.session_mode` to `daily` before it exits on "no disputes"; without
that, tonight's `weekend` marker would suppress the list), then open `claude` in this folder — the hook
injects the unconfirmed backfill on its own. No wrong write came out of the gap; the cost is lead time.

Fix proposal (small): `analysis/proposal_20260920_spawn_on_due_next_checks.md` — spawn on "disputes
**or** unconfirmed rows inside the hook's 14-day horizon", mirror it in the launcher, and have the hook
say so when the last logged session is more than a trading day old.

### ⚠ Ten upcoming rows carry a time that contradicts one already established — the re-seeding problem, at scale — 09-13

Reviewing the cadence table against the calendar today turned up ten rows whose stored time disagrees
with a time I company-sourced in an earlier quarter:

| Symbol | Stored now | Established | Row date |
|--------|-----------|-------------|----------|
| ACN | `amc` | bmo — every observed quarter | 10-01 |
| STZ | `bmo` | amc — Q1 FY27 PR (1 obs) | 10-06 |
| C, FHN, SNA, ERIC, ACI | ~~`Unknown`~~ → all bmo ✅ (09-22 → 09-24) | bmo | 10-13 → 10-15 |
| FNB, REXR | ~~`Unknown`~~ → both amc ✅ (09-23, 09-24) | amc | 10-14 / 10-15 |
| MDT | `Unknown` | bmo — 6:45 ET release, every quarter | 11-17 |

The `Unknown` ones will reach me as `unknown_time` disputes and I'll fix them as they come. **ACN and
STZ are the dangerous ones** (both still unchanged in the DB on 09-20; ACN's advance window opened ~09-15 and hasn't been read — see the top item): they look filled in, so nothing will ever flag them, and a wrong bmo/amc
puts the whole trade on the wrong session. Nothing written today (Sunday; no same-quarter source yet).

Fixes for the class, cheapest first (unchanged since 08-18 / 09-03):
1. **Carry a confirmed time forward** to the next quarter's row instead of re-seeding it from the feed.
2. ~~A `--time`-only mode on `earnings_confirm.py`~~ — ✅ **done: `--time-only` is live (your 09-16
   install).** It lets me *write* a sourced time without touching the date; it does not stop the next
   quarter's row from being re-seeded, so fix 1 is still the one that closes the class.
3. Optional sweep: SEC Item 2.02 furnish times as the default when the feed says Unknown
   (method in `memory/reference_sec_acceptance_time_timing.md`).

Same family, never explained: TECH's time correction "wrote" three times in July and didn't persist (08-04).
_History in the archive: "MDT's wrong time came back…", "CLOSED 09-03 — CTAS's time…", "A time correction I 'wrote' three times…", "`earnings_confirm.py` conflates…"._

### 🐞 Tool fixes, still open — `direct_db_query.py`, and backslash paths in the daily template

- ✅ **`earnings_confirm.py` — fixed** (patch installed 09-16; verified 09-20 from `--help`: `--date`
  and `--by` required, `--time-only` present). ✅ **`launcher.py` template `--write` — fixed** (verified
  09-20, steps 6–7). Thank you — both were the two highest-consequence items on this list.
- **`direct_db_query.py`:** exits 0 and prints "No results returned" on invalid SQL and on 0-row
  updates (suggest: print `rowcount`, exit non-zero on `sqlite3.Error`); splits `--sql` on `;` even
  inside string literals (hit again 09-14); a backslash `--db` path under bash silently creates an
  **empty** database and then reports `no such table`. Small new one: a read-only `PRAGMA table_info`
  trips the write-guard warning and prints nothing (seen once, 09-20). My workarounds hold (forward
  slashes, no `;` in text, SELECT after every write).
- **`launcher.py` daily template still uses backslash `--db` paths** in steps 6–7
  (`E:\options_scanner\data\...`) — the stray-empty-DB hazard above if pasted into bash as-is.
  I always rewrite them to forward slashes; changing the template would remove the trap.

_History in the archive: "`earnings_confirm.py --symbol SYM`…", "`direct_db_query.py` splits…", "Tooling hazard…", "BUG in the daily session prompt…", "The `--write` bug…"._

### ⚠ Phantom earnings events still have nowhere to go — and the fall season re-arms them — 09-13

AES (take-private; no Item 2.02 since 2025-11), EA (take-private cleared 07-30; Q1 went out in a bare
10-Q), MKTX (ICE acquisition; Q2 released 8 days early alongside the deal) and TECH (Merck KGaA) all
reached me this summer as **unconfirmed calendar rows with no dispute row to write to**. All four now
have fresh fall rows — **AES 11-04, EA 11-03, MKTX 11-05, TECH 11-09** — plus KVUE 11-05 and WBD 11-05
(both corporate-action names). They'll surface again in late October. TECH's summer "phantom" turned out
to be real (08-12), so this is a *screen*, not a verdict — I'll run the pre-flight in
`memory/reference_ma_phantom_earnings.md` on each before researching.

The ask is unchanged: a `symbol_metadata` flag (`no_earnings_event` / `inactive`) that the dispute
generator and the calendar respect. A periodic ticker-vs-SEC `company_tickers.json` reconciliation
would also have caught IAC→PPLI automatically.
_History in the archive: "AES is a phantom again…", "EA is a phantom…", "MKTX was dated TODAY…", "Data-quality: symbols the dispute system can't self-assess…"._

### ❓ Policy calls I can't make by research — standing since July/August

1. **EXPD — `dmh`?** Expeditors furnishes midday every quarter and its release states no time;
   `earnings_confirm.py` accepts `dmh`. Set it? (Its fall row, 11-03, currently reads `bmo`.)
2. **Foreign issuers whose release lands after the US close (ASX/HK/Chile):** "D−1 amc" or "D bmo"?
   Both encode the same overnight gap. I've been writing the company's published date (WDS `bmo`;
   SQM `amc` on its 22:00 ET release date). Pick one and I'll apply it consistently. UEC's fiscal
   year-end has the same shape domestically (10-K the prior evening, webcast next morning).
3. **Sites that block every client (ITUB — `itau.com.br` 403s everything):** may an SEC 6-K filename
   cluster stand in for the date, or do I keep holding?

_History in the archive: "EXPD: candidate for `dmh`", "WDS (Woodside)…", "Two symbols need a policy call…", "ITUB…"._

### 💡 Proposals for a dev session (no urgency; each has a fuller write-up in the archive or `analysis/`)

- **Spawn on due next-checks / unconfirmed horizon rows, not only on disputes** —
  `analysis/proposal_20260920_spawn_on_due_next_checks.md` (this one *is* somewhat urgent — top item).
- **Hook: give `confirmed_row_diverged` top priority** and show the signed delta — see
  `analysis/proposal_20260913_hook_diverged_priority_status_tripwire.md` (with two other small items;
  its item 3 predates the patch — the line to add to the prompt is now *"time-only ⇒ `--time-only`"*,
  not the plain UPDATE).
- **Hook: warn when `STATUS.md` is >10 days stale** — would have caught the 12-week maintenance gap in early July. (Same file.)
- **Hook: join live `earnings_upcoming` at injection time**, or stamp the snapshot's age — the frozen
  `db_date` misled me at least four times (07-22, 07-30, 08-06, 08-20).
- **Filter finnhub's lone +6 to +8d dissent** when DB = `+364d` (the DB won every scored case); never
  filter a ±1d or a yfinance dissent.
- **Flag overdue advance PRs** for symbols with a verified channel and a measured lead (PVH was 8d wrong
  with every feed agreeing; the only tell was a PR 7d overdue).
- **Window-gating in the hook** — `analysis/window_gating_in_inject_context_hook.md`.
- **Backfill `symbol_metadata.ir_earnings_url`** from the ⭐ feeds in the cadence table — needs your pick
  between my live-verify-on-Sunday option and a mechanical backfill (08-25 note).

### 🔧 FDX's earnings date is browser-render-only — recurs every quarter (next row: 10-28)

Unchanged since 06-21: no advance PR, no scheduling 8-K; the date lives only on a JS-rendered Q4 events
page. If its events JSON endpoint can be found I can self-serve; otherwise I'll hold and ask for a paste.

### Minor: stray `memory/for_*.md` mailbox duplicates — still present, deletion still blocked for me

`rm memory/for_{market_analyst,system_analyst,trading_advisor}.md` — the canonical copies live in `outbox/`.

---

## Resolved (condensed — full text in the archive)

- **09-16 — `earnings_confirm.py` safety patch: installed by you, verified live 09-20.** Bare
  `--symbol` now errors, `--by` is required, `--time-only` exists, agent writes to `ben` rows are
  refused. My memory note now leads with the patched behaviour. Inbox notice processed.
- **09-14 — PAYX and KMX (dates I locked 09-08 without a company source): both re-sourced.** PAYX was
  wrong — corrected **09-29 → 09-23 `bmo`** from Paychex's PR (yfinance's drift flag was right); KMX's
  09-29 `bmo` was right and is now backed by CarMax's PR. The wrong PAYX lock stood 5 days with the PR
  already on the wire.
- **09-13 — "The Sunday maintenance session has not run since 06-21 … the scheduled task and its
  launcher are both gone" (08-26): CLOSED, and its diagnosis was wrong.** The launcher is at
  `E:\options_scanner\scheduled_tasks\start_earnings_researcher_sunday.bat`, *outside* the workspace;
  the 08-26 check only looked inside `agents/earnings_researcher/`. Task Scheduler lists
  **`!Sunday Earnings Researcher`**, Ready, next run 09-20 18:00, and it launched tonight. I can't tell
  whether the task was missing on 08-26 and re-registered since. Maintenance is caught up as of today.
- **09-03** — false `ben` stamps on ORCL/CTAS cleared; that repair only ever needed your say-so.
- **09-01 → 09-03** — GME, ADBE, CPRT, ORCL, CTAS confirmed as their notes predicted; the method
  lessons (BusinessWire index lag, dates relocating into transaction PRs) are in memory.
- **08-13** — SQM: its events calendar pre-lists release and call; no decision was ever needed.
- **08-12** — TECH: my phantom call was wrong and the event was real. Lesson (verify the channel exists
  for the matching quarter before arguing from absence) is now a standing rule.
- **08-03 → 08-10** — nCino's IR host, MKTX/ATI/ITUB/YPF (past-dated), NNE, INSP, FLO, BR, the frozen
  Allstate feed, the reporting-framing note, the browser-UA unlock, the 16-for-16 unconfirmed check.
- **07-27 → 07-31** — IAC → PPLI rename done; SPA problem solved via IR RSS; `+364d` demoted to
  corroborator; RSS-outage caveat; STE host correction; `skipped` resolution already existed.
- **06-30 convergence locks (10 names) — outcome:** at least 4 (RTX, LMT, CLF, EQT) were wrong by
  4–7d, caught 07-17 by the drift flag and corrected from company PRs. Policy since: no lock without a
  company source. (The 09-08 KMX/PAYX locks above broke that policy by a different route.)
- **June items** (dispute-list horizon bug, UEC chronic date, 06-07 table absence, weekend proposal
  implemented, 06-04 restore truncation, SEC via curl) — archive → Resolved.
