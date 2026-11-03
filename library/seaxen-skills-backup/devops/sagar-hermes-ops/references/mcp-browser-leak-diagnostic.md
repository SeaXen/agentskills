# MCP Browser Leak Diagnostic — when the host feels hung

## Symptom signature

A self-hosted Hermes / Docker / MCP stack that "suddenly becomes unresponsive":
- SSH login hangs or times out
- Gateway stops responding
- `docker ps` / `ps` hang
- Manual power-off required

This is almost always **memory-pressure-induced swap-thrashing**, not a Hermes core bug or a Docker crash. On 7–8 GiB hosts with multiple Docker containers and MCP servers, the leak source is almost always an **MCP server that uses a headless browser pool without proper cleanup**.

## First 60 seconds: prove it is memory pressure

Run these from any shell that still responds (SSH, dashboard terminal tab, recovery console):

```bash
uptime                     # load avg > number of CPUs = overloaded
free -m                   # MemAvailable near 0 + SwapUsed high = starved
docker stats --no-stream  # who is the top memory consumer?
```

Concrete thresholds for "this is the leak, not a normal load":
- `MemAvailable < 500 MiB` AND `SwapUsed > 1 GiB`
- Load average > 4 on a 4-core box
- `systemd-journald: Under memory pressure, flushing caches` in `dmesg` (proves kernel is reclaiming)

## Find the leak source

Most common on Hermes hosts: a headless-browser MCP server (TradingView charts, Playwright-driven scrapers, screenshot tools, web QA bots).

```bash
# How many headless browsers are running?
echo "chromium: $(pgrep -c chromium 2>/dev/null)"
echo "chromedriver: $(pgrep -c chromedriver 2>/dev/null)"
echo "chrome_crashpad: $(pgrep -c chrome_crashpad 2>/dev/null)"

# Total memory held by them
ps -eo pid,rss,args | grep -E "chromium|chromedriver" | grep -v grep \
  | awk '{sum+=$2} END {printf "headless browser RSS: %.1f MiB\n", sum/1024}'

# Who spawned them? Look for an MCP server as the ultimate ancestor.
for p in $(pgrep chromedriver 2>/dev/null); do
  ppid=$(awk '/^PPid:/{print $2}' /proc/$p/status 2>/dev/null)
  ppname=$(cat /proc/$ppid/comm 2>/dev/null)
  echo "chromedriver $p → parent: $ppname (ppid=$ppid)"
done
```

Common signatures:
- `chromedriver` parent = a Python process running `.../tradingview-chart-mcp/main_optimized.py` or similar
- `chromedriver` parent = `defunct` (zombie) — the MCP server crashed but the chromium children survived
- 12+ chromedrivers from a single MCP family = browser pool leak

## Kill in the right order

The wrong order makes things worse. Killing the MCP server parent first causes Hermes to immediately respawn it, and the new MCP starts up its own 4-browser pool while the OLD children are still dying. Result: load spikes to 30+ as 100+ processes get SIGKILLed in a thundering herd, and the system hangs harder.

**Correct order**:

1. **Kill orphan chromium children first** (smallest memory, fastest exit):
   ```bash
   # Only matches scoped user-data-dirs from chromedriver, NOT the user's interactive browser
   pkill -9 -f "chromium.*--user-data-dir=/tmp/org.chromium.Chromium.scoped_dir"
   ```

2. **Kill orphan chromedriver processes**:
   ```bash
   pkill -9 -f chromedriver
   ```

3. **Clean up old user-data-dirs**:
   ```bash
   rm -rf /tmp/org.chromium.Chromium.scoped_dir.* 2>/dev/null
   ```

4. **THEN kill the leaking MCP server** — by this point its child cleanup is easier:
   ```bash
   pgrep -f "tradingview-chart-mcp" | xargs -r kill -TERM
   sleep 5
   ```

5. **Verify recovery**:
   ```bash
   free -m
   uptime
   echo "chromium: $(pgrep -c chromium)"
   ```

If a patched MCP server (with atexit + signal cleanup) is restarted by Hermes, its pool size will be `max_concurrent` × chromedriver, and after the next SIGTERM its children will be reaped cleanly. Verify with `ls /tmp/<mcp-prefix>-*` — deterministic prefixes (e.g. `/tmp/tvscraper-*`) make leak detection trivial.

## What NOT to do

- **Don't `pkill -9 chromium` blanket.** On a host with a real interactive browser session (the user might have Chrome open in the background), this kills their session. Scope by `--user-data-dir=/tmp/org.chromium.Chromium.scoped_dir` to hit only chromedriver-spawned headless instances.
- **Don't kill the MCP server parent first.** Hermes will restart it within seconds. Better: let the patch handle cleanup, then verify with `kill -TERM` followed by checking process counts.
- **Don't trust the 192 Mbit/s "throughput" in your progress bar.** Local TCP send buffer can absorb data even when the remote peer has already sent FIN. Check `/proc/<pid>/io` for actual bytes sent, and check `ss -tnp -p <pid>` for the connection state — `CLOSE-WAIT` means the remote closed but the local kernel hasn't yet.
- **Don't run heavy Python scripts on a host already at >80% memory.** Adding 500 MB of page cache for a chunked upload will push the system into swap. Check `free -m` first; if `MemAvailable < 1 GiB`, stop and reclaim memory before uploading.

## What to put in `~/.bashrc` / `~/.hermes/scripts/`

A reusable watchdog for this class of issue:

```bash
# ~/.local/bin/mcp-mem-watchdog
#!/usr/bin/env bash
# Alert if headless browser RAM > 2 GiB
RAM=$(ps -eo rss,args | grep -E "chromium|chromedriver" | grep -v grep \
      | awk '{sum+=$1} END {printf "%.0f", sum/1024}')
if [ "$RAM" -gt 2048 ]; then
  echo "WARN: headless browsers hold ${RAM} MiB — likely MCP pool leak"
  ps -eo pid,ppid,rss,args | grep -E "chromium|chromedriver" | grep -v grep | head -5
fi
```

## After recovery: prevent the next time

The diagnostic is fine for one incident. The actual fix is at the MCP server source. See `mcp/native-mcp/references/mcp-server-browser-pool-hygiene.md` for the atexit + signal handler + tracked user-data-dir pattern that any MCP server with a headless browser pool needs.

For the user's specific stack, also worth doing once after recovery:

```bash
# Reduce default browser pool sizes in MCP servers that allow it
# (e.g. tradingview-chart-mcp takes --max-concurrent; default is 4 → 1 or 2)
hermes config set mcp_servers.tradingview-chart-mcp.args '["--max-concurrent", "2"]'
```

Smaller pool = smaller per-MCP memory footprint = less damage on the next incident. The performance cost is usually acceptable because the leak, not the lack of parallelism, was the actual pain.

## See also

- `mcp/native-mcp/references/mcp-server-browser-pool-hygiene.md` — required source patch pattern
- `devops/dashboard-ui-operations/references/local-web-service-port-inspection.md` — general "what is on port X" triage recipe
