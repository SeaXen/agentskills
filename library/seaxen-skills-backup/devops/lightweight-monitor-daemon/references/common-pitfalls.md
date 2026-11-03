# Common pitfalls — daemon + web + systemd + notifier

Distilled from real debugging sessions (mostly systor + chromium leak diagnosis). Pitfall → symptom → fix.

## Pitfall: `pkill -f "pattern"` kills your own bash

**Symptom:** You run `pkill -9 -f "chromium"` to kill chromium processes. Your terminal dies immediately with `-9` or `-15`. Subsequent commands fail because the shell session was killed.

**Root cause:** `pkill -f` matches against the **full command line**. Your bash command line contains the pattern as an argument:

```
bash -c '... pkill -9 -f chromium ...'
```

The pattern `chromium` matches your own bash process, so pkill kills the shell running the kill command. Death spiral.

**Fix:** Use `pgrep -x` (exact process name match) instead:

```bash
# Wrong — matches your own bash
pkill -9 -f "chromium"

# Right — only matches processes named exactly "chromium"
PIDS=$(pgrep -x chromium)
for p in $PIDS; do kill -9 $p; done

# Same fix for other names
pgrep -x chromedriver | xargs kill -9
pgrep -x chrome_crashpad | xargs kill -9
```

If you must use `-f`, exclude your own PID:

```bash
pkill -9 -f "chromium" --ignore-pid $$
# Or via pgrep:
PIDS=$(pgrep -f "chromium" | grep -v "^$$\$")
for p in $PIDS; do kill -9 $p; done
```

**Lesson:** `pgrep -x <name>` (exact match on `comm` field) is almost always safer than `pkill -f <pattern>` (regex match on full `cmdline`).

---

## Pitfall: TCP CLOSE-WAIT hides a stalled upload

**Symptom:** You see "200 Mbit/s" in your progress bar, but only 720 MB ever reaches the server. After a few minutes, the upload stalls. `ps` shows the process alive but `ss -tnp` shows the socket in `CLOSE-WAIT`.

**Root cause:** Python's `urllib.request.urlopen()` with a file as `data=` parameter accepts the entire file body into the local TCP buffer, then streams from buffer to socket. If the remote server sends `FIN` (connection half-close), the local buffer keeps draining bytes that the kernel accepts but never actually transmits. Your progress bar counts bytes-read-from-file, not bytes-written-to-remote.

**Fix:** Instrument I/O via `/proc/<pid>/io`:

```bash
# Read the actual bytes-read-from-disk vs bytes-written-anywhere
cat /proc/<pid>/io
#   rchar: ...    (bytes read via read() syscall)
#   wchar: ...    (bytes written via write() syscall)
#   read_bytes: ...   (actual disk reads)
#   write_bytes: ...  (actual disk writes — should be 0 for network upload)
```

For real network throughput:
```bash
# Use ss with byte counters instead of /proc/net/dev
ss -ti dst <server_ip> | grep -oP 'cwnd:\d+|rtt:\d+\.\d+'
# Or use nload / iftop for live bandwidth
```

**Lesson:** Local progress bars are not network throughput. Verify with `/proc/<pid>/io` and `ss -tnp` socket state before declaring "the upload is fast".

---

## Pitfall: stdout buffering hides log output

**Symptom:** You run `python3 daemon.py | tee logfile`. The logfile is empty for hours. Then suddenly all the log lines appear at once.

**Root cause:** Python defaults to **block buffering** for non-TTY stdout. When piped to `tee`, stdout is not a TTY, so Python buffers up to 4 KB before writing. The `tee` command also buffers its output.

**Fix:** Use `python3 -u` (unbuffered) OR write directly to a file with `logging.FileHandler`:

```python
# Option 1: unbuffered Python
import sys
sys.stdout.reconfigure(line_buffering=True)
# Or run as: python3 -u daemon.py

# Option 2: log directly to file
logging.basicConfig(
    handlers=[
        logging.FileHandler("/var/log/<app>/<app>.log"),
        logging.StreamHandler(sys.stdout),  # also goes to stdout
    ],
)
```

For the systemd unit, prefer `StandardOutput=append:/var/log/<app>/collector.log` so systemd itself handles the file write and you don't depend on buffering.

**Lesson:** Always use `-u` for long-running Python piped to anything, OR write logs directly with `logging.FileHandler` and bypass `tee`.

---

## Pitfall: `signal.signal()` only works in main thread

