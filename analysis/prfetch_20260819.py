"""Fetch the four advance PRs surfaced by today's sweep, strip to text."""
import re, sys, urllib.request
from concurrent.futures import ThreadPoolExecutor
sys.stdout.reconfigure(encoding="utf-8")
UA = ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
      "(KHTML, like Gecko) Chrome/126.0 Safari/537.36")
HDRS = {"User-Agent": UA, "Accept": "text/html,application/xhtml+xml,*/*"}

URLS = {
 "M":    "https://www.macysinc.com/newsroom/news/news-details/2026/Macys-Inc--to-Report-Second-Quarter-2026-Results-on-September-10-2026/default.aspx",
 "GTLB": "https://ir.gitlab.com/news/news-details/2026/GitLab-To-Announce-Second-Quarter-Fiscal-2027-Financial-Results/default.aspx",
 "AVGO": "https://investors.broadcom.com/news-releases/news-release-details/broadcom-inc-announce-third-quarter-fiscal-year-2026-financial",
 "COO":  "https://investor.coopercos.com/news-releases/news-release-details/coopercompanies-announces-release-date-third-quarter-2026",
}

def strip(h):
    h = re.sub(r"(?is)<(script|style|noscript|svg)[^>]*>.*?</\1>", " ", h)
    h = re.sub(r"(?s)<!--.*?-->", " ", h)
    h = re.sub(r"(?i)</(p|div|h\d|li|br|tr)>", "\n", h)
    h = re.sub(r"<[^>]+>", " ", h)
    for a, b in [("&nbsp;"," "),("&amp;","&"),("&#39;","'"),("&rsquo;","'"),
                 ("&ldquo;",'"'),("&rdquo;",'"'),("&quot;",'"'),("&#8217;","'"),
                 ("&ndash;","-"),("&mdash;","-")]:
        h = h.replace(a, b)
    h = re.sub(r"[ \t]+", " ", h)
    return "\n".join(l.strip() for l in h.split("\n") if l.strip())

def go(kv):
    sym, url = kv
    try:
        req = urllib.request.Request(url, headers=HDRS)
        with urllib.request.urlopen(req, timeout=30) as r:
            return sym, url, strip(r.read().decode("utf-8", "replace"))
    except Exception as e:
        return sym, url, f"ERR {type(e).__name__}: {e}"

KEY = re.compile(r"before|after|market|a\.m\.|p\.m\.|am |pm |ET|Eastern|conference call|"
                 r"webcast|will report|will announce|will release|September|Septem", re.I)

with ThreadPoolExecutor(max_workers=4) as ex:
    for sym, url, txt in ex.map(go, URLS.items()):
        print(f"\n{'='*74}\n### {sym}\n{url}\n{'-'*74}")
        lines = [l for l in txt.split("\n") if KEY.search(l) and 15 < len(l) < 500]
        seen = set()
        for l in lines[:18]:
            if l not in seen:
                seen.add(l); print("  " + l)
