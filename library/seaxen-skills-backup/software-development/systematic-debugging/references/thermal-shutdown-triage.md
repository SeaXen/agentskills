# Thermal Shutdown Triage (BIOS-Level Emergency Cutoff)

Use when a laptop or small host keeps powering off at a specific, repeatable temperature (typically **80–95°C**) — *not* a clean shutdown, *not* a kernel panic, *not* overnight power loss. The pattern is: hard cut, no clean shutdown trail, new boot, same temperature, repeat.

Distinct from `references/sudden-poweroff-triage.md` (overnight power loss) and `references/overnight-auto-off-vs-hermes-cron.md` (Hermes-cron-vs-power-loss). This file is for the case where the user knows it is thermal and you need to find the cause.

## Fast triage order

### 1. Confirm the cutoff is *hardware*, not *kernel*

The Linux kernel's own `thermal_zone*/trip_point_*_temp` critical thresholds are usually **100–115°C**. If the user reports a hard cutoff at 80–95°C, the kernel's own protection did not fire — your laptop's **BIOS/UEFI emergency protection** (Intel/AMD Tjmax firmware cutoff, EC thermal shutdown) did.

Check the live trip points:

```bash
for z in /sys/class/thermal/thermal_zone*; do
  echo "--- $z ---"
  cat "$z/type"
  for f in "$z"/trip_point_*_type; do
    [ -f "$f" ] || continue
    t=${f##*trip_point_}
    t=${t%_type}
    echo "  $(cat $f) = $(cat $z/trip_point_${t}_temp 2>/dev/null) ($(($(cat $z/trip_point_${t}_temp 2>/dev/null)/1000))°C)"
  done
done
```

If kernel critical temps are ≥100°C but the machine cuts at 85–90°C → **firmware is the actor**, not Linux. The fix is *reducing the CPU load* that causes the cutoff, not changing Linux's trip points (which would not help anyway).

### 2. Find the cutoff temperature precisely

The cutoff temperature is fixed for a given laptop firmware. To pin it down:

- Read a minute-level **power/thermal logger** (see instrumentation below) and find the last temp reading before each reboot.
- Read `~/.hermes/diag/boot_watch.log` (or `journalctl --list-boots`) for hard-reboot frequency.
- Compare the last `x86_pkg_temp` (or equivalent package sensor) reading across all crash events. They will cluster tightly.

```bash
# Find reboot times from the user-installed power_watch.sh-style log
awk -F'[][]' '/boot_id=/{print $2, $7, $NF}' /root/diag/power_watch.log \
  | awk '{print $1, $2}' | sort -u | tail -20

# Find the temperature just before each boot_id change
awk '
  /boot_id=/ {
    if (prev_bid && prev_bid != bid) print prev_ts, prev_pkg
    prev_bid = bid
  }
  { match($0, /\[([0-9 :-]+)\]/, a); prev_ts=a[1]
    match($0, /x86_pkg_temp=([0-9]+)/, m); prev_pkg=m[1]
    match($0, /boot_id=([a-f0-9-]+)/, b); bid=b[1] }
' /root/diag/power_watch.log
```

If the last temp before reboot is 86–90°C and the kernel critical is 100°C → **confirmed BIOS emergency cutoff**.

### 3. Find what pushed the load

Once you know the cutoff is thermal and the cutoff temperature, find the **process that was eating CPU just before cutoff**:

```bash
# Live: top CPU + memory + start time
ps -eo pid,pcpu,pmem,user,start,etime,comm --sort=-pcpu | head -20

# Specifically look for daemon processes (long uptime) burning high CPU%
# These are the ones that load stays high across many minutes.
# A process that ran 5 minutes at 30% CPU = 90 CPU-seconds/min = 1.5 cores
```

Common culprits in this user's setup (laptops + Docker + Hermes + a few always-on apps):

