# Manifest `auto` + Hermes — Jun 2026 case study

Worked example for the **Manifest** section of `ai-model-smoke-test`. User asked whether Manifest custom provider with `default_model: auto` works in Hermes.

## Config (Hermes `providers:`)

```yaml
providers:
  manifest:
    api: https://app.manifest.build/v1
    api_key: mnfst_...
    default_model: auto
    name: Manifest
```

## Expected behavior

- Glossary: only client model id that triggers routing is **`auto`** (`manifest/auto`). Any other id is forwarded as-is.  
  https://manifest.build/docs/reference/glossary.md
- `GET /v1/models` returns a single entry: `id: auto`, `display_name: Manifest Auto`.
- Fresh agents with no Routing providers return **M101** in the body (not generic 404).

## Live results (this session)

| Test | Result |
|---|---|
| `GET /v1/models` | 200, only `auto` |
| `POST /v1/chat/completions` `model: auto` | 404 `upstream_error` |
| `hermes chat -Q … --provider manifest -m auto --max-turns 0` | Same 404 |
| `hermes … --provider custom:manifest` | Same (slug alias OK) |

## Response headers prove routing worked

On HTTP 404 from Manifest chat, headers included:

```
X-Manifest-Tier: default
X-Manifest-Model: custom:dcdd4ad3-9a5f-4c06-af43-090ce61defd3/deepseek-v4-flash
X-Manifest-Provider: custom:dcdd4ad3-9a5f-4c06-af43-090ce61defd3
X-Manifest-Confidence: 1
X-Manifest-Reason: default
```

Body:

```json
{"error":{"message":"Model or endpoint not found","type":"upstream_error","status":404}}
```

**Interpretation:** Manifest selected tier `default` → custom provider UUID → `deepseek-v4-flash`. The upstream custom endpoint (OpenModel-class) returned 404 — same DeepSeek channel issue as direct OpenModel probes.

Hermes ↔ Manifest integration: **OK**. Fix **Manifest Routing** (tier model, fallback chain, or custom provider URL/key), not Hermes `api_mode`.

## Header capture snippet

```python
import json, urllib.request, urllib.error

body = json.dumps({
    "model": "auto",
    "max_tokens": 32,
    "messages": [{"role": "user", "content": "PONG"}],
}).encode()
req = urllib.request.Request(
    "https://app.manifest.build/v1/chat/completions",
    data=body,
    method="POST",
    headers={"Authorization": f"Bearer {KEY}", "Content-Type": "application/json"},
)
try:
    urllib.request.urlopen(req, timeout=90)
except urllib.error.HTTPError as e:
    for k, v in e.headers.items():
        if "manifest" in k.lower():
            print(k, v)
    print(e.read().decode()[:500])
```

## Dashboard fixes

1. **Routing** — ensure custom provider base URL and key match a live endpoint.
2. **Tier `default`** — point primary model at a verified slug (e.g. OpenRouter or OpenModel `glm-5` when DeepSeek channel is down).
3. **Fallback chain** — https://manifest.build/docs/fallback.md

## M101 vs upstream_error

| Error | Layer |
|---|---|
| `[🦚 Manifest M101]` | No providers connected to agent |
| `upstream_error` + `X-Manifest-Model` set | Router OK, upstream failed |