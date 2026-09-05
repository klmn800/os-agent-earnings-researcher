"""SEC bulk sweep for the 2026-07-31 dispute batch.

Uses the local SEC ticker->CIK map dropped into inbox/company_tickers.json.

Per symbol:
  - CIK lookup (absent => foreign private issuer w/o ticker map entry, or delisted)
  - all recent 8-K filings carrying Item 2.02 -> filingDate + acceptanceDateTime ET
  - +364d weekday-aligned prediction off the same-quarter year-ago 2.02 filing
  - any filing made in the last 3 days (catches today's release for BMO reporters)
"""
import gzip, json, time, urllib.request
from datetime import datetime, timedelta, timezone

UA = "options-scanner-earnings-researcher klmn800alerts@gmail.com"
ROOT = "E:/options_scanner/agents/earnings_researcher"
TODAY = datetime(2026, 7, 31)

DB_DATE = {
    "RDW": "2026-08-05", "TECH": "2026-08-05", "CELH": "2026-08-10",
    "CSCO": "2026-08-12", "AAP": "2026-08-13", "FLO": "2026-08-14",
    "PANW": "2026-08-18", "TOL": "2026-08-18", "BIDU": "2026-08-19",
    "NXE": "2026-08-05", "JD": "2026-08-11", "XPEV": "2026-08-18",
    "IAC": "2026-08-03", "YPF": "2026-08-10", "DNN": "2026-08-11",
    "SE": "2026-08-11", "NNE": "2026-08-12", "NU": "2026-08-13",
    "XP": "2026-08-17", "SQM": "2026-08-18", "BJ": "2026-08-21",
    "ABBV": "2026-07-31", "BEN": "2026-07-31", "CBOE": "2026-07-31",
    "CHD": "2026-07-31",
}

ET = timezone(timedelta(hours=-4))  # EDT


def get(url):
    req = urllib.request.Request(
        url, headers={"User-Agent": UA, "Accept-Encoding": "gzip, deflate"})
    with urllib.request.urlopen(req, timeout=30) as r:
        data = r.read()
        enc = r.headers.get("Content-Encoding")
    if enc == "gzip":
        data = gzip.decompress(data)
    return data


ticker_map = {}
for row in json.load(open(f"{ROOT}/inbox/company_tickers.json")).values():
    ticker_map.setdefault(row["ticker"], row["cik_str"])

for sym in DB_DATE:
    cik = ticker_map.get(sym)
    db = DB_DATE[sym]
    print("=" * 72)
    if not cik:
        print(f"{sym}: NO CIK in SEC ticker map (foreign issuer / delisted). DB {db}")
        continue
    try:
        j = json.loads(get(f"https://data.sec.gov/submissions/CIK{cik:010d}.json"))
    except Exception as e:
        print(f"{sym}: CIK {cik} fetch failed: {e}")
        continue
    rec = j["filings"]["recent"]
    forms, dates, accs, items = (rec["form"], rec["filingDate"],
                                 rec["acceptanceDateTime"], rec.get("items", []))
    print(f"{sym} ({j.get('name')}) CIK {cik} | DB {db} | fiscalYearEnd {j.get('fiscalYearEnd')}")

    # recent filings of any form (last 5 days) -- catches a same-day release
    recent = [(dates[i], forms[i]) for i in range(len(forms))
              if (TODAY - datetime.strptime(dates[i], "%Y-%m-%d")).days <= 5]
    if recent:
        print(f"  last-5-days filings: {recent[:8]}")

    # Item 2.02 8-Ks
    hits = []
    for i, f in enumerate(forms):
        it = items[i] if i < len(items) else ""
        if f.startswith("8-K") and "2.02" in (it or ""):
            et = datetime.fromisoformat(accs[i].replace("Z", "+00:00")) \
                if accs[i].endswith("Z") else datetime.fromisoformat(accs[i])
            if et.tzinfo is None:
                et = et.replace(tzinfo=timezone.utc)
            hits.append((dates[i], et.astimezone(ET).strftime("%H:%M"), it))
    if hits:
        print("  Item 2.02 8-Ks (filingDate, ET furnish, items):")
        for h in hits[:10]:
            print("   ", h)
        # +364d off same-quarter year-ago
        tgt = datetime.strptime(db, "%Y-%m-%d")
        best = None
        for d, t, _ in hits:
            dd = datetime.strptime(d, "%Y-%m-%d")
            if 330 < (tgt - dd).days < 400:
                best = dd
                break
        if best:
            pred = best + timedelta(days=364)
            print(f"  +364d from {best:%Y-%m-%d} => {pred:%Y-%m-%d} ({pred:%a}) "
                  f"| DB {db} delta {(datetime.strptime(db,'%Y-%m-%d')-pred).days}d")
    else:
        # foreign private issuers: show recent 6-K cadence
        sixk = [dates[i] for i, f in enumerate(forms) if f.startswith("6-K")][:8]
        print(f"  no Item 2.02 8-K. recent 6-Ks: {sixk}")
    time.sleep(0.12)
