---
name: ai-gateway-docker-deployment
description: Install and operate self-hosted AI gateway / proxy products in Docker, including host-network deployments, DB-backed startup, LAN exposure, and post-install verification.
version: 1.0.0
author: Hermes Agent
license: MIT
metadata:
  hermes:
    tags: [docker, ai-gateway, proxy, litellm, openai-compatible, self-hosting, postgres, host-networking, lan]
---

# AI Gateway Docker Deployment

Deploy self-hosted AI gateway / proxy products that sit in front of one or more model providers and expose an OpenAI-compatible or gateway-style API/UI.

Examples in this class:
- LiteLLM
- similar DB-backed model gateways
- admin/UI + API proxy stacks for LLM routing
- OmniRoute (`diegosouzapw/omniroute:latest`) — single container, host-network, port 20128, data at `/app/data`. No compose file; standalone `docker run -d --network host -v <data>:/app/data`. Update by pull+stop+rm+run.

## When to use
- The user wants an AI gateway installed in Docker.
- The user wants host networking instead of bridge mode.
- The user wants the service reachable from LAN immediately.
- The product has first-boot DB migrations and a health/UI path that must be verified.

## Core rules
1. Prefer a **minimal stack first**.
   - gateway + postgres is usually enough
   - skip prometheus/redis/extras unless the user asked for them
2. If the user asks for **host networking**, actually use `network_mode: host` and avoid fake bridge+ports equivalence.
3. For host networking with bundled Postgres, move Postgres off the common default if needed.
   - Example durable pattern: app on `4000`, Postgres on `5433`
4. Verify **LAN reachability**, not just localhost.
5. Treat first-boot migrations as part of the install, not as a failure by default.

## Recommended install pattern

### 1. Pick a clean app directory
Use the user's preferred self-hosted app root if known. Keep the app in its own directory with:
- `docker-compose.yml`
- `.env`
- short operator README

### 2. Generate secrets up front
For DB-backed gateways, generate and store before first boot:
- master/admin key
- salt/encryption key
- postgres password

Important: if the product documents that the salt/encryption key becomes part of stored credential encryption, treat it as **immutable after models/credentials are added**.

### 3. Write a minimal compose
For host-network installs:
- set both containers to `network_mode: host`
- remove `ports:` blocks unless the product requires them for non-host mode
- point app `DATABASE_URL` at `127.0.0.1:<db-port>`
- give Postgres an explicit non-conflicting host port via command args if needed

### 4. Validate compose before startup
Always run:
- `docker compose config`

Do not proceed until YAML/env interpolation is clean.

### 5. Start and expect a slow first boot
Use:
- `docker compose up -d`

Then watch for:
- image pulls
- DB init
- schema migrations
- app startup banner
- health endpoint becoming ready

Do not mislabel long migration output as a crash unless the process exits or loops.

### 6. Verify four things
Minimum verification set:
1. container state / health
2. network mode really is `host`
3. listening sockets on the expected host ports
4. local **and LAN** HTTP health

### 7. Verify the UI path separately
Many gateways have:
- API/Swagger at `/`
- UI at `/ui` or a redirected subpath

Check the real behavior:
- status code
- redirect target if any
- final HTML load

## UI auth pattern
If the product supports overriding default UI login with env vars, prefer explicit credentials over default admin behavior.

For LiteLLM specifically, set in `.env`:
- `UI_USERNAME`
- `UI_PASSWORD`

This changes UI login only. It does **not** replace the proxy master key or virtual-key auth model.

**Critical Docker rule:** if those values come from `env_file:` / `.env`, a plain `docker compose restart` is not enough. Restart keeps the existing container environment. After changing UI credential env vars, recreate the app container:
- `docker compose up -d --force-recreate --no-deps <service>`

Then verify inside the live container that the vars are present before debugging the browser login flow.

## Product-specific install notes
- LiteLLM fits this skill directly: DB-backed, health/UI split, host-network deploy works well.
- 9router also fits this class operationally even though it is not DB-backed by default: single container, dashboard + API on one port, supports Docker, `PORT` override, and `HOSTNAME=0.0.0.0` for LAN exposure. Set `TZ` (e.g. `Asia/Dhaka`) in compose `environment` and **recreate** the container.
- If the user wants two router products side-by-side on host networking, they must use different app listen ports. With host mode there is no port-mapping layer to save you. **Pitfall:** 9router built-in tunnel health-check may assume default port **20128** while compose uses `PORT=20111` — prefer external Cloudflare Tunnel to the real listen port.

