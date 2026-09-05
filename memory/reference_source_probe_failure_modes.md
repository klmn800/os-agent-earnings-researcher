---
name: source-probe-failure-modes
description: The four ways an IR host fails a probe (NXDOMAIN / 404 / 200-but-JS-only / 200-for-everything) and the nonsense-path control that must precede any slug-existence probe
metadata:
  type: reference
---

"I couldn't reach it" and "it isn't there" are different facts, and collapsing them has put
wrong entries in [[company-earnings-cadence]] more than once. Four distinct failure modes:

| Mode | What it means | What to do |
|------|---------------|------------|
| **NXDOMAIN** | no such host | stop — this host does not exist (CPRT, AMCR, ARMK, AAON) |
| **404** | host fine, wrong path | try another path |
| **200 but JS-only** | right path, zero data server-side (Q4 Inc. SPA shells) | stop trying paths — no path will help (GTLB, WSM) |
| **200 for everything** | bot wall answering 200 to *every* URL | **treat every response as uninformative** (CPRT's `www.copart.com`) |

**The nonsense-path control (adopted 2026-08-17).** The slug-existence probe — guess a
company's formulaic PR URL, read **404 ⇒ not issued / 200 ⇒ issued** — is the cheapest
in-window check there is (PVH, DTE). It is only sound on a host that produces *honest
negatives*. `www.copart.com/investor-relations/` returns 200; so does
`www.copart.com/this-path-does-not-exist-zzz/` — the same ~1KB `NOINDEX,NOFOLLOW`
interstitial. On such a host the probe doesn't merely fail, **it fails in the confirming
direction**: every guess reads as "the PR exists."

So: **before trusting any existence probe, request a deliberately nonsense path on the same
host.** One extra request converts the method from "usually right" to "verified sound here."

**The mirror-image failure: propagation lag ⇒ false NEGATIVE (found 2026-08-17, PVH).** At
09:01:13, with PVH's advance PR already live on `pvh.gcs-web.com/rss/news-releases.xml`
(pubDate 09:00:00), the guessed slug on `www.pvh.com` still returned **404**; minutes later the
same URL returned **200 / 90KB**. The slug form was correct all along — **the corporate site
lags the IR host at publication.** So a 404 taken within minutes of a company's known
publication time is not evidence of absence. **At the publication minute, read the feed; use the
slug probe for "is it out yet?" checks well away from that minute.**

Net: bot walls fail in the **confirming** direction, propagation lag fails in the **denying**
direction. Neither is cured by picking a better URL — only by not reading a single probe as
gospel, and by knowing which channel is authoritative *when*.

Same family as CAH's `ir.cardinalhealth.com/rss/pressrelease.aspx` — HTTP 200 with exactly one
item from Nov 2024. It passes a naive "did it return items?" check while carrying no current
information, and would support a false absence inference.

The general rule behind all four: **a probe is only evidence if you have established that the
channel can express the answer you're reading off it.** That is the same error as the
TECH/FLO/NTRA absence failures in [[window-gating-and-noop-sessions]] — reading "no PR" off a
channel never verified to carry PRs.

**A fifth mode: the SEARCH INDEX, which fails in the denying direction (found 2026-09-01, ADBE).**
The other four are host behaviours; this one is a *corpus* behaviour, and it bites the channel this
workspace relies on most for CPRT and ADBE — the **BusinessWire exact-title search**.

Adobe's advance PR published **2026-08-31**. A `allowed_domains=["businesswire.com"]` exact-title
search that same cycle returned **only prior quarters** — a clean, confident, wrong negative. The
open web search and `stocktitan.net/news/ADBE/` both carried it. **BusinessWire's search index lags
roughly a day.**

Why this one is expensive: absence findings from this channel set the **floor** under an earnings
date (it is the whole basis for "CPRT's 09-03 is excluded"). A false negative therefore does not
just cost a session — it **silently pushes a date later** and produces no symptom.

Rule: **the BW exact-title search is a valid POSITIVE channel, but is not trustworthy as a NEGATIVE
on its most recent ~1 day.** Any absence that drives a floor needs a second, faster-indexing channel.
`stocktitan.net/news/<SYM>/` works and is one fetch — and **verify the cross-check is itself current**
by confirming it carries a known-recent PR, or you have just swapped one unverified silence for another.

Note this sits alongside the PVH propagation lag as the second denying-direction failure, and the
pair generalises: **anything with an intermediary between the publisher and you — a mirror, a CDN, a
search index — can be late, and late always reads as "not issued."** Only the publisher's own feed is
authoritative at the publication minute.

**And a sixth, from the same session (GME): the channel was current and honest, but was answering a
different question.** GameStop's Q2 date never appeared in an advance PR at all — it was a bullet
inside *"GameStop Announces Second Quarter 2026 Preliminary Results"*, issued to satisfy disclosure
alongside a convertible-notes exchange. A **title-pattern** probe returns nothing and reads as
absence, while the answer sat in the body of a PR the same feed had already delivered. **A probe is
only evidence if the channel can express the answer — and a title search cannot express "the date
moved into a differently-titled release." Parse bodies, not headlines** (see [[company-earnings-cadence]]).
