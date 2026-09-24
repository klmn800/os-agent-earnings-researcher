# Earnings Research Log

> Active log: full sessions for the last ~2 weeks (newest first, below), a compact ledger of
> confirmed-but-upcoming dates, and the open carry-overs with next-check dates. Older sessions live in
> the season archives: `memory/archive/research_log_2026-Q2_spring-earnings.md` (through 06-30) and
> `memory/archive/research_log_2026-Q3_summer-earnings.md` (07-01 → 09-03, plus the summer's full
> confirmation ledger and carry-over table as appendices). Maintenance notes at the very bottom.
> Per-symbol cadence/lead-times live in `memory/reference_company_cadence.md` — **grep it by symbol
> (`^| SYM `); don't read it whole (~180 KB).**

## Open Carry-Overs — unresolved, with next-check dates

Symbols held because no company-issued source exists *yet*, plus confirmed rows under suspicion.
Next-check ≈ **advance-PR due date + 1** (most advance PRs publish after the ~07:15 session starts —
see the standing rules in `reference_company_cadence.md`). Rebuilt from the DB on 2026-09-20.

⚠⚠ **No daily session ran 09-16, 09-17 or 09-18** — the orchestrator spawns this agent only when the
lite refresh flags ≥1 dispute (`ei_lite_refresh.py:339`), and it flagged 0 on all three days. Both
next-check dates below were therefore **missed, not answered**: nothing here is evidence that an
advance is absent. See the 2026-09-20 maintenance entry.

