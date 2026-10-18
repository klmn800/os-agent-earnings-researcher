# Source-accuracy audit: 2026-10-18 (second run: back in time)

**Question:** the weak source types had n ≈ 0 in the 10-11 audit, because September confirms were almost all
company-sourced. Ben asked to go back in time. So: how accurate did summer writes turn out to be when they rested on
(A) SEC filing history, (B) feed agreement plus cadence, or (C) a time inferred from a call time or a home-market clock?

## Pool and draw

- **A, SEC filing-history times (n = 29, census).** The 07-15 session's 29 `unknown_time` writes, timed from Item 2.02
  acceptance history with the blanket UTC→ET conversion that the 07-31 note later proved unreliable. Time-only writes: the
  date was never sourced, but the pre-patch tool stamped it `date_confirmed=1` anyway. (The plan called this "the 07-14
  session". The block is in the 07-15 entry.)
- **B, feed / cadence locks (n = 12, census).** The 06-30 session's 10 convergence locks (KMI, CLF, LMT, EQT, SHW, RTX,
  CSGP, SNA, WAL, FNB), plus BAC and C. Those two were labelled "company-sourced" that day but rested on "multiple feeds
  confirmed", so they belong here.
- **C, inferred times with the date sourced (n = 17).** C1: the 12 summer confirms where the company PR gave only a call
  time (GPC, MMM, CNP, DOCS, EBAY, VVV, XRAY, WULF, AMTM, RKT, UUUU, BAH). Every one I could find by grepping the summer
  archive was included, except CAG, KR and MU, which the 10-11 audit had already checked. C2: the 5 foreign issuers whose
  bmo came from a home-market clock (KB, SAN, STLA, UL, ARGX).
- **Draw:** none. All three strata are censuses (58 symbols), so nothing was picked by memory.
- **Lookups:** 6 general-purpose subagents, ~10 symbols each, shuffled across strata (seed 20261018), each with its own
  scratch folder. Blind briefs: symbol, company, recorded date/time and the rules. No source type and no expectation.
- **Rules:** independent evidence only. Item 2.02 8-K / results 6-K with the ET `Accepted` time from the EDGAR index page
  (never the `acceptanceDateTime` field), and/or the dated results release / wire timestamp. No aggregator past-results
  pages. bmo = released before 09:30 ET, amc = at/after 16:00 ET.
- **Re-check:** I re-read all 12 mismatches on EDGAR myself: every 8-K/6-K/10-Q filed 07-10 → 08-20 with its Accepted
  time, plus the Ex-99.1 text for CNP, UGI and AMTM. **All 12 confirmed.** 0 unverifiable.

## Results by symbol

Verdict sign: actual − recorded (+ = it reported later than I had it).

