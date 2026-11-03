# MCP Server with Headless Browser Pool — Hygiene Reference

## Why this exists

In a long-running host with multiple MCP servers, **a headless-browser MCP server that does not register exit cleanup leaks one chromedriver + ~8 chromium children + ~2 crashpad handlers per pool browser per restart**. Each leaked set holds ~250 MiB of RAM. After 5 server restarts × 4 pool size = 20 leaked sets ≈ 5 GiB permanently gone. On a memory-constrained host this **starves the system into swap-thrashing and makes SSH unresponsive**.

Verified on 2026-06-17 with `tradingview-chart-mcp` (Selenium + ChromeDriver), pre-patch: `chromium: 96`, `chromedriver: 12`, `chrome_crashpad: 25`, system load avg 13.28, `free: 250 MiB`, gateway stopped responding.

## The fix is three lines of cleanup logic

If the MCP server spawns Chrome / Chromium / Firefox / WebKit via Selenium, Playwright, Puppeteer, or any wrapper, it **must** wire these three things:

### 1. Track the user-data-dir path on the scraper instance

Chromedriver generates a random scoped user-data-dir (e.g. `/tmp/org.chromium.Chromium.scoped_dir.XXXXXX`). If you do not record the path you cannot clean it. **Set your own deterministic path instead of accepting the random one**:

```python
# in _setup_driver()
import uuid
self._user_data_dir = f"/tmp/{self.server_name}-{uuid.uuid4().hex[:12]}"
chrome_options.add_argument(f"--user-data-dir={self._user_data_dir}")
```

`self.server_name` should be the MCP server name so `/tmp` is browsable for debugging (e.g. `/tmp/tvscraper-3f8a2b91c0d4`).

### 2. Remove the user-data-dir in `close()`

```python
def close(self):
    if self.driver:
        try: self.driver.quit()
        except Exception: pass
        self.driver = None
    if getattr(self, "_user_data_dir", None):
        import shutil
        shutil.rmtree(self._user_data_dir, ignore_errors=True)
```

### 3. Register `atexit` AND signal handlers on the MCP server init

`atexit` alone is not enough — the MCP server can be killed by `SIGTERM`/`SIGINT`/`SIGHUP` from a supervisor or wrapper script without going through normal Python exit:

```python
import atexit, signal

class MyMCPServer:
    def __init__(self, ...):
        # ... pool init ...
        atexit.register(self.cleanup)
        for sig in (signal.SIGTERM, signal.SIGINT, signal.SIGHUP):
            try:
                signal.signal(sig, self._signal_cleanup)
            except (ValueError, OSError):
                pass  # not main thread

    def _signal_cleanup(self, signum, frame):
        self.cleanup()
        signal.signal(signum, signal.SIG_DFL)  # restore default
        os.kill(os.getpid(), signum)            # re-raise

    def cleanup(self):
        if self._shutting_down: return
        self._shutting_down = True
        with self.lock:
            for scraper in self.pool:
                try: scraper.close()
                except Exception: pass
            self.pool.clear()
        # belt-and-suspenders: any orphan chromedriver started by this process
        try:
            import subprocess
            subprocess.run(["pkill", "-9", "-P", str(os.getpid()), "-f", "chromedriver"],
                           timeout=2, capture_output=True)
        except Exception: pass
```

`atexit.register` is the easy one to forget — the import is often already there, but the register call is not. A code search for `atexit` in MCP server code that shows `import atexit` but no `atexit.register` is a strong leak signal.

## Browser-pool-specific failure modes

### Pool size grows on rotation

A "rotate after N requests" path like:

```python
if count >= self.MAX_REQUESTS_PER_BROWSER:
    scraper.close()
    new_scraper = TradingViewScraper(...)  # spawns new chromedriver
    new_scraper._setup_driver()
```

…should NOT leak **as long as** `close()` does the right thing on the old one. If `close()` only calls `driver.quit()` and skips the user-data-dir cleanup, every rotation leaks a scoped_dir. After 20 requests per rotation × 4 pool browsers × 50 chart calls = 200 scoped_dirs in `/tmp`.

### Children outlive chromedriver

When chromedriver exits gracefully, its chromium children usually exit too. When it is `kill -9`'d or OOM-killed, the chromium children may remain. Symptoms:

- `pgrep -c chromedriver` returns 0 but `pgrep -c chromium` is high
- `/tmp/org.chromium.Chromium.scoped_dir.*` count is higher than chromedriver count
- `chrome_crashpad` (the helper that reports crashes) orphans frequently

The `pkill -9 -P <pid> -f chromedriver` belt-and-suspenders in `cleanup()` helps; matching by user-data-dir path is even more reliable:

```python
subprocess.run(["pkill", "-9", "-f", f"chromium.*{self._user_data_dir}"], timeout=2)
```

## Detection on the host

Quick triage when an MCP-using host feels slow:

```bash
# Count orphan headless browsers by parent
for p in $(pgrep chromedriver); do
  pp=$(awk '/^PPid:/{print $2}' /proc/$p/status)
  parent_name=$(cat /proc/$pp/comm 2>/dev/null)
  echo "chromedriver $p parent=$parent_name (ppid=$pp)"
done

# Total memory held
ps -eo pid,rss,args | grep -E "chromium|chromedriver" | grep -v grep \
  | awk '{sum+=$2} END {printf "headless browser RSS: %.1f MiB\n", sum/1024}'

# user-data-dir bloat
du -sh /tmp/org.chromium.Chromium.scoped_dir.* 2>/dev/null | tail -5
ls -d /tmp/org.chromium.Chromium.scoped_dir.* 2>/dev/null | wc -l
```

If the parent of chromedriver is a defunct/zombie process, the MCP server was killed without cleanup — that is the bug. If the parent is a still-running MCP server (e.g. `python .../tradingview-chart-mcp/main_optimized.py`), the MCP has a browser-pool leak.

## Verification that the fix works

After patching:

1. Kill the MCP server with `kill -TERM <pid>` (not `-9`).
2. Within ~5 s, `pgrep -c chromedriver` and `pgrep -c chromium` should both drop noticeably.
3. `ls -d /tmp/<server-prefix>-*` (using the deterministic prefix from step 1) should be empty after cleanup completes.
4. Free RAM should rise. If it does not, another source is still leaking.

## Related references

- For the live-host memory-pressure diagnostic that surfaced this pattern, see `devops/sagar-hermes-ops/references/mcp-browser-leak-diagnostic.md`.
- For why MCP servers tend to leak into `/tmp` in the first place and how to keep that bloat in check, see `devops/sagar-hermes-ops/references/sagar-hermes-tmp-cleanup.md` (if present) or apply the same `rm -rf /tmp/<prefix>-*` pattern after each MCP restart.
