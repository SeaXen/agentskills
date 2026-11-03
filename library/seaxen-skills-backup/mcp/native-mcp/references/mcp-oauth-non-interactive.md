# MCP OAuth in Non-Interactive Agent Sessions

OAuth-protected MCP servers (e.g. `tinyfish`, `cloudflare-api`, `notion` remote) need
a one-time browser-based consent. The normal flow assumes the user is sitting at a
terminal where `hermes mcp login <name>` can pop a browser and capture the localhost
callback.

This reference covers what happens when **the agent is itself running in a
non-interactive environment** (Discord bot, headless service, Docker, SSH without
TTY, CI). The pattern is: enable, transport-test, then hand the OAuth piece back to
the user with a clear "do this from your terminal" instruction.

## 1. Enable without editing config.yaml

The `patch` tool refuses to write to `~/.hermes/config.yaml` (security guard).
Use the canonical CLI:

```bash
hermes config set mcp_servers.<name>.enabled true
hermes config set mcp_servers.<name>.enabled false   # to disable
```

This writes the YAML for you and prints the file path. Prefer this over manual edits
so the change is also picked up by any config watchers.

Verify:

```bash
hermes mcp list | grep <name>
# expect: ✓ enabled
```

## 2. Quick transport test

`hermes mcp test <name>` is the cheapest check that the URL is reachable, the
endpoint speaks MCP, and the auth header handshake is at least accepted up to the
"OAuth required" point:

```bash
hermes mcp test tinyfish
# ✓ ok-ish:  Transport: HTTP → https://agent.tinyfish.ai/mcp
#            Auth: OAuth 2.1 PKCE
# ✗ failed:  MCP OAuth for 'tinyfish': non-interactive environment and
#             no cached tokens found. Run `hermes mcp login tinyfish`
#             interactively first to complete initial authorization.
```

A `1.3s` response time on the failure means **the server is reachable and speaking
MCP** — the failure is purely the OAuth grant, not network or transport.

## 3. The non-interactive OAuth blocker

`hermes mcp login <name>` checks `sys.stdin.isatty()`. In a Discord bot / Docker /
SSH-without-TTY session that returns `False`, and Hermes refuses to even print the
authorization URL:

```
Authentication failed: MCP OAuth for 'tinyfish': non-interactive environment
and no cached tokens found. Run `hermes mcp login tinyfish` interactively
first to complete initial authorization.
```

Wrapping with `script` (PTY faker) gets past the TTY check and reveals the URL,
but does **not** close the round-trip — the OAuth provider redirects to
`http://127.0.0.1:<port>/callback`, and `<port>` is on the **agent's** host loopback,
not the user's. So even with the URL the agent cannot receive the callback.

```bash
# Reveal the OAuth URL (does NOT complete auth)
script -q -c "hermes mcp login tinyfish" /tmp/tinyfish_login.log < /dev/null
sleep 12
cat /tmp/tinyfish_login.log
# expect:  Open this URL in your browser:
#            https://<provider>/oauth/authorize?...&redirect_uri=...
```

**Pitfall — `script -q` buffers the typescript until the child exits.** On a
real `hermes mcp login <name>` that is waiting for the OAuth callback, the log
file stays empty for the full 40s MCP-call window and only fills when the
process times out and dies. If you want the URL *while* the process is alive,
do not use `script`; use a python `pty` wrapper that reads the fd directly:

```python
# /tmp/oauth_driver.py — stream hermes mcp login output live
import os, pty, select, time
URL_FILE, LOG_FILE = "/tmp/tinyfish_url.txt", "/tmp/tinyfish_pty.log"
INPUT_FILE = "/tmp/tinyfish_input.txt"   # drop pasted URL here to inject
pid, fd = pty.fork()
if pid == 0:
    os.execvp("hermes", ["hermes", "mcp", "login", "tinyfish"])
buf = b""
start = time.time()
with open(LOG_FILE, "wb") as logf:
    while time.time() - start < 90:
        # auto-inject any URL the user dropped into INPUT_FILE
        if os.path.exists(INPUT_FILE):
            try:
                line = open(INPUT_FILE).read().strip()
                if line:
                    os.write(fd, (line + "\n").encode())
                    open(INPUT_FILE, "w").close()
            except FileNotFoundError: pass
        r, _, _ = select.select([fd], [], [], 0.3)
        if r:
            try: chunk = os.read(fd, 4096)
            except OSError: break
            if not chunk: break
            logf.write(chunk); logf.flush()
            buf += chunk
            text = buf.decode("utf-8", errors="replace")
            if "https://" in text and not os.path.getsize(URL_FILE):
                idx = text.find("https://")
                end = text.find("\n", idx)
                open(URL_FILE, "w").write(text[idx:end if end!=-1 else len(text)].strip())
        try:
            wpid, _ = os.waitpid(pid, os.WNOHANG)
            if wpid: break
        except ChildProcessError: break
```

Flow: (1) start the driver, (2) wait ~3s, (3) `cat /tmp/tinyfish_url.txt` to
get the live auth URL, (4) send it to the user, (5) when they paste back the
redirect URL, `echo '<url>' > /tmp/tinyfish_input.txt`, (6) the driver injects
it and `hermes mcp login` exchanges the code. The 40s MCP-call window is tight
but doable if the user is ready and Cloudflare Turnstile does not block them.

