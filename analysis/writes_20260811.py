"""IR-URL + dispute-resolution writes for 2026-08-11.
subprocess arg list (never a shell string); no ';' inside literals; --write.
Verified with a follow-up SELECT -- exit code proves nothing."""
import subprocess, sys
sys.stdout.reconfigure(encoding="utf-8")
Q = "E:/options_scanner/tools/direct_db_query.py"
DL = "E:/options_scanner/data/datalake.db"
PF = "E:/options_scanner/data/performance.db"
TODAY, NOW = "2026-08-11", "2026-08-11 08:05:00"

IR = {
 # LI - the Q2 advance PR that landed 04:30 ET this morning
 "LI":  "https://ir.lixiang.com/news-releases/news-release-details/"
        "li-auto-inc-report-second-quarter-2026-financial-results-august",
 # NIO - working feed host, confirmed today (Q1-26 advance PR is the time source)
 "NIO": "https://ir.nio.com/rss/news-releases.xml",
 # PDD - working feed host, confirmed today (pubDates are +0800)
 "PDD": "https://investor.pddholdings.com/rss/news-releases.xml",
 # PVH - NEW working host; www.pvh.com 403s, pvh.gcs-web.com serves the feed
 "PVH": "https://pvh.gcs-web.com/rss/news-releases.xml",
}
# dispute rows fully resolved today (symbol -> date, time)
DISP = {"LI": ("2026-08-26", "bmo")}


def run(db, sql, write=True):
    cmd = [sys.executable, Q, "--db", db, "--sql", sql]
    if write:
        cmd.insert(4, "--write")
    r = subprocess.run(cmd, capture_output=True, text=True)
    out = (r.stdout + r.stderr).strip().replace("\n", " | ")
    print(f"  rc={r.returncode} {out[:220]}")


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

# NIO: time-only write. earnings_confirm.py has no time-only mode, so it was run
# with the DB's own date and the confirmation flag is reset immediately after --
# the TIME is company-sourced (NIO's Q1-26 advance PR: "before the open of the
# U.S. markets", call 8:00am ET) but the DATE 2026-09-01 is not.
print("NIO date_confirmed reset")
run(DL, "UPDATE earnings_upcoming SET date_confirmed=0, date_confirmed_by=NULL "
        "WHERE symbol='NIO'")

print("\n--- verify ---")
run(DL, "SELECT symbol, substr(ir_earnings_url,1,58), ir_url_last_verified "
        "FROM symbol_metadata WHERE ir_url_last_verified='2026-08-11'", write=False)
run(DL, "SELECT symbol, earnings_date, earnings_time, date_confirmed, "
        "date_confirmed_by FROM earnings_upcoming "
        "WHERE symbol IN ('LI','NIO','PDD','PVH','TECH','NCNO','COTY','SQM')",
    write=False)
run(PF, "SELECT symbol, resolution, resolved_date, resolved_time "
        "FROM earnings_date_disputes WHERE trade_date='2026-08-11'", write=False)
