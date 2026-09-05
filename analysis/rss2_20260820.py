"""Round-2 host/path rotation for the five 08-20 symbols whose feed wasn't
found on the first pass: PATH, LULU, TTC, GOLD, CIEN.
Probe order per memory/reference_ir_rss_feeds.md: ir. / investors. / investor. /
www.ir. / X.gcs-web.com, paths /rss/news-releases.xml /rss/pressrelease.aspx
/rss /feed/ /rss/press-releases. Redirects followed, final URL printed."""
import re, socket, urllib.error, urllib.request, sys
from concurrent.futures import ThreadPoolExecutor
sys.stdout.reconfigure(encoding="utf-8")
UA = ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
      "(KHTML, like Gecko) Chrome/126.0 Safari/537.36")
HDRS = {"User-Agent": UA,
        "Accept": "application/rss+xml, application/xml, text/xml, */*"}

HOSTS = {
 "PATH": ["ir.uipath.com", "investors.uipath.com"],
 "LULU": ["corporate.lululemon.com", "investor.lululemon.com",
          "lululemon.gcs-web.com", "info.lululemon.com"],
 "TTC":  ["www.thetorocompany.com", "thetorocompany.com",
          "thetorocompany.gcs-web.com", "toro.gcs-web.com"],
 "GOLD": ["ir.gold.com", "investors.gold.com", "www.gold.com", "gold.gcs-web.com"],
 "CIEN": ["investor.ciena.com", "www.ciena.com", "ciena.gcs-web.com"],
}
PATHS = ["/rss/news-releases.xml", "/rss/pressrelease.aspx", "/rss", "/feed/",
         "/rss/press-releases"]

ITEM_RE = re.compile(r"<item[ >](.*?)</item>", re.S | re.I)
TITLE_RE = re.compile(r"<title>(?:<!\[CDATA\[)?(.*?)(?:\]\]>)?</title>", re.S | re.I)
DATE_RE = re.compile(r"<pubDate>(?:<!\[CDATA\[)?(.*?)(?:\]\]>)?</pubDate>", re.S | re.I)
KEY = re.compile(r"report|results|conference call|earnings|announce|webcast|schedul", re.I)

def probe(t):
    sym, host, path = t
    url = f"https://{host}{path}"
    try:
        req = urllib.request.Request(url, headers=HDRS)
        with urllib.request.urlopen(req, timeout=20) as r:
            body = r.read().decode("utf-8", "replace"); final = r.geturl()
    except socket.timeout:
        return (sym, url, "TIMEOUT", [])
    except urllib.error.HTTPError as e:
        return (sym, url, f"HTTP {e.code}", [])
    except Exception as e:
        return (sym, url, f"ERR {type(e).__name__}", [])
    items = ITEM_RE.findall(body)
    tag = f"-> {final}" if final != url else ""
    if not items:
        return (sym, url, f"200/0items {len(body)}B {tag}", [])
    out = []
    for it in items[:10]:
        d = DATE_RE.search(it); ti = TITLE_RE.search(it)
        out.append(((d.group(1).strip() if d else "?"),
                    (ti.group(1).strip() if ti else "?")))
    return (sym, url, f"** OK {len(items)} items {tag}", out)

jobs = [(s, h, p) for s, hs in HOSTS.items() for h in hs for p in PATHS]
with ThreadPoolExecutor(max_workers=12) as ex:
    res = list(ex.map(probe, jobs))
for sym, url, st, items in res:
    if items or st.startswith("**"):
        print(f"\n{'='*70}\n{sym}  {st}\n  {url}")
        for pub, title in items:
            star = " *" if KEY.search(title) else "  "
            print(f"  {star} {pub:<32} {title[:92]}")
print("\n---- non-feed results ----")
for sym, url, st, items in res:
    if not items and not st.startswith("**"):
        print(f"{sym:<6} {st:<28} {url}")
