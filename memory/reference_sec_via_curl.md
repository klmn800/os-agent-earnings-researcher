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

**Bash gotcha on Windows:** Python under Bash can't write to `/tmp` — use absolute Windows paths under the project workspace — **write to `inbox/fetch/`, NOT `inbox/` itself**, or the context hook reports the scratch file as an unprocessed handoff note next session (see [[feedback-fetch-artifacts-not-in-inbox]]).

⭐ **Endpoint 1 is the best opening tripwire, and it beats a feed read for the "has anything happened at all" question.**
One call per CIK, no host discovery, no RSS-path guessing — and critically **a bot wall cannot fake it**, unlike the
`200-for-every-path` hosts that silently invert slug probes (Copart). It also answers questions a feed cannot: on 2026-08-24
it proved Copart's advance scheduling PR is **not an EDGAR document at all** (four known advance-PR dates, zero 8-Ks),
which converted a months-old assumed gate into a verified one. Sweep the surfaced CIKs with it first, then spend IR-feed
reads only on symbols inside their announcement windows.

⚠ `index.json` per filing (`/Archives/edgar/data/<cik>/<accession_nodash>/index.json`) lists every exhibit with sizes —
cheaper than fetching the 8-K body when you only need to know whether an **Ex-99.1 press release** is attached.
The Ex-99.1 dateline also names the **wire service**, which is the reliable way to learn a company's actual wire
(Copart's said `/PRNewswire/` where the cadence table had claimed BusinessWire).

**Why this matters for the earnings-research workflow:**
- SEC 8-K body text is the gold-standard source for "Sets the Date" / "to Announce Q… Results" press releases (Exhibit 99.1).
- EDGAR full-text search distinguishes "company hasn't filed yet" from "I just can't find the filing" — eliminating one source of false-skip ambiguity.
- Wire-service mirrors (BusinessWire, GlobeNewsWire, PR Newswire) remain useful as fallbacks when company IR is SPA-rendered (and SEC may be slower to index the 8-K than the wire is to publish).

Related: [[feedback-ir-url-caching-spa]] (SPAs are SEC's main workaround use case), [[feedback-direct-db-query]].
