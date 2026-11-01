# Source-accuracy audit #4: 2026-11-01 (confirms dated 10-26 → 10-30)

**Question:** of the confirms whose dates passed this week, did the date and time turn out right, by source type?

**Result: 41 of 42 right on both date and time, 0 unverifiable. The one miss is JBLU, a time inferred from a morning call.**

## Pool and draw

- **Pool:** the 75 ledger rows dated 10-26 → 10-30 (now in the fall archive's Appendix A).
- **Strata, tagged from the ledger source text:** time inferred 13, search summary 10, IR / newsroom page direct 7, PR copy 45.
  Aggregator and feed agreement: 0 (policy since July).
- **Draw:** census of inferred, search summary and IR. 12 of 45 PR copies by `random.seed(20261101)`. That makes 42.
- **Lookups:** 5 general-purpose subagents, shuffled across strata, blind to source type and to what I expected.
- **Rules:** Item 2.02 8-K or results 6-K with the ET Accepted time from the EDGAR index page, Ex-99.1 dateline, dated release.
  No aggregator past-results pages. bmo = before 09:30 ET, amc = at or after 16:00 ET. Release wins over filing time.
- **Re-check:** one mismatch (JBLU). I re-read it on EDGAR myself and it stands.

## Accuracy by source type

| Source type | n checked | date matched | date wrong | time wrong | unverifiable |
|---|---|---|---|---|---|
| Company IR / newsroom page | 7 | 7 | 0 | 0 | 0 |
| PR read as a copy | 12 | 12 | 0 | 0 | 0 |
| Search summary of company text | 10 | 10 | 0 | 0 | 0 |
| Time inferred, date sourced | 13 | 12 | 1 | 1 | 0 |
| Aggregator / feed agreement | 0 | — | — | — | — |

Small n in every row. These do not rank the types. IR, search and inferred are censuses of this pool; PR copy is a sample.
Inferred times by audit: 9/12 (summer, call-time only), 13/13 (October, which also held clock and filing-history inferences),
12/13 (this week). The groups differ, so don't add them up.

## Results by symbol

Accepted times are ET from EDGAR index pages. "by" = upper bound from the filing.

| SYM | Source type | Recorded | Actual | Source of the actual | Verdict |
|---|---|---|---|---|---|
| BA | inferred | 10-27 bmo | 10-27 by 07:30 | 8-K 0001628280-26-067411 | match |
| CARR | inferred | 10-29 bmo | 10-29 by 07:26 | 8-K 0001783180-26-000035 | match |
| CDNS | inferred | 10-26 amc | 10-26 ~16:00 | 8-K 0000813672-26-000116, acc. 16:03; webcast 17:00 | match (soft: tightest amc) |
| ENPH | inferred | 10-27 amc | 10-27 ~16:05 | 8-K 0001463101-26-000101, acc. 16:07 | match |
| GD | inferred | 10-30 bmo | 10-30 by 08:09 | 8-K 0000040533-26-000036 | match |
| HCA | inferred | 10-27 bmo | 10-27 by 07:17 | 8-K 0001193125-26-432665 | match |
| JBLU | inferred | 10-27 bmo | **10-26 amc, ~16:15** | 8-K 0001158463-26-000095, acc. 10-26 16:15:21; Ex-99.1: call "tomorrow, October 27"; Investor Update dated 10-26 | **date off by −1 d, time wrong** |
| JCI | inferred | 10-27 bmo | 10-27 by 06:58 | 8-K 0000833444-26-000101 | match |
| MA | inferred | 10-29 bmo | 10-29 by 08:04 | 8-K 0001141391-26-000122 | match |
| NVS | inferred | 10-27 bmo | 10-27 by 06:08 | 6-K 0001114448-26-000014 | match |
| NVT | inferred | 10-30 bmo | 10-30 by 06:47 | 8-K 0001628280-26-068391 | match |
| PII | inferred | 10-27 bmo | 10-27 06:00 | 8-K 0001628280-26-067358, acc. 10-26 18:21 (filing date 10-27); wire 6:00am | match (evening-before filer) |
| RCL | inferred | 10-27 bmo | 10-27 by 06:32 | 8-K 0000884887-26-000042 | match |
| OKE | search | 10-27 amc | 10-27 by 16:27 | 8-K 0001039684-26-000036 | match |
| PPG | search | 10-27 amc | 10-27 by 16:22 | 8-K 0000079879-26-000315; "about 4:30 p.m. today" | match |
| RRC | search | 10-27 amc | 10-27 ~16:20 | 8-K 0001193125-26-435073, acc. **10-28 07:00**; Item 2.02 and Ex-99.1 say 10-27; 10-Q acc. 10-27 16:45 | match (next-morning 8-K filer) |
| SHW | search | 10-27 bmo | 10-27 by 07:04 | 8-K 0000089800-26-000054 | match |
| SOFI | search | 10-27 bmo | 10-27 by 07:02 | 8-K 0001818874-26-000065 | match |
| STAG | search | 10-27 amc | 10-27 by 16:07 | 8-K 0001479094-26-000032 | match |
| STX | search | 10-27 amc | 10-27 16:05 | 8-K 0001137789-26-000300, acc. 16:12 | match (dateline "Singapore Oct 28" is local) |
| UHS | search | 10-27 amc | 10-27 ~16:16 | 8-K 0001193125-26-434414, acc. 17:03 | match |
| V | search | 10-27 amc | 10-27 by 16:05 | 8-K 0001403161-26-000126 | match |
| WM | search | 10-27 amc | 10-27 by 16:38 | 8-K 0001104659-26-119188 | match |
| HIG | IR | 10-26 amc | 10-26 ~16:05 | 8-K 0000874766-26-000079, acc. 16:07 | match |
| KO | IR | 10-27 bmo | 10-27 by 06:58 | 8-K 0001628280-26-067403 | match |
| NUE | IR | 10-26 amc | 10-26 ~16:30 | 8-K 0001193125-26-432117, acc. 16:54 | match |
| SPGI | IR | 10-27 bmo | 10-27 by 07:15 | 8-K 0000064040-26-000053 | match |
| TRU | IR | 10-27 bmo | 10-27 by 06:15 | 8-K 0001552033-26-000056 | match |
| VZ | IR | 10-26 bmo | 10-26 by 07:00 | 8-K 0000732712-26-000049 | match |
| XOM | IR | 10-30 bmo | 10-30 ~06:30 | 8-K 0002115436-26-000018 | match |
| AMT | copy | 10-27 bmo | 10-27 by 07:03 | 8-K 0001053507-26-000154 | match |
| ARE | copy | 10-26 amc | 10-26 ~16:10 | 8-K 0001035443-26-000077, acc. 16:08 | match |
| BC | copy | 10-29 bmo | 10-29 by 06:18 | 8-K 0000014930-26-000130 | match |
| BRO | copy | 10-26 amc | 10-26 ~17:02 | 8-K 0001193125-26-432142, acc. 17:03 | match |
| BXP | copy | 10-27 amc | 10-27 16:05 | 8-K 0001037540-26-000041, acc. 16:10 | match |
| CINF | copy | 10-26 amc | 10-26 16:05 | 8-K 0000020286-26-000059, acc. 16:07 | match |
| ECL | copy | 10-27 bmo | 10-27 by 08:02 | 8-K 0001628280-26-067418 | match |
| EXEL | copy | 10-29 amc | 10-29 by 16:09 | 8-K 0000939767-26-000114 | match |
| FFIV | copy | 10-27 amc | 10-27 by 16:09 | 8-K 0001048695-26-000074 | match |
| HOOD | copy | 10-27 amc | 10-27 ~16:05 | 8-K 0001783879-26-000164, acc. 16:06 | match |
| ITW | copy | 10-27 bmo | 10-27 by 09:20 | 8-K 0000049826-26-000057 | match (closest bmo) |
| VTR | copy | 10-27 amc | 10-27 by 16:32 | 8-K 0000740260-26-000026 | match |

Wire stamps quoted from finviz copies carry no timezone label; the subagents read them as ET and each fits the 8-K time. The
"by" amc rows rest on the Accepted time plus the company's stated schedule. A release just before 16:00 isn't strictly excluded.

## The miss

**JBLU, 10-27 bmo → actually 10-26 amc.** The 10-13 PR gave a 10am call on 10-27 and no release time. I wrote bmo from the
call on 10-14, five days before the morning-call rule entered the prompt. JetBlue's five prior Item 2.02 8-Ks were all
same-morning on the call day (06:30 to 07:03), so **a prior-quarter check would have endorsed the wrong answer**. The company
changed its habit this quarter.

**What it means for the rule.** The morning-call rule says to settle the release day from the PR wording or the prior quarter.
JBLU shows the second half can fail. When the PR is silent, a morning-call date is a best guess, even with five clean quarters
behind it. That note is now in the cadence rule. One case doesn't justify holding every such row.

## Rule-6 exposures flagged earlier

NVT (9am call) and RCL (10am call), flagged 10-25: both held, same-morning. BA and JCI, called safe 10-18: both held.

## No source type missed repeatedly

One miss in one type, so nothing to propose dropping.
