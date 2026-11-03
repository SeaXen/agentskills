---
name: hermes-standalone-products
description: Install, configure, and operate Hermes standalone web products (personal dashboard, ecosystem dashboard, etc.) as persistent systemd services on dedicated ports.
version: 1.0.0
author: Hermes Agent
license: MIT
metadata:
  hermes:
    tags: [hermes, standalone, dashboard, systemd, installation, systemd, ops]
---

# Hermes Standalone Products

Hermes "products" are standalone web applications (React + Python API) that run on their own ports, separate from the main Hermes dashboard (gateway). They read Hermes state (memory, sessions, cron, plugins) but are not plugin tabs.

## Common Products

| Product | Repo | Default Port | Purpose |
|---------|------|--------------|---------|
| hermes-personal-dashboard | manimohans/hermes-personal-dashboard | 9120 | Zero-setup personal briefing from Hermes context |
| hermes-ecosystem-dashboard | (various) | 9120 | Community add-on inventory, ratings |

## Installation Pattern

```bash
# 1. Clone & install (auto-installs plugin link + enables plugin)
git clone <repo> && cd <repo>
./install.sh --port <PORT> --no-open

# 2. Verify it serves on the port
curl -s http://127.0.0.1:<PORT>/ | head -5

# 3. For LAN access, restart with --lan (binds 0.0.0.0)
./run.sh --lan --port <PORT>
```

## Systemd Service (Auto-restart on Reboot)

**Critical**: The `run.sh` script daemonizes by default. For systemd, **must use `--foreground`** or the service exits immediately.

```ini
# /etc/systemd/system/hermes-<product>.service
[Unit]
Description=Hermes <Product Name>
After=network.target

[Service]
Type=simple
User=root
WorkingDirectory=/root/.hermes/products/<product>
ExecStart=/root/.hermes/products/<product>/run.sh --lan --port <PORT> --foreground
Restart=on-failure
RestartSec=5

[Install]
WantedBy=multi-user.target
```

```bash
sudo systemctl daemon-reload
sudo systemctl enable --now hermes-<product>
```

## Port Management

- Default port in `run.sh` is **9120** (same as main Hermes dashboard)
- If port busy, script **auto-increments** (9121, 9122...)
- **Always specify `--port <PORT>` explicitly** to avoid surprises
- Check actual port: `ss -tlnp | grep :<PORT>`

## Plugin Link Auto-creation

`install.sh` and `run.sh` create a symlink at:
```
/root/.hermes/plugins/<product> -> /root/.hermes/products/<product>
```
and run `hermes plugins enable <product>`. This makes the product's tools/skills available to Hermes chat/cron.

## Cron Job Integration

Products that provide skills (e.g., `briefing-curator`) can be scheduled via Hermes cron:

```bash
# Skill name comes from plugin.yaml `skills:` list, NOT the plugin name
hermes cron create --name "Daily Briefing" \
  --schedule "30 7 * * *" \
  --skill briefing-curator \
  --prompt "Use hermes-personal-dashboard:briefing-curator. Refresh now..."
```

**Pitfall**: The skill name in `plugin.yaml` (`skills: [briefing-curator]`) != plugin name (`hermes-personal-dashboard`). Use the skill name for cron.

## Dashboard API Snapshot

Most products expose `/api/plugins/<product>/snapshot` for status:
```bash
curl -s http://127.0.0.1:<PORT>/api/plugins/<product>/snapshot | jq '.status, .curation'
```
Key fields:
- `status.card_count` — visible cards
- `curation.curated_card_count` — AI-curated cards
- `curation.state` — `needs_ai_curation` / `has_cards`
- `preferences.cron_unavailable` — if Hermes cron module missing

## Common Issues

| Symptom | Cause | Fix |
|---------|-------|-----|
| Service starts then dies | `run.sh` daemonizes, systemd sees exit | Add `--foreground` to `ExecStart` |
| Wrong port (9121 not 9122) | Default 9120 busy, auto-incremented | Specify `--port <PORT>` explicitly |
| "cards: []" but context signals exist | AI curation hasn't run | Trigger `briefing-curator` skill via cron or chat |
| `cron_unavailable: "No module named 'cron'"` | Hermes Gateway cron module not loaded | Ensure Gateway is running; cron ticker active |
| No systemd logs | Journal rotated | `journalctl -u hermes-<product> -f` |

## Verification Checklist

After install + systemd enable:
- [ ] `systemctl status hermes-<product>` shows `active (running)`
- [ ] `ss -tlnp | grep :<PORT>` shows listening on correct port
- [ ] `curl http://127.0.0.1:<PORT>/` returns HTML
- [ ] `curl http://127.0.0.1:<PORT>/api/plugins/<product>/health` returns `{"ok":true}`
- [ ] `hermes tools list` shows plugin enabled
- [ ] Cron jobs created with correct skill name fire on schedule

## References

- `references/hermes-personal-dashboard.md` — Full install log, systemd fix, cron job patterns
- `references/port-conflict-behavior.md` — Auto-increment logic from run.sh
- `references/hermes-personal-dashboard-removal.md` — Complete removal procedure (systemd, product dir, cron jobs, scripts, session output)
