---
name: feedback-direct-db-query
description: The direct_db_query.py tool rolls back UPDATE/INSERT/DELETE unless --write is passed on the command line
metadata:
  type: feedback
---

When calling `python E:\options_scanner\tools\direct_db_query.py` with any write SQL (UPDATE/INSERT/DELETE), you MUST include the `--write` flag or the tool prints "WARNING: Write statement detected but --write flag not passed. Changes rolled back." and does nothing.

**Why:** Safety guard on the tool — prevents accidental writes from read-only exploration. (Until 2026-09-16 the daily prompt template in `launcher.py` omitted `--write` on steps 6–7; it now includes it, matching `CLAUDE.md` — verified 2026-09-20. The rule itself is unchanged.) The guard is keyword-based: a read-only `PRAGMA table_info(...)` also trips the warning — harmless, the output is just suppressed; use `SELECT * ... LIMIT 1` to see columns instead.

**How to apply:** For every UPDATE/INSERT/DELETE call on datalake.db or performance.db via direct_db_query.py, append `--write` to the command. Read-only SELECT does not need it. See [[reference-db-write-forward-slash-paths]] for the two other silent-failure modes (backslash `--db` paths, `;` inside string literals).