| Pattern | Symptom in `ps` | Where to look next |
|---|---|---|
| **Docker container reconnect loop** (e.g. cloudflared, wireguard) | `containerd` 20–40% CPU, `dockerd` 10–20% CPU; container stats show 0% | `journalctl -u docker --since "30 min ago"` for repeated "Retrying connection" / "Failed to dial quic" |
| **Docker container image-defined healthcheck failure loop** | Same daemon-CPU symptom; one container shows `unhealthy` | `docker inspect <name> --format '{{.State.Health.FailingStreak}}'` — if non-zero, it has been failing for hours |
| **In-process runaway** (Python event loop, node LSP, build) | A single `python3`/`node` at 50–100% CPU for many minutes | Trace the parent (`awk '/^PPid:/{print $2}' /proc/$p/status`) and look at the actual command |
| **Kernel build / apt upgrade** | High load + `make` / `dpkg` near the top | `ps -eo etime,comm` should show the binary recently started, but compile jobs can run 5–15 min |

### 4. The "dockerd hot but container stats show 0%" pattern

This is the most common laptop trap. `docker stats` reads the cgroup metrics of each container. If a container is doing **light work that still burns host CPU via socket churn** (reconnect attempts, repeated healthcheck exec calls, log writing), the container's CPU% stays near 0 but `dockerd` + `containerd` eat 30–40% CPU on the host.

**Distinguishing this from a real container workload:**

```bash
# If the daemon CPU is high but per-container CPU is near 0, suspect control-plane churn
docker stats --no-stream --format "table {{.Name}}\t{{.CPUPerc}}\t{{.MemUsage}}"

# Sample Docker events for repeated exec_create / exec_start / exec_die on the same container
docker events --since "10m" --until "now" 2>/dev/null | grep -E "exec_|die|health" | head

# Count healthcheck failures per container
for c in $(docker ps --format '{{.Names}}'); do
  s=$(docker inspect $c --format '{{.State.Health.Status}} {{.State.Health.FailingStreak}}' 2>/dev/null)
  echo "$c: $s"
done
```

If a single container has `FailingStreak > 5` and the daemon CPU is hot, that container is the prime suspect. Override the image-defined healthcheck in compose:

```yaml
healthcheck:
  disable: true   # only for low-risk accessory apps (dashboards, tunnellers, downloaders)
```

Then `docker compose up -d <service>`, and verify with `docker inspect` that `Health.Status` is now `<none>` and daemon CPU drops.

### 5. The cloudflared-style "parallel tunnel reconnect" pattern

`cloudflared` is special — it opens **4 parallel QUIC tunnels** to different Cloudflare edge IPs and retries each independently. When the network drops, the log shows 4 simultaneous "Failed to dial quic ... Retrying in up to 1s" lines, and the daemon CPU sits at 15–25% even when nothing is happening.

This is the single most common cause of "containerd eats 25% CPU for no reason" on laptops running cloudflared. Fixes, in order of preference:

1. **`docker restart cloudflared-web`** — the tunnel may be stuck after a transient network blip; a restart usually clears it.
2. **Re-create the tunnel** if the token is corrupted.
3. **Remove the container** if it is not actively used.
4. **Lower the tunnel's `--retries` and `--max-conns`** flags if you keep the tunnel.

After each fix, sample `containerd`/`dockerd` CPU for 60s — if it is still 20%+, the issue is elsewhere.

## Instrumentation that pays for itself

If the user does not already have a minute-level power/thermal logger, install one **before concluding root cause**. Without it, the next incident is a guess again.

The canonical shape (from `references/sudden-poweroff-triage.md`):

```bash
# /root/diag/power_watch.sh — write once, run every minute from cron
LOG=/root/diag/power_watch.log
TS=$(date '+%Y-%m-%d %H:%M:%S %z')
BOOT_ID=$(cat /proc/sys/kernel/random/boot_id)
THERMALS=$(for z in /sys/class/thermal/thermal_zone*; do
  [ -f "$z/type" ] || continue
  printf '%s=%s;' "$(cat $z/type)" "$(cat $z/temp)"
done | tr -d '\n')
LOAD=$(cut -d' ' -f1-3 /proc/loadavg)
printf '[%s] boot_id=%s load=%s thermals=%s\n' "$TS" "$BOOT_ID" "$LOAD" "$THERMALS" >> "$LOG"
```

Cron line:

```
* * * * * /bin/bash /root/diag/power_watch.sh
```

Plus a `@reboot` boot marker so reboot frequency is visible:

