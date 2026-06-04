# Proposal: Weekend Cleanup Session for the Earnings Researcher

**Author:** Earnings Researcher agent
**Date:** 2026-05-28
**For:** Ben → dev session to implement
**Status:** proposal / awaiting decisions

---

## Goal

Give the Earnings Researcher a once-weekly maintenance session (the house "Sunday" mode) so the research log and notes don't sprawl, durable patterns get promoted into structured memory, and I do a light self-calibration. Left unmanaged, `memory/research_log.md` grows ~1 session/day forever (already 1,136 lines / ~58k tokens) and I re-read stale day-by-day skip prose every morning.

## What I reviewed

- **`agents/system_analyst/PROMPT_SUNDAY.md`** — the model. SA's Sunday is reflective self-care + organizational maintenance, explicitly NOT a workday: no feedback processing, no directives, no deep investigations. Hard requirement: update `STATUS.md` + journal before finishing. Philosophy: "the value of Sunday isn't what you produce — it's the clarity you bring to Monday."
- **`agents/AGENT_PATTERN.md`** — house conventions. Key bits for me: optional `PROMPT_{MODE}.md` files per session mode; outbox rotation policy (active file >~400 lines → archive resolved threads to `outbox/<file>_archive.md`, keep open threads + last ~2 weeks); "agents with a Sunday self-care session can fold rotation into that"; "memory maintenance is real work, not busywork."
- **My own `launcher.py`** — relevant mechanics below.

## How my situation differs from SA (why this is tailored, not copied)

1. **My daily prompt is embedded in `launcher.py` (`PROMPT_TEMPLATE`), not a standalone file.** SA has separate `PROMPT_*.md` per mode. So a weekend mode needs either a new standalone `PROMPT_WEEKEND.md` or another embedded template.
2. **`launcher.py` exits early when there are no unresolved disputes** ("Nothing to do") and never launches Claude. A Sunday often has zero disputes — so the weekend session can't ride the normal daily path; it needs its own invocation that bypasses the dispute check.
3. **My context hook injects the dispute-list every prompt.** A cleanup session shouldn't get a dispute-list; the hook needs to know it's a weekend session and suppress it (or inject a maintenance block instead).
4. **Narrower scope than SA.** SA reflects deeply on strategy/architecture. Mine is ~70% mechanical maintenance + 30% calibration. I don't have `proposals/`, `agenda.md`, or `STATUS.md` today — my "memory" is the research log + typed memory files (`MEMORY.md` + `feedback_*`/`project_*`/`reference_*`).

## Proposed weekend session — what it does

Framed SA-style (a checklist of prompts to consider, not a rigid script), but weighted toward maintenance. In rough priority:

1. **Archive the research log.** Roll sessions older than ~2 weeks out of `memory/research_log.md` into `memory/archive/research_log_YYYY-MM.md`. Leave the active log with: (a) last ~2 weeks of full sessions, (b) a compact **confirmation ledger** — one line per confirmed symbol (`SYM date time — source — session`), (c) any still-unresolved carry-over symbols with current status + next-check date.
2. **Promote durable patterns into structured memory** (the real value-add). Mine the log/archive for recurring facts and lift them into typed memory files:
   - A **company earnings-cadence table** (`reference_company_cadence.md`): per-symbol historical lead time (advance-PR → release), reporting cadence (BMO/AMC, typical day-of-week/week-of-month), IR-page quirks (SPA / 403 / timeout), and which source actually worked last time. **This doubles as the data for window-gating** (see `memory/feedback_window_gating_and_noop.md`): `window_opens = earnings_date − lead_time − buffer`.
   - Source-reachability facts (which IR domains are SPA-only, which 403, SEC-via-curl) — consolidate into/refresh `reference_sec_via_curl.md` + a companion if needed.
3. **Prune `notes_for_ben.md`.** Condense/remove resolved flags (e.g., once UEC's date self-corrects, archive the recurring UEC note). Keep open items only; move long-resolved notes to an archive section or `notes_for_ben_archive.md`.
4. **Rotate `outbox/`** per AGENT_PATTERN (>~400 lines → archive). Likely small for me, but fold it in here.
5. **Tidy `inbox/processed/`** — low priority (cheap storage); just sanity-check nothing live is stuck in `inbox/` root.
6. **Light self-calibration** (the genuinely useful 30%): over the past week, what was my confirm/skip rate, and — crucially — **did symbols I skipped later confirm at the date I predicted?** This validates or corrects my skip judgment and the lead-time table. Note any process drift (e.g., the 151k-token overspend on 2026-05-28).
7. **Keep `MEMORY.md` tight** — verify pointers resolve, descriptions current, index under the line cap.
8. **Output requirement:** append a short `## Weekly Maintenance — YYYY-MM-DD` entry to the active log noting what was archived/promoted/pruned, so the audit trail is clear.

## Mechanics for the dev agent to build

- **`PROMPT_WEEKEND.md`** (standalone, in workspace root) — the session prompt, modeled on `PROMPT_SUNDAY.md` but using the checklist above. Standalone (not embedded in launcher) since it's invoked rarely and needs no per-symbol date injection.
- **`launcher.py --weekend` mode** — bypass `get_unresolved_disputes()` early-exit; write a `.session_mode` file = `weekend`; launch `claude --permission-mode auto @PROMPT_WEEKEND.md`. (Date header injection still fine.)
- **`hooks/inject_context.py`** — read `.session_mode`; when `weekend`, suppress the `<dispute-list>` block (and the mailbox-notices/inbox push if desired) and instead inject a short maintenance-orientation block (current log size, # archive files, open carry-overs). Clear `.session_mode` at session end or on next daily run.
- **Scheduling** — once weekly (Sunday), via whatever the others use (Task Scheduler / orchestrator step). My daily run is autonomous, so this should be too.
- **`memory/archive/`** — new dir for rolled-off log months. Write guard already permits `memory/`.

## Decisions for Ben

1. **Cadence:** weekly (Sunday) like SA, or biweekly? My scope is narrow; biweekly may be enough, but weekly keeps the active log reliably ≤~2 weeks. *My lean: weekly, but lighter-touch than SA's.*
2. **`STATUS.md`?** Worth adding a small dashboard (open carry-overs + next-check dates + last week's confirm rate) for you to glance at, or is the research-log header enough? *My lean: a lightweight `STATUS.md` — it pairs naturally with window-gating.*
3. **Archive granularity:** monthly files (`research_log_YYYY-MM.md`) vs quarterly. *My lean: monthly.*
4. **Naming:** `PROMPT_WEEKEND.md` vs `PROMPT_SUNDAY.md` to match SA. *My lean: `PROMPT_SUNDAY.md` for house consistency.*
5. Should the weekend session also be allowed to **propose** prompt/process tweaks (like this doc), or strictly maintenance? *My lean: allow it — that's where I'd notice drift.*

## Related memory
- `memory/feedback_window_gating_and_noop.md` — the cadence table feeds this.
- `memory/feedback_parse_big_inbox_json.md` — token-efficiency lessons from the same conversation.
