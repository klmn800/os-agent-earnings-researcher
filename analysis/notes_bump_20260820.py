# -*- coding: utf-8 -*-
"""Bump the existing stale-snapshot note in notes_for_ben.md with the 08-20
recurrence (GOLD + KR). Appends to that section, does not open a new one."""
import io

p = "notes_for_ben.md"
s = io.open(p, encoding="utf-8").read()

anchor = "### ⚠ The dispute list I'm given is a stale snapshot"
i = s.index(anchor)
# find the start of the next section after it
j = s.index("\n### ", i + 10)

bump = """

**Recurred again 2026-08-20 — occurrence #4, and it hit 2 of the 3 resolvable disputes.** The list gave
me **GOLD 09-08** and **KR 09-10**; `earnings_upcoming` already held **09-02** and **09-11**, which is
exactly what the company PRs said. So both looked like a 6-day and a 1-day save right up until
`earnings_confirm.py` printed `(was: 2026-09-02 amc)` / `(was: 2026-09-11 Unknown)` — that `(was: ...)`
line is currently the *only* thing standing between me and reporting two corrections I did not make.
Today it cost nothing but a double-take, because I check it every time now. What it does cost every day
is the opener table: I print "DB date" values the DB no longer holds, and I reason about
"DB vs finnhub vs yfinance" on a value that is stale. **The ask is unchanged and small: have the hook
join against live `earnings_upcoming` at injection time, or stamp the snapshot with its age.**
"""

s = s[:j] + bump + s[j:]
io.open(p, "w", encoding="utf-8").write(s)
print("notes_for_ben.md: stale-snapshot note bumped with the 08-20 recurrence")
