"""Apply the 2026-08-06 confirmations: earnings_confirm + ir_earnings_url + dispute resolution.

Gotchas honoured (see memory/):
  - direct_db_query.py needs --write or it silently rolls back
  - --db must use FORWARD SLASHES (a backslash path silently creates a stray DB)
  - --sql is split on ';' even inside string literals -> no semicolons in values
  - only company-owned domains go in ir_earnings_url, never wire URLs
  - the 7 'unconfirmed' rows have NO dispute row -> skip the disputes UPDATE
"""
import subprocess, sys

PY = sys.executable
TOOLS = "E:/options_scanner/tools"
DATALAKE = "E:/options_scanner/data/datalake.db"
PERF = "E:/options_scanner/data/performance.db"
TODAY = "2026-08-06"
NOW = "2026-08-06 08:20:00"

# (symbol, date, time, company IR url, has_dispute_row)
ROWS = [
    # ---- date_disagreement / both: company advance PR found today ----
    ("FLO",  "2026-08-20", "amc", "https://investors.flowersfoods.com/news/news-releases/2026/08-05-2026-141848491", True),
    ("SJM",  "2026-08-26", "bmo", "https://investors.jmsmucker.com/news/news-details/2026/The-J-M--Smucker-Co--to-Report-First-Quarter-Earnings-and-Participate-in-the-2026-Barclays-Global-Consumer-Staples-Conference/default.aspx", True),
    ("WOLF", "2026-08-19", "amc", "https://investor.wolfspeed.com/news/news-details/2026/Wolfspeed-Inc--Announces-Date-of-Fiscal-Fourth-Quarter-Earnings-Call-for-August-19-2026/default.aspx", True),
    ("P",    "2026-08-26", "amc", "https://investor.everpuredata.com/news-and-events/press-releases/press-release-details/2026/Everpure-Announces-Date-and-Conference-Call-Information-for-Second-Quarter-Fiscal-2027-Financial-Results/default.aspx", True),
    # ---- unknown_time: resolved from company PRs ----
    ("NNE",  "2026-08-12", "amc", "https://ir.nanonuclearenergy.com/news-releases/news-release-details/nano-nuclear-hold-third-quarter-business-update-webcast-august", True),
    ("ADSK", "2026-08-27", "amc", "https://investors.autodesk.com/news-releases/news-release-details/autodesk-extends-invitation-join-financial-results-conference-52", True),
    ("GAP",  "2026-08-27", "amc", "https://investors.gapinc.com/press-releases/news-details/2026/Gap-Inc--to-Report-Second-Quarter-Fiscal-2026-Results-on-August-27/default.aspx", True),
    ("MRVL", "2026-08-27", "amc", "https://investor.marvell.com/news-events/press-releases/detail/1029/marvell-technology-inc-announces-conference-call-to-review-second-quarter-of-fiscal-year-2027-financial-results-announces-investor-day-on-october-6-2026", True),
    ("DG",   "2026-08-27", "bmo", "https://investor.dollargeneral.com", True),
    # ---- unknown_time: time from the company's own prior-quarter wording ----
    ("BBWI", "2026-08-27", "bmo", "https://investors.bbwinc.com/news-releases", True),
    ("S",    "2026-08-27", "amc", "https://investors.sentinelone.com/press-releases", True),
    # ---- unknown_time: time from SEC Item 2.02 furnish regime (8/8 quarters) ----
    ("BBY",  "2026-08-27", "bmo", "https://investors.bestbuy.com/News--Events/events-and-presentations/default.aspx", True),
    ("ULTA", "2026-08-27", "amc", "https://www.ulta.com/investor/news-events/press-releases", True),
    # ---- unconfirmed calendar rows reporting TODAY (no dispute row) ----
    ("ABNB", "2026-08-06", "amc", "https://investors.airbnb.com/press-releases/news-details/2026/Airbnb-to-Announce-Second-Quarter-2026-Results/default.aspx", False),
    ("AFL",  "2026-08-06", "amc", "https://investors.aflac.com/press-releases/press-release-details/2026/Aflac-Incorporated-to-Release-Second-Quarter-Results-and-CFO-Video-Update-on-August-6-2026-and-Host-Webcast-on-August-7-2026/default.aspx", False),
    ("AIG",  "2026-08-06", "amc", "https://aig.gcs-web.com/news-releases", False),
    ("AKAM", "2026-08-06", "amc", "https://www.ir.akamai.com/news-releases/news-release-details/akamai-technologies-hold-second-quarter-2026-investor-conference", False),
    ("ATI",  "2026-08-06", "bmo", "https://ir.atimaterials.com/news-events/news-details/2026/ATI-Announces-Webcast-for-Second-Quarter-2026-Results/default.aspx", False),
    ("BMRN", "2026-08-06", "amc", "https://investors.biomarin.com/news/news-details/2026/BioMarin-to-Host-Second-Quarter-2026-Financial-Results-Conference-Call-and-Webcast-on-Thursday-August-6-2026-at-430pm-ET/default.aspx", False),
    ("CART", "2026-08-06", "amc", "https://investors.instacart.com/news-releases/news-release-details/instacart-report-second-quarter-2026-financial-results-august-6", False),
]

for sym, date, tm, url in [(r[0], r[1], r[2], r[3]) for r in ROWS]:
    assert ";" not in url, f"{sym}: semicolon in URL would break --sql splitting"


def run(label, cmd):
    p = subprocess.run(cmd, capture_output=True, text=True)
    tail = (p.stdout or p.stderr).strip().splitlines()
    print(f"  {label}: rc={p.returncode} | {tail[-1][:110] if tail else ''}")
    return p.returncode


for sym, date, tm, url, has_dispute in ROWS:
    print(f"=== {sym}  {date} {tm}")
    run("confirm ", [PY, f"{TOOLS}/earnings_confirm.py", "--symbol", sym,
                     "--date", date, "--time", tm, "--by", "agent"])
    run("ir_url  ", [PY, f"{TOOLS}/direct_db_query.py", "--db", DATALAKE, "--write",
                     "--sql", f"UPDATE symbol_metadata SET ir_earnings_url='{url}', "
                              f"ir_url_last_verified='{TODAY}' WHERE symbol='{sym}'"])
    if has_dispute:
        run("dispute ", [PY, f"{TOOLS}/direct_db_query.py", "--db", PERF, "--write",
                         "--sql", f"UPDATE earnings_date_disputes SET resolution='confirmed_agent', "
                                  f"resolved_date='{date}', resolved_time='{tm}', "
                                  f"resolved_at='{NOW}', research_url='{url}' "
                                  f"WHERE trade_date='{TODAY}' AND symbol='{sym}'"])
    else:
        print("  dispute : skipped (no dispute row)")
