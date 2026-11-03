# Dashboard UI audit evidence recipe

Use this for dense operational dashboards where a screenshot alone is insufficient.

## Evidence matrix

| Surface | Visual check | DOM/runtime receipt |
|---|---|---|
| Desktop home | hierarchy, density, clipping, repeated actions | console errors; visible card/action counts |
| Mobile home | real 390×844 or similar viewport; touch targets; hidden controls; tab overflow | wait for async load; verify final card/KPI counts |
| Settings/modal | grouping, danger separation, narrow-screen fit | `role="dialog"`, `aria-modal`, label, focus movement, Escape, trap/inert background |
| Hidden/recovery | terminology and safe recovery | compare action labels and handlers; flag duplicate actions with identical effect |
| Scanner/import | idle state, action enablement, populated results | execute only non-destructive scan; record count and confirm zero default selections |
| Sections/layout | modal density, clipping, mode affordance | count rows; check labels, semantics, focus, and scroll containment |
| Favicon/PWA | visible brand consistency | live status/content type plus actual image dimensions; manifest and service worker |
| Maintainability | component/style consistency | file size/shape, duplicate overrides, test discovery, source-vs-live freshness |

## Narrow-viewport capture

When the interactive browser cannot resize, use an installed headless browser with:

- an isolated profile under `/tmp`,
- explicit `--window-size`,
- enough virtual-time budget for API-backed rendering,
- screenshots under `/tmp`, never inside a read-only audited repository.

Capture twice if necessary: the first image may contain placeholders. Judge the loaded image, not the loading state.

## Non-destructive boundary

Opening tabs and modals is safe. A scanner GET is usually observational if the user explicitly asked to test it, but importing results, changing settings, restarting services, hiding cards, deleting items, pruning Docker, restoring snapshots, or saving presets crosses into mutation and should not be triggered during a no-modification audit.

## Reporting

Give separate 0–10 scores for desktop, mobile, UX, accessibility, maintainability/testing, and feature completeness. Lead with the verdict, then concise prioritized findings with concrete receipts. Explicitly state whether repository files were modified and distinguish temporary `/tmp` artifacts.