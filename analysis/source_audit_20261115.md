# Source-accuracy audit #6: 2026-11-15 (closing the October census)

**Question:** of the confirms whose dates have passed, did the date and time turn out right, by source type?

**Result: 40 of 40 drawn rows right on date and time, 0 unverifiable. The other 47 pool rows, screened on EDGAR: 47 of 47
dates right, no time contradicted. With audits #3 → #5, every October-wave confirm (213 rows) has now been checked
once: 1 miss (JBLU, time and date), 1 unverifiable time (C).**

Session dated 2026-11-15 (Sunday); the window stayed open and the work finished 11-18. Nothing in it depends on that.

## Pool and draw

- **No new passed confirms:** no weekday session has run since 10-19 (Simple Mode; still skipping Phase 1 through 11-18).
  Following the prompt ("widen only if too small"), the pool is **every passed confirm no earlier audit checked**:
  Appendix A ledger rows 10-13 → 11-05 minus the 127 symbols in audits #3–#5 (SCHW, hand-added to #3, excluded by hand).
  **87 rows: PR copy 70, IR / newsroom direct 17.** Search summary, inferred, aggregator, feed agreement: 0 left.
  Matches the 129 − 42 = 87 expected from 11-08. Script: `analysis/audit_pool_20261115.py` (draw saved in `.json`).
- **Draw:** IR as a census (17), copy 23 of 70 by `random.seed(20261115)`. 40 rows, shuffled, 5 batches of 8.
- **Lookups:** 5 general-purpose subagents, blind to source type and to what I expected. Rules: Item 2.02 8-K or results
  6-K, ET Accepted time from the EDGAR index page, Ex-99.1 dateline and wording; no aggregator past-results pages;
  release wins over filing time; unverifiable when no primary record.
- **The 47 not drawn:** mechanical EDGAR screen (`analysis/edgar_screen_confirmed.py` →
  `edgar_screen_confirmed_20261115.tsv`). 45 ok; 2 flagged (STLD, TER), both next-morning filers, which I resolved by
  reading the Item 2.02 sentence and Ex-99.1 myself (below). This is a filing-date screen, coarser than the subagent
  check on timing: for the 45 "ok" rows the session is read from the filing time only.
- **Re-check:** the subagents reported 0 mismatches, so there was nothing to re-check. I re-read both screen flags.

## Accuracy by source type (subagent sample)

| Source type | n checked | date matched | date wrong | time wrong | unverifiable |
|---|---|---|---|---|---|
| Company IR / newsroom page | 17 (census) | 17 | 0 | 0 | 0 |
| PR read as a copy | 23 | 23 | 0 | 0 | 0 |
| Search summary of company text | 0 (none left) | — | — | — | — |
| Aggregator / calendar site | 0 (none in pool) | — | — | — | — |
| yfinance/finnhub agreement | 0 (none in pool) | — | — | — | — |
| Time inferred, date sourced | 0 (none left) | — | — | — | — |

Plus the EDGAR screen of the remaining 47 copy rows: 47/47 dates, 0 sessions contradicted (STLD and TER resolved below).

**October-wave totals, audits #3 → #6 (summed from each report's own table):**

| Source type | n checked | date right | time right | unverifiable |
|---|---|---|---|---|
| IR / newsroom direct | 46 (10 + 7 + 12 + 17) | 46 | 45 | 1 (C, time) |
| PR copy | 67 by subagent (10 + 12 + 22 + 23) + 47 screened | 114 | 114 | 0 |
| Search summary | 21 (11 + 10) | 21 | 21 | 0 |
| Time inferred, date sourced | 34 (13 + 13 + 8) | 33 | 33 | 0 (JBLU missed both) |

215 report rows in all. Every one of the 214 distinct ledger rows dated 10-13 → 11-05 is covered (127 symbols in audits #3–#5
plus this pool of 87). The extra report row is one symbol counted twice or dated outside the window. I haven't traced which.
Only one date was wrong (JBLU).

## Results by symbol (subagent sample)

Accepted times are ET from EDGAR index pages.

