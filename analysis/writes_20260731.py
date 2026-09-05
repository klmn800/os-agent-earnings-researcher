"""IR-URL cache + dispute-resolution writes for the 2026-07-31 session."""
import subprocess

DQ = "python E:/options_scanner/tools/direct_db_query.py"
LAKE = "E:/options_scanner/data/datalake.db"
PERF = "E:/options_scanner/data/performance.db"
TODAY = "2026-07-31"
NOW = "2026-07-31 08:05:00"

# symbol -> company-domain URL that actually carried the answer (never a wire URL)
IR = {
    "ABBV": "https://investors.abbvie.com/news-releases/news-release-details/abbvie-host-second-quarter-2026-earnings-conference-call",
    "BEN":  "https://investors.franklinresources.com/news-center/press-releases/press-release-details/2026/Franklin-Resources-Inc--to-Announce-Third-Quarter-Results-on-July-31-2026/default.aspx",
    "CBOE": "https://ir.cboe.com/news/news-details/2026/Cboe-Global-Markets-Announces-Date-of-Second-Quarter-2026-Earnings-Release-and-Conference-Call/default.aspx",
    "CELH": "https://ir.celsiusholdingsinc.com/news/news-details/2026/Celsius-Holdings-to-Release-Second-Quarter-Results-on-Thursday-Aug--6-2026/default.aspx",
    "RDW":  "https://ir.rdw.com/news-events/press-releases",
    "AAP":  "https://ir.advanceautoparts.com/investors/financials/quarterly-results/default.aspx",
    "JD":   "https://ir.jd.com/news-releases",
    "BIDU": "https://ir.baidu.com/press-releases",
    "BJ":   "https://newsroom.bjs.com/press-releases/news-details/2026/BJs-Wholesale-Club-Announces-Second-Quarter-Fiscal-2026-Earnings-Conference-Call-Date/default.aspx",
    "DNN":  "https://denisonmines.com/investors/financial-calendar-events/",
    "YPF":  "https://investors.ypf.com",
    "TECH": "https://investors.bio-techne.com/press-releases",
    "CSCO": "https://investor.cisco.com/financial-information/financial-results/default.aspx",
    "SE":   "https://www.sea.com/investor/quarterlyresults",
    "NU":   "https://international.nubank.com.br/investors/",
    "XP":   "https://investors.xpinc.com/en/",
}

# dispute rows resolved this session: symbol -> (date, time, url)
RESOLVED = {
    "RDW":  ("2026-08-05", "amc", IR["RDW"]),
    "CELH": ("2026-08-06", "bmo", IR["CELH"]),
    "CSCO": ("2026-08-12", "amc", IR["CSCO"]),
    "AAP":  ("2026-08-20", "bmo", IR["AAP"]),
    "TOL":  ("2026-08-18", "amc", "https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0000794170&type=8-K"),
    "BIDU": ("2026-08-18", "bmo", IR["BIDU"]),
    "JD":   ("2026-08-13", "bmo", IR["JD"]),
    "YPF":  ("2026-08-10", "amc", IR["YPF"]),
    "DNN":  ("2026-08-11", "amc", IR["DNN"]),
    "SE":   ("2026-08-11", "bmo", IR["SE"]),
    "NU":   ("2026-08-13", "amc", IR["NU"]),
    "XP":   ("2026-08-17", "amc", IR["XP"]),
    "BJ":   ("2026-08-21", "bmo", IR["BJ"]),
}


def run(db, sql):
    r = subprocess.run(f'{DQ} --db {db} --write --sql "{sql}"',
                       shell=True, capture_output=True, text=True)
    return (r.stdout + r.stderr).strip().splitlines()[-1:] or [""]


print("== IR URLs ==")
for sym, url in IR.items():
    sql = (f"UPDATE symbol_metadata SET ir_earnings_url='{url}', "
           f"ir_url_last_verified='{TODAY}' WHERE symbol='{sym}'")
    print(f"  {sym:5} {run(LAKE, sql)[0]}")

print("== dispute resolutions ==")
for sym, (d, t, url) in RESOLVED.items():
    sql = (f"UPDATE earnings_date_disputes SET resolution='confirmed_agent', "
           f"resolved_date='{d}', resolved_time='{t}', resolved_at='{NOW}', "
           f"research_url='{url}' WHERE trade_date='{TODAY}' AND symbol='{sym}'")
    print(f"  {sym:5} {run(PERF, sql)[0]}")
