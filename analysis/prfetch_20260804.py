"""Fetch IR press-release bodies with a browser UA and print date/time sentences.

Same shape as prfetch_20260803.py -- WebFetch times out on exactly the hosts the
browser UA gets through. Pull HTML here, strip tags, print only sentences carrying
a date or a market-open/close phrase.
"""
import re, urllib.request
from concurrent.futures import ThreadPoolExecutor

UA = ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
      "(KHTML, like Gecko) Chrome/126.0 Safari/537.36")

URLS = {
    # --- disputes: advance PRs found in today's RSS sweep ---
    "PANW": "https://investors.paloaltonetworks.com/news-releases/news-release-details/palo-alto-networks-announce-fiscal-fourth-quarter-and-fiscal-7",
    "WDAY": "https://investor.workday.com/news-and-events/press-releases/news-details/2026/Workday-to-Announce-Fiscal-2027-Second-Quarter-Financial-Results-on-August-27-2026/default.aspx",
    "XPEV": "https://ir.xiaopeng.com/news-releases/news-release-details/xpeng-report-second-quarter-2026-financial-results-monday-august",
    "OKTA": "https://investor.okta.com/news-and-events/news-releases/news-details/2026/Okta-to-Announce-Second-Quarter-Fiscal-Year-2027-Financial-Results-on-August-26-2026/default.aspx",
    # --- unconfirmed reporting today: advance PRs ---
    "APTV": "https://ir.aptiv.com/news/news-details/2026/Aptiv-to-Release-Second-Quarter-2026-Financial-Results-on-August-4/default.aspx",
    "BRKR": "https://ir.bruker.com/press-releases/press-release-details/2026/Bruker-Announces-Date-and-Time-of-Second-Quarter-2026-Earnings-Release-and-Webcast/default.aspx",
    "CAT":  "https://investors.caterpillar.com/news/news-details/2026/Caterpillar-Inc--to-Announce-Second-Quarter-2026-Financial-Results-on-August-4/default.aspx",
    "CCEP": "https://ir.cocacolaep.com/news-releases/news-release-details/coca-cola-ep-plc-results-six-months-ended-3-july-2026",
    "CG":   "https://ir.carlyle.com/news-releases/news-release-details/carlyle-announce-second-quarter-2026-financial-results-and-host",
    "DOC":  "https://ir.healthpeak.com/news/news-details/2026/Healthpeak-Properties-Announces-Dates-of-Second-Quarter-2026-Earnings-Release-Conference-Call-and-Webcast/default.aspx",
    "DUK":  "https://investors.duke-energy.com/news/news-details/2026/Duke-Energy-to-announce-second-quarter-2026-financial-results-on-Aug--4/default.aspx",
    "DVA":  "https://investors.davita.com/2026-07-21-davita-inc-schedules-2nd-quarter-2026-investor-conference-call/",
    "DVN":  "https://investors.devonenergy.com/investors/press-releases/press-release-details/2026/Devon-Energy-Schedules-Second-Quarter-2026-Earnings-Release-and-Conference-Call/default.aspx",
}

KEEP = re.compile(
    r"(august|aug\.|market close|market open|before the open|after the close|"
    r"a\.m\.|p\.m\.|eastern|ET\b|conference call|webcast|will (report|release|announce|host))",
    re.I)
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
    text = re.sub(r"&nbsp;", " ", text)
    text = re.sub(r"&amp;", "&", text)
    text = re.sub(r"&#39;|&rsquo;|&#8217;", "'", text)
    text = re.sub(r"\s+", " ", text)
    sents = re.split(r"(?<=[.!?])\s+", text)
    hits, seen = [], set()
    for s in sents:
        s = s.strip()
        if 25 < len(s) < 400 and KEEP.search(s) and s not in seen:
            seen.add(s)
            hits.append(s)
    return sym, url, "ok", hits[:8]


with ThreadPoolExecutor(max_workers=8) as ex:
    for sym, url, status, hits in ex.map(lambda kv: grab(*kv), URLS.items()):
        print("=" * 78)
        print(f"{sym}  {status}\n  {url}")
        for h in hits:
            print(f"   - {h}")
