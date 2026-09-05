## Session: 2026-08-25 (Tuesday) — 07:13 AM ET

4 symbols (1 dispute ORCL, 3 unconfirmed-undisputed CPRT/CNM/GME) — **0 confirmed, 4 gated.**
Every date came back "not out yet," and every one of those was the *predicted* answer. The
value of the session is two **channel discoveries**, both of which convert a symbol that had
no readable source into one that has a verified one.

**One EDGAR sweep answered the tripwire question for all four CIKs at once** (CNM 1856525,
CPRT 900075, ORCL 1341439, GME 1326380) — no earnings 8-K pending on any of them. That is the
cheapest possible opening for a 4-symbol morning and it should be the default shape.

### ⭐ CNM — the cadence row was wrong on both the lead and the channel

CNM was the only symbol genuinely *inside* its window today, so it got the real work — and the
stored row turned out to be wrong twice:

- **Channel.** The old note said `coreandmain.com/news` **403s** and "confirm via wire when PR
  lands." Both halves are false. The corporate host serves fine with a browser UA, and it
  publishes a **working WordPress RSS feed at `coreandmain.com/news/feed/`** (10 items,
  current). Meanwhile **there is no wire at all** — CNM's releases carry a bare
  `News Release FOR IMMEDIATE RELEASE` + `ST. LOUIS, <date>—` dateline with no BusinessWire or
  PRNewswire attribution (checked the Q1 FY26 Ex-99.1). The old note would have sent every
  future session wire-hunting for something that does not exist. **IR URL now cached.**
- ⚠ The two Core & Main hosts behave in **opposite** ways and it matters: `ir.coreandmain.com`
  403s *every* path including a nonsense control (bot wall — rule 3, never probe it), while
  `www.coreandmain.com` **404s honestly** (nonsense control verified), so slug probes are sound
  there. ⚠⚠ **The slug alternates between `core-main-` and `core-and-main-`** — my first probe
  tested only one prefix and would have been a false negative. Probe both.
- **Lead.** The stored band "~14–18d" rested on a mis-recorded date (Q1 FY26 advance logged as
  05-23; it was actually **05-27**). Rebuilt from the feed + news pagination, the lead is
  **exactly 14 days, 4/4 quarters**: Q2 FY25 08-26→09-09, Q3 FY25 11-25→12-09, Q4 FY25
  03-10→03-24, Q1 FY26 05-27→06-10. Metronomic, and past the 3-observation bar.
- ✅ **bmo is now structurally locked**: Item 2.02 acceptance is **11:2x–11:3xZ across 21/21
  quarters** back to 2021 (07:2x ET summer / 07:3x ET winter, zero outliers). DB already had bmo.
- ⚠ **A date discrepancy worth remembering:** the news index dated Q2 FY25 results
  *September 08, 2025*, but the 2.02 **and** the advance PR body both say **Tuesday, Sept 9**.
  The WordPress post date can lead the real release by a day — trust the PR body, not the listing.

**So CNM's advance PR is due TODAY (08-25), ~16:2x ET — roughly nine hours after this session
ran.** 14d before the DB's 09-08, posted after the close, exactly the GWRE/ORCL shape. Two
independent checks confirm it is not out yet: the feed's newest item is **07-06**, and both
slug variants 404 against a 200 positive control (Q1 FY26) and a 404 negative control. Held.

### ⭐ CPRT — yesterday's wire correction was itself wrong

Yesterday I recorded "the wire is PRNewswire, not BusinessWire." That was over-generalised from
the wrong PR type: the `/PRNewswire/` dateline came from a **board-addition** PR (Ex-99.1 of the
08-18 8-K). The **earnings advance** PRs are on **BusinessWire**, confirmed at three of the four
known lead dates — `…/20250827727036/en/Copart-Inc.-to-Release-Fourth-Quarter-Fiscal-2025-Results`,
`…20251111618205…First-Quarter-Fiscal-2026…`, `…20260513849390…Third-Quarter-Fiscal-2026…` — every
one matching the cadence table's advance dates exactly. **Corporate PRs → PRNewswire, earnings
PRs → BusinessWire.** The original flat claim and yesterday's correction were both wrong.

