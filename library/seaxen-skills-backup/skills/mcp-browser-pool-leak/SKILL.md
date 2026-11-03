---
name: mcp-browser-pool-leak
description: Diagnose and fix MCP servers that leak chromedriver/chromium/user-data-dir memory. Use when chromium/chromedriver counts grow without bound, when /tmp/org.chromium.Chromium.scoped_dir.* or /tmp/tvscraper-* dirs accumulate, when a specific MCP server holds 500+ MiB at idle, or when swap climbs despite no real workload.
---

# MCP Browser-Pool Memory Leak Diagnosis

Browser-pool-based MCP servers (selenium/playwright with pre-warmed browser instances) commonly leak memory. The pattern is repeatable across tradingview-chart-mcp, future chart/scraping MCPs, and any tool that uses `webdriver.Chrome(...)` in a pool.

## Symptom signature

- Chromium/chromedriver/chrome_crashpad processes with **high age** (40+ min) parented to either the MCP's python or systemd/init
- `/tmp/org.chromium.Chromium.scoped_dir.*` dirs accumulating without cleanup
- MCP python process holds 70 MB but its children hold 800+ MB
- Memory grows over time without restart
- Affected MCPs show as **Heaviest** in `ps --sort=-rss` despite doing no work

## Diagnostic steps

1. **Find the leaking MCP.** `ps -eo rss,args | grep -E "mcp|MCP" | sort -k1 -rn | head -10` — any MCP process whose children hold way more memory than the python wrapper.

2. **Trace the process tree.** For each high-RSS MCP, find its chromium children:
   ```bash
   pgrep -P <mcp_pid>          # direct children (chromedriver)
   pgrep -P <chromedriver_pid> # grandchildren (chromium)
   ```
   Count: 1 chromedriver → 7-9 chromium children → 1-2 chrome_crashpad. If `ps -eo etime` shows these are old (40+ min), they are orphans.

3. **Confirm the leak source.** Read the MCP code:
   - Look for `__init__` that calls `_setup_driver()` in a loop (browser pool pattern)
   - Check if `atexit.register(cleanup)` exists
   - Check if signal handlers exist for SIGTERM/SIGINT/SIGHUP
   - Check `cleanup()` — does it call `scraper.close()`? Does it kill child chromedriver?
   - Check `close()` — does it remove the user-data-dir?

   If any of those are missing, the MCP will leak.

## Required fix components

Any browser-pool MCP MUST have all of these to avoid leaks:

```python
import atexit, signal

# In __init__:
atexit.register(self.cleanup)
for sig in (signal.SIGTERM, signal.SIGINT, signal.SIGHUP):
    try: signal.signal(sig, self._signal_cleanup)
    except (ValueError, OSError): pass  # not in main thread

def _signal_cleanup(self, signum, frame):
    self.cleanup()
    signal.signal(signum, signal.SIG_DFL)
    os.kill(os.getpid(), signum)

def cleanup(self):
    if self._shutting_down: return
    self._shutting_down = True
    # Close all browsers
    for scraper in self.browser_pool:
        try: scraper.close()
        except Exception: pass
    # Belt-and-suspenders: kill any orphan child chromedriver/chromium
    try:
        subprocess.run(["pkill", "-9", "-P", str(os.getpid()), "-f", "chromedriver"], timeout=2, capture_output=True)
        subprocess.run(["pkill", "-9", "-f", "chromium.*--user-data-dir=/tmp/your-prefix-"], timeout=2, capture_output=True)
    except Exception: pass
    self.browser_pool.clear()
```

In the scraper's `_setup_driver`, set an explicit `--user-data-dir`:
```python
import uuid
self._user_data_dir = f"/tmp/your-prefix-{uuid.uuid4().hex[:12]}"
chrome_options.add_argument(f"--user-data-dir={self._user_data_dir}")
```

In `close()`, always remove the user-data-dir:
```python
import shutil
if getattr(self, "_user_data_dir", None):
    shutil.rmtree(self._user_data_dir, ignore_errors=True)
```

## Immediate cleanup (when fixing later)

To free memory now without restarting the MCP server:

```bash
# Kill orphan chromedriver (parent is defunct or systemd)
pgrep -x chromedriver | xargs -r kill -9

# Kill orphan chromium (parent is PID 1 or missing)
for p in $(pgrep chromium); do
  ppid=$(awk '/^PPid:/{print $2}' /proc/$p/status 2>/dev/null)
  if [ "$ppid" = "1" ] || [ ! -d "/proc/$ppid" ]; then kill -9 $p; fi
done

# Clean up leaked dirs
rm -rf /tmp/org.chromium.Chromium.scoped_dir.* /tmp/tvscraper-*
```

**Use `pgrep -x` (exact process name) NOT `pkill -f`** — the latter will match your own bash session if the search term appears anywhere in its command line.

## Verification

After applying the fix, do a kill cycle and watch the cleanup happen:
```bash
# Before
ls /tmp/tvscraper-* | wc -l  # e.g., 12

# Kill the MCP
kill -TERM <mcp_pid>
sleep 5

# After
ls /tmp/tvscraper-* | wc -l  # should be 0
pgrep chromedriver | wc -l   # should match MCP's pool size, not include old orphans
```

## Reference: tradingview-chart-mcp patch (2026-06-17)

Applied to `/mnt/tb/hermes/scripts/mcp-servers/tradingview-chart-mcp/`:
- `main_optimized.py`: atexit.register, SIGTERM/INT/HUP signal handlers, _signal_cleanup, expanded cleanup() with pkill
- `tview_scraper.py`: deterministic `--user-data-dir=/tmp/tvscraper-<uuid12>`, close() removes dir

Memory saved: ~2.9 GB at idle (4 browsers × ~720 MB per browser pool instance × however many Hermes processes spawn it).

## Herms 3-instance gotcha

User's Hermes runs 3 processes (2 dashboards + 1 gateway). Each spawns its own copy of every MCP. So a single MCP "leak" is actually 2-3 leaks. Kill all parent processes' MCP children, not just one.
