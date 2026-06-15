# Earnings Research Log — Archive: 2026 Spring Earnings Season

> Spring 2026 earnings season — Q1 calendar results (and the fiscal quarters
> reported in this wave), announced ~mid-Apr through mid-May 2026. Rolled off the
> active `research_log.md` during the 2026-05-28 weekly maintenance session.
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