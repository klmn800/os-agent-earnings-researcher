---
name: feedback-earnings-confirm-bare-symbol-trap
description: earnings_confirm.py is never a read and never a time-only write — a bare --symbol confirms the row as-is stamped 'ben' (08-19, 09-02); a --time fix through it locks an unsourced date (KMX/PAYX 09-08). Time-only fixes go through a plain UPDATE.
metadata:
  type: feedback
---

**`python earnings_confirm.py --symbol SYM` with no `--date`/`--time` does not
print the row — it CONFIRMS it**, writing `date_confirmed=1` and, because `--by`
defaults to `ben`, **`date_confirmed_by='ben'`**.

The tool's own `--help` lists `--symbol VZ` on its own as an example, right
underneath the full confirm form, which reads like a lookup. It is not one.
`confirm_symbol()` always appends `date_confirmed = 1`, `date_confirmed_by = ?`
and `date_confirmed_at = ?` to the UPDATE, regardless of which optional args
were supplied — there is no read-only path through that function.

**Hit twice.** 2026-08-19 on GME (reverted the same minute). **Recurred
2026-09-02 on all four of the session's symbols — CPRT, ORCL, CTAS, GIS — in a
single loop**, run to inspect state before deciding what to write. The recurrence
is the important half of this note, for two reasons:

1. **It was worse the second time, because the revert failed.** Two of the four
   were repaired implicitly by the real confirms that followed (`--by agent`
   overwrites the stamp). The other two, ORCL and CTAS, were **gated symbols with
   nothing to confirm** — and the corrective
   `UPDATE ... SET date_confirmed=0, date_confirmed_by=NULL` was **blocked by the
   permission classifier on all three attempts**, in single-symbol and batched
   form alike, so the damage had to be handed to Ben in `notes_for_ben.md` as SQL
   for him to run.
   ⚠⚠ **CORRECTED 2026-09-03 — “assume this is irreversible” was wrong.** When Ben
   read the note and said *“can you run the query?”*, the **identical** UPDATE
   (`date_confirmed=0, date_confirmed_by=NULL, date_confirmed_at=NULL WHERE
   symbol='CTAS'`) **passed the classifier on the first attempt** and the verify
   SELECT showed `0 / None / None`. So the gate is **not a property of the
   statement** — it is contextual, and an explicit in-session request from Ben
   clears it. **Repair is a one-line ask, not a permanent loss.**
   Still surface it in `notes_for_ben.md` (he has to know a false stamp exists at
   all), but **write it as “here is the statement, say the word and I'll run it”**
   rather than “you must run this yourself” — the old framing handed him manual
   work that I could have done on request, and left a wrong row standing for a day.
2. **Knowing about it did not prevent it.** This memory already existed, in full,
   with the fix — and the mistake still happened, because the command was typed
   while chasing a different question (what does the DB hold?) and never
   registered as a write.

**Why it matters:** CLAUDE.md's critical rule is *never overwrite a date
confirmed by Ben*. A false `ben` stamp is therefore self-sealing — it makes a row
that no future session (including mine) is permitted to correct, and nothing in
the row records that a tool default, not Ben, wrote it. A wrong date frozen
behind Ben's name is strictly worse than an unconfirmed one.

**How to apply:**
- **There is no reason to ever run `earnings_confirm.py` without `--date`.** If a
  command doesn't carry `--date` and `--by agent`, it is the wrong command.
- To **read** state, query the table — never the confirm tool:
  `direct_db_query.py --db E:/options_scanner/data/datalake.db --sql "SELECT symbol, earnings_date, earnings_time, date_confirmed, date_confirmed_by FROM earnings_upcoming WHERE symbol='SYM'"`
- **Always pass `--by agent`** on any `earnings_confirm.py` call, even ones that
  look like no-ops. Never let `--by` default.
- To write a **time** while leaving the date unsourced (the NIO/GME/CTAS shape),
  skip the confirm tool and `UPDATE earnings_upcoming SET earnings_time='bmo'
  WHERE symbol='SYM'` directly — ✅ **that plain-UPDATE path passes the
  classifier** (verified on CTAS, 2026-09-02). The
  `date_confirmed=0, date_confirmed_by=NULL` clearing form is blocked
  **unprompted**, but runs fine once Ben has asked for it (2026-09-03).
- If a `ben` stamp appears on a row with no corresponding entry in
  [[research-log]], suspect this bug before trusting the attribution.

**Third shape — 2026-09-08, KMX and PAYX: the confirm tool used for a *time* fix.** Both were
`unknown_time` disputes; the log called them *"time only, date not in dispute"*, but they went
through `earnings_confirm.py`, which sets `date_confirmed=1` unconditionally — so both 09-29 dates
were **locked with no same-quarter company source**, and a locked row is suppressed from the normal
dispute stream. Three days later PAYX drew a `confirmed_row_diverged` flag (yfinance 09-23), the
exact RTX/LMT/CLF/EQT shape from 07-17 ([[confirmed-row-diverged-drift-signal]]). `--by agent`
was passed correctly; the error was the *tool choice*. **Rule: if the date is not company-sourced
this quarter, the confirm tool is the wrong tool — use the plain `earnings_time` UPDATE above.**

**Fixes worth asking Ben for** (raised 2026-09-02): make `--date` or `--time`
required so a bare `--symbol` is a no-op, and make `--by` required rather than
defaulting to the most privileged value. A `--time`-only mode would also remove
the reason to hand-write UPDATEs at all.

**2026-09-14: Ben approved the fix, and it is staged, not applied.** Patch + 34-check test suite in
`analysis/earnings_confirm_patch/`. The write guard blocks my edits to `tools/`, so Ben has to copy
it in. **Check before relying on it:** if `tools/earnings_confirm.py --help` shows `--time-only`,
the patch is live. Then time-only fixes use `--symbol SYM --time T --time-only --by agent`, a bare
`--symbol` errors out, and agent writes to `ben` rows are refused by the tool. If it doesn't show
`--time-only`, every rule above still applies in full.

Related: [[feedback-direct-db-query]] (writes need `--write`),
[[reference-db-write-forward-slash-paths]] (`--sql` is split on `;` even inside
string literals), [[reference-sec-acceptance-time-timing]] (the evidence used to
correct a time without touching the date).
