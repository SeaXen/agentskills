---
name: host-memory-pressure-diagnosis
description: Diagnose and fix Linux host memory pressure on machines running Hermes + Docker + Python + browser-based MCP servers. Use when a host hangs, won't accept SSH, has load average >> core count, shows OOM events in dmesg, or when any session work triggers catastrophic swap thrash. Covers reading pressure signals, finding the actual leak source (not the obvious symptom), safe cleanup without killing your own shell, and prevention patterns for browser-pool MCP servers.
tags: [linux, memory, docker, oom, diagnosis, hermes, mcp]
related_skills: []
---

# Host Memory Pressure Diagnosis

When a host running Hermes + Docker + Python becomes unresponsive, this is the methodology. Skip the temptation to "just kill the top process" — that usually misses the real leak and can kill your own shell.

## Triage: confirm it's actually memory pressure

Before chasing processes, confirm memory is the problem and not e.g. disk I/O, CPU saturation, or a wedged network daemon.

```bash
uptime                          # load average; compare to core count
free -m                         # MemAvailable vs total; Swap used vs SwapTotal
dmesg --since "10 minutes ago"  | grep -iE "oom|memory pressure|under memory"
```

Reading the kernel log is decisive: `Under memory pressure, flushing caches` = chronic starvation but not yet fatal; `Out of memory: Killed process` = OOM-killer fired. If neither, the slowness may be something else.

**The kernel log is the source of truth.** `ps`-only views are deceptive because they show what's scheduled, not what's blocked on swap-in.

**If symptoms match thermal/CPU pressure instead of memory** (hard power-offs, `dmesg` clean of OOM, temperatures climbing before crash, BIOS emergency cut), see `references/thermal-and-cpu-pressure.md` — same methodology, different signals.

## Methodology (ordered)

1. **Quantify pressure**: `free -m` + `SwapUsed`. If `SwapUsed > 0` AND `MemAvailable < 500 MiB`, you're under pressure.
2. **Identify top RSS consumers**: `ps -eo pid,user,pcpu,pmem,rss,comm --sort=-rss | head -20`. RSS, not VSZ.
3. **Group by purpose, not just PID**: a single user-facing tool may have spawned 50+ child processes (browsers, drivers, helpers). Use `pstree -ap <pid>` to see the family.
4. **Trace parents**: `awk '/^PPid:/{print $2}' /proc/<pid>/status` for any suspicious PID. A leak in a child MCP/extension is almost always parented to a long-running daemon (Hermes dashboard, gateway, systemd).
5. **Measure the leak footprint**: `instances × per-instance RSS`. If 3 instances × 970 MiB each = 2.9 GB, that's your leak.
6. **Confirm the pattern repeats**: are children accumulating over time, or stable? Stable count = constant leak. Growing count = respawn loop on top of leak.
7. **Clean up at the source, not the symptom**: don't kill children if a parent will just respawn them. Fix the parent (config disable) or patch the leak source.

## Common leak patterns

### Browser-pool MCP server (Selenium + chromedriver + Chromium)

Most common in this user's setup. Symptoms:
- `pgrep -f chromedriver` returns more than 0
- `pgrep chromium` returns dozens of `--headless --test-type=webdriver` processes
- RSS totals in the 100s of MiB to multiple GiB
- Process tree shows `chromedriver` parented to a Python MCP server script

**Root cause**: MCP server uses a "browser pool" for performance — pre-spawns N headless Chrome instances at startup and never closes them. Each browser = 1 chromedriver + ~7 chromium children + 2-3 crashpad handlers. Without `atexit.register(self.cleanup)` and `signal.signal()` handlers, every graceful or forced exit leaves the whole tree orphaned.

**Quick identification command**:

```bash
# Find the source MCP server
for p in $(pgrep chromedriver); do
  ppid=$(awk '/^PPid:/{print $2}' /proc/$p/status)
  echo "  chromedriver $p → parent $ppid: $(tr '\0' ' ' < /proc/$ppid/cmdline | cut -c1-100)"
done
```

**Per-instance footprint**: ~970 MiB for 4 browsers (max_concurrent=4). Scales linearly with concurrent count.

