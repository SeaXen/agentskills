# Stale-while-revalidate dashboard performance pattern

Use this when a self-hosted dashboard has one slow inventory/probe source (Docker, network scans, route probes) but the UI should remain fast.

## Problem shape

- Dashboard endpoint combines cheap host stats with slow control-plane calls.
- Example: `docker ps -a` + `docker stats --no-stream` can take 1.5–3s on a busy low-power host.
- Normal dashboard refresh should not block on that slow path.
- User cares about CPU/RAM/resource use and expects measured before/after numbers.

## Fix pattern

1. Split data freshness from request latency.
2. Keep a process-local cache with timestamp and `cached/cache_age_ms` metadata.
3. Warm the cache on service start in a daemon thread.
4. Refresh slow inventory in the background every 10–15s.
5. Request path returns cached data immediately.
6. If cache is older than the freshness TTL, return stale data plus `stale: true` and trigger one background refresh.
7. Guard refresh with a lock/`refreshing` flag so concurrent requests do not spawn refresh storms.
8. Add endpoint timing fields: `docker`, `config`, `monitor`, `stats`, `total` ms.
9. Surface stale/refresh state in the UI, e.g. `api · refresh`, instead of freezing.

## Python sketch

```python
STATE = {
    "docker_cache": {"ts": 0.0, "data": None},
    "docker_refreshing": False,
    "docker_lock": threading.Lock(),
}

def docker_cache_snapshot(extra=None):
    cached = STATE["docker_cache"]
    if not cached.get("data"):
        return None
    data = json.loads(json.dumps(cached["data"]))
    data["cached"] = True
    data["cache_age_ms"] = int((time.time() - cached["ts"]) * 1000)
    if extra:
        data.update(extra)
    return data

def schedule_docker_refresh():
    with STATE["docker_lock"]:
        if STATE["docker_refreshing"]:
            return False
        STATE["docker_refreshing"] = True
    def worker():
        try:
            collect_containers(force=True)
        finally:
            with STATE["docker_lock"]:
                STATE["docker_refreshing"] = False
    threading.Thread(target=worker, daemon=True).start()
    return True

def collect_containers(force=False, allow_stale=True):
    cached = STATE["docker_cache"]
    age = time.time() - cached.get("ts", 0)
    if not force and cached.get("data"):
        if age < DOCKER_CACHE_TTL:
            return docker_cache_snapshot()
        if allow_stale:
            started = schedule_docker_refresh()
            return docker_cache_snapshot({
                "stale": True,
                "refreshing": bool(started or STATE["docker_refreshing"]),
            })
    # slow path here; update STATE["docker_cache"]
```

## Verification checklist

- Compile backend / syntax-check frontend.
- Restart service.
- Hit `/api/health`.
- Hit `/api/dashboard` repeatedly and confirm:
  - first warm/cache miss may be slower,
  - warm calls are stable and fast,
  - stale calls return quickly with `stale: true`/`refreshing: true` rather than blocking.
- Run a small benchmark script for `/`, `/api/health`, and `/api/dashboard` serial + concurrent.
- Check service RAM and thread count after the change.
- Intentionally abort a request and verify `BrokenPipeError` is not spamming logs if the server previously logged it.

## BrokenPipe suppression

For Python `http.server`/`socketserver` dashboards, browsers can disconnect mid-write and produce noisy stack traces. Suppress only expected disconnects, not real errors:

```python
class ThreadingHTTPServer(socketserver.ThreadingMixIn, socketserver.TCPServer):
    daemon_threads = True
    allow_reuse_address = True

    def handle_error(self, request, client_address):
        exc_type, exc, _ = sys.exc_info()
        if isinstance(exc, (BrokenPipeError, ConnectionResetError, ConnectionAbortedError)):
            return
        super().handle_error(request, client_address)
```

Also wrap response writes when practical:

```python
try:
    self.end_headers()
    self.wfile.write(body)
except (BrokenPipeError, ConnectionResetError, ConnectionAbortedError):
    return
```

## Reporting format

Give the user concrete before/after numbers:

- dashboard app count/container count
- process RAM/peak RAM/thread count
- cold dashboard latency
- warm dashboard latency
- serial and concurrent endpoint benchmarks
- Docker top RAM/CPU containers
- exact commit hash if code was pushed
