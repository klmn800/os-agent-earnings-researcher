"""SEC submissions sweep for the 2026-08-11 batch.

Per memory/reference_sec_acceptance_time_timing.md:
 - CIKs from the local inbox map, no per-symbol network lookup
 - screen 8-K items for 2.02, and 6-K via primaryDocDescription
 - print acceptanceDateTime RAW (never timezone-convert it)
 - print the year-ago same-quarter date + 364d for a date corroborator
"""
import json, re, sys, urllib.request
from concurrent.futures import ThreadPoolExecutor
from datetime import date, timedelta

sys.stdout.reconfigure(encoding="utf-8")
UA = "options-scanner-earnings-researcher klmn800alerts@gmail.com"
SYMS = ["TECH", "NCNO", "PVH", "PDD", "LI", "NIO", "COTY", "SQM"]

m = json.load(open("inbox/processed/company_tickers_20260731.json"))
cik = {v["ticker"]: str(v["cik_str"]).zfill(10) for v in m.values()}
DESC = re.compile(r"results|earnings|interim|half.?year|[1-4]Q\d\d|Q[1-4]", re.I)


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
    # newest 6 filings of ANY kind - merger / absence watch
    for i in range(min(6, n)):
        print(f"   recent: {f['form'][i]:8s} {f['filingDate'][i]}  "
              f"acc={f['acceptanceDateTime'][i]}  "
              f"{(f.get('primaryDocDescription', ['']*n)[i] or '')[:38]}")
    rows = []
    for i in range(n):
        form, items = f["form"][i], f.get("items", [""] * n)[i] or ""
        desc = (f.get("primaryDocDescription", [""] * n)[i] or "")
        hit = (form.startswith("8-K") and "2.02" in items) or \
              (form.startswith("6-K") and DESC.search(desc))
        if hit:
            rows.append((f["filingDate"][i], f["acceptanceDateTime"][i], form,
                         items, desc, f["accessionNumber"][i]))
    print("   -- earnings-ish filings --")
    for r in rows[:9]:
        print(f"   {r[0]}  acc={r[1]}  {r[2]:5s} items={r[3]:12s} {r[4][:40]}")
    for r in rows[:9]:
        y, mo, dd = map(int, r[0].split("-"))
        if date(2025, 6, 1) < date(y, mo, dd) < date(2025, 12, 31):
            print(f"   ->  +364d from {r[0]} = {date(y,mo,dd)+timedelta(days=364)}")
