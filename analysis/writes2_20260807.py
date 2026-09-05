"""Second write pass 2026-08-07: IR URLs for the straggler confirms + the BABA
dispute row. Same rules: arg list, no ';' in literals, --write, verify after."""
import subprocess, sys
sys.stdout.reconfigure(encoding="utf-8")
Q = "E:/options_scanner/tools/direct_db_query.py"
DL = "E:/options_scanner/data/datalake.db"
PF = "E:/options_scanner/data/performance.db"
TODAY, NOW = "2026-08-07", "2026-08-07 08:55:00"

IR = {
 "ARMK": "https://aramark.gcs-web.com/news-releases/news-release-details/aramark-host-conference-call-third-quarter-fiscal-2026-results",
 "TPR":  "https://tapestry.gcs-web.com/news-releases/news-release-details/tapestry-inc-host-fy26-fourth-quarter-and-year-end-earnings-call",
 "AAON": "https://investors.aaon.com/investor-news/aaon-announces-second-quarter-2026-conference-call-and-webcast",
 "CAH":  "https://newsroom.cardinalhealth.com/2026-07-09-Cardinal-Health-to-Announce-Fourth-Quarter-and-Year-End-Results-for-Fiscal-Year-2026-on-August-11",
 "GLOB": "https://investors.globant.com/2026-07-30-Globant-to-Announce-Second-Quarter-2026-Financial-Results-on-August-13th",
 "AMCR": "https://www.amcor.com/media/news/amcor-to-report-fiscal-2026-fourth-quarter-and-full-year-results",
 "BHP":  "https://www.bhp.com/investor-hub/financial-calendar",
 "BABA": "https://www.alibabagroup.com/en-US/document-2022412636729114624",
}
DISP = {"BABA": ("2026-08-20", "bmo")}


def run(db, sql):
    r = subprocess.run([sys.executable, Q, "--db", db, "--write", "--sql", sql],
                       capture_output=True, text=True)
    print(f"  rc={r.returncode} {(r.stdout + r.stderr).strip().splitlines()[:1]}")


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
