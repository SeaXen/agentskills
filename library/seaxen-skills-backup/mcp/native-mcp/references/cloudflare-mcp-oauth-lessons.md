# Cloudflare MCP OAuth Session Notes

## Issue: Cloudflare API MCP returns 400 with bearer token

**Endpoint:** `https://mcp.cloudflare.com/mcp`

**Failed config:**
```yaml
cloudflare-api-token:
  url: https://mcp.cloudflare.com/mcp
  enabled: true
  headers:
    Authorization: Bearer ${CLOUDFLARE_API_TOKEN}
```

**Error:** `Client error '400 Bad Request' for url 'https://mcp.cloudflare.com/mcp'`

**Root cause:** This endpoint only supports OAuth 2.1 PKCE. Bearer tokens valid for Cloudflare REST API are rejected at the MCP layer.

**Working config:**
```yaml
cloudflare-api:
  url: https://mcp.cloudflare.com/mcp
  auth: oauth
  enabled: true
```

## One-time OAuth flow

1. Run `hermes mcp test cloudflare-api`
2. Browser opens: `https://mcp.cloudflare.com/authorize?response_type=code&client_id=8sQPvvjJ_WRfGU28&redirect_uri=http%3A%2F%2F127.0.0.1%3A...`
3. Sign in to Cloudflare if needed
4. Click **"Allow"** on consent screen
5. Token cached locally — future chat tool calls work automatically

## Related: cloudflare-observability

Uses **different URL**: `https://observability.mcp.cloudflare.com/mcp`
Also uses OAuth, works independently.

## Key lesson

For Cloudflare MCP: **OAuth is mandatory at this endpoint.** Do not attempt bearer-token config — it will 400. Keep OAuth and token configs as separate entries (as per durable lesson).