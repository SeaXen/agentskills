# OpenRouter free/cheap picker curation for Hermes

Use this when a user wants Hermes `/model` or dashboard to emphasize free or low-cost OpenRouter models.

## Core behavior to remember

Hermes does **not** blindly show every model named in a custom list.

Final OpenRouter picker output is the intersection of:
1. curated catalog entries
2. OpenRouter live `https://openrouter.ai/api/v1/models`
3. Hermes tool-support filter

That means models can be:
- visible on OpenRouter docs or website pages
- present in a custom manifest
- but still absent from Hermes if they are not present in the live `/api/v1/models` payload at the moment.

This came up with multiple `:free` models that looked available from web pages but were filtered out by the final live intersection step.

## Working override pattern

`config.yaml`:

```yaml
model_catalog:
  enabled: true
  url: https://hermes-agent.nousresearch.com/docs/api/model-catalog.json
  ttl_hours: 24
  providers:
    openrouter:
      url: file:///root/.hermes/cache/free_openrouter_catalog.json
```

Important: inline `model_catalog.providers.openrouter.models:` does not drive the picker. The provider override path is `url`, not embedded model IDs.

## Useful verification probes

### Show the curated provider list being loaded
```bash
/usr/local/lib/hermes-agent/venv/bin/python - <<'PY'
from hermes_cli.model_catalog import get_curated_openrouter_models, reset_cache
reset_cache()
print(get_curated_openrouter_models())
PY
```

### Show the final picker output Hermes will use
```bash
/usr/local/lib/hermes-agent/venv/bin/python - <<'PY'
from hermes_cli.models import fetch_openrouter_models
models = fetch_openrouter_models(force_refresh=True)
print('count=', len(models))
for i, (mid, desc) in enumerate(models, 1):
    print(f'{i:2}. {mid} || {desc}')
PY
```

### Explain why curated models are missing from the final picker
```bash
/usr/local/lib/hermes-agent/venv/bin/python - <<'PY'
import json, urllib.request
from hermes_cli.model_catalog import get_curated_openrouter_models, reset_cache
from hermes_cli.models import _openrouter_model_supports_tools

reset_cache()
curated = get_curated_openrouter_models() or []
curated_ids = [m for m, _ in curated]
with urllib.request.urlopen('https://openrouter.ai/api/v1/models', timeout=15) as r:
    payload = json.loads(r.read().decode())
live = {str(item.get('id') or '').strip(): item for item in payload.get('data', []) if isinstance(item, dict)}
shown = []
missing = []
for mid in curated_ids:
    item = live.get(mid)
    if item is None:
        missing.append((mid, 'not in live OpenRouter /v1/models response'))
    elif not _openrouter_model_supports_tools(item):
        missing.append((mid, 'filtered: no tool support advertised'))
    else:
        shown.append(mid)
print('shown', len(shown))
for m in shown:
    print('SHOW', m)
print('\nmissing', len(missing))
for m, reason in missing:
    print('MISS', m, '||', reason)
PY
```

## Concrete lesson from this session

A custom `free+cheap` manifest produced a final Hermes picker count of 21 models because several desired free models were absent from the live OpenRouter `/api/v1/models` response. Missing examples included:
- `inclusionai/ring-2.6-1t:free`
- `deepseek/deepseek-r1:free`
- `openrouter/elephant-alpha:free`
- `openrouter/polaris-alpha:free`
- `openrouter/sonoma-dusk-alpha:free`
- `openrouter/sonoma-sky-alpha:free`
- `tencent/hy3-preview:free`
- `poolside/laguna-m1:free`

So if the user says “it’s on OpenRouter, why not in Hermes?”, verify against the live models API before concluding anything is broken.

## Dashboard/CLI mismatch lesson

Dashboard and CLI can disagree temporarily even when they point to the same real config file, because they are separate long-running processes with separate in-memory caches.

Check:
- CLI-resolved config path/home
- gateway `HERMES_HOME`
- dashboard `/api/status`
- dashboard process age / restart state

If needed:
- restart dashboard
- hard-refresh browser tab
- then compare with `fetch_openrouter_models(force_refresh=True)`

## User-facing framing that worked well

When a user asks whether free models can become paid or disappear, answer plainly:
- yes, free models can become paid later
- yes, OpenRouter can stop exposing a free model
- yes, a model can still exist on docs/pages but be hidden from Hermes because the live models API no longer exposes it for picker use
