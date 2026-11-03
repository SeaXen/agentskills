# Theme parity and hardcoded color traps

Use when a user says a custom theme still does not match the reference site, or when light/dark/theme switching only updates part of the UI.

## Signals
- Some cards/header/text/background switch, others stay in the old theme.
- User says parts still look like the default dark theme even after selecting the new theme.
- Light mode still shows dark chips, headers, cards, or inputs.
- DOM shows `data-theme` is correct, but computed colors on key elements are still wrong.

## Root-cause checklist
1. Check for hardcoded Tailwind palette classes (`slate-*`, `zinc-*`, `gray-*`, `neutral-*`) in pages/components that should be theme-driven.
2. Check for custom theme utility classes with opacity suffixes that were never implemented, e.g. `bg-bg/95`, `bg-bg-alt/70`, `border-bg-line/60`, `hover:bg-bg-hover/40`.
3. Check SVG/canvas/chart code for hardcoded stroke/fill colors that ignore CSS variables.
4. Check header/backdrop surfaces separately from card surfaces; both often need their own theme treatment.
5. Verify the real rendered result via computed styles, not only by reading CSS variables.

## Fix pattern
- Add a compatibility layer at the global theme/CSS-variable level so older hardcoded classes map acceptably under the custom theme and light theme.
- Implement missing opacity variants for custom theme utility classes if the codebase uses `bg-*/*`, `border-*/*`, or hover alpha utilities.
- Replace hardcoded chart colors with CSS variables (`var(--accent-1)`, `var(--bg-line)`, etc.).
- Prefer global/theme-layer fixes first; do not hand-patch every page if the root issue is the theme engine.

## Verification standard
- Verify the selected theme is actually active (`data-theme` on `<html>`).
- Inspect computed styles for body, header, card surface, border, text, and at least one input on the live page.
- Spot-check one page using the shared theme utilities and one page known to contain old `slate/zinc` classes.
- For reference-site matching tasks, compare against the real site mode being targeted before styling. Do not infer the palette from memory.

## Pitfalls
- Implementing a new palette without checking the real reference mode (light vs dark).
- Changing only CSS variables while many components still use hardcoded palette classes.
- Assuming custom utility classes with opacity suffixes exist because the base class exists.
- Trusting screenshots or snapshots alone; confirm with computed styles on the live page.
