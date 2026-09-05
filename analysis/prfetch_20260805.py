"""Fetch the advance-PR bodies surfaced by today's RSS sweep (browser UA)."""
import re, urllib.request
from concurrent.futures import ThreadPoolExecutor

UA = ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
      "(KHTML, like Gecko) Chrome/126.0 Safari/537.36")

URLS = {
    "TRMB": "https://investor.trimble.com/news/news-details/2026/Trimble-Second-Quarter-Earnings-Call-and-Webcast/default.aspx",
    "SNOW": "https://investors.snowflake.com/news/news-details/2026/Snowflake-to-Announce-Financial-Results-for-the-Second-Quarter-of-Fiscal-2027-on-September-2-2026/default.aspx",
    "MDB":  "https://investors.mongodb.com/news-releases/news-release-details/mongodb-inc-announces-date-second-quarter-fiscal-2027-earnings",
    "SNPS": "https://investor.synopsys.com/news/news-details/2026/Synopsys-Announces-Earnings-Release-Date-for-Third-Quarter-Fiscal-Year-2026/default.aspx",
    "ALB":  "https://investors.albemarle.com/news-and-events/news/news-details/2026/Albemarle-Corporation-to-Release-Second-Quarter-2026-Earnings-Results-on-Wednesday-August-5-2026/default.aspx",
    "APP":  "https://investors.applovin.com/news/news-details/2026/AppLovin-to-Announce-Second-Quarter-2026-Results/default.aspx",
    "CF":   "https://ir.cfindustries.com/Investors/news/news-details/2026/CF-Industries-Holdings-Inc--Announces-Planned-Schedule-for-Quarterly-Financial-Results-to-be-Released-in-2026/default.aspx",
}

KEY = re.compile(
    r"(august|aug\.|september|sept|market close|market open|before the open|"
    r"after the close|a\.m\.|p\.m\.|eastern|ET\b|conference call|webcast|"
    r"will (report|release|announce|host)|second quarter|third quarter)", re.I)
TAG = re.compile(r"<(script|style)[^>]*>.*?</\1>", re.S | re.I)


def grab(sym, url):
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    try:
        with urllib.request.urlopen(req, timeout=30) as r:
            html = r.read().decode("utf-8", "replace")
    except Exception as e:
        return sym, url, f"FETCH FAILED: {type(e).__name__}: {e}", []
    html = TAG.sub(" ", html)
    text = re.sub(r"<[^>]+>", " ", html)
    for a, b in [("&nbsp;", " "), ("&amp;", "&"), ("&#39;", "'"),
                 ("&rsquo;", "'"), ("&#8217;", "'"), ("&ldquo;", '"'),
                 ("&rdquo;", '"'), ("&#8220;", '"'), ("&#8221;", '"')]:
        text = text.replace(a, b)
    text = re.sub(r"\s+", " ", text)
    hits, seen = [], set()
    for s in re.split(r"(?<=[.!?])\s+", text):
        s = s.strip()
        if 25 < len(s) < 500 and KEY.search(s) and s not in seen:
            seen.add(s)
            hits.append(s)
    return sym, url, "ok", hits[:10]


with ThreadPoolExecutor(max_workers=7) as ex:
    for sym, url, status, hits in ex.map(lambda kv: grab(*kv), URLS.items()):
        print("=" * 78)
        print(f"{sym}  {status}\n  {url}")
        for h in hits:
            print(f"   - {h}")
