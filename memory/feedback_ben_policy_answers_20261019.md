---
name: ben-policy-answers-2026-10-19
description: Ben's answers to the standing policy questions (foreign-release encoding, BK, EXPD dmh, ITUB 6-K proxy, audit cadence, morning-call rule) — apply these instead of re-asking
metadata:
  type: feedback
---

Ben answered the open policy questions on 2026-10-19 (after the 10-18 maintenance summary):

1. **Foreign releases outside US hours ⇒ first US session that can trade the news, `bmo`.** A Saturday release (HDB, IBN)
   or an after-US-close release (ASX/HK/Chile: WDS, SQM; UEC's 10-K-evening/webcast-morning shape) is written as the next
   US trading day, `bmo`. HDB/IBN dated Sat 10-17 ⇒ **Mon 10-19 bmo** once the release is sourced.
   **Why:** the scanner cares about the session that prices the news. **How to apply:** in the daily template's step 4.
   Earlier writes that used "D−1 amc" (SQM) are re-encoded when their next row comes up, not retroactively.
2. **BK: skip.** Its missing `earnings_upcoming` row is deliberate or doesn't matter. Don't re-flag it.
3. **EXPD: `bmo` is fine functionally.** Don't propose `dmh` again; leave its `bmo` rows alone.
4. **ITUB: no answer yet. Test it first.** Ben: "see how it actually shakes out — if that doesn't match with actual
   earnings call date, then it's not useful." So, before ITUB's next report (DB 11-03 amc), log the date the SEC 6-K
   filing cluster predicts, *without* confirming it. After the report, score the prediction against the actual
   release/call date. Only a match makes the method usable. Until then, keep holding ITUB. Tracked in the research-log
   carry-overs.
5. **Source audit: yes, again on 10-25** (forward: the October dates passed by then).
6. **Morning-call rule: made a prompt rule.** Added to `launcher.py` PROMPT_TEMPLATE step 4 and CLAUDE.md step 4
   (see [[company-earnings-cadence]] rule 6).

Items 7, 8 and 10 of the 10-19 recommendations (carry confirmed times forward, diverged-row priority in the hook, the
`no_earnings_event` flag) were sent to the dev session (`options-scanner-90`) on 10-19. Not mine to implement.
