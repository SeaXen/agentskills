# Vue CLI token extraction — condensed recipe

## Symptom
`curl` the page + CSS bundles, `rg ':root'` shows only semantic aliases:
```
:root{--color-bg:var(--v-background-base);--color-primary:var(--v-primary-base);...}
```
`rg -o '\-\-v-[a-z-]+:[^;}]*'` finds nothing in the CSS — values are JS-injected.

## Steps
1. `browser_navigate <url>`
2. `browser_console` → dump computed custom props (see SKILL.md fix block).
3. Build token table from resolved `--v-*` values.
4. `browser_console` → dark-only probe (className, `.dark` class, `--v-background-base`).
5. Write `<id>.css` / `<id>.md` / `<id>.html`; register in theme manager + README.

## Worked example (toolesthub.com, 2026-07)
- `--v-background-base`: `#121212` (dark-only; no `.dark` class)
- `--v-surface-base`: `#1c1c1b`
- `--v-surface-lighten1`: `#272727` (elevated surface)
- `--v-primary-base`: `#ff7448` (coral CTA, pill radius 999px)
- `--v-secondary-base`: `#48e4ff` (cyan accent)
- `--v-text-base`: `#f3f0e8` (warm off-white)
- `--font-body`: `Inter, Arial, sans-serif`
- `--font-display`: `"Google Sans Flex", Inter` (fallback to Inter — not freely hostable)

## Gotchas
- `--color-muted` etc. are `color-mix(in srgb, --v-text-base 46%, transparent)` — keep as mix, don't flatten to a hex.
- Derived tokens (e.g. inset `--surface-2` from `--v-surface-lighten1`) must be labeled *derived* in the spec.
