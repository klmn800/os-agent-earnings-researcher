import urllib.request,urllib.error
UA={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0 Safari/537.36'}
C=[
 'https://news.adobe.com/rss/pressrelease.aspx',
 'https://news.adobe.com/feed',
 'https://news.adobe.com/rss',
 'https://news.adobe.com/feed/rss',
 'https://news.adobe.com/news/rss',
 'https://news.adobe.com/zz-nonsense-control-xyz-9931',   # CONTROL
 'https://news.adobe.com/',
 'https://www.adobe.com/investor-relations/events.html',
 'https://www.adobe.com/investor-relations/zz-nonsense-control-9931.html',  # CONTROL
]
for u in C:
    tag=' <== CONTROL' if 'nonsense' in u else ''
    try:
        r=urllib.request.urlopen(urllib.request.Request(u,headers=UA),timeout=25)
        d=r.read()
        print(f'{r.status}  len={len(d):>8}  {u}{tag}')
    except urllib.error.HTTPError as e:
        print(f'{e.code}  {"":>13} {u}{tag}')
    except Exception as e:
        print(f'ERR  {type(e).__name__:<18} {u}{tag}')
