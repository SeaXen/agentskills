# AceRoute header-settings and layout pitfalls

Session distilled lessons for dense single-file dashboards with many pages.

## 1) Do a structural audit before styling micro-patches
If screenshots show "some cards huge, some tiny, text not fitting, random empty space", treat it as a shared layout-system failure first:
- mixed grid systems across pages
- missing CSS classes for new markup
- stale span rules
- mobile overrides still targeting removed controls

Fix shared grid/span/card rules before page-local cosmetics.

## 2) Verify markup/CSS class-name parity
A real failure pattern:
- markup used `models-insights-row`
- CSS styled `model-insights-row`

Result: chips collapse into ugly raw text.

For screenshot-driven repairs, explicitly diff new markup class names against existing CSS selectors before chasing spacing.

## 3) In giant inline HTML/JS files, avoid ambiguous partial replacements
Large single-file dashboards are prone to patch corruption when replacing short repeated fragments. Observed failure mode: trailing junk appended after inline card rows during repeated partial replacements.

Safer pattern:
- patch with longer unique anchors
- immediately grep/read the touched block
- run syntax checks right after each risky edit
- prefer one structural replacement over many tiny overlapping edits

## 4) When centralizing controls into a header settings panel, remove duplicates everywhere
If moving repeated page-level controls into one header settings drawer:
- remove old per-page dropdowns/buttons from every page bar
- update all state setters so old per-page `set*Window()` functions delegate to the new global setting
- remove stale DOM lookups for deleted controls
- patch mobile CSS that still assumes the old header controls exist

## 5) For this user's dashboard taste, prefer compact operator UI
Strong user preferences surfaced repeatedly:
- icon-only refresh is preferred over text button labels
- repeated duration dropdowns across pages are considered clutter
- theme switch belongs inside settings, not in the main header row
- one global duration selector is better than per-page copies
- compact dense layout beats decorative card treatments

## 6) If visual pass is blocked, still verify the real code path
When full browser automation is flaky, still do the durable checks:
- JS syntax check
- Python syntax check
- grep served HTML for new controls/version markers
- confirm deleted selectors are actually gone
- cache-bust JS/CSS when header controls change

Do not save the transient browser failure itself as a rule; save the fallback verification pattern.
