# Notes for Ben

Issues, questions, and findings from the Earnings Date Researcher agent.
**Open** items first, most urgent at the top — each condensed to what is still live, with a pointer
to its full history. Everything else moved **verbatim** to
[`notes_for_ben_archive.md`](notes_for_ben_archive.md) at the 2026-09-13 maintenance (headings are
unchanged there, so the pointers below are searchable); items closed since are appended there each Sunday.

---

## Open

### ❓ Source-accuracy audit, first run: 48 of 50 past confirms fully right. Run it again next Sunday? — 10-11

I checked **every** agent confirm dated 09-01 → 10-09 (n = 50; no sampling) against the company's own
Item 2.02 8-K / results release on EDGAR. **Dates 49/50, times 49/50, 0 unverifiable.** Full table:
`analysis/source_audit_20261011.md`.

| Source type | n | date right | date wrong | time wrong |
|---|---|---|---|---|
| Company IR / feed, direct | 38 | 37 | 1 (DELL) | 1 (GME) |
| Company PR read as a copy | 11 | 11 | 0 | 0 |
| Search summary only | 1 | 1 | 0 | 0 |
| Aggregator, feed agreement | 0 | — | — | — |

The two misses aren't about who hosted the source. **DELL:** Dell's own events page said 09-03 when I
read it 21 days ahead, and the release then moved to 09-01. **GME:** the date was company-sourced, but
the amc time was inferred from filing history, and GameStop released at 9:00 AM in a financing quarter.
Both cadence rows are fixed. No source type missed repeatedly, so I'm not asking you to ban anything.
The sample can't rank the weak types: September had almost no search-summary or aggregator confirms.
Those are October dates (BX, GM, CME, MSCI, SCHW), and next week's pool reaches them.

**Do you want me to run another source-accuracy audit next Sunday? (Next time: the October dates that have passed by then.)**

### ⚠ BK (BNY) has no calendar row any more, and its 10-15 confirm landed nowhere — 10-11

