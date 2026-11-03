# Tinyfish MCP: OAuth vs API key + headless OAuth pitfalls

## What happened (original 2026 session)
- User supplied Tinyfish setup page, MCP endpoint, and an `sk-tinyfish-...` API key.
- `hermes mcp add tinyfish --url https://agent.tinyfish.ai/mcp --auth oauth` initiated OAuth PKCE successfully, but connection test timed out and Hermes offered to save the config disabled.
- Probing the endpoint showed:
  - no auth -> `401 Unauthorized`
  - `WWW-Authenticate: Bearer resource="https://agent.tinyfish.ai/.well-known/oauth-protected-resource/mcp"`
  - `X-API-Key: sk-...` -> `Unauthorized: Valid OAuth Bearer token required`
  - `Authorization: Bearer *** -> invalid JWT form

## Durable takeaway
Tinyfish Search/Fetch API keys are not the same credential as Tinyfish MCP transport auth. The `/mcp` endpoint requires OAuth bearer tokens obtained via the OAuth flow, not a raw `sk-...` key.

## Good operator response
- Configure Tinyfish MCP with `--auth oauth`.
- If add/test times out, it is still reasonable to save the server config and retry later.
- Explain clearly that the key may be valid for Tinyfish APIs while still being insufficient for MCP.
- Re-run `hermes mcp test tinyfish` after completing OAuth in the browser.

---

## Second failure mode (2026-06-17): headless OAuth can't bind callback port

After fixing the API-key confusion, OAuth was attempted four more times. Every attempt failed with the same error, regardless of what redirect URL the user pasted back:

```
tools.mcp_oauth.OAuthNonInteractiveError: OAuth callback timed out —
could not bind callback port. Complete the authorization in a browser first,
then retry.
```

**Root cause**: `tools/mcp_oauth.py:_wait_for_callback` starts a second `HTTPServer` on the same port that `build_oauth_auth` already reserved. Without `SO_REUSEADDR`, the second bind raises `OSError(EADDRINUSE)`, and the exception handler assumes the previous server is healthy — but the polling fallback in the same function is missing. The paste-fallback stdin reader never gets a chance to run because the bind exception is raised before the paste thread is started.

Confirmed ports from the failed attempts were all free at the time of inspection, so this is a logic bug in the SDK, not a port leak.

**Why the user-visible flow looks misleading:**
- The redirect URL is printed to stderr and includes a `127.0.0.1:<port>/callback` URL.
- The user's browser tries to redirect to that port — but they're on a different machine, so the redirect never reaches the container.
- The intended mitigation is for the user to copy the address-bar URL and paste it into the SDK's stdin reader.
- That reader is never spawned because the bind error short-circuits the function.

**Workarounds attempted, none successful from inside the agent:**
1. `script -q -c "hermes mcp login tinyfish"` with PTY — flow still dies on bind.
2. Custom Python driver that calls `_probe_single_server(name, cfg, connect_timeout=600)` from a background thread and writes pasted URLs to the PTY master — still dies on bind inside `_wait_for_callback`.
3. Pre-binding the port myself before the SDK runs — would require a code patch to `mcp_oauth.py`.

**Conclusion**: Tinyfish MCP cannot be authenticated from this agent's environment (Discord session, no interactive TTY, no reachable localhost callback). Disabling the server is the correct action. If tinyfish is wanted, the user must complete the OAuth flow from a real interactive shell on the host machine (`hermes mcp login tinyfish` in their own terminal), or the SDK code path needs to be patched to:
- Use `SO_REUSEADDR` on the callback `HTTPServer`, OR
- Skip the redundant bind in `_wait_for_callback` and reuse the server started by `build_oauth_auth`, OR
- Always spawn the paste-fallback thread before the bind attempt.
