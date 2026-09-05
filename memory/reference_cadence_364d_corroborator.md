---
name: cadence-364d-weekday-aligned-corroborator
description: The SEC 8-K filingDate +364d weekday-aligned check corroborates dates for fixed-weekday filers — but it went 3-for-6 against company sources, and it fails precisely when yfinance disagrees with DB
metadata:
  type: reference
---

Take a symbol's **same-quarter, year-ago Item 2.02 8-K `filingDate`** and add **364 days** (= 52 weeks, so the weekday is preserved). For companies on a fixed weekday cadence, that lands on the current-year date **exactly**. It costs zero extra web calls — the `filings.recent` JSON you already pull for [[sec-8k-acceptance-time-as-timing-source]] carries `filingDate`, so date-corroboration and time-derivation come out of the *same* fetch.

## Why this got upgraded from "guard" to "corroborator"

It entered the workflow (2026-07-15) as a **defensive** check — a way to avoid stamping `date_confirmed=1` on a wrong date when writing a time. On **2026-07-28** it was run over 11 symbols *before* any company source was in hand, and then two of those symbols (**MCHP**, **HD**) turned up authoritative company sources later the same session. The `+364d` prediction had been **exactly right on both**. Same session, it backed DB to the day on **HRB 08-11, AAP 08-13, MNST 08-06, TOL 08-18, EXPD 08-04** as well.

That is a real predictive track record, not a tautology — but see the limits below before leaning on it.

## ⚠⚠ Then it went 3-for-6. The 2026-07-30 correction — read this before quoting the record above

On **2026-07-30**, five symbols that had carried confident `+364d` predictions got company sources. The check was **wrong on three of them**, and in each case it had been used the day before to write "⇒ DB" in the carry-over table:

| Symbol | `+364d` said | Company PR said | Error |
|--------|--------------|-----------------|-------|
| **GO** | 08-04 (= DB) | **08-12** (GlobeNewswire 07-29) | **−8d** |
| **GRAL** | 08-11 (= DB) | **08-05** (grail.com 07-29) | **+6d** |
| **ZM** | 08-20 (= DB) | **08-25** (GlobeNewswire 07-28) | **−5d** |
| HRB | 08-11 (= DB) | 08-11 ✓ | 0 |
| MCHP / HD (07-28) | ✓ ✓ | ✓ ✓ | 0 |

**2026-07-31 update — it is now 3-for-7, and AAP moved from the "hit" column to the "miss" column.** AAP had been cited above (07-28) as a `+364d` success backing DB's 08-13. Advance Auto's own BusinessWire PR (07-30) says **Thursday 2026-08-20 bmo** — a **−7d miss**. The trap was sharper than the others: by 07-31 the DB itself had already moved to 08-20 (matching yfinance), and `+364d` was used to "correct" a *correct* DB row back to 08-13. That write had to be reverted the same session.

| Symbol | `+364d` said | Company PR said | Error |
|--------|--------------|-----------------|-------|
| **AAP** | 08-13 (year-ago Thu 2025-08-14) | **08-20** (BusinessWire 07-30) | **−7d** |

AAP was a *textbook* precondition match — Thursday-bmo every quarter for years, weekday-aligned prediction, no obvious regime change — and it still missed, because a company can simply slip a week. **If the strongest-looking case in the table can fail, the precondition test is not doing any work.**

So the honest record is **3 right / 4 wrong**, not 2-for-2. Worse, the three misses were *confident and weekday-aligned* — the arithmetic gave no hint it was failing. **ZM shows why:** Zoom looks like a fixed-weekday filer quarter-to-quarter but isn't — Q3 lands Monday, Q4 Tue/Wed, Q2 has been Wed, Thu, and now Tue. The "fixed-weekday filer" precondition is much rarer than it looks, and **there is no cheap way to test it from the filing dates alone** (a company can be weekday-stable for 4 quarters and still move).

## 2026-08-03 — the largest single-day sample so far: 14 hits, 2 misses

