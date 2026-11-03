# Thermal & CPU Pressure Diagnosis

Same methodology as the host memory pressure playbook, applied when the host
isn't crashing from OOM but from CPU saturation and BIOS/firmware thermal
shutdown. Both surface as "system keeps dying mysteriously" with similar
diagnostic shape.

## When to suspect thermal/CPU pressure (not memory)

- Host crashes hard (powers off, not graceful reboot)
- `dmesg` is clean of `Out of memory: Killed process`
- `free -m` shows plenty of `MemAvailable`
- `vmstat 1` shows no swap-in storms
- Crash happens during heavy workload (backup, indexing, compile, container)
- Boot history shows the same uptime pattern (every ~30 min, every 1-2 h)

## Read the thermal sensors directly

The first thing to check is **what the kernel thinks the trip points are**.
A user reports "laptop dies at 88-90°C" — is that the kernel's `critical`
threshold, or the firmware's?

```bash
# Per-zone trip points (in millidegrees C)
for z in /sys/class/thermal/thermal_zone*; do
  echo "--- $(cat $z/type) ($z)"
  for f in $z/trip_point_*_type; do cat $f; done
  echo
  for f in $z/trip_point_*_temp; do cat $f; done
  echo
done
```

Typical x86 laptop output (Broadwell i3 example):

| Zone | Type | Critical | Passive | Active |
|------|------|----------|---------|--------|
| acpitz | x86 ACPI | 108°C | 105°C | — |
| acpitz | x86 ACPI | 105°C | 95°C | 71/55/50/45/40 |
| pch_wildcat_point | PCH | 115°C | 95°C | — |
| B0D4 | Intel package | 100°C | 100°C | 86/81 |
| x86_pkg_temp | CPU package | — | — | — |

**Critical insight:** the kernel's `critical` trip is 100-115°C on most
laptops, but **the firmware/BIOS emergency cut fires earlier** (often 85-90°C
on thin laptops). If the user's reported shutdown temp is below the kernel's
`critical`, the system is being killed by BIOS, not Linux. `thermald` and
CPU throttling can only push the cutoff out so far — if load still reaches
the firmware threshold, the box powers off.

**Implication for triage:** if shutdown happens < kernel's critical temp,
the user's problem is **not solvable by Linux**. They need either: (a) less
load, (b) better cooling, (c) BIOS threshold change if available.

## Quantify current pressure (read sensors + load)

```bash
# All thermal zones, one screen
for z in /sys/class/thermal/thermal_zone*; do
  t=$(cat $z/temp 2>/dev/null)
  [ -n "$t" ] && [ "$t" != "-274000" ] && \
    printf "  %-25s %s°C\n" "$(cat $z/type)" "$((t/1000))"
done

# Load average vs core count
uptime
nproc

# Who's eating CPU right now
ps -eo pid,pcpu,pmem,user,etime,comm --sort=-pcpu | head -10
```

`load average > nproc` sustained = CPU pressure. The system has more runnable
work than cores can service, and that work is generating heat.

## Two failure signatures that look identical but are different

### A. Single process pinned at 100% CPU

Easy: `ps -eo pcpu --sort=-pcpu | head` shows the culprit. Kill or throttle.

### B. Docker daemon burning CPU but all containers show 0%

**This is the trap.** The naive read of `docker stats` shows all containers
at 0% CPU, so you conclude "Docker is fine". But `dockerd` and `containerd`
are each eating 15-25% CPU combined. The containers themselves are idle; the
daemon is busy processing container events (healthcheck failures, restart
loops, log spam, tunnel reconnects).

**Detection:**
```bash
ps -eo pcpu,comm | awk '/dockerd|containerd/ {sum+=$1; n++} END \
  {printf "Docker daemons: %.1f%% across %d procs\n", sum, n}'
# Anything > 5% combined on a quiet system = noise source
```

**Common noise sources (in order of likelihood):**

