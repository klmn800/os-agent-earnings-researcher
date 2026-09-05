import json,urllib.request
UA={'User-Agent':'options-scanner-earnings-researcher klmn800alerts@gmail.com'}
d=json.load(urllib.request.urlopen(urllib.request.Request("https://data.sec.gov/submissions/CIK0001856525.json",headers=UA),timeout=30))
r=d['filings']['recent']
print("--- all 8-Ks with 2.02 (recent file) ---")
for form,fd,acc,doc,items,adt in zip(r['form'],r['filingDate'],r['accessionNumber'],r['primaryDocument'],r['items'],r['acceptanceDateTime']):
    if form.startswith('8-K') and '2.02' in items:
        print(f"  {fd}  accepted {adt}  items={items}  {acc}  {doc}")
print()
print("older files:", [f['name'] for f in d['filings'].get('files',[])])