`earnings_upcoming` has no BK row, and `earnings_date_sources` stops at 10-02 (`no_data`). The 10-06
session confirmed **BK 10-15 bmo** from bny.com, but there was no row for it to write to. It's in my
ledger only. WBS disappeared the same way (that one is right: it's delisted). If BK left the universe
on purpose, ignore this. If not, the scanner will miss BNY's 10-15 print.

### 📈 Daily queue: A + D worked in week 1, but disputes now outnumber the ceiling 3:1 — 10-11

**Scored on 10-06 → 10-09 (the first four runs):** each queue was 40 rows, mixed disputes + unconfirmed
by date. **70 dates confirmed** across the week (4 / 27 / 10 / 10 / 19), and the 83 invisible rows from
10-04 are down to **46 unconfirmed ≤ 10-23**. **D works:** every session wrote cadence rows
for its first-time names. The only gap was 10-05 (TXN, HIG, NSC), which ran on the old prompt; I backfilled
those. The ledger matched the DB with **0 mismatches**.

**New pressure:** disputes per morning went **32 → 51 → 82 → 108 → 112**. Nearest-first is the right
order, so the overflow is the far-dated rows, which is fine for now. Around 10-19, though, a 40-row
queue will carry rows dated only 3–4 days out. Option C (inject next-checks) is still open. If you want
a second lever before the 10-27 → 10-29 peak (~200 unconfirmed rows on those three days), raising the ceiling for
near-dated rows only is the cheap one.

### ⚠ Re-seeded times contradict established ones: 9 of the 10 rows are fixed, but the class isn't — 09-13, updated 09-27

On 09-13 I found ten upcoming rows whose stored time disagreed with a time I had company-sourced in an
earlier quarter. **Nine are now fixed from same-quarter sources** (09-22 → 09-24): ACN amc → **bmo**,
STZ bmo → **amc**, and C, FHN, SNA, ERIC, ACI, FNB, REXR `Unknown` → sourced. All nine went the way the
cadence table predicted. Left: **MDT** (11-17, `Unknown`; bmo, 6:45 ET release every quarter). It will
reach me as an `unknown_time` dispute.

What remains is the mechanism. Every quarter the feed re-seeds the next row, so the same names come back
wrong or `Unknown`. ACN and STZ were the dangerous shape: a filled-in wrong time that nothing flags.

Fixes for the class, cheapest first (unchanged since 08-18 / 09-03):
1. **Carry a confirmed time forward** to the next quarter's row instead of re-seeding it from the feed.
2. ~~A `--time`-only mode on `earnings_confirm.py`~~ — ✅ **done: `--time-only` is live (your 09-16
   install).** It lets me *write* a sourced time without touching the date; it does not stop the next
   quarter's row from being re-seeded, so fix 1 is still the one that closes the class.
3. Optional sweep: SEC Item 2.02 furnish times as the default when the feed says Unknown
   (method in `memory/reference_sec_acceptance_time_timing.md`).

Same family, never explained: TECH's time correction "wrote" three times in July and didn't persist (08-04).
_History in the archive: "MDT's wrong time came back…", "CLOSED 09-03 — CTAS's time…", "A time correction I 'wrote' three times…", "`earnings_confirm.py` conflates…"._

### 🐞 Tool fixes, still open — `direct_db_query.py`, and backslash paths in the daily template

- ✅ **`earnings_confirm.py` — fixed** (patch installed 09-16; verified 09-20 from `--help`: `--date`
  and `--by` required, `--time-only` present). ✅ **`launcher.py` template `--write` — fixed** (verified
  09-20, steps 6–7). Thank you — both were the two highest-consequence items on this list.
- **`direct_db_query.py`:** exits 0 and prints "No results returned" on invalid SQL and on 0-row
  updates (suggest: print `rowcount`, exit non-zero on `sqlite3.Error`); splits `--sql` on `;` even
  inside string literals (hit again 09-14); a backslash `--db` path under bash silently creates an
  **empty** database and then reports `no such table`. Small new one: a read-only `PRAGMA table_info`
  trips the write-guard warning and prints nothing (seen once, 09-20). My workarounds hold (forward
  slashes, no `;` in text, SELECT after every write).
- **`launcher.py` daily template still uses backslash `--db` paths** in steps 6–7
  (`E:\options_scanner\data\...`) — the stray-empty-DB hazard above if pasted into bash as-is.
  I always rewrite them to forward slashes; changing the template would remove the trap.

_History in the archive: "`earnings_confirm.py --symbol SYM`…", "`direct_db_query.py` splits…", "Tooling hazard…", "BUG in the daily session prompt…", "The `--write` bug…"._

### ⚠ Phantom earnings events still have nowhere to go — and the fall season re-arms them — 09-13

AES (take-private; no Item 2.02 since 2025-11), EA (take-private cleared 07-30; Q1 went out in a bare
10-Q), MKTX (ICE acquisition; Q2 released 8 days early alongside the deal) and TECH (Merck KGaA) all
reached me this summer as **unconfirmed calendar rows with no dispute row to write to**. All four now
have fresh fall rows — **AES 11-04, EA 11-03, MKTX 11-05, TECH 11-09** — plus KVUE 11-05 and WBD 11-05
(both corporate-action names). They'll surface again in late October. TECH's summer "phantom" turned out
to be real (08-12), so this is a *screen*, not a verdict — I'll run the pre-flight in
`memory/reference_ma_phantom_earnings.md` on each before researching.

The ask is unchanged: a `symbol_metadata` flag (`no_earnings_event` / `inactive`) that the dispute
generator and the calendar respect. A periodic ticker-vs-SEC `company_tickers.json` reconciliation
would also have caught IAC→PPLI automatically.
_History in the archive: "AES is a phantom again…", "EA is a phantom…", "MKTX was dated TODAY…", "Data-quality: symbols the dispute system can't self-assess…"._

### ❓ Policy calls I can't make by research — standing since July/August

1. **EXPD — `dmh`?** Expeditors furnishes midday every quarter and its release states no time;
   `earnings_confirm.py` accepts `dmh`. Set it? (Its fall row, 11-03, currently reads `bmo`.)
2. **Foreign issuers whose release lands after the US close (ASX/HK/Chile):** "D−1 amc" or "D bmo"?
   Both encode the same overnight gap. I've been writing the company's published date (WDS `bmo`;
   SQM `amc` on its 22:00 ET release date). Pick one and I'll apply it consistently. UEC's fiscal
   year-end has the same shape domestically (10-K the prior evening, webcast next morning).
   **⚠ Live now:** HDB and IBN (Indian bank ADRs) are dated **Saturday 10-17** in the DB (HDB `bmo`,
   IBN `amc`), **6 days out as of 10-11**. A Saturday release reaches the US market Monday 10-19 at the open, so either
   encoding needs a date change. HDB's board meets Sat 10-17 (reports of the NSE notice); IBN still has no notice. I'm holding
   both writes until you pick a rule.
3. **Sites that block every client (ITUB — `itau.com.br` 403s everything):** may an SEC 6-K filename
   cluster stand in for the date, or do I keep holding?

_History in the archive: "EXPD: candidate for `dmh`", "WDS (Woodside)…", "Two symbols need a policy call…", "ITUB…"._

### 💡 Proposals for a dev session (no urgency; each has a fuller write-up in the archive or `analysis/`)

- **Hook: give `confirmed_row_diverged` top priority** and show the signed delta — see
  `analysis/proposal_20260913_hook_diverged_priority_status_tripwire.md` (with two other small items;
  its item 3 predates the patch — the line to add to the prompt is now *"time-only ⇒ `--time-only`"*,
  not the plain UPDATE).
- **Hook: warn when `STATUS.md` is >10 days stale** — would have caught the 12-week maintenance gap in early July. (Same file.)
- **Hook: join live `earnings_upcoming` at injection time**, or stamp the snapshot's age — the frozen
  `db_date` misled me at least four times (07-22, 07-30, 08-06, 08-20).
- **Filter finnhub's lone +6 to +8d dissent** when DB = `+364d` (the DB won every scored case); never
  filter a ±1d or a yfinance dissent.
- **Flag overdue advance PRs** for symbols with a verified channel and a measured lead (PVH was 8d wrong
  with every feed agreeing; the only tell was a PR 7d overdue).
- **Window-gating in the hook** — `analysis/window_gating_in_inject_context_hook.md`.
- **Backfill `symbol_metadata.ir_earnings_url`** from the ⭐ feeds in the cadence table — needs your pick
  between my live-verify-on-Sunday option and a mechanical backfill (08-25 note).

### 🔧 FDX's earnings date is browser-render-only — recurs every quarter (next row: 10-28)

Unchanged since 06-21: no advance PR, no scheduling 8-K; the date lives only on a JS-rendered Q4 events
page. If its events JSON endpoint can be found I can self-serve; otherwise I'll hold and ask for a paste.

### Minor: from the 10-06 session: TSM's time and SCHW's inferred date

- **TSM time corrected amc → bmo** (call 14:00 Taiwan = 02:00 ET). Worth a look if the DB defaults foreign ADRs to amc.
- **SCHW 10-15 is inferred**: Schwab's Fall Business Update PR gives only the event, and earnings rode the update in 3 of 3 prior quarters. Next week's audit will score it.

### Minor: stray `memory/for_*.md` mailbox duplicates — still present, deletion still blocked for me

`rm memory/for_{market_analyst,system_analyst,trading_advisor}.md` — the canonical copies live in `outbox/`.

---

## Resolved (condensed — full text in the archive)

- **10-11: Backfill crowd-out (A + D, implemented 10-05): fixed.** Scored in the 📈 item above; full
  original text archived.
- **10-11: SNA called right, ACI called wrong.** SNA reports **10-22** (webcast PR 10-08, confirmed
  10-09), so the stored 10-15 was a week early as flagged. **ACI's stored 10-13 was right**: the PR
  existed from 09-29, and my 38-days-after-quarter-end arithmetic said 10-20. That arithmetic is no
  longer used as evidence. Also from the 10-06 notes: **WBS's phantom row is gone** from the calendar.
- **10-11: Sonnet week-1 item: superseded.** D fixed the bookkeeping gap. The 10-06 → 10-09 sessions kept
  the ledger and cadence rows current.
- **10-04: REXR's stored 10-14 was wrong, as flagged.** The company PR (09-28) says **10-22 `amc`**,
  confirmed 09-29. The other half of that item (SNA) stays open.
- **09-24 — Sessions no longer need a dispute to spawn (your A + C from the 09-20 proposal).** Verified in
  code 09-27: both gates spawn on disputes OR unconfirmed rows due ≤14d, and the hook warns on a missed
  weekday. **Not yet exercised:** every morning since 09-22 had disputes, so the old gate would have fired too.
  The first zero-dispute morning will be the real test. One residual gap is
  logged in my memory (a next-check on a row >14d out with no dispute still spawns nothing; Monday 09-28
  is such a day, but REXR/AMX/WIT have flagged daily, so it will probably run).
- **09-16 — `earnings_confirm.py` safety patch: installed by you, verified live 09-20.** Bare
  `--symbol` now errors, `--by` is required, `--time-only` exists, agent writes to `ben` rows are
  refused. My memory note now leads with the patched behaviour. Inbox notice processed.
- **09-14 — PAYX and KMX (dates I locked 09-08 without a company source): both re-sourced.** PAYX was
  wrong — corrected **09-29 → 09-23 `bmo`** from Paychex's PR (yfinance's drift flag was right); KMX's
  09-29 `bmo` was right and is now backed by CarMax's PR. The wrong PAYX lock stood 5 days with the PR
  already on the wire.
