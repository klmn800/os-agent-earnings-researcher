"""IR-URL cache + dispute-resolution writes for 2026-07-30.
Uses subprocess (not shell string building) to avoid the 07-27 shell-quoting bug
that silently dropped writes. Verifies with follow-up SELECTs.
"""
import subprocess, sys

PY = sys.executable
Q = "E:/options_scanner/tools/direct_db_query.py"
DL = "E:/options_scanner/data/datalake.db"
PERF = "E:/options_scanner/data/performance.db"
TODAY = "2026-07-30"
NOW = "2026-07-30 08:05:00"

def run(db, sql, write=True):
    cmd = [PY, Q, "--db", db, "--sql", sql]
    if write:
        cmd.insert(4, "--write")
    r = subprocess.run(cmd, capture_output=True, text=True)
    print("   ", (r.stdout or "").strip()[:200], (r.stderr or "").strip()[:200])

# --- IR URLs (company domains only, never wire URLs) ---
IR = {
 "GO":   "https://investors.groceryoutlet.com/news-and-events/news-releases",
 "GRAL": "https://grail.com/press-releases/grail-to-announce-second-quarter-2026-financial-results/",
 "ZM":   "https://investors.zoom.us/news-releases",
 "HRB":  "https://investors.hrblock.com/financial-information/quarterly-results",
 "WMT":  "https://corporate.walmart.com/news/events/fy2027-q2-earnings-release",
}
print("== IR URLs ==")
for sym, url in IR.items():
    print(sym)
    run(DL, f"UPDATE symbol_metadata SET ir_earnings_url='{url}', "
            f"ir_url_last_verified='{TODAY}' WHERE symbol='{sym}'")

# --- dispute resolutions ---
CONFIRMED = {
 "GO":   ("2026-08-12", "amc", "https://www.globenewswire.com/news-release/2026/07/29/3335567/0/en/grocery-outlet-holding-corp-announces-second-quarter-fiscal-2026-earnings-release-and-conference-call-date.html"),
 "GRAL": ("2026-08-05", "amc", "https://grail.com/press-releases/grail-to-announce-second-quarter-2026-financial-results/"),
 "ZM":   ("2026-08-25", "amc", "https://www.globenewswire.com/news-release/2026/07/28/3334718/0/en/zoom-to-release-financial-results-for-the-second-quarter-of-fiscal-year-2027.html"),
 "HRB":  ("2026-08-11", "amc", "https://www.globenewswire.com/news-release/2026/07/28/3334734/0/en/H-R-Block-to-Release-Fiscal-2026-Results-on-August-11-2026.html"),
 "WMT":  ("2026-08-20", "bmo", "https://corporate.walmart.com/news/events/fy2027-q2-earnings-release"),
}
print("\n== dispute rows: confirmed_agent ==")
for sym, (d, t, url) in CONFIRMED.items():
    print(sym)
    run(PERF, f"UPDATE earnings_date_disputes SET resolution='confirmed_agent', "
              f"resolved_date='{d}', resolved_time='{t}', resolved_at='{NOW}', "
              f"research_url='{url}' WHERE trade_date='{TODAY}' AND symbol='{sym}'")

# ROST: time primary-sourced (SEC 8-K furnish), date cadence-only -> not a full confirm
print("\n== dispute rows: skipped (time written, date not company-sourced) ==")
run(PERF, "UPDATE earnings_date_disputes SET resolution='skipped', "
          f"resolved_time='amc', resolved_at='{NOW}', "
          "research_url='SEC 8-K Item 2.02 furnish times 16:02-16:04 ET x8 qtrs => amc. "
          "Date 08-20 is +364d-exact + Thursday-consistent but NOT company-sourced. "
          "Ross advance PR (~14d lead) due ~2026-08-06 - date_confirmed reset to 0' "
          f"WHERE trade_date='{TODAY}' AND symbol='ROST'")

