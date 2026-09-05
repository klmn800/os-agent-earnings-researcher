"""Recheck: which of the DB-says-TODAY symbols have actually filed an Item 2.02
this morning, and pull EDGAR's true-ET `Accepted` for each (serially, to avoid
the rate-limit HTTPErrors the parallel sweep hit).

TECH (06:30 ET) and TRMB (07:0x ET) are the money question: both are clockwork
bmo filers with a DB date of today, so an absent 8-K after ~07:30 ET is real
evidence the date is wrong -- not a gap in coverage.
"""
import gzip, json, re, time, urllib.request
from datetime import datetime

UA = "options-scanner-earnings-researcher klmn800alerts@gmail.com"
ROOT = "E:/options_scanner/agents/earnings_researcher"

SYMS = ["TECH", "TRMB", "ALB", "ALL", "APA", "APP", "BAM", "BWA", "CDW",
        "CF", "CHRD", "COR", "CRL"]
ACCEPTED_RE = re.compile(r'Accepted</div>\s*<div class="info">([^<]+)</div>')


def get(url):
    req = urllib.request.Request(
        url, headers={"User-Agent": UA, "Accept-Encoding": "gzip, deflate"})
    with urllib.request.urlopen(req, timeout=30) as r:
        data, enc = r.read(), r.headers.get("Content-Encoding")
    return gzip.decompress(data) if enc == "gzip" else data


def true_et(cik, accession):
    nod = accession.replace("-", "")
    url = (f"https://www.sec.gov/Archives/edgar/data/{cik}/{nod}/"
           f"{accession}-index.htm")
    for attempt in range(3):
        try:
            html = re.sub(r"\s+", " ", get(url).decode("utf-8", "replace"))
            m = ACCEPTED_RE.search(html)
            return m.group(1).strip() if m else "no-Accepted-field"
        except Exception as e:
            time.sleep(1.5 * (attempt + 1))
            err = f"{type(e).__name__}"
    return f"idx-fail({err})"


ticker_map = {}
for row in json.load(open(f"{ROOT}/inbox/processed/company_tickers_20260731.json")).values():
    ticker_map.setdefault(row["ticker"], row["cik_str"])

print(f"local clock now: {datetime.now():%Y-%m-%d %H:%M:%S}\n")
for sym in SYMS:
    cik = ticker_map[sym]
    j = json.loads(get(f"https://data.sec.gov/submissions/CIK{cik:010d}.json"))
    rec = j["filings"]["recent"]
    hits = [i for i in range(len(rec["form"]))
            if rec["filingDate"][i] == "2026-08-05"
            and "2.02" in (rec.get("items", [""] * 99)[i] or "")]
    if hits:
        for i in hits:
            et = true_et(cik, rec["accessionNumber"][i])
            print(f"{sym:5s} FILED 2.02 TODAY  items={rec['items'][i]:22s} "
                  f"raw={rec['acceptanceDateTime'][i]}  true-ET={et}")
    else:
        # what *did* it file today, if anything?
        today = [f"{rec['form'][i]}" for i in range(len(rec["form"]))
                 if rec["filingDate"][i] == "2026-08-05"]
        print(f"{sym:5s} no Item 2.02 today.  other filings today: {today or 'none'}")
    time.sleep(0.3)