```bash
# /root/diag/boot_watch.sh
LOG=/root/diag/boot_watch.log
TS=$(date '+%Y-%m-%d %H:%M:%S %z')
BOOT_ID=$(cat /proc/sys/kernel/random/boot_id)
printf '[%s] BOOT boot_id=%s\n' "$TS" "$BOOT_ID" >> "$LOG"
```

```
@reboot /bin/bash /root/diag/boot_watch.sh
```

The crash signature is unmistakable in the power_watch log: the last reading shows temps at 86–90°C, then a 1–15 minute gap with **no entries at all**, then a new boot with a different `boot_id`. The hard gap is the proof of a hard cutoff (a clean shutdown writes final journal entries; a BIOS cutoff does not).

## Mitigation ladder (cheapest → most invasive)

| Action | When to use | What it does |
|---|---|---|
| **Stop / restart the runaway container** | First move; always | Drop daemon CPU to baseline |
| **Disable image-defined healthchecks** on accessory apps | Daemon hot + container healthy-but-churning | Stop 30s exec churn |
| **Install `thermald` + `tlp`** | Want hardware throttling below the firmware cutoff | Aggressive throttling long before 88°C |
| **Cap CPU max frequency** | Immediate relief; no install | `echo 2000000 > /sys/devices/system/cpu/cpu*/cpufreq/scaling_max_freq` |
| **Intel-undervolt** (5–15°C cooler) | Sustained load is real work, not a runaway | Sub-mV voltage offset |
| **Clean fan + repaste** | Sustained high temps at low load (60°C+ idle) | Hardware fix |
| **Cooling pad / laptop elevation** | Cheap, immediate | 2–5°C improvement |
| **Raise BIOS thermal shutdown threshold** | Last resort; BIOS-dependent; risky | Lets machine run hotter but extends cutoff limit |

Cap frequency first if the cutoff is happening *right now* and the user wants instant relief — it works without installing anything and survives reboots if added to `/etc/rc.local` or a systemd unit.

## Worked example (this session — DietPi laptop, kula + Hermes + 7 Docker containers)

| Time (Asia/Dhaka) | acpitz | x86_pkg_temp | load | Notes |
|---|---|---|---|---|
| 21:33 | 80 | 80 | 7.5 | Spike starts |
| 21:35 | 83 | 84 | 9.6 | Climbing |
| 21:38 | 86 | 86 | 10.8 | Hot |
| 21:40 | 87 | 88 | 9.9 | Last reading |
| (5 min gap — no logs) | | | | BIOS cutoff |
| 21:45 | 70 | 72 | 4.0 | New boot |

Investigation found:

1. `cloudflared-web` container in tight reconnect loop (4 parallel QUIC tunnels, 1–4s retry each).
2. `medsea` container's image-defined healthcheck had been failing for 56 consecutive attempts (1 every 30s) — daemon burned CPU processing each failure.
3. Combined: `containerd` 22.8% + `dockerd` 17.4% = **40% CPU on Docker management alone**, on top of the rest of the system's idle load.

Fix: `docker stop cloudflared-web` (or restart to clear the stuck tunnel), and either restart `medsea` or override its healthcheck to disable.

## Common pitfalls

- **Don't** recommend raising Linux's thermal-zone critical temp. It is already 100–115°C, far above the firmware cutoff. Raising it changes nothing.
- **Don't** blame a single application container for high daemon CPU without sampling `docker events` first. Control-plane churn (reconnects, healthchecks) is a different failure mode.
- **Don't** assume the cutoff is random. A repeating cutoff temperature across multiple incidents is firmware-determined. Find the runaway, don't blame the hardware.
- **Don't** skip installing a minute-level power/thermal logger after a thermal incident. Without it, the next one is a guess.
- **Don't** confuse a clean shutdown (writes final journal entries, slow unload) with a hard cutoff (instant off, no final log lines, ext4 recovery on next boot). The hard gap in your logger is the proof.
- **Do** prefer stopping or removing a known-bad container over capping CPU frequency for long-term fix. Frequency cap is for instant relief, not for hiding a runaway.
- **Do** verify the fix with both a CPU drop *and* a temperature drop. CPU can be low while temperature is still climbing (because the heat sink is saturated); temperature falling is the real signal.
