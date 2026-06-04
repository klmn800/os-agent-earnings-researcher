---
name: parse-big-inbox-json-dont-read
description: Never Read the raw EDGAR *_filings.json / submissions dumps directly — parse with Python; they blow ~25k tokens each for no value
metadata:
  type: feedback
---

Do **not** call the `Read` tool on the big inbox JSON dumps (`*_filings.json`, i.e. EDGAR `data.sec.gov/submissions/CIK*.json` output). Go straight to a Python parse (`json.load` → print the recent `filings.recent.{form,filingDate,reportDate,accessionNumber,primaryDocument}` rows).

**Why:** On 2026-05-28 Ben flagged a 151k-token spend for a 5-symbol session. ~50k of that was two `Read` calls on `orcl_filings.json` and `uec_filings.json` — each is a single ~159k-char line that is 99% accession-number arrays, hits the 25k read cap, and yields nothing usable. I then parsed them with Python anyway, so the reads were pure waste. The actual web research (searches + EDGAR FTS curls + writes) was appropriately scoped.

**How to apply:**
- Inbox `*_filings.json` or any `submissions/CIK*.json` → parse with a Python snippet, print only the latest ~15 filings. Never `Read` it whole.
- The small JSONs are fine to `Read`: EDGAR full-text-search results (`*_search.json`) are tiny (just `hits.total.value` + a few hits).
- Large append-only `memory/research_log.md` (50k+ tokens): use `Read` with `limit`/`offset` to grab only the recent sessions, not the whole file, unless I genuinely need history.
- HTML 8-Ks: prefer `Grep -o` for earnings/Item signals over a full `Read` when I just need to classify the filing.

Related: [[reference-sec-via-curl]] (the curl workflow that produces these JSON dumps), [[feedback-direct-db-query]].
