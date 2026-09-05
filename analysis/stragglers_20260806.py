"""Straggler chase for 2026-08-06.

FLO  : the Q2 advance PR landed 08-05 on the IR news list -- pull its link+body.
ATI  : the 07-14 webcast PR names the date; my KEY filter dropped that sentence.
BBY/DG/ULTA: no advance-PR channel found -- try the IR events/news HTML pages.
"""
import re, urllib.request
from concurrent.futures import ThreadPoolExecutor

UA = ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
      "(KHTML, like Gecko) Chrome/126.0 Safari/537.36")
TAG = re.compile(r"<(script|style)[^>]*>.*?</\1>", re.S | re.I)

PAGES = {
    "FLO_list": "https://investors.flowersfoods.com/news/news-releases/2026",
    "ATI_pr":   "https://ir.atimaterials.com/news-events/news-details/2026/ATI-Announces-Webcast-for-Second-Quarter-2026-Results/default.aspx",
    "BBY_ev":   "https://investors.bestbuy.com/News--Events/events-and-presentations/default.aspx",
    "DG_news":  "https://newscenter.dollargeneral.com/news/",
    "DG_ir":    "https://investor.dollargeneral.com/news-and-events/news/default.aspx",
    "ULTA_news":"https://ir.ultabeauty.com/news-and-events/press-releases",
}

# broad: any sentence mentioning an August/September date or a clock time
WIDE = re.compile(r"(august|aug\.|september|sept\.|\d{1,2}:\d{2}|a\.m\.|p\.m\.|"
                  r"market open|market close|second quarter|Q2)", re.I)


def txt(html):
    html = TAG.sub(" ", html)
    t = re.sub(r"<[^>]+>", " ", html)
    for a, b in [("&nbsp;", " "), ("&amp;", "&"), ("&#39;", "'"),
                 ("&rsquo;", "'"), ("&#8217;", "'"), ("&#160;", " ")]:
        t = t.replace(a, b)
    return re.sub(r"\s+", " ", t)


def grab(item):
    name, url = item
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    try:
        with urllib.request.urlopen(req, timeout=30) as r:
            html = r.read().decode("utf-8", "replace")
            final = r.geturl()
    except Exception as e:
        return name, url, f"FAIL {type(e).__name__}: {e}", [], []
    # pull any news-detail links that look like scheduling PRs
    links = sorted({m for m in re.findall(r'href="([^"]+)"', html)
                    if re.search(r"report|results|earnings|webcast|conference",
                                 m, re.I)})[:12]
    body = txt(html)
    hits, seen = [], set()
    for s in re.split(r"(?<=[.!?])\s+", body):
        s = s.strip()
        if 25 < len(s) < 420 and WIDE.search(s) and s not in seen:
            seen.add(s)
            hits.append(s)
    return name, final, "ok", links, hits[:14]


with ThreadPoolExecutor(max_workers=6) as ex:
    for name, url, status, links, hits in ex.map(grab, PAGES.items()):
        print("=" * 78)
        print(f"{name}  [{status}]  {url}")
        for l in links:
            print(f"   LINK {l}")
        for h in hits:
            print(f"   - {h}")
