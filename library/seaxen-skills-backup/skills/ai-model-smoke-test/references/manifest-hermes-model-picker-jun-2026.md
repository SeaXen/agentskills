# Manifest + Hermes model picker — Jun 2026

## Question

User selects **Manifest** in Hermes; picker shows only **`auto`**. Wants preferred models like OpenRouter.

## Answer

By design. Manifest is a **router**; the OpenAI-compat catalog exposes the routing keyword `auto` only. Hermes `provider_model_ids()` calls `GET /v1/models` (see `providers/base.py` `fetch_models`).

## Hermes workaround

In `~/.hermes/config.yaml` under `providers.manifest` (or keyed custom provider):

```yaml
discover_models: false
models:
  - auto
  - <tier-primary-or-provider-slug-from-dashboard>
```

Model strings must be ids Manifest accepts on `POST /v1/chat/completions` when **not** using smart routing (or tier-assigned slugs your instance documents). Copy from Manifest dashboard **Routing** after connecting providers.

## Code paths

- `hermes_cli/config.py` — `_KNOWN_KEYS` includes `models`, `discover_models`
- `hermes_cli/model_switch.py` — merges `models` dict/list into picker groups; `discover_models: false` skips live replacement

## Anti-patterns

- Expecting Hermes to scrape Manifest dashboard for 300+ models
- Setting `discover_models: true` (default) after hand-listing favorites — list collapses to `auto` only

## Related

- `manifest-auto-routing-jun-2026.md` — `auto` smoke + `X-Manifest-*` headers
- `manifest-self-hosted-docker-lan-jun-2026.md` — local `mnfst_` key + `:2099/v1`