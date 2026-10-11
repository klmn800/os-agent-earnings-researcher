# Source-accuracy audit: 2026-10-11 (first run)

**Question:** of the dates I confirmed, did the date (and bmo/amc) turn out right, and does that
differ by the kind of source the confirm rested on?

## Pool and draw

- **Pool:** every agent confirm whose date fell **09-01 → 10-09**, i.e. everything already reported
  as of today: 43 September dates plus the 7 early-October ones (ACN, MKC, NKE 10-01; LW, STZ 10-06;
  PEP 10-08; DAL 10-09). **n = 50.** Assembled from the summer archive's Appendix A ledger, the
  09-27 header ledger, session tables and `earnings_date_disputes` (no single DB table keeps past
  confirms, since `earnings_upcoming` rolls forward).
- **Draw:** none. The pool was barely over the 40 target, so I checked **all 50** (a census)
  rather than sampling. No pick-and-choose was possible.
- **Tagging** (by the source the confirm actually rested on, from the original session entry):
  - company IR / newsroom / IR feed fetched directly: 38
  - company PR read as a copy (wire page, stocktitan, finviz, financialcontent): 11
  - company statement seen only via search summaries: 1 (LW)
  - aggregator / calendar site: 0
  - yfinance/finnhub agreement: 0
  - overlay, **time inferred** (call time, "that morning", or Item 2.02 history) with the date
    sourced: 11 (CAG, CCL, CTAS, DAL, DELL, GIS, GME, GOLD, HPE, KR, MU)
- **Lookups:** 5 general-purpose subagents, 10 symbols each, alphabetical batches. Each brief gave
  symbol, company, and the recorded date/time, plus the rules below. It did not say what the source
  was or what I expected.
- **Rules:** independent evidence only. The Item 2.02 8-K (6-K for NIO) with the ET `Accepted`
  time from the EDGAR filing index page, and/or the Ex-99.1 results release itself. Aggregator
  past-results pages were not allowed. bmo = released before 09:30 ET, amc = at/after 16:00 ET.
- **Re-check:** both mismatches (DELL, GME) re-read by me from EDGAR (index page + Ex-99.1 text).
  Both confirmed.

## Results by symbol