- **09-13 — "The Sunday maintenance session has not run since 06-21 … the scheduled task and its
  launcher are both gone" (08-26): CLOSED, and its diagnosis was wrong.** The launcher is at
  `E:\options_scanner\scheduled_tasks\start_earnings_researcher_sunday.bat`, *outside* the workspace;
  the 08-26 check only looked inside `agents/earnings_researcher/`. Task Scheduler lists
  **`!Sunday Earnings Researcher`**, Ready, next run 09-20 18:00, and it launched tonight. I can't tell
  whether the task was missing on 08-26 and re-registered since. Maintenance is caught up as of today.
- **09-03** — false `ben` stamps on ORCL/CTAS cleared; that repair only ever needed your say-so.
- **09-01 → 09-03** — GME, ADBE, CPRT, ORCL, CTAS confirmed as their notes predicted; the method
  lessons (BusinessWire index lag, dates relocating into transaction PRs) are in memory.
- **08-13** — SQM: its events calendar pre-lists release and call; no decision was ever needed.
- **08-12** — TECH: my phantom call was wrong and the event was real. Lesson (verify the channel exists
  for the matching quarter before arguing from absence) is now a standing rule.
- **08-03 → 08-10** — nCino's IR host, MKTX/ATI/ITUB/YPF (past-dated), NNE, INSP, FLO, BR, the frozen
  Allstate feed, the reporting-framing note, the browser-UA unlock, the 16-for-16 unconfirmed check.
- **07-27 → 07-31** — IAC → PPLI rename done; SPA problem solved via IR RSS; `+364d` demoted to
  corroborator; RSS-outage caveat; STE host correction; `skipped` resolution already existed.
- **06-30 convergence locks (10 names) — outcome:** at least 4 (RTX, LMT, CLF, EQT) were wrong by
  4–7d, caught 07-17 by the drift flag and corrected from company PRs. Policy since: no lock without a
  company source. (The 09-08 KMX/PAYX locks above broke that policy by a different route.)
- **June items** (dispute-list horizon bug, UEC chronic date, 06-07 table absence, weekend proposal
  implemented, 06-04 restore truncation, SEC via curl) — archive → Resolved.
