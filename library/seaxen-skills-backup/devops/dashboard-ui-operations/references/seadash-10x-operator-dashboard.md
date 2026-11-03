# SeaDash 10x operator dashboard rewrite pattern

Use when SeaDash is messy enough that the right move is a clean single-file frontend rewrite while preserving the existing Python backend and live config.

## Scope that worked

- Keep backend `server.py` as the source of truth for host/Docker/manual-app data.
- Rewrite `index.html` as dependency-free vanilla HTML/CSS/JS; avoid npm/framework overhead for this lightweight dashboard.
- Preserve real operator features instead of building fake controls:
  - host CPU/RAM/Disk/network snapshot
  - Docker auto-discovery and restart controls
  - manual app add/edit/delete
  - sections, collapse, pinning, per-section modes
  - drag/order and bulk move
  - hide/unhide and hidden recovery tab
  - tags and notes per app
  - health-only view
  - port scanner/import
  - layout-only export/import separate from full config
- Use a small PWA/logo asset set: `assets/logo-192.png`, `assets/logo-512.png`, `favicon.ico`, `assets/social-card.png`, manifest icons.

## Backend additions that fit this class

Add small stdlib helpers rather than introducing dependencies:

- `/api/scan/ports`: gather listening ports from `ss -ltn`, probe common/local ports with existing URL probe helper, return import candidates.
- `/api/docker/bulk-action`: accept selected container names and action; for safe default, restart/start only bad containers and skip healthy running containers.

Do not expose secrets or commit the live `seadash-config.json`. Commit `seadash-config.example.json` instead.

## Frontend implementation rules

- Store layout-only state under config keys such as:
  - `app_order`
  - `app_sections`
  - `custom_sections`
  - `collapsed_sections`
  - `pinned_sections`
  - `section_modes`
  - `hidden_apps`
  - `app_tags`
  - `app_notes`
- Layout-only export/import must include only those keys, not routes, cloud credentials, tokens, or full config.
- Auto-section rules should be practical and name/image/tag based:
  - `jellyfin|plex|emby|metube|youtube|media` -> Media
  - `open-webui|ollama|llm|gemini|ai|stable|comfy` -> AI
  - `qbittorrent|torrent|gopeed|aria|download` -> Download
- Keep card and table parity: Open/Edit/Move/Hide/Select should work in both.
- Use a Health tab for bad local/public probes, stopped/unhealthy containers, and high-risk items.

## Logo handling

For a wide supplied logo image, crop the central saturated/dark content area, generate square PNGs, then wire:

- header logo
- hero logo
- favicon
- apple-touch-icon
- PWA manifest
- social preview card

Small favicon crops need the main whale/penguin/dashboard mark, not the full pale background.

## Verification checklist

Command-line:

- `python3 -m py_compile server.py`
- parse `index.html` with Python `HTMLParser`
- `GET /api/health`
- `GET /api/scan/ports` returns `{ok:true,count:N}`

Browser:

- app count renders after hydration
- expected section names render
- Health tab count/cards render
- Sections modal opens and lists rows
- Scanner tab runs and populates results
- table toggle renders rows
- logo and favicon links load
- browser console has zero JS errors
- visual pass confirms compact dark dashboard with no blank/white page or obvious overlap

Git/private repo hygiene:

- initialize repo only after `.gitignore` excludes `seadash-config.json`, backups, env, and pycache
- add `seadash-config.example.json`
- run a simple tracked-file secret scan before commit
- create private GitHub repo with `gh repo create <owner>/SeaDash --private --source=. --remote=origin --push`
- verify `gh repo view ... --json isPrivate,url,defaultBranchRef` and clean `git status`
