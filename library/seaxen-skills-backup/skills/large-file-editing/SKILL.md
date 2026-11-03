---
name: large-file-editing
description: Strategies for safely editing, refactoring, and adding features to very large or monolithic source files (especially single-file apps, giant inline scripts, or files >500 lines with embedded strings/templates).
---

# Large File Editing

When working with very large files (especially those containing giant string literals, embedded scripts, or repeated similar blocks), direct `patch` operations become extremely fragile due to escaping issues, multiple matches, and context drift.

## Core Principles
- **Read first, patch second** — Always read sufficient unique context before attempting a replace.
- **Prefer unique anchors** — Use surrounding distinctive lines or multi-line context rather than short repeated strings.
- **Avoid string drift** — Never escape quotes in `old_string`/`new_string` when the file uses normal quotes.
- **Consider alternatives to patching**:
  - Extract logic into separate modules when possible.
  - Use `write_file` for complete rewrites of sections when patches repeatedly fail.
  - Add new features via new files/components instead of injecting into the monolith.

## When Patching Fails Repeatedly
1. Stop after 2-3 failed attempts.
2. Switch strategy: use more context, switch to `replace_all` only if safe, or move to a different approach (new component, script injection, etc.).
3. Document the failure pattern in `references/` for the specific file.

## User Preferences Observed
- Strongly prefers compact, working results over verbose explanations.
- Wants live verification ("check in website") after changes.
- Gets frustrated with repeated failed patches on the same file.

## Recommended Workflow
1. Explore structure with `search_files` + targeted `read_file`.
2. Make small, high-confidence changes first.
3. Verify live (dev server + browser tools) before adding more features.
4. If the file is a giant inline-script Next.js page, consider whether a partial refactor (new components) is better than continued patching.

## Atomic CSS block swap for single-file dashboards

When the file is a giant single-page app (SeaDash `:9090`, Next.js `page.tsx` with 1000+ lines of inline CSS, etc.) and the user wants a **complete CSS refresh** without touching the body or JS:

1. **Do not patch a 500+ line CSS block via `patch`.** The `old_string` is too long, fuzzy matchers drift, and any inline JS inside the CSS gets re-escaped. After 2-3 failures, switch strategy.
2. **Read the whole CSS block once** to confirm it lives between two well-defined markers (typically `<style>` and `</style>`, or a single string literal in a Python/JS file).
3. **Back up the file with a timestamped suffix** so the rollback is one `cp` away.
4. **Use a Python script with `re.subn` and a callable replacement**:

   ```python
   import re, pathlib
   src = pathlib.Path('index.html')
   html = src.read_text(encoding='utf-8')
   new_css = pathlib.Path('/tmp/retro.css').read_text(encoding='utf-8')

   new_html, n = re.subn(
       r'<style>.*?</style>',
       lambda m: '<style>\n' + new_css + '\n</style>',
       html,
       count=1,
       flags=re.DOTALL
   )
   assert n == 1, "style block not found"
   src.write_text(new_html, encoding='utf-8')
   ```

5. **Critical pitfall: never use a string template for the replacement.** If the new CSS contains any backslash sequence (`\25A0`, `\1F`, `\A0`, etc. inside `content: '...'`), Python `re.sub` treats it as a backreference and raises `re.error: bad escape \A at position N`. A callable replacement (`lambda m: '...'`) skips template parsing and accepts any string.
6. **Use `count=1` and `re.DOTALL`** so the regex matches the first `<style>...</style>` block including newlines and only the first one.
7. **Inject additional scripts (e.g. boot overlays, typewriter, animations) just before `</body>`** with a plain `.replace('</body>', injection + '\n</body>', 1)`. The boot script runs in parallel with the page's own `loadAll()` and should be self-contained.

For the SeaDash retro CRT retrofit pattern specifically (CSS color tokens, scanline/vignette/flicker stack, ASCII decorations, bracketed-button universal selectors, boot sequence script, six-theme-as-phosphor-colors), see `devops/dashboard-ui-operations/references/seadash-retro-crt-theme.md`. The general pattern above applies to any giant single-file app with an embedded `<style>` block that needs a clean replacement.

## Appended overlay style block for surgical polish (safer default)

When the user asks for **visual polish on a single-file dashboard that already has a large embedded CSS block (150+ class selectors)**, do **not** use the atomic-swap recipe above by default. Atomic replacement of an 800+ line CSS block on a working dashboard will silently delete 100+ specialized class definitions and may break modal architecture (e.g. conflating `.modal` and `.modal-overlay`).

**The safer default for polish passes is to append a second `<style>` block before `</head>`** and only override specific visual properties. The original block stays intact; later rules win on equal specificity.

Recipe:

```python
import pathlib
src = pathlib.Path('/mnt/tb/1Apps/SeaDash/index.html')
html = src.read_text(encoding='utf-8')
refined = pathlib.Path('/tmp/seadash-refined.css').read_text(encoding='utf-8')

inject = '\n<style id="refined">\n' + refined + '\n</style>\n'
new_html = html.replace('</head>', inject + '</head>', 1)
assert new_html != html, "injection failed"
src.write_text(new_html, encoding='utf-8')
```

What this preserves that atomic-swap risks losing:
- every original class definition (`.card-stat`, `.card-action-btn`, `.layout-toolbar`, `.sysinfo-grid`, `.section-icon`, `.settings-group`, `.quick-actions`, `.theme-picker`, `.toast`, `.stats-bar`, `.docker-action-btn`, `.modal`, `.modal-overlay`, `.auth-overlay`, `.auth-box`, etc.)
- every JS binding (`saveLayoutColumn()`, `closeModal(id)`, `toggleLayoutAutoRule(...)`, `applyLayoutPreset()`)
- the modal-architecture distinction (backdrop is `.modal-overlay`, inner panel is `.modal`; visibility toggled by `.modal-overlay.active`)
- the auth overlay (`.auth-overlay { display: none }` is a common omission when overriding only the design tokens)

**When to use atomic-swap vs append-overlay:**
- Use **atomic-swap** when the user explicitly asks for a complete visual redo (e.g. "make SeaDash retro CRT", "remove the old design entirely") AND you are replacing every class definition in one cohesive system.
- Use **append-overlay** when the user asks for polish, refinement, or modernization while the existing structure must remain (the default for "make it look better", "cleaner", "more modern", "prettier").

End-to-end verification after an append-overlay edit (mandatory, not optional):
1. `curl` returns 200 and the new style block is in the served HTML
2. All modal IDs still have `closeModal` handlers in the live DOM
3. Save and Close buttons still fire their `onclick` handlers on real `.click()` events
4. All 30+ critical functions (`typeof window[fn] === 'function'`) are still defined
5. Programmatic `openSettings()` / `openSysInfo()` / `openSystemActions()` / `openLogsModal()` each open the modal, then `closeModal(id)` removes the `active` class
6. The `.auth-overlay` rule is present so the login form does not cover the dashboard

For the concrete SeaDash append-overlay case (worked example with the refined CSS, modal-architecture preservation rule, `.auth-overlay` recovery, and full verification script), see `devops/dashboard-ui-operations/references/seadash-refined-css-overlay.md`.

**Critical pitfall: do not use `[class*="modal"]` selectors** in any overlay CSS. This selector matches both `.modal-overlay` (backdrop) and `.modal` (panel) and they have different display semantics. Apply visuals to `.modal-overlay` and `.modal` separately.

## Related Patterns
- Giant inline `<script>` in Next.js App Router pages
- Repeated JSX/HTML strings inside JS template literals
- Legacy single-file dashboards/tools

