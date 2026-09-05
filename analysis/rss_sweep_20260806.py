"""Bulk IR RSS probe for the 2026-08-06 batch.

Per memory/reference_ir_rss_feeds.md: browser UA, probe both ir./investors.
prefixes, try the six known feed shapes, follow redirects and print the final
URL, and distinguish TIMEOUT/DNS from '200 but no <item>' -- only the second is
evidence about the company. Always print the newest pubDate (allstateinvestors
lesson: a live 200 can be a decade-stale feed).
"""
import re, socket, urllib.error, urllib.request
from concurrent.futures import ThreadPoolExecutor

UA = ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
      "(KHTML, like Gecko) Chrome/126.0 Safari/537.36")
HDRS = {"User-Agent": UA,
        "Accept": "application/rss+xml, application/xml, text/xml, */*"}
TIMEOUT = 12
PATHS = ["/rss/pressrelease.aspx", "/rss/news-releases.xml", "/rss",
         "/news-events/press-releases/rss", "/rss/press-releases", "/feed"]

HOSTS = {
    # -- date_disagreement --
    "NCNO": ["investors.ncino.com", "ir.ncino.com"],
    "HPQ":  ["investor.hp.com", "investors.hp.com"],
    "NTNX": ["ir.nutanix.com", "investors.nutanix.com"],
    "SJM":  ["investors.jmsmucker.com", "ir.jmsmucker.com"],
    "WOLF": ["investor.wolfspeed.com", "ir.wolfspeed.com",
             "investors.wolfspeed.com"],
    # -- both --
    "P":    ["investor.everpuredata.com", "investor.purestorage.com"],
    "LI":   ["ir.lixiang.com", "ir.liauto.com"],
    # -- unknown_time --
    "NNE":  ["ir.nanonuclearenergy.com"],
    "SQM":  ["ir.sqm.com"],
    "ADSK": ["investors.autodesk.com", "ir.autodesk.com",
             "adsknews.autodesk.com"],
    "BBWI": ["investors.bbwinc.com", "ir.bbwinc.com"],
    "BBY":  ["investors.bestbuy.com", "corporate.bestbuy.com"],
    "DG":   ["investor.dollargeneral.com", "newscenter.dollargeneral.com"],
    "GAP":  ["investors.gapinc.com", "www.gapinc.com"],
    "MRVL": ["investor.marvell.com", "ir.marvell.com"],
    "S":    ["investors.sentinelone.com", "ir.sentinelone.com"],
    "ULTA": ["investors.ultabeauty.com", "ir.ultabeauty.com"],
    # -- unconfirmed, DB says TODAY --
    "ABNB": ["investors.airbnb.com", "news.airbnb.com", "ir.airbnb.com"],
    "AFL":  ["investors.aflac.com", "ir.aflac.com"],
    "AIG":  ["investors.aig.com", "ir.aig.com"],
    "AKAM": ["investors.akamai.com", "ir.akamai.com"],
    "ATI":  ["investors.atimaterials.com", "ir.atimaterials.com",
             "investors.atimetals.com"],
    "BMRN": ["investors.biomarin.com", "ir.biomarin.com"],
    "CART": ["investors.instacart.com", "ir.instacart.com"],
}

ITEM_RE = re.compile(r"<item[ >](.*?)</item>", re.S | re.I)
TITLE_RE = re.compile(r"<title>(?:<!\[CDATA\[)?(.*?)(?:\]\]>)?</title>", re.S | re.I)
DATE_RE = re.compile(r"<pubDate>(?:<!\[CDATA\[)?(.*?)(?:\]\]>)?</pubDate>", re.S | re.I)
LINK_RE = re.compile(r"<link>(?:<!\[CDATA\[)?(.*?)(?:\]\]>)?</link>", re.S | re.I)

KEY = re.compile(r"report|results|conference call|earnings|announce|webcast|"
                 r"quarter|financial|invitation|timing|date", re.I)


def probe(job):
    sym, host, path = job
    url = f"https://{host}{path}"
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
        return (sym, url, f"ERR {type(e).__name__}", None, [])
    items = ITEM_RE.findall(body)
    if not items:
        return (sym, url, "200-no-items", final, [])
    rows = []
    for it in items[:14]:
        t, d, l = TITLE_RE.search(it), DATE_RE.search(it), LINK_RE.search(it)
        rows.append(((d.group(1).strip() if d else "?"),
                     (t.group(1).strip() if t else "?"),
                     (l.group(1).strip() if l else "?")))
    return (sym, url, f"OK {len(items)} items", final, rows)


jobs = [(s, h, p) for s, hs in HOSTS.items() for h in hs for p in PATHS]
with ThreadPoolExecutor(max_workers=16) as ex:
    results = list(ex.map(probe, jobs))

for sym in HOSTS:
    print("=" * 78)
    rs = [r for r in results if r[0] == sym]
    hits = [r for r in rs if r[2].startswith("OK")]
    if not hits:
        for r in rs:
            if r[2] != "HTTP 404":
                print(f"{sym}: {r[1]} -> {r[2]}")
        print(f"{sym}: no feed on any path (404s suppressed)")
        continue
    best = max(hits, key=lambda r: len(r[4]))
    print(f"{sym}: FEED {best[1]} -> {best[2]}"
          + (f"  (redirected to {best[3]})" if best[3] and best[3] != best[1] else ""))
    for d, t, l in best[4]:
        star = " ***" if KEY.search(t) else ""
        print(f"   {d[:22]:24s} {t[:100]}{star}")
        if star:
            print(f"        {l}")