| SYM | Source type | Recorded | Actual | Source of the actual | Verdict |
|---|---|---|---|---|---|
| AA | IR | 10-15 amc | 10-15 by 16:14 | 8-K 0001193125-26-422891; slides ~4:15pm, call 5pm EDT 10-15 | match |
| ADC | copy | 10-20 amc | 10-20 by 16:05 | 8-K 0000917251-26-000075; "today announced", call 10-21 9am | match |
| AGNC | copy | 10-19 amc | 10-19 by 16:03 | 8-K 0001423689-26-000144; call 10-20 8:30am | match |
| ARGX | IR | 10-22 bmo | 10-22 07:00 CET (01:00 ET) | 6-K 0001697862-26-000034 (acc. 08:20); release states its own time | match |
| BK | IR | 10-15 bmo | 10-15 by 06:30 | 8-K 0001390777-26-000104 (EDGAR ticker **BNY**); materials ~6:30am | match |
| BPOP | copy | 10-22 bmo | 10-22 by 07:00 | 8-K 0000763901-26-000022; call "today" 11am | match |
| CB | copy | 10-20 amc | 10-20 by 17:24 | 8-K 0001193125-26-426866; "today reported", call 10-21 | match (acc. 6 min before the 17:30 cutoff) |
| CCI | copy | 10-21 amc | 10-21 by 16:17 | 8-K 0001051470-26-000085; call 4:45pm 10-21 (8-K/A 11-04 doesn't move it) | match |
| CZR | copy | 10-27 amc | 10-27 by 16:12 | 8-K 0001590895-26-000032; no call (pending Fertitta deal) | match |
| EFX | copy | 10-20 bmo | 10-20 by 06:31 | 8-K 0000033185-26-000037; call 8:30am | match |
| EWBC | IR | 10-20 amc | 10-20 by 16:04 | 8-K 0001069157-26-000048; call 5pm ET 10-20 | match |
| FE | copy | 10-27 amc | 10-27 by 16:31 | 8-K 0001031296-26-000142; webcast "tomorrow, Oct. 28" | match |
| HUBB | copy | 10-27 bmo | 10-27 by 08:05 | 8-K 0001628280-26-067421; call "today" 10am | match |
| KEY | IR | 10-20 bmo | 10-20 by 06:30 | 8-K 0000091576-26-000020; dateline 10-20 | match |
| KNX | copy | 10-21 amc | 10-21 by 16:06 | 8-K 0001492691-26-000065; call 5:30pm 10-21 | match |
| MAN | IR | 10-15 bmo | 10-15 by 07:41 | 8-K 0001193125-26-422291; call 8:30am ET | match |
| MTB | copy | 10-16 bmo | 10-16 by 06:02 | 8-K 0000036270-26-000057; call "today" 8am | match |
| NDAQ | copy | 10-22 bmo | 10-22 by 07:26 | 8-K 0001120193-26-000017; "today reported" | match |
| NOV | copy | 10-27 amc | 10-27 (release) | 8-K 0001193125-26-435237, acc. **10-28 09:00** (next-morning filer); Item 2.02 "On October 27", call 10-28 | match (amc implied, not stamped) |
| OMC | copy | 10-22 amc | 10-22 by 16:06 | 8-K 0000029989-26-000024; call 4:30pm | match |
| PEGA | copy | 10-20 amc | 10-20 by 16:12 | 8-K 0001013857-26-000057; call 10-21 8am | match |
| PSA | copy | 10-26 amc | 10-26 by 16:11 | 8-K 0001628280-26-067283; call 10-27 | match |
| REXR | IR | 10-22 amc | 10-22 by 16:28 | 8-K 0001571283-26-000058; call 10-23 | match |
| RHI | IR | 10-22 amc | 10-22 by 16:05 | 8-K 0000315213-26-000049; call 5pm | match |
| RNG | copy | 10-22 amc | 10-22 by 16:50 | 8-K 0001384905-26-000058; call 5pm ET | match |
| ROL | copy | 10-21 amc | 10-21 by 16:07 | 8-K 0000084839-26-000042; call 10-22 8:30am | match |
| RTX | IR | 10-20 bmo | 10-20 by 06:57 | 8-K 0000101829-26-000030; call 8:30am | match |
| SNA | copy | 10-22 bmo | 10-22 by 06:33 | 8-K 0000091440-26-000169; webcast 9am CT | match |
| SPCX | IR | 10-20 amc | 10-20 by 16:00 | 8-K 0001628280-26-066482 (CIK 1181412); webcast 4:30pm ET | match |
| SYF | IR | 10-20 bmo | 10-20 by 06:00 | 8-K 0001601712-26-000040; call 8am | match |
| TRV | IR | 10-16 bmo | 10-16 by 06:58 | 8-K 0000086312-26-000180; webcast 9am | match |
| TSCO | copy | 10-22 bmo | 10-22 by 07:26 | 8-K 0000916365-26-000069; call "today" 10am | match |
| UAL | copy | 10-20 amc | 10-20 by 16:00 | 8-K 0000100517-26-000184; call 10-21 10:30am | match |
| WAL | copy | 10-19 amc | 10-19 by 16:19 | 8-K 0001628280-26-066286; call 10-20 noon | match |
| WFC | IR | 10-13 bmo | 10-13 by 06:28 | 8-K 0000072971-26-000318; call 10am | match |
| WH | IR | 10-21 amc | 10-21 by 16:31 | 8-K 0001722684-26-000081; call 10-22 8:30am | match |
| WIT | IR | 10-15 bmo | 10-15, 06:10–09:30 ET | 6-Ks acc. **10-20** (5 days late); board concluded 15:40 IST = 06:10 ET; call 9:30am ET "today" | match |
| WRB | IR | 10-19 amc | 10-19 by 16:12 | 8-K 0000011544-26-000046; call 5pm | match |
| XYL | copy | 10-27 bmo | 10-27 by 07:01 | 8-K 0001524472-26-000146; "today reported" | match |
| ZION | IR | 10-19 amc | 10-19 by 16:06 | 8-K 0000109380-26-000125; call 5:30pm | match |

**Screen flags resolved by me:** STLD (ledger 10-19 amc): 8-K acc. 10-20 09:30, Item 2.02 "On October 19, 2026 … issued a
press release", call Tue 10-20 11am: **match**, next-morning filer. TER (ledger 10-27 amc): 8-K acc. 10-28 06:00, Item 2.02
"On October 27, 2026", call 10-28 8:30am: **match**, next-morning filer.

## Misses

None. No cadence or ledger row needed correcting. Rows annotated with filing quirks the audit surfaced: NOV, STLD, TER
(next-morning filers), WIT (6-K ~5 days late), BK (EDGAR ticker BNY), CB (8-K near the 17:30 cutoff), CZR (pending deal).

## Reading

- The October wave is now closed out: every confirm has been checked once. The only date miss was JBLU, a call-time
  inference. The direct-source types (IR page, PR copy) had no date misses in 160 checks, and in that same group
  the only time I couldn't verify was C (46 IR + 114 copy). That describes this wave's mostly large-cap, habit-bound names. It is not a
  general ranking of sources.
- A seventh audit has no new rows to draw: the pool is empty until weekday confirms resume.
- **Method lesson:** 4 of the 6 date flags across both of today's screens (STLD, TER, CTVA, TTEK) were next-morning
  filers. `edgar_screen.py` now reads the Item 2.02 sentence when a date disagrees and re-dates the row to the stated day.
