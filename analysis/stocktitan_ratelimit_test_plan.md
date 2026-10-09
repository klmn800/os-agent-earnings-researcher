# Stocktitan rate-limit test: plan (written 2026-10-09, before compaction)

Goal: find a spacing and a retry policy for `analysis/helpers/spine.py` that avoids 429s, then edit
`spine.py` with a short note of what the experiment showed. Ben and I run it together in the Claude
window; there's time to let it run as long as needed. Also a tool-learning exercise for me: be honest
about what I observe and what I only infer.

## What we already know (observations, n is tiny)
- 10-09 ~07:25: 8 requests at 9s spacing returned 200. A second batch minutes later returned 429
  on its FIRST request (9 of 9 blocked, ~2.5 KB body, no other header info captured).
- That block was gone by 08:02 (one request returned 200). So it lasted under ~40 min. Exact end unknown.
- 08:02 → 08:07: 10 requests (20s spacing) returned 200; the 11th (SF) returned 429.
- WebFetch of stocktitan *article* pages kept working while curl on listing pages was blocked
  (NEE/GL/QS at ~08:08). WebFetch egresses from somewhere other than this machine, so the block is
  probably per-client-IP. This is an inference from 3 fetches, not a test.
- `curl` with NO user agent / headers gets **403 "Forbidden"** (9 bytes) even when not blocked
  (checked 09:4x: robots.txt 200, bare listing 403). So the 403 I saw at 08:07 was probably
  header-based filtering, not the rate-limit state. n=2, one session.
- Not captured yet: 429 response headers (Retry-After etc.). The probe script records Retry-After.

## Unknowns the test should settle
1. How many requests pass from a cold start at spacing S before the first 429? (burst size)
2. After a 429, how long until a request passes again? (recovery time, as a bracket)
3. Does a refilled budget match a cold start (cycle 2 burst count vs cycle 1)? Sliding window vs bucket.
4. Does probing during a block extend it? (dense vs sparse schedules)
5. Does spacing matter at all (10s vs 20s vs 40s), or is it a total count per window?
6. What does the block cover: whole site, listing pages only, article pages too? (side probes)
7. Does WebFetch of the *listing* page work while curl is blocked, and does it return the headlines
   usably? (manual arm, see below)

## Tool: `analysis/helpers/stocktitan_probe.py`
`python analysis/helpers/stocktitan_probe.py --spacing 20 --cycles 2 --probe-schedule 30,60,120,180,300`
Per cycle: BURST (one request per --spacing seconds until first non-200) then RECOVERY (probe at the
schedule's intervals until a full page returns; last interval repeats; give up at --max-recovery 3600s).
Cycle 1 also runs five SIDE probes once, right after the first block (root, robots.txt, listing with
spine headers, listing with bare curl, an article), 5s apart. Everything is appended to
`inbox/fetch/stocktitan_probe_log.csv` as it happens.
Recovery time is a bracket: between the last failed probe and the first good one.

## Run matrix (each run starts after >=15 min of no stocktitan traffic from this machine)
| Run | Command | Answers |
|-----|---------|---------|
| 1 | `--spacing 20 --cycles 2 --probe-schedule 30,60,120,180,300` | burst size at 20s, recovery bracket (dense probes), refill (cycle 2), side probes |
| 2 | `--spacing 20 --cycles 2 --probe-schedule 300` | same, sparse probes. Compare recovery with run 1 for probe-extension |
| 3 | `--spacing 10 --cycles 2 --probe-schedule 60,120,300` | does spacing change the burst size? |
| 4 | `--spacing 40 --cycles 1 --max-burst 40` | does slow spacing avoid blocking at all? |
Adjust after run 1. If run 1 shows no block within max-burst at some spacing, that spacing is a candidate
production value; confirm with a second run before trusting it.

## How I (Claude) run it, and what I want to learn about my own tools
- Bash foreground calls cap at 10 min, so run with `run_in_background: true` and expect a
  notification when it exits. Load `Monitor` via ToolSearch and tail the log/stdout so I see the
  first BLOCKED and the recovery line as they happen, not only at exit.
- Questions about my tooling to answer honestly afterward: does a ~1 hr background job survive and
  notify? does Monitor stream lines promptly? do I stay responsive to Ben meanwhile?
- Manual arm during run 1's block (when Monitor shows the first BLOCKED): one `WebFetch` of
  `https://www.stocktitan.net/news/SF/` asking for headlines+dates, to settle unknown 7.
  WebFetch caches 15 min per URL, so use a symbol not fetched earlier.
- No research sessions should hit stocktitan while a run is in progress (this test provokes blocks).

## When done
- Write results (counts, brackets, what was inference vs observation) at the bottom of this file.
- Edit `spine.py`: default spacing, stop-or-backoff on 429 (so it never logs a 429 as absence),
  and a comment block summarizing this experiment. Update `memory/reference_stocktitan_jsonld_discovery.md`.
- Update the 10-09 log session block (bookkeeping still owed: FAF, NEE, GL, QS confirms; cadence rows;
  ledger lines; remove them from READ FIRST / carry-over rows).
