# Weekday sessions are coming back: the Earnings Module (your 11-09 handoff, Phase 1)

**From:** dev session with Ben, 2026-11-18

Your handoff turned into PRD 0015 (`tasks/0015-prd-earnings-module.md` in the parent repo, local only). Decisions Ben
made on 11-09:
1. The first piece is the restore: a separate task, `\!Earnings Module`, weekdays 06:00, in either mode.
2. The poller (Phase 3) writes **candidates** only. You approve or reject each one. Nothing confirms without you.
3. Fetchers (browser-UA IR feeds, stocktitan) live in **your** workspace, not the public repo.
4. The Sunday session stays exactly as it is.

**What runs now (Phase 1), in order:**
- (a) **Full calendar refresh** (the old Friday 5.3) whenever the last successful one is more than 6 days old. The first
  run does it straight away, so you'll research a calendar refreshed that morning, not the 10-19 one.
- (b) **Lite refresh** (yfinance/Finnhub re-check of unconfirmed rows due within 21 days, writes today's disputes).
- (c) **Your spawn**, same launcher and same gate as before (disputes or unconfirmed rows due within 14 days), at most
  once a day.

**When:** once Ben registers the task (a pending gate). Your session-gap warning will keep firing until the first run.
The 10-20 → first-run gap is an outage, not a skip pattern; don't score it as one.

**Not changed:** your hook, launcher, prompt, `earnings_confirm.py`. Phase 2 (registry tables, seeding session) comes
after Ben has watched a few live runs.
