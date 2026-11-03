---
name: ai-model-smoke-test
description: Live-test whether an AI model/provider is alive, working, and returning responses. Use when the user asks to test/verify all models in a credential pool, when a model picker returns a suspicious or stale list, after adding an OAuth credential, after a provider outage or model retirement, or when building model fallback chains and needing to confirm each link works.
---

# AI Model Smoke Test

Live-check if a model returns a response, in seconds, without firing a full agent loop. Works for any Hermes provider (openrouter, google-gemini-cli, anthropic, ollama, groq, …).

## When to use

- User asks "test all 5 models" / "does model X work" / "is the credential good"
- Model picker returns a stale or suspicious list
- OAuth credential was just added — verify it actually authenticates
- After provider outage or model retirement
- Building a fallback chain — confirm each link works before relying on it
- Diagnosing "is X down or is it me?"

## The PONG test (works for any provider)

```bash
timeout 90 hermes chat -Q \
  -q "Reply with exactly: PONG. Nothing else." \
  --provider <PROVIDER> \
  -m "<MODEL_ID>" \
  --max-turns 0 2>&1 | tail -10
```

**Why this works:**
- `-Q` quiet: strips banner, spinner, tool previews
- `--max-turns 0`: forces a final answer on the first turn — no agent loop
- "Reply with exactly: PONG" gives a deterministic match — grep for the success string
- `timeout 90`: caps a hung provider so you don't wait forever
- `tail -10`: surfaces the relevant line, cuts the Bitwarden "applied N secrets" preamble and "Unknown toolsets" warnings

**Verdict table:**

| Output contains | Verdict | Action |
|---|---|---|
| `PONG` (literal) | OK Works | report and move on |
| `quota exhausted` + `reset after Ns` | Rate-limited | wait `N+5`s, retry once |
| `404: Requested entity was not found … It may have been renamed or retired` | Retired by provider | drop from cache, don't retry |
| `unknown model` / `model not found` | Wrong model ID | check spelling / cache |
| `not logged in` / `auth` / `401` / `403` | Credential issue | re-run `hermes auth add <provider> --label <label>` |
| `429` / `rate limit` | Rate-limited | back off, retry later |
| `route not found` + `NOT_FOUND` on **custom:** provider | Wrong wire protocol | See **Hermes custom_providers + multi-protocol gateways** below; often `api_mode: anthropic_messages` |
| `no channel available for model … with messages api` | Gateway upstream routing | Key + Hermes protocol OK; provider has no live route for that model. Probe another model on same key (e.g. `glm-5`); check catalog for model id |
| `Model or endpoint not found` + `upstream_error` on **manifest** | Manifest routed; upstream dead | Routing works — read `X-Manifest-Model` / `X-Manifest-Provider` headers; fix tier or custom provider in Manifest dashboard |
| `[🦚 Manifest M101]` / no providers | Manifest agent not wired | Connect a provider on Manifest **Routing** page (not Hermes) |
| empty / only `maximum iterations` line | Alive but verbose | increase `--max-turns`, retry |

## Listing models without a TTY

`hermes model` and `hermes model --refresh` both require an interactive terminal and fail with:
> Error: 'hermes model' requires an interactive terminal.

Workarounds:
- Read the cache directly:
  ```bash
  python3 -c "import json; print('\n'.join(json.load(open('/root/.hermes/provider_models_cache.json'))['<provider>']['models']))"
  ```
- Live-probe candidates with the PONG test — fastest way to find the real list and discover models not yet cached.
- `grep -r "<provider>" /root/.hermes/` to find any profile-specific overrides.

Cache file shape: `{"<provider>": {"fp": "<hash>", "at": <epoch>, "models": [...]}}`.

## Two-tier model list architecture

Hermes stores a provider's available models in **two layers** — fix the right one:

1. **Per-user cache** — `~/.hermes/provider_models_cache.json` (or per-profile copy under `~/.hermes/profiles/<name>/`). The model picker reads this first. This is the right place to filter for tier-specific failures (e.g. drop a model that 404s on your free-tier OAuth).
2. **Shared fallback** — `<hermes-cli-install>/hermes_cli/models.py` inside the **active** venv. The picker falls back here if the cache is empty/invalid. Keep conservative — entries here apply across all users and all credential tiers.

