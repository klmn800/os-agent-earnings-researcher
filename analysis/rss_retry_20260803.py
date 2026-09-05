"""Retry the hosts that TIMEOUT/403'd in rss_sweep_20260803.py with a browser UA.

Per memory/reference_ir_rss_feeds.md a bare timeout is NOT evidence about the
company -- it has to be re-run before "absence" means anything. Several of these
hosts look like they reject the bare project UA rather than being slow.
"""
import re, socket, urllib.error, urllib.request
from concurrent.futures import ThreadPoolExecutor

UA = ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
      "(KHTML, like Gecko) Chrome/126.0 Safari/537.36")
TIMEOUT = 25
PATHS = ["/rss/pressrelease.aspx", "/rss/news-releases.xml", "/rss",
         "/rss/news.xml", "/news/rss", "/rss/press-releases.xml"]

HOSTS = {
    "BWXT": ["investors.bwxt.com"],
    "FANG": ["ir.diamondbackenergy.com"],
    "OKE":  ["ir.oneok.com"],
    "ON":   ["investor.onsemi.com"],
    "AME":  ["investors.ametek.com"],
    "AMGN": ["investors.amgen.com"],
    "APO":  ["ir.apollo.com"],
    "PANW": ["investors.paloaltonetworks.com"],
    "XPEV": ["ir.xiaopeng.com"],
    "NNE":  ["ir.nanonuclearenergy.com"],
    "SQM":  ["ir.sqm.com"],
}

ITEM_RE = re.compile(r"<item[ >](.*?)</item>", re.S | re.I)
TITLE_RE = re.compile(r"<title>(?:<!\[CDATA\[)?(.*?)(?:\]\]>)?</title>", re.S | re.I)
DATE_RE = re.compile(r"<pubDate>(?:<!\[CDATA\[)?(.*?)(?:\]\]>)?</pubDate>", re.S | re.I)
LINK_RE = re.compile(r"<link>(?:<!\[CDATA\[)?(.*?)(?:\]\]>)?</link>", re.S | re.I)
KEY = re.compile(r"report|results|conference call|earnings|announce.*(date|call)|"
                 r"webcast|quarter", re.I)


def probe(sym, host, path):
    url = f"https://{host}{path}"
    req = urllib.request.Request(url, headers={
        "User-Agent": UA,
        "Accept": "application/rss+xml, application/xml, text/xml, */*",
    })
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
        return (sym, url, f"200-no-items ({len(body)}b)", final, None)
    out = []
    for it in items[:25]:
        t = TITLE_RE.search(it); d = DATE_RE.search(it); l = LINK_RE.search(it)
        out.append((d.group(1).strip() if d else "?",
                    re.sub(r"\s+", " ", t.group(1).strip()) if t else "?",
                    l.group(1).strip() if l else ""))
    return (sym, url, f"OK {len(items)} items", final, out)


jobs = [(s, h, p) for s, hs in HOSTS.items() for h in hs for p in PATHS]
with ThreadPoolExecutor(max_workers=12) as ex:
    results = list(ex.map(lambda a: probe(*a), jobs))

by_sym = {}
for r in results:
    by_sym.setdefault(r[0], []).append(r)

for sym in HOSTS:
    print("=" * 78)
    good = [r for r in by_sym[sym] if r[4]]
    if not good:
        print(f"{sym}: still no feed. " + " | ".join(
            f"{r[1].split('https://')[1]} -> {r[2]}" for r in by_sym[sym]))
        continue
    _, url, status, final, parsed = max(good, key=lambda r: len(r[4]))
    print(f"{sym}: {url} -> {status}" +
          (f"  (redirected to {final})" if final and final != url else ""))
    for d, t, l in parsed[:12]:
        mark = " <<<" if KEY.search(t) else ""
        print(f"    {d[:22]:<22} {t[:96]}{mark}")
        if mark:
            print(f"        {l}")
