---
name: system-monitor
description: Background daemon (systemd service, no cron) that monitors CPU load, CPU temperature, memory, swap, disk; sends alerts to Telegram and Discord when thresholds are sustained for 2-3 min. Auto-recovers with recovery notifications. Has 10-min cooldown per metric to avoid spam.
---

# System Monitor (no-cron, systemd daemon)

## What it is

A small Python daemon running as a **systemd user service** (not cron) that polls system metrics every 30s, detects sustained threshold violations, and sends alerts to Telegram and/or Discord.

## Why systemd service, not cron

- Survives reboots automatically (no crontab editing)
- Auto-restarts on crash (`Restart=always`)
- Cleaner logging via journald
- More reliable than `* * * * *` polling
- The user explicitly said "without cron job"

## Monitored metrics & default thresholds

| Metric | Source | Default threshold | Sustained for |
|---|---|---|---|
| CPU load avg (1-min) | `/proc/loadavg` | > 4.0 | 2 min (4 samples × 30s) |
| CPU temperature | `/sys/class/thermal/thermal_zone*/temp` | > 80°C | 2 min |
| Memory free | `/proc/meminfo` | < 500 MB | 2 min |
| Swap usage | `/proc/meminfo` | > 4 GB | 2 min |
| Disk usage | `df -P` | any mount > 90% | 5 min (single sample) |

## What it does on alert

1. Logs to `~/.hermes/logs/system_monitor.log` (JSON one-line per event)
2. Sends Telegram message via bot API (chat_id configurable)
3. Sends Discord message via webhook (if configured)
4. Enters 10-min cooldown for that metric (no re-alerts)
5. On recovery (metric back below threshold for 1 min), sends "recovered" notification

## Install

```bash
# 1. Script + service file already in place (created by setup)
# 2. Edit /root/.hermes/config/system_monitor.yaml for your thresholds + tokens
# 3. Enable the service
systemctl --user daemon-reload
systemctl --user enable system_monitor
systemctl --user start system_monitor

# 4. Verify
systemctl --user status system_monitor
tail -f ~/.hermes/logs/system_monitor.log
```

## Pitfalls learned

- **Don't** put `Restart=always` without `StartLimitIntervalSec` — systemd will respawn forever if it crashes in a tight loop
- **Always** handle SIGTERM cleanly to flush state file
- **Always** have a Discord webhook fallback if Telegram bot is rate-limited
- **Never** alert on a single sample — 30s × 4 samples = 2 min sustained prevents false alarms
- **Always** include the metric VALUE in the alert (not just "high CPU" but "CPU load 5.2 > 4.0")
- **Temperature** readings may not be exposed without root; daemon handles missing temp gracefully (skips, doesn't crash)
- **State file** is JSON, written atomically (tmp + rename) so a kill mid-write doesn't corrupt it
- **Cooldown** is per-metric and per-direction (alert vs recovery), so the same metric doesn't spam
- systemd **user services** don't run at boot unless `loginctl enable-linger <user>` is set
