# Hermes dashboard insecure-bind websocket policy

Use this when `hermes dashboard --tui` loads `/chat` over LAN/public bind but the sidebar shows:
- `events feed disconnected — tool calls may not appear`
- model badge stays `closed`
- chat shell renders but terminal/chat does not go live

## Failure shape

A deceptive partial success:
- `http://<host>:<port>/chat` returns HTML and frontend assets
- bootstrap script may contain a valid `window.__HERMES_SESSION_TOKEN__`
- browser console may show no fatal JS error
- but websocket upgrades for `/api/ws` and `/api/events` fail, often as HTTP `403`

This means **page render succeeded but runtime websocket admission failed**.

## Distinguish the three modes

1. **Loopback bind**
   - host like `127.0.0.1`
   - websocket peers should remain loopback-only
   - token alone is not enough for remote peers

2. **Gated/public mode**
   - auth-required flow with ticket/OAuth gate
   - remote peers can connect if Host/Origin and ticket auth pass

3. **Explicit insecure public bind**
   - `--host 0.0.0.0 --insecure` or `--host :: --insecure`
   - operator explicitly opted into public/LAN exposure
   - remote websocket peers must be allowed, while Host/Origin checks still stay in place

## Practical diagnosis sequence

1. Compare loopback and LAN websocket behavior.
   - If `127.0.0.1` websocket opens but `192.168.x.x` fails with `403`, suspect backend peer policy.
2. Check raw app port before blaming nginx.
   - If raw `:9120` fails the same way, proxy is not the root cause.
3. Check HTML bootstrap separately from websocket behavior.
   - Valid token injection does **not** rule out websocket rejection.
4. Keep Host/Origin reasoning separate.
   - Do not relax DNS-rebinding protections just to make LAN websocket work.

## Durable fix pattern

In websocket admission logic, treat insecure all-interface bind as its own case:
- gated/auth-required mode: allow remote peers subject to auth + Host/Origin
- insecure public bind (`0.0.0.0` / `::`): allow remote peers subject to Host/Origin
- loopback bind: require loopback peers

Do **not** collapse insecure public bind back into loopback-only behavior.

## Verification

- targeted websocket/auth tests pass
- raw LAN websocket opens on both `/api/ws` and `/api/events`
- browser state becomes live instead of `closed`
- proxied path can then be checked separately for auth/upgrade issues
