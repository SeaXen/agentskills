# API Server Placeholder/Weak Key Refusal

Symptom: Hermes gateway is `active (running)` but the API server is not listening and dashboard/connectivity checks show it disconnected.

Exact log message from `journalctl --user -u hermes-gateway.service`:

```
ERROR gateway.platforms.api_server: [Api_Server] Refusing to start: API_SERVER_KEY is a placeholder or too short (<16 chars). This endpoint dispatches terminal-capable agent work — a guessable key is remote code execution. Generate a strong secret (e.g. `openssl rand -hex 32`) and set API_SERVER_KEY before starting the API server on 127.0.0.1.
WARNING gateway.run: ✗ api_server failed to connect
```

## Root Cause

`API_SERVER_KEY` is set to a placeholder, obvious password, or string shorter than 16 characters somewhere in Hermes config. The gateway intentionally refuses to bind the API endpoint because it is a high-privilege dispatch surface.

## Fix

1. Generate a real secret:
   ```bash
   NEW_KEY=$(openssl rand -hex 32)   # 64 hex chars
   ```

2. Update ALL Hermes config locations that contain `API_SERVER_KEY`:
   - `~/.hermes/.env` → `API_SERVER_KEY=<hex>`
   - `~/.hermes/config.yaml` → `API_SERVER_KEY: <hex>` (top-level key, inside config body)
   - Each active profile: `~/.hermes/profiles/<name>/.env` and `~/.hermes/profiles/<name>/config.yaml` if present

3. `.env` format caveat: inside `.env`, use `API_SERVER_KEY=<value>`, NOT `API_SERVER_KEY: <value>`. The colon variant silently breaks dotenv parsing and can cause credential injection failures without obvious errors.

4. `hermes config set api_server_key <hex>` updates the main config, but configs may still carry legacy `API_SERVER_KEY:` keys. After using `hermes config set`, grep for both `API_SERVER_KEY:` and `api_server_key:` and normalize so only one strong `API_SERVER_KEY:` remains.

5. Restart:
   ```bash
   hermes gateway restart
   ```

6. Verify:
   ```bash
   ss -tlnp | grep <expected-api-port>
   curl -s -o /tmp/check -w "%{http_code}" http://127.0.0.1:<expected-api-port>/api/status -H "Authorization: Bearer <hex-key>"
   ```

   A `404` with the expected port listening is healthy — the specific `/api/status` route may differ by Hermes version.

## Short value patterns that trigger refusal

- `opop@9900`
- `changeme`
- anything under 16 chars
- obvious dictionary/pattern-based placeholders

## Why the .env .yaml split matters

Hermes loads secrets from both `config.yaml` (YAML) and `.env` (dotenv). If only one path is updated, the other stale value may still be used depending on load order. Check all four canonical paths before declaring fixed.
