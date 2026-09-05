import urllib.request, urllib.error, re, html
UA = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0 Safari/537.36"}
def probe(u):
    try:
        r = urllib.request.urlopen(urllib.request.Request(u, headers=UA), timeout=30)
        b = r.read().decode("utf-8", "replace")
        return r.status, len(b), b
    except urllib.error.HTTPError as e:
        return e.code, 0, ""
    except Exception as e:
        return f"ERR {type(e).__name__}", 0, ""
tests = [
    ("REAL   copart newsroom", "https://www.prnewswire.com/news/copart-inc/"),
    ("CONTROL nonsense org  ", "https://www.prnewswire.com/news/zzz-not-a-real-company-xyq/"),
    ("REAL   prn rss        ", "https://www.prnewswire.com/rss/all-news-releases-from-PR-newswire-news.rss"),
]
bodies = {}
for label, u in tests:
    s, n, b = probe(u)
    print(f"{label} -> {s}  {n}B")
    bodies[label.strip()] = b
b = bodies.get("REAL   copart newsroom".strip(), "")
if b:
    txt = html.unescape(re.sub(r"\s+", " ", re.sub(r"<[^>]+>", " ", b)))
    hits = re.findall(r"Copart[^|]{0,110}", txt)[:12]
    for h in hits: print("   ITEM:", h.strip()[:120])
