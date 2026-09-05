import json,urllib.request
UA={'User-Agent':'options-scanner-earnings-researcher klmn800alerts@gmail.com'}
for sym,cik in [('CNM','0001856525'),('CPRT','0000900075'),('ORCL','0001341439'),('GME','0001326380')]:
    u=f"https://data.sec.gov/submissions/CIK{cik}.json"
    d=json.load(urllib.request.urlopen(urllib.request.Request(u,headers=UA),timeout=30))
    r=d['filings']['recent']
    print(f"=== {sym} ({d['name']}) fiscal-year-end {d.get('fiscalYearEnd')}")
    n=0
    for form,fd,acc,doc,items in zip(r['form'],r['filingDate'],r['accessionNumber'],r['primaryDocument'],r.get('items',['']*len(r['form']))):
        if fd < '2026-07-01': break
        print(f"  {fd}  {form:8s} items={items:12s} {acc} {doc}")
        n+=1
        if n>14: break
    print()
