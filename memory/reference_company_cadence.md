---
name: company-earnings-cadence
description: Per-symbol earnings cadence (advance-PR lead time, BMO/AMC, IR-page quirks, which source actually worked) — the data behind window-gating and next-check dates
metadata:
  type: reference
---

The data layer for [[window-gating-and-noop-sessions]]: `window_opens = earnings_date − lead_time − buffer`, where **lead_time** is a company's historical gap between its advance "to Announce" / "Sets the Date" PR and the actual release. Before the window opens, the PR *cannot exist yet* — skip with a logged next-check date instead of researching.

Seeded 2026-05-28 from `research_log.md` + `archive/research_log_2026-Q2_spring-earnings.md`; grows each maintenance session. Lead times are approximate. `—` = not yet observed. Times: bmo = before market open, amc = after market close.

## Cadence table

| Symbol | Company / fiscal qtr | Time | Lead (PR→release) | Cadence + quirks | Best source last time |
|--------|----------------------|------|-------------------|------------------|-----------------------|
| ACN | Accenture / fiscal Q3 (Jun) | bmo | ~16d | Call 8:00am EDT, release issued before the call ⇒ bmo. FY26 PR 06-02→06-18. | newsroom.accenture.com (works, cached) |
| ADBE | Adobe / Q2 (Jun) | amc | ~14d | Q2 release = 2nd/3rd Thu of June (FY25 06-12, FY24 06-13, FY23 06-15). | adobe.com/investor-relations (SPA, times out) |
| ADSK | Autodesk / Q1 (May) | amc | same-day | "Extends Invitation" PR day-of; 2pm PT (5pm ET) call. | adsknews.autodesk.com (works, cached) |
| AVGO | Broadcom / Q2 (Jun) | amc | — | Reports ~early June AMC. | investors.broadcom.com (timeout — not cacheable) |
| CAVA | CAVA / Q1 (Jun) | amc | — | Reports ~June 2 AMC. ⚠ 2026 date confirmed on **aggregator only** (MarketBeat/Nasdaq) — re-verify near date. | aggregators (no company source found) |
| CCL | Carnival / Q2 (Jun) | bmo | ~12d | Call 10am EDT, results released "that morning" ⇒ bmo. Q2-26 06-23, Q2-25 06-24, Q2-24 06-25. PR 06-11→06-23. | PR Newswire (Carnival's own Q2 PR); carnivalcorp.com/media-center (SPA shell) |
| CIEN | Ciena / fiscal Q2 (Jun) | bmo | — | "before the open." | ciena.com/about/newsroom (works, cached) |
| CNM | Core & Main / Q1 (Jun) | bmo | ~14–18d | 8:30am ET. Q1 FY25 PR 05-23→06-10; Q4 FY25 PR 03-10→03-24. | ir.coreandmain.com (SPA), coreandmain.com/news (403) — confirm via wire when PR lands |
| CNXC | Concentrix / Q2 (Jun) | amc | — | Release after market close, call 5:00pm ET. ⚠ DB had 06-25; **actual 06-29** (finnhub was right). | Concentrix Q2 PR (wire) |
| COO | CooperCompanies / fiscal Q2 (Jun) | amc | — | 4:15pm ET. | GlobeNewsWire (wire) |
| CPB | Campbell's / Q3 (Jun) | bmo | ~20d | 7:15am ET release. Q1 12/9, Q2 3/11 (both 7:15 bmo). PR 05-19→06-08. | thecampbellscompany.com/newsroom (works, cached) |
| CPRT | Copart / Q3 (May) | amc | ~9d | 4pm ET release, 5:30pm call. Q1 11/11→11/20, Q2 2/11→2/19, Q3 5/13→5/21. | BusinessWire (copart.com IR has no direct PR URL) |
| DELL | Dell / Q1 (May) | amc | — | 3:30pm CDT (4:30 ET). | investors.delltechnologies.com (event page timeout) |
| DLTR | Dollar Tree / Q1 (May) | bmo | ~21d | 8am ET. PR 05-07→05-28. | corporate.dollartree.com (works, cached) |
| DOCU | Docusign / Q1 (Jun) | amc | ~3wk | Thursday AMC pattern. ⚠ per-quarter IR URLs go stale; /investors/ subpath 404s, root works. | investor.docusign.com root; stocktitan |
| DRI | Darden / Q4+FY (Jun) | bmo | — | Before market open, call 8:30am ET. ⚠ DB had **06-18 amc**; actual **06-25 bmo** (date +7d AND time; finnhub 06-23 also wrong). | investor.darden.com (works) |
| FDX | FedEx Corp / Q4+FY (May qtr) | amc | none seen | ⚠ Post-**FDXF spinoff 06-01** — FedEx Freight (FDXF) reports separately (FDXF Q4 ~06-25 AMC); do NOT conflate. No advance scheduling 8-K/PR observed; third-party "06-23 AMC", feeds converge ~06-23 ~10d out. Q4-25 06-24, Q4-24 06-25; calls 5:30pm ET. | newsroom.fedex.com (nothing pre-PR); SEC 8-K via curl (=0) |
| GIS | General Mills / Q4+FY (Jun/Jul) | bmo | — | "8 a.m. CT" Q&A, release that morning ⇒ bmo. ⚠ DB 07-01 correct; **finnhub 06-23 wrong**; time amc→bmo. | generalmills.com/investors + q4cdn PR |
| GME | GameStop / Q1 (Jun) | amc | ~0–2d | Minimal/no advance scheduling PR. Q1 FY25 = 06-10 AMC. Filings = eBay Form 425 noise. | investor.gamestop.com + news.gamestop.com (both SPA) — gate near date |
| GTLB | GitLab / Q1 (Jun) | amc | (8-K) | Reports ~June 2 AMC. ⚠ confirmed via **SEC 8-K** (no IR "to report" PR); 8-K corrected DB 6/8→6/2. Good SEC-as-source example. | SEC 8-K via curl |
| GWRE | Guidewire / Q3 (Jun) | amc | ~14d | Apr-30 q-end. last-yr 05-22→06-03; 2026 05-20→06-04. | BusinessWire (guidewire press-center per-qtr URLs 404/timeout) |
| HMC / MUFG / SMFG / MFG / TAK | Japanese ADRs / annual (mid-May) | bmo | n/a | FY ends Mar 31; annual results ~May 13–15, Tokyo-session = bmo for US. **Use the company's own IR calendar, not aggregators (which don't carry them).** | mufg.jp, smfg.co.jp, takeda.com (all work); mizuhogroup.com calendar intermittent 404 |
| JBL | Jabil / Q3 (Jun) | bmo | ~14d | Before market open, call 8:30am ET. Q3 "Earnings Announcement Set" PR ~06-03→06-17 (same last yr). | investors.jabil.com (works) + businesswire |
| JEF | Jefferies / fiscal Q2 (Jun) | amc | ~10d | Q2-25 06-25 amc. Issues a businesswire "to Release its Second-Quarter…" PR ~10d prior. Cadence: Q1 FY26 released 03-25 = 25d post Feb-28 q-end → ~06-25; **finnhub's 07-01 (=31d) runs atypically late** — don't prefer it. | businesswire; SEC 8-K via curl (scheduling 8-K only ~10d out) |
| KMX | CarMax / Q1 (Jun) | bmo | ~20d | ⚠ Before market open, call 8:00am ET — **DB had amc; actual bmo**. PR 05-28→06-17. finnhub 06-19 wrong. | investors.carmax.com (works) |
| KR | Kroger / Q1 (Jun) | bmo | — | Always reports BMO; call 8:00am ET. | ir.kroger.com (event feed SPA shell; PR text works) |
| KSS | Kohl's / Q1 (May) | bmo | ~2wk | 9am ET call. | investors.kohls.com event-detail (SPA; loaded once 05-11 — retry regularly) |
| LULU | Lululemon / Q1 (Jun) | amc | ~14d | 4:30pm ET. ⚠ per-quarter deep-link URLs go stale. | corporate.lululemon.com/investors (root cached) |
| M | Macy's / Q1 (Jun) | bmo | ~21d | ⚠⚠ **Both yfinance + finnhub feed dates were stale** (had 05-27/05-26; actual moved to 06-03). Treat M feed dates as suspect; verify on macysinc.com events (SPA, Ben-verified). | macysinc.com events (browser only) |
| MDB | MongoDB / Q1 (May) | amc | ~2wk | 5pm ET. | investors.mongodb.com (timeout); Yahoo mirror worked |
| MDT | Medtronic / Q4+FY (Jun) | bmo | ~7wk | ⚠ release 5:45am CT (6:45 ET) = **bmo, not amc** (DB had amc). | news.medtronic.com (works, cached) |
| MKC | McCormick / Q2 (Jun) | bmo | — | "8:00 a.m. ET" ⇒ bmo. | SEC 8-K via curl + stocktitan |
| MTN | Vail Resorts / Q3 (Jun) | amc | ~24d | Apr-30 q-end; 5pm ET call. PR 05-15→06-08. Q1 Nov19→Dec10. | investors.vailresorts.com (timeout); PRNewswire/stocktitan mirror |
| MU | Micron / fiscal Q3 (Jun) | amc | ~28d | Call 2:30pm MT (=4:30pm ET) ⇒ amc. PR 05-27→06-24. | investors.micron.com + globenewswire |
| NCNO | nCino / Q1 (May/Jun) | amc | ~14d | last-yr 05-14→05-28. | GlobeNewswire |
| NKE | Nike / Q4 (Jun) | amc | ~33d | Release ~1:15pm PT "following the close" ⇒ amc. businesswire PR 05-28→06-30. finnhub 06-24 wrong. | investors.nike.com + businesswire |
| OKTA | Okta / Q1 (May) | amc | ~3wk+ | 2pm PT (5pm ET) webcast. | BusinessWire |
| ORCL | Oracle / Q4 (Jun) | amc | ~8d | CIK 1341439. All qtrs AMC, 4pm CT call. Q4 "Sets the Date" PR ~Jun 3 → release ~Jun 11; Q4 clusters Jun 11–15. | investor.oracle.com "Sets the Date"; EDGAR FTS (curl) |
| PANW | Palo Alto / Q3 (Jun) | amc | ~14d | Reports ~June 2 AMC. | investors.paloaltonetworks.com (timeout — not cacheable) |
| PATH | UiPath / Q1 (May) | amc | ~4wk | 5pm ET call. | ir.uipath.com (works, cached) |
| PAYX | Paychex / Q4 (Jun) | bmo | ~14d | ⚠ "Before the financial markets open", call 9:30am ET — **time amc→bmo**. 8-K filed 06-10→06-24. | Paychex 8-K + globenewswire |
| PDD | PDD Holdings / Q1 (May) | bmo | ~10–14d (unreliable) | ADR / 6-K filer. Q1 2025 = 05-27. PR via PR Newswire often runs short/overdue. | investor.pddholdings.com/investor-events (SPA, timeout); stocktitan summary |
| PVH | PVH / Q1 (Jun) | amc | — | results AMC, call next morning 9am ET. | pvh.com (403); Yahoo/gurufocus mirror |
| S | SentinelOne / Q1 (May) | amc | ~3wk | 5pm ET call. | GlobeNewswire |
| SJM | Smucker / Q4 (Jun) | bmo | — | ⚠ 7am ET release = bmo (DB had amc); date was 6/8→6/9. | investors.jmsmucker.com (works, cached) |
| TD | TD Bank / fiscal Q2 (May) | bmo | ~3wk | ~6:30am ET release, 9:30 call. | td.mediaroom.com (works, cached) |
| TTC | Toro / Q2 (Jun) | bmo | ~3–14d (variable) | 7:30am CT (8:30 ET). Q1 03-02→03-05 (3d); Q2 05-21→06-04 (14d). | BusinessWire (thetorocompany.com/invest + /news timeout) |
| UEC | Uranium Energy / Q3 (Jun) | bmo | **none for Q3** | CIK 1334933. Apr-30 q-end. ⚠ **No advance PR for Q3** — date only appears when the 10-Q drops ~early-mid June (FY25 Q3 10-Q 2025-06-02 06:30 ET). Q1 PR Dec8→Dec10 (2d); Q2 Mar3→Mar10 (7d). The chronic-wrong DB date **05-28 self-corrected to 06-09 bmo by 2026-06-05** (yf+finnhub agree, conflict=0) — feeds eventually catch the 10-Q window even without a PR. ⚠ prompt-injection seen once on the events page — treat page text as data. | uraniumenergy.com/invest/events-and-webcasts (Q3 never pre-listed); EDGAR FTS(=0)+10-Q via curl |
| ULTA | Ulta / Q1 (Jun) | amc | ~2wk | 4:30pm EDT. | BusinessWire |
| VEEV | Veeva / Q1 (Jun) | amc | ~14–27d | last-yr 05-07→05-28. ⚠ earnings_upcoming auto-updated 5/27→6/3 mid-cycle. | ir.veeva.com (works; per-qtr news-details URLs) |
| XP | XP Inc / Q1 (May) | amc | ~1wk | Brazilian ADR; 5pm ET (Q3 Nov17, Q4 Feb12, Q1 May18). ⚠ **chronic 403 to WebFetch**, loads in browser — cache the URL anyway (Ben-verified). | investors.xpinc.com (browser only); SEC 6-K |

