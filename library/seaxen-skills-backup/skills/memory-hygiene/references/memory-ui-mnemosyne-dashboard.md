# Mnemosyne dashboard integration checklist

Use when the user wants Hermes dashboard memory UI to expose the active external memory provider cleanly.

## Scope that proved safest

- Treat Mnemosyne support as **read-only first**.
- Keep built-in `USER.md` and `MEMORY.md` visible alongside provider-backed data.
- Prefer one existing `/memory` page with an internal Mnemosyne section over a new top-level page.

## Safe implementation pattern

1. Inspect the plugin backend and built frontend separately.
2. Add provider status to the plugin API payload first.
3. Add frontend rendering for provider summary + detail section.
4. Reuse existing dashboard CSS/components where possible to keep the patch surface small.
5. Validate backend syntax and frontend syntax before touching the running dashboard.

## Verification sequence

1. Confirm the provider is actually active from Hermes CLI.
2. Inspect the provider store directly to confirm real data exists.
3. Verify plugin backend functions return provider payload when imported directly.
4. Hit live dashboard API routes and confirm JSON contains the provider block.
5. Open the dashboard page in a browser and confirm the provider section is visibly rendered.

## Important pitfall

A dashboard plugin rescan may be insufficient after patching plugin routes or frontend bundles.

Observed durable pattern:
- on-disk patch present
- direct backend import works
- live route still returns stale HTML / old payload
- full dashboard restart is required before the new provider route appears live

So do **not** conclude the patch failed until you verify after a restart.

## Mnemosyne-specific notes

- Honest empty states are better than fake richness.
- If tables such as `episodic_memory`, `triples`, or `scratchpad` exist but are empty, show zero-count sections rather than inventing content.
- Avoid creating or mutating provider memories from ambiguous user shorthand during UI work.

## Good result shape

- provider summary card
- active-provider indicator
- db-found indicator
- read-only search/limit controls
- separate counts for working / episodic / facts
- detailed lists only for stores that actually contain data
