# Obsidian vault dashboard (:6065) — dual theme + link fixes

Cross-skill pointer for `obsidian_dashboard.py` polish.

- **Themes:** Classic + Premium, header `<select id="themeSelect">`, `localStorage` `obsmemory.dashboard.theme.v1`. CSS-only via `html[data-theme]`. Full spec: `obsidian-memory-vault` → `references/dashboard-dual-theme-2026-06.md`.
- **Dead home links:** `openNoteByPath(JSON.stringify(path))` + wait for `openNote()` — `obsidian-memory-vault` → `references/obsidian-dashboard-note-links.md`.
- **Honest done bar:** live curl + click QA; do not claim 10/10 on cosmetics alone.