Sixteen symbols got company sources in one session, so this is the first time the check was scored against a batch rather than a trickle. It was **exact on 14** and wrong on two:

| Symbol | `+364d` said | Company source said | Error |
|--------|--------------|---------------------|-------|
| **ARE** | 2026-07-20 | **2026-08-03** (investor.are.com PR) | **−14d** |
| **AME** | 2026-07-30 | **2026-08-04** (investors.ametek.com PR) | **−5d** |

Cumulative record ≈ **17 right / 6 wrong**. Two things worth noting, and they pull in opposite directions:

1. **The >4d guard caught both misses in advance.** Neither would have been written blind — the guard flagged ARE at +14d and AME at +5d off the DB date, which is precisely the "re-research before writing" trigger. The guard is doing more useful work than the prediction is.
2. **Both misses ran in the same direction — the company moved *later* than cadence.** That matches AAP (−7d), GO (−8d) and ZM (−5d); of the six recorded misses, **five predicted a date earlier than reality**. There is no mechanism claimed here, but as a working prior: **when `+364d` disagrees with DB by pointing *earlier*, distrust the prediction, not the DB.**

ARE is also a reminder that "it was flagged before" is not the same as "it was fixed": this exact symbol was flagged at **+14d on 2026-07-15** for the same reason, and the arithmetic is still 14d off a year later — Alexandria simply moved its Q2 release from late July to early August and stayed there. **A stale prediction does not self-correct as the year-ago anchor rolls forward, if the anchor year is itself the outlier.**

## 2026-08-04 — 13 scored in one session, and the directional prior went 7-for-7

The largest same-day scoring yet, because 14 rows claimed to report that session and their company sources all landed at once. **6 exact, 7 wrong — and every single one of the 7 misses predicted a date EARLIER than reality.**

| Symbol | `+364d` said | Company source said | Error |
|--------|--------------|---------------------|-------|
| CAT / CMI / DUK / DVA / DVN | 08-04 | 08-04 | 0 ✓ ×5 |
| **CG** | **08-05** (DB said 08-04) | **08-05** | **0 ✓ — and it beat DB** |
| BRBR | 08-03 | 08-04 | −1d |
| BRKR | 08-03 | 08-04 | −1d |
| OKTA | 08-25 | 08-26 | −1d |
| APTV | 07-30 | 08-04 | −5d |
| **WDAY** | 08-20 (= DB) | **08-27** | **−7d** |
| DOC | 07-23 | 08-04 | −12d |
| **PANW** | 08-17 | **09-01** | **−15d** |

**Cumulative ≈ 23 right / 13 wrong.** More useful than the ratio: **12 of the 13 recorded misses predicted earlier than reality.** The 07-31 working prior ("when `+364d` disagrees with DB by pointing *earlier*, distrust the prediction") is now the single most reliable thing this check produces — it has not failed since it was written.

### ⚠ The asymmetry is now sharp enough to state as a rule

- **`+364d` earlier than DB ⇒ distrust the prediction, not DB.** 12 of 13 misses live here. Companies drift *later* (extra reporting days, merger overhead, calendar creep); they rarely move earlier.
- **`+364d` later than DB ⇒ rare, and worth taking seriously.** **CG is the first clean case**: cadence said 08-05, DB said 08-04, Carlyle's own PR said **08-05**. Until now this file said `+364d` "is not evidence that DB is right" — CG shows the converse is the useful half: **a `+364d` that points later than DB is a real flag on the DB row.** Note CG had **no dispute row at all** — no feed challenged it — so cadence was the *only* signal that anything was wrong. Same shape as the MSI catch.

### PANW is the worst miss on record, and it shows the precondition test is worthless

−15d, on a symbol this file already listed as "not a fixed-weekday filer." Palo Alto's Q4 landed **2026-09-01**, a full two weeks after the year-ago anchor, because its fiscal Q4 reporting slot simply moved. Every non-company source was wrong too (DB 08-18, finnhub + all aggregators 08-24); **only yfinance had 09-01.** This is the [[confirmed-row-diverged-signal]] asymmetry in its purest form and the strongest evidence yet for the "which feed dissents" rule below — cadence, DB and finnhub agreed with each other and were *all three* wrong.

