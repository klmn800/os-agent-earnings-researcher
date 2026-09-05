"""Woodside 6-K history: EDGAR filingDate is ET, so it answers which US session
an ASX-morning release actually lands in. Look at the Aug filings each year."""
import gzip, json, urllib.request

UA = "options-scanner-earnings-researcher klmn800alerts@gmail.com"

def get(url):
    req = urllib.request.Request(url, headers={"User-Agent": UA,
                                               "Accept-Encoding": "gzip, deflate"})
    with urllib.request.urlopen(req, timeout=30) as r:
        d = r.read()
        enc = r.headers.get("Content-Encoding")
    return gzip.decompress(d) if enc == "gzip" else d

j = json.loads(get("https://data.sec.gov/submissions/CIK0000844551.json"))
rec = j["filings"]["recent"]
print(f"{j['name']} | tickers={j.get('tickers')}")
print("6-K / 20-F filings in Aug (any year) and Feb, with ET acceptance:")
for i, f in enumerate(rec["form"]):
    d = rec["filingDate"][i]
    if f.startswith(("6-K", "20-F")) and d[5:7] in ("08", "02"):
        print(f"  {d}  {f:<6} acc={rec['acceptanceDateTime'][i]}  {rec['primaryDocDescription'][i][:70]}")
