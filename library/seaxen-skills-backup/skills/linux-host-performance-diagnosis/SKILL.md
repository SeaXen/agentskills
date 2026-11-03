---
name: linux-host-performance-diagnosis
description: >
  Diagnose CPU load, temperature spikes, and periodic resource consumption on a
  Linux host (laptop or server). Use when the user says their CPU/heat goes up
  at intervals during idle, wants to know what's eating resources, or complains
  about thermal throttling. Covers: identifying periodic culprits (cron, systemd
  timers, container healthcheck storms), distinguishing lifetime-average vs
  current CPU in ps output, debugging container healthcheck failures (BusyBox
  wget IPv6), and right-sizing always-on monitoring services (kula, tianji,
  containerd). Hard rule: DIAGNOSE first — the user will tell you what to stop.
  Never disable or stop anything unless explicitly asked.
triggers:
  - cpu usage go up
  - cpu temp high
  - load average high
  - thermal
  - heat
  - hot
  - periodic spike
  - every few minutes cpu
  - idle cpu high
  - what is eating cpu
  - what is using cpu
---

# Linux Host Performance Diagnosis

## Hard rule: diagnose, don't stop

The user's default request is **find the cause**, not "stop things."
They will explicitly ask you to disable/stop a specific thing after you
identify it. Until then: measure, report, recommend — but do NOT stop or
disable anything.

Violating this rule erodes trust. If you stopped something the user needed,
they will say "why did I need it" or "just find them not stop." Treat that as
a correction and revert immediately.

## Phase 1: Snapshot the current state

Run these together in one batch:

```bash
uptime
cat /sys/class/thermal/thermal_zone*/temp 2>/dev/null | awk '{printf "%.1f°C\n", $1/1000}'
ps -eo pid,ppid,etimes,pcpu,pmem,comm,args --sort=-pcpu | head -25
docker stats --no-stream --format 'table {{.Name}}\t{{.CPUPerc}}\t{{.MemUsage}}'
systemctl list-timers --all | head -20
crontab -l
grep -v '^#\|^$' /etc/cron.d/*
hermes cron list
pidstat -u -C python3 1 5 2>/dev/null | tail -20
```

## Phase 2: Distinguish lifetime-average from current CPU

`ps -o pcpu` shows **lifetime average since process start**, NOT current usage.
This is the #1 misdiagnosis trap.

```bash
# Check kernel wait channel — "futex_wait" or "ep_poll" = idle
cat /proc/<PID>/wchan

# Sample 5 times over 15s to catch spiky processes
for i in 1 2 3 4 5; do
  ps -eo pid,pcpu,comm,args --no-headers | awk '$2 > 3.0' | sort -k2 -nr | head -5
  sleep 3
done

# Thread-level sampling — reveals which threads inside a process are spiking
# (e.g., containerd healthcheck executor threads)
pidstat -t -p <PID> 1 5
```

**Common high-ps-cpu processes that are actually idle:**
- `containerd` (15% lifetime on 10-container host — usually futex_wait)
- `dockerd` (9% lifetime — same)
- Any long-running process: the average smooths out peaks

## Phase 3: Identify periodic culprits

### Cron and timer schedule quick-reference

| Schedule | Source | Typical spike |
|---|---|---|
| `* * * * *` | root crontab (power_watch.sh) | ~0.5s every minute |
| `*:00/10` (systemd) + `5-55/10` (cron) | **sysstat** `sa1` / `debian-sa1` | ~1–5s every **10min** (both can be active — disable **both**) |
| `09,39 * * * *` | phpsessionclean (+ `phpsessionclean.timer`) | ~2–3s every **30min** |
| **every ~4s** (not calendar) | **Systor** `_apps_cache_refresh_worker` → `docker stats --no-stream` | **dockerd/containerd** bursts; feels random, not 15–30m |
| `every 15m` | Hermes cron (e.g. bitwarden-fetch-watchdog) | 5–15s if **enabled** (often paused) |
| `every 240m` | Hermes cron (obsidian-dashboard-watchdog) | ~10s every 4h |
| **continuous** | **`hermes-telemetry-dashboard`** (`serve.py` **:8009**) | **~1 core** — heavy SQLite on **`state.db` (~2 GB)** + 300s cache refresh; browser auto-refresh worsens it. **Multiple background cache loops share `DEFAULT_REFRESH_SECONDS=300`** and wake on the same wall-clock minute, so all-time (`window_hours: 0` / `limit_days>=3650`) cache entries rescan the entire history every 5 minutes. Fix: skip all-time keys from background warm + stagger cache start across caches. |
| **continuous** | **Systor** `docker stats` every **4s** | dockerd/containerd bursts (see above) |

