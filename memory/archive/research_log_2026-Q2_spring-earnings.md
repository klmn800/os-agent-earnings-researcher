# Earnings Research Log — Archive: 2026 Spring Earnings Season

> Spring 2026 earnings season — Q1 calendar results (and the fiscal quarters
> reported in this wave), announced ~mid-Apr through late June 2026. Rolled off the
> active `research_log.md` during weekly maintenance sessions (2026-05-28 onward).
> Sessions below are in chronological order (oldest first).

---

## Session: 2026-04-23 (Thursday)

Processed 50 disputes. Confirmed 42, skipped 8 due to insufficient / conflicting data.

### Confirmed (42)

_[⚠ The body of this 04-23 session was truncated by the 2026-06-04 workspace
restore (archive went 849 lines → 524 bytes). The confirmed-symbol detail is
unrecoverable; the confirmation ledgers in the active log's header tables survived.
See `notes_for_ben.md` → Resolved.]_

---

## Session: 2026-05-28 (Thursday) — 07:18 AM ET

Processed 5 symbols (1 date_disagreement, 2 unknown_time, 2 unconfirmed). Confirmed 0, skipped 5 (ORCL, CNM, GME, UEC, ADBE). Same shape as 05-26/05-27: every symbol is an early-to-mid-June reporter whose company-issued advance scheduling PR hasn't dropped yet — plus GME (issues minimal advance notice) and UEC (no advance-PR pattern; DB date is today and is wrong). Inbox had 10 pre-staged SEC files (filings JSON + 8-K HTML + EDGAR FTS JSON for ORCL/UEC/CNM/GME) — looks like leftover curl output from a prior session; used and moved to `inbox/processed/`.

### Skipped (5) — no authoritative company-issued source

_[⚠ The rest of this 05-28 session was truncated by the 2026-06-04 workspace restore. The detail is unrecoverable; the confirmation ledgers in the (active-log) header tables are intact. All five skips later resolved correctly — see the 05-29 session below and the 06-07/06-14 calibration notes.]_

---

## Session: 2026-05-29 (Friday) — 07:17 AM ET

Big shift from the last several sessions: the advance scheduling PRs that were missing all week finally dropped, so this was a **5-confirm session** (vs 0 on 05-26/27/28). Confirmed CNM, ADBE, LEN, KMX, KR — all from primary/company sources. Skipped ORCL, GME, JBL (still no company-issued date).

**⚠ Hook/DB mismatch — flagged to Ben.** The injected `<dispute-list>` named 5 symbols (ORCL, GME, CNM, ADBE, LEN) but `earnings_date_disputes` for 2026-05-29 has **7 rows**: CNM, GME, JBL, KMX, KR, LEN, ORCL. ADBE was injected as "unconfirmed-but-undisputed" (not in the dispute table); **JBL, KMX, KR were never injected** despite being real unresolved disputes. The session prompt also said "7 symbols." I researched all 7 DB disputes + ADBE. Net: 3 symbols (JBL/KMX/KR) would have been silently dropped if I'd trusted only the injected list. _(Root cause fixed in Ben's 06-11 dev session — a horizon gate on the disputes query; see `notes_for_ben.md` → Resolved.)_

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
| ORCL | 06-10 amc | No "Sets the Date for Q4 FY2026" PR or 8-K yet. EDGAR shows only a CFO-appointment 8-K (04-06) and a board-addition 8-K (05-12) — neither sets the date. finnhub 06-16 is aggregator-only; DB 06-10 unverifiable. Oracle's advance PR historically ~early June → release ~06-11/16. _(Reported 06-10 as DB had it.)_ |
| GME | 06-09 unk | No Q1 FY2026 8-K/PR. GameStop reported Q4 FY25 on 03-24 *without* a conference call — minimal advance notice. Aggregators split (DB/06-09 vs finnhub/06-08). No company source. _(Reported 06-09.)_ |
| JBL | 06-16 bmo | No "Third Quarter FY2026 Earnings Announcement Set" PR yet (latest IR item is the Q2 release from 03-18; last-yr Q3 PR was 06-03 for a 06-17 report). Aggregators say 06-18 BO; DB 06-16. Advance PR imminent — re-check ~06-03. _(Advance PR dropped; confirmed 06-17 bmo on 06-11.)_ |

