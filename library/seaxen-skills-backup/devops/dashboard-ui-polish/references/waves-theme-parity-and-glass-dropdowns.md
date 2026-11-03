# Waves theme parity and glass dropdowns

Use when a dashboard/web app has a new named theme (for example a TraderWaves-like dark glass theme) but parts of the UI still look like the previous theme.

## Symptom pattern
- User says cards/header/background/text still look like the old theme.
- Some pages switch theme correctly, others stay on default dark/light.
- Dropdowns/popovers/selects look especially wrong in glass themes.
- Screenshot feedback points to many mismatched surfaces, not one isolated component.

## Root-cause checklist
1. Search for hardcoded framework colors still in shared pages/components:
   - `bg-slate-*`, `bg-zinc-*`, `text-slate-*`, `text-zinc-*`, `border-slate-*`, `border-zinc-*`
2. Check custom theme utility coverage:
   - if code uses classes like `bg-bg/95`, `bg-bg-alt/70`, `border-bg-line/60`, confirm those classes actually exist
   - missing opacity variants can silently fall back to old-looking styles
3. Inspect computed styles in the live DOM, not just variable definitions.
4. Compare against the reference site directly for:
   - page background
   - card translucency / blur
   - text hierarchy
   - header/nav surface
   - dropdown/popover treatment

## Fix pattern
- Add compatibility overrides for legacy hardcoded Tailwind palette classes under the named theme.
- Add the missing custom utility opacity variants if the codebase already uses them.
- Create explicit classes for glass hero panels and menu flyouts instead of hoping generic cards look right.
- For menus/dropdowns in glass themes, set all of these explicitly:
  - background/gradient
  - border
  - blur
  - radius
  - shadow
  - item radius/hover

## Verification
- Check `data-theme` in the live DOM.
- Read computed `backgroundColor` / `backgroundImage` / `borderColor` for representative surfaces.
- Verify one page with shared dashboard cards and one page with legacy hardcoded classes.
- Verify a dropdown/popup, not just page cards.