| SYM | Source type | Confirmed | Actual | Source of the actual | Verdict |
|---|---|---|---|---|---|
| ACN | IR direct | 10-01 bmo | 10-01 bmo | 8-K 0001467373-26-000037, acc. 10-01 06:42 | match |
| ADBE | copy (BW) | 09-10 amc | 09-10 amc | 8-K 0000796343-26-000147, 09-10 16:06 | match |
| AVGO | IR direct | 09-02 amc | 09-02 amc | 8-K 0001730168-26-000076, 09-02 16:26 | match |
| CAG | IR direct, time inf. | 09-30 bmo | 09-30 bmo | 8-K 0000023217-26-000052, 09-30 07:32 | match |
| CCL | copy, time inf. | 09-29 bmo | 09-29 bmo | 8-K 0000815097-26-000104, 09-29 09:16 | match |
| CIEN | IR direct | 09-03 bmo | 09-03 bmo | 8-K 0001628280-26-060245, 09-03 07:07 | match |
| CNM | IR direct | 09-09 bmo | 09-09 bmo | 8-K 0001856525-26-000091, 09-09 07:29 | match |
| CNXC | copy (GNW) | 09-29 amc | 09-29 amc | 8-K 0001803599-26-000147, 09-29 16:10 | match |
| COO | IR direct | 09-09 amc | 09-09 amc | 8-K 0001628280-26-061155, 09-09 16:34 | match |
| CPB | IR direct | 09-03 bmo | 09-03 bmo | 8-K 0000016732-26-000020, 09-03 07:17 | match |
| CPRT | copy (BW) | 09-10 amc | 09-10 amc | 8-K 0001193125-26-387902, 09-10 16:16 | match |
| CTAS | copy, time inf. | 09-23 bmo | 09-23 bmo | 8-K 0000723254-26-000044, 09-23 08:31 | match |
| DAL | IR direct, time inf. | 10-09 bmo | 10-09 bmo | 8-K 0000027904-26-000035, 10-09 06:30 | match |
| **DELL** | IR direct (events page), time inf. | **09-03** amc | **09-01** amc | 8-K 0001571996-26-000039, acc. 09-01 16:10; Ex-99.1 "ROUND ROCK, Texas, Sept. 1, 2026" | **date off by 2 d** |
| DOCU | IR direct | 09-03 amc | 09-03 amc | 8-K 0001261333-26-000088, 09-03 16:09 | match |
| DRI | IR direct | 09-24 bmo | 09-24 bmo | 8-K 0000940944-26-000032, 09-24 07:04 | match |
| FDS | copy (GNW) | 09-30 bmo | 09-30 bmo | 8-K 0001628280-26-063888, 09-30 07:01 | match |
| GIS | copy (BW), time inf. | 09-23 bmo | 09-23 bmo | 8-K 0001628280-26-063141, 09-23 07:01 | match |
| **GME** | IR feed (date), **time from 2.02 history** | 09-08 **amc** | 09-08 **bmo** | 8-K 0001326380-26-000050, acc. 09-08 09:02; Ex-99.1 BW 09-08, release 9:00 AM EDT | **time wrong** |
| GOLD | IR direct, time inf. | 09-02 amc | 09-02 amc | 8-K 0001193125-26-380542, acc. 17:55; release sets call "today" 4:30pm ET | match |
| GTLB | IR direct | 09-01 amc | 09-01 amc | 8-K 0001628280-26-059820, 09-01 16:12 | match |
| GWRE | IR direct | 09-03 amc | 09-03 amc | 8-K 0001528396-26-000039, 09-03 16:06 | match |
| HPE | IR direct, time inf. | 09-02 amc | 09-02 amc | 8-K 0001645590-26-000078, 09-02 16:06 | match |
| JBL | IR direct | 09-30 bmo | 09-30 bmo | 8-K 0001628280-26-063890, 09-30 07:32 | match |
| JEF | IR direct | 09-28 amc | 09-28 amc | 8-K 0000096223-26-000028, 09-28 16:18 | match |
| KMX | copy (BW) | 09-29 bmo | 09-29 bmo | 8-K 0001170010-26-000102, 09-29 07:00 | match |
| KR | IR direct, time inf. | 09-11 bmo | 09-11 bmo | 8-K 0001104659-26-106890, 09-11 06:59 | match |
| LEN | IR direct | 09-16 amc | 09-16 amc | 8-K 0001628280-26-062287, 09-16 16:42 | match |
| LULU | IR direct | 09-03 amc | 09-03 amc | 8-K 0001397187-26-000126, 09-03 16:07 | match |
| LW | search summaries | 10-06 bmo | 10-06 bmo | 8-K 0001679273-26-000051, 10-06 08:02 | match |
| M | IR direct | 09-10 bmo | 09-10 bmo | 8-K 0001628280-26-061217, 09-10 06:57 | match |
| MDB | IR direct | 09-01 amc | 09-01 amc | 8-K 0001628280-26-059794, 09-01 16:07 | match |
| MDT | IR direct | 09-01 bmo | 09-01 bmo | 8-K 0001628280-26-059697, 09-01 06:47 | match |
| MKC | copy (PRN) | 10-01 bmo | 10-01 bmo | 8-K 0000063754-26-000326, 10-01 07:31 | match |
| MTN | copy (PRN) | 09-28 amc | 09-28 amc | 8-K 0000812011-26-000048, 09-28 16:06 | match |
| MU | IR direct, time inf. | 09-30 amc | 09-30 amc | 8-K 0000723125-26-000018, 09-30 16:02 | match |
| NIO | IR direct | 09-01 bmo | 09-01 bmo | 6-K 0001104659-26-104110, 09-01 07:15 | match |
| NKE | IR direct | 10-01 amc | 10-01 amc | 8-K 0000320187-26-000184, 10-01 16:15 | match |
| NTAP | IR direct | 09-02 amc | 09-02 amc | 8-K 0001002047-26-000003, 09-02 16:05 | match |
| ORCL | IR direct | 09-10 amc | 09-10 amc | 8-K 0001193125-26-387905, 09-10 16:16 | match |
| PANW | IR direct | 09-01 amc | 09-01 amc | 8-K 0001327567-26-000019, 09-01 16:32 | match |
| PATH | IR direct | 09-03 amc | 09-03 amc | 8-K 0001734722-26-000047, 09-03 16:23 | match |
| PAYX | copy (GNW) | 09-23 bmo | 09-23 bmo | 8-K 0000723531-26-000004, 09-23 08:41 | match |
| PEP | IR direct | 10-08 bmo | 10-08 bmo | 8-K 0000077476-26-000050 acc. 10-07 17:57 (filed the evening before); Ex-99.1 dated 10-08, remarks 6:00am ET | match |
| PVH | IR direct | 09-02 amc | 09-02 amc | 8-K 0000078239-26-000055, 09-02 16:23 | match |
| SNOW | IR direct | 09-02 amc | 09-02 amc | 8-K 0001640147-26-000033, 09-02 16:08 | match |
| STZ | IR direct | 10-06 amc | 10-06 amc | 8-K 0000016918-26-000039, 10-06 16:18 | match |
| TTC | IR direct | 09-03 bmo | 09-03 bmo | 8-K 0000737758-26-000041, 09-03 08:44 | match |
| UEC | IR direct (+ copy) | 09-29 bmo | 09-29 bmo | 8-K 0001437749-26-031416, 09-29 06:00 | match |
| ZS | IR direct | 09-03 amc | 09-03 amc | 8-K 0001713683-26-000156, 09-03 16:08 | match |