**Symptom:** You install a SIGTERM handler in a worker thread. The process doesn't shut down on SIGTERM, or the handler is never called.

**Root cause:** `signal.signal()` is a main-thread-only operation in CPython. If you call it from a thread, it raises `ValueError: signal only works in main thread of the main interpreter`.

**Fix:** Install signal handlers in `__main__`, not in worker threads:

```python
# daemon.py
def run():
    # install signals HERE, not at import time
    signal.signal(signal.SIGTERM, handle_term)
    signal.signal(signal.SIGINT, handle_term)
    while _running:
        ...

if __name__ == "__main__":
    run()
```

**Lesson:** All signal setup must happen in the function called from `__main__`, never at module-import time or in a worker thread.

---

## Pitfall: SQLite without WAL under high write load

**Symptom:** SQLite throws `OperationalError: database is locked` when multiple processes or threads try to write. Writes slow down as DB grows.

**Root cause:** Default SQLite journal mode is `DELETE` — every write acquires an EXCLUSIVE lock on the entire DB. With multiple writers or long-running transactions, contention piles up.

**Fix:** Enable WAL mode + normal sync:

```python
import sqlite3
conn = sqlite3.connect("/var/lib/<app>/<app>.db", timeout=10)
conn.execute("PRAGMA journal_mode=WAL")  # readers don't block writers
conn.execute("PRAGMA synchronous=NORMAL")  # ~1s durability loss on power loss
```

**Trade-off:** WAL uses a separate `-wal` file. You need to back up both `<db>.db` and `<db>.db-wal` together.

**Lesson:** For write-heavy workloads (time-series monitoring, logging), always use WAL + NORMAL sync.

---

## Pitfall: `config.yaml` writes fail with PermissionError

**Symptom:** Your daemon's web UI shows "could not save config: [Errno 13] Permission denied" when the user clicks Save in /settings.

**Root cause:** The config file is owned by root (set by `install.sh`), but the web service runs as the user (systemd user service). The user can't write to a root-owned file.

**Fix:** Either:
1. Run the web service as root (defeats the purpose of user services)
2. Have the config owned by the user, but writable only via `sudo` (UX pain)
3. Have the web UI POST to a small helper binary that's `setuid root` for the config write only (best UX, smallest attack surface)
4. Use a separate writable config (e.g. `~/.config/<app>/user.yaml` merged with `/etc/<app>/config.yaml`) so the user layer is writable

For systor v0.1.0 we went with option 4:

```python
CONFIG_PATHS = [
    Path("/etc/systor/config.yaml"),         # root-owned, read-only for user
    Path.home() / ".config/systor/config.yaml",  # user-owned, writable
]
```

**Lesson:** Two-layer config (system + user) is a clean pattern. User layer wins on save, system layer wins on read. No sudo needed.

---

## Pitfall: `subprocess.run()` inherits the full environment

**Symptom:** A child process started via `subprocess.run()` has access to all your secrets (API keys, tokens, paths).

**Root cause:** By default, `subprocess.run()` inherits the parent's full environment. If your daemon runs with `BITWARDEN_SECRETS=...` or `HERMES_API_KEY=...`, those leak to every child.

**Fix:** Pass an explicit minimal `env` dict:

```python
import os, subprocess
subprocess.run(
    ["/usr/bin/python3", "child_script.py"],
    env={"PATH": os.environ["PATH"], "HOME": os.environ.get("HOME", "")},
    # No API keys passed unless the child specifically needs them
)
```

Or use `env=` with `**os.environ, "MY_SPECIFIC_KEY": value}` for an explicit allowlist.

**Lesson:** Always pass an explicit `env=` to subprocess if the child doesn't need all your secrets. Default inheritance is a security footgun.

---

## Pitfall: Long-lived Python threads never release GIL

**Symptom:** Your daemon has 8 CPU cores but uses only 1. CPU-bound work in a thread doesn't get parallelized.

**Root cause:** CPython's GIL (Global Interpreter Lock) means only one thread can execute Python bytecode at a time. Threads are good for I/O-bound work (network, disk), bad for CPU-bound.

**Fix:** Use `multiprocessing` for CPU-bound work, or accept that your single-threaded daemon is I/O-bound (which is fine for monitoring).

**Lesson:** For monitoring daemons (mostly waiting on `/proc` and HTTP), threads are fine. Don't try to parallelize polling across cores — the overhead exceeds the gain.

---

