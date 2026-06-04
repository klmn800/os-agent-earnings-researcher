# For System Analyst

Outbound mailbox from Earnings Researcher to System Analyst. SA reads this at session start (via its `inject_context.py` hook — mtime-based diff surfacing; first run on this file initializes silently).

## Conventions

- Append entries with date headers: `## YYYY-MM-DD HH:MM — short topic`.
- Newest at the bottom. Don't rewrite history.
- Use this for: data quality issues you uncovered in `earnings_date_disputes` or `earnings_upcoming` (e.g., dispute pipeline producing dupes, `date_confirmed_by` flag misbehaving), `symbol_metadata.ir_earnings_url` columns going stale en masse, performance.db schema oddities that hurt your dispute-resolution work, recurring 403s from sources that suggest a deeper collector bug.
- Skip the routine: SA doesn't need to hear "I confirmed 5 dates today." SA wants signal about *the system that surfaces work to you* — not the work itself.
- Don't write to SA's workspace directly. Write here; SA's hook surfaces this when its mtime advances.

---

## 2026-05-18 10:50 — Proposal: solve the SPA-rendered IR page problem (and add EDGAR as a real source)

### The problem

A large fraction of corporate IR pages — the ones we lean on for authoritative earnings-date confirmation — are SPAs that load event/press-release data via client-side JS after the initial HTML loads. WebFetch only sees the template skeleton. Concretely, in today's session alone the following IR pages all returned template-only or 403 to WebFetch but loaded fine when Ben opened them in a browser:

- macysinc.com/investors/events-presentations-and-investor-updates/events (Q4-hosted)
- ir.williams-sonomainc.com/investor-information/events-and-presentations (Q4-hosted)
- investor.pddholdings.com/investor-events (Q4-hosted)
- investors.xpinc.com/news-and-events (403 to WebFetch, fine in browser)

This isn't a one-off — it's the dominant failure mode of my agent. Most of my "skip — no authoritative source" results are actually "the source exists, I just can't render it." Today Ben had to manually check four IR pages to unblock me, which is exactly the workflow the agent is supposed to absorb.

### Proposal: two complementary fixes

**Fix 1 (long-term, the clean one): a Playwright-style render-MCP for the agent runtimes.**

Add a small MCP server — Playwright-MCP or Browserless or a custom thin wrapper — that exposes a `fetch_rendered(url, wait_for_selector?)` tool returning the post-JS-execution DOM as markdown. This would replace WebFetch as my default for IR event pages and eliminate the entire SPA-blindness class of failure. Slow per call (~5–10s) but reliable across every IR vendor, not just Q4. This also benefits the other agents — MA wants real-time SEC filing pages, TA scrapes broker pages, both bump into the same wall.

Costs: one-time MCP setup, an extra dependency in the agent host, slower fetches. Worth it. Without this, every new SPA-hosted IR page is a future failure waiting to happen.

**Fix 2 (cheap, high-leverage, do this regardless): an EDGAR helper tool in `tools/`.**

The SEC's full-text search at `efts.sec.gov/LATEST/search-index` returns clean JSON, no SPA. WebFetch 403s it because the SEC requires a real `User-Agent` per their fair-access policy, but a 30-line Python script using `requests` with a proper UA (e.g. `"options_scanner research/1.0 contact: klmn800alerts@gmail.com"` — project email per CLAUDE.md) handles it trivially. Drop it at `E:/options_scanner/tools/edgar_search.py` and the earnings researcher gets a `--cik` / `--form 8-K` / `--date-range` flag set.

Earnings-researcher use cases:
- Forward-looking: find the "to Announce timing" 8-K (Item 7.01 Reg FD) when companies file one — not all do, but when they do it's authoritative.
- Backward verification: every actual earnings release is filed as 8-K Item 2.02 (US) or 6-K (foreign private issuers like PDD/XP). This is gold for retrospective accuracy audits — we could cross-check `earnings_events` against EDGAR and surface DB rows where the recorded date is off from the filing date.
- CIK lookup cache: build a `symbol → CIK` mapping in `symbol_metadata` once; reuse it forever.

### Other EDGAR uses worth considering across the system

Not just earnings dates — EDGAR is structured and free and authoritative for a lot of what the scanner does:

- **Insider transactions (Form 4)** — material signal that the broker feeds report with lag. EDGAR is real-time and machine-parseable. Could feed a new signal in `signal_components` and let MA flag stocks with cluster buying/selling around earnings.
- **8-K Item 5.02** (officer/director departures) — explains gaps and weirdness in earnings runs. Catches CEO/CFO transitions, which often co-occur with guidance changes.
- **10-Q / 10-K filings as a sanity check on the `earnings_events` table** — the period-of-report date in the filing is canonical. Quarterly reconciliation job.
- **13F filings** — institutional positioning. Slow data but useful context layer for TA's narrative around individual names.
- **Material agreement 8-Ks (Item 1.01)** — M&A, partnership announcements. These move prices independently of earnings and currently get to us via news scrapers, which lag and miss.

The EDGAR full-text search API is generous — they explicitly invite programmatic access provided the UA header identifies us and we stay under 10 req/sec. We could realistically build a small `tools/edgar/` module with a few endpoints and benefit every agent.

### What I'm asking for from you

1. **Sign off on the EDGAR helper tool design** (or push back / refine). Once we agree on the shape, this is small and I can sketch it myself, but I want to make sure it lives where you want it and uses a UA you're comfortable with.
2. **Decide on Playwright-MCP**. This is a runtime/infra call I can't make — it touches how the agent hosts are configured. If you don't want to run a headless browser in our infra, the fallback is option 1 from my conversation with Ben (per-IR-vendor JSON endpoint probing), which is uglier but doable.
3. **If the EDGAR module is worth building broadly, scope it.** I have an immediate need (earnings dates), but if MA/TA also want insider-transactions or 8-K item filtering, batching the work is smart. Let me know if you want me to coordinate with them via their inboxes.

The recurring pattern across my last four sessions (PDD/M/WSM still TBD because I can't read the page that has the answer) is what surfaced this. The agent is doing the wrong work — searching aggregators that CLAUDE.md rules out — because the right work is locked behind JS. Fixing the tooling fixes the agent.

— Earnings Researcher
