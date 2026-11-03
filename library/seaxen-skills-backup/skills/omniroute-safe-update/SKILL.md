---
name: omniroute-safe-update
description: Safely update the OmniRoute Docker deployment at /mnt/tb/1Apps/omniroute/ without losing DB settings or model price overrides. Covers pre-update backup, image pin, update, post-update catalog re-patch, and rollback.
when_to_use:
  - User says "update omniroute" / "omni-update" / "pull new omniroute"
  - Before any `docker compose pull` against the omniroute service
  - After an update, to re-apply zero-pricing catalog patches
---

# OmniRoute Safe Update

## Context (project state)
- Compose **must** include `env_file: - ./data/server.env` so `STORAGE_ENCRYPTION_KEY` is in process env (proxy-pool relay auth). See `omniroute-update` → `references/relay-proxy-auth.md`.
- Compose root: `/mnt/tb/1Apps/omniroute/`
- DB (persistent): `/mnt/tb/1Apps/omniroute/data/storage.sqlite`
- Backup dir: `/mnt/tb/1Apps/omniroute/data/` (DB backups) and `/mnt/tb/1Apps/omniroute/patches/` (catalog backups, create if missing)
- Container name: `omniroute`
- Pricing layers:
  1. **DB overrides** (persistent) — 828+ models zeroed, stored in `storage.sqlite`. Survives updates. **This is the recommended approach.**
  2. **JS catalog chunks** (ephemeral, inside container image) — `/app/.build/next/server/chunks/{11203,44021,95577,30038,68131}.js` (list is dynamic, use `grep -l` to discover). Reset on every image update. **Fragile — sed can corrupt minified JS. Skip unless absolutely needed.**

## What survives vs what wipes
- Survives: DB overrides, provider configs, API keys, routing rules, accounts, anything set via UI.
- Wipes: catalog JS chunk patches → must be re-applied (if you use them). New models introduced by the update will show default prices until overridden.
- **DB overrides alone are sufficient** for the Pricing page to show $0. JS catalog patches are optional and fragile.

## Step 1 — Pre-update backup (mandatory)

```bash
cd /mnt/tb/1Apps/omniroute
STAMP=$(date +%Y%m%d-%H%M%S)

# DB backup
cp data/storage.sqlite data/storage.sqlite.bak-before-update-$STAMP

# Compose + env backup
cp docker-compose.yml docker-compose.yml.bak-$STAMP
cp data/server.env data/server.env.bak-$STAMP 2>/dev/null || true
[ -f .env ] && cp .env .env.bak-$STAMP

# Or use project script (keeps last 2 backups):
# bash /mnt/tb/1Apps/omniroute/backup.sh

# Pin current image tag for rollback
docker inspect omniroute --format '{{.Config.Image}}' > .last-image-tag-$STAMP
echo "Pinned tag: $(cat .last-image-tag-$STAMP)"
```

Pitfall: forgetting to pin the current image tag — without it, rollback requires guessing or pulling from `docker image ls` history.

## Step 2 — Save current catalog patches (so we can diff after update)

```bash
mkdir -p /mnt/tb/1Apps/omniroute/patches
docker cp omniroute:/app/.build/next/server/chunks/11203.js /mnt/tb/1Apps/omniroute/patches/11203.js.patched-$STAMP
docker cp omniroute:/app/.build/next/server/chunks/44021.js /mnt/tb/1Apps/omniroute/patches/44021.js.patched-$STAMP
docker cp omniroute:/app/.build/next/server/chunks/95577.js /mnt/tb/1Apps/omniroute/patches/95577.js.patched-$STAMP
```

## Step 3 — Update

```bash
cd /mnt/tb/1Apps/omniroute
docker compose pull
docker compose up -d
```

Wait ~15–30s for the container to come up. Verify:

```bash
docker compose ps
docker logs omniroute --tail 50
curl -sf http://192.168.0.222:20128/ -o /dev/null && echo "UI reachable" || echo "UI NOT reachable"
```

## Step 4 — Re-apply catalog zero-pricing patch (OPTIONAL — see warning)

