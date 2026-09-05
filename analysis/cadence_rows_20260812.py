# -*- coding: utf-8 -*-
"""Promote the 2026-08-12 findings into memory/reference_company_cadence.md."""
import io

p = "memory/reference_company_cadence.md"
lines = io.open(p, encoding="utf-8").read().split("\n")


def repl(idx, prefix, new):
    assert lines[idx].startswith(prefix), (idx, lines[idx][:60])
    lines[idx] = new


repl(132, "| TECH |",
 "| TECH | Bio-Techne / fiscal Q4+FY (Jun qtr) | **bmo** | **unverified — see below** | "
 "⚠⚠⚠ **2026-08-12 — THE EIGHT-SESSION PHANTOM CASE WAS WRONG. The event was "
 "real.** Bio-Techne filed its Item 2.02 8-K on **2026-08-12 at 06:30:30**, on the 06:30–06:32 "
 "furnish minute it has held 8/8 quarters, items `2.02,8.01,9.01` — press release *\"describing "
 "the results of operations for the quarter and [FY ended June 30, 2026].\"* ✅ "
 "**Company-confirmed 2026-08-12 bmo.** The DB was right the whole time, and the notes here spent "
 "eight sessions building a case against it that culminated in a wrong recommendation (\"do not "
 "trade an 08-12 TECH earnings event\"). ⚠⚠ **Root cause, and the reusable lesson: the "
 "~14–22d lead was measured on Q3 (04-14 → 05-06) and NO ONE EVER VERIFIED THAT A Q4 "
 "ADVANCE PR EXISTS.** Eight sessions of \"no PR yet\" was absence read off an unverified channel "
 "— the FLO/NTRA failure, third occurrence — and the live Merck KGaA merger supplied a "
 "story (AES/KVUE shape) that made one repeated signal feel like six independent ones. `+364d` "
 "⇒ 08-05 was also wrong; Q4 moved a week later than 2025-08-06 / 2024-08-07. **Before "
 "running an absence argument, verify the channel exists for the MATCHING quarter — check "
 "whether the year-ago same quarter had an advance PR at all.** ⚠ Merger still live (PREM14A "
 "08-10); it did not stop the print. ⚠ Its IR calendar page reads \"no upcoming events\" even "
 "when a call is imminent — absence there is not evidence. | SEC Item 2.02 8-K (the filing IS "
 "the source); investors.bio-techne.com/press-releases |")

repl(98, "| M |",
 "| M | Macy's / Q2 (Jul qtr) | **bmo** | **~16d** | Issues \"Macy's, Inc. to Report \\<n\\> "
 "Quarter \\<yr\\> Results on \\<date\\>\" — **date in the title** (Q1: PR 05-18 07:30 → "
 "06-03 release = 16d). Its own results PR posts **06:55 ET** and the Item 2.02 furnishes "
 "~10:59–11:06Z ⇒ **bmo**; time written 2026-08-12. `+364d` off the 2025-09-03 2.02 "
 "⇒ **09-02**, which is the DB date; finnhub's 09-01 is a bare 1d dissent. ⚠⚠ "
 "**CORRECTION (2026-08-12): the feed `investors.macysinc.com/rss/pressrelease.aspx` WORKS** and "
 "carries both the advance and the results PRs — the long-standing \"macysinc.com events, "
 "browser only (SPA)\" note was wrong. ⚠ Prior burn: both yfinance and finnhub carried stale "
 "Q1 dates (05-27/05-26) into an actual 06-03 — feed dates for M are suspect near the window. "
 "| investors.macysinc.com/rss/pressrelease.aspx |")

repl(81, "| GTLB |",
 "| GTLB | GitLab / fiscal Q2 (Jul qtr) | amc | **none — issues no advance PR** | ⚠ "
 "**The COTY shape**: the feed is live and current but GitLab publishes **no scheduling PR**, only "
 "results releases — so an empty feed proves nothing and **the Item 2.02 8-K on the day is "
 "the only source** (that is how the 6/8→6/2 correction was made). Time is company-published "
 "even so: the results release posts to the IR feed at **16:05 ET** and the 2.02 furnishes "
 "20:07–20:17Z ⇒ **amc**; written 2026-08-12. `+364d` off the 2025-09-03 8-K ⇒ "
 "**09-02** = the DB date; **finnhub's 09-08 is a +6d artifact**. ⚠ "
 "`ir.gitlab.com/news-events/events/` 404s. | ir.gitlab.com/rss/pressrelease.aspx; SEC 8-K via curl |")

repl(140, "| VEEV |",
 "| VEEV | Veeva / fiscal Q2 (Jul qtr) | amc | ~21d | Issues \"Veeva to Release Fiscal \\<yr\\> "
 "\\<n\\> Quarter Results on \\<date\\>\" — **date in the title**, answerable off the feed "
 "with no fetch. ✅ Company-confirmed **2026-08-26 amc** (PR **08-05 16:05**): *\"after market "
 "close on August 26, 2026,\"* call 2:00pm PT / 5:00pm ET. Furnishes 20:04–20:05Z ⇒ "
 "16:0x ET, 8/8. `+364d` from 2025-08-27 ⇒ 08-26, exact. ⚠ Prior note (Q1): "
 "earnings_upcoming auto-updated 5/27→6/3 mid-cycle. | ir.veeva.com/rss/pressrelease.aspx |")

