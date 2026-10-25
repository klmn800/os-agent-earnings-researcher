# Source-accuracy audit #3: 2026-10-25 (October confirms, forward)

**Question:** of the confirms whose dates have now passed (October 13 → 23), did the date and time turn out right, and
does that differ by the kind of source the confirm rested on?

## Pool and draw

- **Pool:** every ledger row dated 10-13 → 10-23: 31 rows pruned 10-18 plus 103 pruned today, so 134 rows (both sets are in
  the fall archive's Appendix A).
- **Source types in the pool:**
  - company IR / newsroom page fetched directly: 36
  - PR read as a copy (stocktitan, finviz, financialcontent, biopharmawatch, Yahoo, GNW/BW text): 66
  - company statement seen only through a search summary or snippet: 11 (five of them also have an inferred time: ASML, BX,
    GM, NOK, E)
  - time inferred from a call time, a home-market clock or filing history, with the date from IR or a copy: 21
  - aggregator or calendar site: **0**
  - yfinance/finnhub agreement: **0**

  The no-lock-without-a-company-source policy has held since July, so the last two types never occur in October.
- **Draw:** stratified, random within each stratum (Python `random.seed(20261025)`). Search summary: census, 11. Inferred:
  12 of 21. IR direct: 10 of 36. Copy: 10 of 66. That makes 43. I added **SCHW** by hand (inferred, not drawn) because
  `notes_for_ben` had promised this audit would score it, which makes 44.
- **Lookups:** 5 general-purpose subagents, 8 or 9 symbols each, shuffled across strata (same seed). Blind briefs: symbol,
  recorded date and time, and the rules. They were not told the source type or what I expected. I checked SCHW myself.
- **Rules:** independent primary evidence only. That means the Item 2.02 8-K or results 6-K with the ET `Accepted` time
  from the EDGAR index page, or the dated release or newsroom page with its timestamp. No aggregator past-results pages.
  bmo = before 09:30 ET, amc = at or after 16:00 ET. Where the release dateline and the filing time disagree, the release
  wins.
- **Re-check:** there were 0 mismatches, so nothing needed re-checking. I read the subagents' three flagged edge cases
  (PCG, DHR, AMX) and agree with their calls (see below).

## Results by symbol

| SYM | Source type | Recorded | Actual | Source of the actual | Verdict |
|---|---|---|---|---|---|
| AMX | search summary | 10-20 amc | 10-20 amc | q4cdn 3Q26.pdf Last-Modified 10-20 18:19 ET; call 10-21 9am MX (6-K filed late, 10-22 16:02) | match (weak: file timestamp) |
| ASML | search summary (+ time inferred) | 10-14 bmo | 10-14 bmo | 6-K 0001628280-26-065813, acc. 10-14 06:01 | match |
| BX | search summary (+ time inferred) | 10-22 bmo | 10-22 bmo | 8-K 0001193125-26-428297, acc. 10-22 06:55 | match |
| CMCSA | search summary | 10-22 bmo | 10-22 bmo | 8-K 0001628280-26-066783, acc. 10-22 07:05 | match |
| CME | search summary | 10-21 bmo | 10-21 bmo | 8-K 0001156375-26-000065, acc. 10-21 07:13 | match |
| E | search summary (+ time inferred) | 10-23 bmo | 10-23 bmo | eni.com newsroom, 10-23 07:29 CEST (01:29 ET); no results 6-K yet | match |
| GM | search summary (+ time inferred) | 10-20 bmo | 10-20 bmo | 8-K 0001467858-26-000056, acc. 07:30; Ex-99.1 "For Release … 6:30 a.m. ET" | match |
| MSCI | search summary | 10-20 bmo | 10-20 bmo | 8-K 0001408198-26-000054, acc. 06:46 | match |
| NOK | search summary (+ time inferred) | 10-22 bmo | 10-22 bmo | 6-K 0001104659-26-117972, acc. 07:51; release 08:00 EEST | match |
| PHM | search summary | 10-22 bmo | 10-22 bmo | 8-K 0000822416-26-000041, acc. 07:28 | match |
| SAP | search summary | 10-21 amc | 10-21 amc | news.sap.com release, published 20:07Z = 16:07 ET (no 6-K yet) | match |
| DECK | time inferred (call) | 10-22 amc | 10-22 amc | 8-K 0000910521-26-000028, acc. 16:09; call "today 4:30pm" | match |
| GE | time inferred (call) | 10-20 bmo | 10-20 bmo | 8-K 0000040545-26-000063, acc. 06:30 | match |
| GPC | time inferred (filing history) | 10-20 bmo | 10-20 bmo | 8-K 0000040987-26-000037, acc. 07:47 | match |
| HAL | time inferred (call) | 10-20 bmo | 10-20 bmo | 8-K 0000045012-26-000070, acc. 06:50 | match |
| JBHT | time from filing history | 10-15 amc | 10-15 amc | 8-K 0001437749-26-032715, acc. 16:23 | match |
| LAZ | time inferred ("Thursday morning") | 10-22 bmo | 10-22 bmo | 8-K 0001628280-26-066781, acc. 06:31 | match |
| LMT | time inferred (call) | 10-22 bmo | 10-22 bmo | 8-K 0001628280-26-066780, acc. 06:26 | match |
| PCG | time inferred (filing history) | 10-22 bmo | 10-22 bmo | 8-K 0001004980-26-000056, acc. **10-21 21:04**, EDGAR filing date 10-22; release dated 10-22 | match (see note) |
| PG | time inferred (call) | 10-22 bmo | 10-22 bmo | 8-K 0000080424-26-000250, acc. 07:02 | match |
| PLD | time inferred (call) | 10-15 bmo | 10-15 bmo | 8-K 0001193125-26-422375, acc. 09:18 | match |
| TSM | time inferred (home clock) | 10-15 bmo | 10-15 bmo | 6-K 0001046179-26-000726, acc. 06:40 | match |
| VLO | time inferred (prior quarters) | 10-22 bmo | 10-22 bmo | 8-K 0001628280-26-066795, acc. 08:20 | match |
| SCHW *(added)* | time inferred (Business Update day) | 10-15 bmo | 10-15 bmo | BW release 10-15 7:30am (finviz copy), update 8:30am ET; 8-K 0000316709-26-000035 acc. 16:18 is Schwab's habitual late filing (10/10 quarters ~16:17) | match |
| BYD | IR direct | 10-22 amc | 10-22 amc | 8-K 0001437749-26-033268, acc. 16:06 | match |
| CBRE | IR direct | 10-22 bmo | 10-22 bmo | 8-K 0001138118-26-000028, acc. 07:03 | match |
| FHN | IR direct | 10-15 bmo | 10-15 bmo | 8-K 0000036966-26-000178, acc. 07:31 | match |
| JNJ | IR direct | 10-13 bmo | 10-13 bmo | 8-K 0000200406-26-000189, acc. 08:12 | match |
| JPM | IR direct | 10-13 bmo | 10-13 bmo | 8-K 0001628280-26-065582, acc. 06:30 | match |
| MRSH | IR direct | 10-15 bmo | 10-15 bmo | 8-K 0000062709-26-000256, acc. 08:05 | match |
| MS | IR direct | 10-14 bmo | 10-14 bmo | 8-K 0000895421-26-000288, acc. 07:39 | match |
| PGR | IR direct (8-K 7.01) | 10-14 bmo | 10-14 bmo | 8-K 0000080661-26-000367, acc. 09:00 | match |
| RF | IR direct | 10-16 bmo | 10-16 bmo | 8-K 0001281761-26-000063, acc. 06:01 | match |
| UNH | IR direct | 10-13 bmo | 10-13 bmo | 8-K 0000731766-26-000255, acc. 06:14 | match |
| ALK | PR copy (stocktitan) | 10-20 amc | 10-20 amc | 8-K 0000766421-26-000046, acc. 17:09 | match |
| AXP | PR copy (stocktitan) | 10-23 bmo | 10-23 bmo | 8-K 0000004962-26-000405, acc. 07:00 | match |
| BAC | PR copy (stocktitan) | 10-14 bmo | 10-14 bmo | 8-K 0000070858-26-000481, acc. 06:44 | match |
| CFG | PR copy (finviz) | 10-16 bmo | 10-16 bmo | 8-K 0000759944-26-000206, acc. 06:34 | match |
| COF | PR copy (stocktitan) | 10-20 amc | 10-20 amc | 8-K 0000927628-26-000142, acc. 16:05 | match |
| DHR | PR copy (finviz) | 10-21 bmo | 10-21 bmo | 8-K 0000313616-26-000201, acc. **10-20 17:43**, filing date 10-21; release dated 10-21, call "today 8am" | match (see note) |
| FAF | PR copy (stocktitan) | 10-21 amc | 10-21 amc | 8-K 0001193125-26-427848, acc. 16:15 | match |
| MOH | PR copy (biopharmawatch) | 10-21 amc | 10-21 amc | 8-K 0001179929-26-000042, acc. 16:18 | match |
| NLY | PR copy (financialcontent) | 10-20 amc | 10-20 amc | 8-K 0001043219-26-000077, acc. 16:15 | match |
| SF | PR copy (stocktitan) | 10-21 bmo | 10-21 bmo | 8-K 0001193125-26-427189, acc. 07:00 | match |

## Accuracy by source type

| Source type | n checked | date matched | date wrong | time wrong | unverifiable |
|---|---|---|---|---|---|
| Company IR / newsroom page | 10 | 10 | 0 | 0 | 0 |
| PR read as a copy | 10 | 10 | 0 | 0 | 0 |
| Search summary or snippet only | 11 | 11 | 0 | 0 | 0 |
| Time inferred, date sourced | 13 (12 + SCHW) | 13 | 0 | 0 | 0 |
| Aggregator / calendar | 0 | — | — | — | — |
| yfinance/finnhub agreement | 0 | — | — | — | — |
| **Total** | **44** | **44** | **0** | **0** | **0** |

Five of the search-summary rows also carried an inferred time (all foreign, or GM/BX), and all five held.

## Reading it (and what not to read into it)

- **No misses in 44.** The samples per type are 10 to 13. "0 of 11" for search summaries rules out a high miss rate. It
  does not show that the rate is 0.
- **The weak types held in October, unlike in the summer.** Summer call-time inferences were 9/12 on time (audit #2).
  October's 13 were 13/13. The likely reason is rule 6 (10-18): no October inference rested on a bare morning call
  without a check of the prior quarter's 8-K or dateline. That is plausible but not tested. October is also mostly
  large caps with fixed habits.
- **Search summaries held 11/11.** In every case the summary was of the company's own text (a PR, an IR page or a
  financial calendar), never an aggregator's estimate. That distinction is what matters, and it is the one the weekday
  prompt already draws.
- **Nothing to flag as a repeat-miss source type**, so there is no `analysis/` write-up of a failing type this week.

## Evidence notes worth keeping

- **Evening-before 8-K filers (PCG, DHR):** acceptance after 17:30 ET on D−1, EDGAR filing date D, release dated D with a
  same-morning call, so these are D bmo. Rule: the acceptance time is a latest-possible bound only on the filing date
  EDGAR assigns. Read the filing date and the dateline, not just the `Accepted` clock. (Added to the cadence table.)
- **Late filers (SCHW ~16:17 every quarter; AMX's 6-K 2 days late):** the 8-K time says nothing about the release time.
- **Weakest evidence in the match column:** AMX (CDN file Last-Modified, no wire timestamp), SAP and E (newsroom publish
  time, no 6-K yet). All three are primary but single-source.

## Bonus: what the parked rows did while no session ran (10-20 → 10-23)

These were not in the audit sample. They score the carry-over judgment (step 6). Checked on EDGAR by me.

| SYM | DB row | Actual | Evidence | Note |
|---|---|---|---|---|
| ISRG | 10-20 amc | 10-20 amc | 8-K acc. 10-20 16:05 | DB held. My "no PR 1 day out is suspect" doubt was **wrong** |
| DOW | 10-22 bmo | 10-22 bmo | 8-K acc. 10-22 06:57 | DB held |
| IRDM | 10-22 Unknown | **10-20 bmo** | 8-K acc. 10-20 07:01 | DB **2 days late**. No call, so no advance PR, as predicted |
| SCCO | 10-22 Unknown | **10-20** (amc likely) | Ex-99.1 dated 10-20; 8-K acc. 10-21 09:20; call 10-22 11am | DB had the **call date**, 2 days late |
| INFY | 10-23 amc | 10-23, time unverified | 6-K acc. 10-23 11:45 (after the open) | Date held. My bmo prediction is unscored |
| HDB | 10-17 bmo (Sat) | consistent with 10-19 bmo | 6-Ks acc. 10-19 07:49 (contents not opened) | Ben's 10-19 rule would have written 10-19 bmo |
| IBN | 10-17 amc (Sat) | not checked | — | — |

Overdue-PR doubts now stand at **3 right, 4 wrong** (ISRG added to the wrong side).
