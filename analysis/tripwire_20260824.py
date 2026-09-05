import json, urllib.request
UA = {"User-Agent": "options-scanner-earnings-researcher klmn800alerts@gmail.com"}
for sym, cik in [("ORCL", 1341439), ("CPRT", 900075)]:
    url = f"https://data.sec.gov/submissions/CIK{cik:010d}.json"
    try:
        d = json.load(urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=30))
    except Exception as e:
        print(sym, "ERR", e); continue
    r = d["filings"]["recent"]
    rows = list(zip(r["form"], r["filingDate"], r["acceptanceDateTime"], r["primaryDocument"], r["accessionNumber"], r["items"]))
    rows = [x for x in rows if x[1] >= "2026-07-15"]
    print(f"=== {sym} (CIK {cik}) filings since 2026-07-15: {len(rows)}")
    for f, fd, ad, pd_, acc, items in rows[:15]:
        print(f"   {f:8} {fd}  accepted {ad}  items={items}  {pd_}")