**“15–30 minute” idle bumps:** usually **PHP :09/:39 (30m)** + **sysstat (10m)** stacking on a weak CPU — not the same rhythm as Systor (continuous). Correlate with `bash …/cpu-spike-correlate.sh` on `/root/diag/power_watch.log` and `systemctl list-timers --all`.

**sysstat for spike debugging:** `sar` / `sa1` buckets are **10-minute** history — they do **not** replace live `mpstat`/`pidstat` or timer/cron correlation for “which process spiked for 2 seconds.” Keep the `sysstat` package for `mpstat`/`pidstat`; disabling collection is fine.

### Container healthcheck storms

A container that is `unhealthy` with high `FailingStreak` (100+) retries
every 30s by default. Cumulative effect adds up and fills logs.

```bash
docker inspect <name> --format='{{json .State.Health}}' | python3 -m json.tool
```

### Unnecessary healthchecks on `unless-stopped` containers

A container with a healthcheck but `RestartPolicy: unless-stopped` gets **zero
value** from the healthcheck — Docker does NOT restart it on healthcheck
failure. The healthcheck still runs, enters the container, executes the probe
command, and collects results every N seconds. On a low-power host (laptop i3,
ARM), 3 containers with 30s-interval healthchecks cause containerd to spike to
100%+ CPU for 1-2 seconds every 30s as all probes fire simultaneously.

**Diagnosis:**
```bash
# Check which containers have healthchecks
docker inspect --format '{{.Name}} {{.Config.Healthcheck}}' $(docker ps -q)

# Cross-reference with their restart policy
docker inspect <name> --format '{{json .HostConfig.RestartPolicy}}'
```

**Rule:** If restart policy is `unless-stopped` (or `never`) AND the container
process is simple (single-process, exits on crash), the healthcheck is pure
waste. Remove it from the image/compose and recreate the container.

**Confirmation via thread-level CPU sampling:**
```bash
pidstat -t -p <containerd_PID> 1 5
```
Shows containerd threads spiking to 20-25% each during healthcheck execution
vs ~0% between intervals.

**BusyBox wget + nginx IPv6 gotcha:**

Alpine containers use BusBox `wget`, which resolves `localhost` to `::1`
(IPv6) first. If nginx only listens on `0.0.0.0:80`, healthcheck fails with
"Connection refused."

Fix — add to nginx config:
```nginx
server {
    listen 80;
    listen [::]:80 ipv6only=on;
    ...
}
```

Then **rebuild the image and recreate the container** — an in-memory patch
(container exec + sed) is lost on restart.

### Systemd auto-restart loops

If a service is in `activating (auto-restart)` state, it's crashing and
restarting repeatedly.

Note: `systemctl stop` from inside a Hermes gateway session is blocked
("cannot restart or stop the gateway from inside the gateway process"). Use
`pkill` directly, or ask the user to run from a separate shell.

## Phase 4: Right-size always-on monitors

### kula

Config: `/etc/kula/config.yaml`

**Rule:** `collection.interval` MUST match tier 1 `resolution` exactly.

```yaml
collection:
  interval 5s     # was 1s — cuts CPU ~5x
storage:
  tiers:
    - resolution: 5s   # must match interval
      max_size: 50MB   # was 250MB — 50MB = ~9h raw at 5s
    - resolution: 1m
      max_size: 150MB
    - resolution: 5m
      max_size: 50MB
```

