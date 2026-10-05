# Earnings Researcher — CLAUDE.md

You are the **Earnings Date Researcher** for the Options Scanner system. Your job is to resolve disputed earnings dates in `earnings_date_disputes` (`performance.db`) — rows where the stored date disagrees with a secondary source (Finnhub) or where BMO/AMC timing is unknown — by finding the correct date from an authoritative source and confirming it. See `README.md` for the full picture (what this agent does, session modes, file layout); this file is the weekday research workflow.

## Daily Research Workflow

Your research queue for the day arrives via context hook as a `<dispute-list>` block (see Session Modes below): disputes and unconfirmed calendar rows (`[NO DISPUTE ROW]`) interleaved, nearest date first. Work it top-down. **Before starting, read the header of `memory/research_log.md`** (down to `# Research Sessions`): carry-overs whose next check is due and any READ FIRST block belong on today's list. For each symbol:

1. **Check for a cached IR URL** in the dispute data. If one exists, try WebFetch on it first.
2. **If no cached URL, WebSearch** for the company's earnings date (e.g., "GILD earnings date Q2 2026" or "Gilead Sciences investor relations earnings"). Do this yourself — do not spawn agents.
3. **Look for the official IR press release or investor events page.** Do not use third-party pages. Be mindful of the current date — the correct earnings date should be within a few weeks of it.
4. **Extract:** the correct earnings date + BMO/AMC timing.
5. **Confirm via CLI:**
   ```
   python E:\options_scanner\tools\earnings_confirm.py --symbol SYM --date YYYY-MM-DD --time bmo --by agent
   ```
6. **Save the IR URL:**
   ```
   python E:\options_scanner\tools\direct_db_query.py --db E:\options_scanner\data\datalake.db --write --sql "UPDATE symbol_metadata SET ir_earnings_url='{URL}', ir_url_last_verified='{TODAY}' WHERE symbol='{SYM}'"
   ```
7. **Update dispute resolution**:
   ```bash
   python E:\options_scanner\tools\direct_db_query.py --db E:\options_scanner\data\performance.db --write --sql "UPDATE earnings_date_disputes SET resolution='confirmed_agent', resolved_date='{DATE}', resolved_time='{TIME}', resolved_at='{NOW}', research_url='{URL}' WHERE trade_date='{TODAY}' AND symbol='{SYM}'"
   ```
8. **Log your work** to `memory/research_log.md`: the session block, ledger lines and carry-over updates in the header, and a `memory/reference_company_cadence.md` row (with the advance-PR lead) for each first-time name.

---

## Session Modes

You run in one of two modes. `launcher.py` writes a `.session_mode` marker that your context hook reads to decide what to inject.

| Mode | When | Prompt | What the hook injects |
|------|------|--------|------------------------|
| **Daily** (default) | Weekdays, via the orchestrator | embedded template in `launcher.py` | `<dispute-list>`: one queue of today's disputes + unconfirmed rows due ≤14d, nearest date first, max 40 |
| **Maintenance** | Sundays, via Task Scheduler | `PROMPT_SUNDAY.md` | `<maintenance-session>` — workspace stats, no disputes |

The Sunday session is workspace upkeep + self-calibration, NOT research: archive the research log into `memory/archive/` (quarterly, named by earnings season), promote recurring facts into `memory/reference_company_cadence.md`, prune `notes_for_ben.md`, rotate `outbox/`, and update `STATUS.md`. The dispute list is suppressed on purpose that day — follow `PROMPT_SUNDAY.md`. Launched by `scheduled_tasks/start_earnings_researcher_sunday.bat` (two-step: `launcher.py --prepare-only --prompt PROMPT_SUNDAY.md`, then a visible `claude` window).

---

## Critical Rules

- **NEVER overwrite a date confirmed by Ben** (`date_confirmed_by = 'ben'`). If you disagree with Ben's date, log it in `memory/research_log.md` but do NOT change it.
