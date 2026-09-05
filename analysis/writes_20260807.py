"""IR-URL + dispute-resolution writes for 2026-08-07.
subprocess arg list (never a shell string); no ';' inside literals; --write.
Verified with a follow-up SELECT -- exit code proves nothing."""
import subprocess, sys
sys.stdout.reconfigure(encoding="utf-8")
Q = "E:/options_scanner/tools/direct_db_query.py"
DL = "E:/options_scanner/data/datalake.db"
PF = "E:/options_scanner/data/performance.db"
TODAY, NOW = "2026-08-07", "2026-08-07 08:05:00"

IR = {
 "FLR":  "https://investor.fluor.com/news/news-details/2026/Fluor-Reports-Second-Quarter-2026-Results/default.aspx",
 "LEGN": "https://investors.legendbiotech.com/news-releases/news-release-details/legend-biotech-host-investor-conference-call-second-quarter-2026",
 "COHR": "https://ir.coherent.com/news-releases/news-release-details/coherent-corp-announces-timing-fy2026-fourth-quarter-and-fiscal",
 "AMAT": "https://ir.appliedmaterials.com/news-releases/news-release-details/applied-materials-report-fiscal-third-quarter-2026-results-aug",
 "JKHY": "https://ir.jackhenry.com/news-releases/news-release-details/jack-henry-associates-provide-webcast-fourth-quarter-and-full",
 "KEYS": "https://investor.keysight.com/investor-news-and-events/financial-press-releases/press-release-details/2026/Keysight-Technologies-to-Report-Fiscal-Third-Quarter-Results-on-August-18-2026/default.aspx",
 "ADI":  "https://investor.analog.com/news-releases/news-release-details/analog-devices-report-third-quarter-fiscal-year-2026-financial",
 "BILL": "https://investor.bill.com/news/news-details/2026/BILL-to-Report-Fiscal-Fourth-Quarter-and-Fiscal-2026-Financial-Results/default.aspx",
 "EL":   "https://investors.elcompanies.com/en/news-and-media/newsroom/press-releases/2026/08-05-2026-213516937",
 "HPQ":  "https://investor.hp.com/news-events/news/news-details/2026/HP-Inc--to-Announce-Third-Quarter-Fiscal-2026-Earnings-on-August-26-2026-and-to-Attend-Upcoming-Investor-Conferences/default.aspx",
 "NTNX": "https://ir.nutanix.com/news-releases/news-release-details/nutanix-announces-date-and-conference-call-information-fiscal-6",
 "MKTX": "https://investor.marketaxess.com/news/news-details/2026/MarketAxess-Reports-Second-Quarter-2026-Financial-Results/default.aspx",
}
# dispute rows resolved today (symbol -> date, time)
DISP = {"HPQ": ("2026-08-26", "amc"), "NTNX": ("2026-08-26", "amc")}


def run(db, sql):
    r = subprocess.run([sys.executable, Q, "--db", db, "--write", "--sql", sql],
                       capture_output=True, text=True)
    out = (r.stdout + r.stderr).strip().replace("\n", " | ")
    print(f"  rc={r.returncode} {out[:160]}")


for sym, url in IR.items():
    assert ";" not in url, sym
    print(f"IR {sym}")
    run(DL, f"UPDATE symbol_metadata SET ir_earnings_url='{url}', "
            f"ir_url_last_verified='{TODAY}' WHERE symbol='{sym}'")

for sym, (d, t) in DISP.items():
    print(f"DISPUTE {sym}")
    run(PF, f"UPDATE earnings_date_disputes SET resolution='confirmed_agent', "
            f"resolved_date='{d}', resolved_time='{t}', resolved_at='{NOW}', "
            f"research_url='{IR[sym]}' WHERE trade_date='{TODAY}' AND symbol='{sym}'")

print("\n--- verify ---")
run(DL, "SELECT symbol, substr(ir_earnings_url,1,55), ir_url_last_verified "
        "FROM symbol_metadata WHERE ir_url_last_verified='2026-08-07'")
run(PF, "SELECT symbol, resolution, resolved_date, resolved_time "
        "FROM earnings_date_disputes WHERE trade_date='2026-08-07'")
