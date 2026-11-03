# Manifest Docker Compose Deployment Reference

## Overview
Manifest is an open-source LLM router (manifestdotbuild/manifest) that routes requests to the cheapest capable model. Self-hosted deployment via Docker Compose on port 2099.

## Key Configuration Patterns Learned

### 1. Docker Compose Structure (Postgres + App)
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
      BETTER_AUTH_URL: ${BETTER_AUTH_URL}
      PORT: "2099"
    depends_on:
      postgres:
        condition: service_healthy

volumes:
  postgres_data:
```

### 2. Critical .env Pattern — Use Variable Substitution in DATABASE_URL
The `DATABASE_URL` in docker-compose.yml MUST reference `${DATABASE_URL}` from .env, NOT a hardcoded value. The .env file contains the real password.

```env
# .env
POSTGRES_PASSWORD=<generated_urlsafe_32>
BETTER_AUTH_SECRET=<openssl_rand_hex_32>
BETTER_AUTH_URL=http://localhost:2099
DATABASE_URL=postgresql://manifest:${POSTGRES_PASSWORD}@postgres:5432/manifest
```

### 3. Secret Generation
```bash
# Postgres password (URL-safe, no special chars that need encoding)
openssl rand -base64 32 | tr -d /=+

# BETTER_AUTH_SECRET (64 hex chars)
openssl rand -hex 32
```

### 4. .env Writing Gotcha with Terminal Tool
Hermes terminal tool masks secret-like strings in output (shows `***`). To write actual values:
- Use `execute_code` with Python file write, OR
- Write a script and execute it, OR
- Use heredoc with actual values (but terminal may mask)

Best pattern: generate in Python, write file directly via `execute_code`.

### 5. LAN Exposure
Default compose binds to all interfaces (`0.0.0.0:2099:2099`). For LAN access:
1. Keep ports as `"2099:2099"` (binds 0.0.0.0)
2. Update `.env`: `BETTER_AUTH_URL=http://<lan-ip>:2099`
3. `docker compose up -d`

### 6. Health Verification
```bash
# Container health
docker ps --filter name=manifest --format 'table {{.Names}}\t{{.Status}}'

# Service health
curl -fsS http://localhost:2099/api/v1/health
# Returns: {"status":"healthy","uptime_seconds":...}

# Logs
docker compose logs -f manifest
```

### 7. First-Run Setup
1. Open `http://localhost:2099` → sign up (first account = admin)
2. Go to Routing page → add LLM providers with API keys
3. Get Manifest API key (starts with `mnfst_`) from dashboard
4. Use as OpenAI-compatible endpoint: `http://localhost:2099/v1/chat/completions`

## Reusable Deployment Checklist
- [ ] Create project directory
- [ ] Generate secrets (Postgres password, BETTER_AUTH_SECRET)
- [ ] Write docker-compose.yml with variable substitution for DATABASE_URL
- [ ] Write .env with actual secret values (use execute_code for reliable writes)
- [ ] `docker compose up -d`
- [ ] Wait for postgres healthcheck + manifest startup
- [ ] Verify `/api/v1/health` returns healthy
- [ ] Complete first-run setup in browser
- [ ] Update BETTER_AUTH_URL if exposing beyond localhost

## Reference: Manifest Self-Hosted Docs
- https://manifest.build/docs/self-hosted
- https://hub.docker.com/r/manifestdotbuild/manifest

## Connection to Hermes Dashboard Pattern
Similar pattern used for Hermes Personal Dashboard (port 8009) — both are self-hosted web services with Postgres backend via Docker Compose. This pattern generalizes to: **any self-hosted service with Postgres + web UI deployed via Docker Compose**.