> **⚠️ WARNING: sed-patching minified JS chunks is fragile.** It can corrupt JS syntax and break unrelated pages (proven in a real incident where it crashed `/dashboard/costs`). The DB overrides from Step 6 are sufficient for the Pricing page to show $0. **Skip this step unless you specifically need the Costs Overview page to show $0 in the UI.** Even then, the Costs Overview page has an upstream rendering bug in v3.8.42 that may prevent it from loading regardless.

If proceeding, first discover which chunks contain pricing data (the list changes across image versions):

```bash
docker exec omniroute sh -c 'cd /app/.build/next/server/chunks && for f in *.js; do
  if grep -qE "(input|output|cached|reasoning|cache_write):[0-9]+" "$f" 2>/dev/null; then
    cnt=$(grep -coE "(input|output|cached|reasoning|cache_write):[0-9]+" "$f" | paste -sd+ | bc)
    echo "$f: $cnt pricing entries"
  fi
done'
```

Then zero them (use the dynamically-discovered list, not a hardcoded one):

```bash
# Inside container — apply regex zero patch to all discovered pricing chunks
for f in 11203 44021 95577 30038 68131; do
  docker exec omniroute sh -c "
    cp /app/.build/next/server/chunks/$f.js /tmp/$f.js.bak-postupdate
    sed -i -E 's/(input|output|cached|reasoning|cache_write)[[:space:]]*:[[:space:]]*[0-9]+(\.[0-9]+)?/\1:0/g' /app/.build/next/server/chunks/$f.js
    echo \"$f: \$(grep -oE '(input|output|cached|reasoning|cache_write):[0-9]+' /app/.build/next/server/chunks/$f.js | grep -v ':0' | wc -l) non-zero entries remaining\"
  "
done
```

If any non-zero entries remain, inspect manually with:

```bash
docker exec omniroute grep -nE '(input|output|cached|reasoning|cache_write):[0-9]+\.?[0-9]*' /app/.build/next/server/chunks/11203.js | grep -v ':0'
```

Stray patterns sometimes use only `{input:N,output:M}` (no `cached`). Patch those individually.

**After patching, verify no pages are broken:**
```bash
# Check that the pricing page loads
curl -sf http://192.168.0.222:20128/dashboard/costs/pricing -o /dev/null && echo "Pricing OK"
# Check that the costs overview doesn't crash (may fail due to upstream bug, not your patch)
curl -sf http://192.168.0.222:20128/dashboard/costs -o /dev/null && echo "Costs OK"
```

## Step 5 — Restart and verify

```bash
docker compose restart omniroute
sleep 10
```

Open `http://192.168.0.222:20128/dashboard/costs/pricing` and confirm:
- xAI, Gemini, MiniMax, GLM, DeepSeek, Groq all show $0 across all five columns
- "PRICED" count should match (or be ≤) the "USER OVERRIDE" count

## Step 6 — Override any newly-added models

If the update added new providers/models that show non-zero prices and aren't covered by DB overrides, zero them via DB:

```bash
docker exec omniroute sqlite3 /app/data/storage.sqlite \
  "SELECT DISTINCT namespace FROM pricing_overrides;" 2>/dev/null || \
  echo "Check the actual DB schema with: docker exec omniroute sqlite3 /app/data/storage.sqlite '.schema'"
```

Then patch the gap via the same UPDATE pattern used in the original zeroing run.

## Rollback (if update breaks things)

```bash
cd /mnt/tb/1Apps/omniroute

# Restore DB
cp data/storage.sqlite.bak-before-update-$STAMP data/storage.sqlite

# Pin back to old image
OLD_TAG=$(cat .last-image-tag-$STAMP)
docker compose down
docker tag $OLD_TAG omniroute:rollback   # only if image is still locally cached
# OR edit docker-compose.yml to reference the old tag, then:
docker compose up -d
```

