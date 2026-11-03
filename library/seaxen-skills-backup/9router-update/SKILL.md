---
name: 9router-update
description: Update 9router Docker deployment with verified backup+pull+recreate+patch flow, plus version check, troubleshooting, and hard-refresh.
version: 0.1.0
author: Hermes
platforms: [linux]
metadata:
  hermes:
    tags: [9router, Self-Hosted, Docker, Update, Patch]
    prereqs: [docker, python3, git]
    category: devops
---

# 9router Update — Verified Procedure

Update a self-hosted 9router Docker deployment from one upstream version to the next, **without losing the usage-periods patch** or any other local customizations. Same procedure has been executed at least four times (v0.5.18 → v0.5.45 → v0.5.50 → v0.5.55 → v0.5.59 → **v0.5.65**) without losing data.

## When to Use

- User asks to update / upgrade 9router
- A new upstream commit / release tag exists on `decolua/9router`
- The usage-periods selector (90d / 180d / 365d / All) disappears from `/dashboard/usage` (patch was wiped on a manual `docker run` recreate)
- The dashboard reverted to stock 7d/30d/60d period options

## Critical Rules (verified by failure)

1. **Always run `update.sh`** — never `docker pull && docker stop && docker rm && docker run` by hand. The hand-rolled approach drifts env / volumes / network from `docker-compose.yml` and breaks backups.
2. **Never skip `apply-usage-periods.py`.** It is **NOT** part of the upstream image. Every `docker compose up -d --force-recreate` overwrites the container's compiled JS and silently reverts the period selector back to 7d/30d/60d. The browser cache then hides the loss for hours.
3. **Always verify in the running container**, not just trust script output. Next.js hashes chunk filenames (`5497-XXXXXXXX.js`) on every build — you cannot pin a path.
4. **Hard-refresh the browser** (`Ctrl+Shift+R`) on `/dashboard/usage` after every update. The user's previous session will keep showing the cached 7d/30d/60d selector even if the new bundle is on disk.
5. **Always `docker ps` and confirm** the image digest changed (e.g. `3eb104460661` for v0.5.65). If the digest is unchanged after `docker pull`, the registry returned a cached image.

## When NOT to Use

- Updating **OmniRoute** (different product, different folder, different procedure) — that's `decolua/OmniRoute` / `diegosouzapw/omniroute`. Do not confuse the two.
- The user wants a *fresh install* (no existing data) — use the `9router-self-hosted` skill instead.
- The user wants to add a *new provider* or change Cloudflare relay settings — that's a config edit, not an update.

## Inputs

- Container name: `9router` (hard-coded in the patch script)
- App dir: `/mnt/tb/1Apps/9router` (Linux convention; update if your install is elsewhere)
- Image: `decolua/9router:latest`
- Compose: `/mnt/tb/1Apps/9router/docker-compose.yml`
- Backups: `/mnt/tb/1Apps/9router/backups/<YYYYMMDD_HHMMSS>/`
- Port (default): `20111`

## Step-by-Step Procedure

### 1. Pre-flight — confirm there really is an update

```bash
cd /mnt/tb/1Apps/9router-upstream  # or any decolua/9router checkout with origin pointing to decolua
git fetch origin --tags --force
git tag --sort=-v:refname | head -3          # latest release
git log origin/main --oneline -10           # unreleased commits
echo "Currently running:"
docker exec 9router cat /app/package.json | grep '"version"'
```

If the user supplied a commit URL (e.g. `https://github.com/decolua/9router/commit/4eda76e2…`), verify it lands on a release tag — `git log 4eda76e2 --oneline -1` should show `# v0.5.65 (2026-09-03)` or similar.

### 2. Run the verified update

```bash
cd /mnt/tb/1Apps/9router
bash update.sh
```

What `update.sh` does, in order:
1. `ts=$(date +%Y%m%d_%H%M%S)` → `bk=backups/$ts` → `cp -a data/ $bk/`
2. `docker pull decolua/9router:latest` (registry can take 2–10 min for a 2.6 GB image)
3. `docker stop 9router && docker rm 9router`
4. `docker compose -f docker-compose.yml up -d --force-recreate --remove-orphans` — restores env, volumes, host network, restart policy from the compose file (this is the **single source of truth** for runtime config)
5. `python3 patches/apply-usage-periods.py` — patches the new container's compiled JS in place, then `docker restart 9router` so the patches take effect on first request
6. Polls `http://127.0.0.1:20111/api/health` for up to 30 s
7. Prints `==> OK health on :20111 — revision <sha>` and the hard-refresh reminder

### 3. Verify the patch is actually in the running image

**Do not trust the script's `ok ui ...` lines alone.** The script may report `already stats-api` because of stale state. Re-grep the live container:

```bash
# Confirm new image
docker images decolua/9router --format "{{.ID}} ({{.CreatedSince}})"

# Confirm patched period selector in the UI bundle
docker exec 9router sh -c \
  "grep -oE '90d.{0,40}180d.{0,40}365d.{0,40}all' /app/.next/static/chunks/5497-*.js | head -c 200"

# Confirm patched API allowlist
docker exec 9router grep -oE 'today.*24h.*7d.*30d.*60d.*90d.*180d.*365d.*all' \
  /app/.next/server/app/api/usage/stats/route.js | head -c 200
docker exec 9router grep -oE 'today.*24h.*7d.*30d.*60d.*90d.*180d.*365d.*all' \
  /app/.next/server/app/api/usage/chart/route.js | head -c 200
```

If any of these return nothing, the patch did not apply. Run `python3 patches/apply-usage-periods.py` manually and re-check.

### 4. Remind the user to hard-refresh