### Notes
- **Validation of next-check logic:** CNM (next-check 06-01), ADBE (06-01) both became confirmable today, slightly ahead of schedule — their advance PRs dropped 05-21→05-28. The carry-over windowing is calling it about right.
- **IR access patterns this session:** ir.kroger.com and investors.carmax.com loaded cleanly via WebFetch. adobe.com/investor-relations.html and newsroom.lennar.com/press-releases timed out on WebFetch (read via curl) but were cached anyway as canonical pages. coreandmain.com 403s WebFetch entirely — **only reachable via curl with a browser User-Agent**; left uncached per the don't-cache-403 rule. businesswire.com 403s curl but loads via WebFetch (inverse of coreandmain) — used CarMax's own IR domain instead.
- ORCL/GME/JBL are the same "reports mid/late June, advance PR hasn't dropped" pattern as the rest of the week — all three should be researchable within ~1 week.

---

## Session: 2026-06-11 (Thursday) — 07:16 AM ET

High-volume day and a **clean confirm session**: 13 confirmed, 3 skipped (no company source yet). The advance PRs for almost the whole late-June reporting cluster have now dropped.

**⚠ Hook/DB mismatch — same recurring bug as 05-29 (flagged to Ben again).** The injected `<dispute-list>` named **14** symbols (4 "disputes": CCL, JEF, CNXC, KR; + 10 "unconfirmed-but-undisputed": ADBE, LEN, JBL, KMX, ACN, DRI, FDX, MU, PAYX, MKC). But `earnings_date_disputes` for 2026-06-11 has **6 rows**: CCL, CNXC, GIS, JEF, KR, NKE. So **GIS and NKE — both real, unresolved `date_disagreement` rows — were NEVER injected**, and I'd have missed them entirely if I hadn't read the table directly to write resolutions. Both turned out to need fixes (GIS time, NKE confirm-over-finnhub). Conversely the 10 "unconfirmed" names are NOT in the dispute table (they're datalake-calendar rows that `earnings_confirm.py` updates, no dispute row to resolve — my first DRI `UPDATE ... earnings_date_disputes` hit 0 rows, which is how I noticed). The two lists are assembled from different sources and diverge in *both* directions. _(Root-caused & fixed by Ben in his 06-11 dev session — a `db_date <= today+14d` horizon gate on the disputes query; see `notes_for_ben.md` → Resolved. The defensive every-session cross-check is no longer required, but it's cheap insurance.)_

### Confirmed (13)

Dispute-table rows (resolved → `confirmed_agent` in performance.db):

| Symbol | Date | Time | Source — confirmed |
|--------|------|------|--------------------|
| CNXC | 2026-06-29 | amc | Concentrix Q2 FY26 PR — "release … after market close on Monday, June 29, 2026"; call 5:00pm ET. **DB date 06-25 was wrong** → 06-29 (finnhub had it right). |
| KR | 2026-06-18 | bmo | ir.kroger.com — Q1 call 8:00am ET 06-18 (pre-market ⇒ BMO). Resolved `unknown_time`; date matched DB+finnhub. IR cached. |
| GIS | 2026-07-01 | bmo | generalmills.com/investors + q4cdn PR — "report … on July 1, 2026 … 8 a.m. CT" Q&A; release that morning ⇒ BMO. **DB date 07-01 correct (finnhub 06-23 wrong); time correction amc → bmo.** |
| NKE | 2026-06-30 | amc | investors.nike.com + businesswire (05-28 PR) — "release … June 30, 2026, at approximately 1:15 p.m. PT, following the close" ⇒ AMC. DB 06-30 amc confirmed (finnhub 06-24 wrong). IR cached. |

Datalake-calendar rows (confirmed via `earnings_confirm.py`; no dispute row to resolve):