assert lines[168].startswith("| SNPS |"), lines[168][:40]
new = [
 "| NTAP | NetApp / fiscal Q1 (Jul qtr) | amc | **~22d** | Issues \"NetApp Hosts \\<n\\> Quarter of "
 "Fiscal Year \\<yr\\> Financial Results Webcast\" — the **title names the quarter, not the "
 "date**, so this one must be fetched. ✅ Company-confirmed **2026-09-02 amc** (PR **08-11 "
 "16:01**): *\"**After market close on September 2, 2026**, NetApp will announce financial results "
 "for the first quarter of fiscal year 2027, which ended July 31, 2026,\"* webcast **2:30pm PT**. "
 "Furnishes 20:05Z ⇒ 16:05 ET, 8/8 qtrs. ⚠⚠ **`+364d` FAILS here by 7d**: "
 "2025-08-27 ⇒ 08-26, actual **09-02** — NetApp moved Q1 a week later (the AAP/DE shape). "
 "The DB already had 09-02 and only the time was missing. | investors.netapp.com/rss/pressrelease.aspx |",

 "| A | Agilent / fiscal Q3 (Jul qtr) | amc | **~29d** | Issues \"Agilent to Announce "
 "\\<n\\>-Quarter Fiscal Year \\<yr\\> Financial Results on \\<date\\>\" — **date in the "
 "title**, a long lead ⇒ checkable ~4 weeks out. ✅ Company-confirmed **2026-08-26 amc** "
 "(PR **07-28**): *\"will release financial results for the third quarter of fiscal year 2026 "
 "**after the stock market closes on Wednesday, Aug. 26**,\"* call **1:30pm PDT**. Furnishes 20:06Z "
 "⇒ 16:06 ET, 8/8. `+364d` from 2025-08-27 ⇒ 08-26, exact. ⚠⚠ **NO RSS "
 "ANYWHERE**: `investor.agilent.com` returns **200 with zero `<item>`s** on all six feed shapes, "
 "`investors.agilent.com` fails with an **SSL hostname mismatch**, `ir.agilent.com` is NXDOMAIN. "
 "And the live host carries a **`www.` prefix** — "
 "`www.investor.agilent.com/news-and-events/news/news-details/<yr>/<slug>`. Find the PR by "
 "domain-scoped WebSearch. | www.investor.agilent.com (no feed; search-only) |",

 "| CRM | Salesforce / fiscal Q2 (Jul qtr) | amc | ~21d | Issues \"Salesforce Announces Date of "
 "\\<n\\> Quarter Fiscal \\<yr\\> Earnings Release and Webcast\" (**date NOT in the title** — "
 "fetch it). ✅ Company-confirmed **2026-08-26 amc** (PR **08-05 16:30**): results 08-26 "
 "**after market close**, broadcast **2:00pm PT / 5:00pm ET**. Furnishes 20:18Z ⇒ 16:18 ET. "
 "⚠⚠ **`+364d` FAILS by 7d**: 2025-09-03 ⇒ 09-02, actual **08-26** — Salesforce "
 "moved Q2 a week earlier. ⚠ A cached per-quarter deep link goes stale every quarter (the "
 "cached URL was still the Q1-FY27 one); cache the feed instead. | "
 "investor.salesforce.com/rss/pressrelease.aspx |",

 "| NVDA | NVIDIA / fiscal Q2 (Jul qtr) | amc | ~28d | Issues \"NVIDIA Sets Conference Call for "
 "\\<n\\>-Quarter Financial Results\" ~4wk ahead (**date not in the title**). ✅ "
 "Company-confirmed **2026-08-26 amc** (PR **07-29 17:00**): call **Wednesday, August 26 at 2pm PT "
 "/ 5pm ET**, results published **~1:20pm PT** the same day (= 4:20pm ET) with the CFO commentary "
 "posted immediately after. Furnishes 20:21–20:22Z ⇒ 16:2x ET, 8/8 qtrs, metronomic. "
 "`+364d` from 2025-08-27 ⇒ 08-26, exact. ⚠ The cached IR URL was a **2025** per-quarter "
 "deep link — replaced with the feed. | investor.nvidia.com/rss/pressrelease.aspx |",

 "| WSM | Williams-Sonoma / Q2 (Jul qtr) | bmo | ⚠⚠ **~2d — the shortest lead in "
 "this table** | Issues \"Williams-Sonoma, Inc. announces release date for \\<n\\> quarter results: "
 "\\<weekday, date\\>\" — **date in the title**, but only **2 days ahead** (Q1: PR **05-19** "
 "→ **05-21** release). **An empty feed therefore proves nothing until ~2 days out** — do "
 "not gate or reason from absence here, and do not re-check early. Its events page is also "
 "chronically unpopulated (\"no upcoming events\" with a call imminent). Furnishes "
 "13:02–13:09Z ⇒ ~09:0x ET with a 10:00am ET call ⇒ bmo, 8/8 qtrs. `+364d` from "
 "2025-08-27 ⇒ **08-26** = the DB date. ⚠⚠ **Host: `ir.williams-sonomaINC.com`** "
 "— `ir.`/`investors.williams-sonoma.com` and the gcs-web variant are ALL NXDOMAIN; the `inc` "
 "in the domain is the whole trick. | ir.williams-sonomainc.com/rss/pressrelease.aspx |",
]
lines[169:169] = new

io.open(p, "w", encoding="utf-8").write("\n".join(lines))
print("cadence: 4 rows updated, %d rows added" % len(new))
