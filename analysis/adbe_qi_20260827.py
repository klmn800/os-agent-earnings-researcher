import urllib.request,urllib.error,json
UA={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0 Safari/537.36'}
C=['https://news.adobe.com/query-index.json',
   'https://news.adobe.com/news/query-index.json',
   'https://news.adobe.com/zz-nonsense-control-9931.json']  # CONTROL
for u in C:
    tag=' <== CONTROL' if 'nonsense' in u else ''
    try:
        r=urllib.request.urlopen(urllib.request.Request(u,headers=UA),timeout=30)
        d=r.read()
        print(f'{r.status} len={len(d)} {u}{tag}')
        if 'nonsense' not in u and len(d)>100:
            try:
                j=json.loads(d); print('   keys',list(j)[:8],'total',j.get('total'),'count',len(j.get('data',[])))
            except Exception as e: print('   notjson',d[:120])
    except urllib.error.HTTPError as e: print(f'{e.code} {u}{tag}')
    except Exception as e: print(f'ERR {type(e).__name__} {u}{tag}')
