import io, re

p = 'memory/research_log.md'
t = io.open(p, encoding='utf-8').read()

# 1) insert session entry
entry = io.open('analysis/session_entry_20260902.md', encoding='utf-8').read()
anchor = "# Research Sessions (newest first)\n"
i = t.index(anchor) + len(anchor)
t = t[:i] + entry + t[i:]

# 2) carry-over table: CPRT resolved, ORCL updated, CTAS added
lines = t.split('\n')
out = []
cprt_done = orcl_done = False
for ln in lines:
    if ln.startswith('| CPRT | 2026-09-03 |') and not cprt_done:
        out.append("| ~~CPRT~~ | ~~2026-09-10~~ | **RESOLVED 09-02: 2026-09-10 `amc`** — the advance PR *\"Copart, Inc. to Release Fourth Quarter Fiscal 2026 Results\"* published **09-01 at 10:34 ET on BusinessWire**, one day after the 09-01 session correctly ruled DB's 09-03 out on the absence floor. Verbatim: *\"will release earnings for the fourth quarter of fiscal 2026 **after 4:00 p.m. Eastern Time** (3:00 p.m. Central) **on Thursday, September 10, 2026**,\"* call 5:30pm ET. Found via `stocktitan.net/news/CPRT/` JSON-LD; wire permalink `businesswire.com/news/home/20260901213040/en/`. ⚠ Three channel-model corrections fell out of it — **the advance PR is BusinessWire** (the 08-24 \"it's PRNewswire\" correction came from a corporate release and does not transfer), the **Q4 lead is 9d** (not the 7–8d the row had just narrowed to), and it publishes **mid-morning, not post-close**. | done |")
        cprt_done = True
        continue
    if ln.startswith('| ORCL | 2026-09-10 |') and not orcl_done:
        out.append("| ORCL | 2026-09-10 | **09-02: the decisive read fired, and it eliminated 09-08.** Feed live (`investor.oracle.com/rss/pressrelease.aspx`, 200, 10 items) and newest item is **still the 06-10 Q4 results PR** — the *Sets the Date* advance has not published. EDGAR agrees the company has been quiet: **no filing of any kind since 2026-07-28**. Absence through **09-01 16:01 ET** plus the **7d minimum** lead ⇒ release ≥ **09-09**, so the 09-08 candidate the 08-28 session raised on `+364d` is now **dead**. DB's **09-10** is the only surviving in-band date and finnhub's **09-14** would need a PR on 09-05..09-07 (09-07 is Labor Day) — but cadence is not a company source, so **still no lock**. PR due **09-02/09-03** at the 7–9d band, posting ~16:01 ET. | 2026-09-03 |")
        orcl_done = True
        continue
    out.append(ln)
t = '\n'.join(out)

# 3) add CTAS carry-over right after the ORCL row
ctas_row = "| CTAS | 2026-09-23 | **09-02: gated — the advance PR is not due until ~09-09, and this symbol had no cadence row before today.** Cintas **does** issue an advance: *\"Cintas Corporation Announces Webcast for \\<n\\> Quarter Fiscal Year \\<yr\\> Results\"* — Q4 FY26 went out **07-01 13:29 ET** for a **07-15** release, a **14d lead (1 observation only — needs a 2nd)**. Newest CTAS wire item is **08-10**, so today's absence carries no information. ⚠⚠ **The stored time `amc` is provably wrong: Cintas is bmo, 6/6 quarters** (Item 2.02 acceptance 08:31–08:34 ET, release says *\"today reported\"*, webcast 10:00am ET). Not confirmed — the CLI has no time-only mode and the date is still unsourced. ⚠ **No first-party host exists**: `investors.cintas.com` and `ir.cintas.com` are **NXDOMAIN**, `cintas.gcs-web.com` resolves but 403s on every path. Q1-only Item 2.02 history **2025-09-24 (Wed), 2024-09-25 (Wed), 2023-09-26 (Tue)** steps one day earlier each year ⇒ **09-23 = DB**; finnhub's 09-30 is a week outside that band. | 2026-09-08 |"
i = t.index('| ORCL | 2026-09-10 | **09-02:')
j = t.index('\n', i) + 1
t = t[:j] + ctas_row + '\n' + t[j:]

# 4) Upcoming Confirmed rows
anchor2 = "## Upcoming Confirmed — locked dates (don't re-research)"
k = t.index('|--------|------|------|--------------------|', t.index(anchor2))
k = t.index('\n', k) + 1
new_rows = (
    "| CPRT | 2026-09-10 | amc | 09-02; Copart advance PR (09-01 10:34 ET, BusinessWire) — *\"after 4:00 p.m. Eastern Time … on Thursday, September 10, 2026,\"* call 5:30pm ET. **DB snapshot 09-03 was wrong by +7d**; finnhub's 11-18 was next quarter entirely |\n"
    "| GIS | 2026-09-23 | bmo | 09-02; General Mills advance PR (08-26 08:00 ET, BusinessWire) — reports fiscal 2027 Q1 on Sep 23, release **issued that morning**, Q&A webcast 8am CT. **TIME SET Unknown→bmo**; DB date right, finnhub's 09-15 wrong |\n"
)
t = t[:k] + new_rows + t[k:]

io.open(p, 'w', encoding='utf-8').write(t)
print('research_log.md updated: session entry + CPRT/ORCL/CTAS carry-overs + 2 confirmed rows')