| SYM | Source type | Recorded | Actual | Source of the actual | Verdict |
|---|---|---|---|---|---|
| BAC | feed / cadence lock | 2026-07-14 bmo | 2026-07-14 bmo | 8-K 0000070858-26-000353, acc. 07-14 06:45:08 | match |
| C | feed / cadence lock | 2026-07-14 bmo | 2026-07-14 bmo | BW wire 07-14 08:01 EDT; 8-K 0001104659-26-083383 acc. 09:39 (late) | match |
| CLF | feed / cadence lock | 2026-07-27 bmo | 2026-07-23 bmo | 8-K 0000764065-26-000097, acc. 07-23 06:27:24; Ex-99.1 "CLEVELAND, July 23, 2026", call 8:30am that morning | **date off by -4 d** |
| CSGP | feed / cadence lock | 2026-07-28 amc | 2026-07-28 amc | 8-K 0001057352-26-000061, acc. 07-28 16:05:38 | match |
| EQT | feed / cadence lock | 2026-07-28 amc | 2026-07-21 amc | 8-K 0000033213-26-000041, acc. 07-21 16:31:38; Ex-99.1 PITTSBURGH July 21 (07-14 2.02 was a hedging prelim) | **date off by -7 d** |
| FNB | feed / cadence lock | 2026-07-16 amc | 2026-07-16 amc | Ex-99.1 "after the market close on Thursday, July 16, 2026"; 8-K 0000037808-26-000023 acc. 07-17 07:34 (late filing) | match |
| KMI | feed / cadence lock | 2026-07-22 amc | 2026-07-22 amc | 8-K 0001506307-26-000063, acc. 07-22 16:09:59 | match |
| LMT | feed / cadence lock | 2026-07-28 bmo | 2026-07-23 bmo | 8-K 0001628280-26-049277, acc. 07-23 06:30:57; Ex-99.1 BETHESDA July 23 | **date off by -5 d** |
| RTX | feed / cadence lock | 2026-07-28 bmo | 2026-07-23 bmo | 8-K 0000101829-26-000025, acc. 07-23 06:51:03; call 7:30am 07-23 | **date off by -5 d** |
| SHW | feed / cadence lock | 2026-07-28 bmo | 2026-07-28 bmo | 8-K 0000089800-26-000046, acc. 07-28 07:05:57 | match |
| SNA | feed / cadence lock | 2026-07-16 bmo | 2026-07-23 bmo | 8-K 0000091440-26-000141, acc. 07-23 06:31:34; Ex-99 KENOSHA July 23 | **date off by +7 d** |
| WAL | feed / cadence lock | 2026-07-16 amc | 2026-07-21 amc | 8-K 0001628280-26-049001, acc. 07-21 16:16:47; BW dateline July 21, call 07-22 noon | **date off by +5 d** |
| ALAB | SEC filing history (time only) | 2026-08-04 amc | 2026-08-04 amc | 8-K 0001736297-26-000033, acc. 08-04 16:09:40 | match |
| ATO | SEC filing history (time only) | 2026-08-05 amc | 2026-08-05 amc | 8-K 0000731802-26-000100, acc. 08-05 16:47:05 | match |
| BALL | SEC filing history (time only) | 2026-08-04 bmo | 2026-08-04 bmo | 8-K 0001104659-26-090074, acc. 08-04 07:43:45 | match |
| DECK | SEC filing history (time only) | 2026-07-23 amc | 2026-07-23 amc | 8-K 0000910521-26-000015, acc. 07-23 16:07:23 | match |
| DT | SEC filing history (time only) | 2026-08-05 bmo | 2026-08-05 bmo | 8-K 0001773383-26-000049, acc. 08-05 06:32:18 | match |
| ELF | SEC filing history (time only) | 2026-08-05 amc | 2026-08-05 amc | 8-K 0001600033-26-000036, acc. 08-05 16:14:25 | match |
| EXPE | SEC filing history (time only) | 2026-08-05 amc | 2026-08-05 amc | 8-K 0001324424-26-000051, acc. 08-05 16:00:16 | match |
| FLY | SEC filing history (time only) | 2026-08-04 amc | 2026-08-11 amc | 8-K 0001860160-26-000022, acc. 08-11 16:08:20; call 5pm ET same day | **date off by +7 d** |
| GTES | SEC filing history (time only) | 2026-07-31 bmo | 2026-07-31 bmo | 8-K 0001628280-26-051221, acc. 07-31 07:37:01 | match |
| GXO | SEC filing history (time only) | 2026-08-04 amc | 2026-08-04 amc | 8-K 0001852244-26-000041, acc. 08-04 16:36:44 | match |
| L | SEC filing history (time only) | 2026-08-03 bmo | 2026-08-03 bmo | 8-K 0000060086-26-000045, acc. 08-03 06:06:10 | match |
| LINE | SEC filing history (time only) | 2026-08-05 bmo | 2026-08-05 bmo | 8-K 0001868159-26-000038, acc. 08-05 07:03:23 | match |
| MELI | SEC filing history (time only) | 2026-08-05 amc | 2026-08-05 amc | 8-K 0001099590-26-000021, acc. 08-05 16:00:58 | match |
| NRG | SEC filing history (time only) | 2026-08-04 bmo | 2026-08-04 bmo | 8-K 0001013871-26-000018, acc. 08-04 07:28:50 | match |
| PFE | SEC filing history (time only) | 2026-08-04 bmo | 2026-08-04 bmo | 8-K 0000078003-26-000094, acc. 08-04 07:02:43 | match |
| PINS | SEC filing history (time only) | 2026-08-04 amc | 2026-08-04 amc | 8-K 0001506293-26-000102, acc. 08-04 16:10:11 | match |
| PLTR | SEC filing history (time only) | 2026-08-03 amc | 2026-08-03 amc | 8-K 0001321655-26-000039, acc. 08-03 16:06:14 | match |
| PODD | SEC filing history (time only) | 2026-08-05 bmo | 2026-08-05 bmo | 8-K 0001145197-26-000167, acc. 08-05 07:04:50 | match |
| PPL | SEC filing history (time only) | 2026-07-30 bmo | 2026-08-07 bmo | 8-K 0000922224-26-000042, acc. 08-07 07:50:25; Ex-99.1 "ALLENTOWN ... Aug. 7, 2026" | **date off by +8 d** |
| RBA | SEC filing history (time only) | 2026-08-04 amc | 2026-08-04 amc | 8-K 0001628280-26-052570, acc. 08-04 16:11:38 | match |
| RRX | SEC filing history (time only) | 2026-08-05 bmo | 2026-08-05 bmo | 8-K 0000082811-26-000226, acc. 08-05 07:06:12 | match |
| RYN | SEC filing history (time only) | 2026-08-05 amc | 2026-08-05 amc | 8-K 0000052827-26-000094, acc. 08-05 16:17:50 | match |
| SBAC | SEC filing history (time only) | 2026-08-03 amc | 2026-08-03 amc | 8-K 0001193125-26-330639, acc. 08-03 16:23:13 | match |
| SMR | SEC filing history (time only) | 2026-08-05 amc | 2026-08-05 amc | 8-K 0001822966-26-000086, acc. 08-05 16:15:45 | match |
| TKO | SEC filing history (time only) | 2026-08-03 amc | 2026-08-03 amc | 8-K 0001193125-26-330561, acc. 08-03 16:08:11 | match |
| UGI | SEC filing history (time only) | 2026-08-05 bmo | 2026-08-05 amc | BW wire 08-05 17:30 EDT; Ex-99.1 dated Aug 5, call 08-06 9am; 8-K 0000884614-26-000048 acc. **08-06** 08:35 (next-morning filing) | **time wrong** |
| VFC | SEC filing history (time only) | 2026-07-29 bmo | 2026-07-29 bmo | 8-K 0000103379-26-000113, acc. 07-29 06:02:04 | match |
| VNOM | SEC filing history (time only) | 2026-08-03 amc | 2026-08-03 amc | 8-K 0002074176-26-000050, acc. 08-03 16:04:01 | match |
| VRTX | SEC filing history (time only) | 2026-08-03 amc | 2026-08-03 amc | 8-K 0000875320-26-000256, acc. 08-03 16:09:43 (no dateline) | match |
| AMTM | call time (time) | 2026-08-11 bmo | 2026-08-10 amc | 8-K 0001628280-26-055294, acc. 08-10 16:42:44; Ex-99.1 CHANTILLY Aug 10; call 08-11 8:30am | **date off by -1 d + time wrong** |
| BAH | call time (time) | 2026-07-24 bmo | 2026-07-24 bmo | 8-K 0001628280-26-049494, acc. 07-24 06:49:09 | match |
| CNP | call time (time) | 2026-07-28 amc | 2026-07-28 bmo | 8-K 0001104659-26-087279, acc. 07-28 06:15:27; 10-Q acc. 06:03:16 | **time wrong** |
| DOCS | call time (time) | 2026-08-06 amc | 2026-08-06 amc | 8-K 0001516513-26-000038, acc. 08-06 16:04:42 | match |
| EBAY | call time (time) | 2026-08-05 amc | 2026-08-05 amc | 8-K 0001065088-26-000174, acc. 08-05 16:07:47 | match |
| GPC | call time (time) | 2026-07-21 bmo | 2026-07-21 bmo | 8-K 0000040987-26-000031, acc. 07-21 07:34:06 | match |
| MMM | call time (time) | 2026-07-21 bmo | 2026-07-21 bmo | 8-K 0000066740-26-000242, acc. 07-21 06:34:07 | match |
| RKT | call time (time) | 2026-08-06 amc | 2026-08-06 amc | 8-K 0001805284-26-000082 acc. 17:24 (late); PRN wire 20:05 UTC = 16:05 ET | match |
| UUUU | call time (time) | 2026-08-06 bmo | 2026-08-05 amc | PRN wire Aug 5 4:15pm ET (wire copies); 10-Q 0001385849-26-000029 acc. 08-05 16:03:32; no 2.02 8-K | **date off by -1 d + time wrong** |
| VVV | call time (time) | 2026-08-05 bmo | 2026-08-05 bmo | 8-K 0001674910-26-000062, acc. 08-05 07:00:55 | match |
| WULF | call time (time) | 2026-08-05 bmo | 2026-08-05 bmo | 8-K 0001083301-26-000162, acc. 08-05 07:00:50 | match |
| XRAY | call time (time) | 2026-08-06 amc | 2026-08-06 amc | 8-K 0000818479-26-000253 (items list 9.01 only), acc. 08-06 16:14:10; call 4:30pm ET | match |
| ARGX | home-market clock (time) | 2026-07-23 bmo | 2026-07-23 bmo | 6-K 0001697862-26-000033, acc. 07-23 08:21:57; release 7:00 AM CET (01:00 ET) | match |
| KB | home-market clock (time) | 2026-07-23 bmo | 2026-07-23 bmo | 6-K 0001193125-26-313193, acc. 07-23 06:03:59 | match |
| SAN | home-market clock (time) | 2026-07-22 bmo | 2026-07-22 bmo | 6-K 0000891478-26-000069, acc. 07-22 06:02:38 | match |
| STLA | home-market clock (time) | 2026-07-30 bmo | 2026-07-30 bmo | 6-K 0001605484-26-000062 acc. 10:38 (late); call 2:00pm CEST / 8:00am EDT, release before | match |
| UL | home-market clock (time) | 2026-07-28 bmo | 2026-07-28 bmo | 6-K 0000217410-26-000057, acc. 07-28 08:21:23; release 7:00 AM UK (02:00 ET) | match |
## Accuracy by source type