**Find the active `models.py`** (two install locations often coexist on one machine; the wrong one is silently shadowed):

```bash
# 1. The hermes shim tells you which Python is active
head -1 "$(which hermes)"
# 2. Ask that Python where it loads hermes_cli from
"<python-from-step-1>" -c "import hermes_cli.models; print(hermes_cli.models.__file__)"
```

Common shadowed pair on this host:
- `/usr/local/lib/hermes-agent/hermes_cli/models.py` — system venv, **active** when `hermes` is `/usr/local/lib/hermes-agent/venv/bin/python3`-backed
- `/root/.local/share/uv/tools/hermes-agent/lib/python3.12/site-packages/hermes_cli/models.py` — uv-managed, **not** active, often diverges from the active one

**Read the inline comments before editing `models.py`.** Most provider blocks have a comment block above them explaining intentional cross-tier quirks (e.g. "Code Assist serves two flash slugs with different access gates … Offer both so non-GA users aren't stuck with a slug cloudcode-pa 404s for them."). If a model 404s for you but is in `models.py` with such a comment, the answer is to filter it in **your** cache, not delete it from the shared file.

## Quota patterns

- **Per-minute rolling (e.g. `gemini-3-pro-preview`):** error says "quota will reset after Ns" where N is small (8–13s). Wait `N+5`s, retry. **Parallel testing burns the budget for sibling models** — run sequentially or in small batches (2-3 at a time with `sleep 2` between).
- **Per-day:** "quota will reset at HH:MM" or "daily limit reached" — don't bother retrying same day.
- **Per-account OAuth:** `auth status` says "logged in" but the model returns 401/403. Token may have expired. Re-run `hermes auth add <provider> --label <existing-label>` to refresh.

## Third-party multi-protocol gateway verification

When the user hands you a third-party gateway URL (OpenRouter, OpenModel, Portkey, LiteLLM, Helicone, OpenPipe, etc.) — not a Hermes internal provider — the smoke test is different. You don't have `hermes chat -Q` or a cached model list; you have a hostname and an API key, and you have to discover the protocol by probing.

### 1. Always DNS-check the host BEFORE trusting the user's URL

User-supplied URLs frequently have TLD typos that make the whole call fail silently with `Could not resolve host`:

```bash
getent hosts <api-host> || echo "DNS FAILED — host does not resolve"
```

If DNS fails, try the obvious alternates before declaring the gateway dead:

| User typed | Try | Why |
|---|---|---|
| `api.foo.app` | `api.foo.ai`, `api.foo.com`, `api.foo.io` | Docs on `.ai` but API on `.app` is a real pattern (see OpenModel case) |
| `foo.com` | `www.foo.com`, `console.foo.com`, `app.foo.com` | API sometimes lives on a subdomain the user didn't mention |
| any of the above | the docs host (`docs.foo.tld`) | Often links to the correct API base URL |

If the docs site loads, grep its HTML for the real `base_url` — providers routinely show it in their quickstart code block.

### 2. Probe `/v1/models` to discover the protocol, not just to list models

A multi-model gateway catalogs each model with a `supported_protocols` field. The presence of `["messages"]` or `["responses"]` or `["chat_completions"]` tells you which endpoint to call — `/v1/messages`, `/v1/responses`, or `/v1/chat/completions` respectively.

```bash
curl -s -H "Authorization: Bearer $KEY" https://<api-host>/v1/models \
  | python3 -c "import json,sys; d=json.load(sys.stdin); 
[print(m['id'], m.get('supported_protocols',[])) for m in d['data'][:30]]"
```

Then match the protocol:

| Protocol string | Endpoint path | SDK |
|---|---|---|
| `["chat_completions"]` | `/v1/chat/completions` | openai.OpenAI |
| `["responses"]` | `/v1/responses` | openai.OpenAI (>=1.50) |
| `["messages"]` | `/v1/messages` | anthropic.Anthropic |
| `["gemini"]` | `/v1/models/<model>:generateContent` | google.genai |