See also:
- `references/litellm-host-network-minimal-compose.md`
- `references/router-products-host-network-port-patterns.md`
- `references/9router-dashboard-customization.md` — TZ, Usage periods (90D–All), tunnel pitfall
- `scripts/apply-9router-usage-periods.py` — re-apply usage dropdown after 9router image update

## Durable pitfalls

### Pitfall: compose patching can silently break `depends_on`
When patching YAML blocks around `environment:` / `depends_on:`, re-run `docker compose config` immediately. A malformed compose can look visually fine and still fail schema validation.

### Pitfall: `docker compose up -d` may still look long-running in wrappers
Some terminal wrappers misclassify `docker compose up -d` when large image pulls happen. If that happens, rerun in a bounded shell form and inspect `docker compose ps` + logs instead of assuming the stack failed.

On **Hermes Agent**, foreground `docker compose up -d --force-recreate` can be hard-rejected as starting a long-lived process even with `-d`. Use background execution for recreate, then verify health in a separate command.

### FreeLLMAPI (this host)
- Clone: `/root/freellmapi` (not under `/mnt/tb/1Apps`)
- Image: `ghcr.io/tashfeenahmed/freellmapi:latest`, host network, port **3055**
- Checklist: `references/freellmapi-docker-update.md`

### Pitfall: health can lag behind successful migrations
A DB-backed gateway may finish migrations first, then start the HTTP server later. During that window:
- container can be `running`
- app health can still be `starting`
- ports may not yet be bound

Wait for the actual health endpoint before claiming success.

### Pitfall: `/ui` may redirect
A 307 on `/ui` can be correct if it redirects to `/ui/`. Follow redirects before deciding the UI is broken.

### Pitfall: `network_mode: host` is runtime-only — builds still use bridge

When `docker-compose.yml` has `network_mode: host`, that applies to the **running container only**. During `docker compose build`, pip/npm/apt inside the Dockerfile still uses the default bridge network. If the host has bridge-network egress issues (common on DietPi, some VPS configs), builds fail with:

```
ERROR: Could not install packages due to an OSError: HTTPSConnectionPool(host='files.pythonhosted.org', port=443): Max retries exceeded
[Errno 101] Network is unreachable
```

**Fix:** Add `network: host` to the build config in docker-compose.yml:

```yaml
services:
  myservice:
    build:
      context: .
      network: host   # ← forces build-time networking to use host stack
    network_mode: host  # ← runtime
```

Or pass it on the CLI: `docker build --network=host .`

**Note:** BuildKit's `RUN --mount=type=cache` syntax is NOT supported by all Docker daemons. If you get `the --mount option requires BuildKit`, either enable BuildKit explicitly (`DOCKER_BUILDKIT=1`) or remove the mount directive — don't assume it works.

### Pitfall: host networking + port conflicts when switching between dev and Docker

When using `network_mode: host`, the container binds directly to host ports. If you previously ran the app directly on the host (e.g., `uvicorn` on port 8866 for testing), the Docker container will fail with:

```
[Errno 98] error while attempting to bind on address ('0.0.0.0', 8866): address already in use
```

**Always kill host-side processes before starting the Docker container:**
```bash
fuser -k 8866/tcp 2>/dev/null; sleep 1
docker compose up -d
```

Or use a different port for dev testing than production Docker.

## Verification checklist
- [ ] `docker compose config` passes
- [ ] stack starts without exit loops
- [ ] DB is healthy
- [ ] app container is healthy or serving the documented health endpoint
- [ ] `docker inspect` confirms `host` networking when requested
- [ ] expected host ports are listening
- [ ] localhost health returns expected body/code
- [ ] LAN health returns expected body/code
- [ ] UI route loads or redirects correctly
- [ ] operator README notes paths, ports, and restart commands

## References
- `references/litellm-host-network-minimal-compose.md` — LiteLLM-specific host-network install notes, env vars, and verification flow.
- `references/freellmapi-docker-update.md` — FreeLLMAPI pull/recreate/verify (`/root/freellmapi`, `:3055/api/ping`).
- `references/9router-dashboard-customization.md` — 9router TZ, Usage period patch, tunnel port mismatch.
- `scripts/apply-9router-usage-periods.py` — extend Usage dropdown to 90D/180D/365D/All (ephemeral; re-run after image pull).
