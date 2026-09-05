"""Fetch advance-earnings PR bodies found by the 08-07 RSS sweep and pull the
date/time sentence out of each. Browser UA per reference_ir_rss_feeds.md."""
import re, sys, urllib.request
from concurrent.futures import ThreadPoolExecutor

sys.stdout.reconfigure(encoding="utf-8")
UA = ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
      "(KHTML, like Gecko) Chrome/126.0 Safari/537.36")
URLS = {
 "NTNX": "https://ir.nutanix.com/news-releases/news-release-details/nutanix-announces-date-and-conference-call-information-fiscal-6",
 "HPQ":  "https://investor.hp.com/news-events/news/news-details/2026/HP-Inc--to-Announce-Third-Quarter-Fiscal-2026-Earnings-on-August-26-2026-and-to-Attend-Upcoming-Investor-Conferences/default.aspx",
 "LEGN": "https://investors.legendbiotech.com/news-releases/news-release-details/legend-biotech-host-investor-conference-call-second-quarter-2026",
 "COHR": "https://ir.coherent.com/news-releases/news-release-details/coherent-corp-announces-timing-fy2026-fourth-quarter-and-fiscal",
 "AMAT": "https://ir.appliedmaterials.com/news-releases/news-release-details/applied-materials-report-fiscal-third-quarter-2026-results-aug",
 "KEYS": "https://investor.keysight.com/investor-news-and-events/financial-press-releases/press-release-details/2026/Keysight-Technologies-to-Report-Fiscal-Third-Quarter-Results-on-August-18-2026/default.aspx",
 "ADI":  "https://investor.analog.com/news-releases/news-release-details/analog-devices-report-third-quarter-fiscal-year-2026-financial",
 "BILL": "https://investor.bill.com/news/news-details/2026/BILL-to-Report-Fiscal-Fourth-Quarter-and-Fiscal-2026-Financial-Results/default.aspx",
 "EL":   "https://investors.elcompanies.com/en/news-and-media/newsroom/press-releases/2026/08-05-2026-213516937",
 "JKHY": "https://ir.jackhenry.com/news-releases/news-release-details/jack-henry-associates-provide-webcast-fourth-quarter-and-full",
 "MKTX": "https://investor.marketaxess.com/news/news-details/2026/MarketAxess-to-Host-Conference-Call-Announcing-Second-Quarter-2026-Financial-Results-on-Friday-August-7-2026/default.aspx",
}
SENT = re.compile(r"[^.]*?(?:August|Aug\.|before|after|a\.m\.|p\.m\.|ET|Eastern|"
                  r"market open|market close|conference call)[^.]*\.", re.I)


def go(kv):
    sym, url = kv
    try:
        req = urllib.request.Request(url, headers={"User-Agent": UA})
        with urllib.request.urlopen(req, timeout=25) as r:
            h = r.read().decode("utf-8", "replace")
    except Exception as e:
        return sym, f"ERR {type(e).__name__} {e}", []
    h = re.sub(r"<script.*?</script>|<style.*?</style>", " ", h, flags=re.S | re.I)
    txt = re.sub(r"<[^>]+>", " ", h)
    txt = re.sub(r"&nbsp;|&#160;", " ", txt)
    txt = re.sub(r"&amp;", "&", txt)
    txt = re.sub(r"\s+", " ", txt)
    hits, seen = [], set()
    for m in SENT.findall(txt):
        s = m.strip()
        if 30 < len(s) < 400 and s not in seen:
            seen.add(s)
            hits.append(s)
    return sym, "ok", hits[:6]


with ThreadPoolExecutor(max_workers=8) as ex:
    for sym, st, hits in ex.map(go, URLS.items()):
        print("=" * 74)
        print(f"{sym}: {st}")
        for hh in hits:
            print("   *", hh)
