"""SEC bulk sweep for the 2026-08-03 dispute batch (25 symbols).

Differences from sweep_20260731.py:
  - NEVER timezone-converts acceptanceDateTime (the `Z` is a lie for a subset of
    filings -- see memory/reference_sec_acceptance_time_timing.md). Prints the raw
    field AND fetches the filing index page for EDGAR's ET-rendered `Accepted`.
  - Adds the phantom-earnings screen: periodic reports (10-K/10-Q/20-F) with no
    Item 2.02 within +/-4 days => results-without-an-event.
"""
import gzip, json, re, time, urllib.request
from datetime import datetime, timedelta

UA = "options-scanner-earnings-researcher klmn800alerts@gmail.com"
ROOT = "E:/options_scanner/agents/earnings_researcher"
TODAY = datetime(2026, 8, 3)
IDX_LOOKBACK = 5  # how many recent 2.02 filings to resolve to true ET

DB_DATE = {
    # disputes
    "TECH": "2026-08-05", "FLO": "2026-08-14", "PANW": "2026-08-18",
    "NXE": "2026-08-05", "XPEV": "2026-08-18", "NNE": "2026-08-12",
    "SQM": "2026-08-18", "WDS": "2026-08-24",
    # unconfirmed, reporting today
    "AES": "2026-08-03", "ARE": "2026-08-03", "BWXT": "2026-08-03",
    "CLX": "2026-08-03", "CNH": "2026-08-03", "FANG": "2026-08-03",
    "INSP": "2026-08-03", "MAR": "2026-08-03", "OKE": "2026-08-03",
    "ON": "2026-08-03", "TSN": "2026-08-03",
    # unconfirmed, reporting tomorrow
    "ADM": "2026-08-04", "AMD": "2026-08-04", "AME": "2026-08-04",
    "AMGN": "2026-08-04", "ANET": "2026-08-04", "APO": "2026-08-04",
}

ACCEPTED_RE = re.compile(r'Accepted</div>\s*<div class="info">([^<]+)</div>')


def get(url):
    req = urllib.request.Request(
        url, headers={"User-Agent": UA, "Accept-Encoding": "gzip, deflate"})
    with urllib.request.urlopen(req, timeout=30) as r:
        data = r.read()
        enc = r.headers.get("Content-Encoding")
    if enc == "gzip":
        data = gzip.decompress(data)
    return data


def true_et(cik, accession):
    """EDGAR always renders `Accepted` on the filing index in ET."""
    nod = accession.replace("-", "")
    url = (f"https://www.sec.gov/Archives/edgar/data/{cik}/{nod}/"
           f"{accession}-index.htm")
    try:
        html = re.sub(r"\s+", " ", get(url).decode("utf-8", "replace"))
    except Exception as e:
        return f"idx-fail({e})"
    m = ACCEPTED_RE.search(html)
    return m.group(1).strip() if m else "no-Accepted-field"


ticker_map = {}
src = f"{ROOT}/inbox/processed/company_tickers_20260731.json"
for row in json.load(open(src)).values():
    ticker_map.setdefault(row["ticker"], row["cik_str"])

for sym in DB_DATE:
    cik = ticker_map.get(sym)
    db = DB_DATE[sym]
    print("=" * 78)
    if not cik:
        print(f"{sym}: NO CIK in SEC ticker map => renamed or delisted. DB {db}")
        continue
    try:
        j = json.loads(get(f"https://data.sec.gov/submissions/CIK{cik:010d}.json"))
    except Exception as e:
        print(f"{sym}: CIK {cik} fetch failed: {e}")
        continue
    rec = j["filings"]["recent"]
    forms = rec["form"]; dates = rec["filingDate"]
    accs = rec["acceptanceDateTime"]; items = rec.get("items", [])
    accno = rec["accessionNumber"]
    tickers = j.get("tickers", [])
    print(f"{sym} ({j.get('name')}) CIK {cik} | DB {db} | FYE {j.get('fiscalYearEnd')} "
          f"| tickers={tickers}")
    if not tickers:
        print("  !! tickers=[] => DELISTED. Do not confirm a date.")

    recent = [(dates[i], forms[i]) for i in range(len(forms))
              if (TODAY - datetime.strptime(dates[i], "%Y-%m-%d")).days <= 5]
    if recent:
        print(f"  last-5-days filings: {recent[:10]}")

    hits = []
    for i, f in enumerate(forms):
        it = items[i] if i < len(items) else ""
        if f.startswith("8-K") and "2.02" in (it or ""):
            hits.append((dates[i], accs[i], it, accno[i]))

    if hits:
        print("  Item 2.02 8-Ks (filingDate | raw acceptanceDateTime | true ET | items):")
        for n, (d, raw, it, an) in enumerate(hits[:10]):
            et = true_et(cik, an) if n < IDX_LOOKBACK else "-"
            print(f"    {d} | {raw} | {et} | {it}")
            time.sleep(0.12)
        tgt = datetime.strptime(db, "%Y-%m-%d")
        best = None
        for d, _, _, _ in hits:
            dd = datetime.strptime(d, "%Y-%m-%d")
            if 330 < (tgt - dd).days < 400:
                best = dd
                break
        if best:
            pred = best + timedelta(days=364)
            print(f"  +364d from {best:%Y-%m-%d} => {pred:%Y-%m-%d} ({pred:%a}) "
                  f"| DB {db} delta {(tgt - pred).days}d")
    else:
        sixk = [dates[i] for i, f in enumerate(forms) if f.startswith("6-K")][:8]
        print(f"  no Item 2.02 8-K at all. recent 6-Ks: {sixk}")

    # phantom screen: periodic report with no 2.02 within +/-4 days
    twotwo = [datetime.strptime(d, "%Y-%m-%d") for d, _, _, _ in hits]
    periodic = [(dates[i], forms[i]) for i, f in enumerate(forms)
                if f in ("10-K", "10-Q", "20-F", "40-F")][:4]
    if periodic:
        flags = []
        for d, f in periodic:
            dd = datetime.strptime(d, "%Y-%m-%d")
            near = any(abs((dd - t).days) <= 4 for t in twotwo)
            flags.append(f"{d} {f} {'2.02-ok' if near else '** NO 2.02 **'}")
        print("  periodic reports: " + " | ".join(flags))
    time.sleep(0.12)
