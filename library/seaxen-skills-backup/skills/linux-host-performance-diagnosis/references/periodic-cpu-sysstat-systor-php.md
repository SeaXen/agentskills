# Periodic CPU: sysstat vs Systor vs PHP (DietPi / Hermes host)

Session-validated pattern on i3-5010U + Docker + Hermes + Systor.

## Symptom

User sees **~20–40% CPU** on an otherwise idle graph, often described as every **15–30 minutes**.

## Causes (layered)

| Layer | Cadence | What runs | Notes |
|-------|---------|-----------|--------|
| sysstat | **10 min** | `sysstat-collect.timer` → `sa1`; cron `debian-sa1` `5-55/10` | Disable **timer and cron** |
| PHP | **30 min** | `sessionclean` at **:09, :39** | Timer + `/etc/cron.d/php` |
| Systor | **~4 s** | `docker stats --no-stream` in background worker | Not 15–30m; amplifies dockerd spikes |
| Docker healthchecks | **30 s** (if present) | containerd exec in each container | Remove when `restart: unless-stopped` |

Hermes `every 15m` jobs (e.g. bitwarden watchdog) only matter if **enabled**.

## Diagnose

```bash
mpstat -P ALL 1 20
pidstat -u 1 10 | grep -E 'containerd|dockerd'
pidstat -u -C python3 1 5 | tail -15
pgrep -af 'serve.py.*8009'
systemctl list-timers --all | head -15
bash /root/.hermes/skills/host-memory-pressure-diagnosis/scripts/cpu-spike-correlate.sh
```

## Remove healthchecks (permanent)

- Compose: delete `healthcheck:` block, `docker compose up -d --force-recreate`
- Dockerfile: remove `HEALTHCHECK`, rebuild, recreate
- **MedSea-style nginx:** image listens on **80**; map host port with `-p 8855:80` not `8855:8855` unless config listens on 8855 inside

## Disable sysstat collection (keep mpstat/pidstat)

```bash
systemctl disable --now sysstat-collect.timer
sed -i 's/^5-55\/10/#DISABLED 5-55\/10/' /etc/cron.d/sysstat
```

Observe: spikes at **:15/:25** should no longer align with `sa1`; **:09/:39** may still bump if PHP cleanup runs.

## Systor mitigation

Source: `/mnt/tb/1Apps/systor/systor/web.py` — `_apps_cache_refresh_worker`, `time.sleep(4.0)`.

User must ask before changing production monitoring; suggest 30–60s sleep or stop `systor serve web` when unused.
