import io

p = 'memory/reference_company_cadence.md'
t = io.open(p, encoding='utf-8').read()

add = """- **⚠⚠ Cintas (`CTAS`) has NO first-party IR surface (found 2026-09-02).** `investors.cintas.com` and `ir.cintas.com` are both **NXDOMAIN**; the Q4-managed host `cintas.gcs-web.com` **resolves but returns HTTP 403 "Access Denied" on every path, including `/`** (Akamai). That 403 is *honest* — it is a real refusal, not the Copart-style 200-for-everything wall — so it cannot manufacture a false positive, but nothing on it is readable. Cintas' advance PR (*"Cintas Corporation Announces Webcast for \\<n\\> Quarter Fiscal Year \\<yr\\> Results"*, ~14d lead) is **BusinessWire only** and is **not filed as an 8-K**. Read it at `stocktitan.net/news/CTAS/`.
- **⭐⭐ `stocktitan.net/news/<SYM>/` is a DISCOVERY channel, not just an absence cross-check (2026-09-02, CPRT + GIS).** The page embeds a `CollectionPage` JSON-LD object whose `hasPart` array lists the **last 10 headlines with `datePublished` in UTC and a direct article URL each** — one ~16KB fetch gives a company's whole recent-news spine, and each article page reproduces the **verbatim wire text plus the `View source version on businesswire.com:` permalink**, so the citation stored in `research_url` is the wire's own URL rather than the mirror's. This produced **both of 09-02's confirms**, for two symbols with **zero reachable IR hosts between them**. Two mechanics: **(a)** you must send `curl --compressed`, or the raw brotli body comes back as binary garbage that reads exactly like a bot wall; **(b)** it **rate-limits fast** — the 3rd/4th rapid request returns **HTTP 429**, and `/news/<SYM>/page/2` **404s** (pagination is not that shape). Budget one page fetch per symbol and take everything from the JSON-LD in a single pass.
"""

anchor = "## Source-reachability cheat-sheet\n"
i = t.index(anchor) + len(anchor)
# insert after the blank line that follows the heading
j = t.index('- ', i)
t = t[:j] + add + t[j:]
io.open(p, 'w', encoding='utf-8').write(t)
print('cheat-sheet updated')
