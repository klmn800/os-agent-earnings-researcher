---
name: IR URL caching — SPAs and per-quarter deep links
description: Ben's clarifications to the strict "WebFetch must see earnings info" rule for IR URL caching
metadata:
  type: feedback
---

Two caveats on the CLAUDE.md "only cache if WebFetch loaded + saw earnings info" rule, learned 2026-05-21:

1. **SPA-rendered IR pages**: Several canonical IR events pages render their event list client-side (e.g. `ir.williams-sonomainc.com/.../events-and-presentations/default.aspx`, `investor.fivebelow.com/events/default.aspx`, `investor.pddholdings.com/investor-events`). WebFetch sees only the template scaffold ("Please select a highlighted date" / "Upcoming Events" headers with no children). When Ben explicitly confirms such a URL as the right IR page, cache it — don't skip per the strict rule. The future agent run will still need to fall back to search, but the cached URL is correct.

2. **Per-quarter deep-link URLs are not stable** (LULU/DOCU pattern): Some companies use per-quarter URLs like `corporate.lululemon.com/investors/news-and-events/events-and-presentations/2026/lululemon-athletica-q1-2026-results` or DOCU's `/news-details/2026/Docusign-Announces-Timing-of-First-Quarter-Fiscal-2027-...`. These deep-link URLs go stale each quarter. Ben confirmed them as the best current source but flagged they're "less easy to predict going forward." When a cached URL of this shape returns 404 next quarter, treat that as expected and search fresh.

**Why:** Ben provided these URLs on 2026-05-21 after I'd skipped caching due to the strict rule. He's clarifying that the strict rule was too conservative for SPAs, and that per-quarter URLs are acceptable cache entries even though they'll need refreshing.

**How to apply:**
- When Ben explicitly confirms an IR URL, cache it even if WebFetch can't render earnings info.
- When a cached IR URL returns 404 on the next session's WebFetch, don't treat that as a tooling failure — it likely just rotated; refresh by searching.
- Still don't cache wire services, third-party aggregators, or non-company domains. The "company's own domain" rule still holds.

Related: [[direct_db_query]]
