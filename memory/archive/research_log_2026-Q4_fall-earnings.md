# Earnings Research Log — Archive: 2026 Fall Earnings Season

> Fall 2026 earnings season — Q3 calendar results (plus off-cycle fiscal quarters reporting in the same wave), reported ~late September
> through mid-November 2026. Opened at the 2026-10-18 maintenance with sessions **2026-09-28 → 2026-10-02** (09-28 → 09-30 are
> calendar-Q3 days, filed here because they researched the fall wave) and the 2026-09-27 maintenance entry. Chronological order,
> oldest first. Appendix A keeps ledger rows verbatim as they are pruned (the record later source audits draw from).

---

## Session: 2026-09-28 (Monday) — 07:14 AM ET

6 surfaced (3 disputes: AMX, REXR, WIT `date_disagreement`; 3 disputes: AGNC, CCK, FITB `unknown_time`).
**2 confirmed on company sources (CCK, FITB), 1 time-only (AGNC), 3 held (AMX, REXR, WIT).** 0 dates changed;
1 `Unknown` time filled via historical pattern (AGNC amc), 2 unknown times filled + dates re-confirmed (CCK amc,
FITB bmo). Also fixed a standing bug: AMX's cached IR URL used the broken `pageSize=25` feed param (returns
only 2014–2018 events) — re-cached with `pageSize=100` per the 09-22/09-25 cadence notes.
Reads: 6 searches, 11 WebFetches (2 AGNC investors.agnc.com timeouts, fell back to SEC EDGAR 8-K exhibits).

### Confirmed

