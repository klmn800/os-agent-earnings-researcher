"""HPE feed-shape rotation + SEC Item 2.02 furnish-time history for HPE/GME.

HPE: investors.hpe.com 404s on both standard RSS paths, so rotate the prefix and
path set to find the real feed (the nCino/Agilent lesson: the host usually exists
under a shape we haven't tried). A nonsense-path control runs against each host
FIRST -- without it, a bot-wall host makes every guess read as "found" (the CPRT
trap, standing rule 3).

SEC: acceptanceDateTime of Item 2.02 8-Ks resolves bmo/amc in bulk.
NEVER timezone-convert acceptanceDateTime -- it is ET for some filings and UTC
for others. Printed RAW alongside the form/items so the pattern is judged, not
computed. CIKs resolved BY TICKER via company_tickers.json, never by name.
"""
import json, re, ssl, sys, urllib.error, urllib.request
from concurrent.futures import ThreadPoolExecutor
sys.stdout.reconfigure(encoding="utf-8")

BROWSER = ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
           "(KHTML, like Gecko) Chrome/126.0 Safari/537.36")
SECUA = "options-scanner-research klmn800alerts@gmail.com"

def get(url, ua=BROWSER, timeout=25):
    req = urllib.request.Request(url, headers={"User-Agent": ua, "Accept": "*/*"})
    with urllib.request.urlopen(req, timeout=timeout) as r:
        return r.status, r.read()

# ---------- 1. HPE feed hunt, with per-host nonsense-path control ----------
HOSTS = ["investors.hpe.com", "investor.hpe.com", "ir.hpe.com",
         "www.investor.hpe.com", "hpe.gcs-web.com"]
PATHS = ["/rss/news-releases.xml", "/rss/pressrelease.aspx",
         "/rss/news_releases.xml", "/feed/news.rss",
         "/nonsense-control-path-zzz9/"]   # <-- control MUST 404 on a sane host

def probe(u):
    try:
        st, body = get("https://" + u)
        n = len(re.findall(r"<item[ >]", body.decode("utf-8", "replace"), re.I))
        return u, f"{st}  {len(body)}B  items={n}"
    except urllib.error.HTTPError as e:
        return u, f"HTTP {e.code}"
    except Exception as e:
        return u, f"{type(e).__name__}"

targets = [h + p for h in HOSTS for p in PATHS]
print("=== HPE feed-shape rotation (last row per host is the nonsense control) ===")
with ThreadPoolExecutor(max_workers=10) as ex:
    for u, s in ex.map(probe, targets):
        mark = "CTRL" if "nonsense" in u else "    "
        print(f"  {mark} {u:<52} {s}")

# ---------- 2. SEC: resolve CIK by ticker, then 2.02 furnish history ----------
print("\n=== SEC Item 2.02 furnish history (acceptanceDateTime RAW, never converted) ===")
st, body = get("https://www.sec.gov/files/company_tickers.json", ua=SECUA)
tick = {v["ticker"]: str(v["cik_str"]).zfill(10) for v in json.loads(body).values()}

for sym in ["HPE", "GME"]:
    cik = tick.get(sym)
    print(f"\n--- {sym}  CIK {cik} ---")
    if not cik:
        print("   ticker absent from company_tickers.json"); continue
    st, body = get(f"https://data.sec.gov/submissions/CIK{cik}.json", ua=SECUA)
    d = json.loads(body)
    print(f"   name={d.get('name')}  tickers={d.get('tickers')}")
    r = d["filings"]["recent"]
    rows = list(zip(r["form"], r["filingDate"], r["acceptanceDateTime"],
                    r["items"], r["primaryDocDescription"]))
    n = 0
    for form, fdate, acc, items, desc in rows:
        if form.startswith("8-K") and "2.02" in (items or ""):
            print(f"   {form:<6} filed {fdate}  accepted {acc}  items={items}")
            n += 1
            if n >= 9: break
    print("   -- most recent 6 filings of ANY form (is an advance 8-K out?) --")
    for form, fdate, acc, items, desc in rows[:6]:
        print(f"      {form:<8} {fdate}  {acc}  items={items or '-'}")
