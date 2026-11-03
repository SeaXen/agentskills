# NotebookLM MCP auth on Linux desktop Hermes hosts

Use this when a user asks to set up a NotebookLM integration for Hermes from a repo that is actually Claude/Codex/Cursor-oriented.

## Durable pattern
- Treat the agent-specific repo as a clue, not the install target.
- Prefer the reusable backend: `PleasePrompto/notebooklm-mcp`.
- For normal Hermes use on headless/server-ish Linux, keep the permanent MCP server wrapped with `xvfb-run -a`.
- For **first Google login**, a purely headless wrapper is often the wrong surface even if the host has a desktop.

## Working split
1. **Permanent runtime server**
   - Hermes MCP entry points to a tiny local wrapper script, for example:
   ```bash
   #!/bin/bash
   set -euo pipefail
   exec xvfb-run -a npx -y notebooklm-mcp@latest
   ```
   - Verify with:
   ```bash
   hermes mcp list
   hermes mcp test notebooklm
   ```

2. **Temporary auth helper server**
   - Create a second MCP entry just for first login, using plain `npx notebooklm-mcp@latest` and pass GUI env through the stdio subprocess:
   - `DISPLAY=:0`
   - `XAUTHORITY=/root/.Xauthority` (or the real desktop user's Xauthority file)
   - This keeps normal runtime headless while allowing the one-time visible login window.

3. **Launch auth through Hermes, not by assumption**
   - Call the MCP `setup_auth` tool via Hermes.
   - Watch logs for the good path:
     - `Opening Google login page...`
     - `Please login to your Google account`
     - `Waiting for login...`
   - If you see those lines, the browser launch worked and the remaining step is user interaction on the desktop.

## Important pitfall
- `hermes mcp add` is interactive. Pipe confirmation in automation:
```bash
printf 'Y\n' | hermes mcp add ...
```
- Then verify the saved result with both `hermes mcp list` and `hermes mcp test <name>`.

## Normal cleanup after auth
- Once login is complete and verified, remove the temporary auth helper MCP entry and keep only the permanent headless/runtime entry.
- Tell the user the permanent config change does **not** need to be redone just because an earlier protected-file patch attempt emitted a warning. Trust the final `hermes mcp list` / `hermes mcp test` state.

## What to save from this class of task
- Save the split-pattern (headless runtime + GUI auth helper), not the transient launch errors that led you there.
