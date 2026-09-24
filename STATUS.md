# Earnings Researcher — STATUS

> Lightweight dashboard for Ben. Maintained by the Earnings Researcher during its
> weekly maintenance session (`PROMPT_SUNDAY.md`). Glance here for current
> state without reading the full research log.

**Last updated:** 2026-09-20 (weekly maintenance); carry-overs/ledger refreshed by the 2026-09-23 session

---

## Needs attention Monday (09-21)

1. **No session ran Wed–Fri (09-16, 09-17, 09-18).** The orchestrator only launches me when the
   morning refresh flags ≥1 dispute (`ei_lite_refresh.py:339`); it flagged 0 all three days, so my
   logged next-check dates never ran. Details + a small fix: `notes_for_ben.md` (top item) and
   `analysis/proposal_20260920_spawn_on_due_next_checks.md`.
2. ~~UEC reports Thursday 09-24 and is still unconfirmed~~ **Resolved 09-22:** UEC's advance PR landed
   09-22 07:00 ET — it reports **Tuesday 09-29 `bmo`**, not 09-24 amc (+5d, time flipped). Confirmed.
4. **REXR (09-23):** its 10-14 date is held as probably wrong (advance PR overdue). Next check **09-24** — if no dispute fires that morning (finnhub 10-13 should keep it flagged, but the flagged reason was `unknown_time` and the time is now set), a manual session is needed to read `ir.rexfordindustrial.com/news-events/press-releases`.
3. ~~First reads for whichever session runs next~~ **Done 09-22:** CCL, MU, ACN, STZ all confirmed on
   company sources (ACN amc→bmo, STZ bmo→amc fixed). C confirmed 10-13 bmo; ACI time set bmo, date held.

## Open Carry-Overs

| Symbol | DB date | Why open | Next check |
|--------|---------|----------|------------|
| AMX | 10-13 amc (finnhub 10-20) | Company calendar feed found (Q4 `Event.svc`, cached as IR URL); Q3 is Tuesday amc every year (10-17/10-15/10-14) but **3Q26 not listed yet**. 10-13 fits the trend; 10-20 looks like the +7d artifact | **09-29**, then 10-06 |
| ACI | 10-13 (time now bmo, date unlocked) | FQ2 ends 09-12; the last two FQ2s reported 38d after quarter-end ⇒ **10-20**. Advance PR (BusinessWire, 14d lead) due ~09-29 → 10-06 | **09-30** |
| REXR | 10-14 amc (time set 09-23; finnhub 10-13) | No Q3 advance PR on the IR list (current through 09-17); leads 24–35d (3 obs) ⇒ a 10-14 release's PR was due by 09-20 — **overdue, date probably wrong**. 2026 quarters have been 4th-Thursday amc → 10-22 is the shape to expect (PR 09-17 → 09-28). | **09-24**, then daily to 09-29 |

**Confirmed-but-upcoming (locked, all re-verified against the DB today; don't re-research):**
CTAS 09-23 bmo, GIS 09-23 bmo, PAYX 09-23 bmo, DRI 09-24 bmo, MTN 09-28 amc, JEF 09-28 amc,
CNXC 09-29 amc, KMX 09-29 bmo, CAG 09-30 bmo, FDS 09-30 bmo, JBL 09-30 bmo, MKC 10-01 bmo,
NKE 10-01 amc, LW 10-06 bmo (weakest-sourced). LEN reported 09-16 and was pruned.
**Added 09-22:** UEC 09-29 bmo, CCL 09-29 bmo, MU 09-30 amc, ACN 10-01 bmo, STZ 10-06 amc, C 10-13 bmo.
**Added 09-23:** PGR 10-14 bmo, FHN 10-15 bmo, SYF 10-20 bmo (SYF/FHN snapshots were stale — the feed had already moved them).

**Advance-PR windows open on unconfirmed rows (not read yet):** PEP 10-08, DAL 10-09 (feed moved it from 10-08). MU, ACN, STZ were read and confirmed 09-22 (both contradicting times fixed from the company PRs). The **10-13 → 10-16 cohort (37 rows — banks,
JNJ, ABT, ASML, TSM…)** is inside its measured 27–35d lead window now; it reaches the 14-day horizon
starting ~09-29. Fall phantom watch (late Oct): AES, EA, MKTX, TECH, KVUE, WBD — M&A pre-flight first.

---

## Last Week's Calibration (09-14 → 09-18)

| Metric | Value |
|--------|-------|
| Sessions | **2 of 5** (09-14, 09-15). 09-16 → 09-18: none — zero disputes flagged ⇒ no launch |
| Symbols handled | 6 (JEF, UEC, CCL, MTN + priority carry-overs PAYX, KMX) |
| Confirmed | **4 — all company-sourced** (MTN, KMX, JEF; PAYX **corrected 09-29 → 09-23**) |
| Confirm rate | 4 / 6 (67%); the 2 open are the missed-check carry-overs |
| Skips later proven to be missed confirmable dates | **0 where testable** (JEF). UEC, CCL **untestable** — their checks never ran |
| Gate that fired on its predicted day | JEF (PR 09-14 16:30 ET = predicted; confirmed 09-15, 14d lead) |

**Read:** where the gate could be tested it was right to the day for the second week running (CTAS
09-09, JEF 09-14 — two cases, both off leads with ≥2 observations). The 09-08 write-side error is fully
unwound: PAYX corrected from the company PR, KMX sourced, and the confirm tool patched (your 09-16
install) so a time fix can no longer lock a date. The week's failure was machinery, not judgment — but
one piece of drift is mine: on 09-14 I wrote "read open-window rows the day the window opens" (MTN's PR
sat unread 10 days) and on 09-15 didn't do it for MU/ACN/STZ/PEP. It's now in the log header, not just
a session note.

---

## Maintenance Bookkeeping (09-20)

- **Archived:** sessions 09-01 → 09-03 (329 lines) → summer archive, verbatim, integrity-checked.
  Active log **761 → 503 lines** (62 KB → 44 KB) including today's entry.
- **Cadence table:** PAYX, KMX, MTN, CCL, DAL rows brought current with the 09-14/09-15 results;
  reachability cheat-sheet reconciled (Vail and McCormick → chronic 403; Jefferies RSS works).
- **Memory:** confirm-tool note rewritten around the live patch; `--write` note corrected;
  window-gating note gained the dispute-gated-session caution. `MEMORY.md`: 20 pointers, all resolve.
- **`notes_for_ben.md`:** 2 items closed and archived verbatim (patch installed; PAYX/KMX), 1 new top
  item (missed sessions), tool-fix list cut to what's still open. 170 lines.
- **Inbox:** patch-installed notice integrated → `processed/`. **Outbox:** ≤ 128 lines, no rotation.
- **Proposal:** `analysis/proposal_20260920_spawn_on_due_next_checks.md`.
