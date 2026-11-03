# google-gemini-cli — June 2026 Live Status

Snapshot from live PONG testing on 2026-06-20 with credential `#1 ranapau` (oauth, google_pkce).

## Working models (5 verified via `hermes chat -Q -q "Reply with exactly: PONG" --max-turns 0`)

| Model ID | Quota behavior | Notes |
|---|---|---|
| `gemini-3.1-pro-preview` | generous | fastest response |
| `gemini-3-pro-preview` | **tight per-minute** (8-13s reset) | run sequentially, never parallel |
| `gemini-3-flash-preview` | generous | |
| `gemini-2.5-pro` | generous | **NOT in cache — discovered live** |
| `gemini-2.5-flash` | generous | **NOT in cache — discovered live** |

## Retired / 404 (do not retry)

- `gemini-3.5-flash` — Google's Cloud Code Assist backend returns:
  > `404: Requested entity was not found … is not available at cloudcode-pa.googleapis.com. It may have been renamed or retired.`

## Cache state (post 2026-06-20 patch)

`~/.hermes/provider_models_cache.json` for `google-gemini-cli` was **manually patched on 2026-06-20** to:

```json
["gemini-3.1-pro-preview", "gemini-3-pro-preview",
 "gemini-3-flash-preview", "gemini-2.5-pro", "gemini-2.5-flash"]
```

- Dropped: `gemini-3.5-flash` (404 for free-tier OAuth; see below)
- Added: `gemini-2.5-pro`, `gemini-2.5-flash` (discovered live, not in upstream cache)

**Caveat — `hermes model --refresh` will overwrite this.** The picker is interactive-only; if it ever runs in a TTY, Hermes re-fetches from Cloud Code Assist and the upstream list (4 entries, including the broken `gemini-3.5-flash`) replaces the patch. Re-apply the 5-entry list after any interactive picker run, or move the patch into a profile-local cache under `~/.hermes/profiles/<name>/provider_models_cache.json`.

## Two-tier model list architecture (lesson from this session)

Hermes has two layers of model lists, and you can fix one without touching the other. The session almost edited the wrong one — here is the rule:

| Layer | File | Who it serves | When to edit |
|---|---|---|---|
| Per-user cache | `~/.hermes/provider_models_cache.json` | The local user / account | **Tier-specific fixes** — drop models that 404 on your OAuth tier; add models the upstream cache hasn't seen yet |
| Shared fallback | `/usr/local/lib/hermes-agent/hermes_cli/models.py` | Every user + tier on the host | **Cross-tier changes** — adding a new provider-wide model; documenting intentional quirks in the inline comments |

**Why `gemini-3.5-flash` is in the shared fallback even though it 404s for free-tier OAuth.** The comment block above the `google-gemini-cli` entry in `models.py` says:

> Code Assist serves two flash slugs with different access gates (gemini-cli models.ts): `gemini-3-flash-preview` is the preview flash that subscription/free-tier OAuth users actually reach, while `gemini-3.5-flash` is GA-channel-gated. Offer both so non-GA users aren't stuck with a slug cloudcode-pa 404s for them.

Translation: the shared list intentionally keeps the GA-gated slug so paid users can still pick it. Free-tier users see it in the picker and hit 404. The correct fix is the **per-user cache** (filter the tier-broken slug), not the shared file (which would break paid users).

**Two install locations of `models.py` can coexist — only one is active.** On this host:
- Active: `/usr/local/lib/hermes-agent/hermes_cli/models.py` (loaded by `/usr/local/lib/hermes-agent/venv/bin/python3`, the shim target of `which hermes`)
- Shadowed: `/root/.local/share/uv/tools/hermes-agent/lib/python3.12/site-packages/hermes_cli/models.py` (uv-managed, **not** loaded)

Verify the active one with:
```bash
head -1 "$(which hermes)"                       # → /usr/local/lib/hermes-agent/venv/bin/python3
"$(head -1 "$(which hermes)")" -c \
  "import hermes_cli.models; print(hermes_cli.models.__file__)"
```
Editing the shadowed one is a silent no-op. If `diff` shows the two diverging, trust the import-printed path.

**Manual cache patch recipe** (what was done on 2026-06-20):
```python
import json, time
path = '/root/.hermes/provider_models_cache.json'
with open(path) as f: d = json.load(f)
d['google-gemini-cli']['models'] = [
    "gemini-3.1-pro-preview", "gemini-3-pro-preview",
    "gemini-3-flash-preview", "gemini-2.5-pro", "gemini-2.5-flash",
]
d['google-gemini-cli']['at'] = time.time()  # bump so Hermes sees it as fresh
# leave 'fp' alone — it's an upstream response fingerprint
json.dump(d, open(path, 'w'))
```

## Caveat about the bundled `hermes-agent` skill

The protected bundled skill `hermes-agent` (shipped with Hermes) ships a reference file `references/google-gemini-oauth-provider.md` that contains a stale note:

> **Current Issue (June 2026):** `google-gemini-cli` returns HTTP 404 from Cloud Code Assist. **Workaround:** Use official `gemini` provider with API key.

**This is partially wrong as of June 2026.** Live testing shows the provider is healthy — only **one** model (`gemini-3.5-flash`) returns 404, the other 5 return responses. The "use the official `gemini` provider" workaround is unnecessary.

That skill is **protected** (bundled `hermes-agent` per Hermes' protected-skill list), so the bundle cannot be patched from an agent session. If the user asks to update it, they need to edit the bundle upstream or use a profile-local copy in `~/.hermes/profiles/<name>/skills/`.

## Reproduction

```bash
for m in gemini-3.1-pro-preview gemini-3-pro-preview gemini-3-flash-preview \
         gemini-3.5-flash gemini-2.5-pro gemini-2.5-flash; do
  echo "=== $m ==="
  timeout 90 hermes chat -Q \
    -q "Reply with exactly: PONG. Nothing else." \
    --provider google-gemini-cli -m "$m" --max-turns 0 2>&1 | tail -5
  sleep 2
done
```