After changing:
```bash
systemctl stop kula
rm -f /var/lib/kula/tier_*.dat
systemctl reset-failed kula
systemctl start kula
```

### tianji-reporter

Rust binary collecting CPU/mem/disk/network → tianji.dev. ~1% CPU. Leave
unless explicitly asked to remove.

### containerd / dockerd

Infrastructure. Check `wchan` (futex_wait = idle). Lifetime `ps` % is often a
red herring — but **live** `pidstat -t -p <containerd_pid> 1 5` can show real
1s bursts (healthchecks removed or Systor polling Docker).

### Systor (when installed)

If `systor serve web` is running, a daemon thread refreshes apps cache every
**4s** and calls `docker stats --no-stream` (`systor/web.py`:
`_apps_cache_refresh_worker`). That hammers **dockerd/containerd** on
low-power hosts even when all containers show 0% in stats.

**Mitigation (only when user asks):** increase `time.sleep(4.0)` in that worker
to 30–60s, or stop the web service when the dashboard is unused; raise
`apps.auto_refresh_sec` / `dashboard.refresh_sec` in `/etc/systor/config.yaml`.

### Disable sysstat collection (when user opts out)

Disabling only the systemd timer is **not enough** — Debian also runs
`debian-sa1` from `/etc/cron.d/sysstat` every 10 minutes.

```bash
systemctl disable --now sysstat-collect.timer
# Comment the 5-55/10 line in /etc/cron.d/sysstat (patch tool may refuse — use sed with user approval)
sed -i 's/^5-55\\/10/#DISABLED 5-55\\/10/' /etc/cron.d/sysstat
```

Re-enable: `systemctl enable --now sysstat-collect.timer` and restore the cron line.

### Hermes telemetry dashboard (`hermes-telemetry-dashboard.service`)

Plugin path: `~/.hermes/plugins/hermes-telemetry/dashboard/serve.py`, default **port 8009**.

**Symptom:** Host CPU **30–40%+** while graphs look “idle”; `pidstat` shows **`python3 serve.py` at ~100%** for seconds or hours.

**Cause:** Background cache thread refreshes every **300s**, but each refresh scans large **`state.db`** and telemetry SQLite. Open browser tabs with auto-refresh add concurrent API work.

**Mitigation (only when user asks):**

```bash
systemctl stop hermes-telemetry-dashboard.service
systemctl disable hermes-telemetry-dashboard.service
```

Use only when needed; re-enable for token/cost dashboards.

## OmniRoute memory diagnosis (Docker + Node child process)

When OmniRoute appears to use ~1–2 GiB, do not rely on `docker stats` alone or assume the main PID owns the memory. The container may have a small Next/Node launcher plus a large child process.

```bash
CG=/sys/fs/cgroup/system.slice/docker-$(docker inspect -f '{{.Id}}' omniroute).scope/cgroup.procs
for p in $(cat "$CG"); do
  ps -o pid,ppid,pcpu,pmem,rss,vsz,stat,args -p "$p" --no-headers
done
```

Inspect the large child:

```bash
p=<child-pid>
grep -E 'VmRSS|RssAnon|RssFile|Threads' /proc/$p/status
cat /proc/$p/wchan
tr '\0' '\n' < /proc/$p/environ | grep -E 'OMNIROUTE_MEMORY_MB|NODE_OPTIONS'
grep -E '^(Rss|Pss|Private|Anonymous|AnonHugePages|Swap)' /proc/$p/smaps_rollup
```

The supported heap knob is `OMNIROUTE_MEMORY_MB` (the standalone launcher appends `--max-old-space-size`). Test conservatively at 768 MB before considering 512 MB, but verify actual RSS after a clean recreate. A lower V8 heap ceiling may not reduce RSS when the dominant allocation is native/anonymous memory; do not leave the lower setting if it provides no measurable benefit or increases OOM risk. A clean recreate can temporarily recover accumulated memory without changing provider data.

Also inspect logs for background pressure:

```bash
docker logs --since 15m omniroute 2>&1 | grep -E 'CredentialHealth|ProviderLimitsSync|LocalHealthCheck|TOKEN_REFRESH'
```

