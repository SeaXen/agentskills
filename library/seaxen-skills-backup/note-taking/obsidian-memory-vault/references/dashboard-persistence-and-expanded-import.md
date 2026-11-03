# Obsidian Dashboard Persistence + Expanded Import Notes

Use when maintaining Dr. Sagar's Hermes Obsidian memory vault dashboard or importing more past session history.

## Dashboard persistence pattern

The vault browser dashboard can be persisted as a user systemd service instead of a fragile foreground/background shell process.

Known-good service path:

```text
/root/.config/systemd/user/obsidian-vault-dashboard.service
```

Known-good unit shape:

```ini
[Unit]
Description=Obsidian vault read-only dashboard on port 6065
After=network-online.target
Wants=network-online.target

[Service]
Type=simple
Environment=OBSIDIAN_VAULT_PATH=/mnt/tb/hermes/obsedianvault
Environment=OBSIDIAN_DASHBOARD_PORT=6065
WorkingDirectory=/mnt/tb/hermes
ExecStart=/usr/bin/python3 /mnt/tb/hermes/obsidian_dashboard.py
Restart=always
RestartSec=5

[Install]
WantedBy=default.target
```

Enable/start:

```bash
systemctl --user daemon-reload
systemctl --user enable --now obsidian-vault-dashboard.service
```

Verification:

```bash
systemctl --user is-enabled obsidian-vault-dashboard.service
systemctl --user is-active obsidian-vault-dashboard.service
loginctl show-user root -p Linger
ss -ltnp | grep ':6065 '
curl -fsS http://127.0.0.1:6065/api/graph
```

Expected durable state:

```text
enabled
active
Linger=yes
0.0.0.0:6065 listening
```

## Expanded selective import pattern

After the initial import, useful additional topic clusters included:

- MCP fleet status and Tinyfish OAuth caveat
- Antigravity app/IDE/CLI setup and `agy` usage lessons
- auxiliary title/compression provider routing fixes
- Bangla academic assignment workflow
- Discord gateway "typing but no reply" stall diagnosis
- supply-chain scanner evaluation notes, when relevant to Hermes/AI tooling

Destination aggregate notes created/updated in this pass:

```text
Knowledge/MCP Operations.md
Work/Antigravity Setup.md
Knowledge/Academic Assignment Workflow.md
Knowledge/Hermes Operations.md
System/Assistant/issues-fixes-log.md
Memory/decisions.md
```

Verification used:

- count markdown files under the vault
- count `Imported —` / `Imported/Updated —` markers
- call dashboard `/api/graph`
- confirm service is enabled + active

Known-good expanded result after the session:

```text
notes: 23
links: 84
daily notes: 6
imported markers: 30
service: enabled + active
```

## Pitfalls

- Do not import raw transcripts.
- Do not preserve secrets, tokens, session tokens, OAuth URLs, process IDs, or stale one-off artifact IDs.
- Do not save transient setup failures as durable rules; save the persistence/config pattern that worked.
- If `/mnt/tb/hermes` resolves to `/root/.hermes`, keep the user-facing requested path `/mnt/tb/hermes/obsedianvault` in docs and service environment.
