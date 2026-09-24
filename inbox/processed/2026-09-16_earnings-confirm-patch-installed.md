# earnings_confirm.py safety patch is live

**What changed:** Your 2026-09-14 patch (`analysis/earnings_confirm_patch/earnings_confirm.py`) is now installed at `tools/earnings_confirm.py`, byte-for-byte. Your 34-check suite passed (34/34) before install.

**Why:** Ben approved it on 09-14, but you couldn't write to `tools/`, so it stayed staged until today.

**Files touched:** `tools/earnings_confirm.py`. A stray copy in the repo root was moved to the Recycle Bin.

**Impact on your research:**
- `tools/earnings_confirm.py --help` now shows `--time-only`, which is the check your memory `feedback_earnings_confirm_bare_symbol.md` says to run. The patch is live.
- Time-only fixes: `--symbol SYM --time T --time-only --by agent`. This replaces the plain `UPDATE earnings_time` workaround. The date and every `date_confirmed*` field stay untouched.
- Running `--symbol` without `--date` (and not in `--time-only` mode) now fails with exit 2. `--by` is required, with no default. An agent write to a row Ben confirmed is refused with exit 1. Before, it printed a warning and went ahead.
- Update the memory note so it points to the new tool path instead of saying the patch is only staged.

## Also: the launcher prompt now includes `--write`

In `launcher.py`'s `PROMPT_TEMPLATE`, steps 6 (save IR URL) and 7 (update dispute resolution) now pass `--write` to `direct_db_query.py`. That matches `CLAUDE.md`. Your memory `feedback_direct_db_query.md` says "The session prompt examples omit `--write`". That's no longer true. The rule itself still holds.
