# 9router — timezone, usage periods, built-in tunnel

Deploy path on this host: `/mnt/tb/1Apps/9router/`, image `decolua/9router:latest`, port **20111**, `network_mode: host`.

## Timezone (Asia/Dhaka)

Container defaults to **UTC** if `TZ` is unset. Node `Intl` and dashboard timestamps follow `TZ`.

```yaml
environment:
  PORT: "20111"
  HOSTNAME: 0.0.0.0
  TZ: Asia/Dhaka
```

Recreate after change: `docker compose up -d --force-recreate 9router`.

Verify:
```bash
docker exec 9router node -e "console.log(Intl.DateTimeFormat().resolvedOptions().timeZone)"
# expect Asia/Dhaka
```

Shell `date` may still print UTC if the image lacks `tzdata` for libc — **Node/app UI** is what matters.

## Usage & Analytics — extend period beyond 60D

Stock UI (v0.5.18) only offers **Today, 24h, 7D, 30D, 60D**. There is **no** settings toggle for 90/180/365/All — options are hardcoded in built `.next` bundles.

**Ephemeral patch** (lost on `docker pull` / recreate):

1. Host script (canonical copy): `/mnt/tb/1Apps/9router/patches/apply-usage-periods.py`
2. Skill copy: `scripts/apply-9router-usage-periods.py` in this skill dir
3. Run: `python3 /mnt/tb/1Apps/9router/patches/apply-usage-periods.py`
4. Hard-refresh dashboard Usage page (Ctrl+Shift+R)

Adds: **90D, 180D, 365D, All** — patches client chunk, SSR chunk, `/api/usage/stats`, `/api/usage/chart`, and server chunk `4884.js` (day map + chart `all` branch).

**Data limit:** ranges only include rows in `usageDaily` / `usageHistory` (retention). **All** = every `usageDaily` day key in SQLite.

**Upstream:** request official options in decolua/9router repo; local patch is a workaround.

## Built-in Cloudflare / tunnel button (port pitfall)

9router built-in tunnel health-check may assume default app port **20128** while this install uses **PORT=20111**. Symptom: tunnel enable → `Health check timeout after 60000ms` while `curl http://127.0.0.1:20111/api/health` returns 200.

**Workaround:** use the user's **existing Cloudflare Tunnel** → origin `http://127.0.0.1:20111` (or LAN IP), public API base `https://<hostname>/v1`. Do not rely on the in-app tunnel until ports align or upstream fixes health-check port.

## Local vs tunnel latency (Hermes on same host)

| Target | Use when |
|--------|----------|
| `http://127.0.0.1:20111` | Fastest — 9router on same box |
| `http://192.168.0.222:20111` | Other LAN devices |
| `https://*.xuup.top` | Remote / public only |