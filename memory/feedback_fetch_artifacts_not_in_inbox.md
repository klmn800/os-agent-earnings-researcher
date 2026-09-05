---
name: feedback-fetch-artifacts-not-in-inbox
description: Write curl/urllib scratch output to inbox/fetch/, never inbox/ itself — the context hook flags loose inbox files as unprocessed handoff notes, and 18 spent HTML blobs accumulated there
metadata:
  type: feedback
---

`hooks/inject_context.py` → `check_inbox()` lists **every loose file directly in
`inbox/`** (excluding `README.md` / `.gitkeep`) as *"unprocessed file(s) — read
each, integrate into memory, then move to `inbox/processed/`."* It does **not**
descend into subdirectories.

[[reference_sec_via_curl]] tells me to write curl output under the project
workspace because Python-under-Bash can't write to `/tmp` on Windows — and the
path it gives is `inbox/`. **Those two conventions collide.** Every `curl -o
inbox/foo.html` leaves a file that the next session's hook reports as an
unread message from Ben or another agent.

**On 2026-09-03 the backlog was 18 files** (`st_CPRT.html`, `ctas_gcs.html`,
`orcl_rss_20260902.xml`, …) — all spent fetch artifacts from the 09-02 session,
all already fully written up in `research_log.md`. Zero were handoff notes. The
notice had been crying wolf, which is the expensive part: a real note from Ben
would have been buried in a list of my own garbage.

**How to apply:** scratch fetch output goes to **`inbox/fetch/`**. It satisfies
the Windows-writable-path requirement, and the hook ignores it because it is a
subdirectory. Reserve `inbox/` itself for actual inbound notes, and keep
`inbox/processed/` as the historical record of *notes* — don't dilute it with
HTML blobs.

**Don't "integrate" a fetch artifact.** If an inbox file is an `.html`/`.xml`/
`.json` blob named after a symbol, it is my own scratch, not a message: check
whether the research log already covers that session, then file it under
`inbox/fetch/` and move on. Only `.md` files matching the README's
`YYYY-MM-DD_short-kebab-topic.md` pattern are real handoffs.

`inbox/fetch/` is disposable — safe for a future maintenance session to prune by
age. Related: [[reference_sec_via_curl]], [[reference-stocktitan-jsonld-discovery]].
