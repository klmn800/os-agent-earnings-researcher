"""Pull the advance-PR bodies found by the 08-20 sweep and print the
date/timing sentences verbatim. Browser UA (project UA gets tarpitted)."""
import re, sys, urllib.request
from concurrent.futures import ThreadPoolExecutor
sys.stdout.reconfigure(encoding="utf-8")
UA = ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
      "(KHTML, like Gecko) Chrome/126.0 Safari/537.36")
HDRS = {"User-Agent": UA, "Accept": "text/html,application/xhtml+xml,*/*"}

URLS = {
 "NIO":  "https://ir.nio.com/news-releases/news-release-details/nio-inc-report-unaudited-second-quarter-2026-financial-results",
 "KR":   "https://ir.kroger.com/news/news-details/2026/Kroger-Announces-Second-Quarter-Conference-Call-with-Investors/default.aspx",
 "CPB":  "https://investor.thecampbellscompany.com/news-releases/news-release-details/campbells-company-report-fourth-quarter-and-full-year-fiscal-0",
 "DOCU": "https://investor.docusign.com/news-and-events/press-releases/news-details/2026/Docusign-to-Announce-Second-Quarter-Fiscal-2027-Financial-Results-on-September-3-2026/default.aspx",
 "ZS":   "https://ir.zscaler.com/news-releases/news-release-details/zscaler-host-fourth-quarter-fiscal-year-2026-earnings-conference",
}
KEY = re.compile(r"before|after|market|close|open|a\.m\.|p\.m\.|am ET|pm ET|"
                 r"ET\b|PT\b|CT\b|conference call|webcast|September|Sept|"
                 r"August|202[67]", re.I)

def strip(h):
    h = re.sub(r"(?is)<(script|style|nav|header|footer).*?</\1>", " ", h)
    h = re.sub(r"(?s)<[^>]+>", " ", h)
    h = (h.replace("&nbsp;", " ").replace("&amp;", "&").replace("&#39;", "'")
          .replace("&rsquo;", "'").replace("&quot;", '"').replace("&ldquo;", '"')
          .replace("&rdquo;", '"').replace("&mdash;", "--"))
    return re.sub(r"\s+", " ", h)

def go(kv):
    sym, url = kv
    try:
        req = urllib.request.Request(url, headers=HDRS)
        with urllib.request.urlopen(req, timeout=30) as r:
            txt = strip(r.read().decode("utf-8", "replace"))
    except Exception as e:
        return sym, url, f"ERR {type(e).__name__}: {e}", []
    sents = re.split(r"(?<=[.!?])\s+", txt)
    hits = [s.strip() for s in sents if KEY.search(s) and 30 < len(s) < 500]
    seen, out = set(), []
    for s in hits:
        if s not in seen:
            seen.add(s); out.append(s)
    return sym, url, f"OK {len(txt)}B", out[:14]

with ThreadPoolExecutor(max_workers=5) as ex:
    for sym, url, st, hits in ex.map(go, URLS.items()):
        print(f"\n{'='*72}\n{sym}  {st}\n  {url}")
        for s in hits:
            print(f"   . {s[:320]}")