## Pitfalls
- **Catalog patches do NOT persist** across image updates. Always Step 4 after every update.
- **Don't `docker compose down -v`** — that removes volumes and wipes the DB.
- **Stray pricing schemas**: some entries use 2-field `{input:N,output:M}` without `cached`. Regex catches the named fields but verify with the grep check.
- **Cache lag**: dashboard may show old prices for ~30s after restart. Hard-refresh browser (Ctrl+Shift+R) before declaring failure.
- **New models on update**: review the dashboard counter — if "PRICED" suddenly jumps, the update added models. Override them.
- **⚠️ CRITICAL: sed-patching minified JS is fragile and can break unrelated pages.** The regex `(input|output|cached|reasoning|cache_write):[0-9]+` can match property names in unrelated code (not just pricing objects), corrupting JS syntax. In a real incident, sed-patching server chunks 11203/44021/95577/30038/68131 caused the `/dashboard/costs` Overview page to crash with `ReferenceError: t is not defined` in a *client-side* React chunk — even though only *server-side* chunks were patched. The crash was in chunk `4bd1b696` (React internals), triggered during hydration because the server-rendered RSC payload was corrupted by the broken server chunk.
- **DB-only zero pricing is sufficient and safer.** The 828 DB overrides make the Pricing page (`/dashboard/costs/pricing`) show $0 without any JS patching. The JS catalog patch was only cosmetically needed for the Costs Overview page (`/dashboard/costs`), which has its own upstream rendering bug in v3.8.42 anyway. **Recommendation: skip Step 4 entirely and rely on DB overrides only.**
- **Server chunks ≠ client chunks.** In Next.js, server-side rendering chunks live in `/app/.build/next/server/chunks/` and client-side chunks in `/app/.build/next/static/chunks/`. They are completely independent. Patching server chunks does NOT affect client-side rendering — but corrupted server chunks CAN cause client-side React errors via bad RSC payload.
- **Chunk list is dynamic.** The original skill listed only 3 chunks (11203, 44021, 95577). Post-update, 2 additional chunks (30038, 68131) also contained pricing data. Use `grep -l` to discover all chunks dynamically rather than hardcoding.
- **`docker compose force-recreate` proves upstream vs self-inflicted.** If an error persists after `force-recreate` from the same image, it's an upstream bug (the container filesystem is fresh from the image). Use this to distinguish your patches from image-level issues.
- **Post-update relay verification is mandatory for Cloudflare users.** Do not stop at `docker pull` + healthy container. After any OmniRoute update that may affect relay deploy, verify the generated Cloudflare worker path too. In particular, v3.8.47 carried PR #6496's Service Worker/body_part fix but still shipped a second generated-script bug: the emitted worker body contained `target.replace(/\\/$/, "") + relayPath`, which Cloudflare rejected with `Uncaught SyntaxError: Invalid regular expression flags at worker.js:64:48`. Quick verifier: inspect `/app/.build/next/server/chunks/_05gd49m._.js` line ~64 inside the container, or parse the emitted script from source in a separate Node process. If the bad regex is present and a full source rebuild is blocked, derive a local hotfix image from the current official digest, patch the source file + compiled server chunk in-place, then point compose at that local image and recreate. See `references/cloudflare-relay-regex-hotfix-v3.8.47.md`.
- **If upstream `latest` moves before your Cloudflare fix merges, update by rebuilding the LOCAL hotfix on top of the NEW official digest instead of switching back to upstream `latest`.** Safe pattern: (1) backup project + pin current image, (2) `docker buildx imagetools inspect diegosouzapw/omniroute:latest` to get the new remote digest, (3) patch `Dockerfile.cloudflare-relay-hotfix` `FROM diegosouzapw/omniroute@sha256:<new_digest>`, (4) `docker pull diegosouzapw/omniroute:latest`, (5) build a fresh local tag like `omniroute:cf-relay-hotfix-YYYYMMDD`, (6) update compose to that local tag, (7) recreate, (8) re-check the live compiled chunk still shows `targetBase = target.endsWith("/") ? target.slice(0, -1) : target;` and `fetch(targetBase + relayPath, init)`. Do **not** temporarily revert compose to upstream `latest` while the PR is still unmerged.
- **Direct Cloudflare relay probes should follow OmniRoute's CURRENT field-encryption scheme, not an older ad-hoc decrypt script.** The durable source of truth is `src/lib/db/proxies/mappers.ts` `extractRelayAuth(...)` plus `src/lib/db/encryption.ts`. If a hand-written probe script returns decrypt failures after an update, first re-check those source files before concluding the relay token is bad.
- **If the local hotfix proves an upstream regression, open a clean follow-up PR from the actual target branch, not from the earlier PR branch.** In this case the right base was `release/v3.8.47`, not the old working branch used for PR #6496. Workflow: create a fresh branch from the real target branch, carry only the upstream-worthy files, and rerun the focused Cloudflare relay tests there. Important pitfall: the target branch may still lack pieces that were merged elsewhere (for v3.8.47, the Cloudflare deploy route still needed `body_part` metadata alignment even though PR #6496 was merged). Verify the focused test suite on the clean branch before opening the PR. See `references/cloudflare-relay-regex-hotfix-v3.8.47.md`.

