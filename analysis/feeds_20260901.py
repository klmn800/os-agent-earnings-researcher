import urllib.request,re
UA={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0 Safari/537.36'}
F={'ORCL':'https://investor.oracle.com/rss/pressrelease.aspx','GME':'https://news.gamestop.com/rss/pressrelease.aspx'}
for sym,u in F.items():
    try:
        r=urllib.request.urlopen(urllib.request.Request(u,headers=UA),timeout=45)
        x=r.read().decode('utf-8','replace')
        print(f'--- {sym} HTTP {r.status} len={len(x)}')
        for it in re.findall(r'<item>(.*?)</item>',x,re.S)[:10]:
            t=re.search(r'<title>(?:<!\[CDATA\[)?(.*?)(?:\]\]>)?</title>',it,re.S)
            p=re.search(r'<pubDate>(.*?)</pubDate>',it,re.S)
            l=re.search(r'<link>(?:<!\[CDATA\[)?(.*?)(?:\]\]>)?</link>',it,re.S)
            print(f'   {p.group(1).strip() if p else "?":<34} {t.group(1).strip()[:100] if t else "?"}')
            if l: print(f'      {l.group(1).strip()[:135]}')
    except Exception as e:
        print(f'--- {sym}: ERROR {type(e).__name__} {e}')
