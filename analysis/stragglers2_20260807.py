"""Pass 2: pull the ARMK/TPR advance PRs in full, and retry the SPA/timeout
hosts on alternate path shapes."""
import re, sys, urllib.error, urllib.request
from concurrent.futures import ThreadPoolExecutor

sys.stdout.reconfigure(encoding="utf-8")
UA = ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
      "(KHTML, like Gecko) Chrome/126.0 Safari/537.36")
HDRS = {"User-Agent": UA, "Accept": "text/html,application/xhtml+xml,*/*"}


def fetch(url, timeout=30):
    with urllib.request.urlopen(urllib.request.Request(url, headers=HDRS),
                                timeout=timeout) as r:
        return r.read().decode("utf-8", "replace"), r.geturl()


def flat(h):
    h = re.sub(r"<script.*?</script>|<style.*?</style>", " ", h, flags=re.S | re.I)
    t = re.sub(r"<[^>]+>", " ", h)
    t = re.sub(r"&nbsp;|&#160;|&#039;", " ", t)
    t = re.sub(r"&amp;", "&", t)
    return re.sub(r"\s+", " ", t)


# -- 1. find + fetch the ARMK and TPR advance PRs off their listing pages --
LISTINGS = {
    "ARMK": ("https://aramark.gcs-web.com/news-releases",
             r"conference call to review its third quarter fiscal 2026"),
    "TPR":  ("https://tapestry.gcs-web.com/news-releases",
             r"August 13, 2026"),
}
for sym, (lurl, _) in LISTINGS.items():
    print("=" * 74)
    try:
        h, _f = fetch(lurl)
    except Exception as e:
        print(f"{sym}: listing ERR {e}")
        continue
    links = re.findall(r'href="(/news-releases/news-release-details/[^"]+)"', h)
    host = lurl.split("/news-releases")[0]
    cand = [host + l for l in dict.fromkeys(links)][:6]
    for u in cand:
        try:
            hh, _ = fetch(u)
        except Exception as e:
            print(f"{sym}: {u} ERR {e}")
            continue
        t = flat(hh)
        if re.search(r"(third quarter fiscal 2026 results|fourth quarter.{0,40}2026"
                     r"|Q4 2026|August 13, 2026|August 11, 2026)", t, re.I):
            sents = re.findall(r"[^.]{0,220}(?:August \d{1,2}, 2026|a\.m\.|p\.m\.|"
                               r"market open|market close|before|after)[^.]{0,120}\.", t)
            print(f"{sym}  PR {u}")
            for s in dict.fromkeys(x.strip() for x in sents):
                if 40 < len(s) < 400:
                    print("   *", s)
            break

# -- 2. retry the SPA / timeout hosts on other path shapes --
RETRY = [
 ("BHP",  "https://www.bhp.com/investors/financial-results"),
 ("BHP",  "https://www.bhp.com/investors/shareholder-information/financial-calendar"),
 ("BHP",  "https://bhp.gcs-web.com/news-releases"),
 ("CAH",  "https://ir.cardinalhealth.com/news-releases"),
 ("CAH",  "https://ir.cardinalhealth.com/news/news-details/2026"),
 ("CAH",  "https://newsroom.cardinalhealth.com/"),
 ("AMCR", "https://amcor.gcs-web.com/news-releases"),
 ("AMCR", "https://www.amcor.com/investors"),
 ("GLOB", "https://investors.globant.com/press-releases"),
 ("GLOB", "https://globant.gcs-web.com/news-releases"),
 ("COTY", "https://coty.gcs-web.com/news-releases"),
 ("COTY", "https://investors.coty.com/news-events-and-presentations/events"),
 ("BABA", "https://www.alibabagroup.com/en-US/ir-events-and-presentations"),
 ("SQM",  "https://ir.sqm.com/news-events/events"),
 ("SQM",  "https://ir.sqm.com/events"),
 ("AAON", "https://investors.aaon.com/news-releases"),
 ("AAON", "https://investors.aaon.com/press-releases"),
]
PAT = re.compile(r"[^.\n]{0,160}(?:August|Aug\.)\s*\d{1,2},?\s*2026[^.\n]{0,160}", re.I)


def go(t):
    sym, url = t
    try:
        h, final = fetch(url, timeout=25)
    except urllib.error.HTTPError as e:
        return sym, url, f"HTTP {e.code}", []
    except Exception as e:
        return sym, url, f"ERR {type(e).__name__}", []
    txt = flat(h)
    hits = [s.strip() for s in dict.fromkeys(PAT.findall(txt))][:4]
    return sym, url, f"OK {len(txt)}ch", hits


with ThreadPoolExecutor(max_workers=10) as ex:
    for sym, url, st, hits in ex.map(go, RETRY):
        print("=" * 74)
        print(f"{sym}  {st}  {url}")
        for hh in hits:
            print(f"   - {hh[:250]}")
