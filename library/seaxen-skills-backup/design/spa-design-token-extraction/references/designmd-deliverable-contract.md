# Designmd theme deliverable contract

Exact shape that every theme in `/mnt/tb/#Sea/Designmd/<theme>/` must match. The store's `theme.js` switcher + `README.md` index expect this 5-file layout; missing any one of them breaks discoverability.

## File roles

| File | Purpose | Required content |
|---|---|---|
| `<theme>.css` | Reusable theme CSS | Every rule scoped under `html[data-theme="<theme>"]`. Token vars (`--bg`, `--text`, `--primary`, etc.) at the `:root`-level selector. Optional dark variant under `html.dark[data-theme="<theme>"]` or similar. |
| `<theme>.html` | Visual reference / mockup | Self-contained `<!doctype html>` that loads only `./<theme>.css`. Demonstrates each component pattern (nav, hero, stat cards, table, pills, etc.). |
| `<theme>.md` | Design spec | Token table with `--var: value` rows. Source URL. Visual cues captured. Reuse instructions. Honest note that this is reference, not pixel-perfect clone. |
| `<theme>-prompt.md` | App/product prompt rules | Free-form design guidance for future UIs in this style. Distinct from `<theme>.md` — one is the spec, the other is the prompt. |
| `preview.png` | Rendered screenshot | Full-page render of `<theme>.html`. Verified via `vision_analyze` that every expected section is visible top-to-bottom. |

## CSS conventions

- **Selector**: `html[data-theme="<theme>"]` — never bare `:root` so multiple themes can co-exist.
- **Token names**: kebab-case, semantic (`--bg`, `--muted`, `--accent`, `--radius`), not raw color names.
- **Dark variant**: a second block on the same selector with `.dark` class or a media query. Same token names, different values. Don't introduce `--bg-dark` — keep the names stable across modes.
- **No shadows**: the Designmd store favors borders + soft radii over drop-shadows. Exceptions: subtle inner highlights on primary buttons (`box-shadow: 0 1px 0 rgba(0,0,0,0.12) inset`).
- **Tabular numerics**: any theme with stat cards or data tables should set `font-variant-numeric: tabular-nums` on numeric values.
- **Fonts**: prefer Google Fonts `@import` at the top of the CSS file. Always include a system fallback stack.

## Mockup HTML conventions

- Single page, no JS needed (the CSS does the work).
- Use semantic HTML (`<header>`, `<main>`, `<section>`, `<table>`) so the structure is also a reference for content shape.
- Include 4–6 distinct component patterns so the theme is fully exercised in the render.
- Self-referential link in the footer: "extracted from <source-url>".

## theme.js registration

Append to the `THEMES` map near the top of `/mnt/tb/#Sea/Designmd/theme.js`:

```js
const THEMES = {
  default: { name: 'Amber Dark', css: '/static/themes/amber-dark/default.css' },
  // ...existing themes...
  yourtheme: { name: 'Your Theme', css: '/static/themes/yourtheme/yourtheme.css' },
};
```

The map is iterated by `buildDropdown()` so order = display order. Insert in the chronological slot (latest additions at the bottom).

## README.md entry

Add under the numbered list with the existing format:

```markdown
### N. yourtheme
- Mood: <one-line description of the vibe>
- Palette: <top 2-3 colors with hex>
- Style: <2-3 distinguishing patterns>
- Dark mode: <"yes via html.dark + ThemeManager.setYourthemeDark(true)" or "light-only on purpose" or "dark-only">
- Source: <origin URL>
- Files:
  - `yourtheme/yourtheme.css`
  - `yourtheme/yourtheme.md`
  - `yourtheme/yourtheme-prompt.md`
  - `yourtheme/yourtheme.html`
  - `yourtheme/preview.png`
```

Also append `'yourtheme'` to the "Available theme IDs" list near the bottom of README.md.

## preview.png capture

Use the `fullpage-preview-capture` skill — puppeteer with `fullPage: true` against the local HTML file. Critical bits:

- `executablePath: '/usr/bin/chromium'` (system chromium, not puppeteer's bundled one)
- `waitUntil: 'networkidle0'` then `await document.fonts.ready` + 800ms buffer
- For `#` in path (`/mnt/tb/#Sea/...`), use `file:///mnt/tb/%23Sea/...`
- Always verify with `vision_analyze` listing every expected section top-to-bottom — a green "looks fine" is not enough; name each section

## Anti-patterns (don't)

- ❌ Bare `:root` selector — themes must be scoped to `html[data-theme="..."]`.
- ❌ Pixel-perfect clone with copyrighted imagery or exact copy — store is for portable skins, not redistributable assets.
- ❌ Skipping theme.js registration — the theme is invisible to the dropdown until registered.
- ❌ Skipping README.md entry — the index page breaks discoverability.
- ❌ Hardcoded light + dark as separate CSS files — use one file with mode variants on the same selector.
- ❌ Inline `<style>` blocks in `<theme>.html` — keep all styles in `<theme>.css`.
- ❌ Shadows + glass everywhere — Designmd themes use borders + soft radii as the primary depth signal.
- ❌ Capturing preview.png via chromium `--window-size` — clips tall pages. Use puppeteer `fullPage: true`.

## Reference

- `fullpage-preview-capture` skill — reliable full-page PNG rendering recipe.
- `spa-design-token-extraction` SKILL.md — token resolution (precedes this contract).
