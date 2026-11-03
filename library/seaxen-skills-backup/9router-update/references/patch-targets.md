# Patch targets — what `apply-usage-periods.py` actually edits

The patch is **not** a one-liner. It edits **8 distinct files** across 2 layers (browser bundle + server runtime), because Next.js compiles the same source into two trees:

- `/app/.next/static/chunks/` — the **client-side** JS that runs in the browser
- `/app/.next/server/` — the **server-side** code that runs in Node.js, including API routes

If you miss either layer, the user sees one of these failure modes:

- UI selector shows 90D/180D/365D/All but the chart is empty → server allowlist not patched
- Chart works but selector is back to 7d/30d/60d → client bundle not patched
- Both show old options but `curl /api/usage/stats?period=90d` returns 400 → stats API not patched

## The 8 files

### Client-side (browser bundle)

| File pattern | What it controls | Pattern patched |
|--------------|------------------|-----------------|
| `/app/.next/static/chunks/5497-*.js` | Main app bundle — period dropdown UI in usage page | `OLD_UI` → `NEW_UI` |
| `/app/.next/static/chunks/app/(dashboard)/dashboard/usage/page-*.js` | Usage page entry chunk (Next.js page-level bundle) | `OLD_UI` → `NEW_UI` |

These two are the ones the **user's browser** downloads.

### Server-side runtime

| File | What it controls | Pattern patched |
|------|------------------|-----------------|
| `/app/.next/server/chunks/412.js` | Shared server chunk (Next.js server bundle) | `OLD_UI` → `NEW_UI` |
| `/app/.next/server/app/(dashboard)/dashboard/usage/page.js` | Server-rendered usage page | `OLD_UI` → `NEW_UI` |
| `/app/.next/server/app/api/usage/stats/route.js` | Stats API allowlist | `Set(["today","24h","7d","30d","60d","all"])` → adds `90d, 180d, 365d` |
| `/app/.next/server/app/api/usage/chart/route.js` | Chart API allowlist | `Set(["today","24h","7d","30d","60d"])` → adds `90d, 180d, 365d, all` |
| `/app/.next/server/chunks/4884.js` (stats-map) | Period → day-count map | `{"7d":7,"30d":30,"60d":60}` → adds `90d, 180d, 365d, all:null` |
| `/app/.next/server/chunks/4884.js` (chart-days) | Chart day-aggregation branching | adds 90d/180d/365d branches + all-mode |

The last file is patched **twice** in the same script (once for stats-map, once for chart-days), because both code paths live in the same compiled chunk.

## The OLD_UI and NEW_UI constants

```python
OLD_UI = '{value:"7d",label:"7D"},{value:"30d",label:"30D"},{value:"60d",label:"60D"}'
NEW_UI = (
    '{value:"7d",label:"7D"},{value:"30d",label:"30D"},{value:"60d",label:"60D"},'
    '{value:"90d",label:"90D"},{value:"180d",label:"180D"},{value:"365d",label:"365D"},'
    '{value:"all",label:"All"}'
)
```

Note the **trailing context**: OLD_UI ends at `60D"}'` and the grep must find that exact 47-character string. If upstream renames the labels (e.g. `7D` → `7d`), the patch will silently fail. To debug, run:

```bash
docker exec 9router sh -c \
  "grep -rlF '\"7d\",\"30d\",\"60d\"' /app/.next/static/chunks/ 2>/dev/null"
```

If zero results, upstream changed the structure — see "When upstream breaks the patch" below.

## How the script finds the right chunks

```python
def ui_bundle_paths():
    r = subprocess.run(
        ["docker", "exec", C, "sh", "-lc", f"grep -rlF {OLD_UI!r} /app/.next 2>/dev/null || true"],
        capture_output=True, text=True,
    )
    return [line for line in r.stdout.splitlines() if line]
```

The script does a **recursive grep** for the exact OLD_UI string, then patches every file that matches. This is why it works across Next.js version bumps — the chunk filenames change, but the period selector text is stable (until upstream renames the labels).

The 4 hard-coded server paths (`/app/.next/server/...`) are *not* discovered by grep; they're written into the script. If upstream renames or moves a server route, the script's `read()` returns `None` and the patch is silently skipped. This is the most common silent-failure mode — always verify in the post-update checklist (`SKILL.md` step 3).

## When upstream breaks the patch

If the script reports `WARN no match` or `skip missing ...` for any of the 4 server paths, the structure changed. Recover:

```bash
# 1. Find the new usage API route paths
docker exec 9router sh -c \
  "find /app/.next/server/app/api/usage -name '*.js' 2>/dev/null"

# 2. Find the new chunk that holds the period map
docker exec 9router sh -c \
  "grep -rl '\"7d\":7' /app/.next/server/ 2>/dev/null"

# 3. Update the script and re-run
```

The OLD_UI pattern is much more stable because it's user-facing label text. The server-side allowlist strings are more likely to be touched by upstream refactors.

## Idempotency

The script is safe to run twice in a row. The second run prints `already stats-api` / `already chart-api` for every path that already contains NEW_UI. This makes it harmless to call from a CI or post-update hook.
