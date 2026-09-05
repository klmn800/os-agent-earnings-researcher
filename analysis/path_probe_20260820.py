"""PATH: ir.uipath.com is an SPA on listing pages but serves real per-item
detail pages (the cached Q1 URL rendered fine). Guess the Q2 FY27 event slug
using UiPath's own YYYYMMDD-slug shape -- with a NONSENSE-PATH CONTROL first
(standing rule 3: never trust a slug probe on a host that 200s everything)."""
import re, sys, urllib.request
from concurrent.futures import ThreadPoolExecutor
sys.stdout.reconfigure(encoding="utf-8")
UA=("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
    "(KHTML, like Gecko) Chrome/126.0 Safari/537.36")
B="https://ir.uipath.com/events-presentations/detail/"
URLS={
 "CONTROL-nonsense": B+"20261111-uipath-zzzz-nonexistent-quarter-call",
 "known-good-Q2FY26": B+"20250904-uipath-second-quarter-fiscal-2026-financial-results-conference-call",
 "guess-0903": B+"20260903-uipath-second-quarter-fiscal-2027-financial-results-conference-call",
 "guess-0902": B+"20260902-uipath-second-quarter-fiscal-2027-financial-results-conference-call",
 "guess-0910": B+"20260910-uipath-second-quarter-fiscal-2027-financial-results-conference-call",
}
def strip(h):
    h=re.sub(r"(?is)<(script|style|nav|header|footer).*?</\1>"," ",h)
    h=re.sub(r"(?s)<[^>]+>"," ",h)
    return re.sub(r"\s+"," ",h.replace("&nbsp;"," ").replace("&amp;","&"))
def go(kv):
    t,u=kv
    try:
        r=urllib.request.Request(u,headers={"User-Agent":UA,"Accept":"*/*"})
        with urllib.request.urlopen(r,timeout=25) as f:
            return t,u,f.getcode(),strip(f.read().decode("utf-8","replace"))
    except urllib.error.HTTPError as e: return t,u,e.code,""
    except Exception as e: return t,u,f"ERR {type(e).__name__}",""
with ThreadPoolExecutor(max_workers=5) as ex:
    for t,u,code,txt in ex.map(go,URLS.items()):
        print(f"\n{t:<20} HTTP {code}  {len(txt)}B")
        if txt:
            m=re.search(r"(?:Sep|Aug|Oct)[^|]{0,160}",txt)
            print("   ",txt[:400])
