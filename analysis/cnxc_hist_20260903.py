import json,urllib.request
UA={'User-Agent':'options-scanner-earnings-researcher klmn800alerts@gmail.com'}
d=json.load(urllib.request.urlopen(urllib.request.Request("https://data.sec.gov/submissions/CIK0001803599.json",headers=UA),timeout=45))
r=d['filings']['recent']
print("CNXC 8-K item 2.02 (results) history:")
for form,fd,acc,items in zip(r['form'],r['filingDate'],r['accessionNumber'],r['items']):
    if form=='8-K' and '2.02' in items:
        print(f"  {fd}  items={items}  {acc}")