**A 404 on `/v1/chat/completions` for a model that declares `["messages"]` is correct behavior — not a broken key.** Always check the protocol before declaring failure.

### 3. Test the actual inference endpoint, not just the catalog

`/v1/models` is commonly unauthenticated on multi-provider gateways (the catalog is public marketing). A 200 there proves DNS + TLS + that the gateway is up — it does NOT prove the key is valid for chat. Always make at least one real chat call before reporting success.

### 4. Quoting trap when sending bearer tokens inline

When you need to pass a secret via `curl -H "Authorization: Bearer …"` in a terminal command, **do not hand-type the token inline** — bash quoting will fight you the moment the token contains characters that look special (or the wrapper does redaction substitution that breaks parsing). Instead:

```bash
KEY=$(tr -d '\n' < /tmp/key.txt)   # load from file
curl -s -H "Authorization: Bearer $KEY" https://<api-host>/v1/...
```

This pattern avoids both:
- **Bash quoting bugs** when the token has chars that interact with `$`, backticks, or unbalanced quotes.
- **Runtime redaction substitution** that some toolchains perform on inline placeholders (e.g. `***` in inline commands may be substituted with the actual key value before bash sees it — but not in script files written via `write_file`, leading to inconsistent test results across calls in the same session).

Same applies to Python: read the key from `os.environ["KEY"]` after setting it externally with `KEY="..." python3 script.py`. Do not build the bearer string via concatenation like `"Bearer " + key` in a file that contains literal placeholder text (`"Bearer *** " + key` is a real failure mode — produces `Bearer *** <key>` which is malformed auth).

### 5. Multi-model gateway smoke-test recipe

```bash
HOST="<api-host>"                                  # verify via DNS first
KEY=$(tr -d '\n' < /tmp/key.txt)

# (a) Catalog (may or may not require auth)
curl -s -H "Authorization: Bearer $KEY" "https://$HOST/v1/models" | python3 -m json.tool | head -50

# (b) Pick one OpenAI-protocol and one Anthropic-protocol model, call both
for MODEL in <openai-model> <anthropic-model>; do
  case "$MODEL" in
    *gpt*|*qwen*) PATH_="/v1/chat/completions" ;;
    *claude*|*deepseek*) PATH_="/v1/messages" ;;
  esac
  echo "=== $MODEL via $PATH_ ==="
  curl -s -X POST -H "Authorization: Bearer $KEY" -H "Content-Type: application/json" \
    -d "{\"model\":\"$MODEL\",\"max_tokens\":50,\"messages\":[{\"role\":\"user\",\"content\":\"Reply with just: PONG\"}]}" \
    "https://$HOST$PATH_" | python3 -m json.tool | head -20
done
```

Report two columns that can diverge:
- **DNS + TLS reachable?** (got any HTTP response at all)
- **Auth valid?** (got 200 from a real chat call, not just from `/v1/models`)

## Hermes dual storage: `providers:` dict vs `custom_providers:` list

Hermes can store user OpenAI-compatible endpoints in **two on-disk places**. Runtime and the model **picker** merge them via `get_compatible_custom_providers()`; **removal UI does not**.

| Location | Schema | Typical entries |
|---|---|---|
| Top-level `providers:` | Dict keyed by slug (`api.groq.com`, `tokenrouter`, `manifest`, …) | v12+ canonical shape after migration from legacy list |
| `custom_providers:` | YAML list of `{name, base_url, api_key\|key_env, model, …}` | Legacy; still valid on hybrid configs (`_config_version` 30+) |

**Picker / `custom:<name>`:** Both sources appear. Groq with `key_env: GROQ_API_KEY` in `providers:` is still a user endpoint — not “owned by Manifest” unless the key is literally `manifest:`.

**Remove list gap:** `hermes model` → “Remove custom provider” (`_remove_custom_provider` in `hermes_cli/main.py`) only pops entries from the **`custom_providers:` list**. It does **not** delete keys from `providers:`. If the user added Groq/TokenRouter via dashboard or migration into `providers:`, they will show in the picker but **not** in the remove menu.