## ✅ The one rule worth keeping: look at *which feed* disagrees

The misses and the hits separate cleanly on a signal that costs nothing:

- **Only finnhub disagrees with DB** ⇒ `+364d` backing DB has held up (HRB 08-11, and the whole +7d-artifact family: TOL, CSCO, RDW, TECH…). finnhub's week-shift is a real artifact and cadence exposes it correctly.
- **yfinance disagrees with DB** ⇒ **treat DB as the suspect side and do not let `+364d` talk you out of it.** On GO, GRAL and ZM, yfinance had the right date and `+364d` + DB were both wrong.
- **⚠ Corollary added 2026-07-31 (AAP): when the DB row has *already moved onto* yfinance's date, `+364d` must not be used to move it back.** The dispute row is a snapshot taken when the conflict was live; the calendar row can update underneath it, so `earnings_confirm.py`'s `(was: …)` output is the current truth, not the dispute list. If `(was: …)` shows a date you did not expect, **stop and re-research before writing** — that mismatch is itself the signal that the feeds have converged on something newer than the dispute row. yfinance appears to track the company PR within a day or so of publication, which is exactly the information `+364d` cannot have.

This is the same asymmetry recorded in [[confirmed-row-diverged-signal]] (yfinance-earlier-than-a-stale-confirm ⇒ probable wrong date), arriving from the other direction.

### ⚠⚠ 2026-08-11 (LI) — the first clean counterexample to the finnhub rule: **magnitude matters**

Li Auto's own advance PR (08-11 04:30 ET) says **2026-08-26 bmo**. DB had **08-27**. `+364d` off LI's year-ago Q2 results 6-K (2025-08-28) returns **08-27 — the DB date exactly**. finnhub was alone at **08-26**, and **finnhub was right**.

Read literally, the rule above ("only finnhub disagrees ⇒ `+364d` backing DB has held up") would have dismissed the one correct source in the room. The fix is not to drop the rule — its whole track record is the **+7d week-shift artifact** (TOL, CSCO, RDW, HRB, NCNO, HPQ, NTNX, P…) — but to condition it on the **size of the gap**:

- **finnhub dissents by ~±7d** (or lands on an off-pattern weekday) ⇒ the artifact. `+364d` + DB win; this has never failed.
- **finnhub dissents by ±1–2d** ⇒ **not** the artifact, and the rule says nothing. Check it properly. A one-day gap is what a real schedule change looks like, and neither DB nor `+364d` can see one.

Note the second half of the trap: this is a **6-K filer**, which the hard-limits section already flags as a blind spot — but the anchor still produced a confident, DB-matching, weekday-aligned number, exactly the shape that reads as corroboration. **A known-blind case does not announce itself in the output.** If the symbol is on the 6-K list at the bottom of this file, the arithmetic is decoration, not evidence, no matter how well it agrees with DB.

Cumulative ≈ **23 right / 14 wrong**.

### ⚠⚠ 2026-08-17 (PVH) — an **−8d miss with no dissenting feed at all**, and the only tell was an overdue PR

PVH's own advance PR (08-17 09:00 ET) says **2026-09-02 amc**. DB had **08-25**. `+364d` off the
2025-08-26 Item 2.02 returns **08-25 — the DB date exactly**, Tue→Tue, weekday-aligned, textbook
precondition match. Both wrong by **8 days**.

What makes this the most instructive miss on record is not the size, it's the **silence**: PVH
surfaced as an `unconfirmed` calendar row, **not a dispute** — finnhub and yfinance did not
dissent, so the "which feed disagrees" rule above had *no input to run on*. Every signal in this
file's toolkit either agreed with the wrong date or was unavailable.

