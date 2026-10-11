"""2026-10-11 Sunday maintenance: roll sessions 09-22 → 09-25 plus the 09-20 maintenance entry
out of the active research log into the summer archive (verbatim, chronological, ahead of
Appendix A). These are the last calendar-Q3 sessions, so the summer archive is closed after this.
Same shape as maintenance_archive_20261004.py; git HEAD is the backup. Verifies every moved
non-blank line landed and nothing else left the log."""
import re
from pathlib import Path

ROOT = Path(r"E:/options_scanner/agents/earnings_researcher")
LOG = ROOT / "memory" / "research_log.md"
ARC = ROOT / "memory" / "archive" / "research_log_2026-Q3_summer-earnings.md"

log = LOG.read_text(encoding="utf-8").split("\n")
arc = ARC.read_text(encoding="utf-8").split("\n")


def trim(blk):
    while blk and blk[-1].strip() in ("", "---"):
        blk.pop()
    return blk


# sessions 09-25 → 09-22 sit directly above "# Maintenance History"
s25 = next(i for i, l in enumerate(log) if l.startswith("## Session: 2026-09-25"))
maint = next(i for i, l in enumerate(log) if l.strip() == "# Maintenance History")
blk = log[s25:maint]
idx = [i for i, l in enumerate(blk) if l.startswith("## Session: ")]
sessions = []
for n, i in enumerate(idx):
    j = idx[n + 1] if n + 1 < len(idx) else len(blk)
    sessions.append(trim(blk[i:j]))
dates = [re.search(r"\d{4}-\d{2}-\d{2}", s[0]).group(0) for s in sessions]
assert dates == ["2026-09-25", "2026-09-24", "2026-09-23", "2026-09-22"], dates
sessions.reverse()

# 09-20 maintenance entry = last block of the file
m20 = next(i for i, l in enumerate(log) if l.startswith("## Weekly Maintenance — 2026-09-20"))
mblk = trim(log[m20:])

app = next(i for i, l in enumerate(arc) if l.startswith("## Appendix A"))
ins = app
while arc[ins - 1].strip() in ("", "---"):
    ins -= 1
tail = arc[ins:app]
moved = []
for s in sessions:
    moved += ["", "---", ""] + s
moved += ["", "---", "",
          "_[Maintenance entry moved here from the active log at the 2026-10-11 maintenance, verbatim. "
          "It covers the week of 09-14 → 09-18, whose sessions sit above.]_", ""] + mblk
new_arc = arc[:ins] + moved + tail + arc[app:]
txt = "\n".join(new_arc)
old = "Sessions **2026-07-01 → 2026-09-15**"
assert txt.count(old) == 1
txt = txt.replace(old, "Sessions **2026-07-01 → 2026-09-25**", 1)
old2 = "plus the 09-13 maintenance entry), each inserted ahead of the appendices."
assert txt.count(old2) == 1
txt = txt.replace(old2, "plus the 09-13 maintenance entry) and the 2026-10-11 maintenance (09-22 → 09-25, "
                  "plus the 09-20 maintenance entry; **this closes the archive**: every calendar-Q3 session "
                  "is now here), each inserted ahead of the appendices.", 1)

new_log = trim(log[:s25] + log[maint:m20])
text = "\n".join(new_log) + "\n"
text = re.sub(r"\n---\n\n+---\n", "\n---\n", text)

arc_set = set(l for l in txt.split("\n") if l.strip())
missing = [l for s in sessions + [mblk] for l in s if l.strip() and l not in arc_set]
assert not missing, missing[:3]
log_set = set(l for l in text.split("\n") if l.strip())
kept_expected = [l for l in log[:s25] + log[maint:m20] if l.strip() and l.strip() != "---"]
assert all(l in log_set for l in kept_expected)

ARC.write_text(txt, encoding="utf-8")
LOG.write_text(text, encoding="utf-8")
print("moved:", [s[0][:34] for s in sessions], mblk[0][:45])
print("log lines: %d -> %d" % (len(log), len(text.split("\n"))))
print("archive lines: %d -> %d" % (len(arc), len(txt.split("\n"))))