**To remove `providers:` entries:** Delete the slug block under `providers:` in `config.yaml` (or dashboard config API if exposed). For `key_env` rows, also clear Bitwarden/`.env` if rotating. Keep `manifest:` if still using Manifest routing.

**Hybrid pitfall:** Same URL in both places dedupes in the compat view by `provider_key` / name+URL — but remove only touches the list half. Prefer consolidating new endpoints into **one** section to avoid operator confusion.

See `references/hermes-providers-dict-vs-custom-providers-remove-list-jun-2026.md` for a worked DietPi profile inventory (Groq/TokenRouter in `providers:`, Bynara in `custom_providers:`).

**Consolidate for remove UX:** If the user wants dict entries (Groq, TokenRouter, etc.) in `hermes model` → remove custom provider, migrate slugs into `custom_providers:` and clear `providers:` — recipe in that reference § "Consolidate dict → list".

## Hermes `custom_providers` + multi-protocol gateways (OpenModel, etc.)

When the user says the API key is "set in Hermes" via `custom_providers` (provider slug `custom:<name>`), run **both** tests:

1. **Direct gateway probe** — curl/SDK against the model's real protocol (`/v1/messages`, `/v1/chat/completions`, or `/v1/responses`) using `supported_protocols` from `/v1/models`.
2. **Hermes PONG** — `hermes chat -Q … --provider custom:<name> -m <model> --max-turns 0`.

These can diverge: **API OK + Hermes 404** means the key and model are fine; Hermes is using the wrong protocol.

**Cause:** `resolve_custom_provider` defaults to OpenAI `chat_completions` unless `api_mode` is set. Gateways like OpenModel route `deepseek-v4-flash` (and most Claude/GLM/Kimi slugs) only on Anthropic `/v1/messages`.

**Fix:** In `~/.hermes/config.yaml`, on the matching `custom_providers` entry (or keyed `providers:` entry), add:

```yaml
api_mode: anthropic_messages
```

Use `codex_responses` or `chat_completions` only when `/v1/models` shows that protocol for the model. Valid values: `chat_completions`, `anthropic_messages`, `codex_responses`, `bedrock_converse`.

**Config edit:** The agent often cannot `patch` `config.yaml` (guarded). Tell the user to add `api_mode` via `hermes config edit` or hand-edit; then re-run PONG.

**Diagnosis tip:** Verbose Hermes logs showing `OpenAI client created … base_url=https://…/v1` plus `route not found` → almost certainly missing `api_mode: anthropic_messages` for a `[\"messages\"]` model.

**Reporting:** Split columns — **Gateway inference** vs **Hermes custom provider** — so "key broken" is not confused with "protocol mismatch".

See `references/openmodel-gateway-jun-2026.md` for OpenModel TLD, curl recipe, Hermes wiring, and **channel outages**.

## Manifest (`providers.manifest`, model `auto`)

Manifest is an LLM router — not a model catalog. Clients send **`model: auto`** (aka `manifest/auto`); Manifest picks tier + upstream model. Docs: `https://manifest.build/docs/llms.txt`.

### `/v1/models` behavior

- **Cloud & self-hosted:** returns **one** id: `auto` (sometimes `manifest/auto`).
- **No dashboard sync:** Hermes `/model` picker shows only what `/v1/models` returns — not the 300+ models configured in **Routing**.
- **Workaround:** pin favorites in Hermes via `discover_models: false` + `models:` list (copy ids from Manifest **Routing** / tier primaries).

### Distroless container inspection

Manifest self-hosted image (`manifestdotbuild/manifest`) is **distroless** — no shell, no `ls`, no `grep`. Source is compiled/transpiled and not present in the container.

**What this means:**
- No in-place patching of `/app/server/api/history.go` — it doesn’t exist as source.
- No runtime inspection — can’t `grep` or `find` inside the container.

