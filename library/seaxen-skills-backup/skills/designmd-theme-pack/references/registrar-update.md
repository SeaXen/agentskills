# Registrar Update — Reference

The exact shape of `theme.js` and `README.md` updates for new Designmd themes. Used by the `designmd-theme-pack` skill.

## theme.js pattern

The `THEMES` object maps a theme key to `{name, css}`. Keys use camelCase. CSS paths are absolute, starting `/static/themes/`. New entries go at the **end** of the object (no reordering).

```js
const THEMES = {
  default: { name: 'Amber Dark', css: '/static/themes/amber-dark/default.css' },
  // ... existing themes ...
  brittanychiang: { name: 'Brittany Chiang', css: '/static/themes/brittanychiang/brittanychiang.css' },
  cursor: { name: 'Cursor', css: '/static/themes/cursor/cursor.css' },
};
```

## README.md pattern

Each theme gets a numbered section with 5 lines: Mood / Palette / Type / Style / Source, plus a Files bullet. Numbering increments. The theme id is also added to a bottom bullet list.

```markdown
### 41. cursor
- Mood: warm-paper marketing site for the AI code editor
- Palette: `#f7f7f4` bg (warm paper), `#26251e` fg, orange-tinted glow under code frame
- Type: GT Sectra serif display + Inter body + JetBrains Mono code
- Style: BEM (`.btn--ghost`, `.btn--sm`), solid black CTA, no brand color
- Source: https://cursor.com (extracted 2026-09-07)
- Files:
  - `cursor/cursor.css`
  - `cursor/cursor.md`
  - `cursor/cursor-prompt.md`
  - `cursor/cursor.html`
```

And the bottom bullet list (sorted alphabetically by id):

```markdown
- `cursor`
- `linear`
- `vercel`
- `mercury`
```

## Updating both in one turn

The two writes must happen in the same turn. Concretely:

1. Edit `theme.js` with `patch`, replacing the closing `};` of the `THEMES` object.
2. Edit `README.md` with `patch`:
   - Append a new `### <N>. <name>` section before the "Shared runtime switcher" line
   - Append the new id to the bottom bullet list (keep alphabetical)

Both `patch` calls should use small `old_string` values (a few lines each) to stay under the 8K-token-per-call limit.

## Common mistakes

- **Forgetting the bullet list update.** A theme that's in `theme.js` and the folder but not the README's bullet list is hard to find for future sessions.
- **Reordering existing entries.** Don't sort `THEMES` alphabetically. New entries go at the end. The existing order is the historical order of when each theme was added.
- **Wrong path in `theme.js`.** The path is `/static/themes/<name>/<name>.css`, not `themes/<name>/<name>.css`. The `/static/` prefix is required because the design store is served as static assets.
- **Inconsistent section number.** Each `### N.` must match the order in the README. If the last existing theme is `### 40.`, the new one is `### 41.`.

## What NOT to do

- **Don't move a theme to a different id.** If you need to rename, leave the old one and add a new one. Renaming breaks any saved bookmarks / theme selections the user has.
- **Don't add themes that don't exist on disk.** A registry-only theme is a 404 when selected.
- **Don't remove themes without explicit user request.** Even "obsolete" ones are part of the design history.
