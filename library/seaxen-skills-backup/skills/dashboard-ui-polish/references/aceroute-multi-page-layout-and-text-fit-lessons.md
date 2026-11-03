# AceRoute multi-page layout and text-fit lessons

Use when a user says a dashboard still looks bad across many pages after several local fixes.

## Trigger phrases
- "all pages are disaster"
- "some card are big some are small"
- "many thing not look good"
- "text not fit"
- "too much empty space"

## Working rule
Stop doing local widget tweaks. Audit all affected pages and normalize the shared layout/CSS system first.

## High-value audit checklist
1. Compare markup class names to CSS selectors for every shared section.
   - Example failure class: `model-insights-row` vs `models-insights-row`.
   - These mismatches silently break whole rows and make text jam together.
2. Look for hardcoded giant heights/min-heights creating dead space.
   - Replace fixed heights with tighter `min-height` + `height:auto` where possible.
3. Check podium/highlight cards for missing text clamps.
   - Clamp title/subtitle to 2 lines.
   - Add `word-break` / `overflow-wrap` for long model/session names.
4. Check stack/list rows.
   - Left text should clamp or wrap cleanly.
   - Right metadata should not stay `white-space: nowrap` if it breaks fit.
5. Check chip/filter rows.
   - Wrap instead of forcing one line.
   - Apply max-width + ellipsis to long chips.
6. Remove decorative noise before adding more data.
   - Avoid gratuitous gradients, underline rules, hover lifts, and glow when the user wants dense operator UI.
7. Rebalance page spans globally.
   - Use explicit grid rules for Home / Costs / Requests / Models instead of ad-hoc wide-span hacks.

## Verification pattern
- Run syntax checks after every patch (`node --check`, Python compile).
- Verify served cache-busted asset version.
- Verify live endpoints for any affected pages.
- If browser automation is flaky, use screenshots + code audit + live endpoint verification and say exactly what you could and could not verify visually.

## User-specific preference signal captured here
This user strongly dislikes:
- text collisions
- unequal card sizes
- random decoration
- wasted empty space

Start from dense, compact, low-noise layout defaults and prove page-by-page fit before claiming success.
