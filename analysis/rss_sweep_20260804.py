"""Bulk IR RSS probe for the 2026-08-04 batch.

Per memory/reference_ir_rss_feeds.md:
  - BROWSER User-Agent (the project UA gets tarpitted -- that is what created the
    bogus 'no feed' list); try /rss/pressrelease.aspx, /rss/news-releases.xml,
    /rss, and the two odd shapes (/news-events/press-releases/rss, /rss/press-releases)
  - probe BOTH ir. and investors. prefixes
  - distinguish TIMEOUT / DNS from '200 but no <item>' -- only the second is
    evidence about the company
  - report redirects (a 301 to an unfamiliar host can be a ticker rename)
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
    # -- unconfirmed, DB says TODAY --
    "APTV": ["ir.aptiv.com", "investors.aptiv.com"],
    "BP":   ["www.bp.com"],
    "BR":   ["investors.broadridge.com", "ir.broadridge.com"],
    "BRBR": ["ir.bellring.com", "investors.bellring.com"],
    "BRKR": ["ir.bruker.com", "investors.bruker.com"],
    "CAT":  ["investors.caterpillar.com", "ir.caterpillar.com"],
    "CCEP": ["ir.cocacolaep.com"],
    "CG":   ["ir.carlyle.com", "investors.carlyle.com"],
    "CMI":  ["investor.cummins.com", "ir.cummins.com"],
    "DOC":  ["ir.healthpeak.com", "investors.healthpeak.com"],
    "DUK":  ["investors.duke-energy.com", "ir.duke-energy.com"],
    "DVA":  ["investors.davita.com", "ir.davita.com"],
    "DVN":  ["investors.devonenergy.com", "ir.devonenergy.com"],
    "EA":   ["ir.ea.com", "investors.ea.com"],
    # -- disputes --
    "TECH": ["investors.bio-techne.com"],
    "FLO":  ["www.flowersfoods.com", "investors.flowersfoods.com"],
    "PANW": ["investors.paloaltonetworks.com"],
    "WDAY": ["investor.workday.com", "ir.workday.com"],
    "NXE":  ["www.nexgenenergy.ca"],
    "XPEV": ["ir.xiaopeng.com"],
    "NCNO": ["investors.ncino.com", "ir.ncino.com"],
    "NNE":  ["ir.nanonuclearenergy.com"],
    "SQM":  ["ir.sqm.com"],
    "OKTA": ["investor.okta.com", "ir.okta.com"],
    "PVH":  ["www.pvh.com", "ir.pvh.com", "investors.pvh.com"],
}

ITEM_RE = re.compile(r"<item[ >](.*?)</item>", re.S | re.I)
TITLE_RE = re.compile(r"<title>(?:<!\[CDATA\[)?(.*?)(?:\]\]>)?</title>", re.S | re.I)
DATE_RE = re.compile(r"<pubDate>(?:<!\[CDATA\[)?(.*?)(?:\]\]>)?</pubDate>", re.S | re.I)
LINK_RE = re.compile(r"<link>(?:<!\[CDATA\[)?(.*?)(?:\]\]>)?</link>", re.S | re.I)

KEY = re.compile(r"report|results|conference call|earnings|announce|webcast|"
                 r"quarter|half.?year|financial", re.I)


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
        t = TITLE_RE.search(it)
        d = DATE_RE.search(it)
        l = LINK_RE.search(it)
        rows.append(((d.group(1).strip() if d else "?"),
                     (t.group(1).strip() if t else "?"),
                     (l.group(1).strip() if l else "?")))
    return (sym, url, f"OK {len(items)} items", final, rows)


jobs = [(s, h, p) for s, hs in HOSTS.items() for h in hs for p in PATHS]
found = {}
with ThreadPoolExecutor(max_workers=16) as ex:
    results = list(ex.map(probe, jobs))

for sym in HOSTS:
    print("=" * 78)
    rs = [r for r in results if r[0] == sym]
    hits = [r for r in rs if r[2].startswith("OK")]
    if not hits:
        for r in rs:
            print(f"{sym}: {r[1]} -> {r[2]}")
        continue
    best = max(hits, key=lambda r: len(r[4]))
    print(f"{sym}: FEED {best[1]} -> {best[2]}"
          + (f"  (redirected to {best[3]})" if best[3] and best[3] != best[1] else ""))
    for d, t, l in best[4]:
        star = " ***" if KEY.search(t) else ""
        print(f"   {d[:22]:24s} {t[:100]}{star}")
        if star:
            print(f"        {l}")
