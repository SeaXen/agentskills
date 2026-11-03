# Featherless.ai smoke test + Manifest "Fetch models" false 404

Session: Jul 2026 — user verified `zai-org/GLM-5.2` on Featherless; Manifest UI showed a misleading `/v1/models` 404 with LM Studio/Ollama boilerplate.

## Featherless (OpenAI-compatible)

| Field | Value |
|-------|--------|
| Base URL | `https://api.featherless.ai/v1` |
| Auth | `Authorization: Bearer <key>` (`rc_…` from dashboard) |
| Catalog | `GET https://api.featherless.ai/v1/models` → HTTP **200** (large `{ data: [{ id, … }] }`) |
| Chat | `POST https://api.featherless.ai/v1/chat/completions` |
| Docs | https://featherless.ai/docs (quickstart uses same base_url) |

**Direct PONG (curl):**

```bash
KEY=$(tr -d '\n' < /path/to/key.txt)
curl -sS --max-time 180 -A 'curl/8.0' \
  -H "Authorization: Bearer $KEY" -H "Content-Type: application/json" \
  -d '{"model":"zai-org/GLM-5.2","messages":[{"role":"user","content":"Reply with exactly: PONG"}],"max_tokens":32}' \
  https://api.featherless.ai/v1/chat/completions
```

**Observed HTTP matrix (Jul 2026):**

| URL | HTTP | Notes |
|-----|------|--------|
| `/v1/models` | 200 | Works with or without Bearer on this host |
| `/v1/chat/completions` + valid key | 200 | Inference OK |
| `/v1/models/models` | **404** | Double `/models` — wrong base URL |
| `/models` (no `/v1`) | **401** | Wrong base — different error than 404 |
| Python `urllib` default UA | **403** `error code: 1010` | Cloudflare — use `curl -A curl/8.0` or set UA in scripts |

**GLM-5.2 response shape:** Short PONG test may return text in `choices[0].message.reasoning` with empty `content` — treat as success if either field contains PONG.

**Hermes custom provider:**

```yaml
base_url: https://api.featherless.ai/v1
api_key: <rc_ key or key_env>
model: zai-org/GLM-5.2
# api_mode: chat_completions (default — correct for Featherless)
```

## Manifest custom provider "Fetch models" probe

The red error:

> `{url} returned 404. The server is up but /v1/models isn't exposed — check that the OpenAI-compatible endpoints are enabled (recent LM Studio / Ollama builds expose them by default).`

Comes from Manifest `classifyProbeError` when **any** models probe gets HTTP 404 (`probe-error.ts`). The LM Studio/Ollama text is **generic** — not evidence that Featherless lacks OpenAI endpoints.

**How Manifest builds the probe URL** (`custom-provider.service.ts`):

```text
OpenAI apiKind:  GET {baseUrl trimmed of trailing /}/models
Anthropic apiKind: GET {baseUrl}/v1/models
```

So for Featherless (OpenAI-compatible), **base URL must be** `https://api.featherless.ai/v1` — **not** `https://api.featherless.ai/v1/models`.

| Base URL entered | Manifest actually requests | Typical HTTP |
|------------------|----------------------------|--------------|
| `https://api.featherless.ai/v1` | `…/v1/models` | 200 |
| `https://api.featherless.ai/v1/models` | `…/v1/models/models` | **404** → misleading message |
| `https://api.featherless.ai` | `…/models` | **401** (unauthorized hint) |

**Diagnosis when user reports Featherless 404 on Fetch models:**

1. Confirm direct curl: `curl -A curl/8.0 -o /dev/null -w '%{http_code}\n' https://api.featherless.ai/v1/models` → expect 200.
2. If direct OK but Manifest fails → fix **base URL** (strip `/models` suffix) and set API kind **OpenAI**.
3. Chat can work even when Fetch models fails — user can type `zai-org/GLM-5.2` manually.

**Security:** User pasted full API key in chat — recommend rotation at https://featherless.ai/account/api-keys if channel is not private.