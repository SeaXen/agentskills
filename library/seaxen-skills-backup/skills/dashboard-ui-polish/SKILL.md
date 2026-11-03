---
name: dashboard-ui-polish
description: Refine and verify self-hosted dashboard UI details from screenshot-driven feedback, especially control-row layout, label removal, always-visible inputs, and exact visual matching.
---

# Dashboard UI polish

Use this when the user wants small-but-exact UI changes in a dashboard or web app: remove labels, move controls into the same row, make a search/input always visible, tighten spacing, or match a screenshot more literally.

Finishing-pass skill. Refs: `references/compact-dark-dashboard-css.md`, `references/settings-safety-controls.md`, `references/static-site-header-polish.md`, `references/aceroute-layout-audit.md`, `references/aceroute-header-settings-and-layout-pitfalls.md`, `references/inline-style-and-vision-critique-pitfalls.md`.

## When to use
- User gives screenshot-based correction.
- A feature works functionally but the layout/visibility is still wrong.
- Dense settings/dashboard polish; prefer compact operator UI and fewer repeated controls.

## Core rule
Treat the screenshot literally; if multiple pages look wrong, suspect shared CSS, class-name mismatch, or stale span rules before widget tweaks.

If the user says "one chart, not two" or "attach these together so they look like one bar with two sections," that is the requirement. Do not preserve the previous structure just because it is easier.

For this user, also bias towards compact operator UI:
- icon-only refresh preferred over text button labels
- repeated duration dropdowns across pages are considered clutter
- theme switch belongs inside settings, not in the main header row
- one global duration selector is better than per-page copies

## Inline `<style>` blocks defeat external CSS edits (monolith SPAs)

**Always diff your new CSS selector against the inline `<style>` block in `index.html` before assuming it will apply.** Large monolithic SPAs often have a `<style>` block with `!important` rules on the same selectors you are styling externally. Inline loads after the external link, so the inline wins and your new tiered-grid / hero-card CSS does nothing.

Diagnostic: `browser_console(expression='getComputedStyle(targetEl).gridTemplateColumns')`. If the value is the old `auto-fit minmax` value, the inline block is winning.

Fix: patch the inline `<style>` block in `index.html` rather than adding more specificity to the external file.

## Vision-tool critiques confabulate specifics

A vision-model design critique often returns plausible-sounding specifics (chip text, column bindings, "20+ (untitled) sessions") that do not match the actual UI. Vision LLMs pattern-match admin-template tropes.

For UI critique work:
- Use vision tools for **shape/layout description** (which row layout, what icons, what colors).
- **Do not treat prose critiques as verified fact.** Ground specific textual claims in `rg`, DOM inspection, or `getComputedStyle` before patching.

Detailed patterns, root causes, and verified fix recipes in `references/inline-style-and-vision-critique-pitfalls.md`.

## Verification checklist
- After a layout change, confirm with `getComputedStyle` that the new rule actually applied (catches inline `<style>` override traps).
- Cross-check screenshot claims against served HTML/JS before patching — vision tools confabulate.
- Grep the served HTML for new control/version markers (cache-bust JS/CSS when header controls change).
- Check every tab/page affected, not just the one the user first mentioned.
- Confirm short cards do not stretch to tall chart height on mixed grids.
