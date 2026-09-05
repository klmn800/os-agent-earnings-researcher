"""SEC submissions sweep for the 2026-08-07 batch.

Per memory/reference_sec_acceptance_time_timing.md:
 - CIKs from the local inbox map, no per-symbol network lookup
 - screen 8-K items for 2.02, and 6-K via primaryDocDescription
 - print acceptanceDateTime RAW (never timezone-convert it)
 - print the year-ago same-quarter date + 364d for a date corroborator
"""
import json, re, sys, time, urllib.request
from concurrent.futures import ThreadPoolExecutor
from datetime import date, timedelta

sys.stdout.reconfigure(encoding="utf-8")
UA = "options-scanner-earnings-researcher klmn800alerts@gmail.com"
SYMS = ["FLR","MKTX","AAON","ARMK","CAH","LEGN","AMCR","COHR","TECH","AMAT",
        "GLOB","TPR","BHP","JKHY","KEYS","ADI","BILL","COTY","EL",
        "NCNO","HPQ","NTNX","LI","SQM","BABA"]

m = json.load(open("inbox/processed/company_tickers_20260731.json"))
cik = {v["ticker"]: str(v["cik_str"]).zfill(10) for v in m.values()}
DESC = re.compile(r"results|earnings|interim|half.?year|SEA|[1-4]Q\d\d|Q[1-4]", re.I)


def get(sym):
    c = cik.get(sym)
    if not c:
        return sym, None, "NO CIK IN MAP"
    url = f"https://data.sec.gov/submissions/CIK{c}.json"
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    try:
        with urllib.request.urlopen(req, timeout=25) as r:
            return sym, json.load(r), None
    except Exception as e:
        return sym, None, f"ERR {type(e).__name__} {e}"


with ThreadPoolExecutor(max_workers=6) as ex:
    out = list(ex.map(get, SYMS))

for sym, d, err in out:
    print("=" * 76)
    if err:
        print(f"{sym}: {err}")
        continue
    print(f"{sym}  CIK {cik[sym]}  tickers={d.get('tickers')}  {d.get('name')}")
    f = d["filings"]["recent"]
    n = len(f["form"])
    rows = []
    for i in range(n):
        form, items = f["form"][i], f.get("items", [""] * n)[i] or ""
        desc = (f.get("primaryDocDescription", [""] * n)[i] or "")
        hit = (form.startswith("8-K") and "2.02" in items) or \
              (form.startswith("6-K") and DESC.search(desc))
        if hit:
            rows.append((f["filingDate"][i], f["acceptanceDateTime"][i], form,
                         items, desc, f["accessionNumber"][i]))
    for r in rows[:9]:
        print(f"   {r[0]}  acc={r[1]}  {r[2]:5s} items={r[3]:12s} {r[4][:40]}")
    # +364d corroborator off the year-ago same-quarter filing
    for r in rows[:9]:
        y, mo, dd = map(int, r[0].split("-"))
        if date(y, mo, dd) < date(2025, 12, 31) and date(y, mo, dd) > date(2025, 6, 1):
            print(f"   ->  +364d from {r[0]} = {date(y,mo,dd)+timedelta(days=364)}")
