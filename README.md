# Earnings Researcher

An autonomous Claude Code agent that resolves disputed earnings dates for the [Options Scanner](https://github.com/klmn800/options_scanner) system. When the Earnings Intelligence pipeline's stored date disagrees with a secondary source (or the report timing — before/after market — is unknown), this agent researches the correct date from an authoritative source and writes the confirmation back to the database.

It runs unattended on a daily schedule, plus a weekly self-maintenance session. It's one of five specialized agents in the Options Scanner's [agent fleet](https://github.com/klmn800/agent_lab); see `agents/README.md` in the parent repo for how the fleet fits together.

---

## What it does

Each weekday, the parent orchestrator's Earnings Intelligence pipeline flags symbols where the stored earnings date/time doesn't match what a secondary source (Finnhub) says, or where the BMO/AMC timing is unknown. Those land in `earnings_date_disputes` in `performance.db`. This agent:

1. Reads today's unresolved disputes, prioritized (date disagreements first, then timing-only gaps).
2. Prints a session-opener table so a human glancing at the terminal can see the plan before any tool calls happen.
3. For each symbol: checks a cached IR (investor relations) URL if one exists, otherwise web-searches for the company's own earnings announcement — never third-party aggregators, since those are exactly what's already in dispute.
4. Confirms the date via CLI (`tools/earnings_confirm.py`) and records the source URL, or skips and logs its reasoning if it can't find a reliable source.
5. **Never overwrites a date a human has already confirmed.** If the agent disagrees with a human-confirmed date, it logs the disagreement — it does not change the row.

On Sundays, it runs a different session entirely: no dispute research, just workspace upkeep — rolling the research log into quarterly archives, promoting recurring per-symbol facts (typical lead time between a company's "save the date" PR and the actual report, BMO/AMC pattern, which source actually works for that IR page) into structured reference memory, and an honest self-check on whether last week's skip judgment held up. See `PROMPT_SUNDAY.md` for the full checklist.

## Launching

```powershell
python launcher.py                    # Daily dispute-resolution session, visible window
python launcher.py --headless         # Same, no window (captures output, 45min timeout)
python launcher.py --limit 10         # Cap the batch to 10 highest-priority disputes
python launcher.py --prompt PROMPT_SUNDAY.md --prepare-only   # Sunday session, two-step launch
```

In normal operation this is launched by the parent repo's daily orchestrator (weekdays) and by Task Scheduler via `scheduled_tasks/start_earnings_researcher_sunday.bat` (Sundays) — you don't run it by hand unless you're testing.

If there are no unresolved disputes for the day, the launcher prints that and exits without spawning a Claude session — no wasted tokens on an empty queue.

## How context gets injected

`launcher.py` writes the day's prompt to `.session_prompt.md` and a mode marker (`daily` or `weekend`) to `.session_mode`. A `UserPromptSubmit` hook (`hooks/inject_context.py`) reads that marker and injects the right block at session start: `<dispute-list>` for daily runs, `<maintenance-session>` (workspace stats, no disputes) for Sunday. This is what lets the same agent identity run two very different session shapes without two separate prompt files driving the actual model turn.

## File layout

```
agents/earnings_researcher/
├── README.md                 (this file)
├── CLAUDE.md                 (weekday research workflow — the operational template
│                              also lives inline in launcher.py's PROMPT_TEMPLATE)
├── PROMPT_SUNDAY.md           (Sunday maintenance-session prompt)
├── launcher.py                (spawns the Claude Code session; builds the daily prompt)
├── hooks/inject_context.py    (UserPromptSubmit hook — injects dispute list or maintenance stats)
├── memory/
│   ├── research_log.md            (running day-by-day session log)
│   ├── archive/                   (quarterly rollups, named by earnings season)
│   ├── MEMORY.md                  (index of typed memory files)
│   ├── reference_company_cadence.md  (per-symbol lead time / BMO-AMC / source notes)
│   └── feedback_*.md, reference_*.md, project_*.md   (structured memory, promoted Sundays)
├── analysis/                  (one-off research/probe scripts — kept as a record of method)
├── inbox/, outbox/            (mailbox mesh to peer agents — System Analyst, Trading Advisor, Market Analyst)
├── STATUS.md                  (dashboard: open carry-overs, next-check dates, confirm rate)
└── notes_for_ben.md           (open items surfaced for the human)
```

## Design and rationale

This workspace is a standalone git repo (gitignored from the parent `options_scanner` checkout) so the agent's memory and logs persist independently. The framework skeleton that makes agents like this one possible — launchers, context-injection hooks, session modes, the mailbox mesh — is published separately at [`agent_lab`](https://github.com/klmn800/agent_lab); this repo is the actual working state built on top of it.
