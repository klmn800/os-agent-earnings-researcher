# Notes for Ben

Issues, questions, and findings from the Earnings Date Researcher agent.
Open items first; long-resolved notes condensed into **Resolved** at the bottom.

---

## Open

### ✅ CLOSED 09-03 — the false `ben` stamps are gone; nothing needed from you

Both halves of this resolved themselves today, so **there is no action left here.**

- **ORCL** repaired itself properly: Oracle's *Sets the Date* PR published 09-02 16:00 ET naming
  **2026-09-10, after the close**, so I confirmed it for real — row now `1 / agent / 09-03 07:20:50`.
- **CTAS**: you asked me to run the clearing statement and **it went through on the first try** —
  row now `2026-09-23 bmo / 0 / NULL / NULL`, which is the correct state (date genuinely unsourced,
  gated until Cintas' advance PR ~09-09; the `bmo` time is right and I left it alone).

⚠⚠ **And that outcome corrects what I told you on 09-02.** I wrote that clearing confirmation flags
was blocked for me and handed you SQL to run by hand — I'd tried three times and been refused. The
**same statement ran fine the moment you asked for it.** The gate isn't on the statement, it's on me
doing it unprompted, which is a sensible line — but it means I gave you manual work I could have done
on request, and left a wrong row standing an extra day. I've corrected the memory: from now on I'll
flag a false stamp as *"here's the statement, say the word"* instead of *"you must run this."*

The two tool changes I suggested still stand on their own merits, if you want them: require `--date`
or `--time` so a bare `--symbol` is a no-op read, and require `--by` rather than defaulting it to
`ben` — the most privileged value being the default is what turned a fumbled read into a
self-protecting wrong date.

### ✅ CLOSED 09-03 — CTAS's time is now `bmo`; the *class* of error below is still worth your read

**The specific fix is done:** CTAS reads `2026-09-23 bmo` as of today (date still unsourced/gated,
which is correct). I'm leaving the reasoning below intact because the **class** of error is the real
point — a `date_disagreement` dispute puts only the *date* in question, so a wrong stored **time** on
the same row is invisible to the dispute system and can survive indefinitely. That hole is unchanged.


Separate from the above, and worth a look because it's a class of error rather than a one-off.

Cintas came to me as a `date_disagreement` dispute (DB 09-23 vs finnhub 09-30), so only the *date*
was in question. But the stored **time is `amc`, and Cintas is unambiguously a before-open reporter**:

- Its earnings 8-K has been accepted at **08:31–08:34 a.m. ET in all six quarters** I checked
  (2026-07-15, 2026-03-25, 2025-12-18, 2025-09-24, 2025-07-17, 2024-09-25).
- The release text opens *"Cintas Corporation … today reported results"* and announces a
  **10:00 a.m. ET** webcast to review them.

That's about as structurally locked as `bmo` gets, so **I fixed it** — but not with the confirm CLI,
which has no time-only mode and would have locked the still-unsourced **date** along with it. I wrote
the time alone:

```
UPDATE earnings_upcoming SET earnings_time='bmo' WHERE symbol='CTAS'
```

The date stays unresearched pending Cintas' advance PR (~09-09). Note the asymmetry I ran into today:
a plain field UPDATE like that one goes through fine, while the `date_confirmed=0, date_confirmed_by=NULL`
form is blocked — which is why the item above needs your hands and this one didn't.

**The general point:** a `date_disagreement` dispute never surfaces a bad time, so times can sit wrong
indefinitely on symbols whose dates happen to agree. If you ever want a sweep, the cheap signal is
exactly what I used here — Item 2.02 8-K acceptance timestamps from the SEC submissions API, which are
free and unambiguous (before ~09:30 ET ⇒ bmo, after ~16:00 ET ⇒ amc). A `--time`-only flag on
`earnings_confirm.py` would let me fix these as I find them.

For what it's worth, Cintas' date almost certainly *is* 09-23: its Q1 filings were 2025-09-24 (Wed),
2024-09-25 (Wed), 2023-09-26 (Tue) — one day earlier each year. finnhub's 09-30 is a week outside that.
I'll lock it when the PR lands.

---

### ✅ GME and ADBE both confirmed — and one of them exposed a real hole in my method — 09-01

Two dates locked today, both matching what the DB already had (so nothing moved — they went from
`unconfirmed` to agent-confirmed, which is the point of that queue):

- **GME — 2026-09-08, after close.** GameStop's own PR, 08-31.
- **ADBE — 2026-09-10, after close.** Adobe's advance PR, 08-31, call 2–3 p.m. PT (= 5 p.m. ET).

Both landed on the **first day my gates said they could exist**, which is the system working as
intended. The ADBE catch in particular vindicates a correction from 08-27: this workspace used to
carry Adobe at a "~14 day" lead that had been assumed and never measured. The real lead is 8–10
days, and the PR arrived at exactly 10 — under the old number I'd have opened the window on 08-27
and spent four sessions confirming an absence that was guaranteed.

**The hole, and it's worth your attention because it affects how much my "the PR isn't out yet"
claims are worth:**

Adobe's PR published 08-31. When I ran the **domain-restricted BusinessWire exact-title search** —
the documented channel for both ADBE and CPRT — it returned **only prior quarters**. The open web
search and stocktitan both had it. In other words, **had I used only my own documented channel, I'd
have logged Adobe as "advance not out" on the very day it published.**

That's not a harmless miss. Those absence findings are what set the *floor* under a date (it's the
entire basis for saying Copart's 09-03 is wrong), so a false negative silently pushes a date later
and I'd have no way to notice. I've made it a standing rule: the BusinessWire title search is fine
as a **positive** channel, but is not trustworthy as a **negative** on its most recent ~1 day, and
any absence driving a floor now needs a second, faster-indexing channel. I applied that to Copart
today.

**Second finding, from GME — the date arrived in a PR whose title had nothing to do with earnings.**
GameStop issued no "Announces Release Date" advance this quarter. The date is the **last bullet of a
preliminary-results release**, which itself only exists because GameStop had to disclose alongside
its convertible notes exchange amendments. My title-pattern search would have found nothing. I only
caught it because I was parsing full PR bodies out of the feed.

Generalised and written into the cadence memory: **when a company is mid-transaction — notes
exchange, M&A, offering — the earnings date can relocate into a preliminary-results or transaction
PR that matches no advance-PR title.** So for those symbols, a missing advance PR has a third
meaning beyond "issued" or "skipped": *the information moved*. Cheap fix — grep the feed bodies for
"expects to release" / "will report" instead of matching headlines, on a feed I'm already fetching.

### ✅ CLOSED 09-02 — CPRT confirmed **2026-09-10 `amc`**; the ruled-out call was right

**Resolved the next morning.** Copart's advance PR published **09-01 10:34 ET** (BusinessWire):
*“after 4:00 p.m. Eastern Time … on Thursday, September 10, 2026,”* call 5:30pm ET — exactly the
~09-09/09-10 exposure window predicted below, and DB's 09-03 was wrong by +7d as called. Row now
`1 / agent`. Analysis kept for the record; **nothing needed from you.**


Unchanged conclusion, but I found an error in **my own** numbers and want you to have the corrected
version rather than the one that happened to reach the right answer.

Copart's Q4 advance PR is **still not out**, and I verified that on **two independent channels**
today rather than one: the exact-title BusinessWire search (returns every prior advance, no Q4
FY2026) and **stocktitan**, whose newest Copart item is the **08-18** board-addition PR with nothing
since. The second channel matters — see the ADBE note below for why a one-channel absence is no
longer good enough for me.

**The correction:** this workspace has been gating Copart off an **8–9 day** lead. Filtered to Q4
only, the real leads are **7–8 days** — Q4 FY22 ran **7d** (PR 08-31 → results 09-07), and FY23/24/25
all ran 8d. The 9d came from **Q1 FY26**, a different quarter entirely. That's the third time in a
week a cadence number turned out to be borrowed from the wrong fiscal quarter.

Redoing the floor honestly on the **7d** minimum: silence through 08-31 means the PR is 09-01 or
later, so the release is **≥ 09-08**. 09-08 is a Tuesday, and every Q4 furnish since 2019 has been a
**Wednesday or Thursday (7/7)** — so the near candidates are **Wed 09-09** or **Thu 09-10**. Same
answer as 08-28, now resting on numbers that are actually Q4's.

**Stored 09-03 is excluded even under the more generous 7d floor** (it would have needed the PR by
08-27; five days have passed on a live channel).

⚠ One thing I'd previously have read wrong: **this is not late.** Q4 FY23's advance published on
**09-06**, so a September advance PR is normal for this quarter and continued silence this week
isn't evidence of a skipped quarter.

**What to do with it:** treat 09-03 as wrong. If anything wants to trade CPRT earnings, the window
is ~09-09/09-10, **not this Thursday**. The advance PR names the date outright and resolves this in
one fetch — checking daily.

### ✅ CLOSED 09-03 — ORCL confirmed **2026-09-10 `amc`**; the elimination held

**It decided, and then the company confirmed it.** The 09-02 read found the feed still empty, which
killed **09-08** on the absence floor and left 09-10 as the only in-band survivor — and I declined to
write it, because cadence isn't a company source. Oracle's *Sets the Date* PR then published at
**16:00 ET that same afternoon**: *“released on Thursday, September 10th, after the close of the
market,”* webcast 4:00pm CT. Confirmed 09-03, `1 / agent`. **finnhub's 09-14 was wrong.**
⚠ Worth knowing: Oracle posts these at **16:00–16:01 ET**, so an ORCL advance is never readable in
the morning session that predicts it — always a next-day read. **Nothing needed from you.**


Following up the 08-28 correction (the "reported on the 10th three quarters running" argument was
measured on Q2/Q3/Q4, not Q1 — Oracle's Q1 habit is Mon/Tue, and the stored date is a Thursday).

Oracle's *Sets the Date for its 1Q FY27* PR is **not out** — feed live, newest item still the 06-10
Q4 results release. What that buys us: at Oracle's **7-day minimum** lead, silence through 08-31
puts the release at **≥ 09-08**, which by itself rules out neither candidate.

But it does kill the 8d and 9d routes to **09-08** — those needed the PR on 08-30 or 08-31, and
neither happened. **09-08 now survives only if the PR drops today around 16:01 ET.** So tomorrow's
read is genuinely decisive rather than routine: if the feed is still empty on 09-02, **09-08 is out
and the stored 09-10 becomes the strong favourite**.

No action needed from you. The dispute against finnhub's 09-14 stays unresolved on purpose — I'd
rather hold it one more day and read the company's own PR than lock a date off cadence.

### 🔴 The Sunday maintenance session has not run since 06-21 — the scheduled task and its launcher are both **gone** — 08-26

I went to update `STATUS.md` today and found it stamped **2026-06-21**. That's nine and a half
weeks stale, while the daily sessions have run continuously the whole time (08-13 … 08-25 are all
in the log). So I went looking for why, and it isn't a skipped week — the machinery is missing:

1. **`scheduled_tasks/` does not exist in the workspace.** `CLAUDE.md` documents the Sunday
   launcher as `scheduled_tasks/start_earnings_researcher_sunday.bat`; the directory is absent
   entirely. `PROMPT_SUNDAY.md` is still here, so only the launcher half was lost.
2. **No scheduled task matching "earnings" or "researcher" exists in Task Scheduler.**
   `schtasks /query /fo CSV` returns zero matching rows. (Caveat: that lists what this account can
   see — if you registered it under a different account, check there before believing me.)
3. **The last `## Weekly Maintenance` entry in the research log is 2026-06-21.** There are exactly
   two in the whole active log (06-14, 06-21) and none after.

**What it has cost, concretely — the workspace is now well outside its own policy:**

| | Policy | Actual today |
|---|---|---|
| `memory/research_log.md` | ~150 lines, last ~2 weeks | **2,607 lines, 39 sessions**, oldest 06-12 |
| Archive rotation | quarterly, by season | nothing archived since 06-21 |
| `STATUS.md` | current each Sunday | **stamped 06-21** |
| Carry-over ledger pruning | weekly | resolved rows from July/August still sitting in the table |

The research itself hasn't suffered — cadence promotion has been happening inline in the daily
sessions, which is why the cadence table is in good shape. What's degraded is everything the
Sunday session owns: the log is ~17× its target length (it's the single biggest thing I read at
startup, so this is a real per-session token cost), `STATUS.md` is useless as a dashboard, and
nobody has run the weekly calibration — the confirm-vs-missed-skip scorecard — since June.

**What I'd like to do about it (your call):**

- **The fix I can't do myself:** re-register the Task Scheduler job and restore the `.bat`. I don't
  have the original file and won't guess at its contents; if you still have it, or want me to
  reconstruct it from the two-step invocation `CLAUDE.md` describes (`launcher.py --prepare-only
  --prompt PROMPT_SUNDAY.md`, then a visible `claude` window), say which and I'll draft it.
- **The fix I can do right now, on request:** run the maintenance pass manually in a session —
  archive 06-12 → mid-August out of the active log, prune the resolved carry-overs, refresh
  `STATUS.md`, and write the overdue calibration. It's exactly `PROMPT_SUNDAY.md`'s job list; it
  just needs someone to start it. I did **not** do it today unprompted, because a daily session
  quietly rewriting the log and archive is the kind of scope jump I'd rather you approve first.
- **Worth considering:** a cheap tripwire so this can't rot silently again — the daily context hook
  already knows the date; having it warn when `STATUS.md`'s stamp is more than ~10 days old would
  have caught this in early July instead of late August.

### 💡 The cadence table knows working IR feeds that `symbol_metadata` doesn't — a cheap backfill — 08-25

Today's dispute list said **"Cached IR URL: None"** for ORCL. But `reference_company_cadence.md`
has had `investor.oracle.com/rss/pressrelease.aspx` marked ⭐-working since 08-20, verified
again 08-21. The knowledge existed; it just wasn't in the column the hook reads.

I checked the four symbols on today's list — **all four had `ir_earnings_url = None`** in
`symbol_metadata`, and at least two of them (ORCL, and now CNM) have a known-good feed. So the
two stores have drifted: my memory file is the live record, `symbol_metadata` is stale.

Why it costs something: the injected dispute list is where I decide whether to spend a search.
When it says "None," the cheap path (fetch the known feed) isn't visible at the moment I'm
choosing what to do — so the fallback is a web search, which is the expensive branch. It also
makes every session re-derive a fact that's already written down.

**What I did today:** cached two by hand — `CNM` → `coreandmain.com/news/feed/` (verified this
morning) and `ORCL` → the Oracle feed, stamped `08-21` rather than today, since that's when it
was actually last verified and I didn't re-touch the host.

**Proposal (your call, it's a dev item):** a one-time backfill that walks the ⭐-marked feed URLs
out of `reference_company_cadence.md` into `symbol_metadata.ir_earnings_url`. There are a few
dozen of them and they're in a consistent column of the table. I'd rather not batch-write those
blind, though — some are stamped with old verification dates, and a stale cached URL is worse
than none (it makes me *stop* looking). Two options:

1. I verify each one live in a maintenance session, then write only the ones that respond, with
   an honest `ir_url_last_verified`. Slower, but every row is true when written.
2. You backfill them all mechanically and accept that `ir_url_last_verified` carries the date
   from my notes, not a fresh check.

I lean (1), on a Sunday — it's exactly the kind of workspace upkeep that session is for, and it
turns the cadence table's accumulated host knowledge into something the hook can actually use.


### 🐞 `earnings_confirm.py --symbol SYM` (no other flags) silently confirms the row **as Ben** — 08-19

I ran `python earnings_confirm.py --symbol GME` meaning to *read* GME's stored
state before deciding what to write. It isn't a read. It confirmed the row as-is
and — because `--by` defaults to `ben` — stamped:

```
GME | 2026-09-08 | Unknown | date_confirmed=1 | date_confirmed_by=ben
```

I caught it in the same minute and reverted it (`date_confirmed=0`,
`date_confirmed_by=NULL`), then wrote the time properly. **No damage, and GME is
in a correct state now** — `amc` written from its own 8-K furnish times, date
left unconfirmed because no company source exists yet.

**Why I'm flagging it rather than just remembering it.** CLAUDE.md's critical
rule is *never overwrite a date confirmed by Ben*. So a stray `ben` stamp is
self-sealing: it creates a row that neither I nor any future session is allowed
to correct, and nothing in the row shows that a flag default — not you — wrote
it. In this case it would have frozen a date with **no company source behind
it**. That's the failure mode worth closing, not the one-off.

Two things that make it easy to trip:
1. The tool's own `--help` lists `--symbol VZ` bare as an example, directly under
   the full confirm form. It reads like a lookup.
2. Bare `--symbol` is also the natural thing to type when you want to check state.

**Suggested fixes, cheapest first** — your call, I haven't touched the tool
(and won't, it's outside my write scope):
- Make `--by` **required** whenever the call writes. One-line change, kills the
  whole class.
- Make bare `--symbol` (no `--date`, no `--time`) a **read-only display**, which
  is what the help text implies it already is.
- Or have it refuse to confirm a row whose time is `Unknown` — a confirm that
  leaves the timing unknown is almost never intentional.

I've written this into memory (`feedback_earnings_confirm_bare_symbol.md`) so I
always pass `--by agent` from here on, but the guard belongs in the tool.

**Worth an audit:** if any `date_confirmed_by='ben'` row has no matching entry in
my research log, it may be an earlier instance of this rather than a real
decision of yours. I can run that check next session if you want it.

### 🔁 MDT's wrong time came back with the new quarter — this is re-seeding, not a failed write — 08-18

I corrected Medtronic's `earnings_time` from `amc` to `bmo` last quarter, and my cadence note has carried the reason ever since (Medtronic's advance PR says the release goes out at **5:45 a.m. Central = 6:45 ET**, webcast 6:45am CT — unambiguously BMO). The **new quarter's row arrived this morning with `amc` again.** I re-corrected it and verified it stuck.

Worth separating this from the TECH note further down, because it looks similar and isn't. TECH was a **write that reported success and didn't persist** — same row, same quarter, value silently reverting. This is a **fresh row for a new earnings date being seeded with the wrong time by whatever populates the calendar**, and my correction only ever applied to the old row. Both end with a wrong `amc` in front of you, but the fix is in different places: one is the write path, the other is the upstream time source.

**Two things that would help:**
1. If the calendar seeds `earnings_time` from a third-party feed, MDT is a known-bad entry there — it has been `amc` for at least two quarters running against a company statement that says 6:45 ET. Might be worth checking whether that feed is wrong for a whole cohort of early-morning reporters rather than just Medtronic.
2. **Corrections don't currently carry forward.** A confirmed `bmo` is a fact about the company's habit, not just about one date — MDT has released BMO every quarter I have records for. If a symbol's time has been agent- or Ben-corrected once, it would be reasonable for the next quarter's row to inherit that rather than re-seed from the feed. That would remove a small recurring re-work item and, more importantly, close the window where the wrong time is live in the DB before the symbol happens to reach my dispute list.

Low urgency — I catch it when the symbol comes up, and I caught it today. But I only catch it *because* it reaches my list, and a symbol whose date is never disputed would keep the wrong time indefinitely.

### 💡 PVH was wrong by 8 days and **nothing in the system disagreed with it** — proposal: flag overdue advance PRs — 08-17

Today's one confirm is worth your attention because of *how* it was found. PVH's own PR (08-17 09:00 ET) says it reports **Wednesday 2026-09-02**; the DB said **08-25**. Confirmed, +8d.

What's notable is that **no feed dissented.** PVH came to me as an `unconfirmed` calendar row, not a dispute — finnhub and yfinance both matched the DB, and the `+364d` cadence check reproduced 08-25 exactly. Every automatic signal we have agreed on a date that was 8 days wrong. Had PVH not been surfaced as "unconfirmed," nothing would have questioned it.

The one thing that did point at a problem: **its advance PR was 7 days overdue.** PVH issues a "to Host Conference Call…" PR on a measured **15–16 day** lead through a channel verified for the matching quarter, so by today the PR for an 08-25 release should have existed a week earlier and didn't. That's computable from data we already have — the DB date and the per-symbol lead time in `memory/reference_company_cadence.md`.

**Suggested rule (the inverse of the finnhub filter above):** for symbols with a *verified* advance-PR channel and a measured lead, flag a row when `today > earnings_date − lead − buffer` **and no advance PR has appeared**. That's a "this date is probably wrong" signal that fires where our feeds are silent — the opposite failure mode from the +6/+8d artifact, which is noise where our feeds are loud. Between the two, the daily list would be pointed at the rows that actually move.

⚠ Two honest limits. **(a)** Lateness says the date is *wrong*, not what's *right* — my own replacement guess (09-01) was also wrong, because PVH kept its Monday PR and 16d lead but shifted the release Tue→Wed. So this should flag for research, never auto-correct. **(b)** It only works where the channel is verified for the matching quarter — the TECH lesson. For COTY or GTLB, which issue no advance PR at all, lateness is meaningless and would fire every quarter forever.

**Second, smaller thing you may want to know about session timing.** PVH publishes that PR at **09:00 ET on a Monday**, and my session starts ~07:20 — so the opening read *cannot* see it, and on 08-14 I recorded exactly that non-answer. Today I left a background poll running to 09:30 and it caught the PR at 09:01:13. Worth knowing that for symbols publishing after ~07:30 ET, the single morning read structurally can't answer them; polling (or a second, later pass) is the fix, and it's cheap. No action needed from you unless you'd rather the orchestrator schedule a short second window.

### ✅ SQM never needed your decision — I'd been reading the wrong page. Closed. — 08-13

I escalated SQM to you as a judgment call twice (08-07, 08-11): DB said 08-18, finnhub said 08-19, I'd established the company issues no advance scheduling PR, and I framed the release-vs-call ambiguity as something only you could settle. **You can drop it — SQM answers it itself, in writing, on a page I never opened.**

`ir.sqm.com/news-events/events-calendar` lists both halves separately:

- **August 18, 2026, 10:00 PM EDT** — Publish Second Quarter 2026 Financial Results
- **August 19, 2026, 12:00 PM EDT** — Second Quarter Conference Call

So **DB's 08-18 was the release date and finnhub's 08-19 was the call date** — exactly the split I'd diagnosed, but sourced instead of guessed. Confirmed **2026-08-18 amc** (a 22:00 ET release is unambiguously after the close, and the reaction lands in the 08-19 session, which is what `amc` on 08-18 already encodes). The same calendar shows the pattern holding since 2023, so this should stay stable.

**The mistake is worth naming because it wasn't a wrong fact, it was a wrong equivalence.** I had verified "SQM issues no advance PR" — that part is true — and then treated it as "SQM has no company source." Those are different claims, and the gap between them is that **the events calendar is a separate channel from the press-release feed**. I'd been re-reading the feed every session, correctly finding nothing, and re-deriving the same dead end three times.

I've made "check the calendar before concluding no source exists" a standing rule in the cadence memory. It also caught **DELL** today, whose row said "event page timeout" — true of WebFetch, false of urllib with a browser UA, and its calendar had 09-03 pre-listed the whole time. Six symbols now use the calendar as their primary source (SQM, DELL, DNN, MCHP, LOW, HD).

Honest caveat so this doesn't get oversold: I swept the calendar paths across the other eight symbols today and **it rescued none of them** — five 404 on every path, one host is NXDOMAIN, two return JS-only shells. It's a cheap first check, not a general solution.

### 💡 Proposal: filter the +6/+7d finnhub artifact before it becomes a dispute — 08-13

Three of today's six disputes (NCNO, GTLB, CPRT) were the same non-event: finnhub's date sitting exactly **+6 or +7 days** past a DB date that `+364d` cadence arithmetic reproduces exactly. All three resolved to "DB is fine, hold" — as this pattern has essentially every time it's appeared (HRB, CSCO, TOL, HPQ, NTNX, RDW, P, and more in the archive).

**Suggested rule:** when finnhub is the *only* dissenting source AND its date is +6/+7d from the DB date AND the DB date matches `+364d` from the year-ago confirmed date, don't open a dispute row — or open it at a lower priority that doesn't consume a research slot.

That would have cut today's list from 6 disputes to 3 and lost nothing. The cost of the current behaviour isn't huge per-symbol (they're gated, so I hold them cheaply), but it's steady, and it crowds out the genuinely ambiguous rows.

⚠ Two guardrails, because I don't want this to hide a real move: **(a)** it must require finnhub to be *alone* — when **yfinance** dissents, the DB is the suspect side (PANW, GO, GRAL, AAP all went that way), and **(b)** a **±1d** finnhub dissent is a different animal and must not be filtered — LI's lone 08-26 was right against DB's 08-27 and against `+364d`. This filter is narrowly for the +6/+7d shape only. Your call on whether it's worth the code.

**Update 08-14 — NCNO closed the loop and the filter would have been right.** nCino's own PR
landed 08-13 and says **August 25** — the DB date, exactly as `+364d` predicted; finnhub's
09-01 was noise, as called. GTLB and CPRT are still open but both remain `+364d`-consistent
and window-gated. So the pattern is now 1-for-1 resolved out of the three flagged, with
nothing contradicting it. Nothing new needed from you — just wanted the prediction scored
rather than left hanging, since a filter proposal is only worth acting on if its calls hold up.

**Update 08-17 — this is now the whole dispute list, three sessions running.** Today's list had
**three** disputes and all three are the same artifact: NIO (finnhub 09-09 vs DB 09-01, **+8d**),
GTLB (09-08 vs 09-02, +6d), CPRT (09-09 vs 09-03, +6d). Every one is `+364d`-exact against the
DB date, none has a second dissenting source, and all three were held. Under the proposed filter
**today's dispute list would have been empty** — which is the correct answer, since all three are
window-gated and unresearchable until 08-26 / 09-02 respectively.

One new data point that sharpens the case: **NIO's finnhub date moved from 08-31 to 09-09 between
08-11 and today** — a 9-day swing in six days, on a symbol where nothing was published in between.
A source that revises itself by more than a week while the company is silent isn't a weak signal
to be weighed; on this shape it's noise being treated as a research trigger. I'd also widen the
window in the rule from +6/+7d to **+6 to +8d** on the strength of NIO.

Scorecard so far: of the symbols flagged as this artifact and since resolved by a company source
— NCNO, HRB, CSCO, TOL, HPQ, NTNX, RDW, P — **the DB date won every time**. Still your call, but
it's no longer a marginal cleanup: it's most of what the daily list currently contains.

### ⭕ TECH — I was wrong. The earnings event was real, it happened this morning, and my recommendation to you was bad — 08-12

Bio-Techne filed its Item 2.02 8-K today at **06:30:30**, on the exact furnish minute it has held for eight straight quarters, with the same item set as its last six earnings 8-Ks and a press release "describing the results of operations for the quarter and [fiscal year ended June 30, 2026]." Confirmed **2026-08-12 bmo**. The DB date was right the entire time.

I told you twice — on 08-10 and again on 08-11 — that I would not trade an 08-12 TECH earnings event, and recommended flagging it for suppression. **That was wrong, and if you had acted on it you'd have been positioned against a print that arrived exactly where the calendar said it would.** The date was never mis-written (I held rather than confirming), but the narrative around the hold was far more confident than the evidence justified, and that's the part that reached you.

**What actually went wrong.** Every individual observation across those eight sessions was accurate. The inference was not, for one specific reason: **I never verified that Bio-Techne issues a fiscal-Q4 advance PR at all.** The "~14–22 day lead" I kept measuring the silence against came from its *Q3* cycle. So "no PR yet" was absence measured against a channel I had never confirmed exists for this quarter — which is the same error as FLO (right company, wrong feed) and NTRA (current feed, wrong channel), now for the third time. Two compounding factors made it worse: six restatements of the *same* signal read as six independent ones, and the live Merck KGaA merger supplied a plausible story (the AES/EA shape) that made a hunch feel like a mechanism.

The cheap check that would have killed this on day one: **did the year-ago same quarter have an advance PR before it?** One search. I never ran it.

**What I've changed.** The cadence memory now carries the rule explicitly — an absence argument is only as strong as the verified existence of that channel *for the matching quarter*; without that, the honest output is "date unsourced," never "probable phantom." I'd rather flag this loudly than let it sit as a quiet correction, because the failure mode here isn't a wrong date, it's confident-sounding advice built on an unexamined premise, and that's the more expensive kind.
### ✅ Correction to my own notes: nCino's IR site exists — I'd written it off on an untested prefix — 08-10

For four sessions I've told you nCino "has no IR host at any prefix" and that its advance PR is GlobeNewswire-only. That's wrong. `investors.ncino.com` and `ir.ncino.com` really are both NXDOMAIN — but the live host is **`investor.ncino.com`**, singular, and it serves the "nCino Announces Timing of its Q\<n\> … Conference Call" releases directly. Nobody had tried that prefix.

Nothing was mis-dated because of it — NCNO is held either way, its PR isn't due until ~08-12 — but the reasoning was unsound, and it's a shape worth naming because it's the third instance this month: **a negative result about one path written down as a fact about the company.** STE was a wrong hostname, NTRA was the right feed but the wrong channel, this was two-thirds of a hostname search. `investor.` / `investors.` / `ir.` are all in live use across our coverage, so "no IR host" needs all three tested before it goes in writing. The correction is in the cadence memory and the URL is cached.

### 🐞 The `--write` bug in the session prompt is still there — it would have cost every write today — 08-10

Recurrence marker on the 07-31 note further down, not a new finding. Step 6 of the injected `.session_prompt.md` still gives the `datalake.db` IR-URL update **without `--write`**, so a session following it literally caches zero IR URLs while printing "No results returned" as if it worked. `CLAUDE.md` step 7 has it right; the prompt template in `launcher.py` does not. I used `--write` on both databases and verified the rows.

One new adjacent trap worth adding to that fix: **backslash DB paths break under the bash tool.** `--db E:\options_scanner\data\performance.db` arrives with the backslashes eaten, `direct_db_query.py` silently creates an empty database at the mangled path, and then reports **`no such table: earnings_date_disputes`** — a message that reads like a schema or permissions problem, not a path problem. Forward slashes work. Cheap fix on the tool side would be to reject or normalise a `--db` path that doesn't already exist rather than creating one.

### ⚠⚠ MKTX was dated TODAY and the earnings already happened — a week ago — 08-07

**MarketAxess's Q2 came out on 2026-07-30, not today.** DB had `2026-08-07 bmo`, and so did MarketAxess's own advance PR from 07-15 ("Friday, August 7, 2026, before the market opens," call 10:00am ET). What actually happened on **07-30**:

- **07:44 ET** — 8-K, items 1.01/5.02/7.01: **Intercontinental Exchange will acquire MarketAxess.**
- **07:50 ET** — 8-K, item 2.02: **"MarketAxess Reports Second Quarter 2026 Financial Results."**

Six minutes apart. They pulled the release forward six weekdays to land it with the deal, and — this is the part worth internalising — **the scheduling PR was never retracted.** There is no "we moved it up" release, because the results release *is* the correction. Nothing has been filed since 07-30, and it's now well past MKTX's dead-consistent 07:35–07:50 furnish window.

So this is a phantom I hadn't seen before: not AES/EA (the event stops existing), but **the event moved earlier and left a stale, authentic, correctly-read company source pointing at an empty date.** I've written the screen into memory — for any symbol more than a few days out, check whether a 2.02 has *already* been furnished since the scheduling PR, which is free out of the sweep I already run, and weight it hardest for M&A names.

**I wrote nothing.** Confirming 08-07 locks a date with no event; confirming 07-30 puts a past date in an upcoming-earnings table. **Two asks:** (1) the row needs to move to Q3 or be cleared — I have no safe way to do that; (2) MKTX is being acquired by ICE, so its future earnings events are uncertain and it belongs on the M&A watch list alongside TECH and AMCR.

This is also the **third** finding this month that arrived as an *unconfirmed calendar row with no dispute row to write to* (AES 08-03, EA 08-04, now MKTX). The pattern is consistent: the unconfirmed class is where the dangerous ones live, and it's the one class where I have nowhere to record the finding. It will keep resurfacing every session until something can be written.

### ⚠ TECH — 6th session holding, and the picture hasn't moved — 08-07

No change to report, which is itself the report. `investors.bio-techne.com/rss` reads fine and is **still current only through 07-08**, still with no Q4 scheduling PR — now far past its 14–22d lead. The Merck KGaA acquisition is still live, so a missing PR remains non-neutral evidence rather than a shrug. DB carries `2026-08-12 bmo` (the bmo is solid — 06:30 ET, 8/8 quarters; it was the *date* I refused to lock). **Still needs your call.** I'll keep holding rather than lock a date the company hasn't stated.

### ⚠ SQM — I can now say *why* the feed is silent, which changes what your decision is — 08-07

Previously I reported "no Q2 PR yet" and left it ambiguous whether that was meaningful. It isn't: I confirmed this session that **SQM issues no advance scheduling PR at all** — the results release itself is the first notice (Q1 2026: "SQM REPORTS EARNINGS FOR THE THREE MONTHS ENDED MARCH 31, 2026" posted 05-26 21:57, with nothing before it). Its feed is current through 07-21 and empty *as expected*, so absence supports no inference here and never will.

That means the DB-08-18 / finnhub-08-19 split is **not** waiting on a source that's going to arrive. It's the structural release-vs-call ambiguity I flagged earlier: SQM releases ~22:00 ET (Santiago evening) with the call the following midday, so 08-18 is the release date and 08-19 is the call date, and both are "right" about different events. **This is a convention decision, not a research question** — which side should the DB carry for a foreign issuer whose release lands after the US close? Same class as EXPD. Once you pick, I can apply it consistently.

### ✅ NNE is resolved — and I owe you a correction, because I told you four times it was unresolvable — 08-06
I've been reporting NANO Nuclear's `unknown_time` as **structural**: it files zero Item 2.02 8-Ks (true — results go straight into the 10-Q), so the furnish-time technique can never read it, and I said it needed a default from you.

That conclusion was wrong, and the evidence was sitting in a channel I'd already been reading. NANO Nuclear's advance PR, published 08-05, says it *"will host its third quarter fiscal 2026 business update webcast on **Wednesday, August 12, 2026, at 5:00 p.m. ET**… The webcast will follow the anticipated filing of the … Form 10-Q."* A 5pm ET event after the 10-Q is **amc**, stated by the company, no 8-K involved. **Confirmed 2026-08-12 amc — no decision needed from you.**

The generalisable error: I collapsed *"my primary technique is blind here"* into *"this is unknowable,"* and then escalated. I've written the distinction into the cadence memory so the next structural-looking dead end gets a PR-channel check before it reaches you.

### ⚠ ATI's 8-K was missing at its own stated release time — one to eyeball at the 8:30am call — 08-06
ATI's own PR (07-14) says Q2 results publish **today at 6:30am CT / 7:30am ET**, with the call at 8:30am ET; its last four Item 2.02s furnished **07:33–07:45 ET**. I checked EDGAR at **~08:30 ET** and it had filed **nothing at all** — newest filing is 07-30.

By the rule I've been leaning on (absence past a tight furnish minute is a positive finding), that would read as "not reporting today." I did **not** apply it here, because a company scheduling PR naming the date explicitly outranks the clock, and EDGAR's submissions JSON does lag. So **I confirmed 2026-08-06 bmo on the PR's authority.** Most likely a late 8-K or feed lag, but it's the one confirm today whose corroboration didn't show up on time — worth a glance when the call runs.

### 📋 A framing correction on how I report my own results — 08-06
Worth knowing when you read my summaries. The `db_date` in the dispute list I'm handed is **frozen when the dispute is detected** and never refreshed, while the live calendar keeps moving as the feeds converge. Today all three of my "date corrections" had already self-corrected before the session started — FLO, WOLF and SJM were each already sitting on yfinance's (correct) date in the live table, even though my worksheet showed the old one.

So "the DB was wrong by 8 days" would have been a misleading way to describe that work. What I actually added on those three was an **authoritative lock** — a company source plus `date_confirmed_by='agent'` on a date that was otherwise resting on an unverified feed. Real value, but a different claim, and I'd rather state it accurately than inflate it. I've written the rule into memory: check the live row before calling something a save, and split the report into *corrected* / *locked* / *unchanged*.

The genuinely useful asymmetry underneath it: **the feeds converge on dates, but nothing upstream ever fixes bmo/amc.** Today's only true correction was SJM's time (`amc` → **`bmo`** — Smucker releases at 7:00am ET). Timing regressions are the class of error only this job catches, which is an argument for weighting `unknown_time` disputes higher than I have been.

### ⚠⚠ EA is a phantom, it's dated TODAY, and it's the second one this week — the suppression gap is now costing real signal — 08-04
Exactly the AES shape, one day later, and I still have nowhere to write it.

**The finding:** Electronic Arts filed its **Q1 FY27 10-Q on 2026-08-03 at 20:08 ET with no accompanying Item 2.02 8-K, no press release, and no conference call.** The results went out inside the 10-Q the previous evening. EA's IR feed carries game announcements only. The 07-30 8-K (item 8.01) states plainly: *"as of July 30, 2026, all regulatory approvals required to complete the Merger have been obtained"* — the $55B PIF / Silver Lake / Affinity take-private is cleared to close, and EA had **already** stopped holding calls (there was none for Q3 FY26). **There is no EA earnings event on 08-04.** The DB says `2026-08-04 amc`.

**Why I'm raising it again rather than just logging it:** this is the second phantom in three sessions to arrive as an **unconfirmed calendar row rather than a dispute row**, dated the same day it surfaces. My only writable path for that class is `earnings_confirm.py`, which would stamp a date on an event that doesn't exist. So — as with AES — I wrote nothing, and the finding lives only here and in the log, while the scanner goes on believing EA prints tonight.

Two phantoms in three sessions, both same-day, both invisible to the dispute table, is enough of a pattern that I'd argue the **symbol-level suppression list** is now the higher-value fix of the two I proposed on 08-03. The screen that catches them is cheap and already runs — *periodic report filed with no Item 2.02 within ±4 days* — it just has nowhere to put its answer.

### 🔴 TECH: the 08-05 date was wrong, and I can now prove it — but 08-12 has no source either — 08-05
**Resolution on the narrow question:** Bio-Techne did **not** report today. It furnishes its Item 2.02 at **06:30:1x–06:32 ET in eight straight quarters**; I checked EDGAR at **07:19 ET**, past that window, and it had filed **nothing at all**. For a filer that metronomic, an empty result past its own furnish minute is a finding, not a gap — so yesterday's "actively doubtful" is now simply "wrong," and it was knowable ~2 hours before the open.

**What that does and doesn't settle:** the live calendar had already rolled TECH to **2026-08-12** on its own (yfinance), so the immediate mis-trade risk is gone without my touching it. But **08-12 is not company-sourced either**, and its advance PR would have been due ~07-22–07-29 at Bio-Techne's 14–22 day lead. The feed reads fine and is current only through **07-08**; the IR calendar still says "no upcoming events," which for this company means nothing. The Merck KGaA acquisition is still live, so silence remains evidence rather than noise. My read is unchanged from yesterday: **Q4 most likely goes into the 10-K (FYE 06-30, due late August) with no call at all**, the AES/EA pattern.

**The decision I need is the same one, now cheaper to make:** do you want me to (a) keep holding at unconfirmed until something authoritative appears, (b) write 08-12 on yfinance's authority alone, or (c) treat it as a probable no-call event and flag it for suppression? I've held five sessions; (a) is still defensible but it is no longer producing new information.

*(Also worth noting the good news from the same check: this "absence at a known furnish minute is a positive finding" trick refuted TECH **and** TRMB in one SEC call, and confirmed CDW, COR and CRL in the same pass. It's now written into the cadence memory as a general technique.)*

### 🔴 TECH: fourth session holding, and the DB date is now TOMORROW — I need a decision — 08-04
Bio-Techne's DB date is **2026-08-05**. As of 07:30 today there is **no announced Q4 call**: the advance PR is ~21 days overdue against a 22-day norm (Q3's ran 04-14 for the 05-06 call), the IR feed is current through 07-08 and empty, and the only 8-Ks since the Q3 release are the **Merck KGaA merger pair** (06-25 item 7.01; 06-26 items 1.01/5.02). A company does not normally reach T-1 without announcing a call.

I've deliberately not locked it for four sessions because feed convergence isn't a company source, and that's still the right call — but the useful reading has changed. Through 08-03 my note was "unsourced." Today it's **actively doubtful**: under a live merger, a missing PR is evidence, not silence. My best guess is that Q4 gets folded into the 10-K (FYE 06-30, due ~late August) with no call, the same way AES and EA went quiet. **If you want a position taken rather than a fourth hold, say so and I'll write the reasoning in.**

### ⚠ An IR feed that returns HTTP 200 with items from 2016 — worth knowing before it bites something automated — 08-05
`https://www.allstateinvestors.com/rss/news-releases.xml` is live, well-formed, and serves ten items — **the newest dated November 2016.** Every probe I have classifies it as a healthy feed.

I care about this beyond Allstate because a large part of my method is *inferring from absence*: "the advance PR window has passed and the feed is empty, therefore the date is wrong." That inference is only valid against a feed that is actually current, and a decade-frozen feed defeats it silently while looking like evidence. A timeout is honest; this isn't. I've added a rule to memory to **read the newest `pubDate` before drawing any conclusion from feed contents**, and Allstate's real channel (`allstatenewsroom.com`) is now cached. No action needed from you — flagging it in case anything else in the scanner consumes IR feeds and assumes 200 means fresh.

### ⚠ A time correction I "wrote" three times never actually landed — worth a look at the write path — 08-04
TECH's `earnings_time` was **`amc` in the DB this morning**. My own logs record identifying it as `bmo` (06:30 ET furnish, 8 straight quarters) and writing it on **07-15, 07-27 and 07-31** — the 07-31 entry even describes the follow-up `date_confirmed=0` reset in detail. The value was still wrong today. I re-wrote it and verified it stuck this time.

I can't tell from my side whether those earlier writes silently failed, were rolled back, or were reverted by a later sync. Flagging it because a write that reports success and doesn't persist would quietly undermine every correction I make, and I'd only ever notice by accident — I only caught this one because I happened to re-read the row before writing the time again.

### ❓ ITUB: I think the DB date is a day early, but Itaú's site blocks me completely — 08-04
Itaú Unibanco is the only IR site today that beat me outright: **`itau.com.br` returns 403 on every path, to both a browser-UA `urllib` request and WebFetch.** No feed, no calendar, no PR.

What I could get is suggestive. Itaú's SEC 6-K **filenames** give away its cadence — the quarterly results cluster (`itubxpressrelease`, `itubxmaterialfact`, `itubxinstitutionalpre`, `itubxauditcommitteere`) landed **2025-11-05**, **2026-02-05** and **2026-05-06**, i.e. the first Wed/Thu of the month after quarter-end. That puts Q2 at ~**August 5**, not the DB's **August 4**, and no such cluster had been filed as of Aug 3. The time is unverified too: the Q1 material-fact was accepted **13:47 ET**, which is midday — the ambiguous band — so `amc` isn't established either.

I did **not** write anything, because filename-pattern inference is corroboration, not a company source. Flagging it because it's a live same-day row that I believe is wrong by a day, and because **if you have a way through Itaú's 403** (or want me to treat the 6-K filename cluster as sufficient for foreign filers whose sites block us), that would unlock ITUB and probably other LatAm names.

### 🔧 Broadridge (BR) has no reachable IR host — every prefix is NXDOMAIN — 08-04
Minor but it'll recur quarterly. `investors.broadridge.com`, `ir.broadridge.com` and `broadridge.gcs-web.com` all fail DNS outright; `broadridge.com/investors` and `broadridge.com/investor-relations` both 404. Per the STERIS lesson I checked whether I simply had the wrong host — but every variant genuinely fails, and Broadridge issues no advance scheduling PR either.

So BR's **only** company source is its own Item 2.02 8-K, which it furnishes at **07:59 ET, dead-consistent across 7 quarters**. **Update: this worked.** I left a background EDGAR poll running and it caught the filing at **07:59:07 ET** — within seconds of the predicted time — and BR is confirmed 08-04 bmo off its own filing.

Worth noting as a reusable route: for a symbol with no reachable IR presence but a tight, stable furnish time, **polling EDGAR at that time is a legitimate confirmation path**, not a workaround. It costs one background process and produces a primary source. If you know Broadridge's actual IR URL I'll still cache it, but this class is no longer blocked.

### ✅ Correction to my own 08-03 note: FLO *does* have a working feed — 08-04
In the browser-UA note below I called Flowers Foods "the one genuine holdout — 403s every path regardless of UA." That was wrong. **`www.flowersfoods.com/rss` 301-redirects to `flowersfoods.com/feed/` and serves 10 items** with the browser UA. I'd tested the paths but not followed that redirect.

It matters beyond tidiness: FLO's missing Q2 advance PR now counts as **real evidence** rather than "couldn't check," which strengthens the case that *both* DB's 08-14 (an old-regime Friday) and finnhub's 08-06 are wrong and the true date is ~08-20 (Thu).

### 🔓 Send a browser User-Agent. Most of my "this IR site is unreachable" history was self-inflicted — 08-03
This is the most useful thing I've found in a while and it's a one-line change wherever the sweep lives. The project UA (`options-scanner-earnings-researcher <email>`) is **rejected or tarpitted by a large share of IR hosts**, and the failure looks exactly like "slow site" or "no feed." I re-probed the hosts my own notes had written off, using a stock Chrome UA string, and **9 of 11 came back working on the first attempt**:

| Host | What my notes said | With a browser UA |
|---|---|---|
| `investors.paloaltonetworks.com` | "timeout — not cacheable" | works |
| `ir.sqm.com` | "times out on both paths" | works |
| `investors.bio-techne.com` | "RSS 404s" | works, 20 items |
| `investor.onsemi.com`, `investors.ametek.com`, `investors.amgen.com`, `investors.bwxt.com`, `ir.diamondbackenergy.com`, `ir.xiaopeng.com`, `ir.nanonuclearenergy.com` | timeout | all work |
| `ir.oneok.com` | HTTP 403 | works via a 301 |

**`WebFetch` has the same problem and it's worse, because it burns 60 seconds first.** WebFetch timed out on onsemi, ametek and amgen — the same three hosts that had just rejected the project UA — while a browser-UA `urllib` GET of those exact pages came back in under a second. Three of today's confirms (ON, AME, AMGN) were unobtainable any other way. **A WebFetch timeout on an IR host should be treated as "retry with a browser UA," not as a dead end.**

Two consequences worth your attention:
1. **It's why 16 confirms fit in one session** instead of the usual 4–6.
2. **It retroactively weakens some of my past reasoning.** I've repeatedly used "the feed is current and has no advance PR ⇒ the PR doesn't exist" as evidence. Where that ran off a *timeout*, it was never evidence at all. I've corrected the memory files; flagging it because a few carry-over judgements were built on it.

FLO is the one genuine holdout — `flowersfoods.com` 403s every path regardless of UA.

### ⚠⚠ AES is a phantom again, it's dated TODAY, and I have nowhere to record that — 08-03
Two separate problems, and the second is the one I can't fix from my side.

**The finding** (unchanged, now stronger): AES has filed **no Item 2.02 8-K since 2025-11-04**, while its 10-K (2026-03-02) and Q1 10-Q (2026-05-05) both went out with **no earnings release and no call** — three consecutive periodic reports with no event. Still listed (`tickers=['AES']`); the GIP/EQT take-private hasn't closed. **There is no AES earnings event to trade.**

**The problem:** AES arrived today as an **unconfirmed calendar row, not a dispute row** — and its DB date is **2026-08-03, i.e. today**, so the scanner believes it reports this session. The documented handling for phantoms is "resolve the dispute row as `skipped` and put the reasoning in `research_url`," but **there is no dispute row to write to**. My only writable path for that class is `earnings_confirm.py`, which would stamp a date on a symbol that has no event — the exact thing that handling exists to prevent. So I wrote nothing, and the finding survives only here and in the log.

**What I'd suggest:** either a `no_event` / `skipped` state reachable for unconfirmed calendar rows, or a suppression list the calendar respects. Until one exists this will resurface every session *and* silently re-arm the "AES reports today" signal. Note it stopped appearing for a couple of days after 07-29 and has now come back through a different door, which is why a symbol-level suppression is probably the more durable fix than anything dispute-table-shaped.

### ✅ Calibration, in the pipeline's favour: all 16 "unconfirmed" rows were already correct — 08-03
Worth knowing before anyone treats `unconfirmed` as a synonym for `suspect`. I company-sourced 16 unconfirmed calendar rows today (ARE, BWXT, CLX, CNH, FANG, INSP, MAR, OKE, ON, TSN, ADM, AMD, AME, AMGN, ANET, APO) and **every one matched the DB's date *and* bmo/amc exactly**. Zero corrections. The rows weren't wrong, they just had no provenance attached.

That's a different failure mode from the dispute rows and probably deserves different handling — these were cheap to verify in bulk and none of them needed judgement. If the goal is to burn down the unconfirmed backlog, a batch RSS sweep is very high yield; if the goal is to catch errors, the disputes are still where they live.

### ❓ WDS (Woodside): I moved the date +1d, and there's a convention question behind it — 08-03
Woodside's own investor calendar lists **Half-Year 2026 Results on 25 Aug 2026**; the DB had **08-24 Unknown**. I wrote **08-25 bmo**. The reasoning, because you may want a different convention:

Woodside is an ASX filer, so the release hits the market on the Australian morning of the 25th — which is **~17:30 ET on the 24th**, after the US close. The ADR therefore gaps at the **Aug 25** US open. Last year confirms the mechanics: H1-2025 hit the ASX on Tue **19 Aug 2025**, and EDGAR (whose timestamps are ET) accepted the matching 6-K at **2025-08-19 07:32 ET** — same calendar date, pre-market.

**The ambiguity I want you to arbitrate:** "08-24 amc" and "08-25 bmo" describe the *same overnight gap*, so both are defensible; I picked the one matching the company's published date. If the scanner's window logic treats those two encodings differently, tell me which you want for foreign filers and I'll apply it consistently — this same shape recurs for SQM (Chilean, ~22:00 ET release) and every ASX/HK name.

### ⚠ Inspire (INSP) published the wrong earnings date and corrected it 90 minutes later — 08-03
Small but genuinely dangerous, and I nearly took the wrong one. Inspire's advance PR on 07-06 08:00 was titled *"to Report Second Quarter 2026 Financial Results on **July 6, 2026**"* — the date it was published. At 09:48 the same morning they reissued it as *"**Correction:** … on **August 3, 2026**."* **Both items sit in the feed, and the broken one sorts first on a naive title match.** August 3 is correct (confirmed in the corrected body: "after the close of trading on Monday, August 3").

The general rule I've added to memory: **when two scheduling PRs for the same quarter appear close together, prefer the one prefixed "Correction:".** If any automated scraping of these feeds gets built, that's worth encoding — a company's own PR being wrong is a failure mode I hadn't hit before.

### ⚠ The dispute list I'm given is a stale snapshot — the live datalake had already fixed 3 of today's 5 confirms — 07-30
Plumbing issue, probably a cheap fix, and it's costing real slots. On three of today's five confirms the injected `<dispute-list>` showed one date while `earnings_upcoming` **already held the correct one**:

| Symbol | Dispute list said | `earnings_upcoming` already had | Company PR (my confirm) |
|--------|-------------------|--------------------------------|-------------------------|
| GO | 2026-08-04 | **2026-08-12** | 2026-08-12 ✅ |
| GRAL | 2026-08-11 | **2026-08-05** | 2026-08-05 ✅ |
| ZM | 2026-08-20 | **2026-08-25** | 2026-08-25 ✅ |

The feeds had caught up overnight; the snapshot hadn't. Two consequences: (1) I spend slots re-deriving corrections the datalake has already made, and (2) — worse — **my own reasoning gets poisoned**, because I compare "DB vs finnhub vs yfinance" using a DB value that is no longer the DB value. I wrote "DB is wrong by 8d" about GO when the live table was already right. Same shape as SMCI on 07-22, so this is at least the second occurrence. If the hook read `earnings_upcoming` at injection time instead of a snapshot, or stamped the snapshot's age, both problems go away. **Not urgent-urgent, but it silently degrades the quality of every date_disagreement judgement I make.**


**Recurred again 2026-08-20 — occurrence #4, and it hit 2 of the 3 resolvable disputes.** The list gave
me **GOLD 09-08** and **KR 09-10**; `earnings_upcoming` already held **09-02** and **09-11**, which is
exactly what the company PRs said. So both looked like a 6-day and a 1-day save right up until
`earnings_confirm.py` printed `(was: 2026-09-02 amc)` / `(was: 2026-09-11 Unknown)` — that `(was: ...)`
line is currently the *only* thing standing between me and reporting two corrections I did not make.
Today it cost nothing but a double-take, because I check it every time now. What it does cost every day
is the opener table: I print "DB date" values the DB no longer holds, and I reason about
"DB vs finnhub vs yfinance" on a value that is stale. **The ask is unchanged and small: have the hook
join against live `earnings_upcoming` at injection time, or stamp the snapshot with its age.**

### 🐛 `direct_db_query.py` splits `--sql` on `;` — including inside string literals — 07-30
Cost me 17 silently-failed writes today. The tool splits its `--sql` argument on semicolons to allow multi-statement input, but it doesn't respect quoting, so this:

```sql
UPDATE earnings_date_disputes SET research_url='no PR yet; next-check 07-31' WHERE ...
```
dies with `SQL Error: unrecognized token: "'no PR yet"` — **and the process still exits 0**. That's the same "exit code proves nothing" family as the 07-27 shell-quoting bug. I caught it with the standing follow-up-SELECT rule and worked around it by stripping semicolons from note text, so today's 28 rows are all correctly written — but a proper fix would be to split on `;` only outside string literals, or add a `--single-statement` flag. Flagging it because **any** caller writing free text into a TEXT column hits this, not just me.

### 📉 Calibration reversal you should know about: the `+364d` cadence check went 3-for-6, not 2-for-2 — 07-30
I promoted this check to a "corroborator" on 07-28 after it predicted MCHP and HD exactly. Today it was **wrong on three of five** company-sourced symbols — GO (−8d), GRAL (+6d), ZM (−5d) — and in all three I'd used it the day before to write "⇒ DB backed" in my carry-over table. So the honest record is 3 right / 3 wrong, and I've demoted it back to a defensive sanity guard in memory.

**The useful thing that fell out of it:** the misses and hits separate cleanly on *which feed* disagrees. Where **yfinance** disagreed with DB, yfinance was right all three times (GO, GRAL, ZM) and DB + cadence were both wrong. Where **only finnhub** disagreed (HRB), DB + cadence were right and finnhub was the known +7d artifact. That's a much better prior than anything the arithmetic gives, and it's now the rule I'll work from: **yfinance dissent ⇒ DB is the suspect side; finnhub-only dissent ⇒ probably the week-shift.** Might be worth weighting the two feeds differently in the dispute scorer, if it currently treats them as equivalent.

### ⚠ IAC has now burned a slot for FOUR consecutive sessions (07-27 → 07-30)
No new diagnosis — just the recurrence count, since that's the actionable part. IAC is **People Incorporated, ticker PPLI, since 2026-06-04** (CIK 1800227); re-verified today that IAC is absent from SEC's `company_tickers.json` and PPLI is present. The underlying event is real and correctly dated (**08-03 amc**), so this is a **symbol rename**, not a research problem — I can't resolve it by confirming, and confirming would be wrong because it'd stamp a date onto a ticker that no longer trades. It will keep surfacing every weekday until there's a rename path. (AES and APLS stopped surfacing after 07-29, so whatever handled those may cover this too.)

### 💡 SOLVED (mostly): the SPA problem — IR sites serve their press releases as plain RSS/XML — 07-27
The recurring "IR page is JS-only, WebFetch sees an empty shell" blocker has a cheap general workaround. Most of these sites are **Q4 Inc.-hosted, and Q4 exposes the press-release list as XML** at `/rss/pressrelease.aspx` or `/rss/news-releases.xml` (a couple answer plain `/rss`). It fetches fine with plain `urllib`/`curl`.

Today it found **3 advance earnings PRs that WebFetch, domain-restricted WebSearch, and EDGAR had all missed** — **two of them published that same morning** (Oklo 06:30 ET, Ferguson 06:45 ET). It also makes *absence* meaningful: if a feed is current and has no scheduling PR, the advance genuinely hasn't dropped, which is a real inference rather than a shrug. Worth knowing this **cannot be replaced by EDGAR** — advance-scheduling PRs are almost always wire-only, never an 8-K (re-confirmed today: zero scheduling 8-Ks across 31 CIKs).

Working on ~18 of the hosts I tried, including cisco, natera, monsterbev, hrblock, groceryoutlet, grail, jd, quidelortho, oklo, ferguson, bio-techne. Not on microchip, amcor, flowersfoods, steris, expeditors, standardaero, aaon, sea, xpinc, nu, aes, ypf. **Gotcha: the host prefix matters** — `investors.advanceautoparts.com` has no feed but `ir.advanceautoparts.com` does, so try both variants. Written up in `memory/reference_ir_rss_feeds.md`. **This is probably worth wiring into the pipeline** as a first-class source ahead of WebFetch.

*(Also FYI: the Chrome/browser extension was **not connected** this session — `tabs_context_mcp` returned "Browser extension is not connected." So the usual render fallback wasn't available; the RSS route covered for it. Worth a look if you expect browser automation to be available to me.)*

### ⚠ Correction to my own RSS host list — one wrong hostname made STE look unresearchable for weeks — 07-29
Direct amendment to the 07-27 note above, and worth reading if you wire the RSS sweep into the pipeline. My "no feed found" list included **`investors.steris.com`** — but that host **does not resolve at all** (DNS `ENOTFOUND`). STERIS's IR site is **`www.steris-ir.com`**. So STE wasn't a company-without-a-feed, it was **my wrong hostname**, and it had been sitting in the disputes as a `date_disagreement` on that basis. Today it took one search to find STERIS's own advance PR — *"a press release detailing financial results will be issued after the U.S. market closes on August 5, 2026"* — confirming **08-05 amc**, exactly what the DB already had, with finnhub's 08-10 wrong.

Two more host moves found the same session: **`ir.redwirespace.com` 301s to `ir.rdw.com`**, and **`ir.iac.com` 301s to `ir.people-incorporated.com`** — that second redirect is actually what surfaced the IAC→PPLI rename, which is a nice accident: **a 301 to an unfamiliar host is a ticker-rename signal**, not just a stale bookmark.

The generalisable bit for the pipeline: **a DNS failure and an HTTP 200-with-zero-items are completely different findings**, and only the second says anything about the company. My sweep had been collapsing both into "no feed." It now distinguishes `FAIL <ErrorType>` from `fetched, 0 items`, and the same distinction matters for the timeout problem in the note below — three different causes, three different meanings, one identical-looking empty result.

### ⚠ FLO (Flowers Foods): I think **both feeds are wrong** and the real date is ~08-20 — 07-28
Worth a look because nothing in the dispute system can catch this class. Flowers Foods **changed its reporting regime in Nov 2025**: it used to report **Friday morning ~07:1x ET (bmo)** and now reports **Thursday afternoon ~16:1x ET (amc)** — visible cleanly in its 8-K furnish times (2025-08-15 Fri 07:11 → 2025-11-06 Thu 17:27 → 2026-02-12 Thu 17:15 → 2026-05-21 Thu 16:10).

The DB's *time* has caught up (it says amc). Its **date has not**: **08-14 is a Friday** — an old-regime date. The year-ago Q2 was Fri 2025-08-15, and under the new regime Q1 slipped **+5d** and moved to Thursday (05-21 vs 05-16), which points at **~08-20 (Thu)**. So DB's **08-14** and finnhub's **08-06** are *both* likely wrong, and the true date is **later than either feed**. I did not lock anything — there's no company source yet and Flowers has no RSS feed — but this is the one date on today's list I'd actively distrust. Same failure mode as MSI (a wrong date with no feed dissent), except here the feeds do disagree and *both sides are wrong*, which is worse: a "resolve the disagreement" workflow would pick one and be wrong either way.

**07-29 addition — a third instance of this exact failure mode: AMCR (Amcor).** Same shape as FLO, caught the same way. Amcor's fiscal-Q4 furnish time **flipped from 16:13 ET (amc) in Aug-2024 to 06:14 ET (bmo) in Aug-2025**, and its most recent quarter (2026-05-06) furnished **06:05 = bmo** too. The DB still says **amc** for the 08-13 date. The *date* is fine (`+364d` backs it exactly, and finnhub's 08-19 is the usual +7d artifact) — it's the **time that looks like a stale-regime value**, which is the reverse of FLO, where the time had caught up and the date hadn't. I didn't write it: Amcor's Q1/Q2 filings sit at 17:1x–17:2x, which my rules class as *ambiguous, never amc*, so the recent-4 sample isn't unanimous on non-ambiguous observations and it needs a company source. Flagging because a bmo-vs-amc error is a whole-session directional mistake on the option, and **nothing in the dispute system looks at timing regime at all** — only FLO, CELH and now AMCR turned up because I happened to be reading furnish times.

Smaller sibling: **CELH (Celsius)** — DB says **08-10, a Monday**, but Celsius has reported **Wed/Thu, bmo, ~06:00–07:00 ET for nine straight quarters**, and year-ago+364d gives **08-06**. Here it's **finnhub (08-05) that looks better and DB that looks off-pattern** — the reverse of the usual. Also unlocked pending a company source; its advance PR is due ~07-29–08-03 on a 7–14d lead.

### ⚠ The IR RSS feeds are not reliably up — and an outage is indistinguishable from "no news" — 07-28
Follow-up to yesterday's RSS win, so you don't over-trust it if you wire it into the pipeline. Today **five hosts that worked perfectly yesterday** — `investors.hrblock.com`, `investors.monsterbevcorp.com`, `ir.jd.com`, `ir.cocacolaep.com`, `ir.nanonuclearenergy.com` — **timed out on every single attempt**, parallel and sequential, at 10s / 40s / 45s, while other Q4-hosted feeds on the same sweep answered instantly. WebFetch to those same hosts also timed out at 60s, so it wasn't the fetch method.

That matters because the technique's headline value is that **absence of an advance PR in a current feed is evidence**. A timeout produces the same empty result as a genuinely empty feed while supporting **no inference at all**. If this becomes a pipeline source, it needs to record *why* a feed came back empty (timeout vs. fetched-and-empty) and refuse to feed timeouts into any absence logic. My own reads for HRB/MNST/JD/CCEP/NNE today rest on search + EDGAR only, and I've flagged them as weaker than yesterday's in the log.

Two new working hosts found anyway: **`ir.celsiusholdingsinc.com`** and **`investors.amersports.com`** (the latter produced a confirm — Amer Sports' advance PR had published at **16:05 ET yesterday afternoon**, i.e. *after* the 07-27 session ran).

### ❓ EXPD: candidate for `dmh` — needs your call
Expeditors furnishes its Item 2.02 8-K **midday every single quarter** — 11:05, 11:18, 11:48, 12:37, 12:38, 13:00 ET — which is outside both my `bmo` (<09:30) and `amc` (16:00–16:50) bands, so my rules refuse to classify it. I checked its actual earnings release: it **states no time of day at all**, and Expeditors holds **no traditional conference call** (they publish written Q&A). So this isn't a gap in my evidence, it's a company that genuinely doesn't report on either side of the session. `earnings_confirm.py` accepts **`dmh`** — if you agree that's the right label for EXPD I'll set it, but I didn't want to invent a during-market-hours classification unilaterally. Its date (08-04) is uncontested by the feeds; only the time is open.

### ✅ Re: your question about a non-event resolution path — `skipped` already exists
You asked whether to add a `delisted`/`not_applicable` resolution so corporate-action symbols stop re-appearing. `performance_writer.py` (line ~450) already documents **`'confirmed_ben', 'confirmed_agent', 'unresolved', 'skipped'`** as the vocabulary, and `skipped` was previously unused. I used **`skipped` + a detailed `notes` string** for all 28 non-confirms today, so the reasoning is queryable per row rather than living only in the log. If you want dead tickers *fully* suppressed from the daily list that still needs a real flag (they'll keep generating dispute rows), but at least the resolution field now carries the distinction.

### ⚠ Data-quality: symbols the dispute system can't self-assess (corporate actions) — updated 07-27
These aren't date questions — they're symbols whose *event* is changed by a corporate action the tracker can't see:
- **APLS (Apellis)** — **acquired by Biogen** (deal announced 03-31-2026); Apellis filed **Form 15-12G** on 05-26-2026 (holders of record = **1**). Deregistered/delisting; will **not** report Q2 2026 independently — only Biogen reports consolidated. DB date **07-30 is invalid**. Recommend removing APLS (or mapping to BIIB). *(**07-27 hard confirmation**: the merger **closed 2026-05-14** and APLS is now **absent from SEC's `company_tickers.json` entirely** — the ticker no longer resolves to a CIK, which is about as definitive as delisting evidence gets. Still surfacing on the daily list.)*
- **~~SPCX~~ — CORRECTION (07-23): SpaceX is now PUBLIC and reporting.** My 07-22 note called this a private company with a bogus date and recommended removal — **that was wrong / now outdated.** On 07-21 SpaceX (ir.spacex.com) announced its **first-ever earnings report**: Q2 2026 results **after market close Tuesday Aug 4, 2026**, 4:30pm ET webcast, and the release triggers an **insider lock-up release schedule** (classic post-listing mechanic). **Confirmed 08-04 amc today. Keep the symbol — do NOT remove it.**
- **~~FERG (Ferguson)~~ — ✅ RESOLVED 07-27.** The fiscal-year-end change (Jul 31 → **Dec 31**, five-month transition Aug–Dec 2025) is real and now fully worked through: Ferguson reports on a **calendar** cadence, and its **own PR published 07-27 06:45 ET** confirms **Q2 results Monday Aug 10, 2026**, posted to the site at 6:45am ET with an 8:30am ET call ⇒ **08-10 bmo, confirmed**. The DB had already caught up to 08-10 (the suspect 08-04 is gone), and the time went Unknown→bmo. Nothing left for you to reset.
- **KVUE (Kenvue)** — pending **Kimberly-Clark acquisition**; Kenvue has **stopped hosting quarterly conference calls** (still files a results PR). No call to anchor timing; Q2 date not yet announced (DB 08-06 matches the Aug-6 historical but unconfirmed).
- **⚠ AES — escalated 07-27: there is probably no Q2 earnings EVENT at all.** My earlier note said AES was "still expected to report." The filing record says otherwise: **AES has filed NO 8-K Item 2.02 in all of 2026** (the last one is 2025-11-04), and **Q1-2026 was a bare 10-Q on 05-05 with no earnings release and no call** — the standard pattern for a company that has stopped reporting publicly while a take-private closes. The GIP/EQT consortium deal was signed 03-02, **stockholders approved it 06-26**, and it closes late-2026/early-2027. So the DB's **07-30** and finnhub's **07-29** are both unsourced guesses at an event that likely won't happen; the only real date is the next **10-Q, ~08-04** (2025's Q2 10-Q was 08-01). **Recommend dropping AES from earnings-based scanning until the deal resolves** — an earnings-window signal here would fire on nothing.
- **⚠ IAC — escalated 07-27: this is now a dead ticker, not a pending rename.** My 07-23 note said IAC "is renaming to People Incorporated." That already happened: the company is **People Incorporated** and the stock **moved from IAC to `PPLI` on Nasdaq effective 2026-06-04** (CIK 1800227 unchanged, CUSIP unchanged). **`IAC` no longer trades** and no longer resolves in SEC's ticker file. The row needs to be **re-mapped to PPLI or dropped** — as-is it's a phantom 08-03 print.
- **NEW 07-27 — TECH (Bio-Techne):** agreed **06-25** to be acquired by **Merck KGaA**. Still filing and still expected to report fiscal Q4 (DB 08-05), but flagging it because the KVUE/AES pattern is that acquirees quietly drop the call. Worth watching whether the Q4 FY26 call actually gets scheduled.
- **Still open from before:** **WBD** is mid **split into two companies** (DB 08-06 unconfirmed).
- **~~MCHP~~ — ✅ RESOLVED 07-28, and my 07-27 note was wrong.** I wrote that Microchip "stays unresolvable without a render." It isn't: the date lives on **`ir.microchip.com/news-events/ir-calendar`**, and that page **WebFetches cleanly** — I just hadn't tried it, having concluded from the missing RSS feed that the host was a dead end. It gives the answer verbatim: *"Q1 FY27 Financial Results Conference Call — Thursday, August 6, 2026 at 5:00PM (Eastern)/2:00PM (Pacific)"* ⇒ **08-06 amc, confirmed**, DB right, finnhub's 08-04 wrong. The URL is now cached. **Generalisable lesson: "no RSS feed" ≠ "no machine-readable source" — an IR *calendar/events* page is a different page from the press-release list, and it is often plain server-rendered HTML.** Same shape as HD, whose date is also events-page-only and also fetched fine today.

As of 07-27 these are recorded as **`resolution='skipped'` with the full reasoning in `notes`** (see the `skipped` item above) rather than left `unresolved`, so the distinction is queryable. They will still re-appear on the daily list until something suppresses the symbols themselves.

**07-29 update — third consecutive session, all three again. This is now the single most repetitive waste on the daily list.** Re-verified independently a third time: **APLS** submissions JSON returns **`tickers=[]`** and it is still absent from `company_tickers.json` (Biogen merger closed 05-14, Form 25 filed — it has not traded in **10 weeks**); **AES** still has **zero Item 2.02 8-Ks in 2026**, with both the 10-K (03-02) and Q1 10-Q (05-05) filed with no release and no call; **IAC** still resolves only as **People Incorporated / PPLI** (CIK 1800227). Running total: **~9 slots across three sessions**, and AES alone will keep generating one every session until its deal closes in **late-2026/early-2027** — that's on the order of 100+ more wasted researches if nothing changes. I've now written the detection up as a reusable **bulk pre-flight screen** (`memory/reference_ma_phantom_earnings.md`) so at least it costs one sweep instead of three investigations, but **the screen can't stop the rows being generated** — that still needs the `symbol_metadata` flag (`inactive` / `no_earnings_event`) checked by the dispute generator. Given it's recurred three days running and now has a bounded, known cost, I'd move this up from "low priority."

One concrete addition for whoever implements it: the two tells are cheap and both come from the SEC submissions JSON already being fetched — **`tickers=[]` or absent from `company_tickers.json` ⇒ delisted**, and **a 10-K/10-Q filed with no accompanying Item 2.02 for ≥2 consecutive quarters ⇒ still listed but no longer holds earnings events** (the AES case, which no ticker check catches). The second one is worth having generally — it's the same pattern KVUE is drifting into, and **TECH/WBD** are candidates.

**07-28 update — they did re-appear, all three, and I re-verified each independently rather than citing yesterday.** **APLS** and **IAC** are both still **absent from SEC's `company_tickers.json`** (the ticker→CIK lookup returns nothing), and **AES** still has **zero Item 2.02 8-Ks in 2026** (last: 2025-11-04). So a second day of research produced a second day of the same three non-answers. That's the concrete cost of having no symbol-level suppression: ~3 of every 25 symbols on the daily list are known-dead and consume a slot each session. The `skipped` resolution keeps the *reasoning* queryable but doesn't stop the row being generated — a `symbol_metadata` flag (`inactive`/`no_earnings_event`) checked by the dispute generator would end it. Low priority, but it recurs daily and will keep doing so until the AES deal closes (late-2026/early-2027).

### ⚠ Tooling hazard: `direct_db_query.py --write` reports success on failed SQL — verify every write
Separate from the missing-`--write` bug below, and arguably worse: **the tool exits 0 and prints "No results returned" whether the UPDATE matched 33 rows, 0 rows, or was invalid SQL.** Today a quoting bug in my own batched loop silently dropped **20 of 33** dispute writes while echoing success for every one; I only caught it because I re-read the table afterward instead of trusting the output. Nothing was lost (re-applied and verified by count), but a session that trusted the exit code would have reported 33 resolutions and written 13. Two cheap fixes if you ever touch that script: **print the `cursor.rowcount`** after a write, and **exit non-zero on `sqlite3.Error`**. Until then my own standing rule is: every dispute/metadata write gets a follow-up `SELECT` to confirm it landed.

### 🐞 BUG in the daily session prompt: steps 6 & 7 omit `--write` — those writes silently roll back
The embedded template in `launcher.py` gives the IR-URL and dispute-resolution commands **without `--write`**. `direct_db_query.py` **rolls back non-SELECT statements without that flag and still prints "No results returned"** — i.e. it looks like it worked. `CLAUDE.md` step 7 has `--write` correctly, so the two disagree and the *prompt* is the wrong one. Any session that followed the prompt literally recorded **zero** IR URLs and **zero** dispute resolutions while appearing to succeed. I used `--write` throughout today and verified the rows landed. **Please fix the template in `launcher.py`** (already captured in [[feedback-direct-db-query]], but the prompt keeps re-teaching the wrong thing).

### ⚠ `earnings_confirm.py` conflates "time verified" with "date verified" — 8 rows needed manual revert
`--date` is optional (passing only `--time` leaves `earnings_date` alone — good), **but `date_confirmed = 1` is set unconditionally** (line ~136). So there's no way to say "I trust the time, not the date." That matters because `unknown_time` disputes are exactly the case where I have strong time evidence and *no* company source for the date — and stamping `date_confirmed=1` suppresses the symbol from future dispute lists.
- Today I set 37 times from SEC data, then cadence-checked every date against its own year-ago filing and **reverted `date_confirmed=0` on 8** (ADT, ARE, DOC, HST, MRK, MSI, PSN, SNDK) whose DB date is 7–14d off cadence. Times kept, dates left open.
- **MSI is the case worth your attention:** DB says **07-30**, but Motorola's own Q2 8-Ks are **2025-08-07** and **2024-08-01** ⇒ DB is ~1wk early — and **no feed disagrees**, so nothing would ever have flagged it. My 07-13 session had already flagged this by hand; it's now corroborated. A wrong date with no feed dissent is the failure mode the dispute system structurally can't see.
- **Suggested fix:** a `--time-only` flag (or a separate `time_confirmed` column) so timing can be locked without asserting the date.

### FYI: the injected dispute list's "DB date" is a stale snapshot — 8 of 134 had already moved
`earnings_date_disputes` stores the DB date **as of when the row was written**; the live `earnings_upcoming` had since been refreshed for **PNR, DTE, SYY, EMR, FISV, ATI, NET, AMTM** — and in every one of those 8 the live DB now matches **yfinance**. So the opener table I print can show a date the DB no longer holds (PNR showed 07-21; live was already 07-28). Not harmful, but it makes the list look worse than it is, and it cost me a couple of confused `earnings_confirm` reads ("was: <already-correct>"). If the hook could join against live `earnings_upcoming` instead of the snapshot, the list would be more honest.

### 💡 New technique this session: SEC 8-K Item 2.02 furnish-time ⇒ bmo/amc (29 symbols, zero web calls)
`data.sec.gov/submissions/CIK*.json` exposes `acceptanceDateTime`; for Item 2.02 8-Ks the ET clock time of the furnish tells you the release side. Resolved **29 of the 69 `unknown_time` backlog in one pass**, and independently caught **6 wrong DB times** (DIS, FOX, FOXA, TECH, DKNG, SYY are **bmo** though DB said amc; **WMB** is **amc** though DB said bmo). Validated 31-agree / 7-disagree against known DB times, with all 7 disagreements proven to be DB errors (Disney's own PR: "release results before the opening of regular trading"). Written up in `memory/reference_sec_acceptance_time_timing.md`. **Two traps worth knowing** if you ever automate this: evening furnishes (17:00–22:00) are late paperwork for a *morning* release, not amc — KBR/LDOS would have been written backwards; and **recency beats majority**, because companies really do switch sides (ET moved amc→bmo in 2026, PODD in 2025, DIS ~2023). This might be worth folding into the pipeline as a default `earnings_time` when a feed says Unknown.

### ✅ DONE (07-31, at your request): `IAC` → `PPLI` renamed across the DBs
IAC Inc. renamed to **People Inc.**, Nasdaq ticker **IAC → PPLI** (CIK 1800227; SEC's `company_tickers.json` no longer resolves `IAC`). Ran `tools/symbol_lifecycle.py --rename IAC PPLI --no-interaction` — **3,960 rows across 3 DBs** (datalake, performance, `sector_archive/communication_services`), lifecycle event logged, zero `IAC` rows left. Also fixed in the same pass: `company_name` was **`N/A`** → now **People Inc.** (that blank name is exactly what made this look like a delisted phantom for four sessions running), and `ir_earnings_url` → `ir.people-incorporated.com/quarterly-results` (the old `ir.iac.com` 301-redirects there).

**The rename unblocked the research too** — searching "People Incorporated" immediately surfaced the company's Q2 PR where "IAC" had only returned aggregator noise. **Confirmed PPLI 2026-08-03 amc** (results after the close Mon Aug 3; call Tue Aug 4 8:30am ET — so the Aug 4 date floating around is the *call*, not the release). Dispute row resolved.

**Still worth considering:** this is the second rename after PSTG→P, and it's the dangerous shape — unlike a delisting, the company keeps filing and reporting, so nothing downstream looks broken and the bad symbol just sits there. A periodic ticker-vs-SEC-`company_tickers.json` reconciliation would catch these automatically instead of me finding them one at a time in the dispute list. The signal is cheap: a symbol in `symbol_metadata` that no longer appears in the SEC map is either renamed or delisted, and `submissions/CIK….json` says which.

### ⚠ YPF: 1-for-10 ADR ratio change effective 2026-08-04 — 6 days before its earnings date
Surfaced on `investors.ypf.com` while confirming YPF's 08-10 date. A 1-for-10 ADR ratio adjustment lands **2026-08-04**, i.e. inside the pre-earnings window. Flagging because ratio changes rewrite strike/contract terms and historical price series — if the scanner's YPF option chain or IV history spans 08-04, it'll see a 10x discontinuity that isn't a real move. Not an earnings-date issue; just adjacent to one I was already touching.

### Two symbols need a policy call from you (I can't resolve either by research)
- **NNE (Nano Nuclear)** — `unknown_time` here is **structural, not a research gap**. NNE has filed **zero Item 2.02 8-Ks, ever**; results go straight into the 10-Q, so there is no furnish time and no release/call to time. It has surfaced on multiple sessions and will keep surfacing forever. Want me to default it to something, or should it be excluded from the `unknown_time` sweep?
- **SQM (Soc. Química y Minera)** — a genuine ambiguous case like EXPD, but for a different reason: SQM releases at ~**22:00 ET** (Santiago evening) and holds the call the **following midday**. So the DB's 08-18 is the *release* date and finnhub's 08-19 is the *call* date — both are describing real events. The move lands in the **08-19** session, but calling a 10pm release `amc` isn't literally true. I left it `unknown_time` rather than force it. Your call on how the scanner should encode "evening release, next-day reaction."

### FYI: a bug I introduced and caught — SEC furnish times can't be timezone-converted
Not asking for anything; recording it because it nearly corrupted a batch. SEC's `acceptanceDateTime` is suffixed `Z`, and I "fixed" a DST bug by converting it UTC→ET. **The field is actually ET for some filings and UTC for others — Church & Dwight flipped between its own consecutive quarters** — so the conversion silently turned known 4pm **amc** filers (RDW, ROST) into midday "ambiguous" ones. All of today's writes survived re-verification against EDGAR's ET-rendered `Accepted` field, and my earlier memory values were right all along, but this would have quietly mis-timed a future bulk `unknown_time` sweep. Method note is now in `memory/reference_sec_acceptance_time_timing.md`: use the `Accepted` field on the filing-index page, one extra HTTP call per filing.

### FYI: 07-01 resolved only 6 of 28 — that's expected, not a miss
All 28 disputes sat at DB **07-21/22** with finnhub at **07-28/29** (+7d) across the board. On 07-01 only the companies that actually report **07-21/22** have live advance PRs (they dropped **06-30**), so I gold-standard-confirmed those six (GPC, NLY, HAS, WH, CSX, SAN) and skipped the 22 that report **07-28/29** — their advances won't exist until ~next week (next-check dates set 07-08/07-14). Researching them today would be the pre-PR wasted-cycle zone. **No cadence/convergence locks this session** — all 6 are company-sourced.
- **finnhub was +7d and wrong on every checkable name this batch** — all 6 confirmations backed **DB** (5 exact; HAS off by 1 day). This is the **inverse** of 06-30 (where DB was the stale one). So the +7d error flips direction week-to-week depending on which slice of the cluster surfaces; `finnhub disagreement = go research`, still never a tiebreak either way.
- **Two stale-page traps caught:** a "Robert Half Announces Schedule…" page was the **2024** release (not 2026); Pentair's "07-22" hit was the **2025** advance. Don't lock off a title/date match without confirming the year.

### ⚠ 06-30 session leaned hard on cadence/convergence locks — your call whether to keep (10 names)
The 06-30 session resolved **17 of 25**, but only **7 were gold-standard company-sourced** (REXR, KO, AGNC, NVS, KEY, BAC, C). The other **10 are convergence/cadence locks with no fresh company render** — KMI, CLF, LMT, EQT, SHW, RTX, CSGP (the late-July "+7d / 4th-Tue" cluster), plus SNA, WAL, FNB. Method = the same ELV-style triangulation the 06-26 session used: IR pages JS-only, so I anchored each date on the company's **confirmed prior-quarter day-of-week cadence** + agreement across finnhub/yfinance/aggregator "confirmed" flags. This is more aggressive than 06-26/06-29, which skipped such names. **If you'd rather these waited for company PRs, the 10 are listed in the research-log session entry (06-30) under "convergence / cadence locks" — easy to revert. The 7 company-sourced are solid.** Flagging because it's a deliberate policy shift, not a silent one.

- **Two have imminent company PRs — cross-check when they land:** **FNB** issues a "Schedules Q2…" PR (expected ~07-01) and **WAL** a release-date PR (~07-02). I locked both at **07-16** on cadence; if either PR says otherwise, correct it (don't trust my cadence lock over the company's own PR).
- **EQT lesson (caught & fixed in-session):** I first set EQT bmo off a TipRanks "Before Open" flag, then realized that flag was the **next-morning conference call**, not the release — EQT reports **after close** (Q1'26 04-21 amc). Corrected to **07-28 amc**. General rule now in the log: don't flip a time to bmo off a tracker's "before open" without checking the company's own release-vs-call pattern.

### Recurring tooling gap: FDX earnings date is browser-render-only (no scrapeable source)
FedEx Corp is the one name in my cluster with **no machine-readable company source for its earnings date**. It never files an advance scheduling 8-K and issues no advance PR; the date exists *only* on its JS-rendered IR upcoming-events page (`investors.fedex.com/news-and-events/upcoming-events/default.aspx`), which won't render via WebFetch or curl. This bit me on **06-15 and 06-18** — I correctly held FDX as a carry-over (feeds converging ≠ a company source, per the standing rule), and you had to **paste the rendered page** on 06-18 for me to confirm 06-23 amc. This will recur every quarter (next: Q1 FY27 call 2026-10-28). FedEx IR runs on Q4/Sequence, which usually has an underlying events JSON/XML endpoint — if you can find it (or expose the render some other way), I could self-serve instead of holding + pinging you. Low urgency, predictable cadence. Cached in `reference_company_cadence.md` (FDX row + SPA cheat-sheet).

### Minor: stray mailbox duplicates in `memory/` (safe to delete) — deletion still blocked
`memory/` contains three misplaced copies of outbox mailboxes — `for_market_analyst.md`, `for_system_analyst.md`, `for_trading_advisor.md`. These belong in `outbox/` (where the canonical, peer-readable copies live). Two are byte-identical to the `outbox/` versions; `for_system_analyst.md` is a **truncated 13-line subset** of the canonical 65-line outbox copy. They're not in `MEMORY.md` and carry no unique content. Looks like a 06-04-restore artifact. I retried the delete on **06-21** and the permission layer denied it again (same as 06-14) — `rm` on these is blocked for me. Please remove them (or re-allow): `rm memory/for_{market_analyst,system_analyst,trading_advisor}.md`.

### Proposal: move window-gating into `hooks/inject_context.py` (dev session)
Now that `memory/reference_company_cadence.md` exists (and is well-populated — 51 rows / ~55 tickers after the 06-14 maintenance), the hook could stop surfacing symbols before their advance-PR window opens (`window_opens = earnings_date − lead_time − buffer`) — killing the late-week 0-confirm churn at the source instead of me skipping by hand each morning. Written up in **`analysis/window_gating_in_inject_context_hook.md`** with the mechanic + 3 decisions for you (where lead-time data lives, suppress vs. footer, default lead time). Not urgent; for whenever you next do a dev session on the hook.

---

## Resolved

- **2026-06-14 — Injected dispute-list under-reported the DB → FIXED, note retired.** Saga ran 05-29 → 06-11: the `<dispute-list>` the hook injected diverged from `earnings_date_disputes` in *both* directions (real disputes JBL/KMX/KR on 05-29 and GIS/NKE on 06-11 were never injected; "unconfirmed calendar rows" that have no dispute row *were* injected). Root cause, fixed in your **06-11 dev session**: a `db_date <= today+14d` horizon gate on the disputes query hid disputes whose *stored* date was >14d out (the stored date is the value under dispute). Gate removed from the disputes query, kept on the unconfirmed-backfill query; injected list now split into "DISPUTES" vs "UNCONFIRMED CALENDAR ROWS" sub-headers. No recurrence on 06-12. I've dropped the defensive every-session cross-check (keeping a glance at the table as cheap insurance).

- **2026-06-14 — UEC chronic-wrong date: closed.** The impossible `2026-05-28` date that fired false earnings-window signals for 8+ sessions self-corrected to `2026-06-09 bmo` (feeds `conflict=0`) by 06-05, and **UEC reported 06-09 as predicted**. No manual DB intervention was ever needed; the resolver caught up on its own. Cadence entry in `reference_company_cadence.md` documents the no-advance-PR-for-Q3 pattern.

- **2026-06-14 — `earnings_date_disputes`-absent-on-Sunday: closed, did not recur.** On Sunday 06-07 the table didn't exist in `performance.db`; on weekdays 06-11/06-12 it was present and my UPDATEs persisted; **this Sunday 06-14 it is present again** (with the 06-11/06-12 rows). So the 06-07 absence was a one-off, not a Sunday-suppression behavior. Nothing actionable.

- **2026-06-14 — Weekend/Sunday maintenance proposal: marked IMPLEMENTED.** Everything `analysis/weekend_cleanup_proposal.md` proposed now exists and runs: `PROMPT_SUNDAY.md`, `STATUS.md`, `memory/archive/`, and the `<maintenance-session>` hook injection. Archive granularity landed as quarterly-by-earnings-season (not monthly) and is working well. Marked the proposal file's header IMPLEMENTED; flag me if you'd rather revisit any of it.

- **2026-06-14 — Workspace restore (~06-04) log/archive loss: closed (awareness only).** The git restore (`43c4af6` / `9cb08f1`) truncated `memory/archive/research_log_2026-Q2_spring-earnings.md` (849 lines → 524 bytes, lost most spring detail) and the active log (lost the 06-01→06-05 session entries). **Databases were untouched** (`data/*.db` aren't git-tracked). The operational ledgers (header tables, cadence) survived, so weekday work was never impaired. Truncation markers are now in the archive so the gap is explained, not mysterious. *If the transcript-restore tooling can preserve full file contents next time, that'd avoid the truncation — but no action needed otherwise.*

- **2026-06-07 — Maintenance day wiring confirmed correct.** The prior note flagged the 05-28 maintenance session firing on a Thursday. The 06-07 and 06-14 sessions both fired correctly on **Sunday**. The off-day 05-28 run was a one-off; weekly cadence is on Sunday.

- **2026-05-28 — Stray `inbox/` research artifacts cleared.** Moved all pre-staged SEC files (orcl/uec/cnm/gme `*_filings.json` / `*_search.json` / `*.html` + the 0-byte `jef_8k.htm`) from `inbox/` root into `inbox/processed/`. Inbox root is clean.

- **2026-05-27 — SEC.gov reachable via curl (now in memory).** `WebFetch` 403s on sec.gov, but `Bash` + `curl` with a UA (`klmn800alerts@gmail.com`) gets 8-Ks, the submissions JSON, and EDGAR full-text search. Promoted to `memory/reference_sec_via_curl.md`; SEC 8-K bodies are now a first-class confirmation source.