SKIPPED = {
 "RDW":  "no Q2-26 advance PR yet; ir.rdw.com press-release page current thru 07-21. 2025 lead 7d (PR 07-30 -> 08-06 release) => PR due ~today. +364d => 08-05 = DB; amc from 16:2x-16:3x furnishes. next-check 07-31",
 "TECH": "no Q4 FY26 advance PR; investors.bio-techne.com IR calendar shows no upcoming events. +364d => 08-05 = DB; bmo solid (06:30 furnishes x8). WATCH: Merck KGaA acquisition (DEFA14A 07-09) may cancel the Q4 call entirely. next-check 08-03",
 "TRMB": "no Q2-26 advance PR. investor.trimble.com RSS is CURRENT (newest item today 07-30 07:00) and IR events page lists no upcoming events => real absence. Trimble lead is 14d (Q1: PR 04-22 -> 05-06), so an 08-05 date needs a PR from ~07-22 that does not exist - DB 08-05 now has a genuine counter-signal. finnhub 07-30 (today) also unsupported: no 8-K filed this morning. Both sides unsourced. next-check 07-31",
 "MNST": "no 2026 Q2 advance PR found (monsterbevcorp.com IR timed out; globenewswire domain search empty). Lead 7d (Q1: PR 04-30 -> 05-07) => PR for 08-06 due ~today. +364d => 08-06 AND 91d quarter spacing from Q1 05-07 => 08-06; amc from 16:2x furnishes. finnhub 07-30 would have needed a PR ~07-23 that does not exist. 4th independent line against finnhub. next-check 07-31",
 "NTRA": "no 2026 Q2 advance PR yet. CORRECTION to 07-29 note: Natera DOES issue one, via BusinessWire ~7d ahead (2025: PR 07-31 -> release 08-07) - it just does not hit the IR RSS feed, so the 07-29 'real absence, likely issues none' read was wrong. +364d => 08-06 = DB; amc from 16:1x. next-check 07-31",
 "CSCO": "no Q4 FY26 scheduling PR yet; investor.cisco.com RSS current. Lead 12d (Q3: PR 05-01 16:30 -> 05-13 release) => PR for 08-12 due ~07-31. +364d => 08-12 = DB; amc from 16:0x-16:1x. finnhub 08-19 = +7d artifact. next-check 07-31",
 "AMCR": "date fine (+364d => 08-13 = DB; finnhub 08-19 = +6d). TIME is the suspect field: furnish times alternate by quarter (2026-05-06 06:05 bmo / 2026-02-03 16:12 amc / 2025-11-05 16:20 amc / 2025-08-14 06:14 bmo) - recent-4 NOT unanimous, so the method's own guardrail says stop. DB amc may be stale. investors.amcor.com does not resolve (getaddrinfo failed). next-check 08-04",
 "PANW": "all three sources disagree and arithmetic cannot break it. +364d from 2025-08-18 => 08-17 (Mon), and PANW Q4 was Mon twice running (2025-08-18, 2024-08-19); DB says 08-18 (Tue); finnhub 08-24 (Mon). amc solid (16:0x-16:2x). Needs a company source. IR host timed out again. next-check 08-05",
 "TOL":  "+364d => 08-18 = DB (3rd Tue of Aug; Q3-25 08-19, Q3-24 08-20); finnhub 08-25 = +7d artifact. amc corroborated (16:4x furnish, call next morning). Issues no advance-date PR; investors.tollbrothers.com RSS now 403s. next-check 08-11",
 "FLO":  "regime change confirmed again from furnish times: Fri ~07:1x bmo thru 2025-08-15, then Thu ~16:1x amc from 2025-11-06. DB date 08-14 is a FRIDAY = old-regime; +364d returns the same stale Friday. Q1 slipped +6d under the new regime (2025-05-16 Fri -> 2026-05-21 Thu), so real Q2 date ~08-20 (Thu). BOTH DB 08-14 and finnhub 08-06 probably wrong. investors.flowersfoods.com RSS now 403s. next-check 08-06",
 "BIDU": "6-K filer => SEC Item 2.02 technique structurally blind. ir.baidu.com timed out (3rd session). finnhub 08-26 vs DB 08-19 is the +7d shape. Baidu Q2 lands ~3rd week of Aug, bmo (pre-US-open). next-check 08-10",
 "NXE":  "6-K filer. NexGen announces only via a 'to Host Q<n> Conference Call' PR ~2d ahead (Q1: 05-05 -> ~05-07), so genuinely unresearchable until ~08-03. www.nexgenenergy.ca/rss now 404s (host reachable, path moved). next-check 08-03",
 "JD":   "6-K filer => timing technique blind. ir.jd.com timed out again (3rd session). Q2-25 was 08-14 (Thu); neither DB 08-11 nor finnhub 08-13 matches. ~1wk lead => PR due ~08-04. next-check 08-04",
 "XPEV": "6-K filer; ir.xiaopeng.com timed out again. finnhub 08-25 vs DB 08-18 = +7d shape. next-check 08-10",
 "IAC":  "STRUCTURAL NON-EVENT, 4th consecutive session. IAC renamed People Incorporated, ticker PPLI, effective market open 2026-06-04 (CIK 1800227). Re-verified today: IAC absent from SEC company_tickers.json; PPLI present. Underlying date 08-03 amc is sound (+364d-exact off the 2025-08-04 16:06 ET furnish, PPLI furnishes 16:0x) but this row needs RENAMING to PPLI, not a date confirm. Needs symbol-level fix - see notes_for_ben.md",
 "YPF":  "6-K filer; investors.ypf.com RSS reachable but serves 0 items. No feed date to challenge DB 08-10. next-check 08-04",
 "DNN":  "6-K filer. denisonmines.com/rss works and is CURRENT (newest 07-28) but carries no earnings-date PR; feed is partly junk (a 2016 'Home' row, mis-ordered pubDates - do not trust its date pairing). Denison reports results same-day with no advance PR. next-check 08-04",
 "SE":   "6-K filer; www.sea.com RSS reachable but serves 0 items. Sea Q2 lands mid-Aug bmo (US pre-open); finnhub 08-10 vs DB 08-11 within noise. next-check 08-04",
 "NNE":  "files NO Item 2.02 8-K at all - results go straight into the 10-Q, so the SEC furnish-time technique will NEVER resolve its timing (re-verified: only 8-Ks since 06-01 are items 8.01 and 5.02). FY ends Sep 30. ir.nanonuclearenergy.com timed out again. next-check 08-05",
 "NU":   "6-K filer, no items field => timing blind. international.nubank.com.br RSS now 403s. finnhub absent this snapshot; DB 08-13. next-check 08-05",
 "XP":   "6-K filer; investors.xpinc.com chronic 403 (confirmed again) + no feed. Cadence says ~5pm ET (amc) but that needs a company source to write. finnhub 08-18 vs DB 08-17 within noise. next-check 08-10",
 "SQM":  "6-K filer; ir.sqm.com timed out. finnhub 08-19 vs DB 08-18 within noise. next-check 08-10",
}
print("\n== dispute rows: skipped ==")
for sym, note in SKIPPED.items():
    print(sym)
    note = note.replace("'", "").replace(";", " --")
    run(PERF, f"UPDATE earnings_date_disputes SET resolution='skipped', "
              f"resolved_at='{NOW}', research_url='{note}' "
              f"WHERE trade_date='{TODAY}' AND symbol='{sym}'")

print("\n== VERIFY: dispute rows for", TODAY, "==")
run(PERF, "SELECT resolution, COUNT(*) FROM earnings_date_disputes "
          f"WHERE trade_date='{TODAY}' GROUP BY resolution", write=False)
run(PERF, "SELECT symbol, resolution, resolved_date, resolved_time FROM "
          f"earnings_date_disputes WHERE trade_date='{TODAY}' ORDER BY resolution, symbol", write=False)
print("\n== VERIFY: IR urls ==")
run(DL, "SELECT symbol, ir_earnings_url, ir_url_last_verified FROM symbol_metadata "
        "WHERE symbol IN ('GO','GRAL','ZM','HRB','WMT')", write=False)
