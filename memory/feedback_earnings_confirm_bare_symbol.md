---
name: feedback-earnings-confirm-bare-symbol-trap
description: earnings_confirm.py — PATCHED 2026-09-16 (verified live 09-20) — --date and --by are now required, --time-only exists for time fixes, agent writes to ben rows are refused. The standing rule survives the patch — a date is confirmed only on a same-quarter company source. History of the three pre-patch traps kept below.
metadata:
  type: feedback
---

## Current state — the safety patch is LIVE (installed 2026-09-16, verified 2026-09-20)

My 09-14 patch (`analysis/earnings_confirm_patch/`, 34/34 checks) was installed byte-for-byte at
`tools/earnings_confirm.py` on 2026-09-16 (inbox note `2026-09-16_earnings-confirm-patch-installed.md`).
Verified on 2026-09-20: `--help` shows `--time-only`, `--by {ben,agent}` "required", and the footer
*"This tool only writes. To read a row, query earnings_upcoming."*

What the tool now does:
- **Bare `--symbol SYM` (no `--date`, not `--time-only`) fails with exit 2.** It can no longer silently
  confirm a row.
- **`--by` is required** (`ben` / `agent`), no default. The false-`ben`-stamp route is closed.
- **`--time-only`**: `--symbol SYM --time T --time-only --by agent` writes `earnings_time` and leaves the
  date and every `date_confirmed*` field untouched. **This replaces the plain
  `UPDATE earnings_upcoming SET earnings_time=...` workaround** — use the tool now.
- **An agent write to a row Ben confirmed is refused (exit 1)**, not just warned about.

**How to apply:**
- Company-sourced **date + time** this quarter ⇒ `--symbol SYM --date YYYY-MM-DD --time T --by agent`.
- Only the **time** is sourced (or settled from Item 2.02 furnish history) and the date is not ⇒
  `--symbol SYM --time T --time-only --by agent`. Never the full form.
- To **read** state, query the table — the tool is write-only:
  `direct_db_query.py --db E:/options_scanner/data/datalake.db --sql "SELECT symbol, earnings_date, earnings_time, date_confirmed, date_confirmed_by FROM earnings_upcoming WHERE symbol='SYM'"`
- SELECT the row after every write, as before.
- If `--help` ever stops showing `--time-only` (file reverted/overwritten), every pre-patch rule in the
  history below applies again in full.

**What the patch does NOT fix — the rule that still needs me:** the tool cannot know whether a date is
sourced. `--date D --by agent` on a date with no same-quarter company source still locks it, and a
locked row drops out of the normal dispute stream. **A date is confirmed only on a same-quarter
company source.** The 06-30 convergence batch (≥4 of 10 wrong) and the 09-08 KMX/PAYX locks were both
this error by different routes; only the second route is now closed by tooling.

## History — the three pre-patch traps (why the patch exists)

1. **Bare `--symbol` was a write stamped `ben`.** `confirm_symbol()` always set `date_confirmed=1,
   date_confirmed_by=?, date_confirmed_at=?`, and `--by` defaulted to `ben`. Hit 2026-08-19 (GME,
   reverted the same minute) and **2026-09-02 on four symbols in one loop** (CPRT, ORCL, CTAS, GIS), run
   to "inspect state". Knowing about the trap did not prevent the recurrence — the command was typed
   while chasing a different question and never registered as a write. A false `ben` stamp is
   self-sealing under CLAUDE.md's never-overwrite-Ben rule, which is what made it the worst mistake
   available here.
2. **"Assume the repair is irreversible" was wrong (corrected 2026-09-03).** The clearing UPDATE
   (`date_confirmed=0, date_confirmed_by=NULL, date_confirmed_at=NULL`) was refused by the permission
   classifier three times when I ran it unprompted, and passed first try once Ben said *"can you run
   the query?"*. **A permission denial is evidence about the current context, not a permanent fact
   about the command.** Surface a needed repair in `notes_for_ben.md` as *"here is the statement, say
   the word and I'll run it"* — don't hand Ben the work, and don't record a denial as a capability limit.
3. **A time fix through the confirm tool locked the date (2026-09-08, KMX + PAYX).** Both were
   `unknown_time` disputes; both 09-29 dates ended `date_confirmed=1 / agent` with no same-quarter
   source. PAYX drew a `confirmed_row_diverged` flag on 09-11 (yfinance 09-23 —
   [[confirmed-row-diverged-drift-signal]]); on 09-14 the company PR showed **PAYX was wrong by 6 days**
   (KMX happened to be right). The wrong lock stood 5 days with the PR already on the wire.
- If a `ben` stamp appears on a row dated before 2026-09-16 with no matching entry in
  [[research-log]], suspect trap 1 before trusting the attribution.

Related: [[feedback-direct-db-query]] (writes need `--write`),
[[reference-db-write-forward-slash-paths]] (`--sql` is split on `;` even inside string literals),
[[reference-sec-acceptance-time-timing]] (the evidence for settling a time without the date).
