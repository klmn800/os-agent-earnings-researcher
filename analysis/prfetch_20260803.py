"""Fetch IR press-release bodies with a browser UA and print the date/time sentences.

WebFetch times out on exactly the hosts that rejected the project UA in the RSS
sweep (onsemi, ametek, amgen, bwxt, diamondback...). The browser UA gets through,
so pull the HTML here, strip tags, and print only sentences that carry a date or a
market-open/close phrase.
"""
import re, sys, urllib.request
from concurrent.futures import ThreadPoolExecutor

UA = ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
      "(KHTML, like Gecko) Chrome/126.0 Safari/537.36")

URLS = {
    "ON":   "https://investor.onsemi.com/news-releases/news-release-details/onsemi-announce-second-quarter-financial-results-3",
    "AME":  "https://investors.ametek.com/news-releases/news-release-details/ametek-announces-second-quarter-2026-earnings-call-and-webcasted",
    "AMGN": "https://investors.amgen.com/news-releases/news-release-details/amgen-announces-webcast-2026-second-quarter-financial-results",
    "BWXT": "https://investors.bwxt.com/news-releases/news-release-details/bwx-technologies-announce-second-quarter-2026-results-monday",
    "FANG": "https://ir.diamondbackenergy.com/news-releases/news-release-details/diamondback-energy-inc-schedules-second-quarter-2026-conference",
    "AMD":  "https://ir.amd.com/news-events/press-releases/detail/1289/amd-to-report-fiscal-second-quarter-2026-financial-results",
    "ANET": "https://investors.arista.com/Communications/Press-Releases-and-Events/Press-Release-Detail/2026/Arista-Networks-to-Announce-Q2-2026-Financial-Results-on-Tuesday-August-4-2026/default.aspx",
    "ADM":  "https://investors.adm.com/news/news-details/2026/ADM-to-Release-Second-Quarter-Financial-Results-on-August-4-2026/default.aspx",
    "INSP": "https://investors.inspiresleep.com/news/news-details/2026/Correction-Inspire-Medical-Systems-Inc--to-Report-Second-Quarter-2026-Financial-Results-on-August-3-2026/default.aspx",
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
    text = re.sub(r"&#39;|&rsquo;", "'", text)
    text = re.sub(r"\s+", " ", text)
    sents = re.split(r"(?<=[.!?])\s+", text)
    hits, seen = [], set()
    for s in sents:
        s = s.strip()
        if 25 < len(s) < 400 and KEEP.search(s) and s not in seen:
            seen.add(s)
            hits.append(s)
    return sym, url, "ok", hits[:8]


with ThreadPoolExecutor(max_workers=9) as ex:
    for sym, url, status, hits in ex.map(lambda kv: grab(*kv), URLS.items()):
        print("=" * 78)
        print(f"{sym}  {status}\n  {url}")
        for h in hits:
            print(f"   - {h}")
