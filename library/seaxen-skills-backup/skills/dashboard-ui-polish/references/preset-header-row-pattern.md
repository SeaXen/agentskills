# Preset header row refinement pattern

Use this reference when a user wants a toolbar/header row to become the control itself rather than a label plus a second-line widget.

## Trigger phrases
- "remove this text"
- "make whole bar/row searchbar"
- "not after click"
- "keep Add"
- screenshot pointing to the exact row layout

## Translation to implementation
- Remove the static section label entirely.
- Remove search-toggle/open-close behavior.
- Render a persistent search input in the main row.
- Keep the Add/action button on the same row.
- Let the search input take remaining width.

## Cleanup checklist
- delete obsolete toggle state
- delete obsolete persistence keys for toggle visibility
- remove dead handlers that only supported the old conditional UI
- make sure add/create flows do not still flip the old visibility state

## Verification checklist
- build passes
- live page shows no old label text
- input is visible without clicking anything
- action button is still visible on the same row
- screenshot/vision check matches the user's complaint, not just the code intent

## Why this matters
For this user, small UI layout mismatches are correctness bugs. A functionally similar layout is not enough if the visible arrangement still contradicts the screenshot-guided request.