The redirected URL the user sees in their browser will be of the form
`http://127.0.0.1:<port>/callback?code=...&state=...`. They can either:

- **Easiest:** SSH-port-forward that port from their local machine to the agent
  host before opening the auth URL, so the redirect resolves on the agent where
  the listener is running, OR
- **Manual:** after authorizing in the browser, copy the full `?code=...&state=...`
  portion of the redirect URL and paste it back into a fresh
  `hermes mcp login <name>` run on their own interactive terminal.

**Pitfall — every `hermes mcp login` attempt generates a fresh `state`, port,
and `client_id` (pre-registered to `~/.hermes/mcp-tokens/<name>.client.json`).**
A `code` from a previous timed-out flow is **not** reusable in a new flow — the
`state` will not match and the token exchange will be rejected. If the user
pastes a redirect URL that is older than the currently running flow, ignore it,
start a fresh login, and ask them to re-authorize against the new URL. The
fastest tell: the new flow's URL has a different `port` and `state=` than the
one they pasted.

## 4. What you CANNOT do from the agent

Trying to drive the OAuth from `browser_navigate` is tempting but unreliable:

- The auth provider almost always sits behind a bot-detection CDN (Cloudflare
  Turnstile, etc.) that flags headless/agent browser sessions.
- Even if the consent page loads, the user's real credentials are not in the
  agent's browser, so the auth would have to be the user's anyway.

Do **not** promise the user "I'll complete the OAuth" — the right move is
"server is reachable, OAuth is the only blocker, here is the URL, finish it from
your terminal."

## 5. Reporting status to the user honestly

When a user asks "is X MCP working?", the truthful state after enable + test is
one of four. Name the one you're in:

| State | What the user sees | What to say |
|---|---|---|
| 1. Disabled in config | `✗ disabled` in `hermes mcp list` | "Disabled. Flip with `hermes config set ...`" |
| 2. Enabled, transport fails | `✗ Connection failed` (timeout, DNS, 5xx) | "Server unreachable. Check URL/network." |
| 3. Enabled, transport OK, auth missing | `✗ non-interactive environment and no cached tokens` | "Server reachable, OAuth pending. Run `hermes mcp login <name>` from your terminal." |
| 4. Authed and connected | `✓ enabled` + tools discoverable in chat | "Working. Tools are registered." |

Reporting state 3 as "broken" or "not working" is wrong — the MCP layer is fine,
the OAuth grant is a one-time user action.

## 6. After the user completes auth

Have them verify from their own terminal:

```bash
hermes mcp test <name>      # expect: ✓ Connection successful, N tools
hermes gateway restart      # if running through the gateway
```

If they want the new tools available **right now** in the current agent session,
the agent process needs a reload — `hermes mcp test` does not hot-register
tools into a running session. Either restart the gateway or open a new chat.

## 7. Pitfalls

- **Don't promise to complete OAuth from the agent.** It can't, because the
  callback is on the agent's loopback and the user holds the credentials.
- **Don't conflate "transport test passes" with "MCP is working."** A reachable
  endpoint that needs OAuth is half-working. Tell the user which half.
- **`hermes mcp test` is not a hot-reload trigger.** Enabling a server and
  passing the test does not register tools in the current session.
- **PTY wrappers (`script`, `unbuffer`) bypass the TTY check but not the
  callback locality problem.** They are useful for *revealing* the OAuth URL,
  not for *completing* the flow.
- **Cloudflare-protected providers** (e.g. `accounts.tinyfish.ai`) often block
  the headless browser path entirely. This is a provider policy, not a bug
  to work around.
- **Real root cause of the "could not bind callback port" failure** (added
  2026-06-17 after 4 retry attempts on `tinyfish`): `tools/mcp_oauth.py`
  `_wait_for_callback` (line ~483) starts a *second* `HTTPServer` on the
  same `127.0.0.1:<port>` that `build_oauth_auth` already reserved. The
  `HTTPServer` class does not set `SO_REUSEADDR`, so the second bind raises
  `OSError(EADDRINUSE)`. The exception handler in `_wait_for_callback`
  treats that as "the prior server is fine, fall through" but then
  immediately raises `OAuthNonInteractiveError` instead of falling through
  to the paste-fallback stdin reader. Net effect: the URL is printed, the
  SDK appears to be waiting, but it has actually already given up — every
  pasted redirect URL goes into a void.
  Confirmed: all 4 retry attempt ports were `FREE` at the time of
  inspection, so this is a logic bug, not a leftover listener. PTY wrappers,
  custom Python drivers that write pasted URLs to the master fd, and
  raising `connect_timeout=600` do not help — the bind happens inside
  the SDK and short-circuits the function.
  **If you see this error, stop after 1-2 attempts and report it as an
  environment-class blocker rather than a retryable failure.** Workarounds
  require patching `mcp_oauth.py` (add `SO_REUSEADDR` to the `HTTPServer`,
  or skip the redundant bind entirely) or completing OAuth from a real
  interactive shell on the host machine. The user must run
  `hermes mcp login <name>` from their own terminal.
