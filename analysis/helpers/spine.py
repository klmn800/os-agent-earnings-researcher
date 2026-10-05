"""stocktitan news spine: last 10 headlines per symbol from the page's JSON-LD.

Usage (from the workspace root):  python analysis/helpers/spine.py SYM [SYM ...]
Pass the most urgent symbols first: stocktitan starts returning 429s partway through a batch.
See memory/reference_stocktitan_jsonld_discovery.md for the request shape and its traps.
Promoted from inbox/fetch/spine.py (10-01 session) at the 2026-10-04 maintenance.
"""
import re, subprocess, sys, time
from datetime import date

UA = ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
      "(KHTML, like Gecko) Chrome/126.0 Safari/537.36")
PAT = re.compile(r'"headline":\s*"([^"]+)",\s*"url":\s*"([^"]+)",\s*"datePublished":\s*"([^"]+)"')
KEY = re.compile(r'(?i)quarter|Q[1-4]|earnings|results|call|webcast|announce')
since = date.today().replace(day=1)
since = since.replace(month=since.month - 1) if since.month > 1 else since.replace(year=since.year - 1, month=12)

for i, s in enumerate(sys.argv[1:]):
    if i:
        time.sleep(9)
    f = f"inbox/fetch/st_{s}.html"
    r = subprocess.run(["curl", "-s", "--compressed", "-m", "40", "-A", UA,
                        "-H", "Accept: text/html", "-H", "Accept-Language: en-US,en;q=0.9",
                        f"https://www.stocktitan.net/news/{s}/", "-o", f, "-w", "%{http_code}"],
                       capture_output=True, text=True)
    t = open(f, encoding="utf-8", errors="replace").read()
    items = PAT.findall(t)
    flag = ""
    if r.stdout != "200" or len(t) < 5000 or "Too Many Requests" in t:
        flag = "  <-- UNREAD (429/blocked): not an absence"
    elif not items:
        flag = "  <-- full page but 0 items: check the regex before reading absence"
    print(f"== {s} http={r.stdout} bytes={len(t)} items={len(items)}{flag}")
    for h, u, d in items:
        if d[:10] >= since.isoformat() and KEY.search(h):
            print("  ", d[:16], h[:110], "|", u)