**Patch template** (apply to any Selenium MCP server):

In the scraper class, track the user-data-dir explicitly:
```python
import uuid
self._user_data_dir = f"/tmp/<prefix>-{uuid.uuid4().hex[:12]}"
chrome_options.add_argument(f"--user-data-dir={self._user_data_dir}")
```

In `close()`:
```python
import shutil
if getattr(self, "_user_data_dir", None) and os.path.isdir(self._user_data_dir):
    shutil.rmtree(self._user_data_dir, ignore_errors=True)
```

In the MCP server's pool manager, register cleanup:
```python
import atexit, signal
atexit.register(self.cleanup)
for sig in (signal.SIGTERM, signal.SIGINT, signal.SIGHUP):
    try:
        signal.signal(sig, self._signal_cleanup)
    except (ValueError, OSError):
        pass

def _signal_cleanup(self, signum, frame):
    self.cleanup()
    signal.signal(signum, signal.SIG_DFL)
    os.kill(os.getpid(), signum)

def cleanup(self):
    if self._shutting_down: return
    self._shutting_down = True
    with self.browser_lock:
        for scraper in self.browser_pool:
            try: scraper.close()
            except Exception: pass
    # Belt-and-suspenders: kill any orphan chromedriver children
    try:
        subprocess.run(["pkill", "-9", "-P", str(os.getpid()), "-f", "chromedriver"],
                       timeout=2, capture_output=True)
    except Exception: pass
```

**Disable without removing** (user preference: keep config entry):
```bash
hermes config set mcp_servers.<name>.enabled false
# Restore: same with true
```

Note: this writes to `~/.hermes/config.yaml` (user override layer). Takes effect on next Hermes restart. Already-running processes keep running until restart.

### Page-cache thrash from Python scripts

Running `sha256sum` or `open()` on a multi-GB file set in a loop will pin all those pages in the page cache, evicting everything else. With low RAM, this triggers swap-in storms.

**Detection**: `cat /proc/meminfo | grep -E "^(Cached|Dirty|AnonPages):"` — large `Cached` with small `MemAvailable` = page cache pressure.

**Fix**: process files one at a time, drop_caches between (`sync; echo 3 > /proc/sys/vm/drop_caches` — needs root), or use `O_DIRECT` for large files.

### Docker container memory ceiling (cgroups)

If `/sys/fs/cgroup/memory.max` or `docker stats` shows a container at its limit, that container's OOM-killer fires before the host sees pressure.

**Detection**: `docker stats --no-stream --format "table {{.Name}}\t{{.MemUsage}}\t{{.MemPerc}}"`

**Fix**: raise container memory limit in `docker-compose.yml`, or stop non-essential containers.

### Docker healthcheck CPU burst (periodic spikes, not fail-loop)

If `docker stats` shows all containers at 0% but `containerd` is spiking to 20-30%
every 30s, the healthchecks are **working but wasteful** — they pass, but the
daemon still burns CPU executing them. This is especially painful on low-power
CPUs (i3-5010U, ARM SBCs) where each burst hits 100% for 1-2 seconds.

**Quick disable for diagnosis:**
```bash
# Disable healthcheck on a running container (no restart needed)
docker update --health-cmd="" <ctr>
```

**Permanent fix:** remove healthcheck from Dockerfile or compose file and
rebuild+recreate. See `references/thermal-and-cpu-pressure.md` → "Healthy-but-wasteful healthchecks" section.

**Rule:** If restart policy is `unless-stopped` or `no`, healthchecks provide
zero benefit — remove them from compose/Dockerfile and recreate (not just
`docker update --health-cmd=""` if you want the change to survive rebuilds).

**Paths on this host (examples):** Tradingx `docker-compose.yml`;
MedSea `Dockerfile` under `Sea-knowledge/#MedSea/`. After MedSea rebuild,
verify port map: nginx in image listens on **80** → `-p 8855:80`.

For **calendar periodic** CPU (10m sysstat, 30m PHP) vs **continuous** Systor
`docker stats` polling, see `linux-host-performance-diagnosis` →
`references/periodic-cpu-sysstat-systor-php.md`.

