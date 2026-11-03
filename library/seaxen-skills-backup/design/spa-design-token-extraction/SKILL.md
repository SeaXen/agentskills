---
name: spa-design-token-extraction
description: Extract JS-injected SPA tokens via browser computed styles.
---

# SPA Design Token Extraction

References:
- `references/vue-cli-token-extraction.md` — extended Vue CLI walkthrough
- `references/designmd-deliverable-contract.md` — the 5-file bundle shape every Designmd theme folder must satisfy (CSS + HTML + MD + prompt MD + preview.png) plus theme.js + README registration
- `references/wayback-fallback-for-gated-sites.md` — Wayback Machine CDX replay recipe when the live site is behind Cloudflare Turnstile / hCaptcha / bot gates

## When to Use

- "extract the theme / design tokens from this site"
- "save this site's colors/fonts to my design store"
- `curl` + `rg` on the CSS returns `--color-bg: var(--v-background-base)` with no resolved value
- A SPA (Vue CLI, Webflow, Next.js, Vite) where tokens appear undefined in the downloaded bundle
- Any task that needs the *actual* hex/RGB values, not just variable names
- The live site is behind Cloudflare Turnstile / hCaptcha / aggressive bot detection → use Wayback Machine CDX replay (see `references/wayback-fallback-for-gated-sites.md`)

## The core trap (Vue CLI / JS-injected tokens)

Many SPAs ship CSS where `:root` holds only **semantic aliases** that reference undefined `--v-*` vars:

```css
:root{
  --color-bg: var(--v-background-base);
  --color-primary: var(--v-primary-base);
}
```

The real values (`--v-background-base: #121212`) are injected by the **JS bundle at runtime**, so `curl` + `rg` on the CSS returns empty/undefined tokens. This looks like "no tokens found" — it is a false negative. **Never conclude a site has no tokens from a CSS grep alone.**

## Fix: resolve via computed styles

1. `browser_navigate` the live page (bot-detection may block `web_extract`; the browser stack usually succeeds).
2. `browser_console` evaluating `getComputedStyle(document.documentElement)` to dump every `--v-*` and `--color-*` value:

```js
(() => {
  const s = getComputedStyle(document.documentElement);
  const out = {};
  for (const n of s) {
    if (n.startsWith('--v-') || n.startsWith('--color-')) out[n] = s.getPropertyValue(n).trim();
  }
  out.fontBody = s.getPropertyValue('--font-body');
  out.fontDisplay = s.getPropertyValue('--font-display');
  out.bg = s.backgroundColor;
  out.color = s.color;
  return JSON.stringify(out, null, 2);
})()
```

3. Map the resolved values into your token table.

## Semantic → base mapping (typical)

| Semantic alias | Base var | Example |
|---|---|---|
| `--color-bg` | `--v-background-base` | `#121212` |
| `--color-surface` | `--v-surface-base` | `#1c1c1b` |
| `--color-primary` | `--v-primary-base` | `#ff7448` |
| `--color-text` | `--v-text-base` | `#f3f0e8` |
| `--color-muted` | `color-mix(in srgb, --v-text-base 46%, transparent)` | derived |

## Dark-only detection

Confirm whether the site has a light mode before inventing one:

```js
(() => {
  const r = document.documentElement;
  const s = getComputedStyle(r);
  return JSON.stringify({
    className: r.className,
    surfaceBase: s.getPropertyValue('--v-surface-base').trim(),
    hasDarkClass: r.classList.contains('dark'),
    prefersDark: matchMedia('(prefers-color-scheme: dark)').matches
  });
})()
```

If `--v-background-base` is already near-black and no `.dark` class / `prefers-color-scheme` flip exists, the site is **dark-only** — do not add a light variant.

## Honesty rules

- Label any token you derived (e.g. an inset `--surface-2` taken from `--v-surface-lighten1`) as *derived* in the spec so future readers know it was not a direct source token.
- Google Fonts display faces (e.g. "Google Sans Flex") are often not freely hostable — fall back to Inter and note the substitution.
- State provenance of any preview image: render the local mockup, don't claim a live-site grab.

## From tokens to a Designmd theme folder (end-to-end)

After you have the resolved tokens, the deliverable is a **5-file bundle** that drops into `/mnt/tb/#Sea/Designmd/<theme>/` and is auto-discoverable by the store's `theme.js` switcher. Full contract in `references/designmd-deliverable-contract.md`. Quick checklist:

1. `<theme>.css` — every rule scoped under `html[data-theme="<theme>"]`; tokens as CSS custom properties; optional `html.dark[data-theme="<theme>"]` for dark variant.
2. `<theme>.html` — self-contained mockup loading only the theme CSS; exercises 4–6 distinct component patterns.
3. `<theme>.md` — token table, source URL, visual cues, reuse instructions, honest "this is a reference, not a clone" note.
4. `<theme>-prompt.md` — free-form design guidance distinct from the spec (prompt contract).
5. `preview.png` — full-page render via the `fullpage-preview-capture` skill; verify with `vision_analyze` listing every expected section.

Then:
- Add the theme to the `THEMES` map near the top of `/mnt/tb/#Sea/Designmd/theme.js`.
- Add a numbered entry to `/mnt/tb/#Sea/Designmd/README.md` with mood, palette, style, dark mode note, source URL, and a Files bullet list.
- Append the theme ID to the "Available theme IDs" list at the bottom of README.md.

## Pitfalls

- `web_extract` alone rarely exposes CSS variables — always pull the CSS bundle AND resolve computed styles.
- **Site is behind Cloudflare Turnstile / hCaptcha** → don't waste rounds trying to click the iframe checkbox; jump straight to Wayback Machine CDX replay (`web.archive.org/web/<ts>/<url>` + puppeteer). See `references/wayback-fallback-for-gated-sites.md`.
- Stopping at the empty alias grep → you'll ship a theme with no colors. Always resolve via `browser_console`.
- Don't expand a repo's verification script's expected-set unless you also fix the README format / add markers to every theme — that turns a green check red on unrelated themes (revert instead).
- Theme folder missing any of the 5 files → store's theme.js dropdown or README index breaks for that entry. Verify all 5 exist before declaring the theme done.
- Skipping theme.js registration after writing the CSS → the theme is invisible to the dropdown until added.
- Capturing `preview.png` via `chromium --window-size` instead of puppeteer `fullPage: true` → tall pages clip; only the hero shows.
- Forgetting `#` → `%23` in the `file://` URL when reading from `/mnt/tb/#Sea/...` → blank/black PNG.
- This skill overlaps `designmd-store`'s `references/site-theme-extraction.md` (Next.js / Vite / Webflow). That skill is user-owned; once adopted via `hermes curator adopt designmd-store`, this content can be merged into it.

## Reuse triggers

"extract theme", "save design tokens", "site colors are empty in CSS", "Vue CLI tokens undefined", "getComputedStyle design tokens", "dark-only SPA theme", "add this site to my design store", "designmd theme from URL", "portable skin for my app", "codeburn theme", "extract this dashboard's look".