Large provider-account pools and repeated health-check timeouts often explain slow dashboard/API loading. Disable only clearly unused/duplicate provider connections; never guess which accounts are safe to remove. Preserve `storage.sqlite` and `server.env` before any recreate.

## Phase 5: Report findings

1. **Current state** — load avg, temps, top processes (lifetime vs current clarified)
2. **Periodic culprits** — schedule, impact, already-handled status
3. **Always-on services** — CPU contribution, whether necessary
4. **Recommendations** — ordered by impact, "do you want me to..." for each

Do NOT stop anything. Let the user decide.

## Hermes Dashboard auth (June 2026 hardening)

`--insecure` **still works** despite CLI help saying "DEPRECATED / NO-OP". The official docs confirm it allows binding to `0.0.0.0` without auth. Use it when you need a no-auth public bind (e.g., port 9120 for LAN access without login).

**For auth on a public port**, use hermes' built-in `basic_auth` in config.yaml — bind to `0.0.0.0` directly. Do **not** add nginx `auth_basic` in front. Double layer = double login prompt.

**Crashloop symptom:** `hermes-dashboard.service` in `activating (auto-restart)` with high restart counter (500+), each restart consuming ~6s CPU → periodic temp spikes. Cause: no auth provider configured when binding to `0.0.0.0`.

**Fix — basic auth (recommended for single-user):**
```bash
# Generate hash
PYTHONPATH=/usr/local/lib/hermes-agent python3 -c \
  "from plugins.dashboard_auth.basic import hash_password; print(hash_password('your-password'))"
```
Then set in `config.yaml`:
```yaml
dashboard:
  basic_auth:
    username: sagar
    password_hash: scrypt$16384$8$1$...
    session_ttl_seconds: 86400  # 24 hours; 0 = 12h default
```
Restart from a **separate shell** (not inside gateway): `systemctl restart hermes-dashboard`

**Port layout convention (Dr. Sagar):**
- `9119` = hermes dashboard with official `basic_auth` (no nginx)
- `9120` = hermes dashboard with `--insecure` (no auth, LAN access) — optional

**Nginx reverse proxy + hermes auth interaction:**
If nginx has `auth_basic` AND hermes has `basic_auth`, users get **double auth prompts**.
Fix: remove `auth_basic` from nginx config, let hermes handle it.
If you want nginx-level auth instead, bind hermes to `127.0.0.1` only.

## RAPL energy logging & daily reports

The host's per-minute logger `/root/diag/power_watch.sh` now also records Intel
RAPL energy counters (`rapl_pkg_uj`, `rapl_core_uj`, `rapl_dram_uj`) — cumulative
microjoules since boot. A companion script `/root/diag/energy_report.py`
computes daily watt-hours, average/peak power, and handles reboot resets via
`boot_id`. A midnight Hermes cron job (`no_agent: true`) delivers a daily
energy summary to Discord.

**Key caveat:** RAPL captures CPU package + DRAM only — it undercounts
whole-system wall draw by ~30–50% (no screen, disk, radio, dGPU). For exact
wall wattage, a smart plug on the charger is required. RAPL is for trend
tracking and anomaly detection.

See [RAPL Energy Logging & Daily Reporting](references/rapl-energy-logging.md)
for implementation details, unit conversion, and verification steps.

Bundled scripts (copy to host before use):
- `scripts/energy_report.py` — the daily Wh/power/peak report. Copy to `/root/diag/energy_report.py`.
- `scripts/daily_energy.sh` — midnight cron wrapper. Copy to `~/.hermes/scripts/daily_energy.sh`.

**Discord delivery target:** set in the Hermes cron job's `deliver` field (e.g., `discord:<channel_id>`), not in the script itself. The script is channel-agnostic — it just writes to stdout.

## References

