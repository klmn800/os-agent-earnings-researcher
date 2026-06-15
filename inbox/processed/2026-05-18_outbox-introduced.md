# Outbox folder introduced

## What changed
- Three stub outbox files exist for you at `outbox/for_system_analyst.md`, `outbox/for_trading_advisor.md`, `outbox/for_market_analyst.md`. Headers explain conventions tailored to your role.
- `outbox/README.md` explains the channel: **use it for making requests of peer agents OR answering their requests** — not for routine dispute resolution (that goes to the database).
- Your `CLAUDE.md` Communication Channels table updated with the new paths.
- Your hook (`hooks/inject_context.py`) is unchanged in behavior but the inbound mailbox paths it watches changed from `agents/<peer>/memory/` to `agents/<peer>/outbox/` for TA/SA/MA. Tested OK.

## Why this matters to you
You're not chatty by design. Most of your work writes to the database (`earnings_confirm.py`, `ir_earnings_url` updates), and that's correct — the dispute table closing out IS communication, you don't need an outbox note for it. The outbox is for the unusual:

- "I noticed `earnings_date_disputes` has been producing duplicate rows for SYM for three days" → `outbox/for_system_analyst.md`
- "TA's open play depends on CRWV reporting Thursday but I just confirmed it was moved to next Monday" → `outbox/for_trading_advisor.md`
- "MA's peer-sympathy cohort assumed CAVA was 5/28 but my IR check shows 5/27 AMC" → `outbox/for_market_analyst.md`
- Peer asks you to verify something specific via THEIR outbox → you do it, then reply via YOUR outbox

## Rotation
~400 lines per file → archive resolved/integrated threads to `outbox/<filename>_archive.md` in the same folder. You probably won't hit this for a long time given your low traffic. See `outbox/README.md`.

## No action needed today
Just an FYI. When you next have something worth flagging to a peer, the channel is wired and waiting.
