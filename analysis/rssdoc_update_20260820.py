# -*- coding: utf-8 -*-
"""Append the 2026-08-20 findings to memory/reference_ir_rss_feeds.md:
two new path shapes, one new host prefix, and 8 newly-cached feeds.
Inserted BEFORE the trailing 'Related: [[...]]' backlink line."""
import io

p = "memory/reference_ir_rss_feeds.md"
s = io.open(p, encoding="utf-8").read()

SECTION = """
## Two more path shapes and a sixth host prefix (2026-08-20)

The Aug-fiscal-year-end cluster added three structural finds, all on hosts that looked feedless under
the standard probe:

| Symbol | What the standard probe said | Reality |
|---|---|---|
| **PATH** | all five paths **404** on `ir.uipath.com`, `investors.uipath.com` NXDOMAIN | **`ir.uipath.com/news/rss`** — a `/news/rss` shape, and the href was sitting in the IR home page HTML the whole time |
| **GOLD** | all five paths **404** on `ir.gold.com` | **`ir.gold.com/news-events/press-releases/rss`** — the feed lives *under* the section path |
| **LULU** | `investor.`/`corporate.` 404 on all five standard paths | **`corporate.lululemon.com/rss/press-releases`** (334 items) and **`/rss`** = a separate **events** feed |

**Two rules follow:**

1. **When every path 404s, fetch the IR home page and grep it for `href="*rss*"`.** That one request
   found the UiPath feed after ten wasted probes, and it would have found the Gold.com one too. A site
   that publishes a feed almost always links it. Do this *before* declaring a host feedless — it is
   cheaper than the five-path rotation and strictly more reliable.
2. **`corporate.X` is a sixth host prefix.** The list is now
   **`ir.X`, `investors.X`, `investor.X`, `www.ir.X`, `corporate.X`, `X.gcs-web.com`** — and for TTC,
   plain **`www.X`** (the company's own marketing domain) served the feed while every IR-flavoured
   prefix was NXDOMAIN. ⚠ For TTC the `www.` is load-bearing: bare `thetorocompany.com` 301s to the
   marketing home page and returns 0 items, which reads exactly like "no feed."

**Path-shape list, updated and ordered:** `/rss/news-releases.xml`, `/rss/pressrelease.aspx`, `/rss`,
`/feed/`, `/rss/press-releases`, **`/news/rss`**, **`/news-events/press-releases/rss`**.

**Newly cached this session (all verified carrying an advance earnings PR):**
`investor.ciena.com/rss/pressrelease.aspx`, `investor.thecampbellscompany.com/rss/news-releases.xml`,
`investor.docusign.com/rss/pressrelease.aspx`, `corporate.lululemon.com/rss/press-releases`,
`ir.uipath.com/news/rss`, `www.thetorocompany.com/rss/news-releases.xml`,
`ir.zscaler.com/rss/news-releases.xml`, `ir.gold.com/news-events/press-releases/rss`,
plus `ir.kroger.com/rss/pressrelease.aspx` and `investor.oracle.com/rss/pressrelease.aspx`.

⚠ **Two more "wrong host, reads as no feed" corrections:** `investor.guidewire.com` is NXDOMAIN but
**`ir.guidewire.com` works**, and `investors.ciena.com` (plural) 301s to an SPA with 0 items while
**`investor.ciena.com` (singular)** serves the feed. Both had been written up as "BusinessWire only."

⚠ **A 404 host can still be honest — and that matters for slug probes.** `ir.uipath.com` 404s cleanly
on nonsense paths, which is what made a *guessed* event URL
(`/events-presentations/detail/20260903-uipath-second-quarter-fiscal-2027-…`) a legitimate source for
PATH: the control 404'd and two wrong-date guesses 404'd, so the one 200 meant something. Run the
control first, every time — on a bot-wall host all four would have "confirmed."

"""

anchor = "Related: [[IR URL caching"
i = s.index(anchor)
s = s[:i] + SECTION + "\n" + s[i:]
io.open(p, "w", encoding="utf-8").write(s)
print("reference_ir_rss_feeds.md updated (2026-08-20 section added)")
