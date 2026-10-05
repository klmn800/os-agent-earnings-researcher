"""2026-10-04 Sunday maintenance: roll sessions 09-14 and 09-15 plus the 09-13 maintenance entry
out of the active research log into the summer archive (verbatim, chronological, ahead of
Appendix A). Same shape as maintenance_archive_20260927.py; git HEAD is the backup. Verifies
every moved non-blank line landed."""
import re
from pathlib import Path

ROOT = Path(r"E:/options_scanner/agents/earnings_researcher")
LOG = ROOT / "memory" / "research_log.md"
ARC = ROOT / "memory" / "archive" / "research_log_2026-Q3_summer-earnings.md"

log = LOG.read_text(encoding="utf-8").split("\n")
arc = ARC.read_text(encoding="utf-8").split("\n")


def cut(lines, start_pred, stop_pred):
    s = next(i for i, l in enumerate(lines) if start_pred(l))
    e = next(i for i in range(s + 1, len(lines)) if stop_pred(lines[i]))
    blk = lines[s:e]
    while blk and blk[-1].strip() in ("", "---"):
        blk.pop()
    return s, e, blk


# sessions 09-15 then 09-14 sit directly above "# Maintenance History"
s15, _, _ = cut(log, lambda l: l.startswith("## Session: 2026-09-15"), lambda l: l.startswith("## Session: 2026-09-14"))
maint = next(i for i, l in enumerate(log) if l.strip() == "# Maintenance History")
blk = log[s15:maint]
idx = [i for i, l in enumerate(blk) if l.startswith("## Session: ")]
sessions = []
for n, i in enumerate(idx):
    j = idx[n + 1] if n + 1 < len(idx) else len(blk)
    s = blk[i:j]
    while s and s[-1].strip() in ("", "---"):
        s.pop()
    sessions.append(s)
dates = [re.search(r"\d{4}-\d{2}-\d{2}", s[0]).group(0) for s in sessions]
assert dates == ["2026-09-15", "2026-09-14"], dates
sessions.reverse()

# 09-13 maintenance entry = last block of the file
m13 = next(i for i, l in enumerate(log) if l.startswith("## Weekly Maintenance — 2026-09-13"))
mblk = log[m13:]
while mblk and mblk[-1].strip() in ("", "---"):
    mblk.pop()

app = next(i for i, l in enumerate(arc) if l.startswith("## Appendix A"))
ins = app
while arc[ins - 1].strip() in ("", "---"):
    ins -= 1
tail = arc[ins:app]
moved = []
for s in sessions:
    moved += ["", "---", ""] + s
moved += ["", "---", "",
          "_[Maintenance entry moved here from the active log at the 2026-10-04 maintenance, verbatim. "
          "It covers the week whose sessions sit just above.]_", ""] + mblk
new_arc = arc[:ins] + moved + tail + arc[app:]
txt = "\n".join(new_arc)
old = "Sessions **2026-07-01 → 2026-09-11**"
assert txt.count(old) == 1
txt = txt.replace(old, "Sessions **2026-07-01 → 2026-09-15**", 1)
old2 = "and the 2026-09-27 maintenance (09-08 → 09-11; 09-08 is a reconstructed stub), each inserted ahead of the appendices."
assert txt.count(old2) == 1
txt = txt.replace(old2, "the 2026-09-27 maintenance (09-08 → 09-11; 09-08 is a reconstructed stub) and the "
                  "2026-10-04 maintenance (09-14, 09-15, plus the 09-13 maintenance entry), each inserted ahead "
                  "of the appendices.", 1)

new_log = log[:s15] + log[maint:m13]
while new_log and new_log[-1].strip() in ("", "---"):
    new_log.pop()
text = "\n".join(new_log) + "\n"
text = re.sub(r"\n---\n\n+---\n", "\n---\n", text)

arc_set = set(l for l in txt.split("\n") if l.strip())
missing = [l for s in sessions + [mblk] for l in s if l.strip() and l not in arc_set]
assert not missing, missing[:3]
# nothing else lost from the log
log_set = set(l for l in text.split("\n") if l.strip())
kept_expected = [l for l in log[:s15] + log[maint:m13] if l.strip()]
assert all(l in log_set for l in kept_expected)

ARC.write_text(txt, encoding="utf-8")
LOG.write_text(text, encoding="utf-8")
print("moved:", [s[0][:34] for s in sessions], mblk[0][:45])
print("log lines: %d -> %d" % (len(log), len(text.split("\n"))))
print("archive lines: %d -> %d" % (len(arc), len(txt.split("\n"))))
