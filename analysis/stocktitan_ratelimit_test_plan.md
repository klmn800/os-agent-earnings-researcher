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
  ledger lines; remove them from READ FIRST / carry-over rows). **Done** (commit cdcdca5).

---

# RESULTS (run 2026-10-09, 10:18 to 12:56 ET, this machine's IP, curl with the spine request shape)

Everything below is labelled **Observed** (a log line shows it) or **Inferred** (my reading of the observations).
Raw per-request rows: `inbox/fetch/stocktitan_probe_log.csv` (runs 1 and 3) and `stocktitan_probe_log_v2.csv`
(runs 4b/4c, which add a curl exit/error column).

## Runs as executed (the plan changed as results came in)
| Run | Spacing | What happened |
|-----|---------|---------------|
| 1 | 20 s, 2 cycles | cycle 1: 10 passed, the 11th got a 429 (`Retry-After` 94). Cycle 2: 9 passed plus the recovery probe that opened the window (= 10), then a 429 with `Retry-After` 115. |
| 3 | 10 s, 2 cycles | cycle 1: 10 passed, 429 with `Retry-After` 195. Cycle 2: 9 passed plus the opening probe, 429 with `Retry-After` 205. |
| 2 | (dropped) | It was to compare sparse and dense probes. Runs 1 and 3 already showed a probe 30 s into a block did not move the end time, which the header gave exactly. |
| 4 | 40 s | **Not a rate-limit result.** Request #4 got `http=000` and the probe called it a block. Curl's error was not captured then. |
| 4b | 40 s | 9 passed, then `curl exit 28: Failed to connect ... port 443` on #10, and the Google control request failed with `exit 6: Could not resolve host`. **A local network outage of about 3 min, not stocktitan.** Run 4 was probably the same (11:18 to 11:21, 30 min earlier) but had no control request, so that is **unconfirmed**. |
| 4c | 40 s | **40 of 40 returned 200** over 26 min (12:07 to 12:33). No 429, no outage. |
| 5 | 5 s inside a 9-request budget | The production `spine.py` on 30 real symbols: **30 of 30 read, zero 429s, zero UNREAD**, with 3 sleeps of 256 to 257 s between windows. |

Probe fixes made on the way (commits 1c0c509, 97ab660): curl's exit code and message are recorded; a no-response failure is
checked against Google; if Google also fails, the probe waits for the network and retries without counting the attempt.

## Findings
1. **Observed:** a 429 carries `Retry-After`, and it is exact. In all 4 blocks every reading inside the block (3 to 5 each) pointed to the same
   end time within 1 s, and the first 200 came back inside the bracket it predicted.
2. **Observed:** in all 4 blocks the time from the first request of the window to the end of the block was **299 to 300 s**
   (10:18:27 to 10:23:26, 10:23:49 to 10:28:49, 10:46:08 to 10:51:08, 10:51:20 to 10:56:20). Cycle 2 of each run opened its window with the
   recovery probe that returned the first 200 and then passed 9 more, so **10 requests per window**; the 11th was refused.
3. **Observed:** the pass count did not depend on spacing (10 s and 20 s both gave 10). The penalty (94 to 115 s at 20 s spacing, 195 to 205 s at
   10 s) is just the rest of the 300 s window, so a faster burst leaves more of it.
4. **Inferred (fits 4 of 4 blocks, plus 40/40 and 30/30 clean passes):** a **fixed 300 s window, opened by the first request, limit 10.**
   Not tested: fixed versus sliding window. Both predict the same for a policy of 10 or fewer per 300 s from the first request.
5. **Observed:** the block is site-wide: root, listing pages and article pages returned 429, and **`/robots.txt` returned 200 in both runs** (exempt).
   A **bare `curl` with no User-Agent returned 403 in both runs and also when not blocked** (header filtering, not the rate limit).
6. **Observed:** probes during a block (every 30 to 120 s) did not extend it. Not tested: whether a flood of probes would.
7. **Observed (n = 1):** WebFetch read the listing page `https://www.stocktitan.net/news/SF/` while curl was blocked.
   **Inferred, not tested:** WebFetch has its own egress, so the limit is per client IP. I did not test whether WebFetch calls count against
   curl's window, and kept the two apart during run 5 so as not to confound it.
8. **Validation (run 5):** the policy "9 per 300 s + 5 s pad, shared counter" read 30 symbols across 4 windows without a refusal. That confirms the
   window length and the pad. It did **not** test the edge itself (10 allowed, 11 refused), which rests on the 4 blocks.

## What changed in production
`analysis/helpers/spine.py` (commit efd62f2) enforces the budget (9 per 300 s + 5 s; state in `inbox/fetch/.stocktitan_window.json`, shared by
separate invocations), sleeps until the window closes (or stops with `--no-wait` and lists the unread symbols), honours `Retry-After` on a 429, and
separates a local network outage from a stocktitan failure. Throughput is about 9 symbols per 5 min. **30 symbols took 15 min; a foreground Bash call
times out at 10 min, so use `run_in_background` past about 17 symbols.**

## What I learned about my own tools
- **Background jobs plus Monitor worked well.** A job with a 15-minute pre-wait and a 30-minute run survived (the 10-minute Bash cap applies to foreground
  calls). Monitor delivered each flagged line within seconds. Its 30-minute cap needs re-arming (I did it 4 times); `tail -n 3 -f` on an existing file
  avoids replaying old lines.
- **Monitor filters that match every `side` or `control` line produce one notification per line**, and each one dragged the full dispute-list hook output
  into the conversation. Narrower filters would have cut about 15 of those.
- **I labelled run 4 a block because the tool did.** The probe collapsed three different failures (429, no connection, local outage) into one word,
  "BLOCKED". Recording the curl error is what exposed it. A status label is a claim; log the raw error.
- **I fit the rule after the fact.** The 300 s constant came from looking at four blocks. Run 5 was written down as a prediction that could fail before it ran.
- **A combined command (syntax check, run, delete, commit, push) was denied.** Its pieces ran fine separately. Keep deletes and pushes in their own calls.
