# OpenModel gateway — Jun 2026 case study

Concrete session finding from verifying an OpenModel API key. Use as a worked example for the "Third-party multi-protocol gateway verification" and **Hermes custom_providers** sections of `ai-model-smoke-test`.

## What the user provided

| Item | User value | Correct value |
|---|---|---|
| Docs URL | `https://docs.openmodel.ai/en` | ✅ correct (HTTP 200, real Next.js docs) |
| API base URL | `https://api.openmodel.app/v1` | ❌ **TLD typo** — real host is `https://api.openmodel.ai/v1` |
| API key | `om-…` (om- prefix) | ✅ valid (authenticated successfully) |
| Model | `deepseek-v4-flash` | ✅ exists in catalog, `supported_protocols: ["messages"]` |

## Hermes integration (Jun 2026 session)

User had OpenModel in `~/.hermes/config.yaml` `custom_providers`:

```yaml
- api_key: om-...
  base_url: https://api.openmodel.ai/v1
  model: deepseek-v4-flash
  name: Api.openmodel.ai
```

| Test | Result |
|---|---|
| `POST https://api.openmodel.ai/v1/messages` (Anthropic body + `anthropic-version`) | **200**, text `PONG` |
| `hermes chat -Q … --provider custom:Api.openmodel.ai -m deepseek-v4-flash --max-turns 0` | **404** `route not found` |
| Logs | `OpenAI client created … provider=custom base_url=https://api.openmodel.ai/v1` |

**Fix:** add `api_mode: anthropic_messages` on that entry. Re-test PONG after user edits config (agent `patch` on `config.yaml` is often blocked).

**Wrong base_url tricks:** `https://api.openmodel.ai/anthropic` and `…/v1/anthropic` + `/messages` → 404. Only `https://api.openmodel.ai/v1/messages` works.

Provider slug: `custom:Api.openmodel.ai` (from `name: Api.openmodel.ai`).

## What the user's own docs site claimed

The OpenModel docs quickstart code block literally shows:

```bash
export OPENAI_BASE_URL="https://api.openmodel.app/v1"
export OPENAI_API_KEY="om_******"
```

So the docs themselves ship the wrong TLD. If the user copied from there, they're not at fault. This is a real failure mode: **docs URL != API URL**, and the gateway provider got it wrong on their own marketing page.

## What worked (raw API)

```bash
KEY=$(tr -d '\n' < /tmp/omkey.txt)

# Catalog (HTTP 200, returned full model list):
curl -s -H "Authorization: Bearer $KEY" https://api.openmodel.ai/v1/models

# Real chat call to deepseek-v4-flash (HTTP 200, real response):
curl -s -X POST \
  -H "Authorization: Bearer $KEY" \
  -H "Content-Type: application/json" \
  -H "anthropic-version: 2023-06-01" \
  -d '{"model":"deepseek-v4-flash","max_tokens":200,"messages":[{"role":"user","content":"Say hi."}]}' \
  https://api.openmodel.ai/v1/messages
```

Response included both a `thinking` block and a `text` block:
```json
{
  "model": "deepseek-v4-flash",
  "content": [
    {"type":"thinking","thinking":"…"},
    {"type":"text","text":"Hi."}
  ],
  "stop_reason": "end_turn",
  "usage": {"input_tokens": 14, "output_tokens": 48}
}
```

## What failed and why (lessons)

| Call | Result | Why |
|---|---|---|
| `GET https://api.openmodel.app/v1/models` | DNS failure (`Could not resolve host`) | Wrong TLD — `.app` doesn't resolve |
| `POST https://api.openmodel.ai/v1/chat/completions` with `deepseek-v4-flash` | HTTP 404 `route not found` | Model declares `supported_protocols: ["messages"]` → must use `/v1/messages` |
| Hermes `custom:Api.openmodel.ai` without `api_mode` | Same 404 in chat | Hermes defaults to OpenAI chat_completions on `base_url` |
| `POST …` from Python with `"Bearer *** " + key` as auth | HTTP 401 `invalid api key` | Literal `***` leaked into bearer string |
| Same call from inline `curl` with `$KEY` from file | HTTP 200 | Load key from file/env, not inline placeholders |

## Catalog snapshot (June 2026)

Models observed in `/v1/models`, grouped by `supported_protocols`:

- `["messages"]` (Anthropic-compatible → use `/v1/messages`; Hermes needs `api_mode: anthropic_messages`):
  - `claude-haiku-4-5-20251001`
  - `claude-opus-4-6`, `claude-opus-4-7`, `claude-opus-4-8`
  - `claude-sonnet-4-6`
  - `deepseek-v4-flash`, `deepseek-v4-pro`
  - `glm-4.7`, `glm-5`, `glm-5.1`, `glm-5.2`
  - `kimi-k2.5`, `kimi-k2.6`
  - `qwen3-max`, `qwen3.6-max-preview`, `qwen3.6-plus`, `qwen3.7-max` (dual-protocol)
- `["responses"]` (OpenAI Responses API → use `/v1/responses`; Hermes `api_mode: codex_responses`):
  - `gpt-5.2`, `gpt-5.2-pro`, `gpt-5.3-codex`, `gpt-5.4`, …
- `["gemini"]` (Gemini native):
  - `gemini-3-flash-preview`, …
- `["images"]` (image generation):
  - `1024-x-1024/gpt-image-1.5`

## Working client configs

Anthropic SDK (for any `["messages"]` model):
```python
import anthropic
client = anthropic.Anthropic(base_url="https://api.openmodel.ai", api_key="om-...")
r = client.messages.create(model="deepseek-v4-flash", max_tokens=256,
    messages=[{"role":"user","content":"Say hi"}])
```

OpenAI SDK (for `["responses"]` models like gpt-5.x):
```python
from openai import OpenAI
client = OpenAI(base_url="https://api.openmodel.ai/v1", api_key="om-...")
r = client.responses.create(model="gpt-5.2", input="Say hi")
```

OpenAI SDK (for `["chat_completions"]` models like qwen3.x):
```python
from openai import OpenAI
client = OpenAI(base_url="https://api.openmodel.ai/v1", api_key="om-...")
r = client.chat.completions.create(model="qwen3.7-max",
    messages=[{"role":"user","content":"Say hi"}])
```

Hermes `custom_providers` (messages-only model):
```yaml
- api_key: om-...
  api_mode: anthropic_messages
  base_url: https://api.openmodel.ai/v1
  model: deepseek-v4-flash
  name: Api.openmodel.ai
```

## DeepSeek channel outages (Jun 2026 follow-up)

After `api_mode: anthropic_messages`, Hermes may still fail with:

```json
{"error":{"message":"no channel available for model deepseek-v4-flash with messages api","type":"not_found_error"}}
```

**Not a Hermes regression.** OpenModel stopped routing DeepSeek on `/v1/messages` while other models on the same key still worked.

| Probe | When channel down |
|---|---|
| `deepseek-v4-flash` via `/v1/messages` | 404 `no channel available` |
| `deepseek-v4-pro`, `deepseek-chat` | Same |
| `glm-5`, `claude-haiku-4-5-20251001` | 200 PONG |
| `GET /v1/models` filtered for `deepseek` | Empty list (ids can disappear while gateway is up) |
| Hermes `custom:Api.openmodel.ai` + `glm-5` | PONG OK (proves Hermes + key + `api_mode`) |

**Control test:** swap `model` to `glm-5` on the same custom provider before telling the user to remove `api_mode` or re-enter the key.

Catalog and channel availability can change within hours — always live-probe, do not trust an earlier session's `/v1/models` snapshot.