## Safe cleanup checklist

When you've identified the leak and need to clean it up:

- **Use specific PIDs, not `pkill -f <pattern>`**. `pkill -f` matches anything in the cmdline, including your own bash session if the pattern is too broad.
- **Send SIGTERM first, SIGKILL only if no response**. SIGTERM lets signal handlers run `cleanup()`, which is the whole point of the patch.
- **Wait 5-10 seconds between SIGTERM and SIGKILL**. Cleanup may take a few seconds to reap children.
- **Verify the cleanup worked**: check `pgrep` for the same pattern after the kill. If instances dropped but came back, you have a respawn loop — fix the parent.
- **Don't kill the long-running parent (Hermes, systemd) without confirming it's safe**. A Hermes dashboard restart causes dashboard clients to reconnect. A systemd-killed MCP triggers respawn loop.

```bash
# Safe targeted cleanup pattern
PIDS=$(pgrep -f "<specific-pattern>")
for p in $PIDS; do
  kill -TERM $p
done
sleep 5
# Verify
remaining=$(pgrep -f "<specific-pattern>" | wc -l)
if [ "$remaining" -gt 0 ]; then
  echo "still $remaining alive, escalating"
  pgrep -f "<specific-pattern>" | xargs -r kill -9
fi
```

## Pitfalls

- **"X Mbit/s" can be lying**. When an upload shows great throughput but a socket is in `CLOSE-WAIT` state, the bytes are flowing into the local TCP send buffer, not to the remote. Verify transfer with a remote-side check (HTTP status, response bytes) before claiming success. Inspect with `ss -tnp -p | grep <pid>` for state.
- **`pkill -f` from inside the same shell session can kill your own terminal** if the pattern matches your bash commandline. Use specific PIDs.
- **Hermes gateway auto-respawns child MCPs**. Killing a chart MCP / browser MCP / etc. just causes the parent Hermes gateway to spawn a new one within seconds. Fix at the config level (`enabled: false`) and accept the memory cost until next restart, OR restart Hermes cleanly.
- **`swapoff -a` and `echo 3 > /proc/sys/vm/drop_caches` are dangerous in production** — they don't free memory, they just force the kernel to re-fault pages. Useful for diagnosis, not for solving the problem.
- **Process RSS is not process memory**. RSS counts pages mapped; the same page can be mapped by multiple processes (shared libs). For true memory cost, check `/proc/<pid>/smaps_rollup`. For quick triage, RSS is fine.
- **A single process at 5% memory on a 7 GiB host uses 350 MiB**. Don't dismiss "small" percentages on small-memory hosts.
- **Don't conclude "thermal shutdown" from a single crash.** Confirm with the boot-loop pattern in `boot_watch.log` and the load/temp correlation in `power_watch.log` (see `references/thermal-and-cpu-pressure.md`).
- **Don't trust `docker stats` CPU% for the daemon itself.** A container at 0% CPU can still be the root cause if its healthcheck is in a fail loop. Check `ps -eo pcpu,comm | awk '/dockerd|containerd/'` for total daemon CPU.

## Verification after cleanup

```bash
uptime                          # load should drop
free -m                         # MemAvailable should grow
ps -eo pid,rss,comm --sort=-rss | head -10  # new top consumers
# Verify the leak source is fixed, not just temporarily reduced
pgrep -c <leaked-process-name>   # should be 0 or stable-not-growing
```

If load stays high after the leak is fixed, the system is doing real work (reclaim, dirty page writeback) — give it 2-3 minutes before judging.

## See also

- `references/chromium-mcp-leak.md` — worked example of diagnosing the TradingView chart MCP leak (970 MiB/instance browser pool) end-to-end on a 7.7 GiB host.
- `references/thermal-and-cpu-pressure.md` — sibling playbook for thermal/CPU pressure. Same diagnostic methodology, different signals. Covers: BIOS emergency cut at 88-90°C, Docker healthcheck fail loops (FailingStreak signature), cloudflared reconnect loop signature in `docker logs`, `boot_watch.log` boot-loop pattern, `power_watch.log` load/temp correlation, thermald + schedutil governor mitigation, and disk-space triage order.