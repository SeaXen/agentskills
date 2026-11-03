# Mission Control Bitwarden Controls

Use this when adding or repairing a Hermes Mission Control secrets/provider-health surface for Dr. Sagar.

## Preferred IA
- Put it under `Mission Control → Controls`.
- Use an internal `Bitwarden` sub-tab or grouped cards.
- Do **not** create a new top-level route just for secret status unless the user explicitly asks.

## Safe display rules
- Never render raw secret values.
- Safe fields:
  - enabled / configured
  - env var name
  - source (`bitwarden`, local env, inline/local-only)
  - masked preview only
  - provider base URL / model
  - health/test result
  - drift warnings
- Do not misclassify local-only auth patterns like Ollama as Bitwarden drift.

## Backend pattern
- If the plugin is shipped as a built bundle, patch the served backend/frontend pair directly:
  - `plugins/mission-control/dashboard/plugin_api.py`
  - `plugins/mission-control/dashboard/dist/index.js`
- Build payloads from live runtime state, not only files on disk.
- Load runtime env first with Hermes env loading so Bitwarden-applied vars are present.
- Useful payload sections:
  - Bitwarden v1: status + sync
  - Bitwarden v2: provider wiring
  - Bitwarden v2: drift + API server

## Verification sequence
1. Syntax-check backend/frontend.
2. Call backend functions directly in Hermes venv.
3. Probe authenticated plugin HTTP routes on the real dashboard service.
4. Verify in the browser on the live Mission Control page.

## Port/runtime pitfall
- Do not assume the first open Hermes port is the real Mission Control surface.
- Check the systemd unit `ExecStart` / listening port first.
- Secondary ports or wrapper routes may return shell HTML, `401`, or `405` and mislead you.

## Good endpoint shape
- `GET /api/plugins/mission-control/bitwarden-status`
- `POST /api/plugins/mission-control/bitwarden-sync`

## Notes
- For Dr. Sagar, the right UX is operational clarity: secret source, provider wiring, API-server state, drift warnings, and live sync — not decorative dashboard sprawl.
