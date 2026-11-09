# Handoff: rebuild the earnings pipeline around a per-company source registry

*Written 2026-11-09 by the Earnings Researcher agent for a new dev session with Ben. Discuss before building: Ben wants to
talk it through first. Every number below has a file behind it. Read the file before relying on the number.*

## The goal (Ben's words, paraphrased)

Build up a database of where each company reliably reports its earnings date, so that when active mode comes back the
earnings researcher gets more dates right, earlier and faster, with less searching. Some dependencies probably need
adjusting, or the earnings pieces need to move into a redesigned module that works under Simple Mode.

## 1. Why weekday research stopped (the dependency problem)

- Simple Mode (default since 2026-10-28, `docs/simple_mode/README.md`) skips **step 1.2 Earnings Intelligence** and the
  **Friday step 5.3 Earnings Refresh**. Task Scheduler: `\!main.py` Disabled, `\!main.py (Simple Mode)` Ready.
- **1.2** is `run_earnings_intelligence()` (`main_runners.py:1065`), which runs the EI daily pipeline. The researcher
  agent is spawned from inside it: `strategies/earnings_intel/ei_lite_refresh.py:378` → `_spawn_earnings_researcher()`
  (`:395`, gated by `tools/agent_toggle.py`). So the agent has no launch path of its own.
- **5.3** is `run_earnings_weekly_refresh()` (`main_runners.py:2043`) → `EarningsCollector().collect_weekly_earnings()`:
  archive past events, clean up, fetch the next 90 days from Finnhub per symbol (~780 stocks). It's the only thing that
  writes new dates into `earnings_upcoming` (datalake.db).
- Result: `earnings_upcoming` was last written 2026-10-19 07:22. Simple Mode gating lives in `main.py`, `main_runners.py`,
  `tools/simple_mode.py`.
- **Ordering constraint:** the refresh must run before research. Researching on a frozen table wastes the agent.

## 2. What the research found

### Feed dates are the weak link; company-issued text is reliable

| Check | Result | File |
|---|---|---|
| Source audit #1 (September confirms) | 49/50 right | `analysis/source_audit_20261011.md` |
| Audit #2 (summer weak types) | feed/cadence "locks" **6/12 dates right**; call-time-only time inferences 9/12 | `analysis/source_audit_20261018.md` |
| Audit #3 (October) | 44/44 | `analysis/source_audit_20261025.md` |
| Audit #4 (late October) | 41/42 (JBLU: morning call, evening-before release) | `analysis/source_audit_20261101.md` |
| Audit #5 (October remainder + 11-02 → 11-05) | 42/42 dates, 41/42 times (1 unverifiable) | `analysis/source_audit_20261108.md` |
| Unresearched feed rows vs EDGAR, 10-17 → 10-30 | about 4% of dates wrong (6/146) | 11-01 entry, `memory/research_log.md` |
| Unresearched feed rows vs EDGAR, 11-02 → 11-06 | **about 12% wrong (27/221)**, some by 6–13 days; 16 wrong sessions; 75 no time | `analysis/edgar_screen_20261108_1102-1106.tsv` |

Caveats: small n per source type, mostly large caps with fixed habits, and no aggregator sources in any October pool (policy
since July). The 12% is inflated by the frozen feed. It's a filing-date screen, coarse on timing.

**Implication:** a ranking of websites adds little. Once the text came from the company (its IR page, its PR read on a copy
site, its 8-K), accuracy was ~99%. The costs are elsewhere: (a) **finding** the advance announcement, which is where the
token-heavy sessions went, and (b) **timing traps**.

### Where announcements can actually be found (channels that worked)

| Channel | What it gives | Gotchas | File |
|---|---|---|---|
| EDGAR submissions JSON + filing index | the *after-the-fact truth* (8-K/6-K Item 2.02 date + ET Accepted time) and each company's filing habits. Can't be bot-walled | WebFetch gets 403, use curl/urllib with a UA. Never convert the JSON `acceptanceDateTime` (mixes UTC/ET); read Accepted from the index page | `memory/reference_sec_via_curl.md`, `memory/reference_sec_acceptance_time_timing.md`, `analysis/edgar_screen.py` |
| IR RSS (`/rss/pressrelease.aspx`, `/rss/news-releases.xml`) | the company's PR list as plain XML, even when the IR site is a JS app | needs a browser User-Agent, or it gets tarpitted | `memory/reference_ir_rss_feeds.md` |
| Q4 Inc. `Event.svc/GetEventList` | scheduled earnings events as JSON | oldest first, sort ignored; pageSize=100 | `memory/reference_q4_event_feed.md` |
| stocktitan `/news/<SYM>/` JSON-LD | last 10 headlines + verbatim wire text, any company | 10 req / 300 s; a 429 can arrive as a 200 with a ~2.5 KB body | `memory/reference_stocktitan_jsonld_discovery.md`, `analysis/helpers/spine.py` |
| Direct IR pages | sometimes the only source (FDX: JS-render only) | SPAs, 403s, bot walls that return 200 for every path | `memory/reference_source_probe_failure_modes.md` |

