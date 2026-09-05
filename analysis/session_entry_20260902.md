
## Session: 2026-09-02 (Wednesday) — 07:13 AM ET

4 disputes (CPRT/ORCL/CTAS/GIS) — **2 confirmed, 2 gated**, ~12 HTTP reads, 0 web searches.
Both confirms came from **BusinessWire advance PRs that were already sitting on the wire**, and
both were found by the same one-fetch move: `stocktitan.net/news/<SYM>/`, whose JSON-LD block
lists the last 10 headlines with ISO timestamps **and** their article URLs. Every prior session
had been reading that page as a *cross-check for absence*; today it was the primary discovery
channel for two symbols whose IR hosts do not resolve at all.

### Confirmed (2)

| Symbol | Result | Source |
|--------|--------|--------|
| CPRT | **2026-09-10 `amc`** (DB snapshot said 09-03) | Advance PR *"Copart, Inc. to Release Fourth Quarter Fiscal 2026 Results"*, **09-01 10:34 ET**, BusinessWire: *"will release earnings for the fourth quarter of fiscal 2026 **after 4:00 p.m. Eastern Time** (3:00 p.m. Central) **on Thursday, September 10, 2026**,"* call 5:30pm ET. `businesswire.com/news/home/20260901213040/en/` |
| GIS | **2026-09-23 `bmo`** (time was Unknown) | Advance PR *"General Mills to Webcast Fiscal 2027 First Quarter Earnings Results on September 23, 2026"*, **08-26 08:00 ET**, BusinessWire: *"plans to report results for its fiscal 2027 first quarter on September 23, 2026. A press release, pre-recorded management remarks and supporting slides will be **issued that morning** followed by a webcasted question and answer session … at 8 a.m. CT."* `businesswire.com/news/home/20260826734008/en/` |

### Gated (2)

| Symbol | DB date | Why skipped | Next check |
|--------|---------|-------------|------------|
| ORCL | 2026-09-10 amc | *Sets the Date* PR still absent — feed live (200, 10 items, newest still the **06-10** Q4 results PR), EDGAR clean (no filing since 07-28). This was the read the 09-01 session called **decisive**, and it decided: absence through **09-01 16:01 ET** plus the **7d minimum** lead ⇒ release ≥ 09-09, which **kills the 09-08 candidate**. DB's **09-10** is the only in-band survivor, but cadence is not a company source ⇒ **no lock**. | 2026-09-03 |
| CTAS | 2026-09-23 amc | Advance PR **not due yet**, and this row previously had no cadence entry at all. Cintas *does* issue one — *"Cintas Corporation Announces Webcast for \<n\> Quarter Fiscal Year \<yr\> Results"* — Q4 FY26 went out **07-01 13:29 ET** for a **07-15** release = **14d**. A 09-23 release therefore puts the PR near **09-09**; newest CTAS wire item is **08-10**, so today's absence carries no information. | 2026-09-08 |

### ⭐ Two dead IR hosts, two confirms — stocktitan's JSON-LD is a discovery channel, not just a cross-check

`investors.copart.com` is NXDOMAIN (six hosts, re-verified repeatedly) and `investors.cintas.com`
/ `ir.cintas.com` are **both NXDOMAIN too** — Cintas' Q4-managed host `cintas.gcs-web.com`
resolves but returns **403 Access Denied on every path** (Akamai). Two of today's four symbols
had *no first-party surface at all*, which historically meant "gate and wait."

What changed is how the mirror is read. `https://www.stocktitan.net/news/<SYM>/` embeds a
`CollectionPage` JSON-LD object whose `hasPart` array carries the **last 10 headlines with
`datePublished` in UTC and a direct article URL each**. One `curl --compressed` gives you the
full recent-news spine of a company in ~16KB, and the article pages reproduce the **verbatim
wire text including the `View source version on businesswire.com:` permalink** — so the
citation that lands in `research_url` is the wire's own URL, not the mirror's.

Two operational notes learned the hard way today:
- ⚠ **You must send `--compressed`.** Without it curl returns the raw brotli body, which reads
  as binary garbage and looks exactly like a bot wall. I burned a fetch on that.
- ⚠ **Stocktitan rate-limits fast.** The 3rd and 4th requests in quick succession returned
  **HTTP 429**, and `/news/<SYM>/page/2` **404s** (pagination is not that shape). Budget one
  page fetch per symbol, space them, and pull everything you need from the JSON-LD in one pass.

### ⚠⚠ CPRT — the gate was right about the date being wrong, but the *channel model* was wrong in three places

The 09-01 session concluded "advance absent ⇒ release ≥ 09-09, DB's 09-03 is excluded." That
call was **correct** — the PR published the very next morning naming **09-10**. But the cadence
row's model of *how* Copart publishes was wrong in three ways that all pointed the same
direction (too early):

