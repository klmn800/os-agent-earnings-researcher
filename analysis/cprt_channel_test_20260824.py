import json, urllib.request, re, html
UA = {"User-Agent": "options-scanner-earnings-researcher klmn800alerts@gmail.com"}
def get(u):
    return urllib.request.urlopen(urllib.request.Request(u, headers=UA), timeout=30).read().decode("utf-8","replace")
d = json.loads(get("https://data.sec.gov/submissions/CIK0000900075.json"))
r = d["filings"]["recent"]
print("--- ALL CPRT 8-Ks, last ~2y (form, filed, accepted, items) ---")
for form, fd, ad, acc, items in zip(r["form"], r["filingDate"], r["acceptanceDateTime"], r["accessionNumber"], r["items"]):
    if form.startswith("8-K") and fd >= "2024-08-01":
        print(f"  {form:6} {fd}  {ad}  items={items}  {acc}")
print()
print("--- Known advance-PR dates from cadence table: 2025-08-27, 2025-11-11, 2026-02-11, 2026-05-13 ---")
print()
txt = get("https://www.sec.gov/Archives/edgar/data/900075/000119312526354640/d77107dex991.htm")
body = re.sub(r"<[^>]+>", " ", txt)
body = html.unescape(re.sub(r"\s+", " ", body)).strip()
print("--- 2026-08-18 Ex-99.1 (first 900 chars) ---")
print(body[:900])