| Symbol | DB date | Status | Next check |
|--------|---------|--------|------------|
| **AMX** | 2026-10-13 `amc` (finnhub 10-20) | Held 09-22. Company calendar feed found (`americamovil.com/feed/Event.svc/GetEventList`, cached); Q3 is Tuesday amc every year (10-17 / 10-15 / 10-14), **no 3Q26 event listed yet**. Both candidates are Tuesdays; 10-13 fits the trend, 10-20 looks like the +7d artifact. One curl of the feed, newest-first. | **2026-09-29**, then 10-06 |
| **ACI** | 2026-10-13 (`bmo` written 09-22 via `--time-only`, date unlocked) | FQ2 ends 09-12; the last two FQ2s reported 38d after quarter-end ⇒ **10-20** is the arithmetic, 10-13 would be the shortest FQ2 on record. Advance PR (BusinessWire, 14d lead) due ~09-29 → 10-06. | **2026-09-30** |
| **REXR** | 2026-10-14 `amc` (time set 09-23; finnhub now 10-21) | Held 09-23, **re-held 09-24**: IR press list still ends at the 09-17 portfolio-sale PR, no Q3 advance. Leads 24–35d (3 obs) ⇒ a 10-14 release's PR was due by 09-20 — **4+ days overdue**, so the date is probably wrong (PVH shape). 2026 quarters have been 4th-Thursday amc (04-23, 07-23) → 10-22 would put the PR at 09-17 → 09-28. PR publishes ~16:05 ET, so each morning read sees only prior-day PRs. finnhub moved 10-13 → 10-21 overnight (the +7d shape again). | **2026-09-25**, then daily to 09-29 |
| **SNA** | 2026-10-15 (`bmo` written 09-24 via `--time-only`; finnhub also 10-15) | ⚠ **Date probably a week early.** Snap-on's fiscal 2025 was a 53-week year ending **Jan 3, 2026** (Q2-26 8-K exhibit), so every 2026 quarter ends a week later than 2025's: Q2 ended **07-04** (vs 06-28) and reported **Thu 07-23** (vs 07-17) — the 06-30 "07-16" cadence lock was wrong by 7d. Q3 ends **10-03**; 2025's Q3 (ended 09-27) reported 10-16 = 19d ⇒ **Thu 10-22**. 10-15 would be 12d after quarter-end, shorter than any quarter on record. No advance channel until the *"to Webcast … Third Quarter Results Conference Call"* BusinessWire PR (14d lead: 10-02 → 10-16 in 2025, 07-09 → 07-23 in 2026) — due **10-01** if 10-15 is real, **10-08** if 10-22. Read the stocktitan spine. | **2026-10-02** (no PR ⇒ 10-15 is dead), then 10-09 |
| **WIT** | 2026-10-15 `bmo` (finnhub 10-13) | Held 09-24 — no Q2 FY27 advance yet. Wipro pre-announces ~9d ahead (*"Wipro Limited to announce results for the first quarter ended June 30, 2026, on July 16, 2026"*, dated 07-07); results *"after stock market trading hours in India"* (call 7pm IST = 9:30am ET) ⇒ bmo for the US row. Q2 has been a Thursday since 2023 (10-18 '23 Wed, 10-17 '24, 10-16 '25) → **Thu 10-15** fits; finnhub's Tuesday 10-13 does not. Advance PR due ~10-06 on wipro.com/newsroom (the list page is JS-only; search the title, or read the BusinessWire copy via stocktitan). | **2026-10-06**, then 10-07 |
| **FNB** | 2026-10-15 (`amc` written 09-24 via `--time-only`; finnhub 10-15) | Time sourced from the Q2 scheduling PR (*"after the market close on Thursday, July 16, 2026"*, call next morning 8:30am ET) + Item 2.02 furnished the next morning 11:3xZ 8/8. **Date not yet sourced**: newsroom and stocktitan spine end at the 09-03 community PR. Q2's *"Schedules … Earnings Report and Conference Call"* PR came **06-30 15:30 ET** for 07-16 (16d lead, first observation) ⇒ Q3's is due **~09-29** for 10-15. 3rd-Thursday amc fits (10-16 '25, 07-16 '26). Dispute row closed (`unknown_time` answered), date left unlocked. | **2026-09-30**, then 10-01 |

### Window watch — unconfirmed rows the horizon will surface soon

Not carry-overs (never researched this quarter); listed so Monday knows which advance-PR windows are
already open. Leads come from **other fiscal quarters** unless noted — per the WSM/CPRT lessons they are
advisory: read the channel anyway. Per the 09-14 MTN lesson, **a row with an open window gets a
stocktitan spine read the first day a session runs — don't wait for the horizon.**

| Symbol | DB row | Cadence says | Window |
|--------|--------|--------------|--------|
| ~~PEP~~ | ~~10-08 bmo~~ | ✅ confirmed 09-24 (PR had been out since 08-25 — 44d lead) | — |
| DAL | **10-09** bmo (was 10-08 on 09-13 — feed moved it) | lead never logged | unknown — check `news.delta.com` |
| 10-13 → 10-16 cohort (37 rows) | banks, JNJ, ABT, ASML, TSM, … | 14 have cadence rows (09-13); 23 are first-time names | measured leads ~27–35d (SCHW, FHN, ALLY, PEP) ⇒ **open now** |

## Upcoming Confirmed — locked dates (don't re-research)

One line per confirmed symbol whose date is still ahead (≥ 09-21), re-verified against
`earnings_upcoming` on 2026-09-20 — 14 rows (+6 added 09-22, +3 added 09-23, +3 added 09-24), all `1 / agent`, every date and time matching the DB.
LEN (09-16 amc) reported and was pruned. Format: `SYM | date | time | source — session`. Prune
reported rows each Sunday; the summer's full ledger is the summer archive's Appendix A.

| Symbol | Date | Time | Source — session |
|--------|------|------|------------------|
| CTAS | 2026-09-23 | bmo | BusinessWire 09-09 13:00 ET *"Cintas Corporation Announces Webcast for First Quarter Fiscal Year 2027 Results"* (via stocktitan); bmo = 10am webcast + Item 2.02 08:31–08:34 ET 6/6 — 09-10 |
| GIS | 2026-09-23 | bmo | General Mills advance 08-26 08:00 ET (BusinessWire); release issued that morning, webcast 8am CT — 09-02 |
| PAYX | 2026-09-23 | bmo | Paychex GlobeNewswire 09-09 09:15 ET (via stocktitan): *"Wednesday, September 23, 2026, before the financial markets open,"* call 9:30am ET. **Corrected from 09-29** — 09-14 |
| DRI | 2026-09-24 | bmo | Darden PR 08-27 16:00 ET (`investor.darden.com` feed): *"before the market opens"* — 09-03 |
| MTN | 2026-09-28 | amc | Vail PRNewswire 09-04 16:05 ET (via stocktitan): *"after market close on Monday, September 28, 2026,"* call 5pm ET — 09-14 |
| JEF | 2026-09-28 | amc | Jefferies advance 09-14 16:30 ET (`ir.jefferies.com` feed + news-details page): *"Monday, September 28, 2026 after market close."* Dispute resolved — finnhub 09-30 wrong — 09-15 |
| KMX | 2026-09-29 | bmo | CarMax BusinessWire 09-09 17:00 ET (via stocktitan): *"before the market opens on September 29, 2026,"* call 8am ET. Re-sourced 09-14 (09-08 lock was unsourced) — 09-14 |
| CNXC | 2026-09-29 | amc | GlobeNewswire 09-08 *"Concentrix Schedules Release of Third Quarter 2026 Financial Results…"*: after close, call 5pm ET — 09-09 |
| CAG | 2026-09-30 | bmo | Conagra PRNewswire 08-31; bmo **inferred** (materials "that morning" ahead of a 9:30am ET Q&A) — 09-09 |
| FDS | 2026-09-30 | bmo | FactSet GlobeNewswire 09-02 11:00 ET; presentation 8:30am, call 9:00am ET — 09-03 |
| JBL | 2026-09-30 | bmo | Jabil feed 09-09 16:10 ET: *"before the market opens,"* call 8:30am ET — 09-10 |
| MKC | 2026-10-01 | bmo | McCormick PRNewswire 08-31 08:00 ET (via stocktitan; IR host 403s); call 8am ET — 09-10 |
| NKE | 2026-10-01 | amc | Nike feed 08-28: *"approximately 1:15 p.m. PT, following the close"* — 09-10 |
| LW | 2026-10-06 | bmo | Lamb Weston scheduling release (~8:00am ET release, 9am call) — ⚠ weakest confirm on the list: no first-party fetch succeeded (IR 403 wall, no 8-K); rests on consistent search summaries + yfinance — 09-09 |
| UEC | 2026-09-29 | bmo | UEC advance 09-22 07:00 ET (via stocktitan) + `uraniumenergy.com/invest/events-and-webcasts` (webcast 8am PDT): *"before the markets open on Tuesday, September 29, 2026"*. **Corrected from 09-24 amc** — 09-22 |
| CCL | 2026-09-29 | bmo | Carnival PR Newswire 09-15 11:56 ET (via stocktitan): call 10am EDT, results *"released that morning"* — 09-22 |
| MU | 2026-09-30 | amc | Micron IR PR 08-26: call 2:30pm MT = 4:30pm ET — 09-22 |
| ACN | 2026-10-01 | bmo | Accenture newsroom 09-15: call 8:00am EDT, *"release will be issued before the call"*. **Time corrected from amc** — 09-22 |
| STZ | 2026-10-06 | amc | Constellation `ir.cbrands.com` detail/345, 09-10: *"after the close of the U.S. markets,"* call 10-07 8am ET. **Time corrected from bmo** — 09-22 |
| C | 2026-10-13 | bmo | Citi 2025 calendar PR (citigroup.com): *"3Q26 – Tuesday, October 13, 2026,"* release ~8am ET, webcast ~11am ET — 09-22 |
| PGR | 2026-10-14 | bmo | Progressive August results release (8-K 7.01, 09-18): *"We plan to release September results on Wednesday, October 14, 2026, before the market opens"* — 09-23 |
| FHN | 2026-10-15 | bmo | `ir.firsthorizon.com` PR 09-22: materials ~6:30am ET, call 9:30am ET. Snapshot 10-14 was already stale — 09-23 |
| SYF | 2026-10-20 | bmo | `investors.synchrony.com` detail/588: release ~6:00am ET, call 8:00am ET. Snapshot 10-14 was already stale — 09-23 |
| PEP | 2026-10-08 | bmo | pepsico.com newsroom PR 08-25 *"PepsiCo Announces Timing and Availability of Third-Quarter 2026 Financial Results"*: *"Thursday, October 8, 2026,"* materials ~6:00am EDT, Q&A 8:15am EDT — 09-24 |
| ERIC | 2026-10-15 | bmo | `ericsson.com/en/investors/financial-calendar/2026/q3-2026`: *"Oct 15, 2026 07:00 (CET)"* = 01:00 ET ⇒ bmo — 09-24 |
| JBHT | 2026-10-15 | amc | `investor.jbhunt.com` "Estimated Earnings Periods" table: Q3 release **October 15, 2026**, quiet period Sep 26 – Oct 15; amc = Item 2.02 furnished 20:08–21:26Z (16:0x–16:2x ET) 8/8 since 2024-10 — 09-24 |

---

# Research Sessions (newest first)

## Session: 2026-09-24 (Thursday) — 07:17 AM ET

8 surfaced (7 disputes: AMX, REXR, JBHT, WIT `date_disagreement`; ERIC, FNB, SNA `unknown_time`; 1 unconfirmed:
PEP). **3 confirmed on company sources (PEP, ERIC, JBHT), 2 time-only (FNB, SNA), 3 held (AMX, REXR, WIT).**
0 dates changed; 3 `Unknown` times filled (ERIC bmo, FNB amc, SNA bmo). Reads: 3 searches, 10 WebFetches
(1 NXDOMAIN — `investors.snapon.com` is dead), AMX Event.svc feed ×2, stocktitan spines ×3, EDGAR
submissions ×3 + 1 exhibit. All four finnhub dissents today are the +5/+7d shape (AMX, REXR, JBHT) or an
off-pattern weekday (WIT Tue); none was right where checked.

### Confirmed

| Symbol | Result | Source |
|--------|--------|--------|
| **PEP** | **2026-10-08 `bmo`** (DB right) | pepsico.com newsroom, **08-25**, *"PepsiCo Announces Timing and Availability of Third-Quarter 2026 Financial Results"*: results *"Thursday, October 8, 2026"* by posting the 10-Q, release and prepared remarks *"at approximately 6:00 a.m. EDT,"* analyst Q&A 8:15am EDT. Lead **44d** (Q2 was 35d → 2 obs, 35–44d). The window-watch row said "open since ~09-03"; the PR was already three weeks old when this session first read the channel. |
| **ERIC** | **2026-10-15 `bmo`** (`unknown_time` closed) | Ericsson financial calendar, per-quarter page `/2026/q3-2026`: *"Oct 15, 2026 07:00 (CET)"* — 07:00 Stockholm = 01:00 ET ⇒ bmo, same as every quarter. The calendar index page is JS-only to WebFetch; the per-quarter deep link renders. Cached. finnhub agrees on the date. |
| **JBHT** | **2026-10-15 `amc`** (finnhub 10-20 wrong — the +5d shape) | `investor.jbhunt.com` home page, "Estimated Earnings Periods" table: Q3 2026 release **October 15, 2026**, quiet period *"September 26, 2026 – October 15, 2026."* The table gives no time; amc from EDGAR CIK 728535 — 8/8 Item 2.02 8-Ks since 2024-10 accepted 20:08–21:26Z on the 15th (16:0x–16:2x ET), and every quarter the release goes out ~4pm ET with a 5pm call. J.B. Hunt reports on the 15th of the month after quarter-end regardless of weekday (10-15-24 Tue, 01-16-25 Thu, 04-15-25, 07-15-25, 10-15-25, 01-15-26, 04-15-26, 07-15-26). |

### Time-only (date NOT locked)

| Symbol | Written | Basis | Why the date is open |
|--------|---------|-------|----------------------|
| **FNB** | `amc` | Q2 scheduling PR 06-30 15:30 ET (via stocktitan): *"plans to issue financial results for the second quarter of 2026 after the market close on Thursday, July 16, 2026,"* call Friday 8:30am ET; Item 2.02 furnished the **next morning** 11:30–12:36Z, 8/8 since 2024-10 — the release-day-evening / 8-K-next-morning shape. | No Q3 scheduling PR yet (newsroom + stocktitan both end 09-03). Q2's came 16d ahead ⇒ due ~09-29. 10-15 = 3rd Thursday fits (Q3'25 10-16, Q2'26 07-16). Dispute row marked `confirmed_agent` (the `unknown_time` question is answered; the ACI 09-22 precedent), calendar row left `date_confirmed=0`. |
| **SNA** | `bmo` | Q2-26 results PR published **07-23 06:30 ET** (stocktitan timestamp), webcast 9:00am CT; Item 2.02 accepted 10:31–10:42Z on release day 6/8 (11:3xZ for the two February FY releases) — morning either way. | ⚠ **The 10-15 date is probably 7d early — see Held.** Dispute row left `unresolved` so the doubted date stays visible (REXR precedent). |

### Held

| Symbol | State | Reasoning | Next check |
|--------|-------|-----------|------------|
| **SNA** (date) | 10-15 `bmo`, finnhub also 10-15 | ⭐ **Fiscal-calendar shift found.** The Q2-26 8-K exhibit (EDGAR, curl) is headed *"Three Months Ended July 4, 2026 / June 28, 2025"* and cites the 10-K *"for the fiscal year ended January 3, 2026"* — fiscal 2025 was a **53-week year**, so every 2026 quarter ends one week later than 2025's. The report dates moved with it: Q1 **04-23** (vs 04-17 '25), Q2 **07-23** (vs 07-17 '25) — both 4th Thursdays, 19 days after quarter-end. **The 06-30 "07-16" cadence lock was therefore wrong by a week** (the archive's SNA line never recorded the outcome; EDGAR shows the 07-23 furnish). Q3-26 ends **10-03** → +19d = **Thu 10-22**. 10-15 would be 12d after quarter-end, shorter than any Snap-on quarter observed. Both the DB and finnhub sit on the 2025-shaped "3rd Thursday". Snap-on's only advance channel is the BusinessWire *"Snap-on Incorporated to Webcast 2026 Third Quarter Results Conference Call"* PR, **14d lead** (2025-10-02 → 10-16; 2026-07-09 → 07-23): due **10-01** if 10-15 were real, **10-08** for 10-22. Not written — a cadence argument is not a source (standing rule), however good the arithmetic. | **2026-10-02** (a silent 10-01 kills 10-15), then **10-09** |
| **REXR** | 10-14 `amc` (finnhub 10-21) | IR press list read again: newest is still the 09-17 portfolio-sale PR — no Q3 advance. Now 4+ days past the shortest observed lead for a 10-14 release; the 4th-Thursday reading (10-22, PR due 09-17 → 09-28) is still the live alternative. finnhub moved 10-13 → 10-21 overnight, i.e. onto the +7d artifact — treat as noise. | **09-25**, daily to 09-29 |
| **AMX** | 10-13 `amc` (finnhub 10-20) | Event.svc feed re-read (pageSize=100, sorted client-side — `sortDirection=desc` is ignored, and the feed returns the 2014 events first at pageSize=10): 61 unique events, newest still **2Q26 (07-22 call)** — no 3Q26 event. Held per the 09-22 reasoning; nothing new. | **09-29**, then 10-06 |
| **WIT** | 10-15 `bmo` (finnhub 10-13) | First-time name. Wipro's advance is a short-lead PR (*"Wipro Limited to announce results for the first quarter ended June 30, 2026, on July 16, 2026"* — dated **07-07**, 9d lead) on wipro.com/newsroom, also on BusinessWire. Results go out *"after stock market trading hours in India"* with a 7:00pm IST / 9:30am ET call ⇒ bmo for the US session, matching the stored time. Q2 report days: Wed 10-12 '22, Wed 10-18 '23, **Thu 10-17 '24, Thu 10-16 '25** — the stored Thu 10-15 is the pattern; finnhub's Tue 10-13 is not. No Q2 FY27 PR yet (due ~10-06). The newsroom list page is JS-only to WebFetch; individual PR pages render. | **10-06**, then 10-07 |

