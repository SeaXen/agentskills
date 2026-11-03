# Desktop-first dashboard + PWA pattern

Use this when building a dashboard app that should feel premium on desktop, then compress well into a mobile PWA.

## Visual target
- Desktop-first grid with a large hero panel.
- Big date / day indicator, followed by glossy metric cards.
- Dark background, neon accent colors, thin borders, soft glow.
- Compact chips for modes/tabs at the top of the hero.
- Right-side session/control panel and lower insight panels.
- Metric cards should feel like finished product UI, not placeholder blocks.

## Layout rules
- Prefer 2-column or 3-column desktop grids; mobile can collapse to stacked cards.
- Keep actions and status visible without scrolling on desktop.
- Use dense but readable cards; avoid wasted whitespace.
- Keep controls and input rows inline when possible.

## PWA posture
- Treat the mobile view as a responsive fit of the desktop app, not a separate product.
- Ensure the manifest exists, theme color is set, and the UI remains usable at narrow widths.
- Do not introduce APK-specific scaffolding unless the user explicitly wants it.

## Verification
- Run a build.
- Open the home page in a browser and inspect the rendered layout visually.
- Check that every route responds 200.
- Confirm the desktop layout still reads clearly at mobile width.

## Related
This pairs with the main `SKILL.md` sections on standalone Docker, Vercel, and build verification.