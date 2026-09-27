"""2026-09-27 Sunday maintenance: roll sessions 09-08 -> 09-11 out of the active
research log into the summer archive (verbatim, chronological, before Appendix A).
Same shape as maintenance_archive_20260920.py. Backs both files up first and
verifies every moved non-blank line landed."""
import re
import shutil
import sys
from pathlib import Path

ROOT = Path(r"E:/options_scanner/agents/earnings_researcher")
LOG = ROOT / "memory" / "research_log.md"
ARC = ROOT / "memory" / "archive" / "research_log_2026-Q3_summer-earnings.md"
BAK = Path(sys.argv[1])

BAK.mkdir(parents=True, exist_ok=True)
shutil.copy2(LOG, BAK / "research_log.pre_20260927.md")
shutil.copy2(ARC, BAK / "summer_archive.pre_20260927.md")

log = LOG.read_text(encoding="utf-8").split("\n")
arc = ARC.read_text(encoding="utf-8").split("\n")

start = next(i for i, l in enumerate(log) if l.startswith("## Session: 2026-09-11"))
maint = next(i for i, l in enumerate(log) if l.strip() == "# Maintenance History")
end = maint
while log[end - 1].strip() in ("", "---"):
    end -= 1
block = log[start:end]

idx = [i for i, l in enumerate(block) if l.startswith("## Session: ")]
sessions = []
for n, i in enumerate(idx):
    j = idx[n + 1] if n + 1 < len(idx) else len(block)
    s = block[i:j]
    while s and s[-1].strip() in ("", "---"):
        s.pop()
    sessions.append(s)
dates = [re.search(r"\d{4}-\d{2}-\d{2}", s[0]).group(0) for s in sessions]
assert dates == ["2026-09-11", "2026-09-10", "2026-09-09", "2026-09-08"], dates
sessions.reverse()  # archive is oldest-first

app = next(i for i, l in enumerate(arc) if l.startswith("## Appendix A"))
ins = app
while arc[ins - 1].strip() in ("", "---"):
    ins -= 1
tail = arc[ins:app]
moved = []
for s in sessions:
    moved += ["", "---", ""] + s
new_arc = arc[:ins] + moved + tail + arc[app:]

# archive header: extend the covered range
hdr = "\n".join(new_arc[:12])
assert "Sessions **2026-07-01 → 2026-09-03**" in hdr
assert "and the 2026-09-20 maintenance (09-01 → 09-03, inserted ahead of the appendices)" in hdr
new_arc_text = "\n".join(new_arc)
new_arc_text = new_arc_text.replace(
    "Sessions **2026-07-01 → 2026-09-03**", "Sessions **2026-07-01 → 2026-09-11**", 1)
new_arc_text = new_arc_text.replace(
    "and the 2026-09-20 maintenance (09-01 → 09-03, inserted ahead of the appendices)",
    "the 2026-09-20 maintenance (09-01 → 09-03) and the 2026-09-27 maintenance (09-08 → 09-11; "
    "09-08 is a reconstructed stub), each inserted ahead of the appendices", 1)
new_arc = new_arc_text.split("\n")

new_log = log[:start] + log[end:]
text = "\n".join(new_log)
text = re.sub(r"\n---\n\n+---\n", "\n---\n", text)

arc_set = set(l for l in new_arc if l.strip())
missing = [l for s in sessions for l in s if l.strip() and l not in arc_set]
assert not missing, missing[:3]

ARC.write_text("\n".join(new_arc), encoding="utf-8")
LOG.write_text(text, encoding="utf-8")
print("moved sessions:", [s[0][:34] for s in sessions])
print("moved lines:", sum(len(s) for s in sessions))
print("log lines: %d -> %d" % (len(log), len(text.split("\n"))))
print("archive lines: %d -> %d" % (len(arc), len(new_arc)))
