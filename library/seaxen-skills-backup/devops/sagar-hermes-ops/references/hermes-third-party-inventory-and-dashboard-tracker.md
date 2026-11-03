# Hermes third-party inventory and dashboard tracker

Use this pattern when Dr. Sagar wants durable tracking of unofficial/community Hermes additions without adding a lot of maintenance overhead.

## Goal
Maintain one low-noise inventory for:
- plugins under `~/.hermes/plugins`
- hub/url skills
- other git repos under `~/.hermes`
- external git repos referenced by Hermes config local paths when detectable

## Preferred approach
1. Prefer live filesystem/config inspection over chat-history reconstruction.
   - Inventory the installed state directly.
   - Treat session history as supplemental, not primary provenance.
2. For tracker tabs, prefer **live-first inventory fetch** on page load.
   - Use the plugin/API live inventory as the source of truth.
   - Keep static JSON as fallback or last-known-good data, not the primary load path.
3. Separate the full inventory from the user-facing alert channel.
   - Full inventory can be markdown + JSON.
   - Scheduled notifications should emit only actionable updates.
4. For old copied/manual plugins with no clean upstream metadata, do not force reconnect/remap unless the user explicitly wants migration work.
   - Track them as manual/local.
   - Add inferred upstream hints only when evidence exists in installed files.
5. For dashboard visibility, a local dashboard plugin tab is acceptable when the user wants one place to review the tracker.
   - Keep the tab simple: summary counts, update lists, manual/local items, file paths.
6. If the page exposes a refresh action, make it a **real rescan/rebuild** action.
   - Prefer a label like `Scan live` over a vague `Reload` when the action re-runs the inventory generator.
7. If the page exposes copy buttons for commands, add a clipboard fallback.
   - `navigator.clipboard` can fail in dashboard/browser contexts.
   - Keep a textarea + `document.execCommand('copy')` fallback for operator commands.

## Dashboard implementation note
If a local dashboard plugin route loads but a custom plugin API fetch returns the dashboard HTML shell instead of JSON, do not keep insisting the API path is the right integration point.

Use a simpler fallback:
- generate inventory JSON to a normal report path
- mirror the same JSON into the dashboard plugin static asset directory
- have the dashboard frontend fetch the static JSON asset

This is acceptable for low-frequency inventory views and avoids backend/plugin-mount ambiguity.

## Scheduling pattern
Preferred default for this user:
- weekly Friday run
- refresh the full inventory every run
- only send a chat message when actionable updates exist

## Verify
- inventory script runs successfully
- JSON report is written
- dashboard tab loads real data, not placeholders
- scheduled notifier output is concise and actionable

## Pitfalls
- using chat memory as the primary inventory source
- spamming the user with the full inventory every scheduled run
- counting the tracker plugin itself as a tracked manual plugin
- claiming the dashboard tab works without loading the actual route and checking rendered counts
