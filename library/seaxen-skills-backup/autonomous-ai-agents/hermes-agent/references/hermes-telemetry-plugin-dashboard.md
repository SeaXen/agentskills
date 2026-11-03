# hermes-telemetry Plugin Dashboard Setup

**Plugin:** `nujovich/hermes-telemetry` — budget enforcement + observability for Hermes Agent
**Dashboard:** `serve.py` in plugin's `dashboard/` directory (stdlib-only HTML server)

## Key Properties
- **Port:** Default 8765, configurable via `--port N` or positional `serve.py N`
- **Host:** Default `127.0.0.1` (loopback only). Use `--host 0.0.0.0` for LAN access (warning: no auth)
- **DB Dependency:** Requires `/root/.hermes/telemetry/telemetry.db` — created after gateway restart + first session/cron run
- **Auto-refresh:** 30 seconds (client-side)

## Systemd Service Template (LAN + Auto-start)

```ini
[Unit]
Description=Hermes Telemetry Dashboard
After=network.target

[Service]
Type=simple
User=root
WorkingDirectory=/root/.hermes/plugins/hermes-telemetry/dashboard
# Wait for telemetry DB to exist (created after gateway restart + first session)
ExecStartPre=/bin/bash -c 'while [ ! -f /root/.hermes/telemetry/telemetry.db ]; do sleep 2; done'
ExecStart=/usr/bin/python3 serve.py --host 0.0.0.0 --port 8009
Restart=on-failure
RestartSec=10
StandardOutput=journal
StandardError=journal

[Install]
WantedBy=multi-user.target
```

**Install:**
```bash
sudo tee /etc/systemd/system/hermes-telemetry-dashboard.service > /dev/null << 'EOF'
[Unit]
Description=Hermes Telemetry Dashboard
After=network.target

[Service]
Type=simple
User=root
WorkingDirectory=/root/.hermes/plugins/hermes-telemetry/dashboard
ExecStartPre=/bin/bash -c 'while [ ! -f /root/.hermes/telemetry/telemetry.db ]; do sleep 2; done'
ExecStart=/usr/bin/python3 serve.py --host 0.0.0.0 --port 8009
Restart=on-failure
RestartSec=10
StandardOutput=journal
StandardError=journal

[Install]
WantedBy=multi-user.target
EOF

sudo systemctl daemon-reload
sudo systemctl enable --now hermes-telemetry-dashboard
```

## Prerequisite Sequence (Critical)
The dashboard service will **wait indefinitely** in `ExecStartPre` until the DB exists. You must:

1. **Install & enable plugin:**
   ```bash
   hermes plugins install nujovich/hermes-telemetry
   hermes plugins enable hermes-telemetry
   ```

2. **Restart gateway FROM OUTSIDE the gateway process:**
   ```bash
   hermes gateway restart
   ```
   > ⚠️ Running `hermes gateway restart` from inside a gateway session (e.g., Telegram/Discord chat) is blocked to prevent restart loops. Run from a shell terminal.

3. **Run at least one Hermes session or cron job** to generate initial telemetry data and create the DB.

4. Dashboard service will auto-start once DB appears.

## Verification
```bash
# Check service status
sudo systemctl status hermes-telemetry-dashboard

# Follow logs
sudo journalctl -u hermes-telemetry-dashboard -f

# Verify listener
ss -ltnp | grep 8009
# Expect: 0.0.0.0:8009  (LAN) or 127.0.0.1:8009  (loopback only)

# Test HTTP
curl -s http://localhost:8009/ | head -5
curl -s http://<server-ip>:8009/api/summary
```

## LAN Access Security Note
The dashboard has **no authentication**. Binding to `0.0.0.0` exposes all captured tokens, costs, and tool-call details to any host on the network. Only use on trusted LAN. For untrusted networks, prefer SSH tunneling:
```bash
ssh -L 8009:localhost:8009 user@server &
# Browse http://localhost:8009 on client
```

## Troubleshooting

| Symptom | Cause | Fix |
|---------|-------|-----|
| Service stuck in `activating (start-pre)` | DB doesn't exist yet | Run gateway restart + a session |
| `ERROR: telemetry DB not found` | Plugin not capturing data | Verify plugin enabled + gateway restarted |
| Port 8009 not binding | Another process on port | `sudo lsof -i :8009` and kill/change |
| LAN URL unreachable | Firewall / wrong bind | Check `ss -ltnp` shows `0.0.0.0:8009`, open host firewall |

## Related
- Main skill: `hermes-agent` (Dashboard section)
- Plugin install: `hermes plugins install nujovich/hermes-telemetry`
- Plugin docs: https://github.com/nujovich/hermes-telemetry