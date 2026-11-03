# MCP `hermes mcp test` vs Actual Chat Usage

## Core distinction

| `hermes mcp test <server>` | Actual tool calls in chat |
|----------------------------|---------------------------|
| Starts fresh OAuth flow every run | Uses cached token from `/root/.hermes/mcp-tokens/` |
| Opens browser, waits for consent → times out | Silent, works if token cached |
| Doesn't follow `tools/list` after `initialize` | Full handshake + tool discovery |
| **False negatives for OAuth servers** | **Works if authorization done once** |

## Why test fails for OAuth servers (cloudflare-api, vercel, composio_a, cloudflare-observability)

1. Test generates new PKCE challenge + new callback port each run
2. Browser opens → user must click "Allow" within 40s
3. Test cannot reuse previously authorized token
4. If no human clicks Allow → timeout → "Connection failed"

## Cached tokens location

```
/root/.hermes/mcp-tokens/<server>.json
```

Contains: `access_token`, `refresh_token`, `expires_at`, `scope`

Tokens survive restarts. One-time browser consent → cached → works forever in chat.

## Verification pattern

**Don't trust `mcp test` for OAuth servers.** Instead:

```bash
# 1. Check cached token exists
cat /root/.hermes/mcp-tokens/cloudflare-api.json

# 2. Manual JSON-RPC with cached token (bypasses test handshake)
# Use token from above file
curl -H "Authorization: Bearer <token>" \
     -H "Content-Type: application/json" \
     -d '{"jsonrpc":"2.0","id":1,"method":"initialize","params":{"protocolVersion":"2024-11-05","capabilities":{},"clientInfo":{"name":"test","version":"1.0"}}}' \
     https://mcp.cloudflare.com/mcp

# 3. Or simply: use a tool in chat — Hermes agent loads cached token automatically
```

## Servers affected

| Server | Auth | Test works? | Chat works after auth? |
|--------|------|-------------|------------------------|
| cloudflare-api | OAuth PKCE | ❌ (fresh flow each test) | ✅ |
| vercel | OAuth PKCE | ❌ | ✅ |
| composio_a | OAuth PKCE | ❌ | ✅ |
| cloudflare-observability | OAuth PKCE | ❌ | ✅ |
| notion | stdio (env var) | ❌ (timeout/handshake) | ✅ |
| github | stdio (script) | ✅ | ✅ |
| coingecko | HTTP (no auth) | ✅ | ✅ |
| bybit | stdio (no auth) | ✅ | ✅ |
| alphavantage | stdio (no auth) | ✅ | ✅ |

## Debugging checklist for OAuth servers

1. `hermes mcp test <server>` → copy authorize URL → open in **your browser** → click Allow
2. Wait for "Authorization complete" or redirect to localhost callback
3. Now `cat /root/.hermes/mcp-tokens/<server>.json` shows valid token
4. Chat usage works; `mcp test` still fails (by design)

## Key lessons

1. **`mcp test` is a diagnostic that doesn't mimic chat behavior for OAuth** — it's not a connectivity check
2. **One-time browser consent unlocks permanent chat access** — cached tokens persist
3. **Manual JSON-RPC with cached token is the real verification** — bypasses test limitations
4. **Bearer-token configs for OAuth-only endpoints will 400/403** — don't try `cloudflare-api-token` with API key