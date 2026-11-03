# All-Targets Verification Checklist

**Use this before claiming any sync is complete.** Run `scripts/verify_all_targets.py` after every pipeline run. Hit hard 2026-06-20 when "Notion synced" turned out to mean "36 chapter pages, 0 topic sub-pages".

## The 5+1 Targets

| # | Target | Path / URL | What "synced" means |
|---|--------|-----------|---------------------|
| 1 | **Local source** | `/mnt/tb/Medicine/<Chapter>/` | `.md` files present, `status: full-fcps-mrcp-note` |
| 2 | **Local chapters** | `/mnt/tb/Sea-knowledge/#MedSea/chapters/<slug>/diseases/` | One folder per source note, contains `topic.md` |
| 3 | **Site build** | `/mnt/tb/Sea-knowledge/#MedSea/site/<slug>/topics.json` | `topics[]` count matches chapters count |
| 4 | **Docker live** | `http://localhost:8855/<slug>/topics.json` | HTTP 200, `topics[]` count matches |
| 5 | **Notion DB** | `POST /v1/databases/3805588e-846f-808b-a23b-cf63c89f372e/query` + `GET /v1/blocks/{id}/children` | Row exists for chapter AND child_page count > 0 |
| 6 | **GitHub** | `https://github.com/SeaXen/MedSea` | Last commit includes the chapter |

## Per-Target Verification Commands

```bash
# 1. Local source
ls /mnt/tb/Medicine/Cardiology/ | wc -l

# 2. Local chapters
ls /mnt/tb/Sea-knowledge/\#MedSea/chapters/16-cardiology/diseases/ | wc -l

# 3. Site build (file on disk)
python3 -c "
import json
with open('/mnt/tb/Sea-knowledge/#MedSea/site/16-cardiology/topics.json') as f:
    d = json.load(f)
print(f'Topics: {len(d.get(\"topics\", []))}')
"

# 4. Docker live (HTTP) — IMPORTANT: path is /topics.json, NOT /data/topics.json
curl -s -o /dev/null -w "HTTP %{http_code}\n" http://localhost:8855/16-cardiology/
curl -s http://localhost:8855/16-cardiology/topics.json | python3 -c "
import json, sys
d = json.load(sys.stdin)
print(f'Live topics: {len(d.get(\"topics\", []))}')
"

# 5. Notion (Python — see scripts/verify_all_targets.py)
python3 /root/.hermes/skills/productivity/medsea-publishing-pipeline/scripts/verify_all_targets.py 16

# 6. GitHub
cd /mnt/tb/Sea-knowledge/\#MedSea && git log --oneline -1
git status -s | head
```

## Honest Report Format

When asked "is everything synced?", answer per target, not with a blanket yes. Use this template:

```
✅ Target 1 (local source):    570 files
✅ Target 2 (chapters/):       899 folders
✅ Target 3 (site build):      899 topics in topics.json
✅ Target 4 (docker live):     HTTP 200, 899 topics in live JSON
❌ Target 5 (Notion DB):       1 chapter row, 0 child pages (stub only)
✅ Target 6 (GitHub):          commit e028cb0 pushed to main
```

## Time Costs for Catching Mismatches

| Mismatch | Detection time | Detection cost |
|----------|---------------|---------------|
| local vs chapters (count off) | 10 seconds | `ls \| wc -l` on both |
| chapters vs site (manifest stale) | 30 seconds | rebuild site, recount |
| site vs docker (stale container) | 1 minute | rebuild container, curl |
| **docker vs Notion (page exists ≠ content)** | **5 minutes** | **walk all child_page blocks per chapter** |
| All vs GitHub (push failed) | 30 seconds | `git status`, `git log origin/main..HEAD` |

The Notion check is the slowest — that's exactly why it gets skipped. Make it automatic via `scripts/verify_all_targets.py`.

## What Counts as "Notion Synced"?

Three conditions, ALL must hold:

1. **Chapter page exists in DB** — query `/databases/{MEDSEA_DB}/query`, find a row titled `Chapter N: Title`
2. **Chapter page has child_page blocks** — `blocks/{chapter_id}/children` returns N > 0 child_page items
3. **Each child page has content** — for each child_page, fetch `blocks/{child_id}/children` and confirm > 0 text/heading/code blocks

Condition 1 alone (which most uploader scripts check) proves nothing to the user. Condition 3 is the gold standard but expensive (one API call per topic).

**Pragmatic minimum for "user-visible Notion sync":** conditions 1 + 2 with topic count ≥ 80% of the source.

## nginx `try_files` Gotcha — `/data/topics.json` vs `/topics.json`

The site's nginx config uses `try_files $uri $uri/ $uri/index.html /index.html;` with no specific handler for missing paths. This means `curl /16-cardiology/data/topics.json` returns the rendered index.html with HTTP 200 — it does NOT 404.

**Correct path:** `/16-cardiology/topics.json` (no `/data/` prefix)
**What trips you up:** typical SPA routing convention `/data/topics.json`, but MedSea puts it at the chapter root.

Always test with the actual path the site uses; don't assume standard SPA layout.

## After Every Sync — Minimum Required Checks

```bash
# Local → chapters count match
src=$(ls /mnt/tb/Medicine/<Chapter>/ | wc -l)
chp=$(ls /mnt/tb/Sea-knowledge/\#MedSea/chapters/<slug>/diseases/ | wc -l)
echo "source=$src chapters=$chp"

# Site manifest reflects chapters
st=$(python3 -c "import json; print(len(json.load(open('/mnt/tb/Sea-knowledge/#MedSea/site/$SLUG/topics.json'))['topics']))")
echo "site=$st"

# Docker live reflects site (use correct path!)
live=$(curl -s http://localhost:8855/$SLUG/topics.json | python3 -c "import json,sys; print(len(json.load(sys.stdin)['topics']))")
echo "live=$live"

# Git committed
cd /mnt/tb/Sea-knowledge/\#MedSea && git log --oneline -1
```

If any of these don't match: **fix the pipeline, don't claim success**.

## The `workdir` Shell-Metachar Trap

`workdir` parameter in tool calls blocks paths containing `#` (the `medsea-publishing-pipeline` SKILL.md repo lives at `/mnt/tb/Sea-knowledge/#MedSea`). Errors with: `"Blocked: workdir contains disallowed character '#'. Use a simple filesystem path without shell metacharacters."`

**Workarounds:**
- Omit `workdir` and `cd` inside the command: `bash -c "cd '/path/with/#' && command"`
- Use `cd /mnt/tb/Sea-knowledge/\#MedSea` inside the command body (escape `#` as `\#` in single-quoted shell strings)
- Read/write files by absolute path without `workdir` (works for `read_file`, `write_file`, `patch`)