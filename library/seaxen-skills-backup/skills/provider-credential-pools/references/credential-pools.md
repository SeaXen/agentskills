# Credential pools: practical notes

## Pool keys
- Standard providers use their provider id: `nvidia`, `openrouter`, `anthropic`, etc.
- Custom OpenAI-compatible endpoints use `custom:<normalized_name>`.
  - Example: `custom:bynara.id` for a custom provider named `Bynara.id`.

## Add keys
Use the same pool key repeatedly:

```bash
hermes auth add nvidia --type api-key --label hrsea7 --api-key <KEY_1>
hermes auth add nvidia --type api-key --label drhrsagar --api-key <KEY_2>
hermes auth add custom:bynara.id --type api-key --label hrsea7 --api-key <KEY_1>
```

## Rotation strategy
Set per-provider strategy in `~/.hermes/config.yaml`:

```yaml
credential_pool_strategies:
  nvidia: fill_first
  custom:bynara.id: round_robin
```

Available strategies: `fill_first`, `round_robin`, `least_used`, `random`.

## Removal behavior
- `hermes auth remove <provider> <index>` removes the pool entry.
- For config-seeded custom providers, removal also suppresses the source so Hermes does not re-seed it on the next load.
- If the original credential is still exported in `~/.hermes/.env` or the shell environment, Hermes may keep re-seeding it until that source is removed or suppressed.

## Troubleshooting
- `hermes auth list <provider>` shows the active pool and marks the current credential with `←`.
- If an old inline `api_key` still exists in `custom_providers`, it will seed an extra credential unless you remove that field from config.
- Upstream services often expose model limits but not precise remaining quota through `/v1/models`; track usage externally if the provider dashboard does not expose it.