| Symbol | Resolution | Evidence |
|--------|-----------|----------|
| **CCK** | **2026-10-19 `amc`** (date + time both company-sourced; dispute closed) | crowncork.com/news 09-22 PR *"CROWN HOLDINGS SCHEDULES THIRD QUARTER 2026 EARNINGS CONFERENCE CALL"*: *"release its earnings for the third quarter ended September 30, 2026, after the close of trading on the New York Stock Exchange on Monday, October 19, 2026,"* call Tue 10-20 9:00am EDT. Cached dispute URL (crowncork.com "Schedules Second Quarter 2026...") was stale — replaced with the Q3 PR. |
| **FITB** | **2026-10-19 `bmo`** (date + time both company-sourced; dispute closed) | ir.53.com event-details page for the 3Q26 call (Oct 19, 2026, 9:00am ET); the 2026/2027 annual-dates PR states results are available ~6:30am ET ahead of the call ⇒ bmo. No cached IR URL existed before today — now cached. |
| **AGNC** | **`amc` written via `--time-only`; 2026-10-19 date NOT locked** | No company 8-K/PR found for 3Q26 specifically (SEC EDGAR CIK 1423689 newest 8-K is the 07-20 Q2 release). Time rests on a clean 3/4-year pattern instead: 3Q22, 3Q23, 3Q25 press releases all state *"after market close"* (3Q24's 8-K is silent on timing but same release-day shape); all four years released on the **3rd Monday after quarter-end** (10-24 '22, 10-23 '23, 10-21 '24, 10-20 '25), and 2026-10-19 continues that exactly. Confident enough on time to close the `unknown_time` question; not confident enough on date to lock it without a same-quarter source — matches the FNB/SNA/REXR/ACI precedent of `--time-only` + dispute row `confirmed_agent`, calendar row left unconfirmed. |

### Held

| Symbol | Why held | Next check |
|--------|----------|------------|
| **AMX** | No 3Q26 event yet on the (now-fixed) Event.svc feed — newest is 2Q26 (07-21 amc). DB's 10-13 continues the Tuesday-amc 17→15→14 trend; finnhub's 10-20 is the known +7d artifact shape for this name. | 09-29, then 10-06 |
| **REXR** | No Q3 advance PR (press-releases list checked fresh, events-webcasts page explicitly says no upcoming events). Shortest-lead due date (09-20) is now 8+ days overdue; the 4th-Thursday-2026 cadence guess (10-22) is unconfirmed and its own PR due date (09-28) also just passed. | 09-29, then 09-30 |
| **WIT** | No board-meeting advance PR yet; per the cadence file the 9d-lead pattern puts one due ~10-06, so its absence today isn't informative. Cadence-predicted 10-15 `bmo` matches the DB row exactly; finnhub's 10-13 doesn't fit the Thursday-since-2024 pattern. | 10-06, then 10-07 |

### Notes

- `reference_company_cadence.md` already had detailed prior work on all six symbols (AMX, REXR, WIT held from
  09-22 → 09-25; CCK/FITB/AGNC were first-time names) — checked it before re-researching from scratch, which
  saved a redundant pass on the three held names and confirmed today's holds are consistent with the standing
  reasoning rather than new information.
- AGNC's `investors.agnc.com` news-release detail page timed out on WebFetch twice; SEC EDGAR 8-K exhibits
  (which render reliably) were used instead for the historical timing evidence.
- New cadence rows written for CCK, FITB, AGNC in `reference_company_cadence.md`.

---

## Session: 2026-09-29 (Tuesday) — 07:14 AM ET

22 surfaced (16 disputes, 6 unconfirmed). **8 confirmed on company sources (REXR, VZ, KEY, JNJ, JPM, UNH, WFC, DPZ), 14 held.**
0 stored dates changed (snapshot was stale for REXR 10-14→10-22 and VZ 10-20→10-26; live rows already had them). 2 `Unknown` times filled (VZ, KEY bmo).

### Confirmed

| Symbol | Result | Source |
|--------|--------|--------|
| **REXR** | **2026-10-22 `amc`** (the 4th-Thursday reading was right; finnhub 10-21 / yf 10-22) | ir.rexfordindustrial.com detail/380, PR **09-28 16:05 ET**: *"release third quarter 2026 financial results after the market closes on Thursday, October 22, 2026,"* call Fri 10-23 11am ET. Lead 24d. Dispute closed. |
| **VZ** | **2026-10-26 `bmo`** (yfinance was right; finnhub 10-20 wrong) | Verizon GlobeNewswire/verizon.com **09-28**: *"Monday, October 26, 2026,"* materials 7:00am ET, webcast 8:30am. Dispute closed. |
| **KEY** | **2026-10-20 `bmo`** | investor.key.com 2026 call-dates PR: *"Third quarter 2026 – Tuesday, October 20th, 2026 at 8 a.m. ET,"* results before market open. |
| **JNJ** | 2026-10-13 `bmo` | investor.jnj.com PR 08-31: call 8:30am ET Tue 10-13; release ~6:45am. |
| **JPM** | 2026-10-13 `bmo` | jpmorganchase.com/ir PR 09-17: call 8:30am ET, results ~7:00am. |
| **UNH** | 2026-10-13 `bmo` | unitedhealthgroup.com PR 09-15: results before open, call 8:00am ET. |
| **WFC** | 2026-10-13 `bmo` | newsroom.wf.com *"Wells Fargo Updates 2026 Earnings Release Date Information"*: results ~7:00am ET, call 10am. |
| **DPZ** | 2026-10-13 `bmo` | Domino's PR 09-10 16:05 ET (read via stocktitan wire text; ir.dominos.com timed out): webcast 8:30am ET, results 6:05am. |

### Held

| Symbol | Why | Next check |
|--------|-----|------------|
| **AMX** | Event.svc feed (pageSize=100, parsed with strptime — string-sorting `MM/DD/YYYY` gives garbage) newest still 2Q26; no 3Q26 event. | 10-06 |
| **WIT** | No advance PR yet (due ~10-06). | 10-06 |
| **ACI** | stocktitan newest 09-17, no FQ2 advance. 10-20 still the doubt. | 09-30, 10-07 |
| **KO** | No Q3 timing PR (spine newest 09-25). ⚠ **Q2-26 reported Tue 07-28** — DB 10-20 looks early; finnhub 10-27 may be right this time. Q1/Q2 timing PRs came ~3 weeks ahead. | 09-30 |
| **CLF, EQT** | No Q3 advance (Q2 PRs came 07-02 for 07-23 / 07-21, 19–21d lead ⇒ due ~10-01). DB 10-20 unsourced; bad-batch names (see confirmed_row_diverged). | 10-01 |
| **RTX, LMT, PNR** | No Q3 date found. Q2-26 was Thu 07-23 (RTX, LMT), Tue 07-28 (PNR) — DB 10-20 doubtful. | 10-01 |
| **ADC, PEGA, AGNC** | No Q3 advance found (ADC PRs ~10-01; Q2 was 07-30, so 10-20 doubtful; PEGA Q2 07-21 advance 07-07; AGNC IR/EDGAR silent). | 10-01 |
| **MMM, GPC** | No Q3 date/time yet. GPC Q3'25 advance was 09-30 → due 09-30/10-01. | 10-01 |

### Notes
- Stale snapshot again: REXR and VZ live rows were already right; locks, not corrections.
- WebSearch for KO/RTX/LMT/PNR returned only estimates or Q2 data — not used.
- `direct_db_query` writes print "No results returned"; verified via SELECT that they landed.

---

## Session: 2026-09-30 (Wednesday) — 07:14 AM ET

28 surfaced (all disputes: 20 `date_disagreement`, 4 `both`, 4 `unknown_time`). **8 confirmed on company sources (FNB, KO, RTX, MCO, NLY, GPC, CSX, WH; GPC time inferred), 5 time-only (MMM, VRT, WAL, LRCX, UAL), 15 held incl. LRCX/UAL dates.**
Stored dates changed: FNB 10-15→**10-19** (company PR; yfinance was right, finnhub 10-15 wrong). Others matched the live calendar already (stale snapshot again).

### Confirmed

| Symbol | Result | Source |
|--------|--------|--------|
| **FNB** | **2026-10-19 `amc`** (DB 10-15 was wrong; Q2 lead was 16d, this one 20d) | fnb-online.com PR **09-29**: *"after the market close on Monday, October 19, 2026,"* call Tue 10-20 8:30am ET. |
| **KO** | 2026-10-27 `bmo` (finnhub+yfinance right, DB 10-20 doubt resolved) | investors.coca-colacompany.com detail/1173, PR 09-29 10:00 EDT: *"release third quarter 2026 financial results Oct. 27 before the NYSE opens,"* call 8:30am. Cached URL was the Q2 PR — replaced. |
| **RTX** | 2026-10-20 `bmo` (finnhub 10-27 wrong) | rtx.com PR 09-29: *"Tuesday, October 20, prior to the stock market opening,"* call 8:30am. |
| **MCO** | 2026-10-21 `bmo` (finnhub 10-27 wrong) | Business Wire 09-30 07:00 ET (read via financialcontent copy): *"before the start of NYSE trading on Wednesday, October 21, 2026,"* call 9:00am. ⚠ `ir.moodys.com` news-details URL returned the Q4-25 release when fetched — stale cache, don't use. |
| **NLY** | 2026-10-20 `amc` (yfinance right, finnhub 10-28 wrong) | Business Wire 09-29 (financialcontent copy; businesswire.com 403s WebFetch): *"after the market close on Tuesday, October 20, 2026,"* call Wed 10-21 9:00am. |
| **GPC** | 2026-10-20 (finnhub 10-15 wrong); time **`bmo` inferred** | genpt.com PR 09-29 states date + call 8:30am ET but NOT bmo/amc. bmo from SEC Item 2.02 pattern: 6/6 quarters furnished 11:21–12:09Z (07:2x ET). |
| **CSX** | 2026-10-21 `amc` | GlobeNewswire 09-21: *"after the market close on Wednesday, Oct. 21, 2026,"* call 4:30pm ET. |
| **WH** | 2026-10-21 `amc` | investor.wyndhamhotels.com detail/430, PR 09-23: *"Wednesday, October 21, 2026 at approximately 4:30 p.m. ET,"* call 10-22 8:30am. |

### Time-only (date NOT locked) — from SEC Item 2.02 acceptance times, all 6–7 quarters consistent (times UTC `Z`)
MMM `bmo` (10:33–11:34Z) · VRT `bmo` (10:00–11:00Z) · WAL `amc` (20:08–20:26Z) · LRCX `amc` (20:07–20:09Z) · UAL `amc` (20:00Z). Dispute rows closed `confirmed_agent` only for LRCX and UAL (`unknown_time`); MMM/VRT/WAL left `unresolved` since their dates are still disputed.

### Held

| Symbol | Why | Next check |
|--------|-----|------------|
| **AMX** | Event.svc feed (pageSize=100, strptime) newest still 2Q26 (07-22 call); no 3Q26. | 10-06 |
| **WIT** | No advance PR (due ~10-06). | 10-06 |
| **LMT** | Only aggregators say 10-27; no company PR (Q2 PR was 07-01, Q1 04-01 ⇒ Q3 due ~10-01). news.lockheedmartin.com slug guess 404. investors.lockheedmartin.com 403 to curl. | 10-01 |
| **PNR, EQT, CLF** | No Q3 advance found (PNR Q1 PR 04-14 for 04-28 ⇒ ~2wk lead; EQT/CLF due ~10-01). | 10-01 |
| **ADC** | Q3 PRs historically ~10-01/10-04; none yet. | 10-01 |
| **PEGA, AGNC, GL, QS, RHI, SF, TER, VLTO** | No company Q3 date found by search. (SF Q2 PR came 07-15; RHI Q2 PR 07-16 ⇒ ~1 week lead; VLTO Q2 PR 07-13.) | 10-06 |
| **MMM, VRT, WAL** | Dates undated by company (VRT/RHI aggregator 10-28). | 10-07 |
| **LRCX, UAL** dates | Time locked; date 10-21 unsourced (UAL aggregator 10-20). | 10-07 |

### Notes
- **stocktitan needs the fuller UA** (`Chrome/126.0 Safari/537.36` + Accept + Accept-Language); the shorter `Chrome/120` string got 403 across the board. It then rate-limited (429 → "Too Many Requests" page, 200 status with a 2.5KB body) after ~3 fetches, so no spine data was obtained today; WebSearch surfaced the company PRs instead.
- WebSearch's "confirmed" labels from TipRanks/Nasdaq aggregators (LMT, UAL) were not used.
- direct_db_query writes print nothing; verified via SELECT.

---

## Session: 2026-10-01 (Thursday) — 07:19 AM ET

42 surfaced (36 `date_disagreement`/`both`, 6+ `unknown_time`/`unconfirmed`). **10 confirmed on company sources (ABT, ADC, WIT, AGNC, BX, BKR, CNP, CBRE, ARGX, PCG); 32 held.**
Stored dates changed: **none** — every confirmed date already matched the live calendar (stale snapshot again); CBRE/ARGX/PCG were time-only gains (Unknown → bmo).

### Confirmed

| Symbol | Result | Source |
|--------|--------|--------|
| **ABT** | 2026-10-21 `bmo` (DB 10-14 snapshot stale; finnhub+yfinance right) | abbott.mediaroom.com 09-30: *"Wednesday, Oct. 21, before the market opens,"* call 9am ET. |
| **ADC** | 2026-10-20 `amc` (finnhub 10-27 wrong) | Agree BusinessWire 09-30 16:05 ET: *"after the market closes on Tuesday, October 20, 2026,"* call 10-21 9am. |
| **WIT** | 2026-10-15 `bmo` (finnhub 10-13 wrong) | wipro.com/investors/events page: results *"October 15, 2026, Thursday after stock market trading hours in India"* (≈ US morning). |
| **AGNC** | 2026-10-19 `amc` (finnhub 10-26 wrong) | AGNC PR 09-30 (via stocktitan): *"after market close on October 19, 2026,"* call 10-20 8:30am ET. investors.agnc.com timed out on WebFetch. |
| **BX** | 2026-10-22 `bmo` (finnhub 10-15 wrong); bmo inferred | blackstone.com *"Blackstone Announces Third-Quarter 2026 Investor Call"*: call 10-22 9:00am ET. ⚠ page 403s WebFetch/curl — read via search snippet only; stocktitan spine had no such PR. |
| **BKR** | 2026-10-27 `amc` (yfinance right, finnhub 10-21 wrong) | GlobeNewswire 09-28 (marketscreener copy): *"press release at 5 p.m. Eastern Time on Tuesday, Oct. 27, 2026,"* webcast 10-28 9:30am. Cached URL was the Q2 PR — replaced with the Q3 event page. |
| **CNP** | 2026-10-27 `bmo` (yfinance+finnhub right) | GlobeNewswire 09-29: call 10-27 8am ET, *"released on the same day before the market opens."* |
| **CBRE** | 2026-10-22 `bmo` | ir.cbre.com detail/269 (09-28): *"approximately 6:55 a.m. Eastern time on Thursday, October 22, 2026,"* call 8:30am. Cached URL (detail/267) was the Q2 PR — replaced. |
| **ARGX** | 2026-10-22 `bmo` | argenx HY release (07-23) "Expected financial calendar": *"October 22, 2026: Third Quarter 2026 Financial Results and Business Update."* Time: argenx releases 07:00 CET ⇒ bmo. |
| **PCG** | 2026-10-22 `bmo` (time inferred) | investor.pgecorp.com PR 09-24: call 10-22 11:00am ET; release time not stated. EDGAR acceptance times 8/8 quarters 00:1x–01:57 on the release-day date ⇒ overnight/pre-market. |

### Held (no company source yet)

| Symbol | Why | Next check |
|--------|-----|------------|
| **LMT, PNR, EQT, CLF, GL, QS, RHI** | stocktitan spine (read 10-01) shows no Q3 advance PR; search finds only aggregator estimates. | 10-02 |
| **TER, VLTO, VRT, PEGA, MMM, BPOP, BYD, SF** | stocktitan 429'd the whole batch — spine unread; WebSearch finds nothing company-issued (TER/VRT hits were marketscreener-style estimates). | 10-02 (spine) |
| **AMX** | Event.svc (pageSize=100) newest event still 2Q26 (07-21 amc); no 3Q26. | 10-06 |
| **F, FCX, NSC, SLM, TRU, KBR, WAL** | no company Q3 date; only aggregator "estimated" dates (FCX 10-22, WAL 10-20). | 10-06 |
| **ALK** | No webcast PR yet (Q2's came ~07-08 for 07-22); Investor Day 09-29 only. | 10-06 |
| **POOL, WBS** | No Q3 PR. WBS: no call (pending Santander merger); Q2 was after close 07-21. | 10-06 |
| **AAL, DECK, BC, DOC, TSCO** | No company PR (DECK IR calendar: *"no upcoming events"*; DOC Q3-25 advance was 09-25-2025 so due any day). AAL/DECK 10-22 appear only on marketbeat. | 10-02 |
| **IRDM** | Calls suspended (pending Rocket Lab acquisition); no Q3 date. | 10-06 |

### Notes
- stocktitan JSON-LD now serialises without spaces (`"headline":"..."`) — the old regex in `reference_stocktitan_jsonld_discovery.md` needs `\s*`. It 429'd after 9 fetches at 9s spacing; the second batch got 429 on all 8 even after a pause.
- WebFetch on blackstone.com 403s; on investors.agnc.com times out.
- Helper at `inbox/fetch/conf.sh` (confirm + IR URL + dispute update in one call).
- direct_db_query writes print nothing; verified via SELECT.

---

## Session: 2026-10-02 (Friday) — 07:18 AM ET

34 surfaced (24 `date_disagreement`, 6 `both`, 4 `unknown_time`). **8 confirmed on company sources (CLF, LMT, AAL, BYD, TRU, HCA, BAH, DOC); 26 held.**
Stored dates changed: **none** — all 8 already matched the live calendar (stale snapshot again). Time gains: CLF amc→bmo (corrected), AAL/BAH/DOC Unknown→set.
Process slip: DOC's `research_url` was first written with a guessed BusinessWire path (not from any result); replaced the same minute with the financialcontent copy that search returned. Never construct a URL.

### Held (no company-issued Q3 source yet)

| Symbol | Why | Next check |
|--------|-----|------------|
| **AMX** | feed (pageSize=100) still has no 3Q26 event; newest is 2Q26 07-21 | 10-05 |
| **EQT, MMM, PNR, PEGA, GL, QS, RHI, SF, TER, VLTO** | stocktitan spine (10-02): no Q3 advance PR (only dividend PRs); search = aggregator estimates (MMM "10-20 9am" is marketbeat only) | 10-05 |
| **VRT, WAL, BPOP, F, FCX, NSC, SLM, ITW** | spine hit HTTP 429 (VRT onward); search shows only estimates (WAL "10-20 amc/10-21 call" and FCX 10-22 are aggregator) | 10-05, spine first |
| **ALK, POOL, WBS, IRDM** | IR pages show no Q3 date; IRDM/WBS have no calls (pending deals) so look for a PR only | 10-05 |
| **BC** | no Q3 date PR; Q2 reported **07-30**, so DB 10-22 is doubtful (likely later) | 10-05 |
| **DECK, TSCO** | IR calendar empty / no Q3 PR; marketbeat 10-22 only. TSCO Q2 PR came ~3wk ahead (07-02 for 07-23) so due now | 10-05 |

---

## Weekly Maintenance — 2026-09-27 (Sunday)

Third weekly pass in a row (Task Scheduler, 18:00, Opus). No mailbox notices. Found the 09-25 session
logged but **uncommitted**, with its header and cadence bookkeeping undone. Finished and committed both.

**Archived.** Sessions **09-08 (stub), 09-09, 09-10, 09-11** (216 lines) moved verbatim into the summer
archive ahead of the appendices; archive header range → 07-01 → 09-11. Script
`analysis/maintenance_archive_20260927.py` (backs up both files, asserts every moved non-blank line
landed; passed). Active log keeps 09-14 → 09-25. The 09-13 maintenance entry stays one more week.

**Header rebuilt from the DB.** Carry-overs: REXR, AMX, ACI, FNB, SNA, WIT, each with a new **"How to
read"** column that records the working channel and its known traps, so a session doesn't have to find
them in an older note. The ⚠⚠ "no session ran 09-16 → 09-18" banner is removed (fixed 09-24). Window
watch replaced with the **25 unconfirmed 10-13 → 10-17 rows** by horizon-entry day, plus the Monday caveat
(no unconfirmed row ≤ 10-12 ⇒ Monday spawns only on a dispute). Ledger: CTAS, GIS, PAYX, DRI pruned
(reported), sorted by date, **25 rows checked mechanically against `earnings_upcoming`: 0 mismatches.**

**Promoted / corrected.**
- `reference_q4_event_feed.md` — ⚠ **it was wrong**: it said `sortDirection=desc` works. 09-24 had found
  the feed ignores it and returns oldest first, but that correction only reached a session note and the
  AMX cadence row. The 09-25 read then used the cached URL (`pageSize=25`) verbatim, got 2014–2018, and
  logged "quirk?". Fixed the note, its MEMORY.md line, and the URL inside the AMX cadence row. The cached
  `symbol_metadata` URL still needs `pageSize=100`, which is a weekday DB write (STATUS item 3).
- `reference_company_cadence.md` — **RF** and **TFC** rows added (first-time names confirmed 09-25, never
  written); **DAL** closed out (10-09 bmo, feed move was right; PR date still uncaptured); **REXR** row
  flags the 09-25 bad read ("list ends 03-19" contradicts 09-24's "current to 09-17").
- `feedback_window_gating_and_noop.md` — spawn fix **verified in code** (`ei_lite_refresh.py:375–377`,
  `launcher.py:get_due_unconfirmed`, `inject_context.py:missed_session_warning`) + the residual gap (a
  next-check on a row >14d out with no dispute still spawns nothing) + the 25-row cap (nearest first, so
  overflow slips a day, not lost) + this week's lead-table score (below).
- `MEMORY.md` — Q4-feed and window-gating lines updated; all 21 pointers resolve (the 3 unindexed `for_*.md` are the known stray mailbox duplicates).

**`notes_for_ben.md`:** spawn-gate item → archive verbatim (new "Moved at the 2026-09-27 maintenance"
section) and a Resolved line saying it **hasn't been exercised yet** (every morning since 09-22 had
disputes). Re-seeding item condensed (9 of 10 rows fixed, MDT left, class still open). SNA item widened
to REXR ("two stored dates I believe are wrong"). New item on the first Sonnet session. HDB/IBN (Saturday
10-17) added to policy question 2.

**Inbox/outbox.** Inbox root clean. Outbox unchanged, largest file 128 lines, so no rotation.

**Calibration — week of 09-21 (4 of 5 sessions: 09-22 → 09-25; 09-21 didn't run under the old gate).**
- 21 unique symbols. **15 dates confirmed on company sources (71%)**, 3 time-only with dates held on
  purpose (ACI, FNB, SNA), 3 held (AMX, REXR, WIT). **0 wrong writes.** Stored values corrected: UEC
  date +5d and time, ACN time, STZ time; 9 `Unknown` times filled.
- **Skip judgment:** nothing gated reported or moved inside its skip. UEC's 09-17 check would correctly
  have found nothing (PR 09-22, exact 7d lead to the *true* date). CCL's 09-16 check would have found the
  09-15 PR, so that miss was machinery, not judgment.
- **Lead table:** stable-channel leads held to the day (ACN 16d, UEC 7d, CCL within 1d). **Both 1-obs
  leads borrowed from another fiscal quarter undershot**: PEP 35 → 44d, MU 28 → 35d. Their windows opened
  7–9 days early, and PEP's PR sat 30 days unread. No wrong date resulted (DB right both times). New
  working rule, n=2: start reading 1-obs rows at ~1.5× the lead.
- **finnhub:** 0 of 4 resolved dissents right (JBHT +5d, PGR +19d, SYF −7d, FHN +6d); yfinance right on
  SYF and FHN. The pattern holds.
- **Drift:** (1) **Lessons stranded in session notes.** The AMX sort fix is the second case after MTN/PEP
  (09-14 "read open windows the day they open" was not applied 09-15). A correction that lives only in a
  session block is invisible three days later. Rule for myself: when a session finds a channel quirk, it
  updates the memory note or the carry-over row's "How to read" cell **the same day**. (2) **09-25
  (first Sonnet session):** two bad reads logged as absences, and no bookkeeping. One session isn't a
  sample; I'll score 09-28 → 10-02 on the same points.

**STATUS.md** rewritten.

---

## Appendix A — Upcoming-Confirmed ledger rows pruned after reporting (verbatim)

_Pruned 2026-10-18: dates 10-13 → 10-16. Format `SYM | date | time | source — session`._

| Symbol | Date | Time | Source — session |
|--------|------|------|------------------|
| C | 2026-10-13 | bmo | Citi 2025 calendar PR (citigroup.com): *"3Q26 – Tuesday, October 13, 2026,"* release ~8am ET, webcast ~11am ET — 09-22 |
| DPZ | 2026-10-13 | bmo | Domino's PR 09-10 16:05 ET (stocktitan wire text; ir.dominos.com timed out): results 6:05am, webcast 8:30am ET — 09-29 |
| JNJ | 2026-10-13 | bmo | investor.jnj.com PR 08-31: release ~6:45am, call 8:30am ET Tue 10-13 — 09-29 |
| JPM | 2026-10-13 | bmo | jpmorganchase.com/ir PR 09-17: results ~7:00am, call 8:30am ET — 09-29 |
| UNH | 2026-10-13 | bmo | unitedhealthgroup.com PR 09-15: results before open, call 8:00am ET — 09-29 |
| WFC | 2026-10-13 | bmo | newsroom.wf.com *"Wells Fargo Updates 2026 Earnings Release Date Information"*: results ~7:00am, call 10am ET — 09-29 |
| ACI | 2026-10-13 | bmo | Albertsons PR 09-29, 14d lead (stocktitan wire text) — 10-05 |
| PGR | 2026-10-14 | bmo | Progressive August results release (8-K 7.01, 09-18): *"We plan to release September results on Wednesday, October 14, 2026, before the market opens"* — 09-23 |
| BAC | 2026-10-14 | bmo | BAC PR 09-30 (stocktitan wire text): release ~6:45am ET, call 8:30am. Closes the unsourced 06-30 lock question for Q3 — 10-06 |
| MS | 2026-10-14 | bmo | morganstanley.com/about-us-ir third-quarter-2026 call page (curl 200): release ~7:30am ET, call 9:30am — 10-06 |
| STT | 2026-10-14 | bmo | State Street PR 09-23 (stocktitan wire text): release ~7:30am ET, call 11:00am — 10-06 |
| FAST | 2026-10-14 | bmo | Fastenal PR 09-28 (stocktitan wire text): call Wed 10-14 9:00am CT. bmo **inferred** (release time not stated; DB bmo) — 10-06 |
| ASML | 2026-10-14 | bmo | ASML FY2025 20-F financial calendar (via search): Q3 results 10-14; bmo **inferred** from the usual 07:00 CET release — 10-12 |
| ERIC | 2026-10-15 | bmo | `ericsson.com/en/investors/financial-calendar/2026/q3-2026`: *"Oct 15, 2026 07:00 (CET)"* = 01:00 ET ⇒ bmo — 09-24 |
| FHN | 2026-10-15 | bmo | `ir.firsthorizon.com` PR 09-22: materials ~6:30am ET, call 9:30am ET. Snapshot 10-14 was already stale — 09-23 |
| JBHT | 2026-10-15 | amc | `investor.jbhunt.com` "Estimated Earnings Periods" table: Q3 release **October 15, 2026**, quiet period Sep 26 – Oct 15; amc = Item 2.02 furnished 20:08–21:26Z (16:0x–16:2x ET) 8/8 since 2024-10 — 09-24 |
| WIT | 2026-10-15 | bmo | wipro.com events page: *"Results for the Second quarter ending September 30, 2026, will be announced on October 15, 2026, Thursday after stock market trading hours in India"* (= US morning) — 10-01 |
| AA | 2026-10-15 | amc | q4cdn 3Q26-EarningsAnnouncement.pdf (PR 09-15): after NYSE close, call 5:00pm EDT — 10-06 |
| BK | 2026-10-15 | bmo | bny.com 2026 earnings-calls PR: release ~6:30am ET, call 11:00am — 10-06. ⚠ **No `earnings_upcoming` row exists** (dropped after 10-02); see notes_for_ben |
| MAN | 2026-10-15 | bmo | investor.manpowergroup.com *Announce 3rd Quarter 2026 Earnings Results*: before the open — 10-06 |
| MRSH | 2026-10-15 | bmo | marsh.com PR 09-17: before the open, call 8:30am EDT — 10-06 |
| PLD | 2026-10-15 | bmo | Prologis PR 09-03 (finviz copy): call 9am PT/12pm ET. bmo **inferred** (release time not stated; DB bmo) — 10-06 |
| PNC | 2026-10-15 | bmo | PNC PR 09-03 (stocktitan wire text): release ~6:30am ET, call 10:00am — 10-06 |
| SCHW | 2026-10-15 | bmo | ⚠ **Inferred**: Schwab *Fall Business Update* PR 09-17 (Thu 10-15 8:30am ET); it doesn't mention earnings. Earnings rode the update in 3/3 (Q3'25, Q1'26, Q2'26) — 10-06 |
| TSM | 2026-10-15 | bmo | investor.tsmc.com: call Thu 10-15 14:00 Taiwan = 02:00 ET, so results precede the US open. **Time corrected from amc** — 10-06 |
| USB | 2026-10-15 | bmo | q4cdn USB PR (10-01): before the open, call 8am CT — 10-06 |
| RF | 2026-10-16 | bmo | ir.regions.com 2026 release-dates PR: *"pre-market open on Friday, Oct. 16, 2026,"* call 10am ET — 09-25 |
| TFC | 2026-10-16 | bmo | media.truist.com 09-18: *"before the market opens on Friday, Oct. 16, 2026,"* call 8am ET — 09-25 |
| CFG | 2026-10-16 | bmo | CFG PR (finviz copy): call 9:00am ET — 10-06 |
| MTB | 2026-10-16 | bmo | M&T PR 09-18 (finviz copy): before the open Fri 10-16, call 8:00am ET — 10-06 |
| TRV | 2026-10-16 | bmo | investor.travelers.com *Schedules Conference Call … Q3 2026*: release before the 9:00am ET call — 10-06 |