This matters beyond bookkeeping: CPRT's next-check is **tomorrow** and it had **no readable
channel at all** (every Copart host NXDOMAIN or bot-walled, advance PR verified absent from
EDGAR). It now has one. The BW `<id>` is unguessable, so the check is an **exact-title search**,
and the **YYYYMMDD prefix of the returned URL is itself the publication date**. Ran that search
today against "Copart, Inc. to Release Fourth Quarter Fiscal 2026 Results": **no hit**, while
prior quarters return cleanly — the channel works and the PR is not out. Consistent with the 8–9d
gate (release 09-03 ⇒ PR 08-25..08-26, after 16:00 ET).

⚠ The search summary volunteered "CPRT will release its next earnings report on Sep 9, 2026" —
that is the same **+6d third-party artifact** finnhub carries, not a company source. Ignored.

### Skipped (4) — all window-gated, none overdue

| Symbol | DB date | Why skipped | Next check |
|--------|---------|-------------|------------|
| CNM | 2026-09-08 bmo | **In window, actively researched — PR genuinely not out.** Feed newest 07-06; both slug variants 404 against a valid positive control. Metronomic **14d** lead ⇒ advance due **today ~16:2x ET**, so the first useful morning read is tomorrow. bmo locked 21/21; date held on cadence only | **2026-08-26** |
| CPRT | 2026-09-03 amc | Advance PR not out — exact-title BusinessWire search returns prior quarters but no Q4 FY26. 8–9d lead ⇒ PR due 08-25..08-26, after 16:00 ET. **Channel identified this session** | **2026-08-26** |
| ORCL | 2026-09-10 amc | EDGAR tripwire clean — **no Oracle 8-K since 2026-07-28** (a Form 4), unchanged from yesterday. Lead 7–9d ⇒ PR due 09-01..09-03, posts ~16:01 ET. Zero Oracle hosts touched. Dispute vs finnhub's 09-14 left **unresolved**, row marked `skipped` | 2026-09-02 |
| GME | 2026-09-08 amc | EDGAR clean — newest 8-K is 08-03 (items 1.01/3.02/8.01, offering-related), no 2.02 and no scheduling filing. GME issues advance PRs inconsistently, so absence is weak evidence either way. amc already locked; date held | 2026-08-31 |

### Housekeeping

- **IR URLs cached (2).** `CNM` → `coreandmain.com/news/feed/` (verified today). `ORCL` →
  `investor.oracle.com/rss/pressrelease.aspx`, stamped **08-21**, the date it was actually last
  verified, not today — the cadence table has had this feed marked ⭐-working for weeks while
  `symbol_metadata` still said `None`, so every dispute list was reporting "Cached IR URL: None"
  for a symbol whose channel we know cold. Worth a sweep: **the cadence table's ⭐ hosts and
  `symbol_metadata.ir_earnings_url` have drifted apart.**
- ORCL dispute row for 08-25 marked `resolution='skipped'`.

### Calibration

0 confirms, but the good kind — 4 gated symbols, 4 correct gates, and **no date locked on
cadence alone** despite CNM's +364d and 14d math both pointing squarely at 09-08. The
lesson that repeats from yesterday: **the spare capacity in a gated session is best spent
auditing the stored channel/lead facts, not re-checking dates that cannot have changed.**
Two sessions running, that audit has found the stored row to be wrong — CPRT's wire yesterday
(and again today), CNM's lead *and* channel today. ⚠ It also produced today's real caution:
**yesterday's "correction" was itself a mis-generalisation from a single non-earnings PR.**
A correction drawn from one document of the wrong type is not a correction. Check the PR *type*
before rewriting a channel note — the same trap as measuring a lead from one quarter (WSM).

