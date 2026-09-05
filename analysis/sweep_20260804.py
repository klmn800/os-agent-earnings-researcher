"""SEC bulk sweep for the 2026-08-04 dispute batch (25 symbols).

Today's twist: 14 of the 25 have a DB date of TODAY and are mostly bmo filers,
so an Item 2.02 8-K accepted this morning is a *definitive* same-day source for
both date and time. Check `filed today` first, then fall back to cadence.

Rules carried from memory/:
  - NEVER timezone-convert acceptanceDateTime -- fetch the filing index page and
    read EDGAR's ET-rendered `Accepted` field (reference_sec_acceptance_time_timing)
  - phantom screen: periodic report with no Item 2.02 within +/-4d => no event
  - +364d weekday-aligned cadence is a corroborator ONLY (reference_cadence_364d)
"""
import gzip, json, re, urllib.request
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime, timedelta

UA = "options-scanner-earnings-researcher klmn800alerts@gmail.com"
ROOT = "E:/options_scanner/agents/earnings_researcher"
TODAY = datetime(2026, 8, 4)

DB_DATE = {
    # -- disputes --
    "TECH": "2026-08-05", "FLO": "2026-08-14", "PANW": "2026-08-18",
    "WDAY": "2026-08-20", "NXE": "2026-08-05", "XPEV": "2026-08-18",
    "NCNO": "2026-08-25", "NNE": "2026-08-12", "SQM": "2026-08-18",
    "OKTA": "2026-08-25", "PVH": "2026-08-25",
    # -- unconfirmed, DB says TODAY --
    "APTV": "2026-08-04", "BP": "2026-08-04", "BR": "2026-08-04",
    "BRBR": "2026-08-04", "BRKR": "2026-08-04", "CAT": "2026-08-04",
    "CCEP": "2026-08-04", "CG": "2026-08-04", "CMI": "2026-08-04",
    "DOC": "2026-08-04", "DUK": "2026-08-04", "DVA": "2026-08-04",
    "DVN": "2026-08-04", "EA": "2026-08-04",
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
        return f"idx-fail({type(e).__name__})"
    m = ACCEPTED_RE.search(html)
    return m.group(1).strip() if m else "no-Accepted-field"


ticker_map = {}
src = f"{ROOT}/inbox/processed/company_tickers_20260731.json"
for row in json.load(open(src)).values():
    ticker_map.setdefault(row["ticker"], row["cik_str"])


def work(sym):
    out = []
    p = out.append
    cik = ticker_map.get(sym)
    db = DB_DATE[sym]
    p("=" * 78)
    if not cik:
        p(f"{sym}: NO CIK in SEC ticker map => renamed or delisted. DB {db}")
        return "\n".join(out)
    try:
        j = json.loads(get(f"https://data.sec.gov/submissions/CIK{cik:010d}.json"))
    except Exception as e:
        p(f"{sym}: CIK {cik} fetch failed: {e}")
        return "\n".join(out)
    rec = j["filings"]["recent"]
    forms, dates = rec["form"], rec["filingDate"]
    accs, accno = rec["acceptanceDateTime"], rec["accessionNumber"]
    items = rec.get("items", [""] * len(forms))
    tickers = j.get("tickers", [])
    p(f"{sym} ({j.get('name')}) CIK {cik} | DB {db} | FYE {j.get('fiscalYearEnd')} "
      f"| tickers={tickers}")
    if not tickers:
        p("  !! tickers=[] => DELISTED. Do not confirm a date.")

    # 1. anything filed in the last 2 days -- the same-day 2.02 is the money shot
    for i in range(len(forms)):
        d = datetime.strptime(dates[i], "%Y-%m-%d")
        if (TODAY - d).days <= 2 and (TODAY - d).days >= 0:
            tag = f"items={items[i]}" if items[i] else ""
            p(f"  RECENT: {dates[i]} {forms[i]:8s} {tag} raw={accs[i]}")
            if "2.02" in (items[i] or ""):
                p(f"    *** ITEM 2.02 *** true-ET Accepted: "
                  f"{true_et(cik, accno[i])}  acc={accno[i]}")

    # 2. Item 2.02 history -- timing regime + cadence anchor
    hist = [(dates[i], accs[i], accno[i]) for i in range(len(forms))
            if "2.02" in (items[i] or "")]
    p(f"  Item 2.02 count (recent block): {len(hist)}")
    if not hist:
        p("  !! NO Item 2.02 EVER in recent block -- SEC timing technique is blind")
    for d, a, ac in hist[:8]:
        p(f"    2.02 {d}  raw={a}  ET={true_et(cik, ac)}")

    # 3. +364d weekday-aligned cadence (CORROBORATOR ONLY)
    tgt = datetime.strptime(db, "%Y-%m-%d")
    yr_ago = [d for d, _, _ in hist
              if 320 <= (tgt - datetime.strptime(d, "%Y-%m-%d")).days <= 410]
    for d in yr_ago:
        pred = datetime.strptime(d, "%Y-%m-%d") + timedelta(days=364)
        delta = (pred - tgt).days
        p(f"  +364d from {d} ({datetime.strptime(d,'%Y-%m-%d'):%a}) => "
          f"{pred:%Y-%m-%d %a}  vs DB {db} ({tgt:%a})  delta={delta:+d}d")

    # 4. phantom screen: periodic report with no 2.02 nearby
    twod = {d for d, _, _ in hist}
    for i in range(len(forms)):
        if forms[i] in ("10-Q", "10-K", "20-F") and dates[i] >= "2025-09-01":
            d = datetime.strptime(dates[i], "%Y-%m-%d")
            near = any(abs((d - datetime.strptime(x, "%Y-%m-%d")).days) <= 4
                       for x in twod)
            if not near:
                p(f"  !! PHANTOM FLAG: {forms[i]} {dates[i]} with no Item 2.02 "
                  f"within +/-4d")
    return "\n".join(out)


with ThreadPoolExecutor(max_workers=6) as ex:
    for chunk in ex.map(work, list(DB_DATE)):
        print(chunk)
