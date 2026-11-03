# Hermes custom provider credential pools

Use this for custom OpenAI-compatible providers that need multiple API keys or account rotation.

## Pool key
- Custom providers are pooled under `custom:<normalized_name>`.
- The normalized name comes from the `custom_providers:` entry name.

## Add credentials
Use one `hermes auth add` per key:

```bash
hermes auth add custom:<name> --type api-key --label <label> --api-key <secret>
```

Examples:

```bash
hermes auth add custom:bynara.id --type api-key --label hrsea7 --api-key ...
hermes auth add custom:bynara.id --type api-key --label Drpelagik --api-key ...
```

## Rotation strategy
Set this in `~/.hermes/config.yaml`:

```yaml
credential_pool_strategies:
  custom:bynara.id: fill_first
```

Strategies:
- `fill_first` — use the current healthy key until it exhausts, then move on
- `round_robin` — cycle evenly across healthy keys
- `least_used` — prefer the least-used healthy key
- `random` — pick a healthy key at random

## Maintenance commands
```bash
hermes auth list custom:bynara.id
hermes auth remove custom:bynara.id 1
hermes auth reset custom:bynara.id
```

## Important limitation
Hermes model pickers only show model IDs returned by the provider’s `/v1/models` response. If a routing system uses custom headers or route labels instead of advertising separate model IDs, Hermes will only expose the advertised model(s).