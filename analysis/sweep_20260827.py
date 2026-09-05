import urllib.request, json, sys
UA={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0 Safari/537.36'}
CIK={'CNM':1856525,'CPRT':900075,'ORCL':1341439,'GME':1326380,'ADBE':796343}
for sym,cik in CIK.items():
    url=f'https://data.sec.gov/submissions/CIK{cik:010d}.json'
    try:
        r=urllib.request.urlopen(urllib.request.Request(url,headers=UA),timeout=30)
        d=json.load(r)['filings']['recent']
        print(f'--- {sym} (CIK {cik}) {d["name"] if "name" in d else ""}')
        for i in range(min(6,len(d['form']))):
            print(f'   {d["filingDate"][i]}  {d["form"][i]:<8} items={d.get("items",[""]*99)[i]!r}  acc={d["acceptanceDateTime"][i]}')
    except Exception as e:
        print(f'--- {sym}: ERROR {e}')
