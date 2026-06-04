# Earnings Research Log

> Active log: full sessions for the last ~2 weeks (newest first, below). Older
> sessions rolled off to `memory/archive/research_log_2026-Q2_spring-earnings.md`.
> Maintenance notes at the very bottom. Per-symbol cadence/lead-times live in
> `memory/reference_company_cadence.md` (the data behind window-gating + next-check).

## Open Carry-Overs — unresolved, with next-check dates

Symbols skipped recently because no company-issued source exists *yet*. Next-check ≈
`earnings_date − lead_time − buffer` (see `reference_company_cadence.md`). Don't burn
cycles before the next-check date — the advance PR can't exist yet.

| Symbol | DB date | Status | Next check |
|--------|---------|--------|------------|
| ORCL | 2026-06-10 amc | No Q4 FY26 "Sets the Date" PR/8-K yet (EDGAR shows only CFO 8-K 04-06 + board 8-K 05-12); PR historically ~June 3 → release ~06-11/16. finnhub 06-16 is aggregator-only. | 2026-06-03 |
| JBL | 2026-06-16 bmo | No Q3 FY26 "Earnings Announcement Set" PR yet (latest IR = Q2 release 03-18; last-yr Q3 PR 06-03 → 06-17 report). Aggregators 06-18 BO; DB 06-16. | 2026-06-03 |
| UEC | 2026-05-28 unk ⚠ | **DB date = today and impossible.** UEC files Q3 10-Q with no advance PR ~early-mid June (last-yr 06-02 / 06-06). Can't authoritatively replace. Flagged to Ben (8+ sessions). | 2026-06-04 |
| GME | 2026-06-09 unk | No Q1 FY26 8-K/PR (EDGAR FTS=0, filings = eBay Form 425 noise); minimal advance notice, reports ~06-09/10 AMC. finnhub 06-08. | 2026-06-05 |

Horizon — surfaced before but outside their window; **don't research yet**: ACN 06-18, DRI 06-18. Re-check ~06-08 onward. (LEN→confirmed 06-11, KMX→confirmed 06-17 on 05-29.)

## Upcoming Confirmed — locked dates (don't re-research)

One line per confirmed symbol whose earnings date is still upcoming (≥ 2026-05-28).
Full prose detail is in the session it was confirmed (active log below, or the season
archive). Times: bmo = before market open, amc = after market close.

| Symbol | Date | Time | Source — confirmed |
|--------|------|------|--------------------|
| ADSK | 2026-05-28 | amc | adsknews.autodesk.com — 05-05 |
| BBY | 2026-05-28 | bmo | investors.bestbuy.com — 05-08 |
| DELL | 2026-05-28 | amc | investors.delltechnologies.com — 05-08 |
| DLTR | 2026-05-28 | bmo | corporate.dollartree.com — 05-11 |
| GAP | 2026-05-28 | amc | gapinc.com — 05-08 |
| HRL | 2026-05-28 | bmo | hormelfoods.com — 05-13 |
| KSS | 2026-05-28 | bmo | investors.kohls.com — 05-11 |
| MDB | 2026-05-28 | amc | investors.mongodb.com (Yahoo mirror) — 05-11 |
| NTAP | 2026-05-28 | amc | BusinessWire — 05-13 |
| OKTA | 2026-05-28 | amc | BusinessWire — 05-07 |
| PATH | 2026-05-28 | amc | ir.uipath.com — 05-13 |
| S | 2026-05-28 | amc | GlobeNewswire — 05-08 |
| TD | 2026-05-28 | bmo | td.mediaroom.com — 05-13 |
| HPE | 2026-06-01 | amc | BusinessWire — 05-13 |
| CAVA | 2026-06-02 | amc | MarketBeat/Nasdaq (aggregator-only — re-verify near date) — 04-24 |
| DG | 2026-06-02 | bmo | BusinessWire — 05-12 |
| GTLB | 2026-06-02 | amc | SEC 8-K (05-11) — 05-14 |
| PANW | 2026-06-02 | amc | investors.paloaltonetworks.com — 05-14 |
| ULTA | 2026-06-02 | amc | BusinessWire — 05-20 |
| AVGO | 2026-06-03 | amc | investors.broadcom.com — 05-14 |
| CRWD | 2026-06-03 | amc | BusinessWire — 05-13 |
| FIVE | 2026-06-03 | amc | GlobeNewswire — 05-21 |
| MDT | 2026-06-03 | bmo | news.medtronic.com — 05-14 |
| PVH | 2026-06-03 | amc | pvh.com (Yahoo mirror) — 05-20 |
| VEEV | 2026-06-03 | amc | ir.veeva.com — 05-14 |
| CIEN | 2026-06-04 | bmo | ciena.com — 05-14 |
| COO | 2026-06-04 | amc | GlobeNewswire — 05-14 |
| DOCU | 2026-06-04 | amc | StockTitan — 05-21 |
| GWRE | 2026-06-04 | amc | BusinessWire — 05-22 |
| LULU | 2026-06-04 | amc | corporate.lululemon.com — 05-21 |
| TTC | 2026-06-04 | bmo | BusinessWire — 05-22 |
| CPB | 2026-06-08 | bmo | thecampbellscompany.com — 05-26 |
| MTN | 2026-06-08 | amc | investors.vailresorts.com / stocktitan — 05-26 |
| SJM | 2026-06-09 | bmo | investors.jmsmucker.com — 05-14 |
| CNM | 2026-06-10 | bmo | coreandmain.com (own domain; WebFetch 403 → curl-only, uncached) — 05-29 |
| ADBE | 2026-06-11 | amc | adobe.com/investor-relations.html — 05-29 |
| LEN | 2026-06-11 | amc | newsroom.lennar.com — 05-29 |
| KMX | 2026-06-17 | bmo | investors.carmax.com — 05-29 |
| KR | 2026-06-18 | bmo | ir.kroger.com — 05-29 |

