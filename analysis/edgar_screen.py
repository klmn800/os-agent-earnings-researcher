"""EDGAR filing-date screen of unconfirmed earnings_upcoming rows (Sunday skip calibration).

For each unconfirmed row in [start, end], find the Item 2.02 8-K nearest the stored date
(filed within -21d .. +21d), read the ET "Accepted" time from the filing index page (never
convert the submissions-JSON time: it mixes UTC and ET), and classify the release session.

Coarse by design: next-morning 8-K filers (UGI, RRC) fake a bmo; evening-before filers
(after 17:30 ET -> next-day filingDate, PCG/DHR) are read as next-day bmo. Flags are for
reading, not verdicts.

Usage: python analysis/edgar_screen.py 2026-11-02 2026-11-06 > inbox/fetch/screen.tsv
"""
import json, re, sqlite3, sys, time, urllib.request
from datetime import date, datetime, timedelta

UA = "options-scanner-earnings-researcher klmn800alerts@gmail.com"
DB = "E:/options_scanner/data/datalake.db"


def get(u):
    for i in range(3):
        try:
            return urllib.request.urlopen(urllib.request.Request(u, headers={"User-Agent": UA}), timeout=30).read()
        except Exception as e:  # noqa: BLE001
            err = e
            time.sleep(2 + 3 * i)
    raise err


def session_of(acc):
    """acc: datetime ET of acceptance -> (release_date, session)."""
    t = acc.hour * 60 + acc.minute
    if t < 9 * 60 + 30:
        return acc.date(), "bmo"
    if t >= 17 * 60 + 30:  # evening filing: carries next-day filingDate, release is next morning
        return acc.date() + timedelta(days=1), "bmo(eve-8K)"
    if t >= 16 * 60:
        return acc.date(), "amc"
    return acc.date(), "intraday"


def main(start, end):
    con = sqlite3.connect(DB)
    rows = con.execute(
        "SELECT symbol, earnings_date, earnings_time FROM earnings_upcoming "
        "WHERE date_confirmed=0 AND earnings_date BETWEEN ? AND ? ORDER BY earnings_date, symbol",
        (start, end)).fetchall()
    tk = json.loads(get("https://www.sec.gov/files/company_tickers.json"))
    cik = {v["ticker"]: v["cik_str"] for v in tk.values()}
    print("symbol\tdb_date\tdb_time\tedgar_accepted_et\trel_date\trel_session\tdate_delta\tflag")
    for sym, d, tm in rows:
        c = cik.get(sym.replace(".", "-")) or cik.get(sym)
        if not c:
            print(f"{sym}\t{d}\t{tm}\t\t\t\t\tno_cik")
            continue
        sub = json.loads(get(f"https://data.sec.gov/submissions/CIK{c:010d}.json"))["filings"]["recent"]
        dbd = date.fromisoformat(d)
        best = None
        for i, f in enumerate(sub["form"]):
            if f not in ("8-K", "8-K/A") or "2.02" not in (sub["items"][i] or ""):
                continue
            fd = date.fromisoformat(sub["filingDate"][i])
            if abs((fd - dbd).days) <= 21 and (best is None or abs((fd - dbd).days) < abs((best[0] - dbd).days)):
                best = (fd, sub["accessionNumber"][i])
        time.sleep(0.12)
        if not best:
            kinds = {f for f, fd in zip(sub["form"], sub["filingDate"]) if fd >= start}
            print(f"{sym}\t{d}\t{tm}\t\t\t\t\tno_2.02 ({','.join(sorted(kinds)) or 'nothing filed'})")
            continue
        a = best[1]
        ix = get(f"https://www.sec.gov/Archives/edgar/data/{c}/{a.replace('-', '')}/{a}-index.htm").decode("utf-8", "ignore")
        m = re.search(r'Accepted</div>\s*<div class="info">([^<]+)', ix)
        time.sleep(0.12)
        if not m:
            print(f"{sym}\t{d}\t{tm}\t\t\t\t\tno_accept_time {a}")
            continue
        acc = datetime.strptime(m.group(1).strip(), "%Y-%m-%d %H:%M:%S")
        rd, ses = session_of(acc)
        delta = (rd - dbd).days
        flag = []
        if delta:
            flag.append(f"DATE{delta:+d}")
        s0 = ses.split("(")[0]
        if tm in ("bmo", "amc") and s0 in ("bmo", "amc") and s0 != tm:
            flag.append("SESSION")
        if tm not in ("bmo", "amc"):
            flag.append("db_time_unknown")
        print(f"{sym}\t{d}\t{tm}\t{acc:%Y-%m-%d %H:%M}\t{rd}\t{ses}\t{delta:+d}\t{' '.join(flag) or 'ok'}")
        sys.stdout.flush()


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])
