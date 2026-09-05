"""IR-URL + dispute-resolution writes for 2026-08-12.
subprocess arg list (never a shell string); no ';' inside literals; --write.
Verified with a follow-up SELECT -- exit code proves nothing."""
import subprocess, sys
sys.stdout.reconfigure(encoding="utf-8")
Q = "E:/options_scanner/tools/direct_db_query.py"
DL = "E:/options_scanner/data/datalake.db"
PF = "E:/options_scanner/data/performance.db"
TODAY, NOW = "2026-08-12", "2026-08-12 08:10:00"

IR = {
 # TECH - the rss path 404s; this listing works and is the real PR channel
 "TECH": "https://investors.bio-techne.com/press-releases",
 # NTAP - working feed (carries the "Hosts ... Results Webcast" advance PRs)
 "NTAP": "https://investors.netapp.com/rss/pressrelease.aspx",
 # A - NO RSS on any path/host; note the www. prefix on investor.agilent.com
 "A":    "https://www.investor.agilent.com/news-and-events/news/news-details/"
         "2026/Agilent-to-Announce-Third-Quarter-Fiscal-Year-2026-Financial-"
         "Results-on-Aug--26/default.aspx",
 # CRM - replaces the stale Q1-FY27 deep link with the feed
 "CRM":  "https://investor.salesforce.com/rss/pressrelease.aspx",
 # NVDA - replaces the 2025 per-quarter deep link with the feed
 "NVDA": "https://investor.nvidia.com/rss/pressrelease.aspx",
 "VEEV": "https://ir.veeva.com/rss/pressrelease.aspx",
 "GTLB": "https://ir.gitlab.com/rss/pressrelease.aspx",
 "M":    "https://investors.macysinc.com/rss/pressrelease.aspx",
 # WSM - NEW working host: ir.williams-sonomaINC.com (the -sonoma.com and
 # gcs-web variants are all NXDOMAIN)
 "WSM":  "https://ir.williams-sonomainc.com/rss/pressrelease.aspx",
}
# dispute rows fully resolved today (symbol -> date, time, research url)
DISP = {
 "NTAP": ("2026-09-02", "amc",
          "https://investors.netapp.com/news/news-details/2026/NetApp-Hosts-"
          "First-Quarter-of-Fiscal-Year-2027-Financial-Results-Webcast/"
          "default.aspx"),
}


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

for sym, (d, t, u) in DISP.items():
    print(f"DISPUTE {sym}")
    run(PF, f"UPDATE earnings_date_disputes SET resolution='confirmed_agent', "
            f"resolved_date='{d}', resolved_time='{t}', resolved_at='{NOW}', "
            f"research_url='{u}' WHERE trade_date='{TODAY}' AND symbol='{sym}'")

# GTLB + M: time-only writes. earnings_confirm.py has no time-only mode, so it
# was run with the DB's own date and the flag is reset immediately after.
#   GTLB amc - its own results PR posts 16:05 ET and the 2.02 furnishes 20:0x-
#              20:17Z across quarters. DATE 09-02 is +364d only, not sourced.
#   M    bmo - its own Q1 results PR posted 06:55 ET, 2.02 furnishes ~10:59Z.
#              DATE 09-02 is +364d only, not sourced (advance PR due ~08-17).
for sym in ("GTLB", "M"):
    print(f"{sym} date_confirmed reset")
    run(DL, "UPDATE earnings_upcoming SET date_confirmed=0, "
            f"date_confirmed_by=NULL WHERE symbol='{sym}'")

print("\n--- verify ---")
run(DL, "SELECT symbol, substr(ir_earnings_url,1,56), ir_url_last_verified "
        "FROM symbol_metadata WHERE ir_url_last_verified='2026-08-12'",
    write=False)
run(DL, "SELECT symbol, earnings_date, earnings_time, date_confirmed, "
        "date_confirmed_by FROM earnings_upcoming WHERE symbol IN "
        "('TECH','NTAP','A','CRM','NVDA','VEEV','GTLB','M','NCNO','PVH','WSM')",
    write=False)
run(PF, "SELECT symbol, resolution, resolved_date, resolved_time "
        "FROM earnings_date_disputes WHERE trade_date='2026-08-12'", write=False)
