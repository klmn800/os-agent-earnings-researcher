"""IR RSS probe + PVH slug existence probe for the 2026-08-17 batch.

Feed URLs come from memory/reference_company_cadence.md -- one request per
symbol, no path hunting. CPRT has no reachable IR host (investors.copart.com is
NXDOMAIN) -> BusinessWire only, handled by search, not probed here.

PVH is today's real question (next-check 08-17 per the 08-14 log): its advance
PR is slug-probeable at www.pvh.com/news/press-releases/<formulaic-slug>, so a
guessed GET answers "has the Q2 PR been issued?" deterministically.

pubDate offsets differ per feed (NIO = -0400 ET, PDD = +0800) -- printed RAW.
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
    # -- window OPEN / due today: PR should exist if the DB date is right --
    "PVH":  "https://pvh.gcs-web.com/rss/news-releases.xml",
    # -- window opens tomorrow / in 2d: cheap tripwire read --
    "PDD":  "https://investor.pddholdings.com/rss/news-releases.xml",
    "NIO":  "https://ir.nio.com/rss/news-releases.xml",
    # -- gated or channel-less, but one request each: catches a rare early PR --
    "COTY": "https://investors.coty.com/rss/pressrelease.aspx",
    "GTLB": "https://ir.gitlab.com/rss/pressrelease.aspx",
    "WSM":  "https://ir.williams-sonomainc.com/rss/pressrelease.aspx",
}

# Deterministic existence probe: 200 => PR issued, 404 => not issued.
SLUGS = {
    "PVH-Q2-2026": "https://www.pvh.com/news/press-releases/"
                   "pvh-corp-to-host-conference-call-to-discuss-second-quarter-"
                   "2026-earnings-results",
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


def slug_probe(item):
    name, url = item
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    try:
        with urllib.request.urlopen(req, timeout=TIMEOUT) as r:
            return (name, url, f"HTTP {r.status} ({len(r.read())}B)")
    except urllib.error.HTTPError as e:
        return (name, url, f"HTTP {e.code}")
    except Exception as e:
        return (name, url, f"ERR {type(e).__name__} {e}")


with ThreadPoolExecutor(max_workers=8) as ex:
    results = list(ex.map(probe, FEEDS.items()))
    slugs = list(ex.map(slug_probe, SLUGS.items()))

for sym, url, status, final, rows in results:
    print("=" * 78)
    print(f"{sym}: {status}  {url}"
          + (f"\n   (final: {final})" if final and final != url else ""))
    for d, t, l in rows:
        star = " ***" if KEY.search(t) else ""
        print(f"   {d[:31]:33s} {t[:88]}{star}")
        if star:
            print(f"        {l}")

print("=" * 78)
print("SLUG EXISTENCE PROBES (200 = PR issued, 404 = not issued)")
for name, url, status in slugs:
    print(f"   {name:14s} {status}\n        {url}")