**The one signal that pointed at the truth was not arithmetic — it was the missing advance PR.**
PVH's lead is a measured 15–16d off a verified channel, so by 08-17 the PR for an 08-25 release
was **7 days overdue**, and that absence was real evidence (the channel's existence for the
matching quarter was verified — the [[window-gating-and-noop-sessions]] test PVH passes).

⚠ But note the limit, because it cuts both ways: the overdue PR correctly said *"08-25 is
wrong"* and gave **no** reliable read on what was right — the session's stated hypothesis
(09-01) was also wrong, because PVH kept its Monday PR and 16d lead while moving the release
weekday Tue→Wed. **Lateness licenses distrust of the existing date, never a replacement for it.**

Cumulative ≈ **23 right / 15 wrong**. Practical addition to the standing status: when a row is
`unconfirmed` with **no feed dissent**, `+364d` agreement is worth *less*, not more — there is
no independent check on it, and PVH shows the two can be wrong together. Ask instead: **is this
company's advance PR overdue against a verified lead?**

## Standing status

Demote it back to what it was on 2026-07-15: a **defensive sanity guard** for not stamping `date_confirmed=1` on an unsourced date, and a **tie-breaker against finnhub only**. It is *not* evidence that DB is right, and a `+364d`-backed date should never shorten a next-check or justify skipping a search when a company PR is due. On 07-30 the three misses were all caught by a plain WebSearch that would have run anyway.

## What it is good for

- **Breaking DB-vs-finnhub ties in the right direction.** finnhub's known **+7d week-shift artifact** is exactly what `+364d` is built to expose: on 07-28 it caught HRB (finnhub 08-18 vs cadence/DB 08-11) and TOL (08-25 vs 08-18). It also flags *off-weekday* feed dates — AAP's finnhub 08-17 is a **Monday** for a company that reports Thursday-bmo every quarter.
- **Finding wrong dates nothing else can see.** A DB date on the *wrong weekday* for that company's cadence is a strong tell. **CELH** on 07-28: DB 08-10 is a **Monday**, but Celsius has reported Wed/Thu bmo for 9 straight quarters and `+364d` gives 08-06 — so DB was the suspect side and finnhub's 08-05 the better one. This is the same shape as the MSI catch (07-15), where **no feed challenged a wrong DB date at all**.

## ⚠ Hard limits — do not lock a date on this alone

- **It is corroboration, never a source.** Same standing rule as feed convergence: it does not license `date_confirmed=1`. On 07-28 all 7 cadence-backed dates were still recorded `skipped`, and only MCHP/HD were confirmed — because those two had *company* sources.
- **It breaks precisely when a company changes its reporting regime, and it breaks silently** — it will confidently return an old-regime date. **FLO is the worked example**: Flowers Foods reported Friday ~07:1x (bmo) through 2025-08-15, then switched to Thursday ~16:1x (amc) from 2025-11-06. `+364d` from the year-ago Q2 returns **08-14, a Friday** — an old-regime date that DB had also swallowed. The real date is ~**08-20 (Thu)**. So: **check the furnish-time pattern for a regime change before trusting the date arithmetic** — the same recency rule that governs bmo/amc governs this. The two checks share a failure mode and should be read together.
- Blind to **6-K filers** (foreign private issuers — no `items` field, often no fixed weekday): CCEP, YPF, JD, SE, NU, XP, SQM, XPEV, DNN, **LI, NIO, PDD, BIDU, BABA**. ⚠ Blind does **not** mean silent — see the LI case above, where the anchor returned a confident DB-matching date and was wrong. Blind to companies filing **no Item 2.02 8-K at all** (**NNE** puts results straight in the 10-Q).
- Fiscal-calendar companies that shift a week for 53-week years, or move a release around a holiday, will be off by ~7d legitimately.

Related: [[sec-8k-acceptance-time-as-timing-source]] (same fetch, same recency caveat), [[company-earnings-cadence]] (where per-symbol weekday patterns live), [[window-gating-and-noop-sessions]], [[reference-sec-via-curl]].
