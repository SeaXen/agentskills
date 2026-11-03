# Selective Past-Session Import Pattern

Use when Dr. Sagar asks to bring older Hermes work into the Obsidian vault.

## Goal

Import durable knowledge from past sessions without turning the vault into transcript sludge.

## Source

Use Hermes session search as source of truth. Search by topic clusters, not one giant query.

Good clusters:

- Graphify / SeaDash / port conventions
- WordPress / mdsagar.com / FCPS / MRCP content pipeline
- OpenRouter / model/provider setup
- Fabric / memory / self-improvement policy
- skills / CLI workflows / agent orchestration

## Import rules

- Import by original session date into `Daily/YYYY-MM-DD.md`.
- Add only high-signal bullets: decisions, fixes, root causes, durable setup changes, reusable workflow lessons.
- Prefix imported bullets with `Imported —` so future cleanup can distinguish them from same-day notes.
- Preserve links with `[[wikilinks]]` to project, decision, issue/fix, and knowledge pages.
- Redact secrets as `[REDACTED]`.
- Do not import raw transcript text, message IDs, temporary process IDs, PR numbers, issue numbers, or commit SHAs unless the ID is still operationally necessary.

## Destination updates

After daily imports, update the relevant aggregate pages:

- `Memory/decisions.md` for durable decisions.
- `System/Assistant/issues-fixes-log.md` for verified fixes/root causes.
- `Knowledge/Hermes Operations.md` for reusable Hermes operating knowledge.
- `Work/<project>.md` for durable project state.

## Verification

Verify with at least:

- Daily note count / changed files.
- Search for `Imported —` markers.
- Browser dashboard graph API if the dashboard is running: expected fields include note count, link count, daily count.

## Known-good result from initial import

Initial selective import created/updated 6 daily notes for 2026-05-18, 2026-05-19, 2026-05-22, 2026-05-23, 2026-05-24, and 2026-05-25; added 15 `Imported —` markers; updated decisions, issues/fixes, and Hermes Operations; dashboard saw 20 notes, 70 links, and 6 daily notes.
