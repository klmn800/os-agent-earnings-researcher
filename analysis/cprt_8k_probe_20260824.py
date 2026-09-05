import json, urllib.request, re
UA = {"User-Agent": "options-scanner-earnings-researcher klmn800alerts@gmail.com"}
def get(u):
    return urllib.request.urlopen(urllib.request.Request(u, headers=UA), timeout=30).read().decode("utf-8","replace")
d = json.loads(get("https://data.sec.gov/submissions/CIK0000900075.json"))
r = d["filings"]["recent"]
for form, fd, acc, doc in zip(r["form"], r["filingDate"], r["accessionNumber"], r["primaryDocument"]):
    if form.startswith("8-K") and fd >= "2026-08-01":
        print("###", form, fd, acc, doc)
        idx = get(f"https://www.sec.gov/Archives/edgar/data/900075/{acc.replace('-','')}/index.json")
        for it in json.loads(idx)["directory"]["item"]:
            print("    ", it["name"], it["size"])
