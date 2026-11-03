---
name: provider-credential-pools
description: Manage multiple API keys or OAuth credentials for a single Hermes provider with failover and rotation.
---

# Provider Credential Pools

Use this skill when a Hermes provider needs multiple credentials for the same upstream service and you want automatic rotation, failover, or quota spreading.

## When to use
- The user has more than one API key for the same provider.
- The user wants automatic switch-over when one key hits quota or rate limits.
- The user wants to add/remove/list credentials by index or label.
- The user is using custom OpenAI-compatible endpoints and needs a pool under `custom:<name>`.

## Core model
- A provider can have multiple pooled credentials.
- Hermes chooses one credential per request according to the configured strategy.
- Strategies are provider-scoped, not global.

## Standard workflow
1. Inspect the current pool:
   ```bash
   hermes auth list <provider>
   ```
2. Add credentials to the same provider pool:
   ```bash
   hermes auth add <provider> --type api-key --label <label> --api-key <key>
   ```
3. Set the pool strategy in `~/.hermes/config.yaml`:
   ```yaml
   credential_pool_strategies:
     <provider>: fill_first
   ```
4. Verify the pool order and current active credential with `hermes auth list <provider>`.

## Strategies
- `fill_first`: use the first healthy key until it exhausts, then move on.
- `round_robin`: rotate evenly across all keys.
- `least_used`: prefer the credential with the lowest usage count.
- `random`: choose randomly among healthy credentials.

## Custom provider pools
- Custom OpenAI-compatible endpoints use a pool key of the form `custom:<normalized_name>`.
- Example: a custom provider named `Bynara.id` is addressed as `custom:bynara.id`.
- If a custom provider is seeded from `config.yaml` with an inline `api_key`, removing the pool entry suppresses that seed source; it does **not** edit the user config file automatically.
- See `references/credential-pools.md` for a compact command recipe and provider-specific quirks.

## Removal and cleanup
- Remove by index when labels are ambiguous:
  ```bash
  hermes auth remove <provider> 2
  ```
- `hermes auth reset <provider>` clears exhaustion / cooldown state.
- If a provider is also seeded from environment variables or `~/.hermes/.env`, removing the pool entry may not be enough; remove or suppress the original env source too.

## Practical guidance
- Use `fill_first` when one key is primary and the rest are backups.
- Use `round_robin` when all keys are meant to share load.
- Use `least_used` when traffic is uneven and you want balancing without strict cycling.
- Prefer labels that identify the owner/account, not the secret itself.

## Pitfalls
- A provider may still show one env-seeded credential if a shell variable or `.env` entry remains active.
- A custom provider with an inline `api_key` in `config.yaml` can silently recreate a removed pool entry unless that field is removed or suppressed.
- Some upstream services expose model context windows but do not expose precise remaining quota via the model API; budget tracking may need to be external.

## Verification
- `hermes auth list <provider>` should show the expected number of credentials.
- The current credential is marked with `←`.
- After a removal, re-run `hermes auth list <provider>` to confirm the pool collapsed as expected.