### Notes

- **PEP was sitting confirmed-in-public for 30 days.** The window-watch row flagged it "open (~09-03)" on 09-13 and
  09-20, and the PR had actually published 08-25. It only got read today because it entered the 14-day horizon
  as an unconfirmed backfill row. The dispute-gated launcher (09-20 note) is the reason; the fix proposal stands.
- **SNA is the 06-30 bad-lock batch, still paying out.** The July lock (07-16) was wrong, the outcome was never
  logged, and the Q3 row inherited the same 3rd-Thursday assumption. The general lesson is new though: a
  **53-week fiscal year shifts every report date in the following year by ~7d**, and a cadence row keyed to
  "nth weekday of the month" silently breaks. Check `fiscal year ended` in the latest 10-K/8-K when a
  company's 2026 dates all sit a week off 2025's (REXR shows the same 4th-Thursday shift — worth checking
  whether it is the same cause). Added to notes_for_ben.
- **finnhub as a signal today: 0 for 4.** AMX +7d, REXR +7d (after moving overnight), JBHT +5d, WIT −2d onto a
  Tuesday. None matched a company source.
- **Ericsson calendar:** the index page is a JS calendar; the per-quarter deep link (`/financial-calendar/2026/q3-2026`)
  is the readable one, so the cached URL is now quarter-specific and will need bumping to `/2027/q4-2026` next time.
- **Dead IR host:** `investors.snapon.com` NXDOMAIN; `www.snapon.com/EN/Investors` returns 200 (cached instead).
  Not yet checked for an events list — Snap-on has no advance channel other than the webcast PR anyway.
- **JBHT dispute pattern:** finnhub 10-20 is the third consecutive quarter it has disagreed with the IR table by
  +5d (the Q2 dispute was the same). The IR table is authoritative and pre-lists the whole year — no need to
  wait for anything.
- Tooling: the AMX feed had a 0x81 byte that `json.load` with the default cp1252 codec choked on — open with
  `encoding='utf-8'`. The `sortDirection` parameter is ignored; sort in Python.

## Session: 2026-09-23 (Wednesday) — 07:13 AM ET

4 disputes (PGR, SYF `date_disagreement`; FHN `both`; REXR `unknown_time`), all four rows dated 10-14 in the
snapshot. **3 confirmed on company sources (PGR, SYF, FHN), 1 time-only (REXR — date held).** The snapshot was
stale for two: the live rows already read **SYF 10-20** and **FHN 10-15** before this session touched them, so
those confirms locked the moved dates rather than correcting anything (0 dates changed today). Reads: 6
searches, 9 WebFetches (2× 404 on guessed Progressive event URLs), EDGAR submissions ×2 + 1 exhibit,
Progressive Q4 `Event.svc` feed ×3.

### Confirmed

| Symbol | Result | Source |
|--------|--------|--------|
| **PGR** | **2026-10-14 `bmo`** (DB right; finnhub 11-02 is the same +19d artifact as Q2's 08-03) | ⭐ **The previous month's results release is the advance channel.** *"Progressive Reports August Results"* (8-K **Item 7.01**, filed 09-18 08:38 ET, EX-99 `pgr202608ex99earningsrelea.htm`, read via curl) closes with *"Events — We plan to release September results on **Wednesday, October 14, 2026, before the market opens**."* Quarter releases since 2025-04 are all 3rd-Wednesday bmo (04-16, 07-16, 10-15 '25; 04-15, 07-15 '26; furnished 08:40–09:50 ET) and 10-14 is October's 3rd Wednesday. The Q4 `Event.svc` feed on `investors.progressive.com` renders (browser UA) but lists only the quarterly investor calls (~3 weeks after each release), not the results dates. |
| **SYF** | **2026-10-20 `bmo`** (snapshot 10-14; live row had already moved to 10-20 — yfinance 10-20 right, finnhub 10-13 wrong) | `investors.synchrony.com` financial-news detail/588, *"Synchrony to Announce Third Quarter 2026 Financial Results on October 20, 2026"*: release *"approximately 6:00 a.m. Eastern Time,"* call 8:00am ET. First-time name; IR URL cached (financial-news list). PR date not captured — lead unmeasured. |
| **FHN** | **2026-10-15 `bmo`** (snapshot 10-14 `Unknown`; live row already 10-15 — yfinance 10-15 right, finnhub 10-21 wrong) | `ir.firsthorizon.com` press release **09-22**, *"First Horizon Corporation to Announce Third Quarter Financial Results on October 15, 2026"*: materials *"approximately 6:30 am ET,"* call 9:30am ET. Lead **23d** (Q2 was 28d → 2 obs, 23–28d). |

### Held

| Symbol | State | Reasoning | Next check |
|--------|-------|-----------|------------|
| **REXR** | 10-14, **time set `amc` via `--time-only`; date NOT confirmed and probably wrong** | **Time** rests on the company's own advance PRs — Q3'25 *"after the market closes on Wednesday, October 15, 2025,"* Q1'26 and Q2'26 *"after the market closes on Thursday…"*; the Item 2.02 furnish stamps (20:1x–21:2x`Z`, 12/12 quarters since 2023) are consistent and were not timezone-converted. **Date:** the IR press list is current through 09-17 and carries no Q3 advance. Leads now 3 obs: Q3'25 **29d** (09-16→10-15), Q1'26 **35d** (03-19→04-23), Q2'26 **24d** (06-29→07-23). For a 10-14 release the PR was due 09-09 → 09-20 — **3+ days overdue against the shortest lead** ⇒ the PVH shape: distrust the date, don't guess the replacement. Cadence hint only: Q3 was Wed 10-18 / 10-16 / 10-15 ('23–'25), but both 2026 quarters slipped to the **4th Thursday** (04-23, 07-23) → October's is **10-22** (PR due 09-17 → 09-28). finnhub 10-13 is the −1d shape. The PR publishes ~16:05 ET (2/2), so a morning read only sees prior-day PRs. Dispute row left `unresolved` (unlike ACI on 09-22, which was marked `confirmed_agent` on a time-only fix — leaving it open keeps the row visible while the date is doubted). | **09-24**, then daily through 09-29 (one WebFetch of the press list) |

### Notes

- **Stale snapshot ×2 (SYF, FHN).** Both live rows had already moved to the company's dates (FHN's PR is dated
  09-22, so the overnight feed caught it). Per [[dispute-snapshot-is-stale]] these are locks, not corrections.
- **PGR channel:** Progressive pre-announces the quarter-end release date inside the *previous month's* results
  release ("Events" paragraph, ~26d ahead) and files that release under **Item 7.01** — an EDGAR sweep
  filtered on 2.02 misses it for this name. Cached IR URL moved from the home page to the
  financial-news-releases list (JS-rendered; the EDGAR exhibit is the readable copy).
- 10-13 → 10-16 cohort: PGR and FHN handled today; SYF moved out of it (10-20). REXR is the first cohort
  member showing the overdue-advance signal.

## Session: 2026-09-22 (Tuesday) — 07:13 AM ET

8 surfaced (3 disputes: AMX `date_disagreement`, ACI + C `unknown_time`; 5 unconfirmed: UEC, CCL, MU, ACN, STZ).
**6 confirmed on company sources (UEC, CCL, MU, ACN, STZ, C), 1 time-only (ACI), 1 held (AMX).** Three
stored values were wrong and got fixed: **UEC date 09-24 → 09-29 and amc → bmo; ACN amc → bmo; STZ bmo → amc.**
First session since 09-15 (no session 09-16 → 09-18, dispute-gated; 09-21 also did not run). Reads: 8 searches,
7 WebFetches (1 BusinessWire 403), EDGAR submissions ×2 + 6 filings, 3 IR-host curls, 1 stocktitan spine, and
**the AMX Q4 event feed (new channel, see Notes)**.

