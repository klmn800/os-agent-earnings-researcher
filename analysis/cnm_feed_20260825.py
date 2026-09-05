import urllib.request, urllib.error, ssl
UA={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0 Safari/537.36'}
ctx=ssl.create_default_context(); ctx.check_hostname=False; ctx.verify_mode=ssl.CERT_NONE
urls=[
 "https://ir.coreandmain.com/rss/pressrelease.aspx",
 "https://ir.coreandmain.com/rss/news-releases.xml",
 "https://investors.coreandmain.com/rss/pressrelease.aspx",
 "https://ir.coreandmain.com/zzz-nonsense-control-path",
]
for u in urls:
    try:
        r=urllib.request.urlopen(urllib.request.Request(u,headers=UA),timeout=25,context=ctx)
        b=r.read()
        print(f"--- {u} -> {r.status} {len(b)}B")
        t=b.decode('utf-8','replace')
        print(t[:900].replace('\n',' ')[:900])
    except urllib.error.HTTPError as e:
        print(f"--- {u} -> HTTP {e.code}")
    except Exception as e:
        print(f"--- {u} -> ERR {type(e).__name__}: {e}")
    print()
