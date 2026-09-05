import urllib.request,re
UA={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0 Safari/537.36',
    'Accept':'application/rss+xml, application/xml, text/xml, */*'}
for u in ['https://investors.lennar.com/rss/news',
          'https://investors.lennar.com/rss/press-releases',
          'https://investors.lennar.com/rss/news-releases',
          'https://investors.lennar.com/rss/earnings',
          'https://investors.lennar.com/earnings']:
    try:
        r=urllib.request.urlopen(urllib.request.Request(u,headers=UA),timeout=25)
        b=r.read().decode('utf-8','replace')
        print(f"\n=== {u} -> {r.status} {r.geturl()} len={len(b)}")
        print(b[:2500] if '/earnings' not in r.geturl() or u.endswith('/rss/earnings') else '')
        if u.endswith('investors.lennar.com/earnings'):
            txt=re.sub(r'<script.*?</script>','',b,flags=re.S)
            txt=re.sub(r'<[^>]+>',' ',txt); txt=re.sub(r'\s+',' ',txt)
            print(txt[:3000])
    except Exception as e:
        print(f"\n=== {u} ERR {type(e).__name__} {str(e)[:60]}")
