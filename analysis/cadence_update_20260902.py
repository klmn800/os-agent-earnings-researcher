import io

p = 'memory/reference_company_cadence.md'
lines = io.open(p, encoding='utf-8').read().split('\n')

CPRT_ADD = (
    " ⚠⚠ **2026-09-02 — CONFIRMED 2026-09-10 `amc`, and three parts of this row were wrong.** "
    "The advance PR *\"Copart, Inc. to Release Fourth Quarter Fiscal 2026 Results\"* published **2026-09-01 at 10:34 ET**: "
    "*\"will release earnings for the fourth quarter of fiscal 2026 **after 4:00 p.m. Eastern Time** (3:00 p.m. Central) "
    "**on Thursday, September 10, 2026**,\"* call **5:30 p.m. ET**, permalink `businesswire.com/news/home/20260901213040/en/`. "
    "**(1) The advance PR IS BusinessWire** — dateline `DALLAS --(BUSINESS WIRE)--`. The 08-24 ⚠⚠ correction "
    "(*\"the wire is PRNewswire, not BusinessWire\"*) was measured on the **board-addition** PR and does **not** transfer: "
    "Copart uses **PRNewswire for corporate news and BusinessWire for the earnings advance**, and its *results* releases still "
    "carry no wire at all. **(2) The Q4 advance lead is 9d, not 7–8d** — 09-01 → 09-10. The 09-01 session's "
    "Q4-scoped band (FY22 7d, FY23 8d, FY24 8d, FY25 8d) is now **7–9d**; gate off the **9d**. **(3) It does NOT publish "
    "after 16:00 ET** — every prior version of this row said post-close, which is why sessions only ever read it the next "
    "morning. It published **10:34 ET**, i.e. *during* the session day, so on a due date it is worth a second read that afternoon. "
    "⭐ **How it was found: `stocktitan.net/news/CPRT/` JSON-LD** — with no reachable Copart host in existence, the "
    "mirror's `hasPart` array (10 headlines + UTC timestamps + article URLs) is the **primary discovery channel**, not merely an "
    "absence cross-check. Send `curl --compressed` or you get raw brotli that looks like a bot wall. ✅ The `amc` lock and the "
    "\"no advance 8-K on EDGAR\" fact both held exactly as recorded."
)

GIS_ADD = (
    " ⭐ **2026-09-02 — CONFIRMED Q1 FY27 = 2026-09-23 `bmo`; General Mills issues a clean, early advance PR and this row "
    "should be gated off it.** Title: *\"General Mills to Webcast Fiscal 2027 First Quarter Earnings Results on **September 23, 2026**\"* "
    "— the **date is in the headline**, published **2026-08-26 08:00 ET** on BusinessWire = a **28d lead**, by far the roomiest in "
    "this table. Body: *\"plans to report results for its fiscal 2027 first quarter on September 23, 2026. A press release, pre-recorded "
    "management remarks and supporting slides will be **issued that morning** followed by a webcasted question and answer session on the "
    "results at **8 a.m. CT**.\"* → `bmo` confirmed a second way (release precedes a 9:00 ET Q&A). Permalink "
    "`businesswire.com/news/home/20260826734008/en/`. ⚠⚠ **Do NOT extrapolate GIS from Item 2.02 history — it fails.** "
    "Q1-only furnishes are **2025-09-17 (Wed), 2024-09-18 (Wed), 2023-09-20 (Wed)**, a clean one-day-earlier-per-year walk that predicts "
    "**09-16** — **a full week off** the company's own announced 09-23. A `+364d` argument here would have produced a confident wrong "
    "answer. The lead is long enough that the PR is essentially always out before the dispute is: **check the wire, never the pattern.** "
    "⚠ finnhub said **09-15** (wrong, as in June when it said 06-23). IR feed `investors.generalmills.com/press-releases/default.aspx` "
    "returns 200 but did **not** contain the advance in its first page of text — `stocktitan.net/news/GIS/` did, in one fetch."
)

