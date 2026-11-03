# Stdlib WebSocket terminal streaming for standalone terminal apps

Use when building a Dockerized terminal/dashboard app under package-install constraints where npm/pip/apt are not reliable, but browser terminal streaming is still needed.

## Pattern

A Python stdlib `ThreadingHTTPServer` can serve:
- `/` static UI
- `/api/*` JSON endpoints
- `/api/terminal/ws` WebSocket PTY stream

This keeps the app as one Docker service/container and avoids nginx, FastAPI, xterm.js, or websocket packages for the first streaming milestone.

## Backend shape

Add minimal WebSocket support directly in the handler:
- accept auth via normal header or query token for browser websocket connections
- perform RFC6455 handshake using `Sec-WebSocket-Key` + magic GUID
- send unmasked text frames from server to browser
- read masked browser text frames
- write incoming payload to the PTY master fd
- repeatedly drain PTY output and send it over the websocket
- keep existing HTTP `/read` + `/write` endpoints as fallback

Important implementation notes:
- browser-to-server frames are masked; server-to-browser frames are not
- handle 126/127 extended payload sizes
- set short socket timeouts so PTY draining and WS reads can interleave
- treat close frames and empty reads as connection termination
- create/attach the backend PTY session by sanitized session id

## Frontend shape

For a simple static UI:
- create `ws://host/api/terminal/ws?session=<id>&token=<token>` or `wss://` under HTTPS
- attach websocket per active pane/session
- append incoming messages to that session's output cache
- send commands over WS when open
- fall back to HTTP write/read when WS is unavailable or closed
- show transport state visibly (`ws open`, `ws connecting`, `poll fallback`)

## Verification

Verify three layers:
1. API health over the public port
2. raw websocket handshake and command echo, e.g. send `echo websocket-ok` and assert output contains it
3. browser UI command execution plus console check

Do not claim Hermes terminal parity from this alone. This gives a real streaming PTY path, but it is still not xterm.js terminal emulation.

## Honest clone-status language

Use clear wording:
- "clone-first standalone terminal app" when parity is the goal and several behaviors are copied
- "not exact Hermes dashboard terminal clone yet" until renderer, websocket/xterm behavior, auth/session model, and reconnect semantics match

Avoid saying "same-to-same" unless live browser verification confirms the specific Hermes behaviors the user asked about.