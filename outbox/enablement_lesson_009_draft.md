# DRAFT — for `E:\ai_enablement\lessons\009-record-observations-not-conclusions.md`

> Ben: I can't write outside my workspace (hook blocked it), so the draft is parked here.
> Move it to `E:\ai_enablement\lessons\009-record-observations-not-conclusions.md` and add the
> ledger row below. Delete this file after.
>
> **Ledger row** (append to the table in `AI_Enablement_Lessons_Ledger.md`):
>
> ```
> | 009 | [In agent memory, record what you observed — not what you concluded](lessons/009-record-observations-not-conclusions.md) | Pitfall | earnings-date-researcher | 2026-08-13 |
> ```
>
> Note: this is the first lesson sourced from outside finance-doc-summarizer, and the first about
> agent memory rather than a model capability. Renumber if 009 got taken since 08-04.

---

# 009 — In agent memory, record what you observed — not what you concluded

**Type:** Pitfall
**Source:** earnings-date-researcher (long-running agent with persistent file memory)
**Added:** 2026-08-13
**Deep reference:** `E:\options_scanner\agents\earnings_researcher\memory\reference_company_cadence.md`,
`notes_for_ben.md`

## The lesson

When an agent writes to persistent memory, an **observation** ("I checked channel X, found nothing")
and a **conclusion** ("no source exists") look equally authoritative on the next read — but only one
of them is still true tomorrow. Conclusions silently harden into facts, and later sessions stop
re-testing what was never actually established.

Store the observation and the channel list. Let each session re-derive the conclusion.

## What people get wrong

The assumption is that agent memory degrades the way human memory does — details fade, confidence
drops, you eventually go check again. **It does the opposite.** A memory file is re-read verbatim,
in full confidence, every session. Nothing decays. So a wrong inference written once is re-read as
established fact indefinitely, and each re-reading entrenches it further.

There's a second-order effect that makes it worse: when a stored conclusion gets restated across
several sessions, those restatements start to read like *independent corroboration*. They aren't.
It's one inference echoed N times. An agent reviewing its own notes sees six entries agreeing and
takes that as strong evidence, when the actual evidence base is a single unverified premise.

The failure is specifically about the **gap between a scoped negative and a general one**:

| What was actually observed | What got written down |
|---|---|
| "The press-release feed has no scheduling PR" | "This company issues no advance notice" |
| "`ir.` and `investors.` are both NXDOMAIN" | "This company has no IR host" |
| "No PR in the window the *last* quarter used" | "The event is probably a phantom" |

Every left-hand cell is true and verifiable. Every right-hand cell is a generalization whose
validity depends on a channel list that was never written down — so no later session can audit it.

## Evidence

Five instances in roughly two weeks on one agent, all the same shape:

- **SQM** — Verified correctly that the company issues no advance press release. Recorded it as *"no
  company source is possible."* Three sessions (08-07, 08-10, 08-11) then re-read the same feed,
  correctly found nothing, and re-derived the same dead end. It was escalated to the human operator
  **twice** as a judgment call only they could make. Resolved on 08-13 by fetching one page never
  tried before — the IR **events calendar**, a different surface from the press-release feed, which
  listed both the release datetime and the call datetime, and had done so consistently since 2023.
  Cost: three wasted cycles plus two unnecessary escalations. Fix: one URL.

- **Bio-Techne (TECH)** — the expensive one. A lead-time measured on the *Q3* cycle was used to judge
  silence in the *Q4* cycle, and "no PR yet" was recorded against a channel never confirmed to exist
  for that quarter. Eight sessions compounded it, aided by a live merger that supplied a plausible
  story. The agent twice advised the operator **not to trade an earnings event that was real** and
  arrived exactly where the calendar said it would. No date was ever mis-written — the damage was
  confident-sounding advice resting on an unexamined premise.

- **nCino** — `investors.` and `ir.` both NXDOMAIN, written down as "no IR host at any prefix." The
  live host was `investor.` (singular). Nobody had tried the third prefix. Four sessions.

- **FLO / NTRA** — absence read off a feed that *was* live and current, but was the wrong channel:
  the scheduling releases went out through a different distribution path entirely. Two separate
  companies, same error.

Common thread: **the observation was always right. The stored generalization was always wrong.** And
in each case the correction cost one fetch — the expense was entirely in how long the wrong version
sat unchallenged.

## How to use it

**The rule, stated for an audience:** *write down what you checked, not what you think it means.*

Practically, for any agent with a durable memory file:

1. **Make "channels checked" an explicit field.** Not prose — a list. `checked: [rss_feed, sec_8k]`
   is auditable by a future session; "no source exists" is not. The next run can immediately see
   what *wasn't* tried.
2. **Phrase status as `unsourced`, never `unsourceable`.** One says "I haven't found it yet," the
   other closes the question. Only the first is honestly supportable, and the wording difference is
   what determines whether a later session bothers to look.
3. **Treat repeated entries as one data point.** Before letting N agreeing notes raise your
   confidence, ask whether they're N observations or one inference restated N times.
4. **Require a positive existence check before arguing from absence.** "Nothing on channel X" only
   means something once you've confirmed X is where this thing would appear *for this case*. That
   single check — did the equivalent event have a notice last time? — would have killed four of the
   five failures above on day one.
5. **When you correct one, write the correction as loudly as the original.** The wrong version had
   many sessions to entrench; a quiet fix loses to it.

**The line that makes it land:** human memory forgets and re-checks. Agent memory remembers
perfectly and never re-checks. That's usually the selling point — here it's the failure mode.

**Where it generalizes:** anything that accumulates durable notes across runs — research agents,
incident runbooks, triage bots, codebase knowledge files, RAG stores fed by earlier model output.
Any system where a model reads its own prior conclusions as input has this exposure.

## Caveats

- **Not an argument against storing conclusions.** Conclusions are the value; re-deriving everything
  from raw observations every run is what memory exists to avoid. The ask is to store them *with
  their basis attached*, so they can be audited rather than only inherited.
- **Some negatives really are closed.** "This ticker was delisted; the acquisition closed" is
  settled and should be recorded as settled. The distinction is whether the claim is about a
  **fact in the world** (durable) or about **the completeness of your own search** (not durable).
- **Scoped to durable memory.** Within a single session, working conclusions are fine — the
  conversation context supplies the basis. The hazard is specifically the write-to-disk boundary,
  where the reasoning is dropped and only the verdict survives.
- **The fix has an upkeep cost.** Structured channel lists are more work to write and go stale.
  Worth it for expensive-to-rediscover facts; overkill for routine notes.
