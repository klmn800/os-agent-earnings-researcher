# Source-accuracy audit #5: 2026-11-08 (the last fall confirms, plus earlier rows no draw had picked)

**Question:** of the confirms whose dates have passed, did the date and time turn out right, by source type?

**Result: 42 of 42 right on the date. 41 of 42 right on the time, 0 wrong, 1 unverifiable (C). No misses.**

## Pool and draw

- **Why the pool was widened:** only 5 confirms had newly passed (DOC, KHC, NVST, MAT, KMB, 11-02 → 11-05), since no weekday
  session has run since 10-19. Following the prompt ("widen only if too small"), the pool is **every passed confirm that no
  earlier audit checked**: the 5 new rows plus what audits #3 and #4 didn't draw from 10-13 → 10-30. That's 129 rows.
- **Strata, tagged from the ledger source text:** PR copy 92 (KNX retagged from "search": its source is a finviz copy of the
  BW release), IR / newsroom direct 29, time inferred 8. Search summary 0 (audits #3 and #4 took censuses of it). Aggregator
  and feed agreement 0 (policy since July).
- **Draw:** the 5 new rows forced in. Census of inferred (8). IR 12 of 29, copy 22 of 92, by `random.seed(20261108)`.
  That makes 42.
- **Lookups:** 5 general-purpose subagents, shuffled across strata (same seed), blind to source type and to what I expected.
- **Rules:** Item 2.02 8-K or results 6-K with the ET Accepted time from the EDGAR index page, plus the Ex-99.1 dateline and
  wording. No aggregator past-results pages. bmo = before 09:30 ET, amc = at or after 16:00 ET. The release wins over the
  filing time.
- **Re-check:** 0 mismatches, so nothing needed re-checking. One unverifiable time (C), explained below.

## Accuracy by source type

| Source type | n checked | date matched | date wrong | time wrong | unverifiable |
|---|---|---|---|---|---|
| Company IR / newsroom page | 12 | 12 | 0 | 0 | 1 (time, C) |
| PR read as a copy | 22 | 22 | 0 | 0 | 0 |
| Search summary of company text | 0 | — | — | — | — |
| Aggregator / calendar site | 0 | — | — | — | — |
| yfinance/finnhub agreement | 0 | — | — | — | — |
| Time inferred, date sourced | 8 | 8 | 0 | 0 | 0 |

Every n is small. Inferred is a census of what was left (8 rows), IR and copy are samples. This doesn't rank the types.
Running count for inferred times across audits #3 → #5 (October onward): 13/13, 12/13, 8/8. The summer's call-time-only
group was 9/12. The groups differ, so I'm not adding them up.

## Results by symbol

Accepted times are ET from EDGAR index pages. "by" = upper bound from the filing.

| SYM | Source type | Recorded | Actual | Source of the actual | Verdict |
|---|---|---|---|---|---|
| AAL | inferred | 10-22 bmo | 10-22 by 07:00 | 8-K 0000006201-26-000064; "FOR RELEASE: Thursday, Oct. 22", call 7:30am CT today | match |
| FAST | inferred | 10-14 bmo | 10-14 by 07:56 | 8-K 0000815556-26-000046; "today reported", call today 9am CT | match |
| IBM | inferred | 10-21 amc | 10-21 by 16:19 | 8-K 0000051143-26-000093; call 5pm ET today | match |
| LRCX | inferred | 10-21 amc | 10-21 by 16:13 | 8-K 0000707549-26-000052; dateline 10-21, "today announced" | match |
| MMM | inferred | 10-20 bmo | 10-20 by 06:35 | 8-K 0000066740-26-000308; call 9am ET today | match |
| NSC | inferred | 10-22 bmo | 10-22 by 08:20 | 8-K 0001193125-26-428384; dateline 10-22 | match |
| NVST | inferred | 11-04 amc | 11-04 by 16:14 | 8-K 0001757073-26-000085; dateline Nov 4 PRN, call 2pm PT | match |
| ORI | inferred | 10-22 bmo | 10-22 by 08:49 | 8-K 0000074260-26-000100; dateline 10-22, call 3pm ET today | match |
| ABT | IR | 10-21 bmo | 10-21 by 07:36 | 8-K 0001628280-26-066601; call 8am CT today | match |
| BAH | IR | 10-23 bmo | 10-23 by 06:48 | 8-K 0001628280-26-066971; dateline 10-23 | match |
| C | IR | 10-13 bmo | 10-13, session not proven | 8-K 0001104659-26-115323, acc. **10:09**; "today reported", call 11am ET | **date match, time unverifiable** |
| CCK | IR | 10-19 amc | 10-19 by 16:08 | 8-K 0001628280-26-066281; call "tomorrow, October 20" | match |
| CLF | IR | 10-19 bmo | 10-19 by 06:52 | 8-K 0000764065-26-000112; call "this morning" 8:30am | match |
| ERIC | IR | 10-15 bmo | 10-15, before 03:00 ET | 6-K 0001628280-26-065962 (acc. 11:10, late filer); webcast 09:00 CEST | match |
| FITB | IR | 10-19 bmo | 10-19 by 06:30 | 8-K 0000035527-26-000229; call 9am ET today | match |
| FNB | IR | 10-19 amc | 10-19 amc | 8-K 0000037808-26-000027, acc. **10-20 07:30** (next-morning filer); Ex-99.1 "after the market close on Monday, October 19" | match |
| JBHT | IR | 10-15 amc | 10-15 by 16:23 | 8-K 0001437749-26-032715; call 4pm CDT today | match |
| KMB | IR | 11-05 bmo | 11-05 by 06:33 | 8-K 0001628280-26-070514; "today reported", ~6:30am | match |
| TFC | IR | 10-16 bmo | 10-16 by 06:31 | 8-K 0000092230-26-000108; call 8am ET today | match |
| USB | IR | 10-15 bmo | 10-15 by 06:59 | 8-K 0000036104-26-000054; call 10-15 8am | match |
| ACI | copy | 10-13 bmo | 10-13 by 07:31 | 8-K 0001646972-26-000059; call today 8:30am | match |
| ALLY | copy | 10-20 bmo | 10-20 by 07:20 | 8-K 0001193125-26-425698; Ex-99.2 dated 10-20 | match |
| CNP | copy | 10-27 bmo | 10-27 by 06:15 | 8-K 0001104659-26-118963 | match |
| DOC | copy | 11-02 amc | 11-02 by 16:10 | 8-K 0001628280-26-068878; call Tue Nov 3 | match |
| DPZ | copy | 10-13 bmo | 10-13 by 06:05 | 8-K 0001286681-26-000039 | match |
| DXCM | copy | 10-29 amc | 10-29 by 16:03 | 8-K 0001093557-26-000193; call 4:30pm ET today | match |
| EQT | copy | 10-27 amc | 10-27 by 16:31 | 8-K 0000033213-26-000054 (10-13 off-cycle 2.02 skipped) | match |
| EXR | copy | 10-27 amc | 10-27 by 16:17 | 8-K 0001289490-26-000061; call Wed 10-28 | match |
| GILD | copy | 10-29 amc | 10-29 by 16:03 | 8-K 0000882095-26-000037; call 1:30pm PT today | match |
| GNTX | copy | 10-23 bmo | 10-23 by 08:00 | 8-K 0000355811-26-000060 | match |
| HBAN | copy | 10-22 bmo | 10-22 by 06:19 | 8-K 0000049196-26-000084 | match |
| KHC | copy | 11-04 bmo | 11-04 by 07:00 | 8-K 0001637459-26-000078; Q&A 9am today | match |
| MAT | copy | 11-05 amc | 11-05 by 16:18 | 8-K 0000063276-26-000014; call 5pm ET today | match |
| MDLZ | copy | 10-29 amc | 10-29 by 16:09 | 8-K 0001628280-26-068233; call 5pm ET today | match |
| PKG | copy | 10-21 amc | 10-21 amc | 8-K 0001193125-26-428056, acc. 18:07 (filing date 10-22); call Thu 10-22 | match |
| PNR | copy | 10-27 bmo | 10-27 by 06:51 | 8-K 0000077360-26-000055 | match |
| RITM | copy | 10-23 bmo | 10-23 by 07:24 | 8-K 0001556593-26-000033 | match |
| SPOT | copy | 10-22 bmo | 10-22 by 06:03 | 6-K 0001140361-26-040435; Q&A 8am ET today | match |
| TMO | copy | 10-21 bmo | 10-21 by 06:03 | 8-K 0000097745-26-000173 | match |
| VRSN | copy | 10-22 amc | 10-22 by 16:06 | 8-K 0001014473-26-000038; call 4:30pm today | match |
| WDC | copy | 10-22 amc | 10-22 by 16:04 | 8-K 0001628280-26-066882; call 1:30pm PT today | match |
| WELL | copy | 10-26 amc | 10-26 by 16:33 | 8-K 0000766704-26-000043; call Tue 10-27 | match |

## The unverifiable row

- **C (Citi):** recorded bmo from Citi's own calendar PR ("release ~8am ET, webcast ~11am"). The 8-K was accepted at 10:09,
  after the open, and the release text says only "today". So no primary record proves the release came before 09:30. It is
  likely right, but I'm leaving it unverifiable, per the rule. Noted in Citi's cadence row: its 8-K doesn't time its release.

## Edge cases the subagents handled (I agree with each)

- **FNB** filed the morning after an evening release (07:30 next day); the Ex-99.1 says "after the market close on Monday,
  October 19". Same shape as RRC/UGI.
- **PKG** filed at 18:07, so the filing date is 10-22, but the release is dated 10-21 with the call "Thursday, October 22". That's
  10-21 amc, the reverse of the PCG/DHR evening-before shape.
- **ERIC** filed its 6-K at 11:10 ET. The webcast was 09:00 CEST (03:00 ET), so the report came out before US hours. Under Ben's
  rule that's bmo.

## What this does and doesn't say

- Across audits #3 → #5, 130 October-wave confirms have been checked. 129 were right on date and time (the miss was JBLU), and
  one time is unverifiable. That's evidence that the company-sourced-only policy works for this season's mix, mostly large caps
  with fixed habits. It isn't evidence about small caps or about aggregator sources, which the pool never contains.
- **Diminishing returns:** the remaining unaudited pool is ~87 rows of the same October wave. Another draw from it would mostly
  re-measure what we know. The next informative audit is the first one on a new season's confirms, which needs weekday
  sessions to exist.
