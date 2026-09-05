"""Bulk IR RSS probe for the 2026-08-03 batch.

Per memory/reference_ir_rss_feeds.md:
  - try /rss/pressrelease.aspx, /rss/news-releases.xml, /rss (+ a couple of extras)
  - probe BOTH the ir. and investors. prefixes -- host guesses are the usual failure
  - distinguish TimeoutError / DNS failure from "fetched but no <item>";
    only the second is evidence about the company
  - report redirects (a 301 to an unfamiliar host can be a ticker rename)
"""
import re, socket, urllib.error, urllib.request
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime

UA = "options-scanner-earnings-researcher klmn800alerts@gmail.com"
TIMEOUT = 12
PATHS = ["/rss/pressrelease.aspx", "/rss/news-releases.xml", "/rss",
         "/rss/news.xml", "/feed"]

HOSTS = {
    "ARE":  ["investor.are.com"],
    "BWXT": ["investors.bwxt.com", "ir.bwxt.com"],
    "CLX":  ["investors.thecloroxcompany.com", "ir.thecloroxcompany.com"],
    "FANG": ["ir.diamondbackenergy.com", "investors.diamondbackenergy.com"],
    "INSP": ["investors.inspiresleep.com", "ir.inspiresleep.com"],
    "OKE":  ["ir.oneok.com", "investors.oneok.com"],
    "ON":   ["investor.onsemi.com", "ir.onsemi.com"],
    "TSN":  ["ir.tyson.com", "investors.tysonfoods.com"],
    "ADM":  ["investors.adm.com", "ir.adm.com"],
    "AMD":  ["ir.amd.com", "investors.amd.com"],
    "AME":  ["investors.ametek.com", "ir.ametek.com"],
    "AMGN": ["investors.amgen.com", "ir.amgen.com"],
    "ANET": ["investors.arista.com", "ir.arista.com"],
    "APO":  ["ir.apollo.com", "ir.apolloglobal.com"],
    "TECH": ["investors.bio-techne.com"],
    "PANW": ["investors.paloaltonetworks.com"],
    "FLO":  ["investors.flowersfoods.com", "www.flowersfoods.com"],
    "NXE":  ["www.nexgenenergy.ca"],
    "XPEV": ["ir.xiaopeng.com"],
    "NNE":  ["ir.nanonuclearenergy.com"],
    "SQM":  ["ir.sqm.com", "www.sqm.com"],
    "WDS":  ["www.woodside.com", "investors.woodside.com", "www.woodside.com.au"],
}

ITEM_RE = re.compile(r"<item[ >](.*?)</item>", re.S | re.I)
TITLE_RE = re.compile(r"<title>(?:<!\[CDATA\[)?(.*?)(?:\]\]>)?</title>", re.S | re.I)
DATE_RE = re.compile(r"<pubDate>(?:<!\[CDATA\[)?(.*?)(?:\]\]>)?</pubDate>", re.S | re.I)
LINK_RE = re.compile(r"<link>(?:<!\[CDATA\[)?(.*?)(?:\]\]>)?</link>", re.S | re.I)

KEY = re.compile(r"report|results|conference call|earnings|announce|webcast|"
                 r"quarter|half.?year|financial", re.I)


def probe(sym, host, path):
    url = f"https://{host}{path}"
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    try:
        with urllib.request.urlopen(req, timeout=TIMEOUT) as r:
            body = r.read().decode("utf-8", "replace")
            final = r.geturl()
    except socket.timeout:
        return (sym, url, "TIMEOUT", None, None)
    except urllib.error.HTTPError as e:
        return (sym, url, f"HTTP {e.code}", None, None)
    except urllib.error.URLError as e:
        return (sym, url, f"URLERR {e.reason}", None, None)
    except Exception as e:
        return (sym, url, f"ERR {type(e).__name__}", None, None)
    items = ITEM_RE.findall(body)
    if not items:
        return (sym, url, "200-no-items", final, None)
    parsed = []
    for it in items[:40]:
        t = TITLE_RE.search(it)
        d = DATE_RE.search(it)
        l = LINK_RE.search(it)
        parsed.append((d.group(1).strip() if d else "?",
                       re.sub(r"\s+", " ", t.group(1).strip()) if t else "?",
                       l.group(1).strip() if l else ""))
    return (sym, url, f"OK {len(items)} items", final, parsed)


jobs = [(s, h, p) for s, hs in HOSTS.items() for h in hs for p in PATHS]
with ThreadPoolExecutor(max_workers=16) as ex:
    results = list(ex.map(lambda a: probe(*a), jobs))

by_sym = {}
for sym, url, status, final, parsed in results:
    by_sym.setdefault(sym, []).append((url, status, final, parsed))

for sym in HOSTS:
    print("=" * 78)
    good = [r for r in by_sym[sym] if r[3]]
    if not good:
        print(f"{sym}: no feed. " + " | ".join(
            f"{u.split('https://')[1]} -> {s}" for u, s, _, _ in by_sym[sym]))
        continue
    url, status, final, parsed = max(good, key=lambda r: len(r[3]))
    print(f"{sym}: {url} -> {status}" + (f"  (redirected to {final})"
                                         if final and final != url else ""))
    for d, t, l in parsed[:14]:
        mark = " <<<" if KEY.search(t) else ""
        print(f"    {d[:22]:<22} {t[:96]}{mark}")
        if mark:
            print(f"        {l}")
