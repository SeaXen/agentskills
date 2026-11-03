# Linux diagnostics: common pitfalls

## containerd / dockerd CPU reporting

`ps` shows **lifetime average CPU** for containerd/dockerd, not current usage. A process showing 15% CPU may actually be idle.

**Check actual state:**
```bash
# Process state (S=idle/sleeping, R=running)
cat /proc/<pid>/status | grep State

# What kernel function it's waiting on
cat /proc/<pid>/wchan
# futex_wait_queue = idle, waiting for work

# Lifetime average calculation
cat /proc/<pid>/stat | awk '{print "utime="$14" stime="$15" total="($14+$15)}'
ps -p <pid> -o etimes=  # elapsed seconds
# avg% = (total_jiffies / 100) / elapsed_seconds
```

**Rule of thumb:** If `State: S (sleeping)` and `wchan: futex_wait_queue`, the process is idle regardless of what `ps` shows for CPU%.

## kula config: interval must match tier 1 resolution

kula crashes on startup if `collection.interval` and tier 1 `resolution` don't match exactly.

```yaml
collection:
  interval: 5s    # ← must match tier 1 below
storage:
  tiers:
    - resolution: 5s   # ← must match interval above
      max_size: 50MB
    - resolution: 1m
      max_size: 150MB
    - resolution: 5m
      max_size: 50MB
```

**Error:** kula exits with status 1, systemd shows `Main process exited, code=exited, status=1/FAILURE`.

**Fix:** Ensure both values match. After changing, `systemctl reset-failed kula && systemctl restart kula`.

## nginx + BusyBox wget: IPv6 healthcheck failure

BusyBox wget resolves `localhost` to IPv6 `::1` first. If nginx only listens on IPv4 (`listen 80;`), healthcheck fails with "Connection refused".

**Symptom:** Container healthcheck fails 1000+ times, `wget: can't connect to remote host: Connection refused`.

**Fix:** Add IPv6 listen to nginx:
```nginx
server {
    listen 80;
    listen [::]:80 ipv6only=on;
    ...
}
```

**Note:** This change is in-memory only on a running container. For permanent fix, update the Dockerfile/image and rebuild.
