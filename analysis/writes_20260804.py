"""Dispute-row 'skipped' notes for the 2026-08-04 session.

The confirmed rows + IR URLs were written inline earlier. This records the seven
disputes that stay open, each with the evidence and a next-check date.

Two quoting gotchas, both from memory/reference_db_write_forward_slash_paths.md:
  - direct_db_query.py splits --sql on ';' even inside string literals => no
    semicolons in the note text (asserted below)
  - apostrophes must be SQL-escaped by doubling them, or the UPDATE silently
    truncates at the quote. Single quotes survive the bash double-quoted arg fine.
"""
import subprocess

DQ = "python E:/options_scanner/tools/direct_db_query.py"
PERF = "E:/options_scanner/data/performance.db"
TODAY = "2026-08-04"
NOW = "2026-08-04 07:40:00"

SKIPPED = {
 "TECH": "Q4 FY26 advance PR now ~21d overdue (Q3 lead was 22d - PR 04-14 for the 05-06 call). investors.bio-techne.com/rss is CURRENT through 07-08 and empty of it, so this is a real absence, not a fetch failure. Only 8-Ks since the 05-06 Q3 release are the Merck KGaA merger pair (06-25 item 7.01, 06-26 items 1.01/5.02). DB date 08-05 is TOMORROW and no call has been announced, so 08-05 is now actively doubtful rather than merely unsourced. WROTE time=bmo (06:30 ET furnish x8 qtrs - the DB amc error was flagged 07-15, 07-27 and 07-31 and had still never been written) then reset date_confirmed=0. 4th consecutive session holding - needs Ben.",
 "FLO":  "Unchanged and still the one date I actively distrust. flowersfoods.com/feed is current through Q1 (05-21 results) with no Q2 advance PR. Regime change Fri-bmo to Thu-amc since Nov-2025 makes DB 08-14 an old-regime FRIDAY, and finnhub 08-06 has no support either (Q1 lead was 15d, so an 08-06 release needed a PR by ~07-22 that does not exist). Real date ~08-20 (Thu). BOTH feeds probably wrong. next-check 08-06",
 "NXE":  "~2d lead by design. www.nexgenenergy.ca/rss is current (newest 06-30) and still carries no 'NexGen to Host Q2 2026 Conference Call' PR as of 07:30 ET. DB 08-05 is tomorrow, which would have needed that PR today. 6-K filer, so the SEC Item 2.02 timing technique is structurally blind. finnhub 08-12 is the alternative. next-check 08-05",
 "NCNO": "TIME RESOLVED = amc (Item 2.02 furnishes 16:03-16:07 ET x5 qtrs, recent-4 unanimous, plus nCino's own Q1 FY27 PR - results after market close 05-27, call 4:30pm ET). DATE not company-sourced. nCino issues an 'Announces Timing of its Q<n> Financial Results Conference Call' PR ~13d ahead (Q1 FY27 - PR 05-14 for the 05-27 release), so the Q2 FY27 PR is due ~08-12. +364d gives 08-25 Tue = DB exactly and finnhub 09-01 is the familiar +7d artifact, but cadence corroborates and does not source. date_confirmed reset to 0. next-check 08-12",
 "NNE":  "Time is STRUCTURALLY unanswerable - zero Item 2.02 8-Ks ever, results go straight into the 10-Q. Do not spend further calls on NNE timing - it needs a Ben default or a policy exception. The DATE is researchable though: NNE issues a 'to Hold Q<n> Business Update Webcast on <date>' PR ~7d ahead (05-07 for the 05-14 webcast). Feed is current through 07-27 with no Q3 PR yet, so for DB 08-12 it is due ~08-05. next-check 08-05",
 "SQM":  "Unchanged, still needs Ben. 6-K filer that issues NO advance-date PRs at all - the feed (current through 07-21) confirms the pattern rather than merely failing to find one. SQM releases ~22:00 ET with the call the following midday, so DB 08-18 is the release date and finnhub 08-19 is the call date - both describe real events and neither is what amc literally means. Genuine ambiguous-time case, same family as EXPD.",
 "PVH":  "TIME RESOLVED = amc (Item 2.02 furnishes 16:17-16:23 ET x7 qtrs, recent-4 unanimous, plus PVH's own Q1 2026 PR - results released after the market closes Wed 06-03 with the call Thu 06-04 at 9:00am ET). DATE not company-sourced. PVH issues a 'to Host Conference Call to Discuss Q<n> Earnings Results' PR ~16d ahead (Q1 - PR 05-18 for the 06-03 release), so the Q2 PR is due ~08-10. +364d gives 08-25 Tue = DB exactly, and the finnhub 08-24 candidate is a MONDAY, which is off-pattern for PVH. date_confirmed reset to 0. next-check 08-10",
}


def run(db, sql):
    r = subprocess.run(f'{DQ} --db {db} --write --sql "{sql}"',
                       shell=True, capture_output=True, text=True)
    return (r.stdout + r.stderr).strip().splitlines()[-1:] or [""]


print("== dispute rows: skipped, with evidence ==")
for sym, note in SKIPPED.items():
    assert ";" not in note, f"{sym}: semicolon would split the SQL"
    assert '"' not in note, f"{sym}: double quote would end the bash arg"
    esc = note.replace("'", "''")
    sql = (f"UPDATE earnings_date_disputes SET resolution='skipped', "
           f"resolved_at='{NOW}', research_url='{esc}' "
           f"WHERE trade_date='{TODAY}' AND symbol='{sym}'")
    print(f"  {sym:5} {run(PERF, sql)[0]}")