ORCL_ADD = (
    " ⚠ **2026-09-01 read repeated 09-02 and it was decisive: 09-08 is ELIMINATED.** Feed live (200, 10 items) and newest is "
    "**still the 06-10 Q4 results PR**; EDGAR shows **no filing of any kind since 2026-07-28**. Absence through **09-01 16:01 ET** plus "
    "the **7d minimum** lead ⇒ release **≥ 09-09**, which kills the `+364d`-derived **09-08 (Tue)** candidate raised on 08-28. "
    "**DB's 09-10 (Thu) is now the only surviving in-band date**, and finnhub's **09-14 (Mon)** would require the PR on 09-05..09-07 with "
    "**09-07 = Labor Day**. Still **cadence, not a company source ⇒ no lock**. PR due **09-02/09-03**, posts ~16:01 ET ⇒ next "
    "read **09-03**."
)

CTAS_ROW = (
    "| CTAS | Cintas / Q1 FY27 (Aug-31 qtr-end); FY ends May-31 | **bmo (DB says `amc` — WRONG)** | **~14d (1 observation — needs a 2nd)** | "
    "CIK 723254. ⚠⚠ **The stored time `amc` is provably wrong and no dispute will ever surface it** — CTAS disputes come in as "
    "`date_disagreement`, so the time is never questioned. Cintas is **bmo, 6/6 quarters**: Item 2.02 acceptance times are **08:31–08:34 ET** "
    "(2026-07-15 08:31:16, 2026-03-25 08:31:08, 2025-12-18 08:31:05, 2025-09-24 08:34:41, 2025-07-17 08:31:26, 2024-09-25 08:30:58), the release "
    "opens *\"today reported results\"*, and it names a **10:00 a.m. ET** webcast. ✅ **An advance PR exists**: "
    "*\"Cintas Corporation Announces Webcast for \\<n\\> Quarter Fiscal Year \\<yr\\> Results\"* — Q4 FY26 published **2026-07-01 13:29 ET** "
    "for a **2026-07-15** release = **14d**. ⚠ That is **one observation**; per the WSM count-the-observations rule, do not trust it as a band "
    "until a 2nd is measured (next chance: the Q1 FY27 advance, expected ~09-09). It is **not on EDGAR** (no 7.01/8.01 8-K around 07-01). "
    "⚠⚠ **No first-party IR host exists**: `investors.cintas.com` and `ir.cintas.com` are **NXDOMAIN**, and `cintas.gcs-web.com` resolves "
    "but returns **403 Access Denied on every path** including `/` (Akamai) — an honest 403, not a 200-for-everything wall, so it cannot "
    "manufacture a false positive, but it is unusable. Channel is **BusinessWire via `stocktitan.net/news/CTAS/`**. "
    "**Q1-only Item 2.02 dates: 2025-09-24 (Wed), 2024-09-25 (Wed), 2023-09-26 (Tue)** — one day earlier each year ⇒ **2026-09-23 (Wed) = DB**; "
    "finnhub's **09-30** sits a full week outside that band. | `stocktitan.net/news/CTAS/` (JSON-LD) + EDGAR submissions API. No IR host. |"
)

for i, ln in enumerate(lines):
    if ln.startswith('| CPRT | Copart'):
        parts = ln.rsplit('|', 2)
        lines[i] = parts[0].rstrip() + CPRT_ADD + ' |' + parts[1] + '|' + parts[2]
    elif ln.startswith('| GIS | General Mills'):
        parts = ln.rsplit('|', 2)
        lines[i] = parts[0].rstrip() + GIS_ADD + ' |' + parts[1] + '|' + parts[2]
    elif ln.startswith('| ORCL | Oracle'):
        parts = ln.rsplit('|', 2)
        lines[i] = parts[0].rstrip() + ORCL_ADD + ' |' + parts[1] + '|' + parts[2]

# insert CTAS row after CPRT (alphabetical neighbourhood)
for i, ln in enumerate(lines):
    if ln.startswith('| CPRT | Copart'):
        lines.insert(i + 1, CTAS_ROW)
        break

io.open(p, 'w', encoding='utf-8').write('\n'.join(lines))
print('cadence updated: CPRT/GIS/ORCL amended, CTAS row added')
