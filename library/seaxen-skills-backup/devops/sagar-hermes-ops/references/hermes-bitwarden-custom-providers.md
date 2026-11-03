# Hermes Bitwarden + Custom Providers

Use this when Dr. Sagar wants Hermes secrets cleaned up, migrated into Bitwarden Secrets Manager, or custom OpenAI-compatible providers moved out of plaintext config.

## Core shape

1. **Normalize the live Hermes home first**
   - Canonical live home on this system: `/root/.hermes`
   - `/mnt/tb/hermes` may only be a symlink alias
   - Before doing any secret work, verify:
     - `hermes config path`
     - `hermes config env-path`
     - service/runtime `HERMES_HOME`
     - samefile semantics if `/root/.hermes` vs `/mnt/tb/hermes` both appear

2. **Bitwarden bootstrap model**
   - Hermes still needs one local bootstrap credential: `BWS_ACCESS_TOKEN`
   - The rest of the provider/API secrets can live in Bitwarden and be injected into `os.environ` at Hermes startup
   - After setup, verify with:
     - `hermes secrets bitwarden status`
     - `hermes secrets bitwarden sync`
     - `hermes dump`

3. **Custom providers should not keep raw `api_key:` when env-backed is possible**
   - For `custom_providers`, prefer:

```yaml
custom_providers:
  - name: Api.groq.com
    base_url: https://api.groq.com/openai/v1
    model: llama-3.3-70b-versatile
    key_env: GROQ_API_KEY
```

   - Same pattern for SambaNova / Together / similar OpenAI-compatible endpoints
   - `key_env` is cleaner than leaving inline `api_key:` or `${ENV_VAR}` templates

4. **Verification split**
   - Verify the env vars exist in Bitwarden / process env
   - Verify `config.yaml` no longer contains plaintext `api_key` values for the migrated providers
   - Verify backups do not silently retain the old keys if the goal is a full cleanup

## Safe disclosure rule

When the user asks to inspect key values, prefer **narrow local extraction**:
- read only the specific provider rows from `config.yaml`
- or print only the exact env vars requested

Avoid telling the user to run broad Bitwarden listing commands in chat because some output modes expose **all project secrets and values**, not just the targeted provider key.

## Cleanup caveat

A migration is not fully clean if any of these still contain the old provider secrets:
- `config.yaml`
- `.env`
- `config.yaml.pre-...bak`
- ad-hoc copied backups or temp files

Treat the backup files as sensitive until removed or rotated.

## End-to-end provider proof

For live proof that a Bitwarden-backed custom provider actually works in this Hermes build, prefer the **runtime resolver path** over a normal `hermes chat` smoke test.

Why:
- `hermes chat` can inject extra payload/tool metadata that causes unrelated provider-side request errors
- that kind of failure does **not** prove the key or Bitwarden wiring is wrong

Use Hermes' own runtime environment:

```bash
PYTHONPATH=/usr/local/lib/hermes-agent \
HERMES_HOME=/root/.hermes \
/usr/local/lib/hermes-agent/venv/bin/python3 - <<'PY'
from hermes_cli import env_loader
from agent.auxiliary_client import resolve_provider_client

env_loader.load_hermes_dotenv()
client, model = resolve_provider_client('Api.groq.com', model='llama-3.3-70b-versatile')
resp = client.chat.completions.create(
    model=model,
    messages=[{'role': 'user', 'content': 'Reply exactly: GROQ_OK'}],
    max_tokens=16,
    temperature=0,
)
print(resp.choices[0].message.content)
PY
```

Interpretation:
- exact echo response like `GROQ_OK` / `SAMBANOVA_OK` = provider works end-to-end through Hermes runtime
- provider HTTP billing/credit errors (for example Together `402 credit_limit exceeded`) = Hermes reached the provider correctly; remaining issue is provider account state
- empty content with `finish_reason=length` on SambaNova-style models can be a too-small `max_tokens` issue, not a missing key; retry with a larger token budget before calling it a failure

## Session-specific learned pattern

Observed durable workflow:
- canonicalize `HERMES_HOME`
- enable Bitwarden
- move provider secrets into Bitwarden
- replace custom provider `api_key:` with `key_env:`
- verify Bitwarden injection and clean config separately
- prove providers through `env_loader.load_hermes_dotenv()` + `resolve_provider_client(...)` + a minimal chat completion
- treat `hermes chat` verification failures carefully if they are caused by payload/tool-shape issues instead of auth
- then audit residual secret copies in backups
