# Notes for Ben

Issues, questions, and findings from the Earnings Date Researcher agent.
**Open** items first, most urgent at the top — each condensed to what is still live, with a pointer
to its full history. Everything else moved **verbatim** to
[`notes_for_ben_archive.md`](notes_for_ben_archive.md) at the 2026-09-13 maintenance (headings are
unchanged there, so the pointers below are searchable).

---

## Open

### 🔧 `earnings_confirm.py` safety patch — staged, needs you to apply (the write guard blocks me) — 09-14

You OK'd me editing the tool, but `.claude/hooks/earnings_researcher_write_guard.py` blocks every write
outside my workspace (correctly, it's your guard, so I didn't route around it). The patch is staged at
`analysis/earnings_confirm_patch/` with a diff (`earnings_confirm.diff`) and a 34-check scratch-DB test
suite (all pass, production hash unchanged). What it changes:
- `--date` required to confirm. A bare `--symbol` is an error now, not a silent confirm.
- `--by` required, `ben`/`agent` only (was: defaults to `ben`).
- New `--time-only` mode: writes `earnings_time`, never touches `date_confirmed*` (the PAYX/KMX fix).
- Refuses any non-`ben` write to a `ben`-confirmed row. Today it only warns.

No code imports it. The launcher template and CLAUDE.md already pass `--date --time --by agent`. Your
04-23 bulk CSV would need `--by ben` on a re-run. To apply:
```
copy E:\options_scanner\agents\earnings_researcher\analysis\earnings_confirm_patch\earnings_confirm.py E:\options_scanner\tools\earnings_confirm.py
```

### ✅ RESOLVED 09-14 — PAYX and KMX: two dates I locked without a company source — and one is now flagged as probably wrong — 09-13

> **Resolved 2026-09-14, no action needed from you.** Both advance PRs had been out since 09-09.
> **PAYX was wrong: now 2026-09-23 `bmo`** (Paychex GlobeNewswire, *"Wednesday, September 23, 2026,
> before the financial markets open"*). yfinance's flag was right. **KMX's 09-29 `bmo` was right** and is
> now backed by CarMax's BusinessWire PR. Both re-confirmed `--by agent` with sources, and the PAYX
> `confirmed_row_diverged` row is resolved. The reset SQL below is moot. Archive at the next maintenance.

On **09-08** I fixed the *times* on KMX and PAYX (both `unknown_time`; `bmo` is solid on history for
both) but ran them through `earnings_confirm.py`, which sets `date_confirmed=1` on every call. So both
**2026-09-29** dates are now locked as agent-confirmed with **no same-quarter company source behind
them**. My own memory already said to use a plain `earnings_time` UPDATE for a time-only fix; I didn't.

On **09-11** the drift detector raised **`confirmed_row_diverged` on PAYX — yfinance now says 09-23**,
six days earlier. That is exactly the shape that exposed the bad 06-30 batch in July (RTX/LMT/CLF/EQT:
all four locked dates were late, yfinance was right every time). The 09-11 session log doesn't mention
it. It's the first thing Monday reads.

- **Monday:** read Paychex's Q1 FY27 advance PR if it's out (historically mid-September) and correct or
  re-confirm from it; same for CarMax's Q2 advance.
- **Your call:** return both rows to unconfirmed until then, so they aren't suppressed behind a lock
  with nothing under it. Say the word and I'll run it (times stay `bmo`):
  ```
  UPDATE earnings_upcoming SET date_confirmed=0, date_confirmed_by=NULL, date_confirmed_at=NULL WHERE symbol IN ('KMX','PAYX')
  ```
  Waiting for the PRs instead is also fine — Monday's read likely settles PAYX either way.

### ⚠ Ten upcoming rows carry a time that contradicts one already established — the re-seeding problem, at scale — 09-13

Reviewing the cadence table against the calendar today turned up ten rows whose stored time disagrees
with a time I company-sourced in an earlier quarter:

| Symbol | Stored now | Established | Row date |
|--------|-----------|-------------|----------|
| ACN | `amc` | bmo — every observed quarter | 10-01 |
| STZ | `bmo` | amc — Q1 FY27 PR (1 obs) | 10-06 |
| C, FHN, SNA, ERIC, ACI | `Unknown` | bmo | 10-13 → 10-15 |
| FNB, REXR | `Unknown` | amc | 10-14 / 10-15 |
| MDT | `Unknown` | bmo — 6:45 ET release, every quarter | 11-17 |

The `Unknown` ones will reach me as `unknown_time` disputes and I'll fix them as they come. **ACN and
STZ are the dangerous ones**: they look filled in, so nothing will ever flag them, and a wrong bmo/amc
puts the whole trade on the wrong session. Nothing written today (Sunday; no same-quarter source yet).

Fixes for the class, cheapest first (unchanged since 08-18 / 09-03):
1. **Carry a confirmed time forward** to the next quarter's row instead of re-seeding it from the feed.
2. A **`--time`-only mode** on `earnings_confirm.py` (or a `time_confirmed` column) so a time can be
   locked without asserting the date — its absence is what produced the PAYX/KMX locks above.
3. Optional sweep: SEC Item 2.02 furnish times as the default when the feed says Unknown
   (method in `memory/reference_sec_acceptance_time_timing.md`).

Same family, never explained: TECH's time correction "wrote" three times in July and didn't persist (08-04).
_History in the archive: "MDT's wrong time came back…", "CLOSED 09-03 — CTAS's time…", "A time correction I 'wrote' three times…", "`earnings_confirm.py` conflates…"._

### 🐞 Tool fixes, still open — `earnings_confirm.py`, `direct_db_query.py`, the daily prompt template

- **`earnings_confirm.py`:** bare `--symbol` is a *write* stamped `by=ben` (hit 08-19 and 09-02);
  `--by` defaults to `ben`; `date_confirmed=1` is set on every call. Suggested: require `--by`, make
  bare `--symbol` a read, add `--time-only`.
- **`direct_db_query.py`:** exits 0 and prints "No results returned" on invalid SQL and on 0-row
  updates (suggest: print `rowcount`, exit non-zero on `sqlite3.Error`); splits `--sql` on `;` even
  inside string literals; a backslash `--db` path under bash silently creates an **empty** database and
  then reports `no such table`. My workarounds hold (forward slashes, no `;` in text, SELECT after every write).
- **`launcher.py` daily template — re-verified 09-13 (lines 333/337): steps 6 and 7 still omit
  `--write`** and use backslash `--db` paths. A session following the prompt literally writes nothing
  and appears to succeed. `CLAUDE.md` has `--write`; the template doesn't.

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

- **Hook: give `confirmed_row_diverged` top priority** and show the signed delta — see
  `analysis/proposal_20260913_hook_diverged_priority_status_tripwire.md` (with two other small items).
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
