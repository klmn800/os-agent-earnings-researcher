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
| JEF | 2026-06-24 amc | Jefferies Q2 FY26 (dispute: DB 06-24 vs finnhub 07-01). Still no advance PR as of 06-12 (stocktitan JEF fresh to 06-11, latest news still Q1/March); feeds still split (`conflict=1` @ 06-12). Cadence favors DB: Q1 FY26 released 25d post-quarter-end (→ ~06-25); finnhub's 07-01 = 31d, atypical. Don't lock until Jefferies' businesswire PR drops. | 2026-06-15 |
| FDX | 2026-06-23 amc | **FedEx Corp** (post-FDXF-spinoff 06-01). No company advance PR as of 06-12, but **the feeds have since converged: stored=yf=finnhub=06-23, `conflict=0`** (was third-party-only on 06-11). Per the feed-convergence rule that's corroboration of the third-party 06-23, not a company confirmation — still don't lock without FedEx's own PR. FDXF spinco reports 06-25 — do NOT conflate. Datalake-calendar row, not a dispute. | 2026-06-15 |

(Prior carry-overs all cleared: JBL confirmed 06-11; ORCL/GME/UEC reported 06-09/10; CCL confirmed 06-12.)

## Upcoming Confirmed — locked dates (don't re-research)

One line per confirmed symbol whose earnings date is still upcoming (≥ 2026-06-15).
Reported symbols are pruned each maintenance session; full prose detail stays in the
session it was confirmed (active log below, or the season archive). Times: bmo = before
market open, amc = after market close. (`earnings_date_disputes` exists & persisted
correctly on 06-11/06-12 and is present again this Sunday 06-14 — the 06-07 Sunday-absence
did not recur.)

| Symbol | Date | Time | Source — confirmed |
|--------|------|------|--------------------|
| JBL | 2026-06-17 | bmo | investors.jabil.com / businesswire — 06-11 |
| KMX | 2026-06-17 | bmo | investors.carmax.com — 06-11 |
| ACN | 2026-06-18 | bmo | newsroom.accenture.com — 06-11 |
| KR | 2026-06-18 | bmo | ir.kroger.com — 06-11 |
| FDX? | 2026-06-23 | amc | *unconfirmed* — FedEx Corp, feeds converged 06-23 but no company PR (carry-over) |
| CCL | 2026-06-23 | bmo | Carnival Q2 PR (PR Newswire, 06-11) — 06-12 |
| MU | 2026-06-24 | amc | investors.micron.com / globenewswire — 06-11 |
| PAYX | 2026-06-24 | bmo | Paychex 8-K / globenewswire — 06-11 |
| DRI | 2026-06-25 | bmo | investor.darden.com — 06-11 |
| MKC | 2026-06-25 | bmo | SEC 8-K / stocktitan — 06-11 |
| CNXC | 2026-06-29 | amc | Concentrix Q2 PR — 06-11 |
| NKE | 2026-06-30 | amc | investors.nike.com / businesswire — 06-11 |
| GIS | 2026-07-01 | bmo | generalmills.com/investors / q4cdn PR — 06-11 |

---

# Research Sessions (newest first)

## Session: 2026-06-12 (Friday) — 07:15 AM ET

Quiet day: 3 symbols (1 dispute JEF, 2 unconfirmed-undisputed CCL/FDX). **1 confirmed, 2 skipped** (advance PRs not out yet). All three were carry-overs from 06-11.

**Inbox:** `jef_8k.htm` arrived but was **0 bytes** (failed download — empty placeholder, no content). Moved to `inbox/processed/`. Did not block JEF research; went to source directly.

### Confirmed (1) — datalake-calendar row (no dispute row to resolve)

| Symbol | Date | Time | Source — confirmed |
|--------|------|------|--------------------|
| CCL | 2026-06-23 | bmo | Carnival's own Q2 PR (PR Newswire, issued **06-11**): "conference call … Tuesday, June 23, 2026, at 10 a.m. (EDT)" to discuss Q2 results "expected to be released **that morning**" ⇒ BMO. Matches DB (06-23 bmo). Confirmed via `earnings_confirm.py`; IR URL (carnivalcorp.com/media-center/news-releases) cached. **Cleared from carry-over.** Note: prior carry-over row mis-stated DB date as 06-24 — actual is 06-23. |

### Skipped (2) — no company-issued source yet, stay as carry-overs