### Per-company habits that decide timing (the part a registry must hold)

From `memory/reference_company_cadence.md` (249 KB, ~427 symbol rows, prose; grep `^| SYM `, don't read it whole):
- **Advance-PR lead time** varies by company (SNA 14d ×3, EQT 20, BMRN ~7, IRDM none, so EDGAR is the only signal). One
  observation is noisy in both directions.
- **Rule 6:** a morning call alone doesn't date the release (AMTM, UUUU, JBLU released the evening before).
- **Filing habits:** next-morning 8-K filers (UGI, RRC, FNB) fake a bmo; evening-before filers (PCG, DHR, PKG at 18:07)
  carry the next day's filing date; late filers (SCHW ~16:17, Citi ~10:09) never time the release.
- **Foreign off-hours releases → first US session, `bmo`** (Ben's 10-19 policy, `memory/feedback_ben_policy_answers_20261019.md`).
- **Feed-dissent patterns:** yfinance dissenting from the DB has meant the DB was wrong (7/7); finnhub-only +6–8d dissent is
  mostly an artifact (`memory/reference_cadence_364d_corroborator.md`).

### What exists today vs what's needed

- `symbol_metadata.ir_earnings_url`: **574 of 824** populated, last verified 2026-10-19. Mostly **per-quarter article deep
  links on copy sites** (stocktitan 78, finviz 35 among top hosts), which go stale each quarter. It's a cache, not a registry
  (`memory/feedback_ir_url_caching_spa.md`).
- The durable knowledge (channels, leads, habits) lives in the cadence table's prose, which code can't read.
- Known recurring defects (`notes_for_ben.md`): the feed re-seeds next quarter's time and overwrites confirmed ones (fix: carry
  the confirmed time forward). No `no_earnings_event` flag for acquired/delisted names (ROKU closed into Fox 11-06; MKTX reported
  early twice under a pending deal; AES, EA). `direct_db_query.py` exits 0 on bad SQL. Backslash `--db` paths create an empty DB.

## 3. Recommendations (the agent's; Ben decides)

1. **Give earnings its own module, independent of Simple Mode's Phase 1.** Three stages on their own schedule:
   (a) calendar refresh (today's 5.3 logic, plus a lighter daily delta); (b) a **deterministic channel poller** that, for
   symbols inside their announcement window, reads each one's registered channel and confirms when the company text states
   a date and time; (c) **spawn the agent only for what (b) couldn't resolve**. That's where token savings come from.
2. **Build an `earnings_sources` registry table** (one row per symbol, maybe per channel). Candidate fields: `channel_type`
   (ir_rss / q4_event_feed / stocktitan / edgar_only / ir_page / manual), `channel_url`, `needs_browser_ua`,
   `advance_lead_days_median` + `n`, `release_session_habit`, `filing_habit` (same-time / next-morning / evening-before /
   late), `last_success_at`, `quarters_correct` / `quarters_checked`, `phantom_status`, `notes`. Seed it by parsing the
   cadence table (33 rows are starred as verified feeds) and the 574 cached URLs. Expect hand-review: the table is prose.
3. **Let EDGAR score the registry automatically after each season.** `analysis/edgar_screen.py` already compares stored dates
   with Item 2.02 acceptance times. Extend it to update `filing_habit`, `release_session_habit` and the hit rates with no agent
   tokens. This is how the database "learns which sources report accurately".
4. **Carry confirmed times forward and add the `no_earnings_event` flag.** Both are already proposed (`notes_for_ben.md`, 10-19).
5. **Keep the no-lock-without-a-company-source rule.** The one source class that failed badly (feed/cadence locks, 6/12) is
   the class a naive "agreeing feeds = confirmed" shortcut would reintroduce.

## 4. Questions to settle before building

- Does anything consume `earnings_upcoming` under Simple Mode? (Earnings Signals is disabled.) That sets the urgency.
- Quick restore first (switch to full mode, or run 1.2 + 5.3 standalone; `python main.py --earnings-intel` exists, but I
  haven't verified it spawns the agent or refreshes the calendar), or go straight to the redesign?
- Registry scope: all ~824 `symbol_metadata` symbols, or only the ones the scanner trades?
- Where the poller runs, and stocktitan's rate limit and terms if it becomes a primary channel.
- Standards: this is a non-trivial build, so it's the PRD → task-list → gated-build workflow in `~/.claude/standards/ai-dev-tasks/`.

## 5. Read these, in this order

1. `agents/earnings_researcher/STATUS.md` and `notes_for_ben.md` (open items + proposals)
2. `agents/earnings_researcher/README.md`, `CLAUDE.md` (what the agent does today)
3. `analysis/source_audit_20261108.md` and `analysis/source_audit_20261018.md` (best and worst source classes)
4. `memory/MEMORY.md`, then the channel files listed in section 2
5. `strategies/earnings_intel/ei_lite_refresh.py` (spawn + dispute generation), `main_runners.py:1065` and `:2043`
6. `memory/reference_company_cadence.md`, by grep only
