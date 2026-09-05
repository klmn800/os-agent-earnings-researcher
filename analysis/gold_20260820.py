import re, sys, urllib.request
sys.stdout.reconfigure(encoding="utf-8")
UA=("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
    "(KHTML, like Gecko) Chrome/126.0 Safari/537.36")
def get(u):
    r=urllib.request.Request(u,headers={"User-Agent":UA,"Accept":"*/*"})
    with urllib.request.urlopen(r,timeout=30) as f: return f.read().decode("utf-8","replace"), f.geturl()
def strip(h):
    h=re.sub(r"(?is)<(script|style|nav|header|footer).*?</\1>"," ",h)
    h=re.sub(r"(?s)<[^>]+>"," ",h)
    for a,b in [("&nbsp;"," "),("&amp;","&"),("&#39;","'"),("&rsquo;","'"),("&quot;",'"')]:
        h=h.replace(a,b)
    return re.sub(r"\s+"," ",h)
# find the news-release link for the 08-19 "Sets Fiscal Fourth Quarter" PR
raw,_ = get("https://ir.gold.com/")
links=set(re.findall(r'href="([^"]*(?:news|press|release)[^"]*)"',raw,re.I))
print("candidate links:")
for l in sorted(links)[:40]: print("  ",l)