| Symbol | Date | Time | Source — confirmed |
|--------|------|------|--------------------|
| ADBE | 2026-06-11 | amc | businesswire 06-01 PR — "after market close … Thursday, June 11, 2026", call 2–3pm PT. Matched DB. |
| LEN | 2026-06-11 | amc | newsroom.lennar.com 05-28 PR — release after close 06-11; call 06-12 11am ET. Matched DB. |
| JBL | 2026-06-17 | bmo | investors.jabil.com + businesswire 06-03 PR — "before the market opens", call 8:30am ET 06-17. Matched DB. (Was a carry-over; advance PR has now dropped.) |
| KMX | 2026-06-17 | bmo | investors.carmax.com — Q1 "before the market opens" 06-17, call 8:00am ET. **Time correction amc → bmo.** |
| ACN | 2026-06-18 | bmo | newsroom.accenture.com 06-02 PR — call 8:00am EDT 06-18, "release issued before the call" ⇒ BMO. Matched DB. |
| DRI | 2026-06-25 | bmo | investor.darden.com PR — Q4/FY "before the market opens … June 25, 2026", call 8:30am ET. **DB was 06-18 amc → corrected to 06-25 bmo (date +7d AND time).** |
| MU | 2026-06-24 | amc | investors.micron.com + globenewswire 05-27 PR — call 2:30pm MT (=4:30pm ET) ⇒ AMC. Matched DB. |
| PAYX | 2026-06-24 | bmo | Paychex 8-K (filed 06-10) + globenewswire — "before the financial markets open", call 9:30am ET. **Time correction amc → bmo.** |
| MKC | 2026-06-25 | bmo | SEC 8-K + stocktitan — "8:00 a.m. ET" 06-25 ⇒ BMO. Matched DB. |

### Skipped (3) — no authoritative company-issued source yet

| Symbol | DB date | Note |
|--------|---------|------|
| CCL | 06-24 bmo | Carnival Q2 FY26 (qtr end 05-31). No scheduling 8-K and no first-party IR notice yet (checked SEC submissions + carnivalcorp.com IR pages, both JS-rendered/empty). Historical: reports Q2 late June BMO (Q2-25 06-24, Q2-24 06-25). finnhub 06-22. Left unresolved + noted in dispute row. Recheck ~06-16. _(Confirmed 06-12 when PR dropped — date is 06-23 bmo.)_ |
| JEF | 06-24 amc | Jefferies Q2 FY26 (qtr end 05-31). No scheduling 8-K yet (latest 8-K 04-28); issues a businesswire "to Release its Second-Quarter…" PR ~10d prior — not out yet. Historical Q2-25 was 06-25 AMC. DB 06-24 amc, finnhub 07-01. Left unresolved + noted. Recheck ~06-16. _(Confirmed 06-18 — Business Wire advance dropped 06-16; finnhub 07-01 was wrong.)_ |
| FDX | 06-23 amc | **FedEx Corp** (not FedEx Freight). Note the 06-01 spin-off: FDXF now reports separately (FDXF Q4 set for 06-25 AMC — do not confuse). FedEx Corp Q4 (FY end 05-31): no scheduling 8-K (only spin-off + a debt 8-K) and nothing in newsroom.fedex.com yet. Third-party "expected 06-23 AMC" only; historical Q4-25 06-24, Q4-24 06-25, calls 5:30pm ET. Not in dispute table (datalake-calendar row) — left DB date as-is. Recheck ~06-16. _(Confirmed 06-18 06-23 amc — Ben supplied the rendered IR upcoming-events page.)_ |

### Notes
- **SEC via curl works; WebFetch 403s sec.gov** (per `reference_sec_via_curl.md`). Used `data.sec.gov/submissions/CIK*.json` to enumerate 8-Ks for CCL/JEF/FDX and confirm no scheduling filing exists yet — a fast authoritative "it hasn't dropped" check.
- **IR sites are JS-rendered** (Q4/gcs-web hosts): carnivalcorp.com, ir.jefferies.com, ir.kroger.com event feeds all return shells via WebFetch ("Select year: Loading…"). For the confirmable names the businesswire/globenewswire/stocktitan PR text carried the full quote, so WebFetch on those was enough.
- **DB-write classifier note:** a single batched `--multi` UPDATE of `symbol_metadata` (11 inferred IR homepages) was **denied** by auto-mode as "agent-inferred mass modification, not the dispute workflow." Per-symbol UPDATEs following the documented step-by-step workflow (with verified URLs) are allowed. Cached IR only for KR/NKE (verified-resolving domains); skipped homepage guesses for the rest.
- Carry-overs cleared this session: **JBL** confirmed (advance PR dropped as predicted). ORCL/GME/UEC from last week have since reported (06-09/10).