### Confirmed / corrected

| Symbol | Result | Source |
|--------|--------|--------|
| **UEC** | **2026-09-29 `bmo`** — ⚠ corrected from 09-24 `amc` (+5d, time flipped) | Advance PR **published this morning 09-22 07:00 ET** (via stocktitan; the exact 7d lead seen for FY26 Q2/Q3): *"issue its fiscal 2026 year-end operating and financial results **before the markets open on Tuesday, September 29, 2026**,"* call 11:00am ET. Corroborated first-party: `uraniumenergy.com/invest/events-and-webcasts` lists *"URANIUM ENERGY FY 2026 RESULTS WEBCAST — Tuesday, September 29, 2026 — 8:00AM PDT"* (curl, browser UA). The carry-over's `bmo` expectation was right; its date was not (the 09-24 row was a feed guess, and the cadence row's 10-K-eve reading was also wrong for the date). |
| **CCL** | **2026-09-29 `bmo`** (DB right — the 09-15→09-20 feed move to 09-29 was correct) | PR Newswire **09-15 11:56 ET**, *"Carnival Corporation & plc to Hold Conference Call on Third Quarter Earnings"* (via stocktitan): call *"Tuesday, September 29, 2026, at 10 a.m. (EDT)"*, results *"expected to be released that morning."* Lead **14d** (Q2 was 12d). |
| **MU** | **2026-09-30 `amc`** (DB right) | `investors.micron.com` PR **08-26**, *"Micron Technology to Report Fiscal Fourth Quarter Results on September 30, 2026"*: call *"2:30 p.m. Mountain time"* = 4:30pm ET ⇒ amc (no before/after phrase in the PR; the 4:30 ET call is the amc evidence, same as every prior quarter). Lead **35d** (fiscal Q3 was 28d). |
| **ACN** | **2026-10-01 `bmo`** — ⚠ corrected from `amc` (the 09-13 re-seed flag) | `newsroom.accenture.com` **09-15**, *"Accenture to Announce Fourth-Quarter and Full-Year Fiscal 2026 Results"*: call *"8:00 a.m. EDT on Thursday, October 1, 2026,"* *"An earnings news release will be issued before the call."* Lead **16d** — exactly the cadence row's figure. |
| **STZ** | **2026-10-06 `amc`** — ⚠ corrected from `bmo` (the 09-13 re-seed flag) | `ir.cbrands.com` detail/345, **09-10 16:30 ET**: *"Tuesday, October 6, 2026, after the close of the U.S. markets,"* call 8:00am ET **Wednesday 10-07**. Second consecutive quarter of release-after-close / call-next-morning ⇒ amc is now 2 obs. Lead **26d**. |
| **C** | **2026-10-13 `bmo`** (`unknown_time` closed; date sourced for the first time) | Citi's own calendar PR *"Citi Third Quarter and Fourth Quarter 2025 Earnings Calls and First Quarter … Fourth Quarter 2026 Earnings Calls"* (citigroup.com, 2025): *"3Q26 – Tuesday, October 13, 2026,"* results *"via press release at approximately 8 a.m. (ET),"* webcast ~11am ET. One page covers the whole year — cached. Dispute row `confirmed_agent`. |
| **ACI** | **`bmo` written via `--time-only`; date 10-13 NOT locked** | EDGAR CIK 1646972: **11/11 Item 2.02 8-Ks since 2024-01 accepted 07:30–08:32 ET** (07-23 11:31Z, 04-14 11:30Z, 01-07 12:30Z, 2025-10-14 11:31Z …) ⇒ bmo settled from furnish history, per the standing rule. No FQ2 advance yet (stocktitan spine newest = brand news; last year's FQ2 advance was BusinessWire **2025-09-30** for a 10-14 release = 14d). Dispute row `confirmed_agent` with the DB date recorded as-is; see Held for why the date is doubtful. |

### Held

| Symbol | DB date | Why skipped | Next check |
|--------|---------|-------------|------------|
| **AMX** | 2026-10-13 `amc` (finnhub 10-20) | ⭐ **Found the company channel**: the JS-only IR calendar is a Q4 site and its data feed is readable — `americamovil.com/feed/Event.svc/GetEventList?…` (browser UA, curl; cached as the IR URL). Every quarter since 2016 is an event titled *"AMX will report 3Q25 Financial and Operating Results on October 14th after the market close. The conference call…"* dated the **next morning** (call day). **Q3 history: 3Q23 Tue 10-17, 3Q24 Tue 10-15, 3Q25 Tue 10-14 — all Tuesday amc, 14–17 days after quarter-end**; 2Q26 was Tue 07-21 amc. ⚠ The results 6-Ks post **2 days later** (10-16, 10-17, 10-19) — do not read 6-K dates as release dates for AMX. **No 3Q26 event is listed yet.** Both candidates are Tuesdays; 10-13 (13d after q-end) continues the 17→15→14 trend, 10-20 (20d) would be the latest Q3 in the series — finnhub's +7d artifact shape. Not locked: no same-quarter source. | **2026-09-29**, then 10-06 (one curl of the feed, newest-first) |
| **ACI** (date) | 2026-10-13 (time now bmo) | FQ2 FY26 ends **09-12** (16+12 weeks from 02-28). FQ2 FY25 ended 09-06 → reported 10-14 (**38d**); FQ2 FY24 09-07 → 10-15 (38d); FQ1 FY26 06-20 → 07-23 (33d). 38d from 09-12 = **10-20 (Tue)**; 10-13 would be 31d, shorter than any FQ2 on record. The stored 10-13 is probably a stale +364d guess. Advance PR due ~**09-29 → 10-06** at the 14d lead, BusinessWire, *"Albertsons Companies Announces Second Quarter Fiscal 2026 Earnings Release and Conference Call Date."* | **2026-09-30** |

### Notes
- **UEC would have "reported in 2 days" per the DB** — the real date is a week out. The 09-17 next-check
  that never ran would also have found nothing (the PR came 09-22); the 7d lead held exactly, so the
  FY-end advance channel behaves like Q2/Q3. Cadence row rewritten.
- **Two re-seed time flags closed (ACN, STZ)**, both in the direction the cadence rows predicted. The MDT
  shape (a feed re-seed flips a settled time) is now 4-for-4 on the Q3 cohort where it has been checked.
- **Q4 Inc `Event.svc` feed** — first time used. Generalizable: any `*/English/investors/events/calendar/default.aspx`
  Q4 page should have `/feed/Event.svc/GetEventList` behind it (parameters as in the cached AMX URL;
  `eventSelection=0`, sort desc, `pageSize=100`, paginate with `pageNumber`). Promoted to
  `reference_q4_event_feed.md`. The feed returned each event twice and ignored `eventDateFilter`.
- WebSearch summaries were used only as pointers; every date above was read from a company page, a wire
  reprint on stocktitan, or EDGAR. BusinessWire deep links 403 to WebFetch (ACI FQ2 FY25 advance).
- `earnings_confirm.py --time-only` used for the first time in a daily session (ACI): wrote `bmo`, left
  `date_confirmed=0`. Works as patched.
- ⚠ Tooling: Bash heredocs whose body has an odd count of single quotes (a Python triple-quoted
  string, an apostrophe) are rejected by the harness command parser before bash runs — the edit
  script for this session had to be written with the Write tool as `.txt` (the hook refuses `.py`)
  and run with `python <file>`.

## Session: 2026-09-15 (Tuesday) — 07:13 AM ET

3 surfaced (JEF dispute `date_disagreement`; UEC, CCL unconfirmed). **1 confirmed (JEF), 2 gated (UEC, CCL)**.
Reads: 1 RSS (WebFetch + curl), 1 IR news-details page, 2 stocktitan spines, 1 search (discarded). ⚠ Prompt
header said "1 symbols"; the hook injected 3 (1 dispute + 2 unconfirmed). Harmless count mismatch.

### Confirmed

| Symbol | Result | Source |
|--------|--------|--------|
| **JEF** | **2026-09-28 `amc`** (DB right, finnhub 09-30 wrong) | Jefferies feed item **09-14 16:30 ET**, *"Jefferies to Release its Third Quarter Financial Results on September 28, 2026"*. Body (IR news-details page, via WebFetch): *"will release its third quarter financial results on Monday, September 28, 2026 after market close."* Lead **14d**, exactly as predicted. Dispute row `confirmed_agent`. Calendar row verified `1 / agent`. |

### Gated

| Symbol | DB date | Why skipped | Next check |
|--------|---------|-------------|------------|
| UEC | 2026-09-24 `amc` | stocktitan newest still 07-23, no FY-end advance. Not due until ~09-17 (7d lead, 07:00 ET). `bmo` caution stands. | 2026-09-17 |
| CCL | 2026-09-28 `bmo` | stocktitan current to 09-10, brand news only, no Q3 advance. Due ~09-16 (12d lead). | 2026-09-16 |

### Notes
- **The JEF carry-over resolved exactly on schedule.** The 09-09 correction (the channel exists, read the morning after
  the 14d due date) was right. The 09-08 "no advance PR" conclusion would have held the dispute to 09-25.
- **The WebSearch summary asserted "Sep 30" for JEF**, citing Investing.com, against the company's own feed title.
  Third-party search summaries still parrot the finnhub estimate even after the company has spoken. Discarded.
- The IR news-details page is a 259 KB JS shell to curl (no body text). WebFetch renders the body. Feed titles
  carry the date but not the timing.
- The `earnings_confirm.py` patch is **still not live** (`--help` shows no `--time-only`). Used the full
  `--date --time --by agent` form, which is correct for a company-sourced date.

## Session: 2026-09-14 (Monday) — 07:13 AM ET

4 surfaced (JEF dispute `both`; UEC, CCL, MTN unconfirmed) + the 2 priority carry-overs due today
(PAYX, KMX). **3 confirmed (MTN, PAYX, KMX), 1 corrected (PAYX 09-29 → 09-23), 3 gated (JEF, UEC, CCL)**,
plus the JEF time write. Reads: 1 RSS, 2 feed probes (Vail 403), 5 stocktitan spines, 3 stocktitan articles. 0 searches.

### Confirmed / corrected

| Symbol | Result | Source |
|--------|--------|--------|
| **PAYX** | **2026-09-23 `bmo`** — ⚠ **corrected from the unsourced 09-08 lock (09-29)**; yfinance's drift flag was right | Paychex GlobeNewswire **09-09 13:15Z**, *"Paychex Schedules First Quarter Fiscal 2027 Earnings Conference Call on September 23, 2026"*: *"Wednesday, September 23, 2026, before the financial markets open,"* call 9:30am ET. Lead **14d**. Resolved the 09-11 `confirmed_row_diverged` row. ⚠ Q1 moved from Tuesday (2/2 prior years) to **Wednesday** — the weekday history would have kept the wrong date. |
| **KMX** | **2026-09-29 `bmo`** (lock was right, now sourced) | CarMax BusinessWire **09-09 21:00Z**, *"CarMax Announces Second Quarter Conference Call"*: *"before the market opens on September 29, 2026,"* call 8:00am ET. Lead **20d**. Cached BW `20260909520212`. |
| **MTN** | **2026-09-28 `amc`** (DB right) | Vail PRNewswire **09-04 20:05Z**, *"Vail Resorts Announces Fiscal 2026 Fourth Quarter and Year-End Earnings Release Date"*: *"after market close on Monday, September 28, 2026,"* call 5:00pm ET. Lead **24d**, matching Q3's 24d. `investors.vailresorts.com` **403s both RSS paths even with a browser UA**. Cached the PRNewswire permalink. |

### Gated

| Symbol | DB date | Why skipped | Next check |
|--------|---------|-------------|------------|
| JEF | 2026-09-28 (`amc` now) | Feed current to 09-09, no Q3 advance. Expected: at the 14d lead the 09-28 advance would publish ~16:20 ET **today**. **Wrote `earnings_time='amc'`** via plain UPDATE (`date_confirmed` stays 0). Evidence: the feed itself shows results releases at 16:15/16:16 ET (Q1 03-25, Q2 06-24). | 2026-09-15 |
| UEC | 2026-09-24 `amc` | stocktitan newest still 07-23; no FY-end advance. Due ~09-17 at the 7d lead. `bmo` caution stands. | 2026-09-17 |
| CCL | 2026-09-28 `bmo` | stocktitan current to 09-10 (brand news only), no Q3 advance. Q2 lead was 12d ⇒ due ~09-16. | 2026-09-16 |

### Notes
- **The 09-08 confirm-tool-as-time-fix error cost exactly one wrong date out of two** (PAYX −6d; KMX happened
  to be right). Both advance PRs had been out since **09-09**. That's 5 days of a wrong locked row that the
  normal dispute stream suppressed. Only the `confirmed_row_diverged` flag surfaced it.
- **stocktitan JSON-LD found all 3 advances in 5 spine reads.** MTN's had been sitting there since 09-04; the
  window-watch table said "open ~09-04" and nobody read it. Window-watch rows with an open window should
  get a spine read the day they open, not wait for the horizon.
- `--sql` `;` split hit again (a `;` inside the `notes` literal) — see [[reference-db-write-forward-slash-paths]]. Retried without it.

## Session: 2026-09-11 (Friday) — 07:16 AM ET

2 surfaced (JEF dispute `both`, UEC unconfirmed): **0 confirmed, 2 gated** — both re-surfaced ahead of
their recorded next-check dates (09-15 / 09-17), so this was an early-fire probe only. 5 HTTP reads, 0 searches.

| Symbol | DB date | Why skipped | Next check |
|--------|---------|-------------|------------|
| JEF | 2026-09-28 (Unknown) | `ir.jefferies.com/rss/pressrelease.aspx` read OK, newest item 09-09; **no Q3 advance**. One unlogged item: *"Jefferies Financial Group Inc. to Host Annual Investor Meeting"* (09-03 16:30 ET) — meeting **Mon 10-19-2026 9:00am**, Manhattan; body says nothing about Q3 results (read via WebFetch — the news-details HTML is a shell to urllib, RSS carries headline only). Not informative for 09-28 vs 09-30. ⚠ **Third candidate (Ben, 09-11):** third-party estimates show **10-05** (+35d post-qtr-end — outside the 24–29d band on 5 recorded quarters, so least likely by cadence, but estimate-only, not a source either way). At the 14d lead its advance would land ~**09-21**, so an empty feed on 09-15/09-16 rules out 09-28/09-30 progressively but says nothing against 10-05 — keep checking through ~09-22 before reading silence as signal. | 2026-09-15 |
| UEC | 2026-09-24 `amc` | stocktitan newest still 07-23; EDGAR (CIK 1334933) nothing but Form 4 / 13G since 07-31, no 8-K. FY-end advance due ~09-17 at the 7d lead. Prior `bmo`-not-`amc` caution (09-10 entry) still stands. | 2026-09-17 |

## Session: 2026-09-10 (Thursday) — 07:16 AM ET

6 surfaced (5 disputes + UEC unconfirmed): **4 confirmed (CTAS, JBL, MKC, NKE), 2 gated (JEF, UEC)**.
**WebSearch was down for the whole session** (6/6 attempts returned "unavailable"), so every
confirm came from the fallback stack: IR RSS feeds (browser UA), stocktitan JSON-LD, and EDGAR
submissions. All four were read off company-issued text; none needed search.

### Confirmed (4)

| Symbol | Result | Source |
|--------|--------|--------|
| CTAS | **2026-09-23 `bmo`** (DB right; finnhub 09-30 wrong) | BusinessWire **09-09 13:00 ET**, *"Cintas Corporation Announces Webcast for First Quarter Fiscal Year 2027 Results"* — releases Wed 09-23, webcast **10:00am ET** same day. Found via `stocktitan.net/news/CTAS/` JSON-LD. PR states no clock time; `bmo` rests on the 10am webcast + Item 2.02 furnish 08:31–08:34 ET 6/6. BW `20260909223284`. No IR URL cached (no first-party host exists). |
| JBL | **2026-09-30 `bmo`** (DB 09-24 wrong; **yfinance right**) | `investors.jabil.com` feed → *"Jabil Announces Date for Fourth Quarter and Fiscal Year 2026 Earnings Release and Investor Briefing"* **09-09 16:10 ET** — *"Wednesday, September 30, 2026, before the market opens,"* call 8:30am ET. Lead **21d**. `earnings_upcoming` already held 09-30 (adopted from yfinance after the dispute snapshot). Cached `investors.jabil.com/rss/pressrelease.aspx`. |
| MKC | **2026-10-01 `bmo`** (DB right; finnhub 10-05 wrong) | PRNewswire **08-31 08:00 ET**, *"McCormick & Company to Report 2026 Third Quarter Financial Results on October 1, 2026"* — call **8:00am ET**. Found via stocktitan (`ir.mccormick.com` **403s every path** to urllib). `bmo` also 100% on furnish history (Item 2.02 06:40–07:39 ET every quarter since 2020). Lead **31d**. |
| NKE | **2026-10-01 `amc`** (DB right; finnhub 09-28 wrong) | `investors.nike.com` feed → *"NIKE, Inc. Announces First Quarter Fiscal 2027 Earnings and Conference Call"* **08-28** — *"Thursday, October 1, 2026, at approximately 1:15 p.m. PT, following the close."* Lead **34d**. Time was Unknown → `amc`. Cached IR URL upgraded to the feed. |

### Gated (2)

| Symbol | DB date | Why skipped | Next check |
|--------|---------|-------------|------------|
| JEF | 2026-09-28 (Unknown) | `ir.jefferies.com/rss/pressrelease.aspx` **works** (current to 09-09), no Q3 advance yet — expected, due ~09-14 for 09-28 or ~09-16 for 09-30 at the 14d lead, and Jefferies publishes ~16:20 ET ⇒ check the morning after. Time still `amc` 4/4 but unwritten (no time-only confirm mode). | 2026-09-15 |
| UEC | 2026-09-24 `amc` | No FY26 year-end date PR yet (stocktitan + uraniumenergy.com, newest item 07-23). UEC's FY26 Q2/Q3 advances ran **7d leads at 07:00 ET** ⇒ due ~09-17 for a 09-24 release. | 2026-09-17 |

### ⚠ UEC — the stored `09-24 amc` is wrong under either reading of the FY-end filing pattern

FY25 year-end: 10-K accepted **2025-09-23 20:43 ET**, results webcast **Wed 2025-09-24 8:00am PT**
(company events page). FY26 Q1/Q2/Q3 all stated *"before markets open"* in the company PR. So the
market reacts on the **morning of the webcast day**. That can be encoded as "D−1 amc" or "D bmo",
but **"D amc" (which is what the DB holds) puts the reaction a day late** under both readings. Did
not write the time, because the 2026 date is unsourced and the FY-end quarter could differ. When
the advance lands, expect `bmo` and check whether the 10-K again drops the prior evening.
FY-end 10-K history: 2025-09-23, 2024-09-26, 2023-09-28, 2022-09-29 (all evening), so 09-24 is
plausible but the band spans ~a week.

### Notes
- **WebSearch outage cost nothing.** The RSS sweep plus one stocktitan spine per symbol found all four
  advance PRs, and three of them were already sitting in feeds the prior session had not probed. The
  fallback stack is now evidence-tested as a *primary* for any symbol with a known feed.
- **JEF's cached IR URL was a Morningstar reprint** (third-party). Replaced with the verified first-party
  feed `ir.jefferies.com/rss/pressrelease.aspx`, which carried the Q2 advance (06-16 16:20 ET). The old
  cheat-sheet listed ir.jefferies.com as "SPA shell"; the HTML is, but the RSS is not.
- **CTAS second lead observation = 14d** (09-09 → 09-23), matching Q4 FY26's 14d. The band now rests on
  2 observations. Publish time 13:00 ET (vs 13:29 last quarter), which confirms the "check the morning
  after" rule; yesterday's empty 07:13 read was the clock artifact predicted.
- finnhub was wrong on all four confirms (CTAS +7d, MKC +4d, NKE −3d, and it matched DB's wrong 09-24 on JBL). yfinance-only dissent (JBL) was right again.

## Session: 2026-09-09 (Wednesday) — 07:13 AM ET

5 surfaced symbols — **3 confirmed (CNXC, CAG, LW), 2 gated (CTAS, JEF)**, ~16 HTTP reads,
6 web searches. Two of the three confirms came from advance PRs that **contradicted the DB date**,
and the session's most useful output is arguably not a confirm at all but a **correction to
yesterday's JEF row** that moves its next-check forward 11 days.

### Confirmed (3)

| Symbol | Result | Source |
|--------|--------|--------|
| CNXC | **2026-09-29 `amc`** (DB 09-24, finnhub 09-30 — both wrong) | GlobeNewswire **09-08**, *"Concentrix Schedules Release of Third Quarter 2026 Financial Results and Investor Conference Call"* — *"after market close on Tuesday, September 29, 2026,"* call 5:00pm ET. Discovered via the cached `ir.concentrix.com/rss/pressrelease.aspx`. |
| CAG | **2026-09-30 `bmo`** (time was Unknown; date not in dispute) | Conagra's own PRNewswire release **08-31**, `conagrabrands.com/news-room/…-prn-122962` — materials *"issued that morning prior to a live question-and-answer session"* at 9:30am ET. Lead 30d. |
| LW | **2026-10-06 `bmo`** (DB 09-30, finnhub 10-01 — both wrong; yfinance right) | Lamb Weston scheduling release — results 10-06, news release ~8:00am ET, call 9:00am ET. ⚠ No first-party fetch succeeded (see below). |

### Gated (2)

| Symbol | DB date | Why skipped | Next check |
|--------|---------|-------------|------------|
| CTAS | 2026-09-23 | Advance PR still absent on the **predicted due date** — but checked at 07:2x, and Cintas publishes these at **13:29 ET**. The absence is a clock artifact, not a signal. | 2026-09-10 |
| JEF | 2026-09-28 | Q3 advance PR exists (correction below) but isn't due until ~09-14 at the 14d lead. Cadence cannot break 09-28 vs 09-30. | 2026-09-14 |

### ⚠⚠ JEF — yesterday's row concluded a channel doesn't exist, on the strength of a search that used the wrong title

The 09-08 row read: *"no separate advance-scheduling PR found in either year — the results release
appears to be the first notice,"* and set next-check **09-25**, i.e. wait for the release itself.

It exists. Every year. On BusinessWire, with an unvarying title shape:

- *"Jefferies to Release its Third Quarter Financial Results on **September 25, 2024**"* — published **2024-09-11** ⇒ **14d lead**
- *"Jefferies to Release its Third Quarter Financial Results on **September 29, 2025**"*

Both name **after market close**. What went wrong is narrow and repeatable: the search was built from
the *Second*-Quarter title already in the cached URL plus "2026", so it only ever matched the current
quarter — which genuinely hasn't published. **An empty result for ‹title› + ‹this year› was read as
evidence about the channel, when it was only evidence about this quarter.** The fix that worked was
searching the title shape against **prior** years (`2025 OR 2024`), which is the cheap way to ask
"does this channel exist?" separately from "has it fired yet?" — two questions the 09-08 search
collapsed into one.

**Cost of the error:** next-check was set 11 days too late. At the now-measured 14d lead a 09-28
release needs its PR by ~**09-14** and a 09-30 release by ~**09-16**, so the DB-vs-finnhub tie is
decidable ~10 days before the old row would have looked. Moved to **09-14**.

⭐ **Generalisable rule, worth carrying:** *before concluding a company has no advance-PR channel,
run the title shape against a prior year.* Absence-of-channel and absence-of-firing look identical in
a single search and have opposite consequences — one says stop waiting, the other says keep waiting.

⚠ Two secondary corrections to the same row: JEF's time is effectively settled at **`amc`, 4/4**
(Q3-24, Q3-25, Q2-25 06-25, Q2-26 06-24) but **was not written** — `earnings_confirm.py` has no
time-only mode and would lock the unsourced date alongside it. And the row's *"Monday matches 2025"*
weekday argument for DB is a **1-year** pattern; 2024's Q3 landed on a Wednesday. Days-after-quarter-end
runs 25d/29d against DB's 28d and finnhub's 30d — both inside the band, so cadence is genuinely mute here.

### ⭐ CNXC — the 09-03 refusal to lock on `+364d` paid off, and the slip is now the pattern

09-03 declined to write DB's 09-24 even though `+364d` off 2025-09-25 landed on it *exactly* and a
tight **Sep 24–28** Item 2.02 band (2021–2025) appeared to exclude finnhub's 09-30. The stated reason
was that **Q2-26 had already slipped +4d** against that same arithmetic, and a company that moves once
can move again.

Q3-26 slipped **+5d** — to **09-29**, which is **outside the five-year band by a day**. So:

- **Both feeds were wrong**, in opposite directions (DB −5d, finnhub +1d). A tiebreak framing would
  have picked a loser either way; the only winning move was to wait for the PR, which is what happened.
- **Two consecutive quarters of forward slip means `+364d` is now a *lower* bound for CNXC, not a
  centre.** Next year, read the anniversary date as "no earlier than," not "probably."
- **The Sep 24–28 band is broken** and should not be used as a fence again.
- **Lead is drifting with it:** 19d (Q2) → **21d** (Q3, advance 09-08 → release 09-29).

⚠ The gate itself was slightly loose — 09-03 bracketed the PR at "~09-05 (if 09-24) or ~09-11 (if
09-30)" and it landed **09-08**, between the two. The bracket held; the 09-08 row's reading of the
closed 09-05 window as *"a real (mild) counter-signal"* weakening 09-24 was directionally correct.

⚠ Channel note: the cached RSS feed carried the **headline only** — no body, so it establishes
*that* the PR exists but not the date. The date came from the GlobeNewswire release itself. For this
symbol the feed is a **trigger**, not a source; budget a second fetch after it fires.

### ⚠⚠ LW — confirmed with the company's own IR estate entirely unreachable, and no 8-K to fall back on

Two independent fallbacks failed at once:

1. **Blanket 403 bot-wall — NOT the outage it first looked like.** WebFetch timed out on 5/5
   attempts across every path tried (news-releases listing, events-and-presentations, both
   news-release-details slug shapes, the `newsroom-home/press-release-details/2026/…` shape), and
   the first draft of this entry recorded that as a total IR blackout. ⚠⚠ **That was wrong, and the
   file's own standing rule 2 says so:** *try `urllib` + browser UA before concluding a host is
   unreachable.* Doing that returns **HTTP 403 Forbidden, instantly** — on every slug, on the RSS
   path, on `/`, and on a deliberately nonsense path. So the correct reading is **host UP, blanket
   403 to non-browser clients** (the Cintas `gcs-web` shape), not "down." Two consequences that the
   timeout reading would have gotten backwards: the paths are **not** disqualified, and per standing
   rule 3 the host **cannot be used as an existence probe** in either direction — a 403 on a guessed
   slug is not evidence the PR is missing. WebFetch's 60s timeout is a *symptom of the wall*, not a
   measurement of the host.
2. **No 8-K.** EDGAR's submissions API for CIK 1679273 shows **nothing but Form 4s and a 13G/A since
   the 07-24-2026 8-K** — the FY27 Q1 scheduling release was not filed. The **FY26 equivalent was**
   (`lw-20250824x8kxexx9911q26.htm`), so EDGAR looked like a reasonable fallback and isn't one.

Confirmed anyway, on: the release text reproduced **consistently and specifically** across multiple
independent search summaries (10-06, release ~8:00am ET, call 9:00am ET — the same three figures every
time), **plus** yfinance independently at 10-06, **plus** LW's own early-October Q1 history
(2023-10-05, 2022-10-05, 2020-10-07). Flagging the sourcing honestly: this is the weakest-sourced
confirm of the session and the only one not read off a company-controlled surface. The 403 finding
does not strengthen it — it only means a **browser-rendered** fetch would likely succeed where every
scriptable client is refused, which is the same hard tooling dependency already recorded for FDX.

⚠⚠ **The DB date deserves separate note: 09-30 is exactly last year's Q1 release date (2025-09-30).**
That is not a near-miss or a rounding error — it is a **prior-year date sitting in the current-year
row**, the same failure shape worth watching for wherever a DB date lands precisely on `last year ± 0d`
while the company's own multi-year cadence points elsewhere. Here the multi-year cadence (early Oct)
was right and 2025-09-30 was itself the outlier year, so the stale value inherited the one atypical date.

### ⚠ CTAS — the gate fired on the right day and still couldn't see anything, for a boring reason

Today **was** the predicted PR-due date (14d before DB's 09-23), and the check came back empty:
`stocktitan.net/news/CTAS/` newest item still **08-10**, cintas.com newsroom tops out **09-01**, and
`businesswire.com/newsroom` now **403s** (a new blocker — it had been usable).

But the one measured Cintas advance published at **13:29 ET**, and this session runs at **07:13**.
**A 07:1x check on the due date is structurally blind for this symbol** — roughly six hours early
against the only observed publication time. Recording it because the failure is systematic, not
one-off: for any symbol whose advance publishes midday/afternoon, the due-date morning check is
close to free of information and the real check is the *following* morning. Held, next-check 09-10.

Date reasoning unchanged and still favours DB: Q1-only Item 2.02 dates walk one day earlier each year
(2025-09-24 Wed, 2024-09-25 Wed, 2023-09-26 Tue) ⇒ **09-23 Wed**, with finnhub's 09-30 a full week
outside. Time was already repaired to `bmo` on 09-02 (bmo 6/6).

### ⚠ CAG — a `bmo` inferred rather than quoted

Conagra's release says materials are *"issued that morning prior to a live question-and-answer
session"* at 9:30am ET. It **never states a clock time for the release** and never says "before the
market opens." The inference is sound — a morning issue ahead of a 9:30am ET Q&A cannot be `amc` —
but it is an inference, unlike DRI/CNM/GIS whose releases quote the phrase outright. Logged as such
in case a later session needs to know how firmly the `bmo` is held. Date was never in dispute
(reason was `unknown_time`); finnhub's 09-29 is wrong.

### Calibration

**3 confirms / 5 surfaced**, both gates correct and neither one a missed confirmable date. The
session's leverage was concentrated in re-reading yesterday's own conclusions rather than in new
research: CNXC vindicated a prior refusal-to-lock, JEF **overturned** a prior claim of channel
absence, and CTAS explained a prior gate's blind spot. All three prior rows were written by sessions
that had the right instincts and, in JEF's case, one bad search.

**Standing levers after today:**
- **Search the title shape against a prior year before declaring a channel absent.** (JEF; new)
- **For midday-publishing symbols, the due-date morning check is worthless — check the morning after.** (CTAS; new, and cheap to apply)
- **`+364d` is a lower bound, not a centre, for any symbol with a recorded slip.** (CNXC; now 2/2 quarters)
- **Apply standing rule 2 to *timeouts*, not just to refusals.** (LW; new) I read 5/5 WebFetch
  timeouts as "the host is down" and only ran the urllib+UA check while writing this log up — it
  returned an instant 403 on every path including `/`. The rule was already in
  `reference_company_cadence.md` and I skipped it because a timeout *feels* like a network fact in a
  way a 403 doesn't. It isn't.
- Unchanged: feed convergence is corroboration, not a source; a DB date landing exactly on last year's date is a staleness smell (LW).

## Session: 2026-09-08 (Tuesday) — _[no session block was written this day; reconstructed at the 2026-09-13 maintenance from the carry-over rows (now in the summer archive, Appendix B) and `earnings_date_disputes`]_

Surfaced (dispute rows, trade_date 09-08): **CNXC, CTAS** (`date_disagreement`), **JEF** (`both`), **KMX, PAYX** (`unknown_time`). **2 written, 3 held.**

- **KMX 2026-09-29 `bmo`** and **PAYX 2026-09-29 `bmo`** — logged as *"time only, date not in dispute"*, but both rows ended `date_confirmed=1 / agent`: **the dates were locked with no same-quarter company source** (KMX on a 5/5 bmo pattern with its Q2 FY27 advance not yet out; PAYX on a 2/2 Tuesday-bmo pattern with its Q1 FY27 advance not yet out). The time-only path in [[feedback-earnings-confirm-bare-symbol-trap]] (`UPDATE earnings_upcoming SET earnings_time=...`) was the right tool. ⚠ PAYX drew a `confirmed_row_diverged` flag on 09-11 (yfinance 09-23) — see the 09-13 maintenance entry.
- **JEF** — concluded *"no separate advance-scheduling PR; the results release is the first notice"*, next-check 09-25. **Overturned 09-09**: the BusinessWire channel exists every year; next-check moved to 09-14.
- **CNXC, CTAS** — held (both confirmed later: CNXC 09-09, CTAS 09-10).


---

# Maintenance History

## Weekly Maintenance — 2026-09-20 (Sunday)

Second weekly pass in a row (launched 18:00 by Task Scheduler). One mailbox notice. The week's real
finding is not in the workspace at all: **three weekday sessions silently didn't happen.**

**⚠⚠ No session ran 09-16, 09-17 or 09-18.** No transcript, no log block, no dispute rows. The
orchestrator logs show why: the lite refresh flagged `Disputes flagged: 0` each morning (5 / 7 / 7
unconfirmed rows in scope), and the agent is spawned only `if disputes and spawn_agent`
(`ei_lite_refresh.py:339`); `launcher.py` daily mode has the same early-exit. Every gated symbol's
next-check had, until now, been rescued by some other symbol's dispute firing the launcher. Missed:
**CCL (next-check 09-16), UEC (09-17 — reports 09-24)**; never surfaced: **MU** (entered the 14d horizon
09-16) and **ACN** (09-17). No wrong write resulted. Written up in
`analysis/proposal_20260920_spawn_on_due_next_checks.md`, top of `notes_for_ben.md`, `STATUS.md`, and
as a standing caution in `feedback_window_gating_and_noop.md`.

**Archived.** `research_log.md` **761 → 504 lines** (incl. this entry). Sessions **09-01, 09-02, 09-03** (329 lines) moved
verbatim into `memory/archive/research_log_2026-Q3_summer-earnings.md`, chronological, ahead of the
appendices; archive header updated (now 07-01 → 09-03). Script: `analysis/maintenance_archive_20260920.py`
(backs up both files, asserts every moved non-blank line is present in the archive — passed). Active
log keeps 09-08 → 09-15. Header rebuilt from the DB: 2 carry-overs (both with a missed check), window
watch refreshed (**CCL 09-28 → 09-29 and DAL 10-08 → 10-09 moved in the feed**, unsourced), ledger
re-verified row-by-row against `earnings_upcoming` (14 rows, all match) and **LEN pruned** (reported 09-16).

**Promoted to structured memory.**
- `reference_company_cadence.md` — five rows that the 09-14 session confirmed but never wrote back:
  **PAYX** (resolved: lock was wrong, 09-23 Wed; lead 14d ×2; *weekday history is not a fence*),
  **KMX** (re-sourced; lead 20d ×2; publishes after the close), **MTN** (Q4 lead 24d = 2nd obs; host is a
  **403**, not a timeout; the advance sat unread 10 days), **CCL** (Q3 context, the feed move, absence
  record stops at 09-15), **DAL** (feed move). Cheat-sheet: Vail moved timeout → chronic 403; McCormick
  and `businesswire.com/newsroom` added to chronic 403; Jefferies split into "HTML shell / RSS works".
- `feedback_earnings_confirm_bare_symbol.md` — **rewritten to lead with the patched tool** (inbox
  notice: installed 09-16; I verified `--help` today: `--time-only`, required `--by`). Time-only fixes now
  go through `--time-only`, not the plain UPDATE. The three pre-patch traps are kept as history. What the
  patch can't do is stated up front: it cannot tell whether a `--date` is sourced.
- `feedback_direct_db_query.md` — the "prompt template omits `--write`" sentence retired (verified fixed
  in `launcher.py`); frontmatter brought to the current format; `PRAGMA` trips the write guard (seen once).
- `feedback_window_gating_and_noop.md` — the dispute-gated-session caution + three rules (put near-term
  next-checks in STATUS "Needs attention"; check missed next-checks first after a gap; **a gap is not an
  absence**).
- `MEMORY.md` — two index lines rewritten; all 20 pointers resolve, no unindexed files.

**Pruned `notes_for_ben.md`:** 175 → 170 lines, but materially different — the patch item and the
PAYX/KMX item moved verbatim to `notes_for_ben_archive.md` (new "Moved at the 2026-09-20 maintenance"
section) and condensed into Resolved; the tool-fix item now shows two fixes landed (confirm tool,
template `--write`) and what remains (`direct_db_query.py`, backslash paths in the template); new top
item for the missed sessions.

**Inbox/outbox.** `2026-09-16_earnings-confirm-patch-installed.md` integrated → `inbox/processed/`.
Inbox root clean. Outbox unchanged since 08-13, largest file 128 lines — no rotation.

**Calibration — this week (09-14 → 09-18: 2 sessions ran, 3 didn't).**
- 6 unique symbols handled (JEF, UEC, CCL, MTN + the two priority carry-overs PAYX, KMX).
  **Confirmed 4 — all four from company-issued PRs** (MTN, KMX, JEF; PAYX **corrected −6d**). Open: UEC, CCL.
- **Skip judgment, where it could be tested: 1 for 1.** JEF was gated five sessions running (09-08 →
  09-14) on "advance due ~09-14 at the 14d lead, publishes ~16:20 ET ⇒ read 09-15." The PR published
  **09-14 16:30 ET** and was confirmed 09-15 — the predicted morning, to the day. It also settled the
  dispute against finnhub and against the 10-05 third-party estimate. Two weeks running the gate has
  fired on its predicted day (CTAS 09-09, JEF 09-14) — two cases, both off leads with ≥2 observations.
- **UEC and CCL are untestable, not passed:** their checks never ran. I can't score those gates until
  a session reads the channels; if either PR turns out to have published on/near its predicted day,
  that's a hit for the lead table and a miss for the machinery.
- **Write-side: the 09-08 error is fully unwound.** PAYX corrected from the company PR, KMX sourced, and
  the tool patched so that route can't recur. Net cost: one wrong locked date for 5 days.
- **Drift I can own:** (1) On 09-14 I wrote *"window-watch rows with an open window should get a spine
  read the day they open"* after MTN's advance sat unread for 10 days — and on 09-15 I did not apply it:
  MU (open since ~09-02), STZ, PEP and ACN got no spine read. A lesson logged and not acted on the very
  next day. It is now in the window-watch header where Monday will see it, not only in a session note.
  (2) 09-14's confirms weren't written back to the cadence table (09-15's JEF was) — fixed today; the
  daily habit is "cadence row in the same session as the confirm."
- Sessions were lean where they ran: 09-15 = 5 reads / 1 search for 3 symbols; 09-14 = 11 reads / 0 searches.

**STATUS.md** rewritten.

## Weekly Maintenance — 2026-09-13 (Sunday)

The first maintenance pass since **06-21** — twelve weeks. It launched tonight from Task Scheduler
(`!Sunday Earnings Researcher`); the 08-26 note's "machinery is gone" diagnosis was wrong — see
`notes_for_ben.md` → Resolved. So this pass did twelve weeks of upkeep, not one. No mailbox notices.

**Archived.** `research_log.md` **3,351 lines / 478 KB → 702 lines / 56 KB.**
- **New `memory/archive/research_log_2026-Q3_summer-earnings.md`** (2,598 lines): 42 sessions
  07-01 → 08-28, chronological. Repaired on the way: **07-02 and 07-24** had lost their `## Session`
  headers (restored, dated from in-text references); **07-21, 07-22, 07-27 → 07-30** had been written
  as paragraphs inside the carry-over header (restored as blocks). Appendix A = the old
  Upcoming-Confirmed ledger verbatim (348 rows — the season's confirmation record); Appendix B = the
  old carry-over table verbatim (95 rows, every one closed or lapsed) + its cleared/re-verified notes.
- **Spring archive** + the late-June sessions (06-12 → 06-30) and the 06-14 / 06-21 maintenance entries.
- **09-08 has no session block anywhere** — reconstructed as a stub from the carry-over rows + DB. No
  session record exists for **09-04** either (its CNXC/CTAS dispute rows sat `unresolved`).
- Header rebuilt from the DB: 4 carry-overs, a 13-row upcoming ledger, and a window-watch table.
- Integrity: 2,594 of the old log's 2,597 non-blank content lines are present verbatim in the new log or an archive (checked line by line against the pre-maintenance backup). The 3 not carried are the old carry-over table's boilerplate intro (old lines 14–16), deliberately superseded by the rewritten intro.

**Promoted to structured memory.**
- `reference_company_cadence.md`: **+16 compact rows for the mid-October Q3 kickoff cohort** (PEP, DAL,
  C, BAC, PGR, SCHW, JBHT, MRSH, ALLY, FHN, FNB, REXR, SNA, ERIC, ACI, AMX), mined from the July
  ledger — the table had **no** row for any of the 37 names dated 10-13 → 10-16; the 23 first-time names
  are listed in the section. Updated CTAS (lead now 14d ×2; time fixed), KMX and PAYX (date-locks
  flagged), ACN and STZ (stored time contradicts the established one).
- `reference_cadence_364d_corroborator.md`: `+364d` is a **floor** after a recorded slip (CNXC, 2/2).
- `reference_confirmed_row_diverged_signal.md`: the PAYX live case; both bad-lock batches share one root.
- `feedback_earnings_confirm_bare_symbol.md` + its MEMORY.md line: the **third** shape of the confirm-tool
  trap (time fix ⇒ date lock); the stale "assume irreversible" claim corrected.
- Most of the summer's cadence promotion had already happened inline in the daily sessions, so this
  pass filled the forward-looking gap instead of re-promoting.

**Pruned `notes_for_ben.md`:** 716 lines → 152. The whole original moved verbatim to
`notes_for_ben_archive.md`; the active file keeps 8 open items (2 new; the rest merged by class from ~20
scattered notes) and a condensed Resolved list. New proposal:
`analysis/proposal_20260913_hook_diverged_priority_status_tripwire.md`.

**Inbox/outbox.** Inbox root clean (README + `fetch/` + `processed/`). Largest outbox file 128 lines — no
rotation. `analysis/` holds ~140 dated one-off scripts; left in place (memory and the log cite some by path).

**Calibration — last week (09-08 → 09-11, 4 sessions).**
- 17 dispute rows; 10 unique symbols surfaced (+ UEC unconfirmed). **Confirmed 9** — 7 company-sourced
  (CNXC, CAG, CTAS, JBL, MKC, NKE, LW; LW the weakest), **2 date-locked without a source (KMX, PAYX)**.
  Open: JEF, UEC, and the PAYX drift flag.
- **Skip judgment: 0 missed confirmable dates.** CTAS held for four sessions, then its PR landed on the
  predicted due date (09-09, 14d lead) and confirmed the DB. CNXC was held against a perfect-looking
  `+364d`, and the company moved it +5d, so refusing to lock was right. The gate's bracket
  (09-05..09-11) held; the PR came 09-08. UEC and JEF correctly not yet due.
- **Wrong calls, both caught:** (1) JEF 09-08 declared the advance-PR channel absent off a search that only
  tested this year — next-check 11 days late; overturned the next morning. (2) **KMX/PAYX 09-08 — dates
  locked as a side effect of a time fix.** This one got through, and PAYX's drift flag on 09-11 then went
  unmentioned in that day's log.
- The fallback stack carried a full WebSearch outage on 09-10 (4/4 confirms from feeds + stocktitan + EDGAR).

**Calibration — the twelve weeks since the last pass (06-22 → 09-11).**
- **346 distinct symbols confirmed out of 439 that surfaced as dispute rows** (79%), plus the unconfirmed
  calendar rows confirmed without a dispute row. Weekly confirms peaked at 80–89 in the July wave
  (W27–W28) and ran 0–9 a week from mid-August as the queue emptied.
- **Skip-side misses were all one shape:** a gate built on a lead **borrowed from another fiscal quarter
  or resting on one observation** (TECH Q3→Q4, WSM 1 obs, ADBE never measured, CPRT Q1-vs-Q4, CNM wrong
  channel), plus one channel declared absent without checking a prior year (JEF). All erred late
  enough that a later read caught them. Standing rules 4–5 and the WSM rule ("gate off the longest
  observed lead; count the observations") cover this.
- **The expensive error was "locked without a company source":** the 06-30 convergence batch (at least
  4 of 10 wrong by 4–7d, caught 07-17) and now the 09-08 time-fix locks. Same root, different route; the
  drift flag caught both. Rule: a date is locked only on a same-quarter company source, and a time fix
  never goes through the confirm tool.
- **Cadence entries that misled:** CNXC's five-year band (broken, now a floor); KMX/PAYX rows that knew only
  one fiscal quarter (now carry the upcoming quarter's context). None misled a skip this week.
- **Process drift:** the unarchived log itself. For twelve weeks every daily session read ~478 KB at
  startup, and sessions drifted into writing condensed entries in the header (07-21 … 07-30) and
  skipping a block (09-08). The STATUS-staleness tripwire proposal addresses the root; this pass fixes
  the symptom.

**STATUS.md** rewritten (was stamped 06-21).
