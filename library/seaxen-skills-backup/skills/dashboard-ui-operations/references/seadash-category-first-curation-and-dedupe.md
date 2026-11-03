# Category-first curation and dedupe

Use when the user wants SeaDash to feel like a curated dashboard instead of an auto-generated inventory dump.

## Durable patterns

- Prefer one primary inventory split when the user says each app should appear only once.
  - Good default: `Docker Apps` and `Non-Docker Apps`.
  - Hide duplicate exposure-derived sections (`public`, `internal`, `sensitive`) from the main page instead of deleting their underlying alert logic.
- Treat duplicated `custom_apps` entries as overlays, not separate visible cards.
  - Match on stable identity (`source_name`/`name` plus section semantics).
  - Merge durable metadata from custom config into the primary app record.
  - Keep live runtime state from Docker/core discovery.
- If the user thinks in categories, rename the UI accordingly.
  - `Layout Studio` -> `Categories & Layout`
  - `Column` -> `Category`
- Remove starter/demo categories from persisted config when the user wants a clean personal dashboard. Example anti-pattern: a leftover `Daily Ops` category that keeps reappearing after reload.
- If `Core Apps` are really just another non-Docker bucket from the user's perspective, unify them under `Non-Docker Apps` and hide the separate core section.

## Verification checklist

- No duplicate visible app names across main sections.
- Exposure alerts still exist in banner/modal, but exposure sections are hidden if the dashboard is in curated mode.
- Category picker uses the same deduped source as visible sections.
- Edit modal resolves against deduped visible data, not raw backing arrays.
- Table mode shows the same operator-useful data as card mode, especially status and reachable URLs.
- After adding new category fields, reopen the modal and verify the inputs actually exist in the live DOM.

## Useful category customization fields

Start with low-risk fields that improve curation without forcing a data-model rewrite:

- category title
- icon
- accent color
- note/subtitle
- badge label
- style preset (`default`, `compact`, `highlight`)

These are good first additions before attempting deeper features like nested groups or per-category permissions.
