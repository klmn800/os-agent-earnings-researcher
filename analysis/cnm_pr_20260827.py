import urllib.request,re,html
UA={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0 Safari/537.36'}
u='https://coreandmain.com/news/core-and-main-to-announce-fiscal-2026-second-quarter-results/'
r=urllib.request.urlopen(urllib.request.Request(u,headers=UA),timeout=40)
x=r.read().decode('utf-8','replace')
print('HTTP',r.status,'len',len(x))
b=re.sub(r'<script.*?</script>|<style.*?</style>','',x,flags=re.S)
b=html.unescape(re.sub(r'<[^>]+>',' ',b))
b=re.sub(r'\s+',' ',b)
i=b.find('ST. LOUIS')
print(b[max(0,i-200):i+1800] if i>=0 else b[:2500])
