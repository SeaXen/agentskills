# Healthcheck Waste on `unless-stopped` Containers

## Pattern

Containers with a `Healthcheck` configured but `RestartPolicy.Name = "unless-stopped"` get zero value from the healthcheck — Docker does NOT restart the container on healthcheck failure. The healthcheck still runs every N seconds, enters the container, executes the probe, collects results.

## Reproduction (2026-06-24, i3-5010U, 9 containers)

```
$ docker inspect --format '{{.Name}} {{.Config.Healthcheck}}' $(docker ps -q)
/tradingx    {[CMD node -e require('http').get('http://127.0.0.1:8799/api/health',...)] 30s 5s 15s 0s 3}
/medsea      {[CMD-SHELL wget -q --spider http://localhost/ || exit 1] 30s 3s 0s 0s 0}
/termix      {[CMD-SHELL wget -q -O /dev/null http://localhost:30001/health || exit 1] 30s 10s 1m0s 0s 3}

$ docker inspect medsea --format '{{json .HostConfig.RestartPolicy}}'
{"Name":"unless-stopped","MaximumRetryCount":0}
```

All three: `unless-stopped`. None use healthcheck result for restart.

## Impact

- containerd spiked to **116% CPU** for 1-2s every 30s as all 3 healthchecks fired simultaneously
- dockerd spiked to 20% in sync (responding to container state queries)
- On a 15W i3-5010U, this manifested as perceived "20-30% idle" oscillation

## Confirmation

```bash
# Thread-level view — shows containerd threads spiking during healthcheck execution
$ pidstat -t -p 1167 1 5
12:37:40  1167   -   83.00  33.00   0.00   0.00  116.00  1  containerd
12:37:40    -  1256  20.00   4.00  0.00  11.00  24.00  0  |__containerd
12:37:40    -  4239  12.00   6.00  0.00   7.00  18.00  2  |__containerd
12:37:40    -  4240  11.00   6.00  0.00   7.00  17.00  2  |__containerd
12:37:40    -  4254  11.00   7.00  0.00   9.00  18.00  1  |__containerd
12:37:40    -  4276  19.00   6.00  0.00  10.00  25.00  0  |__containerd
```

## Rule

**If `RestartPolicy` is `unless-stopped` or `never`, AND the container is a single-process app (exits on crash), the healthcheck is pure waste.** Remove from image/compose and recreate.

## Fix — Full Removal Workflow

Cannot change healthcheck on a running container. Must update source config and rebuild/recreate.

### Step 1: Locate the healthcheck source

Healthchecks live in one of two places — find which:

```bash
# Check compose files (preferred — declarative)
find /mnt/tb -name "docker-compose.yml" -not -path "*/hermes-backups/*" | while read f; do
  grep -l "healthcheck" "$f" 2>/dev/null
done

# Check Dockerfiles (healthcheck baked into image)
find /mnt/tb -name "Dockerfile" -not -path "*/hermes-backups/*" | while read f; do
  grep -l "HEALTHCHECK" "$f" 2>/dev/null
done
```

### Step 2: Remove the healthcheck

**From compose file** — delete the `healthcheck:` block (typically 8-12 lines):
```yaml
# DELETE this entire block:
    healthcheck:
      test:
        ["CMD", "node", "-e", "..."]
      interval: 30s
      timeout: 5s
      retries: 3
      start_period: 15s
```

**From Dockerfile** — delete the HEALTHCHECK line:
```dockerfile
# DELETE this:
HEALTHCHECK --interval=30s --timeout=3s \
  CMD wget -q --spider http://localhost/ || exit 1
```

### Step 3: Rebuild and recreate

**Compose-based containers:**
```bash
cd /path/to/app
docker compose down
docker compose build --no-cache <service>
docker compose up -d
```

**Dockerfile-based containers:**
```bash
cd /path/to/app
docker stop <container> && docker rm <container>
docker build -t <image>:latest .
docker run -d --name <container> --restart unless-stopped -p <port> <image>:latest
```

### Step 4: Watch for port-mapping pitfalls

After rebuild, the new image may have a different internal port than the old container config. Check:

```bash
# Verify the container's internal port mapping
docker port <container>

# Compare with the app's expected port
docker exec <container> cat /etc/nginx/conf.d/default.conf | grep "listen"
```

**Common pitfall:** Old container had custom config listening on e.g. 8855, but a fresh `nginx:alpine` image listens on 80. If the host port mapping was `-p 8855:8855`, the rebuilt container needs `-p 8855:80` instead.

### Step 5: Verify functionality (not just "Up")

```bash
# HTTP probe
curl -s -o /dev/null -w "%{http_code}" http://localhost:<port>/

# For apps with APIs
curl -s http://localhost:<port>/api/health

# Confirm healthcheck is gone
docker inspect <container> --format '{{.Config.Healthcheck}}'
# Should return <nil>
```

### Step 6: Confirm CPU improvement

```bash
# Sample containerd CPU over 30s — should be ~0% now
pidstat -p <containerd_PID> 1 30
```

### Real-world example (2026-06-24)

**Tradingx** (compose-based):
```bash
# Removed healthcheck from /mnt/tb/1Apps/Tradingx/docker-compose.yml
cd /mnt/tb/1Apps/Tradingx
docker compose down && docker compose build --no-cache && docker compose up -d
```

**Medsea** (Dockerfile-based):
```bash
# Removed HEALTHCHECK from /mnt/tb/Sea-knowledge/#MedSea/Dockerfile
cd /mnt/tb/Sea-knowledge/#MedSea
docker build -t medsea-site:latest .
docker stop medsea && docker rm medsea
docker run -d --name medsea --restart unless-stopped -p 8855:80 medsea-site:latest
# Note: changed from -p 8855:8855 to -p 8855:80 because fresh nginx listens on 80
```

**Result:** containerd dropped from 10-29% spikes every 30s to ~1.5% average. All apps continued functioning normally.
