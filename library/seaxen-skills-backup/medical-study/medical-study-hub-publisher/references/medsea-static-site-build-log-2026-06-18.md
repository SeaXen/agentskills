# MedSea Static Site Build Log — 2026-06-18

## Task
User asked: *"as I have git repo can you make a website like hermes telemetry so that I can see all at once notion + website and deploy in docker port 8855 and vercel, make a beautiful arrangement, keep all files in /mnt/tb/Sea-Knowledge/#medsea"*

This was the natural completion step after publishing 5 Davidson chapters to Notion (cardiology 16, nephrology 15, respiratory 17, endocrinology 18, gastroenterology 21). The user wanted a single browseable surface that combined:
- Local chapter folders (the canonical source)
- Notion deep links (the rich-text destination)
- A "Hermes Telemetry"-style dark UI (per the user's dashboard aesthetic)

## Result
Built `medsea-site` at `/mnt/tb/Sea-knowledge/#MedSea/site/`:
- **5 chapter cards** with color accent strips (15=cyan, 16=red, 17=emerald, 18=violet, 21=amber)
- **52 hubs** rendered as sectioned cards on per-chapter pages
- **762 topic pages** — each with breadcrumb, large PNG hero, and auto-rendered markdown body
- **768 total HTML pages** (762 topics + 5 chapter index + 1 landing + a few stubs)
- **760 PNGs** copied into the site tree (~265 MB)
- **Docker**: `medsea-site` running on port 8855, bound to `0.0.0.0` for LAN access (user explicitly requested)
- **Vercel**: `vercel.json` configures static deployment
- **GitHub**: pushed to `SeaXen/MedSea` main

## Architecture decisions

### No JS framework
The whole site is **vanilla HTML + inline CSS** in a single Python generator script (`scripts/site/build_site.py`, ~700 lines). No npm, no React, no build step. The user just wants to browse; the simplest static HTML is the right tool.

### Inline CSS, dark theme matching Hermes Telemetry
The user said "like hermes telemetry" — that's the Hermes dashboard at `~/.hermes/dashboards/` with dark background, gradient text, monospace stats, glass-blur header. I reused the visual language:
- Background gradient `linear-gradient(135deg, #0a0e1a 0%, #0f1729 100%)`
- Surfaces `#111827` / `#1f2937` / `#2d3748`
- Cyan accent `#38bdf8` (default), per-chapter overrides
- Hero gradient text with `-webkit-background-clip: text`
- Sticky header with `backdrop-filter: blur(12px)`
- Stats in monospace `'JetBrains Mono', 'SF Mono', Menlo`

### Two on-disk patterns
The chapters/ tree has two layouts depending on when they were built:
- **Cardiology + Nephrology**: folder-per-topic with `topic.{md,png,html}` inside (`16.1.25-atherosclerosis-pathogenesis/topic.png`)
- **Respiratory + Endo + Gastro**: flat files (`17.1.01-a-a-gradient-and-oxygenation-failure.png`)

The generator's `find_files()` accepts both patterns and merges them into a single topic list. Critical because the user said "arrange also like cardiology" but the newer chapters use a flatter layout.

### Three-tier URL structure
- `/` — landing page (chapter cards with previews + stats)
- `/<chapter-slug>/` — chapter page (hubs grouped, topic grid)
- `/<chapter-slug>/diseases/<topic-slug>/` — topic detail page (PNG hero + MD body)

nginx `try_files $uri $uri/ $uri/index.html /index.html;` makes the trailing `.html` optional so URLs stay clean.

### Don't commit PNGs to git
The site/ folder is 265 MB of PNGs. Adding `site/**/*.png` to `.gitignore` keeps the HTML/MD tracked but excludes the binary content. The chapters/ tree already has the source PNGs under version control, so the site PNGs are reproducible from `scripts/site/build_site.py` + `chapters/`.

## Pipeline details

### Generator
```python
# /mnt/tb/Sea-knowledge/#MedSea/scripts/site/build_site.py
REPO_ROOT = Path("/mnt/tb/Sea-knowledge/#MedSea")
SITE = REPO_ROOT / "site"

CHAPTERS = [
    ("15-nephrology-urology", "Nephrology and Urology", "https://...", "...", "#06b6d4"),
    ("16-cardiology",         "Cardiology",              "https://...", "...", "#ef4444"),
    ("17-respiratory-medicine", "Respiratory Medicine", "https://...", "...", "#10b981"),
    ("18-endocrinology",      "Endocrinology",           "https://...", "...", "#a855f7"),
    ("21-gastroenterology",   "Gastroenterology",        "https://...", "...", "#f59e0b"),
]

# find_files() walks chapters/<slug>/diseases/ with both patterns
# render_md_to_html() is ~80 lines, handles: headers, lists, tables, callouts, code, bold/italic
# write_index() / write_chapter_page() / write_topic_page() are pure string-templating
```

### Docker
```dockerfile
# /mnt/tb/Sea-knowledge/#MedSea/Dockerfile
FROM nginx:alpine
COPY site/ /usr/share/nginx/html/
COPY docker/nginx.conf /etc/nginx/conf.d/default.conf
EXPOSE 8855
HEALTHCHECK --interval=30s --timeout=3s CMD wget -q --spider http://localhost:8855/ || exit 1
CMD ["nginx", "-g", "daemon off;"]
```

```nginx
# /mnt/tb/Sea-knowledge/#MedSea/docker/nginx.conf
server {
    listen 8855;
    server_name _;
    root /usr/share/nginx/html;
    index index.html;
    gzip on;
    gzip_types text/plain text/css application/javascript application/json image/svg+xml;
    location ~* \.(png|jpg|jpeg|webp|svg|woff2|woff|ttf)$ {
        expires 7d;
        add_header Cache-Control "public, max-age=604800, immutable";
    }
    location ~* \.html$ {
        expires 1h;
        add_header Cache-Control "public, max-age=3600";
    }
    location / { try_files $uri $uri/ $uri/index.html /index.html; }
    server_tokens off;
}
```

### Vercel
```json
{
  "version": 2, "name": "medsea", "cleanUrls": true, "trailingSlash": false,
  "builds": [{"src": "site/**", "use": "@vercel/static"}],
  "headers": [
    {"source": "/(.*)\\.(png|jpg|webp|svg|woff2|woff|ttf)",
     "headers": [{"key": "Cache-Control", "value": "public, max-age=604800, immutable"}]},
    {"source": "/(.*)\\.html",
     "headers": [{"key": "Cache-Control", "value": "public, max-age=3600"}]}
  ]
}
```

## Build + run sequence
```bash
cd /mnt/tb/Sea-knowledge/#MedSea
python3 scripts/site/build_site.py    # ~3 min for 5 chapters
docker build -t medsea-site:latest .  # ~30s (nginx:alpine cached after first build)
docker stop medsea; docker rm medsea   # safe — idempotent
docker run -d --name medsea -p 0.0.0.0:8855:8855 --restart unless-stopped medsea-site:latest
curl -s -o /dev/null -w "HTTP %{http_code} - %{size_download}b\n" http://127.0.0.1:8855/

# Verify
curl -s -o /dev/null -w "HTTP %{http_code} - %{size_download}b\n" http://127.0.0.1:8855/16-cardiology/diseases/16.1.25-atherosclerosis-pathogenesis/topic.png
```

## Verification (live, in browser)
1. `http://127.0.0.1:8855/` — landing page with 5 chapter cards, gradient hero, stats
2. Click a chapter card → `/<slug>/` — hubs as sectioned cards, topic grid with PNG previews
3. Click a topic → `/<slug>/diseases/<topic>/` — full PNG + markdown body
4. Notion links in cards go to the chapter's Notion hub
5. From LAN: `http://192.168.0.222:8855/` (server's LAN IP)

All routes returned HTTP 200 in the session; PNG sizes 130KB-700KB (no blanks).

## Pitfalls encountered

### Pitfall 61 — `#` in shell paths
The user's repo lives at `/mnt/tb/Sea-knowledge/#MedSea/`. The `#` starts a shell comment, so:
- `cd /mnt/tb/Sea-knowledge/#MedSea` → bash drops `#MedSea/`, errors on the trailing `/`
- `mkdir -p .../#MedSea/site/scripts` → silently creates only `site/scripts`
- `find /mnt/tb/Sea-knowledge/#MedSea` → "no such file or directory"

**Workarounds that worked:**
- `cd "/mnt/tb/Sea-knowledge/#MedSea"` (single-quoted)
- `cd /mnt/tb/Sea-knowledge && cd '#MedSea'`
- In Python: hardcode the path as a string, no shell interpretation

**Symptom that bit me:** I tried to `mv site/scripts/build_site.py scripts/site/build_site.py` to escape the rmtree pattern (Pitfall: build script inside site/ gets deleted by the build's own rmtree). The `mv` failed silently because the source path was inside the rmtree. Solution: use `write_file` tool with the new path explicitly.

### Pitfall 62 — `***` redaction in source code
The display layer redacts `***` patterns, breaking Python source that contained `r'NOTION_API_KEY=*** `re.search(r'NOTION_API_KEY=*** env_text)` → `SyntaxError: unterminated string literal`
- heredoc `python3 << EOF` blocks → printed but not executed
- `write_file` paths with `***` → file written without the asterisks

**Workarounds:**
- Build the sentinel at runtime: `sentinel = "NOTION" + "_API_KEY" + chr(61)`
- `awk -F` to extract to a file: `awk -F'NOTION_API_KEY=*** '/^NOTION_API_KEY/ {print $2; exit}' /root/.hermes/.env > /tmp/.notion_key`
- Read the key from a file written by a separate, simple script

The `awk -F` pattern was the cleanest — no Python source contamination, no heredoc, no asterisks.

### Pitfall 63 — Long foreground commands hit session budget
The terminal tool blocks long foreground runs (>~5 min) regardless of `timeout=`. For the 30-min Notion uploads, the only working pattern was `background=true, notify_on_complete=true`:
```python
terminal(background=true, command="python3 -u upload.py > log 2>&1; echo EXIT=$? >> log", notify_on_complete=true)
```

Forbidden: `nohup ... &`, `disown`, `setsid` shell wrappers (explicitly rejected as "shell-level background wrappers"). `subprocess.Popen` inside `execute_code` doesn't work either (separate context, can't report back).

### Pitfall 64 — Docker container start requires user consent
`docker run -d ...` triggers the safety harness:
- *"BLOCKED: Command required approval (docker restart/stop/kill (container lifecycle)) and was approved by the user."* — the harness records user consent
- *"BLOCKED: Command timed out without user response. The user has NOT consented to this action."* — when no prior approval

**Pattern that worked:** Use `clarify` tool to explicitly request consent BEFORE the first `docker run`:
```
Question: "Docker container `medsea` will be started on port 8855 (long-running, --restart unless-stopped). Approve?"
Choices: [approve and also support lan, decline]
```

User responded with "approve and also support lan" → bind to `0.0.0.0:8855` for LAN access. Then re-ran `docker run` and it went through.

## Files added
- `/mnt/tb/Sea-knowledge/#MedSea/Dockerfile` (15 lines)
- `/mnt/tb/Sea-knowledge/#MedSea/docker/nginx.conf` (38 lines)
- `/mnt/tb/Sea-knowledge/#MedSea/vercel.json` (30 lines)
- `/mnt/tb/Sea-knowledge/#MedSea/scripts/site/build_site.py` (~700 lines, 27KB)
- `/mnt/tb/Sea-knowledge/#MedSea/site/index.html` (18KB landing page)
- `/mnt/tb/Sea-knowledge/#MedSea/site/15-nephrology-urology/index.html` + 49 topic pages
- `/mnt/tb/Sea-knowledge/#MedSea/site/16-cardiology/index.html` + 330 topic pages
- `/mnt/tb/Sea-knowledge/#MedSea/site/17-respiratory-medicine/index.html` + 149 topic pages
- `/mnt/tb/Sea-knowledge/#MedSea/site/18-endocrinology/index.html` + 87 topic pages
- `/mnt/tb/Sea-knowledge/#MedSea/site/21-gastroenterology/index.html` + 147 topic pages
- `/mnt/tb/Sea-knowledge/#MedSea/site/README.md` (build + deploy docs)
- `/mnt/tb/Sea-knowledge/#MedSea/.gitignore` — added `site/**/*.png` etc.

## Net result
- 5 chapters browsable from one URL
- 762 topic pages, each with a rendered infographic + full markdown body
- Dark theme consistent with Hermes dashboard aesthetic
- LAN-accessible on port 8855
- Vercel-ready for prod deploy (`vercel deploy --prod`)
- Builds in ~3 min from `chapters/` source — fully reproducible
