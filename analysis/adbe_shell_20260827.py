import urllib.request,re
UA={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0 Safari/537.36'}
r=urllib.request.urlopen(urllib.request.Request('https://news.adobe.com/',headers=UA),timeout=30)
x=r.read().decode('utf-8','replace')
print('--- shell len',len(x))
for m in set(re.findall(r'https?://[A-Za-z0-9./_\-]*(?:api|graphql|content|feed|rss|json)[A-Za-z0-9./_\-]*',x)):
    print('  API?',m)
for m in set(re.findall(r'(?:src|href)="([^"]+)"',x)):
    if any(k in m.lower() for k in ('api','json','feed','rss','graphql')): print('  REF ',m)
print('--- head ---'); print(x[:900])