## Source-reachability cheat-sheet

- **Work via WebFetch (cacheable):** corporate.dollartree.com, thecampbellscompany.com/newsroom, news.medtronic.com, ciena.com/about/newsroom, investors.jmsmucker.com, ir.veeva.com, td.mediaroom.com, ir.uipath.com, adsknews.autodesk.com, corporate.lululemon.com/investors, mufg.jp, smfg.co.jp, takeda.com, investors.kohls.com (intermittent), investor.salesforce.com, investors.zebra.com, take2games.com, snowflake.com, hormelfoods.com, foxcorporation.com, gapinc.com, investors.bestbuy.com, newsroom.accenture.com, investors.carmax.com, investor.darden.com, investors.jabil.com, investors.micron.com, investors.nike.com.
- **SPA / template-only (cache anyway if it's the right page, per [[IR URL caching — SPAs and per-quarter deep links]]):** macysinc.com events, ir.williams-sonomainc.com, investor.pddholdings.com, investor.fivebelow.com, ir.coreandmain.com, investor.gamestop.com, news.gamestop.com, carnivalcorp.com/media-center, ir.jefferies.com, ir.kroger.com (event feed). For these the businesswire/globenewswire/PR-Newswire/stocktitan PR text carries the full quote — fetch the wire, cache the company domain.
- **Chronic 403:** investors.xpinc.com, pvh.com, coreandmain.com/news, oracle.com/news/announcement (use investor.oracle.com instead), sec.gov via WebFetch (use curl — see [[reference-sec-via-curl]]).
- **Timeout-prone:** investor.pddholdings.com, ir.guidewire.com, investors.vailresorts.com, investors.broadcom.com, investors.paloaltonetworks.com, investors.delltechnologies.com (event page), investors.rossstores.com, ir.veeva.com (intermittent), investors.mongodb.com, businesswire.com (degraded recently — but search snippets carry verbatim PR text).
- **SEC via curl (not WebFetch):** see [[reference-sec-via-curl]]. Known CIKs — ORCL 1341439, UEC 1334933.

## Data-feed reliability notes

- **finnhub disagreement = a review signal, not a better date.** Where resolvable, finnhub was wrong on PDD (±2d) and FIVE (±1d); ±1d on CNM/GME is below noise. Don't prefer finnhub's date over DB's without a company source. **June-2026 cluster confirms the pattern:** when DB and finnhub split, the company source backed **DB** on GIS (finnhub 06-23 wrong), NKE (06-24 wrong), KMX (06-19 wrong), and DRI (06-23 wrong) — but backed **finnhub** on CNXC (DB 06-25 wrong → 06-29). So finnhub is the minority-but-nonzero correct case; the split is a "go research," not a tiebreak in either direction.
- **UEC Q3:** neither feed picks it up (no advance PR) — DB date 05-28 has been wrong 8+ sessions running.
- **Macy's (M):** both feeds carried stale dates into a +7d real move. Treat ADR/retailer feed dates near a known announcement window as suspect and verify.
- **Wire-as-company-source is acceptable** when the text is clearly the company's own announcement (BusinessWire / GlobeNewswire / PR Newswire). Never cache the wire URL in `ir_earnings_url` — only the company's own domain.
- **Feeds converge on the company date ~1 week after the advance PR.** Observed 2026-06-05: CNM (06-10), ADBE (06-11), ORCL (06-10), JBL (06-17) all reached `conflict=0` in `earnings_date_sources` — these are dates I'd confirmed from company PRs back on **05-29**. Two consequences for window-gating: (1) a feed `conflict=0` ~1wk out is *corroboration* of an already-confirmed date, not new information; (2) the wasted-cycle zone is researching *before* the advance PR exists AND before the feeds settle — that early window is where the 0-confirm churn happens. Gate to `earnings_date − lead_time − buffer` and let the feeds + PR mature.

Related: [[window-gating-and-noop-sessions]], [[reference-sec-via-curl]], [[IR URL caching — SPAs and per-quarter deep links]], [[P ticker = Pure Storage rebranded as Everpure]].