| Source type | n | date right | date wrong | time right | time wrong | unverifiable |
|---|---|---|---|---|---|---|
| B. Feed agreement + cadence lock (06-30) | 12 | **6** | **6** (−7, −5, −5, −4, +5, +7) | 12 | 0 | 0 |
| A. Time from SEC filing history (07-15) | 29 | 27 † | 2 † (+7, +8) | **28** | 1 (UGI) | 0 |
| C1. Time inferred from the call time (date sourced) | 12 | 10 | 2 (−1, −1) | **9** | 3 (CNP, AMTM, UUUU) | 0 |
| C2. Time from a home-market clock (foreign issuers) | 5 | 5 | 0 | 5 | 0 | 0 |
| **All** | **58** | 48 | 10 | 54 | 4 | 0 |

† A's dates were never sourced. They were the DB's own dates, locked as a side effect of the time-only write, so they
score the DB plus that side effect, not a source.

For comparison, the 10-11 run (09-01 → 10-09 confirms, mostly company-sourced): dates 49/50, times 49/50.

**Reading it (small n, summer only, don't generalise beyond this):**
- **Feed/cadence locks are a coin flip on the date: 6 of 12 wrong, by 4–7 days.** Every miss is a whole-week-ish shift,
  in both directions, and in each case the feeds agreed with each other. This is the one type that missed repeatedly. Policy
  since 07-17 is already "no lock without a company source", so this confirms the policy, not a new ban. BAC and C were
  right only because the big banks pre-announce months ahead and every feed copies that.
- **SEC filing history is good for time (28/29)**, even with the conversion bug. Most filers sit far enough inside
  06:00–09:30 or 16:00–16:50 that a 4-hour shift would have been caught as implausible. The one miss is a different failure:
  **UGI files its 8-K the next morning**, so its history looks like a clean bmo signature for an evening release.
- **"Morning call ⇒ bmo" is the weak inference: 3 of 12 wrong.** AMTM and UUUU released the **evening before** a morning
  call, so the inference cost the date as well as the time. In AMTM's case I moved a correct DB date to a wrong one. CNP
  had a correct `bmo` flipped to `amc` off a call time that wasn't the real one (the actual call was 8am ET).
- **Home-market clocks held 5/5.** European/Korean releases at 07:00 local are hours before the US open, so there is no margin problem.

## Why each miss happened

| SYM | Why the source misled | Fixed |
|---|---|---|
| CLF, RTX, LMT, EQT | 06-30 "4th-Tuesday" cadence + feeds all copying one stale estimate; actual Q2 was the week before. Known since 07-17 (drift flag) | cadence rows (CLF, RTX added; LMT, EQT already had it) |
| SNA | "3rd-Thursday" rule was an artifact of the 53-week 2025 year; quarter-end moved +7d | row already carried it (09-24) |
| WAL | Same 3rd-Thursday shape; actual Tue 07-21. **Never caught before today**: no drift flag fired | cadence row rewritten |
| PPL, FLY | Time-only write (pre-09-16 tool) stamped an unsourced DB date as confirmed; PPL's feeds had pointed later | rows added; the tool cause is closed (`--time-only` since 09-16 leaves `date_confirmed` alone) |
| UGI | Filing history: 8-K accepted the next morning (08:35) for a 17:30 release | row added; SEC note extended |
| AMTM, UUUU | Call next morning; release came the prior evening. PR stated no release time | rows added; standing rule added |
| CNP | Recorded call time didn't match the actual 8am call; correct DB bmo flipped to amc | row annotated |

## What I'm asking Ben

Nothing to ban: feed/cadence locks are already disallowed, and the other types mostly held. One prompt tweak worth
considering (`notes_for_ben.md`): when a PR gives **only a morning call time**, treat the release time as unknown (so the
date could be the evening before) unless the PR or the prior quarter's release shows a same-morning release. I've made it a
standing rule in my own memory either way.

## Next run (10-25)

Forward: the October dates that have passed by then. Pool = the fall archive's Appendix A (pruned ledger rows) plus
whatever is pruned on 10-25. Weak ones to make sure are included: GM, MSCI (10-20), CME, ELV, MOH (10-21), BX (10-22),
SCHW (10-15, date inferred), ASML (10-14, bmo inferred), and every inferred-time row dated ≤ 10-23. (BA, JCI, ENPH and NVS report 10-27, so they go in the 11-01 run.)
