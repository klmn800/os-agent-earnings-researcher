"""Woodside investor calendar (WebFetch 403s -> browser UA) + APO RSS at the
corrected /news-events/ path (their IR uses /news-events/, not /news-and-events/).
"""
import re, urllib.request
from concurrent.futures import ThreadPoolExecutor

UA = ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
      "(KHTML, like Gecko) Chrome/126.0 Safari/537.36")

URLS = {
    "WDS-investors": "https://www.woodside.com/investors",
    "WDS-reports":   "https://www.woodside.com/investors/reports-investor-briefings",
    "WDS-events":    "https://www.woodside.com/media-centre/events",
    "APO-rss":       "https://ir.apollo.com/news-events/press-releases/rss",
    "PANW-press":    "https://www.paloaltonetworks.com/company/press/2026",
}

DATEY = re.compile(r"(20 aug|19 aug|august|aug\s*20|half.?year|h1|full.?year|"
                   r"quarter|results|report|briefing)", re.I)


def grab(key, url):
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    try:
        with urllib.request.urlopen(req, timeout=30) as r:
            html = r.read().decode("utf-8", "replace")
    except Exception as e:
        return key, url, f"FAILED {type(e).__name__}: {e}", []
    # RSS?
    items = re.findall(r"<item[ >](.*?)</item>", html, re.S | re.I)
    if items:
        out = []
        for it in items[:12]:
            t = re.search(r"<title>(?:<!\[CDATA\[)?(.*?)(?:\]\]>)?</title>", it, re.S | re.I)
            d = re.search(r"<pubDate>(.*?)</pubDate>", it, re.S | re.I)
            out.append(f"RSS  {d.group(1)[:22] if d else '?':<22} "
                       f"{re.sub(r'\\s+', ' ', t.group(1)).strip()[:100] if t else '?'}")
        return key, url, f"RSS OK {len(items)} items", out
    html = re.sub(r"<(script|style)[^>]*>.*?</\1>", " ", html, flags=re.S | re.I)
    text = re.sub(r"\s+", " ", re.sub(r"<[^>]+>", " ", html))
    text = text.replace("&nbsp;", " ").replace("&amp;", "&")
    hits, seen = [], set()
    # calendar-ish fragments: a date token near a results/report word
    for m in re.finditer(
            r"[^.]{0,120}\b\d{1,2}\s+(?:jan|feb|mar|apr|may|jun|jul|aug|sep|oct|nov|dec)[a-z]*"
            r"\s+20\d{2}[^.]{0,120}", text, re.I):
        s = m.group(0).strip()
        if DATEY.search(s) and s not in seen and len(s) > 25:
            seen.add(s)
            hits.append("CAL  " + s[:260])
    for m in re.finditer(r"[^.]{0,140}(half.?year|full.?year)[^.]{0,140}", text, re.I):
        s = m.group(0).strip()
        if s not in seen and len(s) > 30:
            seen.add(s)
            hits.append("TXT  " + s[:240])
    return key, url, "ok", hits[:14]


with ThreadPoolExecutor(max_workers=5) as ex:
    for key, url, status, hits in ex.map(lambda kv: grab(*kv), URLS.items()):
        print("=" * 78)
        print(f"{key}  {status}\n  {url}")
        for h in hits:
            print("   " + h)