---

# Research Sessions (newest first)

## Session: 2026-05-29 (Friday) — 07:17 AM ET

Big shift from the last several sessions: the advance scheduling PRs that were missing all week finally dropped, so this was a **5-confirm session** (vs 0 on 05-26/27/28). Confirmed CNM, ADBE, LEN, KMX, KR — all from primary/company sources. Skipped ORCL, GME, JBL (still no company-issued date).

**⚠ Hook/DB mismatch — flagged to Ben.** The injected `<dispute-list>` named 5 symbols (ORCL, GME, CNM, ADBE, LEN) but `earnings_date_disputes` for 2026-05-29 has **7 rows**: CNM, GME, JBL, KMX, KR, LEN, ORCL. ADBE was injected as "unconfirmed-but-undisputed" (not in the dispute table); **JBL, KMX, KR were never injected** despite being real unresolved disputes. The session prompt also said "7 symbols." I researched all 7 DB disputes + ADBE. Net: 3 symbols (JBL/KMX/KR) would have been silently dropped if I'd trusted only the injected list.

### Confirmed (5)

| Symbol | Date | Time | Source — confirmed |
|--------|------|------|--------------------|
| CNM | 2026-06-10 | bmo | coreandmain.com/news (own domain) — "will issue its financial results for the first quarter ended May 3, 2026, before the market opens on Wednesday, June 10, 2026." Resolved `unknown_time`. **IR URL not cached** — WebFetch 403s the page (only loads via curl + browser UA). |
| ADBE | 2026-06-11 | amc | adobe.com/investor-relations.html — "Upcoming events: Thursday, June 11, 2026 — Q2 FY2026 earnings call 2:00pm Pacific Time" (= 5pm ET = AMC). Date+time already matched DB; now confirmed. IR cached (note: WebFetch timed out, read via curl). |
| LEN | 2026-06-11 | amc | newsroom.lennar.com (05-28 PR) — "the Company will release its second quarter 2026 earnings after the market closes on June 11, 2026 … conference call on June 12, 2026 at 11:00 a.m." Date+time matched DB. IR cached (press-releases listing). |
| KMX | 2026-06-17 | bmo | investors.carmax.com (05-28 PR) — "will report its financial results for the first quarter ended May 31, 2026 before the market opens on June 17, 2026 … conference call … at 8:00 a.m. ET." **Correction: DB time amc → bmo.** Date matched; finnhub 06-19 was wrong. IR cached. |
| KR | 2026-06-18 | bmo | ir.kroger.com — "host its first quarter 2026 earnings conference call at 8:00 a.m. ET on Thursday, June 18, 2026" (8am call ⇒ results out pre-market = BMO; Kroger always reports BMO). Resolved `unknown_time`; date matched DB+finnhub. IR cached. |

### Skipped (3) — no authoritative company-issued source yet

| Symbol | DB date | Note |
|--------|---------|------|
| ORCL | 06-10 amc | No "Sets the Date for Q4 FY2026" PR or 8-K yet. EDGAR shows only a CFO-appointment 8-K (04-06) and a board-addition 8-K (05-12) — neither sets the date. finnhub 06-16 is aggregator-only; DB 06-10 unverifiable. Oracle's advance PR historically ~early June → release ~06-11/16. |
| GME | 06-09 unk | No Q1 FY2026 8-K/PR. GameStop reported Q4 FY25 on 03-24 *without* a conference call — minimal advance notice. Aggregators split (DB/06-09 vs finnhub/06-08). No company source. |
| JBL | 06-16 bmo | No "Third Quarter FY2026 Earnings Announcement Set" PR yet (latest IR item is the Q2 release from 03-18; last-yr Q3 PR was 06-03 for a 06-17 report). Aggregators say 06-18 BO; DB 06-16. Advance PR imminent — re-check ~06-03. |

### Notes
- **Validation of next-check logic:** CNM (next-check 06-01), ADBE (06-01) both became confirmable today, slightly ahead of schedule — their advance PRs dropped 05-21→05-28. The carry-over windowing is calling it about right.
- **IR access patterns this session:** ir.kroger.com and investors.carmax.com loaded cleanly via WebFetch. adobe.com/investor-relations.html and newsroom.lennar.com/press-releases timed out on WebFetch (read via curl) but were cached anyway as canonical pages. coreandmain.com 403s WebFetch entirely — **only reachable via curl with a browser User-Agent**; left uncached per the don't-cache-403 rule. businesswire.com 403s curl but loads via WebFetch (inverse of coreandmain) — used CarMax's own IR domain instead.
- ORCL/GME/JBL are the same "reports mid/late June, advance PR hasn't dropped" pattern as the rest of the week — all three should be researchable within ~1 week.

## Session: 2026-05-28 (Thursday) — 07:18 AM ET

Processed 5 symbols (1 date_disagreement, 2 unknown_time, 2 unconfirmed). Confirmed 0, skipped 5 (ORCL, CNM, GME, UEC, ADBE). Same shape as 05-26/05-27: every symbol is an early-to-mid-June reporter whose company-issued advance scheduling PR hasn't dropped yet — plus GME (issues minimal advance notice) and UEC (no advance-PR pattern; DB date is today and is wrong). Inbox had 10 pre-staged SEC files (filings JSON + 8-K HTML + EDGAR FTS JSON for ORCL/UEC/CNM/GME) — looks like leftover curl output from a prior session; used and moved to `inbox/processed/`.

### Skipped (5) — no authoritative company-issued source