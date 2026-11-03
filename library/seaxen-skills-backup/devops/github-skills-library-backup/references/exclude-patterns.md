# Exclude patterns (with reasoning)

Use these `--exclude` flags when staging the skills library. Each entry has a one-line reason. Strip count + size from the 2026-08-15 audit of SeaXen's `/root/.hermes/skills/`.

## Required excludes (always apply)

| Pattern | What | Approx size | Reason |
|---|---|---:|---|
| `.hub/` | Hermes internal index cache (40 MB index-cache + taps.json) | 40 MB | Regenerable from `~/.hermes/skills/` on next start |
| `.curator_backups/` | Old hermes-curator backup archives | 22 MB | Already-backup-of-the-backup; clutters the new backup |
| `*.log` | Runtime logs from Hermes + scripts | varies | One `browser_dashboard.log` was 86 MB; GitHub warns at 50 MB |
| `__pycache__/` | Python bytecode cache | <1 MB | Regenerable on next import |
| `*.pyc` | Compiled Python | <1 MB | Same |
| `.DS_Store` | macOS Finder metadata | trivial | Noise |

## Hermes runtime state (rsync pulls, must be gitignored separately)

`rsync` doesn't know these are runtime state. Pull the whole tree first, then either add to `.gitignore` BEFORE `git add .` OR `git rm -r --cached -f` after the first commit + amend.

| Path | What | Why strip |
|---|---|---|
| `.archive/` | Hermes archive directory | Runtime state, regenerable |
| `.bundled_manifest` | Hermes manifest cache | Runtime state |
| `.curator_state` | Hermes curator state file | Runtime state |
| `.usage.json` | Usage telemetry | Personal data + runtime |
| `.usage.json.lock` | Lock file for usage.json | Runtime |

## Credentials (verify BEFORE staging, STOP if any)

```bash
find /root/.hermes/skills \( -name '.env*' -o -name '*.pem' -o -name '*.key' -o -name 'credentials*' \) -not -path '*/node_modules/*'
```

If this returns anything:

1. **STOP** the backup
2. Tell the user what's there and where
3. Ask whether to:
   - Add to `.gitignore` and exclude
   - Add to exclude without gitignore (rsync-level only)
   - Leave in the backup (user's risk)

Common hits (none observed on SeaXen's box 2026-08-15, but defensive):

- `.env` files under `mcp-servers/` or custom integrations
- `*.pem` from a TLS cert experiment
- `credentials.json` from a Discord bot test

## Excludes that are NOT a good idea

| Pattern | Why not |
|---|---|
| `node_modules/` | Some skill bundles **ship** `node_modules` for a reason (pinned binaries, build artifacts the agent runs without `npm install`). Audit each instance. |
| `*.lock` | lockfile is small and useful for restoration |
| `*.pyc` (already excluded) | — |
| `LICENSE*` | Per-repo LICENSE files are part of the IP trail |
| `__pycache__/` (already excluded) | — |

## Sanity checks post-staging

```bash
STAGE=/tmp/hermes-skills-backup-$(date +%Y%m%d)

# 1. No big files snuck through
find "$STAGE" -type f -size +50M -not -path '*/.git/*' | head

# 2. No credentials snuck through
find "$STAGE" \( -name '.env' -o -name '*.pem' -o -name '*.key' -o -name 'credentials*' \) | head

# 3. Stripped size is reasonable (~79 MB expected for SeaXen's box)
du -sh "$STAGE"

# 4. Manifest + INDEX survived
test -f "$STAGE/_verbatim-manifest.json" && echo "manifest OK"
test -f "$STAGE/INDEX.md" && echo "INDEX OK"
test -f "$STAGE/learnables/INDEX.md" && echo "learnables INDEX OK"
```

If any of those fail, fix the staging before proceeding to push.
