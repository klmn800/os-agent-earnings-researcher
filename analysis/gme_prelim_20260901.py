import urllib.request,re,html
UA={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0 Safari/537.36'}
x=urllib.request.urlopen(urllib.request.Request('https://news.gamestop.com/rss/pressrelease.aspx',headers=UA),timeout=45).read().decode('utf-8','replace')
for it in re.findall(r'<item>(.*?)</item>',x,re.S)[:2]:
    t=re.search(r'<title>(?:<!\[CDATA\[)?(.*?)(?:\]\]>)?</title>',it,re.S).group(1).strip()
    d=re.search(r'<description>(?:<!\[CDATA\[)?(.*?)(?:\]\]>)?</description>',it,re.S)
    body=re.sub(r'<[^>]+>',' ',d.group(1)) if d else '(no description)'
    body=html.unescape(re.sub(r'\s+',' ',body)).strip()
    print('='*100); print(t); print('-'*100); print(body[:3500])
