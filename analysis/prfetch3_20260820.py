import re, sys, urllib.request
from concurrent.futures import ThreadPoolExecutor
sys.stdout.reconfigure(encoding="utf-8")
UA=("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
    "(KHTML, like Gecko) Chrome/126.0 Safari/537.36")
HDRS={"User-Agent":UA,"Accept":"text/html,application/xhtml+xml,*/*"}
def strip(h):
    h=re.sub(r"(?is)<(script|style|nav|header|footer).*?</\1>"," ",h)
    h=re.sub(r"(?s)<[^>]+>"," ",h)
    for a,b in [("&nbsp;"," "),("&amp;","&"),("&#39;","'"),("&rsquo;","'"),
                ("&quot;",'"'),("&ldquo;",'"'),("&rdquo;",'"'),("&mdash;","--")]:
        h=h.replace(a,b)
    return re.sub(r"\s+"," ",h)
KEY=re.compile(r"before|after|market|close|open|a\.m\.|p\.m\.|ET\b|PT\b|"
               r"conference call|webcast|September|Sept|August|202[67]",re.I)
JOBS={
 "GOLD": "https://ir.gold.com/news-events/press-releases/detail/222/gold-com-sets-fiscal-fourth-quarter-and-full-year-2026-earnings-call-for-wednesday-september-2-at-4-30-p-m-et",
 "GOLD-cal": "https://ir.gold.com/news-events/ir-calendar/detail/20260902-q4-2026-earnings-conference-call",
 "PATH": "https://www.businesswire.com/news/home/20260806817905/en/UiPath-Announces-Second-Quarter-Fiscal-2027-Financial-Results-Conference-Call",
}
def go(kv):
    t,u=kv
    try:
        req=urllib.request.Request(u,headers=HDRS)
        with urllib.request.urlopen(req,timeout=30) as r:
            return t,u,strip(r.read().decode("utf-8","replace"))
    except Exception as e:
        return t,u,f"ERR {type(e).__name__}: {e}"
with ThreadPoolExecutor(max_workers=3) as ex:
    for t,u,txt in ex.map(go,JOBS.items()):
        print(f"\n{'='*72}\n{t} ({len(txt)}B)\n  {u}")
        if txt.startswith("ERR"): print("  ",txt); continue
        seen=set()
        for s in re.split(r"(?<=[.!?])\s+",txt):
            s=s.strip()
            if KEY.search(s) and 25<len(s)<450 and s not in seen:
                seen.add(s); print("   .",s[:320])
                if len(seen)>=12: break
