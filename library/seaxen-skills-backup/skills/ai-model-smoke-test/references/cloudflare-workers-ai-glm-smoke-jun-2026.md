# Cloudflare Workers AI — account-scoped OpenAI + `/ai/run` smoke (Jun 2026)

## Endpoints (same account)

| Path | Use |
|---|---|
| `https://api.cloudflare.com/client/v4/accounts/{ACCOUNT_ID}/ai/v1/chat/completions` | Hermes `custom_providers` base_url (OpenAI-compat) |
| `https://api.cloudflare.com/client/v4/accounts/{ACCOUNT_ID}/ai/run/{MODEL}` | Direct run (messages JSON, no `model` in body) |

Auth: `Authorization: Bearer {cfut_...}` Workers AI / API token with AI permissions.

Model example: `@cf/zai-org/glm-5.2` (reasoning model).

## Verified minimal probe

```python
# Token: read from file — NOT inline in shell (redaction → literal *** → 401)
from pathlib import Path
import json, urllib.request, urllib.error

TOKEN = Path("/tmp/cf_token.txt").read_text().strip()
ACCT = "<account_id>"
MODEL = "@cf/zai-org/glm-5.2"

def post(url, body):
    req = urllib.request.Request(
        url, data=json.dumps(body).encode(),
        headers={"Authorization": "Bearer " + TOKEN, "Content-Type": "application/json"},
        method="POST",
    )
    try:
        with urllib.request.urlopen(req, timeout=120) as r:
            return r.status, r.read().decode()[:5000]
    except urllib.error.HTTPError as e:
        return e.code, e.read().decode()[:5000]

url_run = f"https://api.cloudflare.com/client/v4/accounts/{ACCT}/ai/run/{MODEL}"
code, body = post(url_run, {"messages": [{"role": "user", "content": "Reply with exactly: OK"}]})
```

**Live result:** `ai/run` HTTP **200**, `message.content` = `OK`.

`ai/v1/chat/completions` HTTP **200** but with `max_tokens: 32` and reasoning models, `content` may be **empty** — text in `reasoning_content`. Use `max_tokens` ≥ 256 for a visible `content` field.

## Hermes wiring

```yaml
custom_providers:
  - name: Cloudflare GLM 5.2
    base_url: https://api.cloudflare.com/client/v4/accounts/<ACCOUNT_ID>/ai/v1
    api_key: cfut_...
    model: "@cf/zai-org/glm-5.2"
```

## Pitfalls

- Inline `export CF_TOKEN='...'` in agent terminal may be redacted to `***` → false 401.
- Posted tokens in chat → rotate in Cloudflare dashboard.
- Reasoning models ≠ empty API — bump `max_tokens`.