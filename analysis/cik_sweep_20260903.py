import json,urllib.request
UA={'User-Agent':'options-scanner-earnings-researcher klmn800alerts@gmail.com'}
def get(u):
    return json.load(urllib.request.urlopen(urllib.request.Request(u,headers=UA),timeout=45))
want={'FDS','CNXC','DRI','LEN'}
t=get("https://www.sec.gov/files/company_tickers.json")
m={}
for v in t.values():
    if v['ticker'] in want: m[v['ticker']]=str(v['cik_str']).zfill(10)
print(m)
for sym in ['FDS','LEN','CNXC','DRI']:
    cik=m.get(sym)
    if not cik: print(sym,'NO CIK'); continue
    d=get(f"https://data.sec.gov/submissions/CIK{cik}.json")
    r=d['filings']['recent']
    print(f"\n=== {sym} ({d['name']}) CIK {cik} FYE={d.get('fiscalYearEnd')}")
    n=0
    for form,fd,acc,doc,items in zip(r['form'],r['filingDate'],r['accessionNumber'],r['primaryDocument'],r.get('items',['']*len(r['form']))):
        if fd < '2026-07-15': break
        print(f"  {fd}  {form:10s} items={items:14s} {acc} {doc}")
        n+=1
        if n>18: break
