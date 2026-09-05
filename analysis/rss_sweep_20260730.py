"""IR RSS/news sweep for 2026-07-30. Q4-hosted IR sites expose /rss/pressrelease.aspx
(cf. memory/reference_ir_rss_feeds.md). Threaded, generous timeouts, prints newest
few titles + pubDates per host so I can see (a) is the feed current, (b) is there an
advance earnings-date PR.
"""
import re, urllib.request, concurrent.futures as cf

UA = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) options-scanner-earnings-researcher klmn800alerts@gmail.com"

HOSTS = [
 ("GO",   "https://investors.groceryoutlet.com/rss/pressrelease.aspx"),
 ("RDW",  "https://ir.rdw.com/rss/pressrelease.aspx"),
 ("RDW2", "https://ir.redwirespace.com/rss/pressrelease.aspx"),
 ("TECH", "https://investors.bio-techne.com/rss/pressrelease.aspx"),
 ("TRMB", "https://investor.trimble.com/rss/pressrelease.aspx"),
 ("MNST", "https://investors.monsterbevcorp.com/rss/pressrelease.aspx"),
 ("NTRA", "https://investor.natera.com/rss/pressrelease.aspx"),
 ("GRAL", "https://investors.grail.com/rss/pressrelease.aspx"),
 ("HRB",  "https://investors.hrblock.com/rss/pressrelease.aspx"),
 ("CSCO", "https://investor.cisco.com/rss/pressrelease.aspx"),
 ("AMCR", "https://investors.amcor.com/rss/pressrelease.aspx"),
 ("PANW", "https://investors.paloaltonetworks.com/rss/pressrelease.aspx"),
 ("ZM",   "https://investors.zoom.us/rss/pressrelease.aspx"),
 ("ROST", "https://investors.rossstores.com/rss/pressrelease.aspx"),
 ("TOL",  "https://investors.tollbrothers.com/rss/pressrelease.aspx"),
 ("FLO",  "https://investors.flowersfoods.com/rss/pressrelease.aspx"),
 ("JD",   "https://ir.jd.com/rss/news-releases.xml"),
 ("SE",   "https://www.sea.com/rss/news-releases.xml"),
 ("NU",   "https://international.nubank.com.br/rss/pressrelease.aspx"),
 ("XP",   "https://investors.xpinc.com/rss/pressrelease.aspx"),
 ("SQM",  "https://ir.sqm.com/rss/pressrelease.aspx"),
 ("BIDU", "https://ir.baidu.com/rss/news-releases.xml"),
 ("XPEV", "https://ir.xiaopeng.com/rss/news-releases.xml"),
 ("YPF",  "https://investors.ypf.com/rss/pressrelease.aspx"),
 ("DNN",  "https://denisonmines.com/rss"),
 ("NXE",  "https://www.nexgenenergy.ca/rss"),
 ("NNE",  "https://ir.nanonuclearenergy.com/rss/pressrelease.aspx"),
 ("GRAL2","https://investors.grail.com/rss/news-releases.xml"),
]

def fetch(pair):
    sym, url = pair
    try:
        req = urllib.request.Request(url, headers={"User-Agent": UA})
        with urllib.request.urlopen(req, timeout=25) as r:
            raw = r.read().decode("utf-8", "replace")
    except Exception as e:
        return sym, url, f"FAIL {type(e).__name__}: {e}", []
    items = re.findall(r"<item>(.*?)</item>", raw, re.S)
    rows = []
    for it in items[:8]:
        t = re.search(r"<title>(?:<!\[CDATA\[)?(.*?)(?:\]\]>)?</title>", it, re.S)
        d = re.search(r"<pubDate>(.*?)</pubDate>", it, re.S)
        rows.append(((d.group(1).strip()[:22] if d else "?"),
                     (t.group(1).strip()[:110] if t else "?")))
    return sym, url, f"ok ({len(items)} items)", rows

with cf.ThreadPoolExecutor(max_workers=14) as ex:
    for sym, url, status, rows in ex.map(fetch, HOSTS):
        print(f"\n--- {sym}  {status}  [{url}]")
        for d, t in rows:
            print(f"    {d}  {t}")