1. **Docker healthcheck fail loop.** Inspect:
   ```bash
   docker inspect <ctr> --format '{{.State.Health.FailingStreak}} | {{json .State.Health.Log}}'
   # FailingStreak climbing (56 → 369 → 500+) = healthcheck is wrong
   ```
   The healthcheck is wrong if the container itself runs fine but the
   healthcheck command (often `wget localhost:port`) hits a port that
   doesn't exist inside the container. Fix with
   `docker update --health-cmd="..." <ctr>` or remove the healthcheck
   entirely with `--health-cmd=""`.

2. **Container restart loop.** `docker ps -a` shows the same image
   constantly restarting. Either fix the container's startup command or
   `docker update --restart=no <ctr>` to stop the noise.

3. **Log spam from a flapping service.** `docker logs --tail 50 <ctr>`
   shows thousands of identical error lines. The container might be
   otherwise fine, but Docker is re-emit/logging them at high frequency.
   The fix is upstream (the flapping service), not Docker.

4. **Tunnel/reconnect loop.** Some networking containers (cloudflared,
   wireguard, zerotier) emit a tight loop of "Retrying connection in 1s"
   if the upstream is unreachable. `docker logs` shows the signature.
   Either fix the network/token or stop the container.

## Periodic CPU spikes on idle hosts (sustained-low, periodic-high pattern)

Different from sustained CPU pressure. The host is otherwise idle
(`load ~0.5-1.5`) but climbs to `load 4-6` every 15-30 min and settles
back in 1-2 min. Cause is almost always a periodic task firing.

### Discovery workflow (ordered)

1. **Confirm the periodicity.** Tail the last 60-90 min of `power_watch.log`
   and find timestamps where `load` jumps > 2x baseline. Compute intervals
   between spikes. If intervals are consistent (15, 20, 30 min), it's a
   scheduled task. If they're noisy, look for sync/reconnect loops instead.

2. **Check root crontab first** — cheapest:
   ```bash
   crontab -l
   ```

3. **Check `/etc/cron.d/`** — common offenders:
   ```bash
   ls /etc/cron.d/
   for f in /etc/cron.d/*; do echo "=== $f ==="; cat "$f"; done
   ```
   - `sysstat` runs `debian-sa1` every 10 min at `:05,:15,:25,...`
   - `php` runs `sessionclean` every 30 min at `:09,:39`
   - Anything else is user-added; review the schedule

4. **Check systemd timers**:
   ```bash
   systemctl list-timers --all
   ```
   Sort by `LEFT` to find short-interval timers (`RandomizedDelaySec` is
   common and hides the true cadence).

5. **Check Hermes cron (if installed)**:
   ```bash
   hermes cron list
   ```
   Look for `every Nm` schedules. Each one spawns a fresh Python
   interpreter and runs the script — heavy if the script does HTTP/API
   work. Common offenders: `bitwarden-fetch-watchdog` (every 15m, calls
   Bitwarden API + scrapes dashboard HTML + reads `/proc/<pid>/environ`).

6. **Check Docker container healthchecks** — any "unhealthy" container
   is hammering the daemon. See below for the IPv6 trap.

### Cross-correlate spike timestamps with candidate schedules

`power_watch.log` samples at `:01` of each minute. If a spike is logged
at `11:09:01 load=4.44`, the underlying event was around `11:08:30-11:09:30`.
Match that window against cron anchors:

| Spike minute | Likely source |
|---|---|
| `:09` or `:39` | `phpsessionclean` (system cron, every 30 min) |
| `:05, :15, :25, ...` | `sysstat-collect` / `debian-sa1` (every 10 min) |
| `:06, :21, :36, :51` | Hermes `bitwarden-fetch-watchdog` (every 15m) |
| `:00` of hour | `cron.daily` / `cron.hourly` runs |
| `RandomizedDelaySec` | systemd timer — check the unit file, not the schedule |

For automated spike-source correlation, run `scripts/cpu-spike-correlate.sh`
in this skill's directory.

