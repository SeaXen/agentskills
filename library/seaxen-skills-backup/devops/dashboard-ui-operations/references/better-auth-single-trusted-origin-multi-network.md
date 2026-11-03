---
name: better-auth-single-trusted-origin-multi-network
description: Diagnosis and resolution pattern for self-hosted apps that use Better Auth (Manifest, some dashboards) and reject every origin except one trusted URL. Covers LAN, Tailscale, and Cloudflare Tunnel access from the same host.
applies_to: dashboard-ui-operations
---

# Better Auth single trusted origin — multi-network access pattern

## Symptom

App loads, sign-up form renders, clicking **Create account** shows a red banner:

> Invalid origin

Browser console / network tab shows the POST returns a 4xx with the same string. App logs (e.g. `docker logs <container>`) show:

```
ERROR [Better Auth]: Invalid origin: http://192.168.0.222:2099
INFO  [Better Auth]: If it's a valid URL, please add http://192.168.0.222:2099
                      to trustedOrigins in your auth config
 Current list of trustedOrigins: http://localhost:2099,http://localhost:2099
```

This is **not** CORS, not the reverse proxy, not the tunnel. The app uses [Better Auth](https://www.better-auth.com/) and trusts exactly one origin. Accessing from any other URL (LAN IP, Tailscale, Cloudflare Tunnel) is rejected as a CSRF defense.

## Root cause

Better Auth reads a single trusted origin from app config — usually injected via `BETTER_AUTH_URL` env var. Setting this to one value whitelists exactly that URL. Comma-separated env values **do not work**; the trustedOrigins list lives in the source code or DB, not in env vars (the logged list often shows the same value twice as a source-read artifact, which is misleading).

## The three access paths on a single Docker host

For a self-hosted app on the same Linux box, the operator typically wants to reach it from:

1. **Direct LAN** — `http://192.168.0.222:2099` (and `http://localhost:2099` from the host itself)
2. **Tailscale** — `http://100.x.x.x:2099` from a remote Tailscale node
3. **Cloudflare Tunnel** — `https://mf.xuup.top` (HTTPS public, terminates to the host:port)

With a single Better Auth instance, **max coverage is 2 of 3**. Tailscale cannot be bridged by a Host-header rewrite, so the realistic 2-of-3 combinations are:

- LAN + CF tunnel
- LAN + Tailscale (operator must access the LAN IP from the Tailscale side; usually rejected by users)
- CF tunnel only (every network uses the tunnel URL)

## Resolution patterns

### Pattern A — Tunnel as the only canonical URL (simplest)

Set `BETTER_AUTH_URL=https:...t>`. Reach the app via the tunnel from any network (LAN, Tailscale, public). The CF tunnel terminates TLS and forwards to host:2099 with `Host: <tunnel-host>`.

**Trade-off:** every client must use the tunnel URL. Browsers, APIs, even local CLI scripts. Direct LAN access fails.

### Pattern B — LAN IP as canonical + CF tunnel httpHostHeader rewrite

Set `BETTER_AUTH_URL=http:/... Configure Cloudflare Tunnel to forward with `httpHostHeader: 192.168.0.222:2099` so the Host header reaching the app matches `BETTER_AUTH_URL`. Then:

- `http://192.168.0.222:2099` (direct LAN) → app sees `Host: 192.168.0.222:2099` → matches → ✅
- `https://mf.xuup.top` (CF tunnel) → tunnel rewrites Host to `192.168.0.222:2099` → matches → ✅
- Tailscale `100.x.x.x:2099` → app sees `Host: 100.x.x.x:2099` → no rewrite available → ❌

**How to set httpHostHeader in Cloudflare Tunnel:**

- **Dashboard path:** Zero Trust → Networks → Tunnels → select tunnel → Configure → Public Hostname tab → edit the hostname entry → under **Additional application settings → Origin server → HTTP Host header**, set the value to the LAN IP/port. Save.
- **Config file (cloudflared):**
  ```yaml
  tunnel: <id>
  credentials-file: /root/.cloudflared/<id>.json
  ingress:
    - hostname: mf.xuup.top
      service: http://192.168.0.222:2099
      originRequest:
        httpHostHeader: 192.168.0.222:2099
    - service: http_status:404
  ```
  Reload: `cloudflared tunnel run <id>` (or restart the systemd service).

### Pattern C — Multi-instance (last resort)

Run **N** copies of the app on different host ports, each with its own `BETTER_AUTH_URL` and ideally a separate database (or at least a separate first-admin slot). This is the only way to cover all three networks with one machine, and it doubles the maintenance surface. Use only when Patterns A/B are unacceptable.

## Verification after change

A healthy `/api/v1/health` 200 is **not** enough — it doesn't go through the auth path. Verify the actual signup:

```bash
# 1. Probe the app with the Host header the browser will send
curl -s -H "Host: 192.168.0.222:2099" http://localhost:2099/api/v1/health
curl -s -H "Host: mf.xuup.top" https://mf.xuup.top/api/v1/health

# 2. Attempt signup with a real email (or test endpoint if available)
curl -X POST -H "Host: 192.168.0.222:2099" -H "Content-Type: application/json" \
  -d '{"email":"test@example.com","password":"...","name":"Test"}' \
  http://localhost:2099/api/v1/setup/admin

# 3. Confirm the browser flow end-to-end
#    - Open the URL in a real browser
#    - Submit the signup form
#    - Confirm the red "Invalid origin" banner is gone
#    - Confirm the user lands on the dashboard
```

## Common mistakes to avoid

- **Comma-separated `BETTER_AUTH_URL`.** Better Auth does not parse multiple values. The trustedOrigins log line showing a single value duplicated is not a hint to add more.
- **Trusting the dashboard-tunnel log line as a config knob.** The "If it's a valid URL, please add ... to trustedOrigins" message is informational only — the trustedOrigins list is hardcoded in the app's source/DB. Without modifying the image, env vars are the only handle.
- **Restarting the app but forgetting the browser cache.** After a `BETTER_AUTH_URL` change, hard-refresh the signup page (Ctrl+Shift+R). A stale browser session can keep the old origin in the form's request and produce the same error.
- **Setting httpHostHeader to the tunnel hostname.** That would tell the app the request came from `mf.xuup.top` while `BETTER_AUTH_URL` is the LAN IP — still a mismatch. Set httpHostHeader to the **same value as `BETTER_AUTH_URL`**.
- **Health 200 on the public URL is not enough.** `/api/v1/health` often bypasses Better Auth. After tunnel + Host-header changes, verify signup/login in a browser.
- **Automated probes and Cloudflare:** Python `urllib` default User-Agent may get **HTTP 403** on `https://mf.xuup.top` while `curl` returns 200. Use `User-Agent: curl/8.0` in scripts (`ai-model-smoke-test/scripts/hermes-verify-public-health.py`).

## Real-world example: Manifest on port 2099

This is the exact pattern used in production for the [Manifest LLM router](https://manifest.build/docs/self-hosted):

- App image: `manifestdotbuild/manifest`
- Stack: `docker-compose.yml` with `postgres` + `manifest` services
- Default port: 2099
- `BETTER_AUTH_SECRET` must be 32+ random bytes (set via `openssl rand -hex 32`)
- `BETTER_AUTH_URL` is the single trusted origin
- Image logs telemetry by default; opt out with `MANIFEST_TELEMETRY_DISABLED=1`
- Image warns if `MANIFEST_ENCRYPTION_KEY` is not set separately from `BETTER_AUTH_SECRET` — they should be different secrets to limit blast radius
- A warning about HSTS being disabled appears if `BETTER_AUTH_URL` is HTTP (expected for LAN-only; expected to be HTTPS for public)
- A `MANIFEST_ENCRYPTION_KEY` warning means the app falls back to using `BETTER_AUTH_SECRET` for both session signing and at-rest provider key encryption — set a separate 32+ char secret to avoid the leak

`docker-compose.yml` skeleton (omit `httpHostHeader` config — that lives in cloudflared, not the app):

```yaml
services:
  postgres:
    image: postgres:16-alpine
    restart: unless-stopped
    environment:
      POSTGRES_DB: manifest
      POSTGRES_USER: manifest
      POSTGRES_PASSWORD: ${POSTGRES_PASSWORD}
    volumes:
      - postgres_data:/var/lib/postgresql/data
    healthcheck:
      test: ["CMD-SHELL", "pg_isready -U manifest -d manifest"]
      interval: 10s
      timeout: 5s
      retries: 5
  manifest:
    image: manifestdotbuild/manifest:latest
    restart: unless-stopped
    ports:
      - "2099:2099"
    environment:
      DATABASE_URL: ${DATABASE_URL}
      BETTER_AUTH_SECRET: ${BETTER_AUTH_SECRET}
      BETTER_AUTH_URL: ${BETTER_AUTH_URL}   # set to ONE canonical URL
      PORT: "2099"
    depends_on:
      postgres:
        condition: service_healthy
volumes:
  postgres_data:
```

`.env` skeleton:

```env
POSTGRES_PASSWORD=*** rand -hex 16>
DATABASE_URL=postgresql://manifest:***@postgres:5432/manifest
BETTER_AUTH_SECRET=*** rand -hex 32>
BETTER_AUTH_URL=http:/...2099   # or https://mf.xuup.top — pick one
MANIFEST_ENCRYPTION_KEY=<openssl rand -hex 32>   # recommended, separate from auth secret
MANIFEST_TELEMETRY_DISABLED=1   # optional
```

## When this skill is wrong

If the app does not use Better Auth, this pattern is irrelevant. Other auth libraries (NextAuth/Auth.js, Clerk, custom JWT) have their own trusted-origin logic and may support multiple origins natively via comma-separated env or a `ALLOWED_ORIGINS` env var. Check the auth lib before assuming single-origin is the constraint.
