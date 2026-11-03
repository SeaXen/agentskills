# /proc-based metrics without psutil

For systor's v0.3.0 the user asked for **CPU usage %, disk I/O load, and top processes by CPU/memory** — and said "if it not make app heavy". Pulling in `psutil` (~3 MB compiled, plus ~50 MB during build) violated the lightweight ethos. All three metrics can be read from `/proc` and `/sys` directly with stdlib only.

This reference is the canonical recipe for delta-based metrics from kernel filesystems.

## The shared pattern: module-level state + delta between calls

CPU%, disk I/O rates, and per-process CPU% all need **two samples to compute a rate**. Keep the previous sample in a module-level variable, compute the delta on each call.

```python
# At module top
_prev_cpu: tuple[int, int] | None = None  # (total, idle)

def cpu_percent() -> float | None:
    """% CPU between the previous and current call. First call returns None."""
    global _prev_cpu
    total, idle = _read_cpu_stat()           # fast (~0.1 ms)
    prev = _prev_cpu
    _prev_cpu = (total, idle)
    if prev is None:
        return None                          # no baseline yet
    dt = total - prev[0]
    di = idle - prev[1]
    if dt <= 0:
        return 0.0
    return round(100.0 * (dt - di) / dt, 1)
```

Important rules:
- **No per-call `time.sleep()`** — sleep adds the sample-interval cost and biases the rate when you're not actually measuring a quiet interval.
- **First call returns None** — caller renders `—` in UI; do not return `0.0` (which falsely claims "0% CPU right now").
- **State is process-local** — if you run multiple workers (gunicorn), each has its own baseline. Acceptable for a 2-thread waitress.
- **Caller pre-warms** — in the daemon startup, call once before entering the main loop so the first user request has data.

## CPU% from `/proc/stat`

`/proc/stat` first line: `cpu  user nice system idle iowait irq softirq steal guest guest_nice`

```python
def _read_cpu_stat() -> tuple[int, int]:
    line = Path("/proc/stat").read_text().splitlines()[0]
    vals = [int(x) for x in line.split()[1:]]
    total = sum(vals)
    # idle + iowait = "not doing work"
    idle = vals[3] + (vals[4] if len(vals) > 4 else 0)
    return total, idle
```

Per-core CPU% is the same pattern reading `/proc/stat` lines 2+ (`cpu0`, `cpu1`, ...). Combine for total.

## Disk I/O from `/proc/diskstats`

`/proc/diskstats` line format (14+ fields): `major minor name reads_completed reads_merged sectors_read time_reading writes_completed writes_merged sectors_written time_writing ...`

Sectors are always 512 bytes (regardless of physical/logical sector size — the kernel reports the latter via `sectors_written` regardless of `lsblk` output).

```python
def _read_diskstats_raw() -> dict[str, tuple[int, int]]:
    """Return {device_name: (read_sectors, write_sectors)} for whole disks only."""
    out = {}
    for line in Path("/proc/diskstats").read_text().splitlines():
        parts = line.split()
        if len(parts) < 14:
            continue
        name = parts[2]
        # Skip pseudo / virtual devices
        if any(name.startswith(p) for p in ("loop", "ram", "dm-", "md", "sr", "zd", "nbd", "fd")):
            continue
        # Skip partitions: keep whole disks only (sda, not sda1; nvme0n1, not nvme0n1p1)
        if name.startswith(("sd", "vd", "hd", "xvd")) and name[-1].isdigit():
            continue
        if name.startswith("nvme"):
            tail = name.rsplit("p", 1)[-1]
            if tail.isdigit():
                continue
        out[name] = (int(parts[5]), int(parts[9]))  # sectors read, sectors written
    return out

_prev_disk: dict[str, tuple[int, int]] = {}
_last_disk_ts: float = 0.0

def disk_io_mbps() -> dict:
    """{read_mbps, write_mbps, devices: [{name, read_mbps, write_mbps}]}."""
    global _prev_disk, _last_disk_ts
    cur = _read_diskstats_raw()
    prev = _prev_disk
    now = time.time()
    elapsed = now - _last_disk_ts if _last_disk_ts else 0
    _prev_disk = cur
    _last_disk_ts = now
    if not prev or elapsed <= 0:
        return {"read_mbps": 0.0, "write_mbps": 0.0, "devices": []}
    devs, total_r, total_w = [], 0.0, 0.0
    for name, (r, w) in cur.items():
        if name in prev:
            pr, pw = prev[name]
            r_mbps = (max(0, r - pr) * 512) / elapsed / (1024 * 1024)
            w_mbps = (max(0, w - pw) * 512) / elapsed / (1024 * 1024)
            devs.append({"name": name, "read_mbps": round(r_mbps, 3), "write_mbps": round(w_mbps, 3)})
            total_r += r_mbps; total_w += w_mbps
    return {"read_mbps": round(total_r, 3), "write_mbps": round(total_w, 3), "devices": devs}
```

Common bugs in the filter:
- `name[-1].isdigit()` filters `sda1` but lets `sda` through — correct.
- `name.startswith("nvme")` alone is wrong — it accepts `nvme0n1` AND `nvme0n1p1`. The `p1` check is mandatory.
- Forgetting the `>= 14` length check — `/proc/diskstats` lines for some virtual devices are shorter and would IndexError.

