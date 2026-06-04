---
name: reference-sec-via-curl
description: SEC.gov is reachable via Bash+curl (with UA) but not via WebFetch — useful for 8-Ks, filing lists, and EDGAR full-text search
metadata:
  type: reference
---

`WebFetch` to `sec.gov` returns HTTP 403. `Bash` + `curl` succeeds with a proper User-Agent.

**Working command shape:**
```bash
curl -sL -A "options-scanner-earnings-researcher klmn800alerts@gmail.com" "https://www.sec.gov/Archives/edgar/data/<CIK>/<accession_nodash>/<doc>.htm" -o "<workspace>/inbox/<file>.html"
```

The User-Agent string must include a contact email per SEC's fair-access policy. Use the project email `klmn800alerts@gmail.com` (defined in CLAUDE.md → "External Service Contact"), not Ben's personal email.

**Three SEC endpoints I use routinely:**

1. **Recent filings list per CIK** (JSON):
   `https://data.sec.gov/submissions/CIK<10-digit-zero-padded>.json`
   Returns `filings.recent.{form,filingDate,accessionNumber,primaryDocument,...}` as parallel arrays. Parse with Python.

2. **Filing body** (HTML):
   `https://www.sec.gov/Archives/edgar/data/<cik-no-zeros>/<accession-no-dashes>/<primaryDocument>`
   Note the path expects CIK with leading zeros stripped, accession with dashes removed. May 301-redirect.

3. **EDGAR full-text search** (JSON):
   `https://efts.sec.gov/LATEST/search-index?q=<phrase>&forms=8-K&ciks=<cik>&dateRange=custom&startdt=YYYY-MM-DD&enddt=YYYY-MM-DD`
   Returns `hits.total.value` and `hits.hits[*]._source.{file_date,adsh,...}`. Useful for "has Company X filed any earnings-date 8-K in date range" — `total.value == 0` is an authoritative "no announcement yet."

**Bash gotcha on Windows:** Python under Bash can't write to `/tmp` — use absolute Windows paths under the project workspace (e.g. `E:/options_scanner/agents/earnings_researcher/inbox/`).

**Why this matters for the earnings-research workflow:**
- SEC 8-K body text is the gold-standard source for "Sets the Date" / "to Announce Q… Results" press releases (Exhibit 99.1).
- EDGAR full-text search distinguishes "company hasn't filed yet" from "I just can't find the filing" — eliminating one source of false-skip ambiguity.
- Wire-service mirrors (BusinessWire, GlobeNewsWire, PR Newswire) remain useful as fallbacks when company IR is SPA-rendered (and SEC may be slower to index the 8-K than the wire is to publish).

Related: [[feedback-ir-url-caching-spa]] (SPAs are SEC's main workaround use case), [[feedback-direct-db-query]].