1. **The advance PR IS BusinessWire.** The row carried a ⚠⚠ CORRECTION from 08-24 saying
   *"the wire is PRNewswire, not BusinessWire."* That correction was drawn from the **board-addition**
   PR (a corporate release) and does not transfer: today's advance dateline reads
   **`DALLAS --(BUSINESS WIRE)--`**. Copart uses **both wires for different release types**.
2. **The lead is 9d for Q4, not 7–8d.** 09-01 → 09-10 = **9 days**. The 09-01 session had just
   *narrowed* the band to 7–8d on Q4-specific evidence and used the **7d minimum** as the floor.
   The floor logic still worked, but a gate built off "7–8d" would have expected the PR by 09-03
   and read 09-01's absence as later than it was.
3. **It does NOT publish after 16:00 ET.** Every version of this row said the advance posts
   post-close, so the useful read was "next morning." It published at **10:34 ET** — *during*
   the session day. A same-day afternoon re-read would have caught this ~20 hours earlier.

### ⚠ CTAS — the stored `amc` is provably wrong, and no dispute would ever have surfaced it

The dispute was filed as `date_disagreement` (DB 09-23 vs finnhub 09-30), so the **time** was
never in question — but it is wrong. Cintas is **structurally bmo, 6/6 quarters**: Item 2.02
acceptance times are **08:31–08:34 ET** (2026-07-15 08:31:16, 2026-03-25 08:31:08,
2025-12-18 08:31:05, 2025-09-24 08:34:41, 2025-07-17 08:31:26, 2024-09-25 08:30:58), the release
reads *"today reported results"*, and it names a **10:00 a.m. ET** webcast. I did **not** confirm
the row, because confirming would have locked the unsourced date along with the time — the CLI
has no time-only mode. Flagged for Ben instead.

On the date itself, DB is strongly favoured without being sourced: Cintas' **Q1-only** Item 2.02
dates are **2025-09-24 (Wed), 2024-09-25 (Wed), 2023-09-26 (Tue)** — stepping exactly one day
earlier each year, extrapolating to **2026-09-23 (Wed) = DB**. finnhub's **09-30** sits a full
week outside that three-year band.

### ⚠⚠ TOOL HAZARD — `earnings_confirm.py --symbol SYM` (no `--date`) is a WRITE, and it stamps `by=ben`

I ran `earnings_confirm.py --symbol X` on all four symbols expecting a read-only status query;
its help text lists it as *"Confirm current date/time as-is."* It **is** a write. With no
`--date`/`--time` it keeps the existing values but **always** executes
`date_confirmed=1, date_confirmed_by=?, date_confirmed_at=?` — and `--by` **defaults to `ben`**.
All four rows were stamped `date_confirmed_by='ben'` at **07:18:46**.

This is the single worst mistake available in this workspace, because CLAUDE.md's hardest rule
is *never overwrite a date confirmed by Ben* — so a false `ben` stamp is **self-protecting**:
it makes a wholly unresearched date look like the one source that must not be touched.

CPRT and GIS were repaired implicitly by the real confirms (`--by agent` overwrites the stamp).
**ORCL and CTAS are still falsely marked `date_confirmed_by='ben'`** — the revert UPDATE was
blocked by the permission classifier three times (clearing confirmation flags is gated), so it
is written up in `notes_for_ben.md` with the exact SQL. **Never use this tool to inspect state.**
Read `earnings_upcoming` with `direct_db_query.py` instead:

```
python tools/direct_db_query.py --db data/datalake.db --sql "SELECT symbol, earnings_date, earnings_time, date_confirmed, date_confirmed_by FROM earnings_upcoming WHERE symbol='SYM'"
```

### Other notes

- ⚠ **`direct_db_query.py` breaks on a `;` inside a string literal** — it splits the statement
  before parsing, so a `notes='...; ...'` value dies with `unrecognized token`. Both dispute
  UPDATEs failed on this first try. Use commas or dashes in note text.
- **The CPRT dispute snapshot was stale by the time I read it.** The dispute row recorded
  `db_date=2026-09-03`, but `earnings_upcoming` already held **09-10** when I queried it at
  07:18 — a feed self-corrected between dispute generation and the session. Worth checking the
  live row rather than trusting the injected snapshot when the two can be compared cheaply.
- **GIS needed no cadence extrapolation, and that is lucky.** Its Q1 Item 2.02 history —
  2025-09-17 (Wed), 2024-09-18 (Wed), 2023-09-20 (Wed) — extrapolates to **09-16**, which is
  **a week off the company's own announced 09-23**. A `+364d`-style argument would have
  produced a confident wrong answer here.
- **finnhub scoreboard, 4/4 wrong:** CPRT 11-18 (next quarter entirely), ORCL 09-14 (a Monday
  needing a PR on 09-05..09-07, and 09-07 is Labor Day), CTAS 09-30 (outside a 3-year band),
  GIS 09-15 (company says 09-23).

---
