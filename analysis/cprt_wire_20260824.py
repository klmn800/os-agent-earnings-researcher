import json, urllib.request, re, html
UA = {"User-Agent": "options-scanner-earnings-researcher klmn800alerts@gmail.com"}
def get(u):
    return urllib.request.urlopen(urllib.request.Request(u, headers=UA), timeout=30).read().decode("utf-8","replace")
# Q4 FY25 results 8-K (matching quarter) + Q3 FY26 results 8-K
for label, acc in [("Q4 FY25 results 2025-09-04", "0000900075-25-000017"),
                   ("Q3 FY26 results 2026-05-21", "0001193125-26-234447")]:
    n = acc.replace("-", "")
    idx = json.loads(get(f"https://www.sec.gov/Archives/edgar/data/900075/{n}/index.json"))
    ex = [i["name"] for i in idx["directory"]["item"] if re.search(r"ex.?99", i["name"], re.I) and i["name"].endswith(".htm")]
    print(f"### {label}  exhibits={ex}")
    for e in ex[:1]:
        t = get(f"https://www.sec.gov/Archives/edgar/data/900075/{n}/{e}")
        b = html.unescape(re.sub(r"\s+", " ", re.sub(r"<[^>]+>", " ", t))).strip()
        print("   ", b[:420])
        for m in re.finditer(r"(PRNewswire|BUSINESS WIRE|Business Wire|GLOBE NEWSWIRE)", b, re.I):
            print("    WIRE HIT:", m.group(0)); break
    print()
