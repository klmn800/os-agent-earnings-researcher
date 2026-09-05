"""Browser-UA fetch of the IR pages for the four symbols with no usable RSS:
APO (feed 404s), PANW (feed has no Q4 advance PR), FLO (403 everywhere),
WDS (Australian, no Q4-style feed).

Prints sentences carrying a date / market-timing phrase, plus any anchor text
that looks like an earnings-scheduling item.
"""
import re, urllib.request
from concurrent.futures import ThreadPoolExecutor

UA = ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
      "(KHTML, like Gecko) Chrome/126.0 Safari/537.36")

URLS = {
    "APO-news":   "https://ir.apollo.com/news-and-events/news/default.aspx",
    "APO-events": "https://ir.apollo.com/news-and-events/events/default.aspx",
    "PANW-news":  "https://investors.paloaltonetworks.com/news-releases",
    "PANW-events": "https://investors.paloaltonetworks.com/events-and-presentations",
    "FLO-news":   "https://www.flowersfoods.com/news/news-releases/category/investor-relations/",
    "WDS-news":   "https://www.woodside.com/investors/news-and-announcements",
    "WDS-cal":    "https://www.woodside.com/investors/financial-reporting-calendar",
}

DATEY = re.compile(r"(august|aug\.?\s*\d|second quarter|half.?year|q2|fourth quarter|"
                   r"fiscal fourth|full.?year|market close|market open|2026)", re.I)
EARN = re.compile(r"(report|results|earnings|conference call|webcast|announce)", re.I)
TAGS = re.compile(r"<(script|style|nav|footer)[^>]*>.*?</\1>", re.S | re.I)


def grab(key, url):
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    try:
        with urllib.request.urlopen(req, timeout=30) as r:
            html = r.read().decode("utf-8", "replace")
            final = r.geturl()
    except Exception as e:
        return key, url, f"FAILED {type(e).__name__}: {e}", [], []
    anchors = []
    for m in re.finditer(r'<a[^>]+href="([^"]+)"[^>]*>(.*?)</a>', html, re.S | re.I):
        txt = re.sub(r"\s+", " ", re.sub(r"<[^>]+>", " ", m.group(2))).strip()
        if 15 < len(txt) < 160 and EARN.search(txt) and DATEY.search(txt):
            anchors.append((txt, m.group(1)))
    body = TAGS.sub(" ", html)
    text = re.sub(r"\s+", " ", re.sub(r"<[^>]+>", " ", body))
    text = text.replace("&nbsp;", " ").replace("&amp;", "&")
    sents = []
    seen = set()
    for s in re.split(r"(?<=[.!?])\s+", text):
        s = s.strip()
        if 30 < len(s) < 320 and EARN.search(s) and DATEY.search(s) and s not in seen:
            seen.add(s)
            sents.append(s)
    note = "ok" + (f" (redirect -> {final})" if final != url else "")
    return key, url, note, sents[:6], anchors[:10]


with ThreadPoolExecutor(max_workers=7) as ex:
    for key, url, status, sents, anchors in ex.map(lambda kv: grab(*kv), URLS.items()):
        print("=" * 78)
        print(f"{key}  {status}\n  {url}")
        for t, h in anchors:
            print(f"   LINK  {t}\n         {h}")
        for s in sents:
            print(f"   TEXT  {s}")