**Workarounds:**
- Fork Manifest → edit source → rebuild image → redeploy.
- Proxy `/api/v1/history` → Hermes cron → store 90+ days in SQLite/Postgres.
- Query `public.messages` directly (data is there; just not exposed).

See `references/manifest-distroless-inspection-jun-2026.md`.

### Self-hosted Docker + LAN

Official install is **Docker Compose** only (image `manifestdotbuild/manifest` + Postgres). Default bind is **localhost**; exposing LAN requires:

1. `ports: ["${PORT:-2099}:${PORT:-2099}"]` (not `127.0.0.1:...`).
2. `BETTER_AUTH_URL` in `.env` = exact browser URL (e.g. `http://192.168.0.222:2099`).
3. Generate `BETTER_AUTH_SECRET` (`openssl rand -hex 32`); prefer separate `MANIFEST_ENCRYPTION_KEY` for stored provider credentials.

**Smoke after install:**

```bash
curl -sS http://<host>:2099/api/v1/health
curl -sS http://<host>:2099/setup
```

Hermes uses a **new** `mnfst_` key from the local dashboard — not the cloud agent key. Point `providers.<name>.api` at `http://<host>:2099/v1`, `default_model: auto`.

See `references/manifest-self-hosted-docker-lan-jun-2026.md` for full recipe (install dir, volume name, Ollama `host.docker.internal`, backup one-liner).

**Hermes config** (keyed `providers:` section is fine):

```yaml
providers:
  manifest:
    api: https://app.manifest.build/v1
    api_key: mnfst_...
    default_model: auto
    name: Manifest
```

**Smoke test:**

```bash
# Catalog: expect ONLY id "auto"
curl -s https://app.manifest.build/v1/models -H "Authorization: Bearer $MNFST_KEY"

timeout 90 hermes chat -Q -q "Reply with exactly: PONG." \
  --provider manifest -m auto --max-turns 0 2>&1 | tail -10
```

`--provider manifest` and `custom:manifest` both resolve if `auth.json` / config define the entry.

**Verdict split:**

| Signal | Meaning |
|---|---|
| `GET /v1/models` → only `auto` | Normal |
| PONG + `X-Manifest-*` headers on success | Routing + upstream OK |
| HTTP 404, body `upstream_error`, **no** M101 | **Manifest routing works**; fix the upstream named in `X-Manifest-Model` / `X-Manifest-Provider` (often a custom OpenModel/DeepSeek slug) |
| M101 in body | Zero providers on that Manifest agent — dashboard **Routing** |
| M100 | Provider connected but missing API key on Routing |

On failed chat, capture response headers (Python `urllib` on `HTTPError`):

```python
# X-Manifest-Model, X-Manifest-Provider, X-Manifest-Tier, X-Manifest-Confidence
```

**Control test:** If `auto` fails but you suspect Hermes, POST the same body to `/v1/chat/completions` with `model: auto` — identical error means router OK, upstream not.

See `references/manifest-auto-routing-jun-2026.md` for a worked upstream-404 case (auto → custom provider → `deepseek-v4-flash`).

### Hermes `/model` picker shows only `auto`

Expected: Hermes lists models from `GET {api}/v1/models`; Manifest returns **one** id (`auto`). Not OpenRouter-style catalog parity.

**Pin favorites in Hermes** (copy ids from Manifest **Routing** / tier primaries):

```yaml
providers:
  manifest:
    api: http://192.168.0.222:2099/v1
    api_key: mnfst_...
    default_model: auto
    discover_models: false
    models:
      - auto
      - glm-5
      - openrouter/anthropic/claude-haiku-4.5
    name: Manifest
```

- `discover_models: false` — keep the explicit `models:` list; default `true` replaces it with live `/v1/models` (only `auto`).
- `models` as list or dict both work (`hermes_cli/config.py` normalizes list → dict).
- Wrong ids still appear in picker but fail at chat time — smoke-test with PONG per id.

Alternatives: separate `providers:` rows per pinned model (same `api`+key, different `default_model`); or use OpenRouter/OpenModel directly when you need a full live catalog.

See `references/manifest-hermes-model-picker-jun-2026.md`.

