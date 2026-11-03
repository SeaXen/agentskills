# Dashboard dual theme: Classic + Premium (2026-06)

**File:** `/mnt/tb/hermes/obsidian_dashboard.py`  
**Port:** `6065`  
**Persistence:** `localStorage` key `obsmemory.dashboard.theme.v1` (`classic` | `premium`)

## User expectation (Dr. Sagar)

- Keep **both** themes; **header select** switches appearance.
- **Classic** = existing `:root` GitHub-dark telemetry UI (unchanged behavior).
- **Premium** = full visual pass on **same** pages/APIs — not a separate app.

## Implementation contract

1. Early `<head>` inline script sets `document.documentElement.setAttribute('data-theme', …)` before paint.
2. Header: `<select id="themeSelect">` → `setDashboardTheme(value)`.
3. Premium overrides via `html[data-theme="premium"] { --vars… }` + component rules (header blur, stat/panel shadow, `premiumPageIn` animation, reader `max-width: 72ch`, DM Sans + JetBrains Mono via Google Fonts).
4. **Do not** fork JS logic per theme — CSS only unless user asks for premium-only layout hiding panels.

## Verify (ad-hoc)

```bash
curl -sS http://127.0.0.1:6065/ | grep -E 'themeSelect|setDashboardTheme|premiumPageIn'
python3 -m py_compile /mnt/tb/hermes/obsidian_dashboard.py
```

Restart: `systemctl --user restart obsidian-vault-dashboard` (outside gateway if blocked); fallback `pkill -f obsidian_dashboard.py` + `Restart=always`.

## Related

- Home links / Learn tab: `references/obsidian-dashboard-note-links.md`, `references/dashboard-learn-bridge-tab-2026-06.md`
- Visual direction history: `references/dashboard-premium-redesign-pass.md`