"""Fetch the advance-PR bodies surfaced by today's RSS sweep (browser UA)."""
import re, urllib.request
from concurrent.futures import ThreadPoolExecutor

UA = ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
      "(KHTML, like Gecko) Chrome/126.0 Safari/537.36")

URLS = {
    # --- advance PRs naming the date, published in the last 72h ---
    "WOLF": "https://investor.wolfspeed.com/news/news-details/2026/Wolfspeed-Inc--Announces-Date-of-Fiscal-Fourth-Quarter-Earnings-Call-for-August-19-2026/default.aspx",
    "P":    "https://investor.everpuredata.com/news-and-events/press-releases/press-release-details/2026/Everpure-Announces-Date-and-Conference-Call-Information-for-Second-Quarter-Fiscal-2027-Financial-Results/default.aspx",
    "GAP":  "https://investors.gapinc.com/press-releases/news-details/2026/Gap-Inc--to-Report-Second-Quarter-Fiscal-2026-Results-on-August-27/default.aspx",
    "MRVL": "https://investor.marvell.com/news-events/press-releases/detail/1029/marvell-technology-inc-announces-conference-call-to-review-second-quarter-of-fiscal-year-2027-financial-results-announces-investor-day-on-october-6-2026",
    "ADSK": "https://investors.autodesk.com/news-releases/news-release-details/autodesk-extends-invitation-join-financial-results-conference-52",
    "NNE":  "https://ir.nanonuclearenergy.com/news-releases/news-release-details/nano-nuclear-hold-third-quarter-business-update-webcast-august",
    "SJM":  "https://investors.jmsmucker.com/news/news-details/2026/The-J-M--Smucker-Co--to-Report-First-Quarter-Earnings-and-Participate-in-the-2026-Barclays-Global-Consumer-Staples-Conference/default.aspx",
    # --- today's reporters ---
    "BMRN": "https://investors.biomarin.com/news/news-details/2026/BioMarin-to-Host-Second-Quarter-2026-Financial-Results-Conference-Call-and-Webcast-on-Thursday-August-6-2026-at-430pm-ET/default.aspx",
    "CART": "https://investors.instacart.com/news-releases/news-release-details/instacart-report-second-quarter-2026-financial-results-august-6",
    "ATI":  "https://ir.atimaterials.com/news-events/news-details/2026/ATI-Announces-Webcast-for-Second-Quarter-2026-Results/default.aspx",
    "ABNB": "https://investors.airbnb.com/press-releases/news-details/2026/Airbnb-to-Announce-Second-Quarter-2026-Results/default.aspx",
    # --- prior-quarter PRs, fetched for the TIME regime only (unknown_time) ---
    "BBWI_t": "https://investors.bbwinc.com/news-releases/news-release-details/bath-body-works-report-first-quarter-results-may-27-2026",
    "S_t":    "https://investors.sentinelone.com/press-releases/news-details/2026/SentinelOne-Announces-Date-of-Fiscal-First-Quarter-2027-Financial-Results-Conference-Call-and-Participation-in-Upcoming-Investor-Conference/default.aspx",
    "HPQ_t":  "https://investor.hp.com/news-events/news/news-details/2026/HP-Inc--to-Announce-Second-Quarter-Fiscal-2026-Earnings-on-May-27-2026/default.aspx",
    "NTNX_t": "https://ir.nutanix.com/news-releases/news-release-details/nutanix-announces-date-and-conference-call-information-third-5",
    # --- FLO: scheduling PRs live on the IR news list, not the /feed/ RSS ---
    "FLO_list": "https://investors.flowersfoods.com/news/news-releases/2026",
}

KEY = re.compile(
    r"(august|aug\.|september|sept|market close|market open|before the open|"
    r"after the close|a\.m\.|p\.m\.|eastern|ET\b|PT\b|conference call|webcast|"
    r"will (report|release|announce|host)|second quarter|third quarter|"
    r"fourth quarter|first quarter)", re.I)
TAG = re.compile(r"<(script|style)[^>]*>.*?</\1>", re.S | re.I)


def grab(item):
    sym, url = item
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
    return sym, url, "ok", hits[:12]


with ThreadPoolExecutor(max_workers=8) as ex:
    for sym, url, status, hits in ex.map(grab, URLS.items()):
        print("=" * 78)
        print(f"{sym}  [{status}]  {url}")
        for h in hits:
            print(f"   - {h}")
