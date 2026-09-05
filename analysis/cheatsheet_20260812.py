# -*- coding: utf-8 -*-
"""Append 2026-08-12 host + corroborator findings to the cadence memory's
cheat-sheet and data-feed reliability sections."""
import io

p = "memory/reference_company_cadence.md"
s = io.open(p, encoding="utf-8").read()

CHEAT = "\n## Source-reachability cheat-sheet\n"
assert CHEAT in s
add_hosts = (
 "\n- **⚠⚠ Agilent (`A`) has NO RSS anywhere, and the live host has a `www.` prefix.** "
 "`investor.agilent.com` returns **200 with zero `<item>`s** on all six feed shapes (reads as "
 "\"feed exists but empty\" — it doesn't exist), `investors.agilent.com` fails with an **SSL "
 "hostname-mismatch**, `ir.agilent.com` is NXDOMAIN. The PRs live at "
 "**`www.investor.agilent.com/news-and-events/news/news-details/<yr>/<slug>`** and are reachable "
 "only by domain-scoped WebSearch. A fourth prefix shape to add to the `investor.`/`investors.`/"
 "`ir.` rotation: **`www.investor.`**.\n"
 "- **⚠ Williams-Sonoma's host is `ir.williams-sonomaINC.com`** — `ir.` and `investors.` on "
 "`williams-sonoma.com`, plus the gcs-web variant, are all NXDOMAIN. The company's legal name is "
 "in the domain. Found 2026-08-12; the symbol had no cached IR URL because of it.\n"
 "- **✅ CORRECTION 2026-08-12 — `investors.macysinc.com/rss/pressrelease.aspx` WORKS.** The "
 "long-standing \"macysinc.com events, browser-only SPA\" note was wrong; the feed carries both "
 "the advance and the results PRs.\n"
 "- **Seven of nine new symbols on 2026-08-12 answered to `/rss/pressrelease.aspx`** "
 "(netapp, salesforce, nvidia, veeva, gitlab, macysinc, williams-sonomainc). Probe that path "
 "first, always — it is the single highest-yield shape in this universe.\n"
)
s = s.replace(CHEAT, CHEAT + add_hosts, 1)

FEED = "\n## Data-feed reliability notes\n"
assert FEED in s
add_feed = (
 "\n- **⚠⚠ The Jul-quarter cohort breaks `+364d` in BOTH directions — 2026-08-12 produced "
 "two failures in one session.** **NTAP** moved Q1 a week *later* (2025-08-27 ⇒ 08-26, actual "
 "**09-02**) and **CRM** moved Q2 a week *earlier* (2025-09-03 ⇒ 09-02, actual **08-26**). Both "
 "DB dates were already right. Same-session, `+364d` was exact for A, NVDA, VEEV, GTLB and M. "
 "The corroborator's hit rate is fine on stable filers and unreliable on fiscal-quarter enders "
 "whose calendar shifts with the 52/53-week year — **never let it overrule a company PR, and "
 "never let it overrule a DB date that already matches yfinance** (the AAP rule).\n"
 "- **Enterprise-software / instrument makers announce EARLY — 21–29 day leads.** The "
 "2026-08-12 batch: A 29d, NVDA 28d, NTAP 22d, CRM 21d, VEEV 21d. That is double the 7–15d that "
 "dominates the rest of this table, so a symbol in this cohort **3–4 weeks out is worth checking, "
 "not gating**. The mirror-image warning is WSM at a **2-day** lead. Lead time is per-company and "
 "spans 2d to ~10 weeks across this universe — there is no usable default.\n"
)
s = s.replace(FEED, FEED + add_feed, 1)

io.open(p, "w", encoding="utf-8").write(s)
print("cheat-sheet + feed notes appended")