## Pitfall: `time.sleep()` doesn't break on SIGTERM

**Symptom:** You send SIGTERM to your daemon. It doesn't exit for 30 seconds (the full poll interval). systemd kills it with `SIGKILL` after `TimeoutStopSec`, then marks it as `failed`.

**Root cause:** `time.sleep(N)` is uninterruptible in the sense that SIGTERM handler runs but the sleep doesn't return early in older Python. (Python 3.11+ improved this.)

**Fix:** Use granular sleep with frequent checks:

```python
# Wrong — sleeps full interval, SIGTERM doesn't break it
while _running:
    do_work()
    time.sleep(poll_interval)

# Right — checks _running flag every second
while _running:
    do_work()
    for _ in range(poll_interval):
        if not _running: break
        time.sleep(1)
```

**Lesson:** Use `for _ in range(N): if not _running: break; time.sleep(1)` instead of `time.sleep(N)` for interruptible waits.

---

## Pitfall: `__pycache__/` pollutes git

**Symptom:** You `git add .` and end up committing hundreds of `__pycache__/*.pyc` files.

**Fix:** Already in the systor `.gitignore`:

```
__pycache__/
*.py[cod]
*$py.class
```

**Lesson:** Always include `__pycache__/` in `.gitignore` for Python projects.

---

## Pitfall: `restart=on-failure` lets transient errors become death spirals

**Symptom:** Your daemon crashes. systemd restarts it. It crashes again immediately. systemd restarts it. After 5 crashes in 10 seconds, systemd gives up and marks the service failed.

**Fix:** Use `StartLimitBurst` and `StartLimitIntervalSec`:

```ini
[Service]
Restart=always
RestartSec=10
StartLimitBurst=5
StartLimitIntervalSec=120
```

This says "restart up to 5 times in 120 seconds, then give up". Prevents a tight crash loop.

**Lesson:** Always pair `Restart=always` with `StartLimitBurst` to prevent death spirals.

---

## Pitfall: `os.path.exists()` lies for symlinks and broken paths

**Symptom:** `os.path.exists("/proc/some-nonexistent-file")` returns `False`. You log "file not found". But the path exists in the kernel and would return data if you read it.

**Fix:** Use `os.stat()` and catch `FileNotFoundError`, or use pathlib's `Path.is_file()` (which follows symlinks differently).

**Lesson:** For /proc and /sys, always wrap reads in try/except and return `None` on error. Don't trust `exists()` for kernel filesystems.

---

## Pitfall: HTTP `localhost` vs `127.0.0.1` vs `0.0.0.0`

**Symptom:** Your dashboard works on the host but not from another machine on the LAN. Or your dashboard is accessible from the internet and you didn't mean it to be.

**Root cause:**
- `localhost` might resolve to `::1` (IPv6) or `127.0.0.1` (IPv4) depending on `/etc/hosts` and IPv6 status
- `127.0.0.1` is loopback only — accessible from the host itself
- `0.0.0.0` binds to **all** interfaces — accessible from anywhere

**Fix:** Default to `127.0.0.1` (loopback only). To expose to LAN, bind to the LAN IP. Never bind to `0.0.0.0` without a reverse proxy + auth.

```python
# Default — loopback only
"web": {"host": "127.0.0.1", "port": 6677}

# LAN only — find your IP and bind to it
"web": {"host": "192.168.1.100", "port": 6677}

# Internet — REQUIRES reverse proxy + auth
"web": {"host": "0.0.0.0", "port": 6677}  # don't do this without auth
```

**Lesson:** Default `127.0.0.1`. Be explicit when you mean LAN. **Match the deployment context:** for a small LAN-only host behind a home router, `0.0.0.0` is the normal pattern (the user explicitly asks for "open in lan port" and trusts the NAT as the perimeter). Do **not** pre-add auth tokens, `lan_only` IP gates, JWT masks, or token-regeneration buttons unless the user asks — that was the over-engineering pattern that triggered "revert back if you do anything wrong" in systor's v0.2 refactor. For internet-facing deployments, multi-user servers, or anything outside a trusted-LAN scenario, the rule flips: those need reverse proxy + auth + TLS, and `0.0.0.0` without auth is genuinely wrong. Same code, two opposite defaults — read the deployment first.

---

## Pitfall: `shutil.disk_usage()` hangs forever on FUSE/autofs mounts