### Custom provider "Fetch models" probe (OpenAI vs Anthropic paths)

Dashboard **Fetch models** does **not** always call `{base}/v1/models`. For `apiKind: openai` it calls `{base}/models` (trailing slashes stripped first). Users who paste the full catalog URL as base (e.g. `…/v1/models`) get a **404** on `…/v1/models/models` and the misleading LM Studio/Ollama boilerplate — even when `GET …/v1/models` works from curl.

**Fix:** Set base to the OpenAI client `base_url` only (`https://api.featherless.ai/v1` for Featherless). Split diagnosis: **direct curl catalog** vs **Manifest probe URL** in the report.

See `references/featherless-manifest-fetch-models-jul-2026.md` (Featherless + GLM-5.2 worked example).

### Self-hosted Docker + LAN

Official install is **Docker Compose** only (image `manifestdotbuild/manifest` + Postgres). Default bind is **localhost**; exposing LAN requires:

1. `ports: ["${PORT:-2099}:${PORT:-2099}"]` (not `127.0.0.1:…`).
2. `BETTER_AUTH_URL` in `.env` = exact browser URL (e.g. `http://192.168.0.222:2099`).
3. Generate `BETTER_AUTH_SECRET` (`openssl rand -hex 32`); prefer separate `MANIFEST_ENCRYPTION_KEY` for stored provider credentials.

**Smoke after install:**

```bash
curl -sS http://<host>:2099/api/v1/health
curl -sS http://<host>:2099/setup
```

Hermes uses a **new** `mnfst_` key from the local dashboard — not the cloud agent key. Point `providers.<name>.api` at `http://<host>:2099/v1`, `default_model: auto`.

See `references/manifest-self-hosted-docker-lan-jun-2026.md` for full recipe (install dir, volume name, Ollama `host.docker.internal`, backup one-liner).

## Cloudflare Workers AI (account-scoped)

Base URL (OpenAI-compat):

`https://api.cloudflare.com/client/v4/accounts/<ACCOUNT_ID>/ai/v1`

Direct run (non-OpenAI shape):

`POST .../accounts/<ACCOUNT_ID>/ai/run/@cf/<org>/<model>`

**Smoke (Jun 2026, `@cf/zai-org/glm-5.2`):**

| Endpoint | HTTP | Notes |
|---|---|---|
| `/ai/run/@cf/zai-org/glm-5.2` | 200 | `messages` array; content in `result.choices[].message.content` |
| `/ai/v1/chat/completions` | 200 | Use `model: @cf/zai-org/glm-5.2`; **reasoning model** — low `max_tokens` can yield empty `content` and text in `reasoning_content` |

**Auth:** Cloudflare API token (`cfut_...`) as `Authorization: Bearer`. Load token from a **file** in Python (`Path.read_text`) — inline shell tokens often get redacted to `***` → false 401.

**Hermes custom provider shape:**

```yaml
- name: Cloudflare GLM 5.2
  base_url: https://api.cloudflare.com/client/v4/accounts/<ACCOUNT_ID>/ai/v1
  api_key: <cfut token or key_env>
  model: '@cf/zai-org/glm-5.2'
```

See `references/cloudflare-workers-ai-glm-smoke-jun-2026.md`.

## Featherless.ai (serverless open models)

OpenAI-compatible hosted inference — `https://api.featherless.ai/v1`, Bearer `rc_…` keys. Catalog at `GET /v1/models`; chat at `POST /v1/chat/completions`. Smoke with curl (`-A curl/8.0`) not bare `urllib` (Cloudflare 403). Example model: `zai-org/GLM-5.2` (may echo short replies in `reasoning`).

When **Manifest Fetch models** fails with 404/LM Studio text but curl to `/v1/models` is 200, the base URL almost certainly includes `/models` — see Manifest subsection above and `references/featherless-manifest-fetch-models-jul-2026.md`.

## ZenMux free models

Free slugs (e.g. `z-ai/glm-4.7-flash-free`) share subscription **~10–15 RPM** and rolling 5h window; not for parallel smoke batches. See `references/zenmux-free-tier-rate-limits.md`.