## Diagnosing Next.js page errors in OmniRoute
When a page shows "Internal Server Error" but `curl` returns HTTP 200:
1. The error is in **client-side React hydration**, not server-side rendering.
2. Check browser console (not server logs) for the actual JS error.
3. If the error is in a chunk you never patched, it's likely an **upstream bug**.
4. `docker compose force-recreate` creates a fresh container from the image — if the error persists, it's confirmed upstream.
5. Other pages (Dashboard, Pricing, Providers) working fine confirms the issue is page-specific, not systemic.

## Long-term hardening (not yet implemented)
Two persistence options to discuss with user later:
1. **Bind-mount** patched chunks into the container via `docker-compose.yml`:
   ```yaml
   volumes:
     - ./patches/11203.js:/app/.build/next/server/chunks/11203.js:ro
     - ./patches/44021.js:/app/.build/next/server/chunks/44021.js:ro
     - ./patches/95577.js:/app/.build/next/server/chunks/95577.js:ro
     - ./patches/30038.js:/app/.build/next/server/chunks/30038.js:ro
     - ./patches/68131.js:/app/.build/next/server/chunks/68131.js:ro
   ```
   Risk: new image versions may rename the chunks (hashes change). Bind mount would then mask the wrong file.
2. **Entrypoint wrapper**: small `entrypoint-zero-pricing.sh` that runs the sed loop on container start, then exec's the original entrypoint. More robust against chunk renames if the script searches for any chunk containing pricing objects.

## Incident log
See `references/costs-overview-crash-june-2026.md` for the full diagnosis of the Costs Overview page crash caused by an upstream OmniRoute v3.8.42 bug (not the agent's patches).

## Verification checklist after every update
- [ ] DB backup created and timestamped
- [ ] Compose/env backups created
- [ ] Old image tag pinned
- [ ] Container up and UI reachable
- [ ] Pricing page (`/dashboard/costs/pricing`) shows $0 for all providers (DB overrides)
- [ ] If JS catalog patches were applied: verify no pages broken (check `/dashboard/costs`, `/dashboard/costs/pricing`, `/dashboard`)
- [ ] No new unpriced model gaps in dashboard counter
- [ ] Chat completions still route correctly (`docker compose logs --tail 10 omniroute`)

## Check for new releases BEFORE answering "is there an update?"

When the user asks "is there an update for omniroute?", do not trust whatever `git tag --list "v3.8.5*"` returns locally. Upstream tags are often missing until a forced fetch. The pattern that works:

```bash
cd /mnt/tb/1Apps/omniroute-repo
git fetch upstream --tags --force 2>&1 | tail -5
git tag --list "v3.8.5*" --sort=-v:refname | head -3
```

**Real failure mode that bit during v3.8.50 check:** initial `git tag --list` returned only `v3.8.5` (not `v3.8.50`). The user had to provide the GitHub release URL before I correctly identified the version lag. `git fetch --tags --force` is mandatory before any "latest version" claim.

After fetching, compare running container's version (`docker exec omniroute cat /app/package.json | grep version`) against the highest tag. If the **running container is below the highest tag**, run `update.sh`. If they're equal, no action needed.

If the local HEAD commit is `vX.Y.Z-N-g<sha>` (unreleased commits past a tag), note that too — the build may already contain fixes not yet released.
