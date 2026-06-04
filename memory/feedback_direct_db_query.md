---
name: direct_db_query requires --write for writes
description: The direct_db_query.py tool rolls back UPDATE/INSERT/DELETE unless --write is passed on the command line
type: feedback
---

When calling `python E:\options_scanner\tools\direct_db_query.py` with any write SQL (UPDATE/INSERT/DELETE), you MUST include the `--write` flag or the tool prints "WARNING: Write statement detected but --write flag not passed. Changes rolled back." and does nothing.

**Why:** Safety guard on the tool — prevents accidental writes from read-only exploration. The session prompt examples omit `--write` but it is required.

**How to apply:** For every UPDATE/INSERT/DELETE call on datalake.db or performance.db via direct_db_query.py, append `--write` to the command. Read-only SELECT does not need it.