**Symptom:** `/api/storage/mounts` (or any endpoint that enumerates disks) occasionally hangs for 60+ seconds. curl times out. The browser tab shows "infinity load" until you kill the request. On a Linux box that mounts anything over FUSE (rclone, sshfs, google-drive-ocamlfuse, mergerfs, snapfuse, etc.) or has `autofs` entries that haven't been triggered yet, this fires intermittently. Sometimes the same endpoint returns in 3ms; sometimes it locks up.

**Root cause:** `shutil.disk_usage(path)` is `statvfs()` under the hood. On a hung FUSE mount, the user-space driver process can block indefinitely while waiting for the network or the remote backend (e.g. rclone waiting on a flaky Google Drive API). The kernel forwards `statvfs` to the FUSE driver and waits forever. `findmnt`-based enumeration compounds this: it surfaces all `autofs` / `fuse.*` mountpoints as "live", and your endpoint dutifully calls `disk_usage` on each one.

**Fix:** Two changes together — neither alone is enough:

1. **Hardcode the candidate mount list.** Do not enumerate. Pick the 2–3 mounts you actually want to surface (e.g. `/`, `/mnt/tb`, `/root`) and stop there. Anything reachable through `findmnt` is a potential hang source.

2. **Wrap every `shutil.disk_usage()` call in a thread with a hard timeout.** Return `unavailable: true` on timeout instead of blocking:

```python
import threading, shutil
from pathlib import Path

def _disk_usage_bounded(path: Path, timeout: float = 2.0):
    """statvfs can hang forever on hung FUSE mounts. Thread + timeout."""
    box: dict = {}
    def _run():
        try:
            u = shutil.disk_usage(str(path))
            box["ok"] = (u.total, u.used, u.free)
        except Exception as e:
            box["err"] = str(e)
    t = threading.Thread(target=_run, daemon=True)
    t.start(); t.join(timeout)
    if t.is_alive():
        return None  # FUSE driver is hung — caller returns "unavailable"
    return box.get("ok")

def mount_payload(path: Path) -> dict:
    usage = _disk_usage_bounded(path, timeout=2.0)
    if usage is None:
        return {"mount": str(path), "unavailable": True,
                "total": 0, "used": 0, "free": 0, "used_pct": 0}
    total, used, free = usage
    return {"mount": str(path), "total": total, "used": used,
            "free": free, "used_pct": round(used / total * 100, 1) if total else 0}
```

**Lesson:** Any syscall that crosses into a user-space filesystem driver (FUSE, autofs, sshfs, rclone, snap, flatpak) can hang indefinitely. `shutil.disk_usage`, `os.stat`, `os.walk`, `open`, `listdir` — all inherit the driver's worst-case latency. Always thread+timeout these when they cross an HTTP request boundary. Never let an HTTP request's fate depend on a user-space driver's responsiveness.

---

## Pitfall: Expensive cold-cache endpoints need a background refresher

**Symptom:** First call to `/api/expensive` takes ~2s. Subsequent calls in the same 2s window are instant (<5ms). User navigates away for 3s, navigates back, gets the 2s wait again. From the user's seat: "the app feels slow / sometimes loads like infinity". Measured: `time_total=2.07s` cold, `time_total=0.001s` warm.

**Root cause:** The endpoint does expensive fan-out work (psutil.cpu_percent for many processes, docker stats for many containers, findmnt + statvfs, network sampling, etc.) **synchronously inside the request handler**. A short cache TTL (e.g. 2s) means any pause longer than the TTL re-triggers the cold path. The "instant warm" path feels great; the "2s cold" path feels broken. Net impression: the app is unreliable.

**Fix:** Two changes together. Either alone leaves a window where the request blocks:

1. **Background refresher thread** that pre-warms the cache every N seconds (4s is the sweet spot for human-perceived "instant"):

```python
_cache = {"ts": 0.0, "rows": []}
_cache_lock = threading.Lock()

def _refresh_worker():
    while True:
        try:
            rows = _expensive_fanout()  # psutil + docker + findmnt etc.
            with _cache_lock:
                _cache["ts"] = time.time()
                _cache["rows"] = rows
        except Exception:
            pass  # keep the old cache rather than poisoning it
        time.sleep(4.0)

threading.Thread(target=_refresh_worker, name="<app>-cache", daemon=True).start()
```

2. **Bump the cache TTL** to match or slightly exceed the refresher interval (e.g. 6s for a 4s refresher). The 2s gap lets the refresher race ahead and prevents serving stale-then-stale.

