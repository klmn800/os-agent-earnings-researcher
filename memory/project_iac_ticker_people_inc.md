---
name: IAC ticker is now PPLI (People Inc.)
description: IAC Inc. renamed to People Inc. and its Nasdaq ticker changed IAC -> PPLI; the "IAC (N/A)" dispute row is a dead-ticker phantom
metadata:
  type: project
---

CIK **1800227** now reports as **People Inc.** with `tickers: ["PPLI"]` on Nasdaq. **`IAC` no longer resolves in SEC's `company_tickers.json`.** The rename was flagged as "expected by its Q2 earnings in August 2026," and by 2026-07-31 SEC had already switched the ticker over.

The dispute list surfaced this as **`IAC (N/A)`** on 2026-07-31 — and that `N/A` company name is the same dead-ticker signature described in [[reference_ma_phantom_earnings]]. `earnings_upcoming` still carried an `IAC` row (2026-08-03, Unknown) and **no `PPLI` row**, so the live company's date was tracked under a symbol that no longer trades.

## ✅ Resolved 2026-07-31 — renamed in the DBs

Ben approved the rename; `tools/symbol_lifecycle.py --rename IAC PPLI --no-interaction` moved **3,960 rows across 3 databases** (datalake, performance, `sector_archive/communication_services`) and logged a `renamed` lifecycle event. Zero `IAC` rows remain. Follow-ups done in the same pass: `company_name` `N/A` → **People Inc.**, `ir_earnings_url` → the new host, and the date confirmed **2026-08-03 amc** (People Incorporated's own PR: results after the close Mon Aug 3, call Tue Aug 4 8:30am ET — matching the `+364d` prediction exactly).

**`tools/symbol_lifecycle.py --rename OLD NEW` is the right tool for this class of problem** — it auto-discovers every table with a `symbol`/`primary_symbol`/`peer_symbol` column, so nothing is missed, and it refuses to clobber an existing target symbol without `--force`. Its own `--help` uses `PSTG P` as the example. Run it with `--no-interaction` (prompts otherwise, which won't work headless).

**Why:** this is the second rename of its kind after [[P ticker = Pure Storage rebranded as Everpure]], and it fails differently from a delisting — the company keeps filing and keeps reporting, so nothing looks obviously broken. The research succeeds, the write lands on a dead symbol, and the scanner never sees it.

**How to apply:**
- **A missing CIK in `company_tickers.json` is not proof of delisting — check for a rename first.** Search the SEC map by CIK/company name rather than by ticker; `submissions/CIK…json` returns the *current* `tickers` array, which is the authoritative answer.
- Do **not** stamp `earnings_confirm.py` on the dead ticker — rename first, then confirm. Renaming also *unblocks* the research: searching the new name ("People Incorporated") surfaced the Q2 PR immediately, where "IAC" had returned nothing but aggregator noise.
- **A stale `company_name = 'N/A'` in `symbol_metadata` is the tell.** It's what made this look like a phantom for four straight sessions. Fix it as part of any rename, or the next session re-diagnoses it from scratch.
- PPLI cadence: reports **amc**, furnish 16:0x–16:1x ET, Monday or Tuesday — Q2-25 2025-08-04 (Mon), Q3-25 11-03 (Mon), Q4-25 2026-02-03 (Tue), Q1-26 2026-05-04 (Mon), Q2-26 **2026-08-03 (Mon), company-confirmed**. Call is the **next morning, 8:30am ET** — so don't read the call date (Aug 4) as the release date. ⚠ its 2026-04-28 08:25 ET Item 2.02 was a restructuring 8-K (items `2.02,2.05,5.02,7.01`), not earnings — exclude it from furnish-time majorities.
- IR: **`ir.people-incorporated.com/quarterly-results`** is canonical; `ir.iac.com/quarterly-results` **301-redirects** there. ⚠ the new host returns nothing to curl/WebFetch (HTTP 000 — WAF or dead origin), so cache it per [[IR URL caching — SPAs and per-quarter deep links]] and get the actual PR text from PR Newswire. Same shape as `purestorage.com` → `everpuredata.com` in [[P ticker = Pure Storage rebranded as Everpure]].

Related: [[reference_ma_phantom_earnings]], [[company-earnings-cadence]], [[sec-8k-acceptance-time-as-timing-source]].