## Reporting results

Use a markdown table, one row per model. Always include two columns that can diverge:
- **In cache?** — was it in `provider_models_cache.json`?
- **Works?** — did the PONG test pass?

If the cache is stale, suggest `hermes model` interactively to refresh, and report any models discovered live that aren't in cache.

## Post-test cleanup

PONG tests create ephemeral CLI sessions (one per `hermes chat -Q` invocation). These are junk — no useful context, just "PONG" + tool-limit messages. Clean up after batch testing.

**Find low-message sessions** (SQLite query against state.db):

```bash
python3 -c "
import sqlite3
conn = sqlite3.connect('/root/.hermes/state.db')
cur = conn.cursor()
cur.execute('''SELECT s.id, s.message_count, s.source
    FROM sessions s WHERE s.message_count < 3 ORDER BY s.started_at DESC''')
for r in cur.fetchall():
    print(f'{r[0]}  msgs={r[1]}  src={r[2]}')
"
```

**Verify content before deleting** (make sure they're really junk):

```bash
python3 -c "
import sqlite3
conn = sqlite3.connect('/root/.hermes/state.db')
cur = conn.cursor()
cur.execute('''SELECT role, substr(content,1,100) FROM messages
    WHERE session_id=? ORDER BY timestamp''', ('<session_id>',))
for r in cur.fetchall(): print(f'[{r[0]}] {(r[1] or \"\").replace(chr(10),\" \")}')
"
```

**Delete:**

```bash
hermes sessions delete <session_id> -y
```

**Key facts:**
- `~/.hermes/state.db` is the active session store (has `sessions` + `messages` tables)
- `~/.hermes/sessions.db` exists but is empty/unused on this host
- `hermes sessions list` works interactively; the Python query above works from cron/automation
- Empty Discord sessions (0 msgs) are also safe to delete — they're connection blips

## Pitfalls

- **Don't run 5+ PONG tests in parallel on a rate-limited provider.** You'll burn each model's quota and all 5 will return "quota exhausted". Run sequentially, or batch 2-3 with `sleep 2` between.
- **`--max-turns 0` is required.** Without it the agent enters its tool loop and you get a wall of logs; with it you get a one-shot answer.
- **Output is wrapped in noise.** The Bitwarden "applied N secrets" line and "Warning: Unknown toolsets" warnings sit above the actual response. `tail -10` cuts through.
- **Stale cache ≠ dead model.** A model missing from the cache can still work — the cache is just the last-seen list. Always probe candidates not in cache if you suspect the provider has added models.
- **Stale cache ≠ working model.** A model in cache can be retired (404). Always verify, never trust the picker.
- **`hermes model --refresh` overwrites manual cache patches.** It is also interactive-only — it fails with `Error: 'hermes model' requires an interactive terminal` if you try to run it from a non-TTY session. If you hand-edit the cache to filter tier-specific failures, the next interactive `hermes model` run can re-fetch from the provider and replace your filter. Re-apply after refresh, or duplicate the filter into a profile-local copy under `~/.hermes/profiles/<name>/provider_models_cache.json`.
- **Don't patch the shared `models.py` for tier-specific fixes.** The shared fallback is meant to work for every credential tier on the host. A model that 404s on your free-tier OAuth may work for paid/subscription OAuth. Always filter in the per-user cache; leave `models.py` alone unless the change is genuinely cross-tier.
- **Cache shape is `{"<provider>": {"fp": "<hash>", "at": <epoch>, "models": [...]}}`.** Hand-edits: replace `models` array, bump `at` to current epoch, leave `fp` alone (it's an upstream response fingerprint — Hermes will recompute on the next real refresh).
- **OpenModel / messages-only models via Hermes custom provider:** A passing curl to `https://api.openmodel.ai/v1/messages` does not imply Hermes works. Without `api_mode: anthropic_messages`, Hermes hits `/v1/chat/completions` and returns `route not found` even with a valid `om-` key.
- **After `api_mode` is set, OpenModel can still 404 DeepSeek:** Error `no channel available for model <id> with messages api` is upstream capacity/routing — not Hermes. Same key may work for `glm-5` or Claude; `/v1/models` may omit DeepSeek ids temporarily. Do not revert `api_mode`.
- **Manifest `auto` is not broken when only one model appears in `/v1/models`:** That single id is the routing opt-in. Failure with `upstream_error` means fix Manifest tier/fallback or the custom provider behind the routed slug.
- **Manifest Routing UI "Fetch models" 401:** Custom OpenAI-compatible providers may show red HTTP 401 on probe while chat works — probe often omits the stored API key. Add models manually; test with dashboard **Chat** or `POST /v1/chat/completions`.
- **Manifest "Fetch models" 404 + LM Studio/Ollama hint:** Generic `probe-error.ts` message — **not** proof the upstream lacks `/v1/models`. For OpenAI-compatible hosts, Manifest probes `{baseUrl}/models`, so base must end at `/v1` (e.g. Featherless: `https://api.featherless.ai/v1`). If base includes `/v1/models`, probe hits `…/models/models` → 404 while direct `GET …/v1/models` is 200. See `references/featherless-manifest-fetch-models-jul-2026.md`.
- **Featherless / Cloudflare:** Default Python `urllib` may get **403** (`error code: 1010`) on `api.featherless.ai`; use `curl -A curl/8.0` for catalog and chat smoke tests. GLM-5.2 may return PONG in `message.reasoning` with empty `content`.
- **Groq/TokenRouter in picker but missing from remove list:** Endpoints in top-level `providers:` are not in the CLI remove menu until moved to `custom_providers:` — or delete slug in YAML. See dual-storage + reference § consolidate.
- **Cloudflare public health checks:** Default Python `urllib` User-Agent may get **403** on tunnel hostnames while `curl` gets 200. Set `User-Agent: curl/8.0` (or similar) in verification scripts; see `scripts/hermes-verify-public-health.py` pattern.

## See also

- `references/google-gemini-cli-jun-2026.md` — current live status of the `google-gemini-cli` provider (5 working models + 1 retired).
- `references/openmodel-gateway-jun-2026.md` — third-party multi-protocol gateway case study (TLD typo, protocol routing, Hermes `api_mode`, DeepSeek channel outages).
- `references/manifest-auto-routing-jun-2026.md` — Manifest `auto` + Hermes PONG, `X-Manifest-*` headers, upstream vs M101.
- `references/manifest-hermes-model-picker-jun-2026.md` — why only `auto` appears; `discover_models: false` + `models:` pin list.
- `references/manifest-self-hosted-docker-lan-jun-2026.md` — Docker Compose on LAN, `BETTER_AUTH_URL`, Hermes `manifest-local` provider, health/setup curls.
- `references/hermes-providers-dict-vs-custom-providers-remove-list-jun-2026.md` — `providers:` dict vs `custom_providers:` list; why remove menu skips Groq/TokenRouter; consolidate dict→list recipe.
- `references/cloudflare-workers-ai-glm-smoke-jun-2026.md` — CF Workers AI `/ai/v1` + `/ai/run`, `@cf/zai-org/glm-5.2`, token-from-file pitfall.
- `references/featherless-manifest-fetch-models-jul-2026.md` — Featherless curl smoke, GLM-5.2 `reasoning` field, Manifest Fetch models URL doubling (`/models/models` false 404).
- `references/zenmux-free-tier-rate-limits.md` — ZenMux free models ~10–15 RPM.
- `scripts/smoke_test_provider.sh` — runnable loop that walks the cache and reports a table.
- `scripts/verify_third_party_gateway.sh` — one-shot verifier for a third-party multi-protocol gateway: DNS-checks the host (tries alt TLDs if needed), parses `/v1/models` for protocol hints, and fires real inference probes against both an OpenAI-protocol and an Anthropic-protocol model.
- `scripts/hermes-verify-public-health.py` — ad-hoc LAN + `mf.xuup.top` health with curl-like User-Agent (avoids false 403 from default Python UA on CF).