```python
if cached_ts > 0 and time.time() - cached_ts < 6.0 and cached_rows:
    return jsonify({"rows": cached_rows})  # always served from cache
# cold-start fallback only fires during the first ~4s after process start
rows = _expensive_fanout()
```

**Why both:** The refresher alone leaves a ~4s cold window at process start. The TTL alone leaves a "stale but cached" wall — any navigation gap longer than the TTL re-triggers the cold path. Together, the request always hits cache after the first 4s, and the user never sees a blocking request.

**Lesson:** For endpoints whose cold-path work costs >100ms (anything involving psutil, docker, findmnt, glob over a large tree, database queries with joins), the right pattern is **background refresh + TTL ≥ refresh interval**. The TTL alone is a false economy — it looks like caching but the user still feels the cold cost on every navigation.

**Debugging recipe when an endpoint "feels slow":**
1. Time the endpoint from the host: `for i in 1..5; do curl -w '%{time_total}\n' -o /dev/null http://localhost/api/x; done`
2. If first call is >> rest, it's a cold-cache problem → background refresher + TTL
3. If every call is slow, the cold path is doing too much → narrow the fan-out (limit, sample, timebox)
4. If calls hang >5s, a syscall is blocked → thread+timeout wrapper, especially on FUSE/autofs

---

## Pitfall: Recursive size walks inside file-manager listings

**Symptom:** `/api/storage/browse` on a folder with 30+ subdirectories takes ~2 seconds per request. The folder's direct contents are small (a handful of files) — the slowness is in computing subdirectory sizes for the listing. User clicks a folder, waits 2s, sees it open. Feels like "Storage is slow / sometimes infinity load".

**Root cause:** `_entry_payload(child)` calls a recursive `_dir_size_limited(child, 400)` for every subdirectory to show its size in the listing. With 30 subdirectories × 400 files each, that's 12000+ `stat()` calls per request. Worst case: a deeply nested knowledge base (e.g. medical chapter tree) trips this on every folder click.

**Fix:** File-manager listings should compute sizes as **immediate-children-only** using `os.scandir()`. Reserve recursive walks for an explicit on-demand Deep Scan action that the user invokes:

```python
def dir_size_immediate(path: Path) -> tuple[int, int, int]:
    """O(1) syscalls per entry. Fast enough for every listing."""
    total = files = dirs = 0
    try:
        with os.scandir(path) as it:
            for entry in it:
                try:
                    if entry.is_symlink():
                        continue
                    if entry.is_file(follow_symlinks=False):
                        total += entry.stat(follow_symlinks=False).st_size
                        files += 1
                    elif entry.is_dir(follow_symlinks=False):
                        dirs += 1
                except Exception:
                    continue
    except Exception:
        pass
    return total, files, dirs

def _entry_payload(p: Path) -> dict:
    try: st = p.lstat()
    except Exception: st = None
    typ = "symlink" if p.is_symlink() else "dir" if p.is_dir() else "file"
    size = 0
    if typ == "file" and st:
        size = st.st_size
    elif typ == "dir":
        size, _f, _d = dir_size_immediate(p)  # NOT recursive
    return {"name": p.name, "path": str(p), "type": typ, "size": size,
            "mtime": st.st_mtime if st else 0,
            "mtime_text": _fmt_ts(st.st_mtime if st else 0)}
```

For Deep Scan, keep the recursive walker available — just don't call it from the listing endpoint:

```python
def dir_size_recursive(path: Path, max_files: int = 200_000) -> tuple[int, int, int]:
    total = files = dirs = 0; seen = 0
    try:
        for root, dnames, fnames in os.walk(path):
            dirs += len(dnames)
            for name in fnames:
                seen += 1
                if seen > max_files:
                    return total, files, dirs
                try:
                    fp = Path(root) / name
                    if fp.is_symlink(): continue
                    total += fp.stat().st_size; files += 1
                except Exception: continue
    except Exception: pass
    return total, files, dirs
```

**Also avoid triple-`lstat()`** per entry in the listing loop — old code did `is_file()` + `lstat()` + `lstat()` + `lstat()` (size + mtime + mtime_text) per child. Single `lstat()` then read fields off the result.

**Lesson:** File-manager listings must be O(1)-per-entry. Recursive walks belong in on-demand analysis tools (Deep Scan / Tree Size / etc.), not in the browse endpoint. Same rule applies to file counts, search results, glob enumeration, anything shown "as you browse" — keep the deep version behind an explicit user action.
