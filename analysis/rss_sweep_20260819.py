"""IR RSS sweep for the 2026-08-19 batch.

Known-good feeds come from memory/reference_company_cadence.md. Four symbols
(AVGO/HPE/COO/GME) have no cadence feed entry, so this also rotates the
investor./investors./ir./news. prefix set for them -- one pass, no hand probing.

Window state going in (from the carry-over ledger):
  NIO  next-check TODAY  -- 10-13d lead, DB 09-01 => advance PR due ~today
  M    16d lead, DB 09-02 => advance PR should ALREADY be out (~08-17)
  WSM  2d lead,  DB 08-26 => not due until ~08-24; absence proves NOTHING
  GTLB no advance PR ever => tripwire only, 8-K on the day is the source
  COTY no advance PR ever => tripwire only, 8-K on the day is the source
CPRT is not probed: all six Copart hosts are NXDOMAIN or a 200-for-everything
bot wall (standing rule 3), BusinessWire is the only channel.

pubDate offsets differ per feed (NIO = -0400 ET) -- printed RAW, never converted.
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
    # -- window OPEN: the advance PR should exist if the DB date is right --
    "NIO":  "https://ir.nio.com/rss/news-releases.xml",
    "M":    "https://investors.macysinc.com/rss/pressrelease.aspx",
    # -- gated / channel-less, but one request each: catches a rare early PR --
    "WSM":  "https://ir.williams-sonomainc.com/rss/pressrelease.aspx",
    "GTLB": "https://ir.gitlab.com/rss/pressrelease.aspx",
    "COTY": "https://investors.coty.com/rss/pressrelease.aspx",
    # -- no cadence entry yet: rotate the prefix set to FIND the feed --
    "AVGO-a": "https://investors.broadcom.com/rss/news-releases.xml",
    "AVGO-b": "https://investors.broadcom.com/rss/pressrelease.aspx",
    "HPE-a":  "https://investors.hpe.com/rss/news-releases.xml",
    "HPE-b":  "https://investors.hpe.com/rss/pressrelease.aspx",
    "COO-a":  "https://investor.coopercos.com/rss/news-releases.xml",
    "COO-b":  "https://investors.coopercos.com/rss/pressrelease.aspx",
    "GME-a":  "https://investor.gamestop.com/rss/news-releases.xml",
    "GME-b":  "https://news.gamestop.com/rss/pressrelease.aspx",
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
    except socket.timeout:
        return (sym, url, "TIMEOUT", [])
    except urllib.error.HTTPError as e:
        return (sym, url, f"HTTP {e.code}", [])
    except Exception as e:
        return (sym, url, f"ERR {type(e).__name__}: {e}", [])

    items = ITEM_RE.findall(body)
    if not items:
        return (sym, url, f"200 but 0 items ({len(body)}B)", [])
    out = []
    for it in items[:14]:
        t = TITLE_RE.search(it)
        d = DATE_RE.search(it)
        l = LINK_RE.search(it)
        out.append((
            (d.group(1).strip() if d else "?"),
            (t.group(1).strip() if t else "?"),
            (l.group(1).strip() if l else ""),
        ))
    return (sym, url, f"OK {len(items)} items", out)


with ThreadPoolExecutor(max_workers=8) as ex:
    results = list(ex.map(probe, FEEDS.items()))

for sym, url, status, items in results:
    print(f"\n{'='*72}\n{sym}  {status}\n  {url}")
    for pub, title, link in items:
        star = " *" if KEY.search(title) else "  "
        print(f"  {star} {pub:<34} {title[:96]}")
        if KEY.search(title) and link:
            print(f"       -> {link}")
