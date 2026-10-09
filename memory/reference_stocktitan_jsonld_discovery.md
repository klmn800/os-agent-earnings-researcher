---
name: reference-stocktitan-jsonld-discovery
description: stocktitan.net/news/<SYM>/ embeds JSON-LD with the last 10 headlines, UTC timestamps and article URLs — a one-fetch discovery channel for symbols with no reachable IR host
metadata:
  type: reference
---

`https://www.stocktitan.net/news/<SYM>/` embeds a `CollectionPage` JSON-LD block
whose `hasPart` array lists the **last 10 news items as
`{headline, url, datePublished}`**, with `datePublished` in **UTC**. One ~16KB
fetch gives a company's entire recent-news spine, no host discovery and no RSS
path guessing. Each article page reproduces the **verbatim wire text** plus the
`View source version on businesswire.com: <permalink>` line — so the URL stored
in `research_url` can be the **wire's own**, not the mirror's.

This workspace had been using stocktitan only as a *cross-check for absence*
(added after BusinessWire's title search was caught lagging ~1 day on ADBE,
2026-09-01). **On 2026-09-02 it produced two outright confirms — CPRT and GIS —
for symbols with no first-party surface between them** (`investors.copart.com`
and all five sibling hosts NXDOMAIN; `investors.cintas.com` / `ir.cintas.com`
NXDOMAIN, `cintas.gcs-web.com` 403 on every path). Treat it as a **primary
discovery channel**, not a fallback.

Extraction: use **`analysis/helpers/spine.py SYM [SYM ...]`** (run from the workspace root; it
writes `inbox/fetch/st_SYM.html`, prints Q3-relevant headlines since the 1st of last month, and paces
itself to the rate limit below). The working request shape as of **2026-10-01**:

```bash
curl -s --compressed -m 40   -A "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0 Safari/537.36"   -H "Accept: text/html" -H "Accept-Language: en-US,en;q=0.9"   "https://www.stocktitan.net/news/CPRT/" -o inbox/fetch/st_CPRT.html
# JSON-LD now serialises WITHOUT spaces -> make every gap \s*
re.findall(r'"headline":\s*"([^"]+)",\s*"url":\s*"([^"]+)",\s*"datePublished":\s*"([^"]+)"', t)
```

⚠ **Changed 09-30 → 10-01:** (a) the short `Chrome/120` UA started getting **403 on every symbol**, and
the fuller UA + `Accept` + `Accept-Language` headers fix it; (b) the JSON-LD dropped the spaces after
`:` and `,`, so the old regex silently matched **zero items**, which reads as "no news". If a page comes
back at full size with `items=0`, suspect the regex before concluding anything.

**Two mechanics that will otherwise waste a fetch each:**

- ⚠ **Send `--compressed`.** Without it curl returns the raw brotli body, which
  prints as binary garbage and looks exactly like a bot wall — easy to
  misdiagnose as an unreachable host.
- ⚠ **Rate limit, measured 2026-10-09** (full log: `analysis/stocktitan_ratelimit_test_plan.md`). `/news/<SYM>/page/2`
  **404s** (pagination is not that shape, so the JSON-LD's 10 items are all you get per fetch): one page fetch per symbol.
  The limit is **10 requests per fixed 300 s window, opened by the first request** (4 of 4 blocks fit it; 299 to 300 s from
  window-open to block-end every time). It is a *count*, not a rate: 10 passed at 10 s spacing and at 20 s spacing, then the 11th got
  **HTTP 429 + `Retry-After`**, which is exact (it counts down to the window end). 40 requests at 40 s spacing (about 8 per window) all passed.
  The block is site-wide (root, listing and article pages); `/robots.txt` stays reachable. A bare `curl` with no User-Agent gets 403 even
  when not blocked. A 429 can also arrive as HTTP 200 with a ~2.5KB "Too Many Requests" body, so check the size.
  **`analysis/helpers/spine.py` now enforces this itself** (9 per 300 s + 5 s pad; the counter lives in `inbox/fetch/.stocktitan_window.json`
  and is shared between invocations; it sleeps for the window, or stops with `--no-wait`; it honours `Retry-After`; it tells a local network
  outage from a stocktitan failure). 30 symbols were read in 15 min with no refusal. **Run it with `run_in_background` past about 17 symbols
  (foreground Bash caps at 10 min), and do not fetch stocktitan by hand at the same time: those requests count against the same window.**
  A 429'd or unread spine is *unread, not absent*; log it as "spine unread" and fall back to search or the IR host. **Do the most urgent
  symbols first.** Not tested: whether WebFetch shares the limit (one WebFetch of a listing page worked while curl was blocked).
  Older note (09-30 to 10-02): 9 fetches at 9 s spacing went through on 10-01 and then everything 429'd; that fits the same window.

**How to apply:** for any symbol whose IR host is NXDOMAIN, SPA-only, or behind a
bot wall, hit this **before** concluding "no channel exists and we must gate."
An absence read here is also stronger than a BusinessWire-search absence, since
the search index lags a day and this does not.

Related: [[reference-source-probe-failure-modes]] (NXDOMAIN / 404 / bot-wall
taxonomy), [[reference-ir-rss-feeds]] (the first-party equivalent when a host
exists), [[reference-sec-via-curl]] (EDGAR submissions as the other zero-discovery
tripwire), [[feedback-window-gating-and-noop]].
