import re, sys, urllib.request
from concurrent.futures import ThreadPoolExecutor
sys.stdout.reconfigure(encoding="utf-8")
UA = ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
      "(KHTML, like Gecko) Chrome/126.0 Safari/537.36")
HDRS = {"User-Agent": UA, "Accept": "*/*"}
def strip(h):
    h = re.sub(r"(?is)<(script|style|nav|header|footer).*?</\1>", " ", h)
    h = re.sub(r"(?s)<[^>]+>", " ", h)
    for a,b in [("&nbsp;"," "),("&amp;","&"),("&#39;","'"),("&rsquo;","'"),
                ("&quot;",'"'),("&ldquo;",'"'),("&rdquo;",'"'),("&mdash;","--")]:
        h = h.replace(a,b)
    return re.sub(r"\s+"," ",h)
def go(kv):
    tag, url = kv
    try:
        req = urllib.request.Request(url, headers=HDRS)
        with urllib.request.urlopen(req, timeout=30) as r:
            return tag, url, strip(r.read().decode("utf-8","replace")), r.geturl()
    except Exception as e:
        return tag, url, f"ERR {type(e).__name__}: {e}", url
JOBS = {
 "CIEN-PR": "https://investor.ciena.com/news/news-details/2026/Ciena-Announces-Reporting-Date-and-Web-Broadcast-for-Fiscal-Third-Quarter-2026-Results/default.aspx",
 "PATH-news": "https://ir.uipath.com/news",
 "PATH-cached": "https://ir.uipath.com/news/detail/445/uipath-announces-first-quarter-fiscal-2027-financial-results-conference-call",
 "GOLD-ir": "https://ir.gold.com/",
}
with ThreadPoolExecutor(max_workers=4) as ex:
    for tag, url, txt, final in ex.map(go, JOBS.items()):
        print(f"\n{'='*72}\n{tag}  ({len(txt)}B) final={final}\n{url}")
        if tag == "CIEN-PR":
            i = txt.find("HANOVER")
            print(txt[i:i+900] if i>0 else txt[:900])
        elif tag.startswith("PATH"):
            for m in re.finditer(r"[^.]{0,200}(?:financial results|conference call|second quarter fiscal 2027|Sept)[^.]{0,200}\.", txt, re.I):
                print("   .", m.group(0).strip()[:300])
        else:
            print(txt[:1200])