### Docker healthcheck fail loop (the busiest silent CPU drain)

If a container is `unhealthy` with `FailingStreak` climbing into the
hundreds, every failed healthcheck tick burns daemon CPU. `docker stats`
will show the container at ~0% CPU — the work is in `dockerd` +
`containerd` processing the event.

```bash
# Find all containers with FailingStreak > 10
for c in $(docker ps --format '{{.Names}}'); do
  streak=$(docker inspect "$c" --format '{{.State.Health.FailingStreak}}' 2>/dev/null)
  case "$streak" in "<no value>"|"") ;;
    *) [ "$streak" -gt 10 ] 2>/dev/null && echo "$c: FailingStreak=$streak" ;;
  esac
done
```

**Disable a broken healthcheck without rebuilding the image:**
```bash
docker update --health-cmd="" <ctr>          # removes healthcheck entirely
# Or stop the noise source:
docker stop <name>
```

### The BusyBox wget + IPv6 localhost trap (nginx containers)

The single most common cause of an infinite-loop unhealthy container
with a `wget` healthcheck.

**Symptom:**
- `docker inspect <ctr> --format '{{json .State.Health}}'` shows
  `FailingStreak` climbing (e.g. 56 → 369 → 1250+)
- Healthcheck log says `wget: can't connect to remote host: Connection refused`
- Host can reach the service fine (`curl http://localhost:<hostport>/` returns 200)
- Inside the container, `wget -q --spider http://localhost/` fails
- nginx (or any web server) IS listening inside the container

**Root cause — three facts that combine to break it:**

1. **nginx defaults to IPv4-only listen** — the official nginx container
   config has `listen 80;` which means `0.0.0.0:80` (IPv4 only).
2. **`/etc/hosts` inside the container maps `localhost` to BOTH IPv4
   and IPv6:**
   ```
   127.0.0.1   localhost
   ::1         localhost ip6-localhost ip6-loopback
   ```
3. **BusyBox `wget` (Alpine images) resolves `localhost` to `::1` first**
   and tries to connect to `[::1]:80` — which nginx is not listening
   on. BusyBox's wget has no `--prefer-family=IPv4` option (unlike GNU
   wget), so you can't tell it to prefer IPv4. It just fails.

**Verify before fixing:**
```bash
docker exec <ctr> sh -c '
  echo "--- /etc/hosts ---"; cat /etc/hosts
  echo "--- nginx listening? ---"; netstat -tln | grep ":80"
  echo "--- wget localhost ---"; wget -q --spider http://localhost/ && echo OK || echo FAIL
  echo "--- wget with explicit IPv4 ---"; wget -q --spider http://127.0.0.1/ && echo OK || echo FAIL
'
# Expect: hosts has ::1, netstat shows only 0.0.0.0:80, localhost wget fails, 127.0.0.1 works
```

**Fix in running container (no rebuild needed):**
```bash
docker exec <ctr> sh -c '
  cp /etc/nginx/conf.d/default.conf /etc/nginx/conf.d/default.conf.bak
  sed -i "s/^    listen 80;$/    listen 80;\n    listen [::]:80 ipv6only=on;/" \
    /etc/nginx/conf.d/default.conf
  nginx -s reload
'
sleep 35   # wait for next healthcheck tick
docker inspect <ctr> --format 'Status={{.State.Health.Status}} FailingStreak={{.State.Health.FailingStreak}}'
# Expect: Status=healthy, FailingStreak=0
```

