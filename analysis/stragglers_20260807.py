"""Non-RSS IR probes for the 08-07 stragglers: plain-HTML press-release and
events/calendar pages (the CMI lesson -- a company with no scheduling PR is not
automatically unresearchable). Browser UA, follow redirects, print final URL."""
import re, sys, urllib.error, urllib.request
from concurrent.futures import ThreadPoolExecutor

sys.stdout.reconfigure(encoding="utf-8")
UA = ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
      "(KHTML, like Gecko) Chrome/126.0 Safari/537.36")
HDRS = {"User-Agent": UA, "Accept": "text/html,application/xhtml+xml,*/*"}

TARGETS = [
 ("AAON", "https://investors.aaon.com/news/default.aspx"),
 ("AAON", "https://investors.aaon.com/events-and-presentations/default.aspx"),
 ("ARMK", "https://www.aramark.com/investor-relations"),
 ("ARMK", "https://aramark.gcs-web.com/rss/pressrelease.aspx"),
 ("ARMK", "https://aramark.gcs-web.com/news-releases"),
 ("CAH",  "https://ir.cardinalhealth.com/news/default.aspx"),
 ("CAH",  "https://ir.cardinalhealth.com/events-and-presentations/default.aspx"),
 ("AMCR", "https://www.amcor.com/investors/financial-information/results"),
 ("AMCR", "https://www.amcor.com/media/news"),
 ("GLOB", "https://investors.globant.com/news-releases"),
 ("GLOB", "https://investors.globant.com/news-events/press-releases"),
 ("TPR",  "https://www.tapestry.com/investors/"),
 ("TPR",  "https://tapestry.gcs-web.com/rss/pressrelease.aspx"),
 ("TPR",  "https://tapestry.gcs-web.com/news-releases"),
 ("BHP",  "https://www.bhp.com/investors/financial-results"),
 ("BHP",  "https://www.bhp.com/news/media-centre"),
 ("COTY", "https://investors.coty.com/news-events-and-presentations/events/default.aspx"),
 ("SQM",  "https://ir.sqm.com/events-and-presentations"),
 ("SQM",  "https://ir.sqm.com/news-events/ir-calendar"),
 ("BABA", "https://www.alibabagroup.com/en-US/ir-financial-reports-quarterly-results"),
 ("BABA", "https://www.alibabagroup.com/en-US/ir-news"),
 ("NCNO", "https://www.globenewswire.com/en/search/organization/nCino"),
]

# Aug/Sep date mentions and release-timing verbs
PAT = re.compile(
  r"[^.\n]{0,180}(?:August|Aug\.|Aug\s+\d|September|Sept\.)\s*\d{1,2},?\s*2026[^.\n]{0,180}",
  re.I)
TIMING = re.compile(r"before market|after market|market open|market close|"
                    r"a\.m\.|p\.m\.|AEST|ET\b|Eastern", re.I)


def go(t):
    sym, url = t
    try:
        with urllib.request.urlopen(urllib.request.Request(url, headers=HDRS),
                                    timeout=20) as r:
            h = r.read().decode("utf-8", "replace")
            final = r.geturl()
    except urllib.error.HTTPError as e:
        return sym, url, f"HTTP {e.code}", []
    except Exception as e:
        return sym, url, f"ERR {type(e).__name__} {str(e)[:60]}", []
    h = re.sub(r"<script.*?</script>|<style.*?</style>", " ", h, flags=re.S | re.I)
    txt = re.sub(r"<[^>]+>", " ", h)
    txt = re.sub(r"&nbsp;|&#160;", " ", txt)
    txt = re.sub(r"&amp;", "&", txt)
    txt = re.sub(r"\s+", " ", txt)
    hits, seen = [], set()
    for m in PAT.findall(txt):
        s = m.strip()
        if s not in seen and len(s) > 20:
            seen.add(s)
            hits.append(s)
    note = f"OK {len(txt)}ch" + (" (redir)" if final != url else "")
    return sym, url, note, hits[:5]


with ThreadPoolExecutor(max_workers=10) as ex:
    for sym, url, st, hits in ex.map(go, TARGETS):
        print("=" * 74)
        print(f"{sym}  {st}  {url}")
        for hh in hits:
            star = " ***" if TIMING.search(hh) else ""
            print(f"   - {hh[:280]}{star}")
