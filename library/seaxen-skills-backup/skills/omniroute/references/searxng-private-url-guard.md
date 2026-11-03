# OmniRoute search provider blocked on private/local URL

## Symptom

Provider page shows:
- `error`
- `Upstream error`
- `Blocked private or local provider URL`

This appeared on the OmniRoute `searxng-search` provider page.

## Verified facts

- The exact guard string comes from OmniRoute source:
  - `src/shared/network/outboundUrlGuard.ts`
- Relevant constants / flags:
  - `PROVIDER_URL_BLOCKED_MESSAGE = "Blocked private or local provider URL"`
  - `OMNIROUTE_ALLOW_PRIVATE_PROVIDER_URLS`
  - `OMNIROUTE_ALLOW_LOCAL_PROVIDER_URLS`
- Feature flag definition says:
  - `OMNIROUTE_ALLOW_PRIVATE_PROVIDER_URLS` default = `false`
  - `OMNIROUTE_ALLOW_LOCAL_PROVIDER_URLS` default = `true`
- In the running container, `OMNIROUTE_ALLOW_PRIVATE_PROVIDER_URLS` was unset.

## Practical meaning

If a provider URL points to:
- `localhost`
- `127.0.0.1`
- `192.168.x.x`
- another RFC1918/private address

OmniRoute may refuse it unless private provider URLs are explicitly allowed.

## Hermes-specific detail

Hermes' bundled SearXNG web plugin expects:
- env var: `SEARXNG_URL`
- value = base URL only, e.g. `http://localhost:8080`

Do **not** set:
- `http://host:port/search`

because Hermes appends `/search?format=json&q=...` itself.

## Diagnostic sequence

1. Read the exact provider status text in OmniRoute.
2. If it says `Blocked private or local provider URL`, inspect OmniRoute env / `server.env` first.
3. Confirm the target endpoint is actually reachable.
4. Only after the endpoint works, wire Hermes to the base URL.

## Important caveat

You can have two independent failures at once:
1. OmniRoute policy block on private/local URLs.
2. SearXNG not actually listening on the assumed host/port.

Do not assume the policy error means the target service is healthy.
