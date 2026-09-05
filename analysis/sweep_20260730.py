"""SEC bulk sweep for 2026-07-30 dispute batch.

Per symbol:
  - CIK lookup (absent => delisted screen, cf. reference_ma_phantom_earnings)
  - all recent 8-K filings carrying Item 2.02 -> filingDate + acceptanceDateTime in ET
  - +364d weekday-aligned prediction off the same-quarter year-ago 2.02 filing
  - most recent filings of any form (phantom / still-listed-no-event screen)
"""
import json, os, sys, time, urllib.request
from datetime import datetime, timedelta, timezone

UA = "options-scanner-earnings-researcher klmn800alerts@gmail.com"
BASE = "E:/options_scanner/agents/earnings_researcher/inbox"

SYMS = ["GO","RDW","TECH","TRMB","MNST","NTRA","GRAL","HRB","CSCO","AMCR","FLO",
        "PANW","TOL","BIDU","ZM","NXE","JD","XPEV","IAC","YPF","DNN","SE","NNE",
        "NU","XP","SQM","ROST","WMT","PPLI"]

DB_DATE = {
 "GO":"2026-08-04","RDW":"2026-08-05","TECH":"2026-08-05","TRMB":"2026-08-05",
 "MNST":"2026-08-06","NTRA":"2026-08-06","GRAL":"2026-08-11","HRB":"2026-08-11",
 "CSCO":"2026-08-12","AMCR":"2026-08-13","FLO":"2026-08-14","PANW":"2026-08-18",
 "TOL":"2026-08-18","BIDU":"2026-08-19","ZM":"2026-08-20","NXE":"2026-08-05",
 "JD":"2026-08-11","XPEV":"2026-08-18","IAC":"2026-08-03","YPF":"2026-08-10",
 "DNN":"2026-08-11","SE":"2026-08-11","NNE":"2026-08-12","NU":"2026-08-13",
 "XP":"2026-08-17","SQM":"2026-08-18","ROST":"2026-08-20","WMT":"2026-08-20",
 "PPLI":"2026-08-03",
}

def get(url, dest=None):
    req = urllib.request.Request(url, headers={"User-Agent": UA,
                                               "Accept-Encoding": "gzip, deflate"})
    with urllib.request.urlopen(req, timeout=30) as r:
        data = r.read()
    if r.headers.get("Content-Encoding") == "gzip":
        import gzip
        data = gzip.decompress(data)
    if dest:
        open(dest, "wb").write(data)
    return data

# --- ticker -> CIK map (cached) ---
tmap_path = os.path.join(BASE, "company_tickers.json")
if not os.path.exists(tmap_path):
    get("https://www.sec.gov/files/company_tickers.json", tmap_path)
tmap = json.load(open(tmap_path))
cik_of = {}
for row in tmap.values():
    cik_of.setdefault(row["ticker"].upper(), int(row["cik_str"]))

def et(iso_utc):
    # acceptanceDateTime is naive ET already per SEC docs? No - it is ET (EDT/EST).
    # SEC publishes acceptanceDateTime in US/Eastern. Return as-is.
    return iso_utc.replace("T", " ")[:16]

out = []
for sym in SYMS:
    cik = cik_of.get(sym)
    if cik is None:
        out.append((sym, "NO-CIK (delisted/absent from company_tickers.json)", [], [], None))
        continue
    path = os.path.join(BASE, f"sub_{sym}.json")
    try:
        raw = get(f"https://data.sec.gov/submissions/CIK{cik:010d}.json", path)
        sub = json.loads(raw)
    except Exception as e:
        out.append((sym, f"FETCH-FAIL {e}", [], [], None))
        continue
    time.sleep(0.12)
    tickers = sub.get("tickers", [])
    rec = sub["filings"]["recent"]
    forms = rec["form"]; fdates = rec["filingDate"]; items = rec.get("items", [""]*len(forms))
    acc = rec.get("acceptanceDateTime", [""]*len(forms))
    twos = []
    for i, f in enumerate(forms):
        if f.startswith("8-K") and "2.02" in (items[i] or ""):
            twos.append((fdates[i], et(acc[i]), items[i]))
    latest = [(fdates[i], forms[i]) for i in range(min(6, len(forms)))]
    # +364d off same-quarter year-ago 2.02
    pred = None
    tgt = datetime.strptime(DB_DATE[sym], "%Y-%m-%d")
    for d, a, it in twos:
        dt = datetime.strptime(d, "%Y-%m-%d")
        if 330 <= (tgt - dt).days <= 400:
            pred = (dt + timedelta(days=364)).strftime("%Y-%m-%d (%a)")
            break
    out.append((sym, f"tickers={tickers}", twos[:8], latest, pred))

for sym, status, twos, latest, pred in out:
    print(f"\n=== {sym}  DB={DB_DATE.get(sym)}  {status}")
    if pred:
        print(f"    +364d => {pred}")
    if twos:
        for d, a, it in twos:
            print(f"    2.02  {d}  furnish {a}  items={it}")
    else:
        print("    (no Item 2.02 8-K in recent window)")
    print(f"    latest filings: {', '.join(f'{d} {f}' for d, f in latest)}")