| Symbol | DB date | Note |
|--------|---------|------|
| JEF | 2026-06-24 amc | **Dispute** (DB 06-24 vs finnhub 07-01). Jefferies has **not** issued its Q2 advance PR yet (stocktitan JEF current to 06-11 stock data, latest news still Q1/March 25). No scheduling 8-K filed (latest 8-K 04-28). Cadence math favors DB: Q1 FY26 released March 25 = 25d after the Feb-28 quarter-end → ~06-25 for the May-31 quarter; finnhub's 07-01 = 31d, atypically late. **Did NOT lock** — no authoritative source. Left dispute row unresolved. Next check ~06-15. |
| FDX | 2026-06-23 amc | **FedEx Corp** post-FDXF-spinoff (FDXF began trading 06-01). FedEx has **not** issued its FY26-Q4 advance PR (stocktitan FDX latest = 06-08 dividend + board change; the 06-08 8-K is a director election, not earnings). The widely-cited "06-23 AMC" is third-party ("expected") only. **FDXF spinco reports 06-25 — separate company, do not conflate.** Datalake-calendar row, no dispute row. Skipped; next check ~06-15. |

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
| JEF | 06-24 amc | Jefferies Q2 FY26 (qtr end 05-31). No scheduling 8-K yet (latest 8-K 04-28); issues a businesswire "to Release its Second-Quarter…" PR ~10d prior — not out yet. Historical Q2-25 was 06-25 AMC. DB 06-24 amc, finnhub 07-01. Left unresolved + noted. Recheck ~06-16. _(Still open 06-12; carry-over.)_ |
| FDX | 06-23 amc | **FedEx Corp** (not FedEx Freight). Note the 06-01 spin-off: FDXF now reports separately (FDXF Q4 set for 06-25 AMC — do not confuse). FedEx Corp Q4 (FY end 05-31): no scheduling 8-K (only spin-off + a debt 8-K) and nothing in newsroom.fedex.com yet. Third-party "expected 06-23 AMC" only; historical Q4-25 06-24, Q4-24 06-25, calls 5:30pm ET. Not in dispute table (datalake-calendar row) — left DB date as-is. Recheck ~06-16. _(Still open 06-12; feeds since converged 06-23.)_ |

### Notes
- **SEC via curl works; WebFetch 403s sec.gov** (per `reference_sec_via_curl.md`). Used `data.sec.gov/submissions/CIK*.json` to enumerate 8-Ks for CCL/JEF/FDX and confirm no scheduling filing exists yet — a fast authoritative "it hasn't dropped" check.
- **IR sites are JS-rendered** (Q4/gcs-web hosts): carnivalcorp.com, ir.jefferies.com, ir.kroger.com event feeds all return shells via WebFetch ("Select year: Loading…"). For the confirmable names the businesswire/globenewswire/stocktitan PR text carried the full quote, so WebFetch on those was enough.
- **DB-write classifier note:** a single batched `--multi` UPDATE of `symbol_metadata` (11 inferred IR homepages) was **denied** by auto-mode as "agent-inferred mass modification, not the dispute workflow." Per-symbol UPDATEs following the documented step-by-step workflow (with verified URLs) are allowed. Cached IR only for KR/NKE (verified-resolving domains); skipped homepage guesses for the rest.
- Carry-overs cleared this session: **JBL** confirmed (advance PR dropped as predicted). ORCL/GME/UEC from last week have since reported (06-09/10).

---

## Weekly Maintenance — 2026-06-14 (Sunday)

Clean maintenance session. Dispute list suppressed; followed `PROMPT_SUNDAY.md`. The workspace was already in good shape from 06-07, so this was light.

**Archived:** rolled the **05-28** (truncated stub) and **05-29** (5-confirm) sessions off the active log into `memory/archive/research_log_2026-Q2_spring-earnings.md` — both are now >2 weeks old. Active log holds the last 2 weeks (06-11, 06-12) + ledgers. Active log back to ~150 lines. Also added a truncation marker to the archived 04-23 session header (its body was lost in the 06-04 restore).

**Pruned ledgers:** dropped ADBE/LEN (reported 06-11) from the Upcoming-Confirmed table; it now lists only dates ≥ 06-15. Cleared CCL from carry-overs (confirmed 06-12). Carry-overs down to **JEF + FDX**, both next-check Monday 06-15.