0 unverifiable: every symbol had an Item 2.02 8-K (or 6-K) on EDGAR.

## Accuracy by source type

| Source type | n checked | date matched | date wrong | time wrong | unverifiable |
|---|---|---|---|---|---|
| Company IR / newsroom / feed, direct | 38 | 37 | 1 (DELL) | 1 (GME, inferred time) | 0 |
| Company PR read as a copy | 11 | 11 | 0 | 0 | 0 |
| Search-result summary only | 1 | 1 | 0 | 0 | 0 |
| Aggregator / calendar site | 0 | — | — | — | — |
| yfinance/finnhub agreement | 0 | — | — | — | — |
| *Overlay: time inferred, date sourced* | *11* | *10* | *1 (DELL)* | *1 of 11 (GME)* | *0* |

**Overall: 48 of 50 fully right (date and time); dates 49/50; times 49/50.**

How far to read this: two misses in 50 is too few to rank source types. "Copies 11/11" and
"direct 36/38" are **not** evidence that copies beat company pages. Both misses were company-origin
statements that were *true when read* and then failed for reasons unrelated to who hosted them
(below). The two weakest types (search summary, aggregator) have n = 1 and n = 0 in this pool; this
September pool simply contains almost none of them. Most of my weak confirms are October dates (BX, GM,
CME, MSCI, SCHW, plus ELV/MOH via biopharmawatch), which next week's audit will reach.

## The two misses: why the source misled

- **DELL, date −2 d.** Confirmed 08-13, **21 days ahead**, from Dell's IR *upcoming events*
  page ("Fiscal Year 2027 Second Quarter Results — Sep 3, 2026 at 3:30 PM CDT"). Dell actually
  reported **Tue 09-01**. The page was right when read; the event moved earlier afterwards. The cadence
  row then *told sessions not to look again* ("calendar pre-lists it ... never needs its ~14d
  advance PR"), so nobody saw the move. Class: **an early pre-listed calendar date treated as
  final.** Fix: cadence row now says pre-listed dates are provisional until the ~14d advance PR
  (or a re-read inside 14d) confirms them.
- **GME, time wrong (amc → bmo).** The date came from GameStop's own 08-31 preliminary-results PR,
  but the time was **inferred from Item 2.02 history** (8/9 quarters at 16:0x ET). The one outlier,
  2024-06-07 06:19 ET, was offering-linked. This quarter was offering-linked as well (a convertible-notes
  exchange; the 08-31 8-K carried 1.01/3.02 with the preliminary 2.02), and the full results came
  **09-08 at 9:00 AM ET**. Class: **time inferred from filing history across a regime change.** The
  outlier pattern was in the cadence row and I didn't apply it. Fix: the GME row now says that in a
  financing quarter, expect a morning release.

## Side findings for the SEC references

- **The submissions JSON `items` field can omit 2.02** (GWRE's 09-03 results 8-K is listed as
  5.02/9.01 only). A filter on `items` would have missed it. When a quarter's 2.02 seems absent, open
  the 8-Ks filed that day.
- **An 8-K accepted after 17:30 ET gets the next day's filing date** (PEP: accepted 10-07 17:57,
  filingDate 10-08, for a 10-08 6:00am release). GOLD's was accepted 17:55 on its release date.
  Acceptance times outside 06:00–09:30 / 16:00–16:50 need the release text, not a guess.
- **GME filed two 2.02 8-Ks** that quarter (08-31 preliminary, 09-08 full). Match the *complete* results.

## Not done here

No DB rows touched. These dates have passed, and `date_confirmed_by='ben'` rows are never mine.