- [AceRoute CPU bursts + cadence fix](references/aceroute-cpu-bursts.md) — stop/remeasure, BWS journey prefetch, compose knobs
- [Hermes telemetry :8009 5-min spike fix](references/hermes-telemetry-5min-spike-fix.md) — multi-cache synchronized wake-up, all-time key skip, deterministic stagger, DB-level verification
- [Healthcheck waste on `unless-stopped` containers](references/healthcheck-unless-stopped-waste.md) — why working healthchecks on `unless-stopped` containers burn CPU for zero value
- [Periodic CPU: sysstat vs Systor vs PHP](references/periodic-cpu-sysstat-systor-php.md) — 10m/30m calendar spikes vs 4s Docker polling; disable checklist
- [Nginx + Hermes auth interaction](references/nginx-hermes-auth-interaction.md)
- [RAPL Energy Logging & Daily Reporting](references/rapl-energy-logging.md) — extending power_watch.sh with energy counters; daily Wh reports; reboot reset handling; RAPL vs wall-draw caveat

## Scripts

- `scripts/energy_report.py` — daily energy report (Wh, avg/peak power) from RAPL logs; reboot-safe via boot_id
- `scripts/daily_energy.sh` — midnight cron wrapper for the report; channel-agnostic (deliver target set in cron job)

## Pitfalls

- **containerd/dockerd lifetime average**: Always check `wchan` first
- **kula config mismatch**: interval and tier 1 resolution must match exactly
- **BusyBox wget IPv6**: Alpine containers need nginx on `[::]:80` too
- **systemctl from inside gateway**: Use `pkill` or ask user to run from separate shell
- **ps pcpu is lifetime**: Sample multiple times to catch spiky processes
- **Self-inflicted monitoring**: power_watch.sh (`* * * * *`) causes a small spike every minute
- **Hermes dashboard crashloop**: `--insecure` no longer disables auth; configure `basic_auth` in config.yaml
- **Healthcheck on `unless-stopped`**: A container with healthcheck but `unless-stopped` restart policy gets zero value — Docker does NOT restart on healthcheck failure. The probe still runs and burns CPU. Remove it.
- **Rebuild port mismatch**: After rebuilding a Dockerfile-based container, the new image may listen on a different port than the old custom config (e.g., fresh `nginx:alpine` listens on 80, but old run used `-p 8855:8855`). Always verify with `curl` and `docker port <container>`; map `-p 8855:80` when nginx listens on 80 inside.
- **sysstat disable incomplete**: `systemctl disable sysstat-collect.timer` alone leaves cron `debian-sa1` on `5-55/10` — spikes every 10m continue.
- **hermes-telemetry :8009**: Can hold **~100% of one core** for hours — check with py-spy/pidstat before blaming Docker/sysstat. The first fix (PR #82) only bounded one cache (`ModelEfficiencyCache`); **4 sibling caches (`ProvidersCache`, `ProviderHealthCache`, `DailyTokenChartCache`, `DailyModelChartCache`) kept the same `DEFAULT_REFRESH_SECONDS=300` loop** and piled onto the same SQLite connection every 5 minutes. Comprehensive fix (PR #91) skips all-time/zero-window keys from background warm and staggers initial cache start. **Lesson: when fixing a periodic CPU bug in a class hierarchy with N subclasses, check ALL subclasses for the same loop pattern.** DB-level verification (`SELECT built_at FROM endpoint_payload_cache`) is more reliable than a CPU watch. See `references/hermes-telemetry-5min-spike-fix.md`.
- **Bursty AceRoute/uvicorn :8866**: not steady 10–30%; 1s samples alternate 0% and 45–100%. Journey CLI prefetch reloads Bitwarden secrets. Prefer 10–20×1s samples; stop+remeasure only when asked. Ops: `learnables/aceroute-system`.
- **Disruptive network tests**: user forbids long WARP connect/disconnect and multi-minute speedtests on this host (Hermes Discord looks offline). Short checks only unless explicitly asked + warned.
- **Terminal false-positive on `uvicorn`**: shell lines containing `uvicorn` may be blocked; use Python `/proc` sampling or docker inspect/stats instead.
- **Scope**: this Hermes runs on DietPi host, not a physical laptop — say so when user says "laptop".
- **Stop exception**: if user names stop/restart/remeasure a process, do the controlled A/B; default remains diagnose-only.
