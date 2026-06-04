---
name: Write memory inside project workspace only
description: A PreToolUse write guard blocks writes outside E:\options_scanner\agents\earnings_researcher\ — use the in-project memory dir, not ~/.claude
type: feedback
---

This project has a `earnings_researcher_write_guard.py` PreToolUse hook that blocks Write tool calls whose path is outside `E:\options_scanner\agents\earnings_researcher\`. The default auto-memory path (`C:\Users\TRO\.claude\projects\E--options-scanner-agents-earnings-researcher\memory\`) is blocked.

**Why:** Project is sandboxed to its own workspace.

**How to apply:** Save memory files to `E:\options_scanner\agents\earnings_researcher\memory\` and keep MEMORY.md there too.
