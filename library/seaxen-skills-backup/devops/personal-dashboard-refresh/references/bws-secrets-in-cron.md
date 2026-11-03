# BWS Secrets in Cron Subprocesses

## Problem

Hermes gateway injects Bitwarden Secrets Manager (BWS) secrets as environment variables into its **own process**. However, cron jobs with `no_agent: true` run as **standalone Python subprocesses** that do NOT inherit the gateway's environment.

### What works
- Hermes gateway process → has BWS-injected env vars (e.g., `OPENROUTER_API_KEY`, `TELEGRAM_BOT_TOKEN`)
- `hermes` CLI commands → run in gateway context, have access

### What doesn't work
- Cron `no_agent: true` scripts → fresh Python process, **no BWS env vars**
- Cron `skills: [...]` with LLM → runs in gateway, has BWS env vars
- Manual `python3 script.py` from shell → no BWS env vars

## Affected Scripts

| Script | Needs | Current Behavior |
|--------|-------|------------------|
| `openrouter_free_watch.py` | `OPENROUTER_API_KEY` | Falls back to `.env` (placeholder only → 401) |
| `openrouter_free_watch_heartbeat.py` | `OPENROUTER_API_KEY` | Same |
| `bitwarden-fetch-watchdog.sh` | BWS token | Runs as shell, may have different env |

## Solutions

### Option 1: Add Real Keys to `.env` (Simplest)

```bash
echo 'OPENROUTER_API_KEY=sk-or-...' >> /root/.hermes/.env
```

Scripts already check `.env` as fallback.

### Option 2: BWS CLI in Scripts (Implemented)

Added `_get_bws_key()` function to both OpenRouter scripts:

```python
def _get_bws_key():
    try:
        result = subprocess.run(
            ['bws', 'secret', 'get', 'openrouter-api-key'],
            capture_output=True, text=True, timeout=10
        )
        if result.returncode == 0:
            secret = json.loads(result.stdout)
            return secret.get('value', '').strip()
    except Exception:
        pass
    # Fallback: list secrets and find openrouter
    ...
```

**Limitation**: `bws` CLI is not installed on the system.

### Option 3: Hermes Injects to Cron Subprocesses (Future)

Would require Hermes scheduler to load BWS secrets and pass them to `no_agent: true` subprocesses. Not currently implemented.

## Priority Order in Scripts

1. **BWS CLI** — `bws secret get openrouter-api-key`
2. **Environment variable** — `os.environ.get('OPENROUTER_API_KEY')`
3. **`.env` file** — `/root/.hermes/.env` or `/mnt/tb/hermes/.env`

## Verification

Test if key is available in cron context:

```bash
# Simulate cron environment (no BWS)
env -i PATH=/usr/bin:/bin python3 -c "import os; print(os.environ.get('OPENROUTER_API_KEY', 'NOT FOUND'))"
```

Should print the key from `.env` if added, or `NOT FOUND`.

## Related

- `references/standalone-scripts.md` — Dashboard scripts also affected
- OpenRouter scripts: `/root/.hermes/scripts/openrouter_free_watch*.py`
- `.env` location: `/root/.hermes/.env` (credential store, protected from direct read)