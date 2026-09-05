"""SEC bulk sweep for the 2026-08-05 dispute batch (25 symbols).

11 of the 25 have a DB date of TODAY (the unconfirmed block) -- for those an
Item 2.02 8-K accepted this morning is a definitive same-day source for both
date and time. TECH + TRMB are also dated today and are ~06:30/07:0x bmo
filers, so if they really report today the 8-K already exists at 07:16 ET.

Rules carried from memory/:
  - NEVER timezone-convert acceptanceDateTime -- fetch the filing index page and
    read EDGAR's ET-rendered `Accepted` field (reference_sec_acceptance_time_timing)
  - phantom screen: periodic report with no Item 2.02 within +/-4d => no event
  - +364d weekday-aligned cadence is a corroborator ONLY (reference_cadence_364d)
  - 6-K filers have no `items`; screen primaryDocDescription instead
"""
import gzip, json, re, urllib.request
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime, timedelta

UA = "options-scanner-earnings-researcher klmn800alerts@gmail.com"
ROOT = "E:/options_scanner/agents/earnings_researcher"
TODAY = datetime(2026, 8, 5)

DB_DATE = {
    # -- disputes: date_disagreement / both --
    "TECH": "2026-08-05", "TRMB": "2026-08-05", "FLO": "2026-08-14",
    "NCNO": "2026-08-25", "HPQ": "2026-08-26", "NTNX": "2026-08-26",
    "SNOW": "2026-08-26", "MDB": "2026-08-26", "P": "2026-08-26",
    # -- disputes: unknown_time --
    "NNE": "2026-08-12", "SQM": "2026-08-18", "FIVE": "2026-08-26",
    "KSS": "2026-08-26", "SNPS": "2026-08-26",
    # -- unconfirmed, DB says TODAY --
    "ALB": "2026-08-05", "ALL": "2026-08-05", "APA": "2026-08-05",
    "APP": "2026-08-05", "BAM": "2026-08-05", "BWA": "2026-08-05",
    "CDW": "2026-08-05", "CF": "2026-08-05", "CHRD": "2026-08-05",
    "COR": "2026-08-05", "CRL": "2026-08-05",
}

SIXK_RE = re.compile(r"results|earnings|interim|half.?year|\bSEA\b|[1-4]Q\d\d|\bQ[1-4]\b",
                     re.I)
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
    pdd = rec.get("primaryDocDescription", [""] * len(forms))
    tickers = j.get("tickers", [])
    p(f"{sym} ({j.get('name')}) CIK {cik} | DB {db} | FYE {j.get('fiscalYearEnd')} "
      f"| tickers={tickers}")
    if not tickers:
        p("  !! tickers=[] => DELISTED. Do not confirm a date.")

    # 1. anything filed in the last 2 days -- the same-day 2.02 is the money shot
    for i in range(len(forms)):
        d = datetime.strptime(dates[i], "%Y-%m-%d")
        if 0 <= (TODAY - d).days <= 2:
            tag = f"items={items[i]}" if items[i] else f"desc={pdd[i]!r}"
            p(f"  RECENT: {dates[i]} {forms[i]:8s} {tag} raw={accs[i]}")
            if "2.02" in (items[i] or "") or (
                    forms[i] == "6-K" and SIXK_RE.search(pdd[i] or "")):
                p(f"    *** RESULTS FILING *** true-ET Accepted: "
                  f"{true_et(cik, accno[i])}  acc={accno[i]}")

    # 2. results-filing history -- timing regime + cadence anchor
    hist = [(dates[i], accs[i], accno[i], items[i] or pdd[i])
            for i in range(len(forms))
            if "2.02" in (items[i] or "")
            or (forms[i] == "6-K" and SIXK_RE.search(pdd[i] or ""))]
    p(f"  results-filing count (recent block): {len(hist)}")
    if not hist:
        p("  !! NO Item 2.02 EVER in recent block -- SEC timing technique is blind")
    for d, a, ac, lbl in hist[:8]:
        p(f"    {d}  raw={a}  ET={true_et(cik, ac)}  [{lbl}]")

    # 3. +364d weekday-aligned cadence (CORROBORATOR ONLY)
    tgt = datetime.strptime(db, "%Y-%m-%d")
    for d, _, _, _ in hist:
        if 320 <= (tgt - datetime.strptime(d, "%Y-%m-%d")).days <= 410:
            pred = datetime.strptime(d, "%Y-%m-%d") + timedelta(days=364)
            p(f"  +364d from {d} ({datetime.strptime(d,'%Y-%m-%d'):%a}) => "
              f"{pred:%Y-%m-%d %a}  vs DB {db} ({tgt:%a})  "
              f"delta={(pred - tgt).days:+d}d")

    # 4. phantom screen: periodic report with no 2.02 nearby
    twod = {d for d, _, _, _ in hist}
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
