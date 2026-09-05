"""HPE has no RSS. Its host answers honestly (nonsense control 404s), so path
probing IS trustworthy here -- find the events/news surface instead."""
import re, sys, urllib.error, urllib.request
from concurrent.futures import ThreadPoolExecutor
sys.stdout.reconfigure(encoding="utf-8")
UA = ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
      "(KHTML, like Gecko) Chrome/126.0 Safari/537.36")
PATHS = ["/news-events/events", "/news-events/upcoming-events",
         "/events-and-presentations", "/news-events/press-releases",
         "/news-events", "/financial-reporting/quarterly-results",
         "/nonsense-control-zzz9"]
def probe(p):
    u = "https://investors.hpe.com" + p
    try:
        req = urllib.request.Request(u, headers={"User-Agent": UA})
        with urllib.request.urlopen(req, timeout=30) as r:
            b = r.read().decode("utf-8", "replace")
        hits = re.findall(r"(?i)[^<>]{0,90}(?:third quarter|Q3|September\s+\d{1,2},?\s*2026)[^<>]{0,90}", b)
        return p, f"{r.status} {len(b)}B", hits[:6]
    except urllib.error.HTTPError as e:
        return p, f"HTTP {e.code}", []
    except Exception as e:
        return p, type(e).__name__, []
with ThreadPoolExecutor(max_workers=7) as ex:
    for p, s, hits in ex.map(probe, PATHS):
        mark = "CTRL" if "nonsense" in p else "    "
        print(f"{mark} {p:<42} {s}")
        for h in hits:
            t = " ".join(h.split())
            if len(t) > 12: print(f"        | {t[:150]}")
