"""IR RSS probe for the 2026-08-14 batch.

Known-good feed URLs come straight from memory/reference_company_cadence.md, so
this is one request per symbol, not a path hunt. CPRT has no reachable IR host
(investors.copart.com is NXDOMAIN) -> BusinessWire only, not probed here.

Browser UA required for NCNO/PVH per the cadence notes. pubDate offsets differ
per feed (NIO = -0400 ET, PDD = +0800) -- printed RAW, never converted.
"""
import re, socket, urllib.error, urllib.request, sys
from concurrent.futures import ThreadPoolExecutor

sys.stdout.reconfigure(encoding="utf-8")
UA = ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
      "(KHTML, like Gecko) Chrome/126.0 Safari/537.36")
HDRS = {"User-Agent": UA,
        "Accept": "application/rss+xml, application/xml, text/xml, */*"}
TIMEOUT = 20

FEEDS = {
    # -- window OPEN, PR should exist --
    "NCNO": "https://investor.ncino.com/rss/news-releases.xml",
    "PVH":  "https://pvh.gcs-web.com/rss/news-releases.xml",
    # -- window opens within a few days: cheap tripwire read --
    "NIO":  "https://ir.nio.com/rss/news-releases.xml",
    "PDD":  "https://investor.pddholdings.com/rss/news-releases.xml",
    # -- gated, but the feed is one request: catches a rare early PR --
    "COTY": "https://investors.coty.com/rss/pressrelease.aspx",
    "GTLB": "https://ir.gitlab.com/rss/pressrelease.aspx",
    "WSM":  "https://ir.williams-sonomainc.com/rss/pressrelease.aspx",
}

ITEM_RE = re.compile(r"<item[ >](.*?)</item>", re.S | re.I)
TITLE_RE = re.compile(r"<title>(?:<!\[CDATA\[)?(.*?)(?:\]\]>)?</title>", re.S | re.I)
DATE_RE = re.compile(r"<pubDate>(?:<!\[CDATA\[)?(.*?)(?:\]\]>)?</pubDate>", re.S | re.I)
LINK_RE = re.compile(r"<link>(?:<!\[CDATA\[)?(.*?)(?:\]\]>)?</link>", re.S | re.I)
KEY = re.compile(r"report|results|conference call|earnings|announce|webcast|"
                 r"timing|release date", re.I)


def probe(item):
    sym, url = item
    req = urllib.request.Request(url, headers=HDRS)
    try:
        with urllib.request.urlopen(req, timeout=TIMEOUT) as r:
            body = r.read().decode("utf-8", "replace")
            final = r.geturl()
    except socket.timeout:
        return (sym, url, "TIMEOUT", None, [])
    except urllib.error.HTTPError as e:
        return (sym, url, f"HTTP {e.code}", None, [])
    except urllib.error.URLError as e:
        return (sym, url, f"URLERR {e.reason}", None, [])
    except Exception as e:
        return (sym, url, f"ERR {type(e).__name__} {e}", None, [])
    items = ITEM_RE.findall(body)
    if not items:
        return (sym, url, f"200-no-items ({len(body)}B)", final, [])
    rows = []
    for it in items[:8]:
        t, d, l = TITLE_RE.search(it), DATE_RE.search(it), LINK_RE.search(it)
        rows.append(((d.group(1).strip() if d else "?"),
                     (t.group(1).strip() if t else "?"),
                     (l.group(1).strip() if l else "?")))
    return (sym, url, f"OK {len(items)} items", final, rows)


with ThreadPoolExecutor(max_workers=8) as ex:
    results = list(ex.map(probe, FEEDS.items()))

for sym, url, status, final, rows in results:
    print("=" * 78)
    print(f"{sym}: {status}  {url}"
          + (f"\n   (final: {final})" if final and final != url else ""))
    for d, t, l in rows:
        star = " ***" if KEY.search(t) else ""
        print(f"   {d[:31]:33s} {t[:88]}{star}")
        if star:
            print(f"        {l}")
