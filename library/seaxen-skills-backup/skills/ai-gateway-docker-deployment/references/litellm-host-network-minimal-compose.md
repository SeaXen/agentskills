# LiteLLM host-network minimal compose

Session-derived pattern for installing LiteLLM as a LAN-reachable Docker app with host networking.

## Why this pattern
- User wanted LAN access.
- User explicitly wanted `network_mode: host`.
- Minimal stack was preferred over the upstream compose with Prometheus.

## Concrete shape
- app directory: `/mnt/tb/1Apps/litellm`
- containers:
  - `litellm`
  - `litellm-db`
- host ports:
  - LiteLLM: `4000`
  - Postgres: `5433`

## Required env vars
- `LITELLM_MASTER_KEY`
- `LITELLM_SALT_KEY`
- `POSTGRES_PASSWORD`
- `DATABASE_URL`
- optional UI overrides:
  - `UI_USERNAME`
  - `UI_PASSWORD`

## Important LiteLLM facts confirmed from docs
- UI credentials can be changed via `UI_USERNAME` and `UI_PASSWORD`.
- Default UI auth otherwise falls back to admin + master key behavior.
- `LITELLM_SALT_KEY` should not be changed after adding models/credentials.

## Startup behavior worth expecting
First boot can take a while because LiteLLM may:
1. run `prisma migrate deploy`
2. run post-migration sanity checks / diff generation
3. only then bind `0.0.0.0:4000`

So during install it is normal to see:
- DB healthy first
- app container `running` but health still `starting`
- no listener on `4000` yet
- long migration logs before HTTP becomes ready

Do not call it broken too early.

## Verification pattern that worked
1. `docker compose config`
2. `docker compose up -d`
3. `docker compose ps`
4. `docker logs --tail ... litellm litellm-db`
5. `docker inspect` for network mode + health
6. `ss -ltn` for `4000` and `5433`
7. curl local health:
   - `http://127.0.0.1:4000/health/liveliness`
8. curl LAN health:
   - `http://<lan-ip>:4000/health/liveliness`
9. check UI separately:
   - `/ui` may 307 redirect to `/ui/`
   - follow redirects before judging it

## Real pitfalls hit in session
### 1. Compose patch drift around `depends_on`
A quick patch accidentally malformed the compose structure under `environment:`. `docker compose config` caught it immediately. Lesson: after any YAML patch near `environment:` / `depends_on:`, validate before startup.

### 2. Wrapper false-positive on `docker compose up -d`
A terminal wrapper flagged `docker compose up -d` as if it were starting a long-lived foreground server. Bounded shell execution plus `docker compose ps`/logs was the correct fallback.

### 3. `/ui` route semantics
LiteLLM served health first, then `/ui` returned `307` to `/ui/`. That redirect was correct; the final HTML loaded after following redirects.

## Good operator summary to leave behind
Document in a local README:
- compose path
- env path
- host ports
- LAN URL
- restart/log commands
- note that UI credentials and proxy master key are separate concerns