## Top processes from `/proc/<pid>/stat`

The `/proc/<pid>/stat` file has 52 fields. The tricky one is `comm` (field 2) — it's the **process name in parens** and **may contain spaces and parens**:

```
1234 (node) S 1 1234 1234 0 -1 4194560 ...
```

You must split on the **last** `)` to handle names like `(node --inspect=0)` correctly.

```python
def _read_proc_stat(pid: int):
    try:
        with open(f"/proc/{pid}/stat", "rb") as f:
            data = f.read().decode(errors="replace")
        lparen = data.index("(")
        rparen = data.rindex(")")          # rindex, not index — handles spaces/parens
        comm = data[lparen + 1:rparen]
        rest = data[rparen + 2:].split()
        # Field indices in `rest` (after "comm) state"):
        #   rest[0]=state  rest[1]=ppid  rest[2]=pgrp  rest[3]=session
        #   rest[4]=tty_nr rest[5]=tpgid rest[6]=flags rest[7]=minflt
        #   rest[8]=cminflt rest[9]=majflt rest[10]=cmajflt rest[11]=utime  ← clock ticks
        #   rest[12]=stime ← clock ticks    rest[13]=cutime rest[14]=cstime
        #   ...    rest[21]=rss (in pages) rest[22]=...
        utime = int(rest[11])
        stime = int(rest[12])
        rss_pages = int(rest[21])
        return comm, utime, stime, rss_pages
    except Exception:
        return None
```

CPU% formula:

```python
clk_tck = os.sysconf("SC_CLK_TCK") or 100
elapsed_sec = now - last_scan_ts         # wall-clock between scans
cpu_pct = 100.0 * ((utime - prev_utime) + (stime - prev_stime)) / clk_tck / elapsed_sec
```

Memory RSS:
- `/proc/<pid>/stat` field 24 (1-indexed) = `rss` in **pages** (typically 4 KB).
- `mem_mb = rss_pages * page_size / (1024 * 1024)`.

For process command line (used as `title` tooltip):
```python
cmdline = Path(f"/proc/{pid}/cmdline").read_bytes().replace(b"\x00", b" ").decode(errors="replace").strip()
```

### Performance cost

For ~250 processes, this loop takes ~5 ms — acceptable for a one-off scan every 30 seconds. To keep the UI snappy, **do not call from the request handler**; cache the result in the web app's module state and refresh on a separate timer.

### First call returns 0% for everything

Because there's no previous baseline, the first call cannot compute a delta. Mitigation: **pre-warm in the daemon** by calling once at startup so the web endpoint's first user call has real data:

```python
# In collector.py run()
from .metrics import read_top_processes
read_top_processes(n=1, by="cpu")   # populates _prev_proc baseline
log.info("collector: pre-warmed process CPU baseline")
```

## Refresh / range / pause persisted in localStorage

For a dashboard that lets users pick refresh interval and time range:

```js
const SETTINGS_KEY = 'systor.dashboard';
let settings = { refreshMs: 5000, rangeHours: 6, paused: false };
try { settings = { ...settings, ...JSON.parse(localStorage.getItem(SETTINGS_KEY) || '{}') }; } catch {}

function saveSettings() { localStorage.setItem(SETTINGS_KEY, JSON.stringify(settings)); }

// On control change
refreshSel.addEventListener('change', () => {
  settings.refreshMs = parseInt(refreshSel.value);
  saveSettings();
  restartTimers();
});
```

Restart all `setInterval` timers after a change so the new interval takes effect immediately without a page reload.

## Pitfalls

- **Don't `time.sleep()` inside the rate reader.** Use module-level previous-sample state and call twice (or pre-warm). Sleeping wastes a poll interval.
- **Don't return `0.0` when there's no baseline.** Return `None` and let the UI render `—`. False zeros are worse than honest dashes.
- **Don't split `/proc/<pid>/stat` on the first `)`.** Use `rindex` so names like `(my weird (name))` parse correctly.
- **Don't compute CPU% with `psutil.cpu_percent(interval=N)`** inside a request handler. That `N`-second sleep **inside the handler** stalls the UI for the full sample interval.
- **Don't add `psutil` to satisfy one metric.** `/proc` covers everything `psutil` does for these three metrics. Keep the dep tree small.
- **For nvme devices, the partition suffix is `p<n>`, not just `<n>`.** `nvme0n1p1` is a partition of `nvme0n1`. Filter accordingly.
- **Linux kernel always reports 512-byte sectors in `/proc/diskstats`** regardless of physical sector size. Don't multiply by `lsblk` output.
- **The `psutil` package is heavy** (~3 MB compiled, much more during build, requires `gcc`). For lightweight monitors that run on small VPS / Raspberry Pi / DietPi class hardware, the `pip install` step alone can take 30+ seconds. `/proc` is free.

## Reference

- `/mnt/tb/1Apps/systor/systor/metrics.py` — full implementation of all four readers (`_cpu_percent_delta`, `_read_diskstats_raw`, `read_disk_io_mbps`, `read_top_processes`)
- `/mnt/tb/1Apps/systor/systor/web.py` `api_top_processes` — `/api/top-processes?by=cpu|mem&n=10` endpoint
- `/mnt/tb/1Apps/systor/systor/templates/dashboard.html` — top-process tables + refresh/range dropdowns