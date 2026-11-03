# Hermes MCP onboarding from agent-specific repos

Use this when a user shares a repo that is branded as a Claude Code skill, Codex helper, Cursor integration, or similar and asks to "set it up in Hermes".

## Durable pattern

1. **Do not assume the shared repo is the Hermes install target.**
   - First classify whether it is:
     - a Hermes-native skill,
     - an MCP server Hermes can consume,
     - or an agent-specific wrapper that only works in another client.
2. **If the shared repo is agent-specific, look for the real reusable backend.**
   - Common outcome: the skill repo is only a thin Claude/Codex wrapper around a separate MCP server.
   - For Hermes, prefer wiring the MCP server directly instead of trying to install the foreign skill unchanged.
3. **For `hermes mcp add` automation, expect an interactive tool-enable prompt.**
   - Pipe confirmation explicitly in non-interactive flows:
     ```bash
     printf 'Y\n' | hermes mcp add <name> --command <cmd>
     ```
4. **If the stdio command needs wrapper behavior, use a local wrapper script instead of fighting CLI arg parsing.**
   - Good examples:
     - `xvfb-run -a npx -y notebooklm-mcp@latest`
     - env setup before `npx`
     - `gh auth token` export before a GitHub MCP server
   - Put the logic in a script under the Hermes scripts tree, then point `hermes mcp add` at that script.
5. **Verify in three layers:**
   - `hermes mcp add ...` or config entry succeeds
   - `hermes mcp list` shows the server enabled
   - `hermes mcp test <name>` discovers tools successfully
6. **Tell the user when a new session is required.**
   - After saving MCP config, Hermes may require a new session before the tools are callable in chat.

## NotebookLM-specific note

The PleasePrompto `notebooklm-skill` repo is Claude Code-specific. For Hermes, the correct integration is the companion MCP server `notebooklm-mcp`.

## Pitfalls

- Treating a foreign-agent skill repo as if it were directly installable in Hermes.
- Trying to cram `xvfb-run -a ...` or other wrapper behavior into `hermes mcp add --args ...` when a tiny wrapper script is safer and clearer.
- Forgetting that `hermes mcp add` prompts for tool enablement and will not finish unattended unless confirmation is piped.
- Stopping after config write without `hermes mcp test <name>`.