The browser will keep showing the cached old bundle. Tell the user to press `Ctrl+Shift+R` on `/dashboard/usage` and confirm the period selector now includes `90D`, `180D`, `365D`, `All`.

## Verifying the Live State (post-update checklist)

| Check | Command | Expected |
|------|---------|----------|
| Container up | `docker ps --filter name=9router --format "{{.Status}}"` | `Up N minutes (healthy)` |
| Health endpoint | `curl -s http://127.0.0.1:20111/api/health` | `{"ok":true}` |
| New version | `docker exec 9router cat /app/package.json \| grep '"version"'` | New tag (e.g. `0.5.65`) |
| New image | `docker inspect 9router --format '{{.Image}}' \| xargs docker images --format "{{.ID}}"` | Image ID changed vs pre-update |
| UI patch in bundle | `docker exec 9router sh -c "grep -c '90D' /app/.next/static/chunks/5497-*.js"` | ≥ 1 |
| API patch (stats) | `docker exec 9router grep -c '180d' /app/.next/server/app/api/usage/stats/route.js` | ≥ 1 |
| API patch (chart) | `docker exec 9router grep -c '180d' /app/.next/server/app/api/usage/chart/route.js` | ≥ 1 |
| Backup exists | `ls -t /mnt/tb/1Apps/9router/backups/ \| head -1` | Today's timestamp |

## What `apply-usage-periods.py` Patches (for reference)

| File | Old value | New value |
|------|-----------|-----------|
| `static/chunks/5497-*.js` (UI bundle) | `{7d, 30d, 60d}` | `{7d, 30d, 60d, 90d, 180d, 365d, all}` |
| `static/chunks/app/(dashboard)/dashboard/usage/page-*.js` | same | same |
| `server/chunks/412.js` | same | same |
| `server/app/(dashboard)/dashboard/usage/page.js` | same | same |
| `server/app/api/usage/stats/route.js` | `Set(["today","24h","7d","30d","60d","all"])` | adds `90d`, `180d`, `365d` |
| `server/app/api/usage/chart/route.js` | `Set(["today","24h","7d","30d","60d"])` | adds `90d`, `180d`, `365d`, `all` |
| `server/chunks/4884.js` (stats map) | `{"7d":7,"30d":30,"60d":60}` | adds `90d`, `180d`, `365d`, `all:null` |
| `server/chunks/4884.js` (chart days) | `let f="7d"===a?7:"30d"===a?30:60,...` | adds 90d/180d/365d branches + all-mode |

The script greps for the **old** pattern, so it is idempotent — running it twice is safe; the second run says `already ...` for every path.

## Common Failures and Fixes

### `update.sh` reports OK but `/dashboard/usage` still shows 7d/30d/60d

**Cause:** Browser cache. The JS bundle hash changed on disk but the browser served the cached one.

**Fix:** User must hard-refresh (`Ctrl+Shift+R` or `Cmd+Shift+R`). On the same LAN via Cloudflare, also purge Cloudflare cache for the asset.

### `docker pull` hangs or fails

**Cause:** Registry rate-limit, network blip, or large image on slow link.

**Fix:**
```bash
# Check progress
docker ps -a | grep pull  # no — pull is not a container
# Actually:
ps aux | grep "docker pull" | grep -v grep
# Or:
docker images decolua/9router --format "{{.ID}} {{.CreatedSince}}"  # if digest appeared, it finished
```

If `docker pull` is stuck, kill it (`pkill -f 'docker pull'`) and re-run `update.sh`. The backup is still on disk.

### Patch script says `WARN no match` on every file

**Cause:** Upstream changed the bundled JS structure. The old pattern `{value:"7d",label:"7D"},…` is no longer present.

**Fix:** Inspect the current usage-page chunk inside the container to find the new selector:
```bash
docker exec 9router sh -c \
  "find /app/.next -name '*.js' -exec grep -l '7d.*30d.*60d' {} \;"
```
Update the `OLD_UI` and `OLD_MAP` constants in `patches/apply-usage-periods.py` to match the new structure, then re-run.

### Container starts but `api/health` returns 000 (timeout)

**Cause:** Port conflict, env not loaded, or upstream bug.

**Fix:**
```bash
docker logs 9router --tail 50
docker inspect 9router --format '{{.State.Health.Status}}'
ss -tlnp | grep 20111
```

### Image digest didn't change after `docker pull`

**Cause:** Docker cache returned the same image.

**Fix:**
```bash
docker pull decolua/9router:latest --no-cache
```
Confirm the new digest, then re-run `update.sh`.

## Reference Links

- Upstream: https://github.com/decolua/9router
- v0.5.65 release commit: https://github.com/decolua/9router/commit/4eda76e2abbcffe6e1b0511f4117f448240c46db
- Local checkout: `/mnt/tb/1Apps/9router-upstream`
- App dir: `/mnt/tb/1Apps/9router`
- Companion skill (install from scratch): `9router-self-hosted`
- Sibling product (DO NOT confuse): OmniRoute at `decolua/OmniRoute` / `diegosouzapw/omniroute` — runs on `:20128`, uses `OMNIROUTE_ALLOW_PRIVATE_PROVIDER_URLS=true`.

## Files in This Skill

- `SKILL.md` — this file
- `references/update-flow.md` — annotated walkthrough of `update.sh` line-by-line
- `references/patch-targets.md` — exhaustive list of files the patch touches across versions
- `scripts/verify-update.sh` — one-shot verifier (runs all 7 post-update checks and prints ✅ / ❌)
- `scripts/quick-version-check.sh` — non-destructive "is there an update?" probe
- `templates/CHANGELOG-patch-note.md` — drop-in note to attach to a release message
