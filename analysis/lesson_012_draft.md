# 012 — Before you let an agent write anything, find out whose name it writes under

**Type:** Pitfall
**Source:** earnings_researcher agent (options_scanner)
**Added:** 2026-08-19
**Deep reference:** `E:\options_scanner\agents\earnings_researcher\notes_for_ben.md` (08-19 entry); `memory/feedback_earnings_confirm_bare_symbol.md`

## The lesson

Most business tools record **who did something** — `approved_by`, `created_by`, `--user`,
"last edited by." Those fields were designed when only people used the tool, so they
often **default to the account owner**. Point an agent at that tool and its work can get
filed under *your* name, with nothing in the record showing a machine did it.

That is bad on its own. It becomes much worse if your process also says *"don't override
what a human decided."* Then the agent can create an entry that **nobody is allowed to
correct** — including the agent, including you next month, because the record says you
already decided it.

## What people get wrong

The assumption is that the risk of giving an agent write access is **bad data** — it
writes something wrong, you notice, you fix it. That's the failure everyone plans for.

The failure they don't plan for is **bad provenance**: the data may be wrong *and* wearing
your authority. Those need different defenses. You catch bad data by reviewing content.
You catch bad provenance by checking the byline — and almost nobody reviews the byline,
because for twenty years the byline was never in question.

The trap is that both halves are individually sensible:

- *"The actor field defaults to the logged-in owner"* — correct for two decades of human use.
- *"Never override a human's decision"* — correct, and the reason human-in-the-loop works.

Neither is a mistake. Put an agent between them and they produce something neither
anticipated: **the agent can manufacture an authority it is then forbidden to question.**
And the more disciplined your deference rule is, the more permanently the bad entry sticks.

## Evidence

Single observed instance, caught immediately — treat this as an argued pitfall, not a
measured one.

In an agent that researches and confirms corporate earnings dates, the confirm tool is:

```
earnings_confirm.py --symbol SYM --date YYYY-MM-DD --time amc --by agent
```

Run it with **only** `--symbol` and it doesn't show you the record — it confirms the
record as it stands, and `--by` **silently defaults to the human owner**. The tool's own
`--help` lists the bare `--symbol` form as an example, directly under the full command,
so it reads like a lookup.

The agent ran it expecting to read a row. It wrote:

```
GME | 2026-09-08 | date_confirmed=1 | date_confirmed_by='ben'
```

The date had **no source behind it** — that was exactly why the agent was inspecting the
row instead of confirming it. And the project's standing rule is *never overwrite a date
confirmed by Ben*, so that one stray default had converted an open question into a
permanent, unappealable "fact."

Caught and reverted within a minute, so the cost here was zero. The point is what the cost
*would* have been: a wrong date, protected by a rule designed to protect good judgment,
surviving every future review because every future reviewer was forbidden to touch it.

## How to use it

The one-line version for an audience: **"Your agent may be signing your name."**

A demo that lands in thirty seconds — open any shared doc, ticket, or CRM record an agent
has touched and read the "last modified by" field aloud. If it says a person's name, ask
the room how they'd ever know which edits that person actually made.

Three questions to hand someone before they connect an agent to a system of record:

1. **What does this tool put in its "who did it" field when the agent calls it?** Don't
   reason about it — run one write and go look at the record.
2. **Can that field be left to a default?** If yes, that's the bug. Provenance should
   *fail closed* — refuse the write rather than guess an identity.
3. **Does any rule in our process treat that field as authority?** Approval gates,
   "don't override the human," sign-off requirements, audit exemptions. Every one of them
   becomes a lock the agent can throw.

The fix is nearly always cheap and belongs in the tool, not in the agent's instructions:
make the actor argument **required**. Telling the agent "always pass `--by agent`" is a
reminder, and reminders fail; a required flag cannot.

The wider habit worth naming: when you introduce an agent into a workflow, audit not just
what it can *change* but what it can *assert* — and make sure agent-written and
human-written stay distinguishable in the record forever after.

## Caveats

- **One instance, from an internal tool, caught in under a minute.** No cost figure. It
  qualifies as a silent pitfall on reasoning, not on measured damage — say so if asked.
- **Only bites where an identity field carries weight.** If nothing in your process treats
  "who did it" as authority, this is untidy record-keeping, not a trap.
- **Not an argument against agent write access.** The same agent, in the same session, made
  a genuine 8-day correction to a date the system had wrong. The argument is for making the
  byline non-defaultable, which costs one line of validation.
- Mature audited platforms with real service accounts and separate machine identities
  mostly get this right already. The exposure is in **internal scripts and homegrown
  tools** — the ones written when "the user" and "a person" meant the same thing.
