# OmniRoute update notes — release lag, relay verification, and post-update hangs (2026-07)

## When this mattered
- GitHub release/changelog claimed a fix (v3.8.45 / #6149), but Docker `latest` had not actually moved yet.
- After updating, OmniRoute accepted TCP on `:20128` but returned no HTTP response and showed `unhealthy`.
- Relay deploy checks needed separation between token/account problems and OmniRoute-generated worker bugs.

## 1) Do not trust GitHub release page as proof Docker `latest` has the fix
A GitHub release can be live while Docker Hub `latest` is still on the previous build.

### Reliable version check for Docker `latest`
```bash
docker run --rm diegosouzapw/omniroute:latest node -e "const p=require('/app/package.json'); console.log(p.version);"
```
Use this instead of assuming `latest` matches the newest GitHub release.

### Important edge case
An explicit tag can be mentioned in the release notes but still not exist on Docker Hub yet. Example pattern:
- GitHub shows `v3.8.45`
- `docker pull diegosouzapw/omniroute:v3.8.45` returns `not found`
- `latest` is still `3.8.44`

Operational rule: if the tag 404s, revert compose back to `latest`, bring the app back up, and wait for the registry publish.

## 2) If OmniRoute binds `:20128` but browser hangs with no response after update
Symptoms:
- `ss` shows port `20128` listening
- TCP connect succeeds on `127.0.0.1:20128` and LAN IP
- `curl` times out with **0 bytes received**
- container status shows `unhealthy`
- healthcheck is `node healthcheck.mjs` with 5s timeout

### Logs that point to the real issue
Look for repeated patterns like:
- `[ProxyFetch] ... HeadersTimeoutError ...`
- `[ProxyHealth] Sweep complete: 1 tested, 0 alive ...`
- `ModelSync ... fetch failed`

Interpretation: the background proxy-health / proxy-fetch path is wedging startup enough that HTTP accepts connections but does not finish responding.

### Working fix
Disable the background proxy health scheduler in OmniRoute env and recreate the container:

`data/server.env`
```env
PROXY_HEALTH_ENABLED=false
```

Then recreate:
```bash
docker compose up -d --force-recreate
```

### Verification after the fix
Expect all of these:
- `docker compose ps` -> `healthy`
- `curl http://127.0.0.1:20128/` -> `307 /dashboard`
- `curl http://<LAN-IP>:20128/` -> `307 /dashboard`
- logs show normal model sync completion again

## 3) Relay debugging: separate account/token validity from OmniRoute deploy bugs
### Vercel
Token validity can be checked independently with:
```bash
curl -H "Authorization: Bearer $VERCEL_TOKEN" https://api.vercel.com/v2/user
```
If this succeeds, the token is not the cause.

### Deno
If the API returns `invalidToken`, treat Deno auth as a separate problem from OmniRoute worker generation.

### Cloudflare
Cloudflare Workers account/token validity can be proven independently:
- verify token
- list workers/subdomain
- perform a direct worker upload with `Content-Type: application/javascript`

If direct Cloudflare upload works but OmniRoute UI says:
`Cloudflare Worker upload failed: Content-Type must be one of: application/javascript, text/javascript, multipart/form-data`
then that points to an OmniRoute-side request formatting bug, not a user-side Cloudflare permission issue.

## 4) Practical relay conclusion from this session
- Vercel token path can be valid while OmniRoute relay generation is still broken.
- Deno token can be invalid at the same time; do not conflate Deno auth failure with Vercel/Cloudflare worker-template issues.
- Cloudflare direct API success is strong evidence when OmniRoute UI still fails with a Content-Type upload error.

## 5) Safe operator behavior
- Never leave compose pinned to a non-existent tag after a failed `docker pull`; revert immediately so the app can come back up.
- After any OmniRoute update that touches relays/proxies, verify both:
  1. actual image/app version
  2. HTTP responsiveness on `127.0.0.1:20128` and LAN IP
- If the app becomes `unhealthy` and hangs, check proxy-health before blaming the release itself.
