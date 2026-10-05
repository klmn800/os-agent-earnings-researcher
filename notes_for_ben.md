# Notes for Ben

Issues, questions, and findings from the Earnings Date Researcher agent.
**Open** items first, most urgent at the top — each condensed to what is still live, with a pointer
to its full history. Everything else moved **verbatim** to
[`notes_for_ben_archive.md`](notes_for_ben_archive.md) at the 2026-09-13 maintenance (headings are
unchanged there, so the pointers below are searchable); items closed since are appended there each Sunday.

---

## Open

### ✅ IMPLEMENTED 10-05 (A + D) — 83 upcoming rows (≤ 10-23) couldn't reach a daily session: disputes crowded the backfill out — 10-04

**10-05:** you had me implement options A and D. The queue is now one date-sorted list (ceiling 40, overflow listed), and the daily prompt reads the log header and does the bookkeeping. First live run: tomorrow 07:15. I'll score it at the 10-11 maintenance. Option C (inject next-checks) is still open. The text below is kept until then.

**This is the one to fix before the 10-19 wave.** The hook backfills unconfirmed rows only into
`25 − disputes` slots. Disputes have run 28 / 42 / 34 a morning since 09-30, so the backfill has been
**empty**, and any row where the three feeds agree (so no dispute row) never reaches a session. As of tonight:
**107 unconfirmed rows report 10-05 → 10-23 and 83 of them are invisible.** They include all of BAC, MS,
TSM, PNC, SCHW, USB, BK, STT, ASML (10-14/15), and TSLA, IBM, INTC, TXN, T, PG, GE, GM, ISRG, … (10-20 → 10-23).
Two carry-over checks were silently skipped too: **ACI (09-30) and SNA (10-02), both rows whose stored date
I think is wrong.**

Agreement among the feeds isn't safety. This quarter all three were wrong together on REXR, LMT and DOC
(3 of 21 scored disputes), and SNA is probably a fourth.

There's a second, smaller cause: the daily prompt template never points the session at the log header
or the carry-overs, and it sorts `unconfirmed` last. So my "front-load these" note in the header was
never going to be read. The Sonnet sessions did exactly what the template says.

**Ask:** pick from `analysis/proposal_20261004_backfill_crowded_out.md`. **A** (one list, sorted by
earnings date) is my preference, **B** (always backfill ≥10) is the smallest change, and **D** (two
lines in `PROMPT_TEMPLATE`: read the header first; write cadence rows for first-time names) costs
almost nothing and makes the stopgap reliable. **Stopgap in place:** the research-log header now opens
with a READ FIRST block listing all 83 by date, but without D a session only finds it by habit.

My 09-27 note told you the ceiling only made rows "slip a day". That was wrong: I hadn't read how the
ceiling applies. Corrected.

### ⚠ SNA 10-15 is probably a week early (→ 10-22); its check was missed — 09-24, updated 10-04

If the scanner keys anything to SNA's stored 10-15, treat it as unconfirmed. Snap-on's 53-week fiscal 2025
shifted every 2026 quarter-end by +7d, and Q3 ends 10-03, so the release should be **Thu 10-22**. The
webcast PR (14d lead) decides it: one dated ~10-01 means 10-15 is real, none means 10-22 (PR due 10-08).
The 10-02 read never happened (crowd-out above), so it's first on Monday's list. **ACI** is the same
shape (stored 10-13; fiscal arithmetic says 10-20; advance overdue if 10-13 were real). Also first Monday.

**REXR resolved as predicted:** PR 09-28 → **10-22 `amc`**, confirmed 09-29. All three feeds had it
wrong (10-14 / 10-14 / 10-21). Full history in the archive.

The general point for the calendar seeder still stands: after a 53-week fiscal year, every "nth weekday"
date shifts by a week. Checking the fiscal-year-end date on the latest 10-K cover would catch it.

### 👀 Sonnet daily sessions, week 1 (09-28 → 10-02, n=5): good research, no upkeep, and the prompt doesn't ask for upkeep — 10-04

**Research quality is good.** 36 dates confirmed on company sources from ~65 symbols, 8–10 a morning,
**0 wrong writes found**, one stored date corrected (FNB +4d) and one time (CLF). The two failure points
from 09-25 are gone: AMX's feed was read correctly every day, and rate-limited reads were logged as
*unread* rather than as absences. Two sourcing slips, both minor: a constructed BusinessWire URL went
into DOC's `research_url` (fixed within the minute), and BX was confirmed from a search snippet of a
company page that 403s (flagged as weak in the ledger).

**Bookkeeping didn't happen:** no cadence rows after 09-28 (I backfilled 30 tonight), carry-over
table never updated, ledger lines skipped for 09-29/09-30. But the daily template never asks for any of
that. The Opus sessions did it unprompted, the Sonnet ones do what's written. **So I'd fix the prompt
(proposal D above), not the model.** Lead times are what window-gating runs on, and they only accumulate
if somebody writes them down.

### ⚠ Re-seeded times contradict established ones: 9 of the 10 rows are fixed, but the class isn't — 09-13, updated 09-27

On 09-13 I found ten upcoming rows whose stored time disagreed with a time I had company-sourced in an
earlier quarter. **Nine are now fixed from same-quarter sources** (09-22 → 09-24): ACN amc → **bmo**,
STZ bmo → **amc**, and C, FHN, SNA, ERIC, ACI, FNB, REXR `Unknown` → sourced. All nine went the way the
cadence table predicted. Left: **MDT** (11-17, `Unknown`; bmo, 6:45 ET release every quarter). It will
reach me as an `unknown_time` dispute.

What remains is the mechanism. Every quarter the feed re-seeds the next row, so the same names come back
wrong or `Unknown`. ACN and STZ were the dangerous shape: a filled-in wrong time that nothing flags.

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
   **⚠ Live now:** HDB and IBN (Indian bank ADRs) are dated **Saturday 10-17** in the DB (HDB `bmo`,
   IBN `amc`), 13 days out. A Saturday release reaches the US market Monday 10-19 at the open, so either
   encoding needs a date change. I'll read their dates this week and hold the write until you pick a
   rule. (Today they're invisible to sessions anyway: see the crowd-out item.)
3. **Sites that block every client (ITUB — `itau.com.br` 403s everything):** may an SEC 6-K filename
   cluster stand in for the date, or do I keep holding?

_History in the archive: "EXPD: candidate for `dmh`", "WDS (Woodside)…", "Two symbols need a policy call…", "ITUB…"._

### 💡 Proposals for a dev session (no urgency; each has a fuller write-up in the archive or `analysis/`)

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

- **10-04: REXR's stored 10-14 was wrong, as flagged.** The company PR (09-28) says **10-22 `amc`**,
  confirmed 09-29. The other half of that item (SNA) stays open.
- **09-24 — Sessions no longer need a dispute to spawn (your A + C from the 09-20 proposal).** Verified in
  code 09-27: both gates spawn on disputes OR unconfirmed rows due ≤14d, and the hook warns on a missed
  weekday. **Not yet exercised:** every morning since 09-22 had disputes, so the old gate would have fired too.
  The first zero-dispute morning will be the real test. One residual gap is
  logged in my memory (a next-check on a row >14d out with no dispute still spawns nothing; Monday 09-28
  is such a day, but REXR/AMX/WIT have flagged daily, so it will probably run).
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
