# Large Single-File Web UI Pattern — SeaDash Lessons

## Context
SeaDash is a premium dashboard built as a monolithic `index.html` (1800+ lines) with all CSS and JS embedded. This is intentional for portability — no build step, no npm, just one file.

## Pitfall: write_file Truncation on Large Files

**Symptom:** `write_file` silently truncates content when writing very large files (observed at ~65KB+). The tool returns success but the file is incomplete. The last line may be cut mid-word.

**Detection:** After writing, always verify:
```bash
wc -l index.html
tail -5 index.html
```

**Recovery pattern:**
1. Read the file to find the truncation point
2. Use `patch` with `mode='replace'` to append the missing content
3. Verify the fix with `read_file` on the last 10-20 lines

**Prevention:** For files >50KB, write in sections:
1. Write the CSS/HTML structure first
2. Write the JS in chunks using `patch` to append
3. Or use `execute_code` with Python to write the file in chunks

## Monolithic HTML Architecture

**When to use:** Self-hosted dashboards, single-file tools, portable apps where the user wants `scp` deployment with zero dependencies.

**Structure pattern (SeaDash v2):**
```
index.html
├── <style>          # All CSS (variables, components, modals, animations)
├── <body>           # HTML structure (header, sections, modals)
│   ├── Header       # Logo, stats, search, view toggle, theme toggle
│   ├── Quick Actions # Button bar
│   ├── Sections     # Core/Docker/Custom/Bookmarks (grid + table views)
│   └── Modals       # All dialogs (add/edit, sysinfo, docker, logs, settings)
└── <script>         # All JS (state, render, API, modals, init)
```

**CSS organization:**
1. `:root` variables (colors, radii, shadows, transitions)
2. Theme overrides (`[data-theme="..."]`)
3. Reset & base styles
4. Layout (header, sections, grid, table)
5. Components (cards, buttons, modals, toasts, toggles)
6. Utilities (animations, drag states, responsive)

**JS organization:**
1. State constants & config
2. Helper functions (esc, url, api, post, toast)
3. Theme management
4. Settings management
5. View toggle & search
6. Render functions (card, row, bookmarks, favorites)
7. Drag & drop
8. App modal (CRUD)
9. Bookmarks
10. System info / Docker / Logs / Processes / Network
11. Backup & restore
12. Auth
13. Data fetching
14. PWA registration
15. Init

## Systemd Service Pattern for Python HTTP

```ini
[Unit]
Description=SeaDash - Premium Server Dashboard
After=network.target docker.service
Wants=docker.service

[Service]
Type=simple
WorkingDirectory=/path/to/seadash
ExecStart=/usr/bin/python3 /path/to/seadash/server.py
Restart=always
RestartSec=5
Environment=DASHBOARD_PORT=9090

[Install]
WantedBy=multi-user.target
```

**Common issues:**
- Port already in use: `sudo ss -tlnp | grep 9090` then kill old process
- Permission denied on Docker socket: `sudo usermod -aG docker $USER`
- Service fails silently: `sudo journalctl -u seadash -n 50`

## Verification Checklist After Deploy

```bash
systemctl is-active seadash
curl -s http://localhost:9090/api/health
curl -s http://localhost:9090/ | head -c 200
curl -s http://localhost:9090/api/stats | python3 -c "import json,sys; d=json.load(sys.stdin); print(f'CPU:{d.get(\"cpu_pct\",\"—\")}%')"
curl -s http://localhost:9090/api/docker | python3 -c "import json,sys; d=json.load(sys.stdin); print(f'containers={len(d[\"containers\"])}')"
wc -l /path/to/seadash/index.html
tail -3 /path/to/seadash/index.html
```
