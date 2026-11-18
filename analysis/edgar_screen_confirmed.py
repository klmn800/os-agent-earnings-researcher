"""EDGAR filing-date screen of CONFIRMED ledger rows (closes an audit census mechanically).
Reads rows from analysis/audit_pool_20261115.json ('pool' minus 'draw'), same classification as edgar_screen.py.
Usage: python analysis/edgar_screen_confirmed.py > analysis/edgar_screen_confirmed_20261115.tsv"""
import json, re, sys, time
from datetime import date, datetime
sys.path.insert(0, "analysis")
from edgar_screen import get, session_of
d = json.load(open("analysis/audit_pool_20261115.json"))
drawn = {r["sym"] for r in d["draw"]}
rows = [r for r in d["pool"] if r["sym"] not in drawn]
tk = json.loads(get("https://www.sec.gov/files/company_tickers.json"))
cik = {v["ticker"]: v["cik_str"] for v in tk.values()}
print("symbol\tstratum\tledger_date\tledger_time\tform\tedgar_accepted_et\trel_date\trel_session\tdate_delta\tflag")
for r in sorted(rows, key=lambda r: (r["date"], r["sym"])):
    sym, dd, tm = r["sym"], r["date"], r["time"]
    c = cik.get(sym.replace(".", "-")) or cik.get(sym)
    if not c:
        print(f"{sym}\t{r['stratum']}\t{dd}\t{tm}\t\t\t\t\t\tno_cik"); continue
    sub = json.loads(get(f"https://data.sec.gov/submissions/CIK{c:010d}.json"))["filings"]["recent"]
    dbd = date.fromisoformat(dd); best = None
    for i, f in enumerate(sub["form"]):
        is202 = f in ("8-K", "8-K/A") and "2.02" in (sub["items"][i] or "")
        if not (is202 or f == "6-K"): continue
        fd = date.fromisoformat(sub["filingDate"][i])
        if -3 <= (fd - dbd).days <= 10 and (best is None or abs((fd - dbd).days) < abs((best[0] - dbd).days) or (best[2] == "6-K" and is202)):
            best = (fd, sub["accessionNumber"][i], f)
    time.sleep(0.12)
    if not best:
        print(f"{sym}\t{r['stratum']}\t{dd}\t{tm}\t\t\t\t\t\tno_2.02"); continue
    a = best[1]
    ix = get(f"https://www.sec.gov/Archives/edgar/data/{c}/{a.replace('-', '')}/{a}-index.htm").decode("utf-8", "ignore")
    m = re.search(r'Accepted</div>\s*<div class="info">([^<]+)', ix); time.sleep(0.12)
    if not m:
        print(f"{sym}\t{r['stratum']}\t{dd}\t{tm}\t{best[2]}\t\t\t\t\tno_accept {a}"); continue
    acc = datetime.strptime(m.group(1).strip(), "%Y-%m-%d %H:%M:%S")
    rd, ses = session_of(acc); delta = (rd - dbd).days; flag = []
    if delta: flag.append(f"DATE{delta:+d}")
    s0 = ses.split("(")[0]
    if s0 in ("bmo", "amc") and s0 != tm: flag.append("SESSION")
    if s0 == "intraday": flag.append("intraday_filing")
    if best[2] == "6-K": flag.append("6K_late_filer_possible")
    print(f"{sym}\t{r['stratum']}\t{dd}\t{tm}\t{best[2]}\t{acc:%Y-%m-%d %H:%M}\t{rd}\t{ses}\t{delta:+d}\t{' '.join(flag) or 'ok'}  {a}")
    sys.stdout.flush()