**Why the in-memory patch is enough for diagnosis but not for prod:**
container restart reverts the nginx config. For a permanent fix, update
the Dockerfile / image build to include the `listen [::]:80 ipv6only=on;`
line, or change the healthcheck to use `127.0.0.1` (but only if the
BusyBox build in your image supports the `-4` flag — many don't).

**Same trap applies to:** any web server that defaults to IPv4-only
listen (Apache, lighttpd, custom servers) inside a BusyBox/Alpine
container, when the healthcheck uses `wget http://localhost/...`.

### Making the fix permanent (patch source + rebuild + recreate)

The in-container patch above is good for unblocking the container
right now, but it **does not survive a container restart** — Docker
re-pulls a fresh layer from the image, and the COPY'd
`docker/nginx.conf` overwrites your in-place edit. To make the IPv6
fix durable:

1. **Patch the source config in the build context**, not just the
   running container:
   ```bash
   # Find the Dockerfile / build context
   grep -l "FROM nginx" /path/to/project 2>/dev/null
   # Patch the same line in the SOURCE nginx config
   sed -i 's/^    listen 80;$/    listen 80;\n    listen [::]:80 ipv6only=on;/' \
     /path/to/project/docker/nginx.conf
   ```

2. **Extract the original container's run options** so recreation is
   lossless:
   ```bash
   docker inspect <ctr> --format '\
     Image={{.Config.Image}} \
     Cmd={{json .Config.Cmd}} \
     PortBindings={{json .HostConfig.PortBindings}} \
     Restart={{.HostConfig.RestartPolicy.Name}} \
     Env={{json .Config.Env}}'
   ```

3. **Rebuild the image**. If the build context has a heavy `COPY`
   (multi-GB `site/` dir with thousands of files), it can exceed
   foreground timeouts. Use background + notify:
   ```bash
   # Foreground (fast builds, < 2 min)
   docker build -t <image>:<tag> /path/to/project
   # Background (heavy builds, > 2 min)
   docker build -t <image>:<tag> /path/to/project 2>&1 \
     | tee /tmp/<image>-rebuild.log &   # or use terminal(background=true, notify_on_complete=true)
   ```

4. **Recreate the container with the same options**:
   ```bash
   docker stop <ctr> && docker rm <ctr>
   docker run -d --name <ctr> --restart unless-stopped \
     -p <hostport>:<containerport> <image>:<tag>
   ```

5. **Wait one healthcheck interval** (~30s for typical setups), then
   verify the new container is healthy from a fresh state.

## Healthy-but-wasteful healthchecks (CPU tax with zero benefit)

Different from the fail-loop pattern above. The healthcheck **passes** (container is healthy), but it still burns CPU for nothing. This is the most common silent drain on small hosts.

### When to suspect it

- `docker stats` shows all containers at 0% CPU
- `containerd` + `dockerd` combined at 15-30% CPU with periodic 1-second spikes to 100%+
- `pidstat -t -p <containerd-pid>` shows ALL containerd threads spiking simultaneously every N seconds
- All containers are healthy (`docker ps` shows `(healthy)`)
- Restart policy is `unless-stopped` (healthcheck result is never used)

### Root cause

Containerd runs healthchecks on schedule regardless of whether the result matters. With 3+ containers each on a 30s interval, containerd enters all containers simultaneously, spawns `wget`/`node` processes, waits for responses, collects results — then discards them because `unless-stopped` ignores health status.

On a 15W i3-5010U, each burst hits 100%+ CPU for 1-2 seconds. Between bursts the system idles at 5-10%. The oscillation looks like "20-30% at idle" but is actually 0% → 100% → 0% every 30s.

### Diagnosis

```bash
# 1. Confirm healthchecks exist and are passing
for c in $(docker ps --format '{{.Names}}'); do
  hc=$(docker inspect "$c" --format '{{json .Config.Healthcheck}}' 2>/dev/null)
  rp=$(docker inspect "$c" --format '{{.HostConfig.RestartPolicy.Name}}')
  [ "$hc" != "null" ] && echo "$c: healthcheck=$hc restart=$rp"
done

# 2. Catch the burst in real-time (run for 60s)
pidstat -u 1 60 | grep -E "containerd|dockerd" | awk '$8 > 10 {print}'

# 3. Correlate with mpstat
mpstat -P ALL 1 30 | awk '/^[0-9]/ && $NF < 80 {print $1, $NF"% idle"}'
```

### Fix: remove healthchecks that serve no purpose

**Rule of thumb:** If restart policy is `unless-stopped` or `no`, the healthcheck provides zero functional benefit. It only marks the container as "unhealthy" in `docker ps` but triggers no action.

**Before removing, verify the container doesn't use healthcheck for:**
- Docker Swarm/K8s orchestration (uses health for scheduling)
- External monitoring that reads `.State.Health.Status`
- Any script that polls `docker inspect` health status

If none apply, remove the healthcheck.

**For compose files:**
```yaml
# Remove the entire healthcheck: block
healthcheck:
  test: [...]
  interval: 30s
  ...
```

**For Dockerfiles:**
```dockerfile
# Remove the HEALTHCHECK line
HEALTHCHECK --interval=30s --timeout=3s \
  CMD wget -q --spider http://localhost/ || exit 1
```

**After patching source, rebuild + recreate:**
```bash
# Compose
docker compose down && docker compose build --no-cache && docker compose up -d

# Dockerfile (heavy builds — use background)
docker build -t <image>:<tag> /path/to/project 2>&1  # background + notify
docker stop <ctr> && docker rm <ctr>
docker run -d --name <ctr> --restart unless-stopped -p <port> <image>:<tag>
```

**Verify fix:** Wait 2 healthcheck intervals (~60s), then check:
```bash
mpstat -P ALL 1 5
# Should show no spikes > 10% on any core
```

### Pitfall: shell variable interpolation when writing compose files

`${SIGNAL_LISTENER_SECRET:-}` in YAML gets eaten by the shell during heredoc/file writes. Use Python to write the file, or `git show HEAD:<file>` + Python line filtering to avoid shell interpolation entirely.

## Cloudflared reconnect loop — the most common case

`big-bear-cloudflared-web` (and similar) tunnels that fail to reach
Cloudflare's edge produce this exact pattern in `docker logs`:

```
ERR Failed to dial a quic connection ... timeout: no recent network activity
INF Retrying connection in up to 1s
ERR Connection terminated
INF Registered tunnel connection connIndex=N
... (loops every 1-4 seconds for 4+ parallel connIndex)
```

Symptom on the host: `dockerd` + `containerd` combined CPU hits 30-50%
even though the container itself shows < 1% CPU.

Diagnosis:
```bash
docker logs --tail 50 <cloudflared-ctr> 2>&1 | \
  grep -E "Retrying|ERR" | head -10
```

Fix paths:
- The tunnel token may be wrong/expired → reissue in Cloudflare Zero Trust
- The network is blocking QUIC/UDP 7844 → fall back to `protocol: http2`
- Just stop the container if it's no longer needed: `docker stop <name>`

## Boot-loop signature in `boot_watch.log`

If the user has a cron-based `boot_watch.sh` logging each boot, the crash
loop shows up as a clear pattern:

```
2026-06-17 18:52:59  BOOT  (52 min uptime)
2026-06-17 21:00:27  BOOT  (27 min uptime)   ← kept crashing
2026-06-17 22:27:58  BOOT  (31 min uptime)
2026-06-17 23:54:53  BOOT  (21h 5m uptime)   ← only one that survived
2026-06-18 21:00:40  BOOT  (current)
```

Look for:
- 5-minute gaps in `power_watch.log` between last entry and the new boot
  ID — the system was off, not gracefully shut down
- A change in crash cadence (e.g. "stayed up 21 h, then crashed again")
  that correlates with a config change or new container being added

## Power/thermal log correlation (the real diagnostic)

The fastest way to find the culprit when a host keeps overheating is to
correlate **`load average`** and **`x86_pkg_temp`** in the power_watch log.

Pattern that confirms CPU-driven thermal cutoff:

```
21:33:01  load=7.5    x86_pkg_temp=80
21:34:01  load=10.9   x86_pkg_temp=82
21:35:01  load=9.6    x86_pkg_temp=84
21:36:01  load=9.4    x86_pkg_temp=86
21:37:01  load=8.7    x86_pkg_temp=86
21:38:01  load=10.8   x86_pkg_temp=86
21:39:01  load=10.0   x86_pkg_temp=87
21:40:01  load=9.9    x86_pkg_temp=88     ← last reading
[5 min gap, no logs]
21:45:56  load=4.0    x86_pkg_temp=72     ← new boot
```

The temperature follows the load with a 1-2 minute lag. The 5-min gap
after the last reading is the system actually being off (not graceful
shutdown). This is the signature of BIOS emergency cut.

## Mitigation (cheapest → most invasive)

| Fix | What it does | When to use |
|------|--------------|-------------|
| Stop the noisy container | Eliminates root cause | Always do this first |
| Switch CPU governor `performance` → `schedutil` | Lets CPU idle down to 500 MHz | Background services on a server |
| Install `thermald` | Smart throttling before BIOS threshold | Safety net on laptops/hosts without good cooling |
| Cap CPU max freq (`echo 1500000 > /sys/.../scaling_max_freq`) | Hard limit | Last resort before hardware fix |
| Clean fan + repaste | 10-20°C improvement | Physical maintenance |
| Raise BIOS thermal threshold | If BIOS exposes it | Risky; can damage hardware |

The order on a server: stop noise → switch governor → install thermald →
cap freq. The order on a laptop: stop noise → elevate + cool → clean
fan → repaste → undervolt.

## `thermald` install on Debian 13 (no DPTF table)

```bash
apt install thermald
systemctl enable --now thermald
# Polling mode is fine for most CPUs without an Intel DPTF table
journalctl -u thermald -n 20
# Expect: "Polling mode is enabled: 4"
```

`thermald` will start throttling via P-state and T-state limiting when
any zone approaches critical. It does **not** prevent a firmware emergency
cut if load still reaches the BIOS threshold — it just buys time.

## Governor persistence

The kernel reverts to the BIOS-default governor on boot. To persist
`schedutil` on Debian 13:

- `cpufrequtils` is not in trixie repos. Writing
  `/etc/default/cpufrequtils` does nothing without the package.
- The `schedutil` governor is actually the systemd default on modern
  Debian/Ubuntu — verify with:
  ```bash
  cat /sys/devices/system/cpu/cpu*/cpufreq/scaling_governor
  # all should show "schedutil"
  ```
- If a custom value is needed at boot, use a systemd unit or `rc.local`,
  not `/etc/default/cpufrequtils`.

## Disk-space triage (related, often a hidden cause)

If a host is overheating while idle, also check whether a runaway
`docker image prune`, `du`, or backup operation is writing massive
amounts of data — disk I/O contention can pin a CPU. Quick check:

```bash
# Top disk consumers
dust -d 1 / -n 10

# Docker image bloat
docker system df
# Images: 136 (47 GB) where 23 are active = ~35 GB reclaimable

# Per-directory, fastest to slowest
du -sh /var /opt /usr /root /tmp 2>/dev/null | sort -hr
```

**Disk cleanup order on a 100 GB root partition that hits 90%+:**

1. `docker image prune -a -f` (often 30-40 GB reclaimable)
2. Remove old `.zip` backups in `/root` (1-2 GB)
3. `go clean -cache` if Go is installed; else `rm -rf /root/go/pkg/mod`
4. `journalctl --vacuum-time=7d` (5-20 MB)
5. `apt clean` (small but free)

After step 1, the user's root typically drops from 91% → 50% used.

## Pitfalls

- **Don't trust `docker stats` alone.** A container at 0% CPU can still
  be the root cause if its logs or healthchecks are noise-generating. Look
  at the daemon's CPU, not just the container's.
- **Don't conclude "BIOS protection" from a single crash.** Confirm with
  the boot-loop pattern in `boot_watch.log` and the load/temp correlation
  in `power_watch.log`. A single crash could be anything.
- **Don't disable the firmware thermal cut** to make the problem go away.
  That's how you cook a CPU. Mitigate the load, not the protection.
- **A node-MainThread or pyright-langserver** at 5-15% CPU on a quiet
  host is an IDE/editor language server, not a runaway. Check the parent
  process before killing.
- **Daemon configs with cross-validating fields crash on partial edits.**
  Many metrics daemons enforce `interval == tier1_resolution` (kula, vnstat
  variants, custom rollup tools) or `port == advertised_port` style
  invariants. `sed`-patching one without the other sends the daemon into
  a crashloop with cryptic "validation failed" exit codes. Always
  cross-check the config comment block ("Tier 1 (raw): must match
  collection.interval") and grep for the second occurrence before
  declaring the patch done. After editing, watch
  `systemctl status <svc>` and the journal for the first 30s — a daemon
  that starts, immediately exits, and auto-restarts has a config-level
  problem, not a runtime one.
- **`sed` anchored patterns silently miss on indent mismatch.** When
  patching YAML / nginx / similar with `sed -i 's/^      foo: 1s$/.../'`,
  always verify the exact whitespace first:
  `sed -n 'N p' file | cat -A` (the `cat -A` shows tabs as `^I` and
  trailing spaces as `$`). A 4-space vs 6-space mismatch causes the
  sed to no-op without error — the daemon then restarts with the old
  value, often crashing because the partial edit broke an invariant
  (see previous pitfall). For "only replace the FIRST occurrence"
  patterns (e.g. tier 1, not tier 1/2/3), use the 0-address form:
  `sed -i '0,/- resolution: 1s$/{s/- resolution: 1s$/- resolution: 5s/}'`.
- **Heavy `COPY` in Dockerfiles blows past foreground build timeouts.**
  A build context with `COPY site/` of 1+ GB and thousands of files can
  take 2-3 minutes just to ingest. Foreground `docker build` (with
  default 180s timeout) will hit the limit and abort mid-layer. Either
  bump the timeout, or use `terminal(background=true,
  notify_on_complete=true)` so you can keep working while the COPY
  churns. Verify layer cache invalidation first: a source-only change
  (`docker/nginx.conf`) should invalidate only the COPY of that file,
  not the `COPY site/` layer. If both invalidate, check that
  `.dockerignore` doesn't accidentally include build artifacts that
  bust the cache.
- **`go: command not found`** but `/root/go/pkg/mod` is 2 GB: Go is
  installed (probably at `/usr/local/go/bin`) but not in PATH. Safe to
  delete `/root/go/pkg/mod` — modules will re-download on next build.
- **thermal-conf.xml doesn't exist** → thermald runs in polling mode.
  This is fine for most CPUs without an Intel DPTF table, just less
  aggressive than the full P-state+T-state control.

## Reference commands cheat-sheet

```bash
# All-in-one thermal snapshot
sensors 2>/dev/null; \
  for z in /sys/class/thermal/thermal_zone*; do \
    t=$(cat $z/temp 2>/dev/null); \
    [ -n "$t" ] && [ "$t" != "-274000" ] && \
      printf "  %-25s %s°C\n" "$(cat $z/type)" "$((t/1000))"; \
  done

# Docker daemon vs containers
ps -eo pcpu,comm | awk '/dockerd|containerd/ {s+=$1; n++} \
  END {printf "Docker daemons: %.1f%% across %d procs\n", s, n}'
docker stats --no-stream --format \
  "table {{.Name}}\t{{.CPUPerc}}\t{{.MemUsage}}"

# Healthcheck fail detection
for c in $(docker ps --format '{{.Names}}'); do
  streak=$(docker inspect $c --format '{{.State.Health.FailingStreak}}' 2>/dev/null)
  [ "$streak" != "<no value>" ] && [ "$streak" -gt 5 ] 2>/dev/null && \
    echo "$c: FailingStreak=$streak"
done
```
