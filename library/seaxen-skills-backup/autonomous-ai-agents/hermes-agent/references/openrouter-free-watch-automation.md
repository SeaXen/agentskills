# OpenRouter free-watch automation

Use this pattern when the user wants Hermes to both notify on OpenRouter free-model changes and automatically keep the Hermes model picker/current alias set in sync.

## Recommended architecture

- Create a `cronjob` with:
  - `script: openrouter_free_watch.py`
  - `no_agent: true`
  - `deliver: origin`
- Keep the script under `~/.hermes/scripts/`.
- Use the user's custom OpenRouter catalog override file, typically:
  - `~/.hermes/cache/free_openrouter_catalog.json`
- If the user wants CLI-friendly direct selection, also maintain aliases in `~/.hermes/config.yaml` under `model_aliases:`.

## What the watcher should do

1. Load `OPENROUTER_API_KEY` from env or known Hermes `.env` paths.
2. Query:
   - `https://openrouter.ai/api/v1/auth/key`
   - `https://openrouter.ai/api/v1/models`
3. Build current live free-model set from `pricing.prompt == 0` and `pricing.completion == 0`.
4. Compare with prior state in a state file such as:
   - `~/.hermes/cron_state/openrouter_free_watch.json`
5. Alert on:
   - paid usage increase
   - remaining credit drop
   - watched model availability/free-status changes
   - newly added free models
   - removed free models
6. Update the local free-model catalog file so Hermes picker follows live OpenRouter free inventory.
7. Update an auto-managed alias block in `config.yaml` for newly discovered free models.
8. Stay silent when nothing changed.

## Important implementation details

### 1) Keep cheap/manual catalog entries
When rewriting the custom catalog JSON, do not destroy the user's non-free curated entries. Preserve cheap/manual models and only replace the free-model portion.

### 2) Do not spam on every run
When deciding whether the catalog changed, compare normalized payloads and ignore timestamp-only fields such as `updated_at`. Otherwise every run looks like a change and the cron will notify constantly.

### 3) Preserve manual aliases
Only manage aliases inside a clearly marked block, for example:

- `# BEGIN AUTO OPENROUTER FREE ALIASES`
- `# END AUTO OPENROUTER FREE ALIASES`

Parse the `model_aliases:` section and exclude manually maintained aliases from auto-generation.

### 4) Insert the managed block in the right place
Write the auto alias block inside `model_aliases:` and before the fallback-model comment block. If the block is inserted after `model_aliases:` ends, YAML structure becomes wrong or aliases disappear from the intended section.

### 5) Make reruns idempotent
After the first sync run, a second immediate run should usually produce empty stdout. For `no_agent=True` cron jobs, empty stdout means no user notification, which is the desired steady state.

## Verification checklist

- Run the script manually once: expect sync/update output if drift exists.
- Run it again immediately: expect empty stdout if no changes remain.
- Confirm the catalog file contains current free models.
- Confirm the config file still contains manual aliases plus the managed auto block.
- Confirm the cron job still points to the same script and remains enabled.

## Notes

- Some OpenRouter free models may not end with `:free` (for example `openrouter/owl-alpha` or `openrouter/free`). Use pricing-based detection, not suffix-only detection.
- Good alias naming pattern for auto-generated aliases: `or-auto-<slug>`, with truncation/hash fallback for very long model IDs.
