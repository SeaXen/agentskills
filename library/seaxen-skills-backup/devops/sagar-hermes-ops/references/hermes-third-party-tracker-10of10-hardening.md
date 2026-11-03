# Hermes third-party tracker 10/10 hardening

Use this reference when a Hermes dashboard tracker tab needs to move from "looks okay" to operator-grade.

## What made the difference
- Treat live plugin/API inventory as the source of truth.
- Keep static JSON as fallback / last-known-good only.
- Wire refresh to a real rescan (`Scan live`), not just a re-read of cached data.
- Show refresh health clearly: source, generated time, last refresh result, generator path.
- Split counts into `auto-tracked` vs `manual-only` so weak coverage is visible.
- Add a hide/show toggle for manual items to keep triage screens readable.

## Manual/copied plugin handling
Do not pretend certainty when upstream metadata is missing.

Recommended fields in the generated inventory:
- `primary_source_url`
- `source_links`
- `source_confidence`
- `source_reason`
- `search_url`
- `manual_reason`

Recommended confidence buckets:
- `exact_repo` — clear repo match for the plugin
- `candidate_repo` — likely repo but not fully proven
- `related_links` — only docs/provider/signup links found
- `unknown` — no trustworthy upstream metadata found

## UI pattern for manual rows
Each manual row should expose:
- confidence chip
- hostname/source chip when available
- `Open source`
- `Search more` or `Find source`
- `Copy path`
- `why manual`
- `source confidence`

Good operator utility bar actions:
- `Copy all paths`
- `Copy source links`
- `Copy lookup searches`

## Verification pattern
1. Syntax/compile check backend generator.
2. Syntax check frontend bundle.
3. Regenerate the inventory and inspect the output payload.
4. Verify the live browser page.
5. Check browser console for JS errors.
6. If the dashboard has both a wrapper route and a raw/plugin route, verify the raw/plugin route too.

## Important distinction
A wrapper route can be auth-gated or cached and still make the tab look broken or stale.
That does not prove the tracker tab itself is broken.

For honest verification:
- test the normal app route if available
- also test the raw/plugin route when available
- treat differences between them as routing/session issues until proven otherwise

## Copy actions
Do not rely only on `navigator.clipboard`.
Use a fallback path for dashboard/browser contexts that block direct clipboard access.

## Standard of success
"10/10" here means:
- visually clean
- live and current
- operationally useful
- explicit about uncertainty
- no fake certainty for heuristic manual-source matches