**Promoted to memory:** added **13 new symbols** to `reference_company_cadence.md` from the 06-11/06-12 confirm wave (CCL, JEF, FDX, JBL, KMX, ACN, KR, DRI, MU, PAYX, MKC, CNXC, NKE, GIS) with lead times, BMO/AMC, and the DB-vs-finnhub error notes — high-value window-gating data for next year's late-June cluster. Refreshed the source-reachability cheat-sheet (carnivalcorp.com / ir.jefferies.com / ir.kroger.com event feeds are SPA shells; wire text carries full quotes).

**Pruned `notes_for_ben.md`:** moved the dispute-list-mismatch saga (05-29 + 06-11) to **Resolved** (Ben fixed the horizon-gate root cause 06-11); resolved the UEC chronic-date note (self-corrected, no longer recurring); closed the `earnings_date_disputes`-absent-on-Sunday note (table present again this Sunday — did not recur); marked `analysis/weekend_cleanup_proposal.md` **implemented**. Open items now: only the window-gating-in-hook proposal (dev-session item).

**Inbox/outbox:** inbox root clean (README + processed/ only); all outbox files ≤ 65 lines — no rotation.

**Calibration (06-08 → 06-14).** Confirms: **14** (13 on 06-11, 1 on 06-12). Skips that proved to be missed confirmable dates: **0**.
- Last Sunday's 4 carry-overs all resolved correctly: ORCL/GME/UEC reported 06-09/10 (as their feed dates predicted), JBL's advance PR dropped → confirmed 06-17 bmo on 06-11.
- This week's skips held up: **CCL** skipped 06-11 (no PR yet) → confirmable 06-12 when the PR dropped — a clean 1-day-early skip, exactly the intended behavior. **JEF** still split (`conflict=1`), correctly unlocked. **FDX** feeds converged to 06-23 (`conflict=0`) but still no company PR — correctly held as a carry-over, not locked. This is the feed-convergence rule working as designed: convergence is corroboration, not a company source.
- **Standing lever** remains the same — minimize too-early cycles. No new drift this week; the 06-11 session was high-yield (13/16), the opposite of the 05-28 churn problem.

**STATUS.md** updated to match.

---

## Weekly Maintenance — 2026-06-07 (Sunday)

Clean maintenance session. The dispute list was suppressed; followed `PROMPT_SUNDAY.md`.

**Data-loss discovery (the headline).** The git workspace restore (`43c4af6` / `9cb08f1`, ~06-04) truncated two files: the Q2 spring archive (849 → 524 bytes, now ends mid-04-23) and the active log (ends mid-05-28; no 06-01→06-05 session entries survive). Verified the **databases were untouched** — `data/*.db` aren't git-tracked, so `earnings_upcoming` + `earnings_date_sources` are intact and current through the 06-05 feed run. Flagged to Ben in `notes_for_ben.md`; the operational ledgers (header tables, cadence) survived, so weekday work isn't impaired.

**Archived:** nothing — active log is 107 lines, well under the roll threshold.

**Promoted to memory:** updated `reference_company_cadence.md` — UEC entry (chronic-wrong 05-28 date self-corrected to 06-09 bmo by 06-05) and a new feed-reliability note: aggregator feeds converge on the company-confirmed date ~1 week after the advance PR (so a feed `conflict=0` a week out is corroboration, and the wasted-cycle zone is researching before *both* the PR and feed-settle).

**Pruned:** `notes_for_ben.md` — retired the "ran on a Thursday" note (today fired correctly on Sunday); downgraded UEC from urgent to self-resolved; added the restore + missing-`earnings_date_disputes`-table flags. Trimmed the active-log "Upcoming Confirmed" ledger to dates ≥ 06-08 (dropped ~31 already-reported rows). Inbox cleared (6 files → `processed/`). Outbox small; no rotation.

**Calibration (the useful part).** Window 05-28→06-07 is only partially auditable (restore wiped 06-01→05 logs), but the DB tells the real story: by 06-05 the feeds had **converged on every date I confirmed from company PRs on 05-29** — CNM 06-10, ADBE 06-11, ORCL 06-10, JBL 06-17, all `conflict=0`. That's a clean measurement that the researcher's company-source confirmations led the aggregators by ~1 week. No skip proved to be a missed confirmable date (CNM/ADBE skips both confirmed at predicted dates). Skip judgment stays well-calibrated; the open lever remains fewer too-early cycles, now backed by the feed-convergence timing above. Carry-overs ORCL/GME/UEC/JBL all next-check Monday 06-08.

**STATUS.md** updated to match.
