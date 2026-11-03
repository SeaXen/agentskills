# Hermes Personal Dashboard — Install Log & Patterns

## Install Commands (June 10, 2026)

```bash
# Initial install on port 9122
cd /tmp && git clone https://github.com/manimohans/hermes-personal-dashboard.git
cd hermes-personal-dashboard
./install.sh --port 9122 --no-open

# Restart for LAN access (0.0.0.0)
kill $(cat "/root/.hermes/run/hermes-personal-dashboard.pid")
/root/.hermes/products/hermes-personal-dashboard/run.sh --host 0.0.0.0 --port 9122 --insecure --no-open

# Systemd service (required --foreground)
sudo tee /etc/systemd/system/hermes-personal-dashboard.service > /dev/null <<'EOF'
[Unit]
Description=Hermes Personal Dashboard
After=network.target

[Service]
Type=simple
User=root
WorkingDirectory=/root/.hermes/products/hermes-personal-dashboard
ExecStart=/root/.hermes/products/hermes-personal-dashboard/run.sh --lan --port 9122 --foreground
Restart=on-failure
RestartSec=5

[Install]
WantedBy=multi-user.target
EOF

sudo systemctl daemon-reload
sudo systemctl enable --now hermes-personal-dashboard
```

## Verification Results

| Check | Result |
|-------|--------|
| Port | 9122 (0.0.0.0) |
| HTML served | ✓ |
| Health endpoint | ✓ |
| Plugin enabled | ✓ (`personal_dashboard`) |
| Skills available | ✓ (`briefing-curator`) |
| Systemd auto-restart | ✓ |

## Cron Jobs Created

```bash
# Daily briefing (07:30)
cronjob create --name "Personal Dashboard Daily Briefing" \
  --schedule "30 7 * * *" \
  --skill briefing-curator \
  --prompt "Use hermes-personal-dashboard:briefing-curator. Refresh..."

# Hourly signal refresh
cronjob create --name "Personal Dashboard Frequent Signal Refresh" \
  --schedule "0 * * * *" \
  --skill briefing-curator \
  --prompt "Use hermes-personal-dashboard:briefing-curator. Refresh time-sensitive..."

# Weekly planning (Fri 15:00)
cronjob create --name "Personal Dashboard Planning Refresh" \
  --schedule "0 15 * * 5" \
  --skill briefing-curator \
  --prompt "Use hermes-personal-dashboard:briefing-curator. Refresh planning..."
```

**Key learning**: Skill name is `briefing-curator` (from `plugin.yaml`), NOT `hermes-personal-dashboard`.

## Dashboard State Before Curation

```json
{
  "status": { "card_count": 0 },
  "curation": {
    "state": "needs_ai_curation",
    "curated_card_count": 0,
    "context_count": 42
  },
  "preferences": { "cron_unavailable": "No module named 'cron'" }
}
```

42 context signals detected from Hermes memory/sessions/cron, but 0 cards until AI curation runs.

## Curation Trigger

```bash
# Via Hermes chat (Discord):
Use hermes-personal-dashboard:briefing-curator. Refresh the Personal Dashboard now from existing Hermes memory, sessions, cron output, and prior work. Write useful cards and record the refresh result.
```

## File Locations

| Path | Purpose |
|------|---------|
| `/root/.hermes/products/hermes-personal-dashboard/` | Product install |
| `/root/.hermes/plugins/hermes-personal-dashboard/` | Plugin symlink |
| `/root/.hermes/plugins/hermes-personal-dashboard/cards.db` | Card database |
| `/root/.hermes/run/hermes-personal-dashboard.log` | Server log |
| `/root/.hermes/run/hermes-personal-dashboard.pid` | PID file |
| `/root/.hermes/products/hermes-personal-dashboard/skills/briefing-curator/SKILL.md` | Curation skill |