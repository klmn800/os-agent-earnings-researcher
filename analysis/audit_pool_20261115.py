"""Rebuild the source-audit pool: Appendix A ledger rows dated 10-13 -> 11-05 minus symbols checked by audits #3-#5.
Stratum tags from the ledger source text (same heuristic as 11-08). Usage: python analysis/audit_pool_20261115.py"""
import re, random, json
arch = open("memory/archive/research_log_2026-Q4_fall-earnings.md", encoding="utf-8").read()
appx = arch[arch.index("## Appendix A"):]
rows = []
for line in appx.splitlines():
    m = re.match(r"\|\s*([A-Z][A-Z0-9.\-]*)\s*\|\s*(2026-\d\d-\d\d)\s*\|\s*(\w+)\s*\|\s*(.*)\|\s*$", line)
    if m and "2026-10-13" <= m.group(2) <= "2026-11-05":
        rows.append(dict(sym=m.group(1), date=m.group(2), time=m.group(3), src=m.group(4).strip()))
audited = set()
for f in ["source_audit_20261025.md", "source_audit_20261101.md", "source_audit_20261108.md"]:
    for line in open("analysis/" + f, encoding="utf-8"):
        m = re.match(r"\|\s*([A-Z][A-Z0-9.\-]*)\s*\|", line)
        if m and line.count("|") >= 7 and m.group(1) not in ("SYM",):
            audited.add(m.group(1))
audited.add("SCHW")  # hand-added to audit #3 ("SCHW *(added)*"), missed by the row regex
def tag(s):
    l = s.lower()
    if "inferred" in l: return "inferred"
    if re.search(r"via search|search summary|search result", l): return "search"
    if re.search(r"stocktitan|finviz|wire text|financialcontent|biopharmawatch|businesswire|prnewswire|globenewswire|accesswire|copy", l): return "copy"
    return "IR"
pool = [dict(r, stratum=tag(r["src"])) for r in rows if r["sym"] not in audited]
seen=set(); pool=[r for r in pool if not (r["sym"] in seen or seen.add(r["sym"]))]
from collections import Counter
print("ledger rows", len(rows), "audited syms", len(audited), "pool", len(pool), Counter(r["stratum"] for r in pool))
random.seed(20261115)
ir = [r for r in pool if r["stratum"] == "IR"]
cp = [r for r in pool if r["stratum"] == "copy"]
other = [r for r in pool if r["stratum"] not in ("IR", "copy")]
draw = ir + other + random.sample(cp, max(0, 40 - len(ir) - len(other)))
random.shuffle(draw)
json.dump(dict(pool=pool, draw=draw), open("analysis/audit_pool_20261115.json", "w"), indent=1)
print("draw", len(draw), Counter(r["stratum"] for r in draw))
for r in draw: print(*[str(x).encode("ascii","replace").decode() for x in (r["sym"], r["date"], r["time"], r["stratum"], "|", r["src"][:110])])
