import urllib.request, urllib.error, re, socket
UA={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0 Safari/537.36',
    'Accept':'application/rss+xml, application/xml, text/xml, */*'}
HOSTS={
 'FDS':['investor.factset.com','ir.factset.com','investors.factset.com','factset.gcs-web.com'],
 'LEN':['investors.lennar.com','ir.lennar.com','investor.lennar.com','lennar.gcs-web.com'],
 'CNXC':['ir.concentrix.com','investors.concentrix.com','investor.concentrix.com','concentrix.gcs-web.com'],
 'DRI':['investor.darden.com','investors.darden.com','ir.darden.com','darden.gcs-web.com'],
}
PATHS=['/rss/pressrelease.aspx','/rss/news-releases.xml','/rss','/feed/','/news-events/press-releases/rss','/rss/news.xml']
socket.setdefaulttimeout(20)
for sym,hosts in HOSTS.items():
    print(f"\n########## {sym}")
    for h in hosts:
        for p in PATHS:
            u=f"https://{h}{p}"
            try:
                r=urllib.request.urlopen(urllib.request.Request(u,headers=UA))
                b=r.read().decode('utf-8','replace')
            except Exception as e:
                print(f"  {u:70s} ERR {type(e).__name__} {str(e)[:45]}"); continue
            items=re.findall(r'<item>(.*?)</item>',b,re.S)
            print(f"  {u:70s} OK {r.status} final={r.geturl()[:60]} items={len(items)} len={len(b)}")
            for it in items[:12]:
                t=re.search(r'<title>(?:<!\[CDATA\[)?(.*?)(?:\]\]>)?</title>',it,re.S)
                d=re.search(r'<pubDate>(.*?)</pubDate>',it,re.S)
                l=re.search(r'<link>(.*?)</link>',it,re.S)
                print(f"      {(d.group(1)[:22] if d else '?'):24s} | {(t.group(1).strip()[:88] if t else '?')}")
                if t and re.search(r'schedul|conference call|to announce|results|earnings|first quarter|third quarter',t.group(1),re.I) and l:
                    print(f"         -> {l.group(1).strip()[:130]}")
            if items: break
        else:
            continue
        break
