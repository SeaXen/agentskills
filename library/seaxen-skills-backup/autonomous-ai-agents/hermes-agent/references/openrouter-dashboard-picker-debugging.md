# OpenRouter dashboard picker debugging

Use this when Hermes CLI and dashboard disagree about OpenRouter models, or when a model is valid/live but does not show in the web picker.

## Key facts

- Dashboard model picker loads from `GET /api/model/options`
- That endpoint is protected by an ephemeral dashboard session token
- The token is injected into `/` as:
  - `window.__HERMES_SESSION_TOKEN__`
- The authenticated header is:
  - `X-Hermes-Session-Token: <token>`
- OpenRouter live-catalog gotcha: if the picker helper hits `https://openrouter.ai/api/v1/models` **without** `Authorization: Bearer $OPENROUTER_API_KEY`, OpenRouter may return a reduced public subset. Result: the dashboard can show fewer free models (for example missing `qwen/qwen3-coder:free` or `poolside/laguna-m.1:free`) even though they exist in the curated catalog and in the authenticated API response.
- CLI helper output can be compared from Hermes venv using:
  - `from hermes_cli.models import fetch_openrouter_models`
  - `from hermes_cli.inventory import build_models_payload, load_picker_context`

## Quick verification flow

1. Check dashboard health:
   - `/api/status`
   - verify `hermes_home` and `config_path`
2. Extract session token from dashboard HTML `/`
3. Call `/api/model/options` with `X-Hermes-Session-Token`
4. Compare dashboard OpenRouter list vs CLI/helper output
5. If dashboard differs, inspect whether inventory builder is using the picker-aware path

### Response-shape pitfall

The current `/api/model/options` payload returns provider rows like:

- `providers[].slug`
- `providers[].name`
- `providers[].models`

For this endpoint, `providers[].models` is commonly a **list of model-id strings**, not a list of `{id: ...}` objects. When verifying whether a model such as `openrouter/free` is present, test membership directly against the string list before assuming the dashboard omitted it.

## Important code-path distinction

Two similar but not identical provider-list builders exist:

- `list_authenticated_providers()`
  - general inventory path
  - can diverge from actual CLI picker behavior for OpenRouter
- `list_picker_providers()`
  - picker-aware path
  - replaces OpenRouter rows with `fetch_openrouter_models()` output
  - this is the safer source when dashboard and CLI must match

## Durable fix discovered

If dashboard omits models that the CLI picker/backend helpers can see, patch Hermes so the dashboard inventory builder uses:

- `list_picker_providers()`

instead of:

- `list_authenticated_providers()`

This aligns dashboard OpenRouter listing with the CLI picker.

## OpenRouter-specific caveats

Even a custom curated catalog is not the final truth. Hermes still filters by:

1. curated catalog / override manifest
2. OpenRouter live `/api/v1/models`
3. Hermes tool-capability checks

So an OpenRouter web page can still say `free` while Hermes hides the model because the live API no longer serves it.

## Related references

- `references/openrouter-free-and-cheap-picker.md`
- `references/openrouter-free-models-2026.md`
