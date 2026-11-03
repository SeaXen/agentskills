# OpenAI Codex pooled auth: why `round_robin` can still look like one account

Use when Dr. Sagar asks why Hermes keeps using one Codex auth even though the pool strategy is `round_robin`.

## Core rule
Configured strategy and effective behavior are not the same thing.

`round_robin` rotates only across **available** credentials.
- `ok` = eligible
- `exhausted` = temporarily excluded until reset/cooldown
- `dead` = excluded until re-auth replaces the bad token state

If only one entry is `ok`, the pool behaves like single-auth regardless of the configured strategy.

## Good explanation pattern
1. Show configured strategy.
2. Show live pool entry states.
3. Derive the effective healthy set.
4. State the consequence plainly.
5. Recommend re-auth / cleanup only if needed.

Example operator conclusion:
- strategy = `round_robin`
- statuses = 1 `ok`, 1 `exhausted`, 4 `dead`
- effective usable set = 1 credential
- consequence = no visible rotation is possible

## Practical notes
- `dead` usually means revoked/invalidated/stale OAuth state, not a rotation bug.
- `exhausted` means quota/rate window, not permanent breakage.
- The right fix is usually to re-auth dead entries and optionally remove stale ones, not to change `round_robin`.
- If the user only wants to know whether auth works, a successful live `hermes chat --provider openai-codex ...` probe is enough.
