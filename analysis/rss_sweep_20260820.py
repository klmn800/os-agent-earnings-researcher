"""IR RSS sweep for the 2026-08-20 batch.

Window state going in (leads from memory/reference_company_cadence.md):
  NIO  10-13d lead, DB 09-01 => PR due 08-19..08-22  -- day 2 of 4, CHECK
  CPB  ~20d lead,  DB 09-03  => PR due ~08-14, OVERDUE if date right
  DOCU ~3wk lead,  DB 09-03  => PR due ~08-13, OVERDUE if date right
  PATH ~4wk lead,  DB 09-03  => PR due ~08-06, OVERDUE if date right
  GWRE ~14d lead,  DB 09-03  => due ~TODAY
  LULU ~14d lead,  DB 09-03  => due ~TODAY
  TTC  3-14d lead, DB 09-03  => due 08-20..08-31, front edge
  CIEN/ZS/KR/ORCL/GOLD -- lead unknown or gated, one request each
GATED, NOT PROBED: WSM (2d lead, not due until ~08-24 -- absence is
information-free, standing rule) and CPRT (all hosts NXDOMAIN or the
200-for-everything bot wall; BusinessWire only, gate ~08-26).

Browser UA per the standing rule; redirects followed and final URL printed.
pubDate printed RAW, never timezone-converted.
"""
import re, socket, urllib.error, urllib.request, sys
from concurrent.futures import ThreadPoolExecutor

sys.stdout.reconfigure(encoding="utf-8")
UA = ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
      "(KHTML, like Gecko) Chrome/126.0 Safari/537.36")
HDRS = {"User-Agent": UA,
        "Accept": "application/rss+xml, application/xml, text/xml, */*"}
TIMEOUT = 25

FEEDS = {
    "NIO":     "https://ir.nio.com/rss/news-releases.xml",
    "PATH":    "https://ir.uipath.com/rss/news-releases.xml",
    "KR-a":    "https://ir.kroger.com/rss/news-releases.xml",
    "KR-b":    "https://ir.kroger.com/rss/pressrelease.aspx",
    "ORCL-a":  "https://investor.oracle.com/rss/news-releases.xml",
    "ORCL-b":  "https://investor.oracle.com/rss/pressrelease.aspx",
    "GOLD-a":  "https://ir.gold.com/rss/news-releases.xml",
    "GOLD-b":  "https://ir.gold.com/rss/pressrelease.aspx",
    "CIEN-a":  "https://investor.ciena.com/rss/news-releases.xml",
    "CIEN-b":  "https://investors.ciena.com/rss/pressrelease.aspx",
    "CPB-a":   "https://investor.thecampbellscompany.com/rss/news-releases.xml",
    "CPB-b":   "https://investor.campbellsoupcompany.com/rss/news-releases.xml",
    "DOCU-a":  "https://investor.docusign.com/rss/news-releases.xml",
    "DOCU-b":  "https://investor.docusign.com/rss/pressrelease.aspx",
    "GWRE-a":  "https://investor.guidewire.com/rss/news-releases.xml",
    "GWRE-b":  "https://ir.guidewire.com/rss/news-releases.xml",
    "LULU-a":  "https://corporate.lululemon.com/rss/news-releases.xml",
    "LULU-b":  "https://investor.lululemon.com/rss/news-releases.xml",
    "TTC-a":   "https://investors.thetorocompany.com/rss/news-releases.xml",
    "TTC-b":   "https://ir.thetorocompany.com/rss/news-releases.xml",
    "ZS-a":    "https://ir.zscaler.com/rss/news-releases.xml",
    "ZS-b":    "https://investors.zscaler.com/rss/news-releases.xml",
}

ITEM_RE = re.compile(r"<item[ >](.*?)</item>", re.S | re.I)
TITLE_RE = re.compile(r"<title>(?:<!\[CDATA\[)?(.*?)(?:\]\]>)?</title>", re.S | re.I)
DATE_RE = re.compile(r"<pubDate>(?:<!\[CDATA\[)?(.*?)(?:\]\]>)?</pubDate>", re.S | re.I)
LINK_RE = re.compile(r"<link>(?:<!\[CDATA\[)?(.*?)(?:\]\]>)?</link>", re.S | re.I)
KEY = re.compile(r"report|results|conference call|earnings|announce|webcast|"
                 r"timing|release date|schedul", re.I)


def probe(pair):
    sym, url = pair
    req = urllib.request.Request(url, headers=HDRS)
    try:
        with urllib.request.urlopen(req, timeout=TIMEOUT) as r:
            body = r.read().decode("utf-8", "replace")
            final = r.geturl()
    except socket.timeout:
        return (sym, url, "TIMEOUT", [])
    except urllib.error.HTTPError as e:
        return (sym, url, f"HTTP {e.code}", [])
    except Exception as e:
        return (sym, url, f"ERR {type(e).__name__}: {e}", [])

    items = ITEM_RE.findall(body)
    tag = f"(final {final})" if final != url else ""
    if not items:
        return (sym, url, f"200 but 0 items ({len(body)}B) {tag}", [])
    out = []
    for it in items[:14]:
        t = TITLE_RE.search(it)
        d = DATE_RE.search(it)
        l = LINK_RE.search(it)
        out.append(((d.group(1).strip() if d else "?"),
                    (t.group(1).strip() if t else "?"),
                    (l.group(1).strip() if l else "")))
    return (sym, url, f"OK {len(items)} items {tag}", out)


with ThreadPoolExecutor(max_workers=8) as ex:
    results = list(ex.map(probe, FEEDS.items()))

for sym, url, status, items in results:
    print(f"\n{'='*72}\n{sym}  {status}\n  {url}")
    for pub, title, link in items:
        star = " *" if KEY.search(title) else "  "
        print(f"  {star} {pub:<34} {title[:96]}")
        if KEY.search(title) and link:
            print(f"       -> {link}")
