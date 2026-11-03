# Manifest custom tiers vs Hermes model picker (Jun 2026)

## What was verified
- Manifest custom routing tiers can be keyed off arbitrary request headers, e.g.:
  - header key: `x-manifest-tier`
  - header value: `bynara`
- This does **not** make `bynara` a model ID.
- Hermes custom-provider model selection is driven by the endpoint's `GET /v1/models` response.
- On the tested Manifest endpoint, `GET /v1/models` returned only:
  - `auto`

## Operational consequence
- In Hermes, the model picker will show only `auto` for that Manifest endpoint.
- Adding many upstream models or custom tiers inside Manifest does not automatically produce multiple selectable Hermes models.
- Manifest tiers/routes are server-side routing rules; Hermes treats them separately from model IDs unless the endpoint itself exposes them as models.

## Correct explanation shape for Dr. Sagar
1. Verify `/v1/models` first.
2. If it returns only `auto`, say plainly that Hermes is behaving as designed.
3. Explain that custom Manifest tiers are header-based routes, not models.
4. Do not call it a Hermes bug unless the endpoint exposes multiple model IDs and Hermes still hides them.

## Practical workaround
- If Dr. Sagar wants multiple Manifest routes selectable inside Hermes, expose them as separate Hermes custom providers / proxy base URLs, each injecting a different fixed header such as:
  - `x-manifest-tier: bynara`
  - `x-manifest-tier: reasoning`
- Then Hermes can switch by provider/base URL, even though it cannot natively surface Manifest custom-tier headers in the standard model picker.

## Important nuance
- Docs listing built-in Manifest tiers (`simple`, `standard`, `complex`, `reasoning`) do not invalidate custom header-based tiers configured in the Manifest UI.
- A request using `x-manifest-tier: bynara` is correct **only if** that custom tier exists in Manifest with the exact same key/value match.
