# Chromium-based MCP server leak — worked example

Real session on 2026-06-17: a `tradingview-chart-mcp` was leaking 7.6 GB of memory on a 7.7 GiB host, causing the system to hang twice in one day (manual power-off required).

## Symptom

- Load average 4-13 (1m / 5m) on a 2-core box
- SSH login timed out
- `free -m` showed `MemAvailable: 1210 MiB` and `Swap: 3056 MiB / 5999 MiB used`
- `dmesg --since "10 minutes ago" | grep memory pressure` showed 11 occurrences of `Under memory pressure, flushing caches` in 3 minutes
- Browser tabs wouldn't load, gateway stopped responding

## What we initially thought was wrong

- Python upload script running concurrently — looked like the trigger, but the script only used ~700 MiB of working set
- Multiple Docker containers running — each was small (60-110 MiB)
- Chromium processes — there were 96 of them at ~150-200 MiB each, totaling ~2.8 GiB. But chromium is normal on this machine, so this wasn't the smoking gun by itself

## What was actually leaking

A `tradingview-chart-mcp` MCP server (browser-pool architecture) had spawned 12 chromedriver processes (each managing 7-8 chromium children) that had been orphaned across multiple MCP server restarts. Total leaked: 7.6 GiB.

The MCP server used a "browser pool" for performance:
```python
def _initialize_browser_pool(self):
    for i in range(self.max_concurrent):  # max_concurrent=4 default
        scraper = TradingViewScraper(...)
        scraper._setup_driver()
        self.browser_pool.append(scraper)
```

Per instance: 4 browsers × (1 chromedriver + 7 chromium + 2 crashpad) ≈ 970 MiB permanently allocated. With 5 chart MCP instances running (Hermes spawns one per dashboard/gateway process), total = 4.85 GiB just for this one MCP.

## How we found it

```bash
# 1. Confirmed memory pressure
free -m
# → Swap: 3.0 GiB used, only 250 MiB free

# 2. Found chromium processes with suspicious flags
ps -eo pid,args | grep chromium | grep -v grep | head -5
# → all had `--headless --test-type=webdriver --user-data-dir=/tmp/org.chromium.Chromium.scoped_dir.XXXX`
# → these are NOT user browser tabs, they're chromedriver-spawned test instances

# 3. Traced parents to find the spawner
for p in $(pgrep chromedriver); do
  ppid=$(awk '/^PPid:/{print $2}' /proc/$p/status)
  echo "chromedriver $p → parent $ppid: $(tr '\0' ' ' < /proc/$ppid/cmdline | cut -c1-100)"
done
# → all parents were python processes running main_optimized.py from tradingview-chart-mcp
```

## Fix applied (in three layers)

### Layer 1 — patch the MCP server itself

Files: `main_optimized.py` and `tview_scraper.py` in the MCP directory.

`tview_scraper.py` — track our own user-data-dir so we can clean it deterministically:
```python
def _setup_driver(self):
    # ... existing options ...
    import uuid
    self._user_data_dir = f"/tmp/tvscraper-{uuid.uuid4().hex[:12]}"
    chrome_options.add_argument(f"--user-data-dir={self._user_data_dir}")
    # ... rest of method

def close(self):
    # ... existing driver.quit() ...
    if getattr(self, "_user_data_dir", None):
        import shutil
        if os.path.isdir(self._user_data_dir):
            shutil.rmtree(self._user_data_dir, ignore_errors=True)
```

`main_optimized.py` — register cleanup on init, on signal, and force-kill any orphans:
```python
def __init__(self, max_concurrent=4, config=None):
    # ... existing init ...
    self._shutting_down = False
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
        import subprocess
        subprocess.run(
            ["pkill", "-9", "-P", str(os.getpid()), "-f", "chromedriver"],
            timeout=2, capture_output=True)
    except Exception:
        pass
```

### Layer 2 — disable the MCP at config level (user wanted this for now)

```bash
hermes config set mcp_servers.tradingview-chart.enabled false
```

This writes to `/root/.hermes/config.yaml` (user override layer, takes precedence over project config). Entry preserved — easy to re-enable with `hermes config set mcp_servers.tradingview-chart.enabled true`.

### Layer 3 — kill the running chart MCPs (config change doesn't auto-reload)

```bash
PIDS=$(pgrep -f "tradingview-chart-mcp/main_optimized.py")
for p in $PIDS; do kill -TERM $p; done
```

Used SIGTERM (not SIGKILL) so the new signal handler could run cleanup. Verified each kill removed 4 `/tmp/tvscraper-*` dirs and freed ~970 MiB.

## What went wrong (in the original MCP code)

1. The MCP imported `atexit` but never called `atexit.register()` on the cleanup method
2. No signal handlers for SIGTERM/SIGINT/SIGHUP
3. `chromedriver` defaults to a random scoped user-data-dir (`/tmp/org.chromium.Chromium.scoped_dir.<6hex>`) that the application code can't easily find to clean up
4. The browser pool (max_concurrent=4) was sized for production servers with 32+ GiB RAM. On a 7.7 GiB host, one instance consumed 970 MiB permanently

## Memory before/after

| | Before | After | Delta |
|---|---|---|---|
| Free RAM | 121 MiB | 2,504 MiB | +2,383 MiB |
| Chromium processes | 96 | 12 | -84 |
| Chromedriver | 12 | 12 (replaced with clean) | 0 |
| /tmp/org.chromium.Chromium.scoped_dir.* | 13 | 0 | -13 |
| /tmp/tvscraper-* (new pattern) | 0 | 0 (cleaned by signal handler) | n/a |

On next Hermes restart (when disabled config takes full effect): chart MCPs won't spawn at all, freeing another ~2.9 GiB. Projected free RAM: ~5.4 GiB.

## Lessons for next time

- Any MCP server using Selenium/Playwright + headless Chrome MUST register `atexit` and signal handlers. Importing the module is not enough.
- Browser pool MCP servers scale linearly in memory with `max_concurrent`. On small-memory hosts, set `--max-concurrent=1` or `--disable-pooling` even if it's slower per call.
- "High CPU at idle" can be swap-in activity, not real work. `vmstat 1 5` and look at the `si` column (swap-in).
- A new MCP server should have its memory budget documented and its cleanup verified before being added to a small-memory production host.
