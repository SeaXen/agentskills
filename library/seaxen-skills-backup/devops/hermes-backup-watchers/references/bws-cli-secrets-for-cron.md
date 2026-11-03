# Bitwarden Secrets Manager CLI for Cron Subprocesses

## Problem

User has secrets in Bitwarden Secrets Manager (BWS) that are injected into the Hermes gateway process via Bitwarden Secrets Manager integration. **Cron subprocesses (`no_agent: true` scripts) do NOT inherit this injection** — they run in a clean environment without the injected env vars.

This caused OpenRouter watch cron jobs to fail with `OPENROUTER_API_KEY not found` even though the secret existed in Bitwarden.

## Solution: Use bws CLI Directly in Scripts

Install the `bws` CLI and have scripts fetch secrets directly using the secret ID.

### Installation

```bash
curl -L -o /tmp/bws.zip https://github.com/bitwarden/sdk-sm/releases/download/bws-v1.0.0/bws-x86_64-unknown-linux-gnu-1.0.0.zip
unzip -o /tmp/bws.zip -d /tmp/bws-extract/
cp /tmp/bws-extract/bws /usr/local/bin/bws
chmod +x /usr/local/bin/bws
bws --version  # → bws 1.0.0
```

### Finding Secret ID

```bash
bws secret list
# Find the secret with key "OPENROUTER_API_KEY"
# Note the "id" field (UUID)
```

Example output:
```json
{
  "id": "f6ee6e99-3f56-410a-8a19-b4590070c320",
  "key": "OPENROUTER_API_KEY",
  "value": "sk-or-...",
  ...
}
```

### Python Script Pattern

```python
import subprocess
import json

def _get_bws_key(secret_id: str) -> str:
    """Get secret value from Bitwarden Secrets Manager via bws CLI."""
    try:
        result = subprocess.run(
            ['bws', 'secret', 'get', secret_id],
            capture_output=True,
            text=True,
            timeout=10
        )
        if result.returncode == 0:
            secret = json.loads(result.stdout)
            return secret.get('value', '').strip()
    except Exception:
        pass
    return ''

def load_env_key():
    # 1. Try bws CLI first (Bitwarden Secrets Manager)
    key = _get_bws_key('f6ee6e99-3f56-410a-8a19-b4590070c320')
    if key:
        return key
    
    # 2. Fallback to environment variable
    key = os.environ.get('OPENROUTER_API_KEY', '').strip()
    if key:
        return key
    
    # 3. Fallback to .env files
    for path in ENV_PATHS:
        if path.exists():
            for line in path.read_text().splitlines():
                if line.startswith('OPENROUTER_API_KEY='):
                    return line.split('=', 1)[1].strip()
    
    return ''
```

### Priority Order

1. **bws CLI** — Works in cron subprocesses (no injection needed)
2. **Environment variable** — Works if injected or set in .env
3. **`.env` file** — Local fallback

### Applied Fixes

- `/root/.hermes/scripts/openrouter_free_watch.py` — Updated `_get_bws_key()` with correct secret ID
- `/root/.hermes/scripts/openrouter_free_watch_heartbeat.py` — Same fix

### Notes

- bws CLI requires authentication (device approval or access token) on first run
- After auth, token is cached and subsequent runs work non-interactively
- Secret ID is stable — use it instead of secret name for reliability
- The `bws secret get <ID>` returns full JSON with the decrypted `value` field