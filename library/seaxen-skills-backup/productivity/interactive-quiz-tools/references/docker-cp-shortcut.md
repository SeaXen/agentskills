# Docker-Cp Shortcut for Static-Site Iterations

**The fast way to deploy new files to a static-site container (validated 2026-06-21 on `medsea` container at port 8855).**

## The problem

The MedSea container is built with `COPY site/` in the Dockerfile — NOT a bind mount. Files added to the host `site/` directory do NOT appear in the running container. The two deployment paths are:

| Method | Time | When to use |
|---|---|---|
| `docker build --no-cache + restart` | ~5 minutes (1.2 GB site) | Final deployment, before container restart |
| `docker cp + chmod -R a+r` | ~3 seconds | During development iteration |

For interactive quiz/flashcard UIs, you iterate on the JS/HTML frequently. A 5-minute rebuild per change is unacceptable. Use `docker cp` during development; do a full rebuild before any production container restart.

## The shortcut

```bash
# 1. Copy new files
docker cp /mnt/tb/Sea-knowledge/#MedSea/site/exam medsea:/usr/share/nginx/html/exam
docker cp /mnt/tb/Sea-knowledge/#MedSea/site/flashcards medsea:/usr/share/nginx/html/flashcards
docker cp /mnt/tb/Sea-knowledge/#MedSea/site/assets/questions.json medsea:/usr/share/nginx/html/assets/questions.json
docker cp /mnt/tb/Sea-knowledge/#MedSea/site/assets/exam-engine.js medsea:/usr/share/nginx/html/assets/exam-engine.js

# 2. CRITICAL — fix permissions
docker exec medsea chmod -R a+r /usr/share/nginx/html/exam /usr/share/nginx/html/flashcards /usr/share/nginx/html/assets

# 3. Verify
curl -s -o /dev/null -w "%{http_code} %{size_download}b\n" http://localhost:8855/exam/
curl -s -o /dev/null -w "%{http_code} %{size_download}b\n" http://localhost:8855/assets/questions.json
```

The `deploy_to_medsea.sh` script in `scripts/` wraps this.

## The `chmod -R a+r` pitfall (CRITICAL)

`docker cp` preserves the source file permissions. If the host file is `600` (often happens with files written via `write_file` tool which uses restrictive defaults), nginx in the container runs as the `nginx` user (uid 101) and CANNOT read those files.

**Symptom:** `GET /exam/` returns `403 Forbidden` even though the file exists. The error in nginx logs is `Permission denied`.

**Fix:** `docker exec medsea chmod -R a+r <new-dirs>` after every `docker cp`.

**Alternative:** If you're about to do a full `docker build`, you can set perms on the host first (`chmod -R a+r /path/to/site/{exam,flashcards,assets}`) — the COPY step preserves them. But during `docker cp` iteration, you have to do it inside the container.

## The `-p 8855:80` port mapping rule (CRITICAL)

The MedSea container's `EXPOSE 8855` directive in the Dockerfile is documentation only. The actual nginx config inside the container listens on **port 80** (default nginx behavior):

```nginx
server {
    listen 80;
    listen [::]:80 ipv6only=on;
    server_name _;
    root /usr/share/nginx/html;
    ...
}
```

So the docker port mapping must be **host:container = 8855:80**:

```bash
docker run -d --name medsea --restart unless-stopped -p 8855:80 medsea-site:latest
```

**NOT** `-p 8855:8855` — that maps host 8855 to container 8855, but nothing inside the container listens on 8855. The container will be "Up" but `curl http://localhost:8855/` will hang or return `HTTP 000` (connection refused, no response).

Verified twice in one session (initial deploy + post-rebuild redeploy, 2026-06-21). Always run after a container recreate:

```bash
docker ps --format '{{.Names}}\t{{.Ports}}' | grep medsea
# MUST show: medsea   0.0.0.0:8855->80/tcp
# If shows medsea   8855/tcp (no host mapping) or 0.0.0.0:8855->8855/tcp, the port mapping is wrong.
```

## Pretty-URL routing (no rewrites needed)

The MedSea nginx config has this `try_files` directive:

```nginx
location / {
    try_files $uri $uri/ $uri/index.html /index.html;
}
```

This means `GET /exam/` will try, in order:
1. The exact file `/exam/` (404 unless you have a file literally named `exam`)
2. The directory `/exam/` with `index.html` inside (this is what works for `/exam/`)
3. The file `/exam/index.html` (also works)
4. The root `/index.html` (fallback)

So `GET /exam/` and `GET /exam/index.html` both serve the same file. No rewrite rules needed. Just create the directory and drop `index.html` in it.

## Why not bind-mount the site?

The MedSea container was designed to bake the site into the image (1.2 GB). A bind mount would:
- Slow file I/O for the nginx worker (4,000+ topic files served per request)
- Require the host site/ to be in a known location (brittle for container restarts)
- Make the image non-portable (can't `docker save` it)

`docker cp` during development + full image rebuild for production is the right tradeoff.

## When to do a full rebuild (NOT just docker cp)

Use `docker build --no-cache` for:
- Adding/chapter renames (chapters/16-cardiology/, etc.) — `docker cp` can copy directories but large recursive copies are slow
- Changing nginx config (port, gzip, cache headers) — config is baked into the image
- Changing the Dockerfile (new dependencies, COPY changes)
- Production deployment where you want the image to be self-contained
- Before `docker save` / `docker push` / cross-host migration

Use `docker cp` for:
- Single file changes (HTML, JS, CSS)
- Adding new directories with 5-20 files (interactive tools, asset bundles)
- Iterating on UI/UX without waiting for full rebuild
- A/B testing two versions of the same file

## Build context size warning

`docker build` for MedSea takes ~5 minutes because the COPY step processes 1.2 GB (mostly PNGs in `chapters/*/diseases/*/topic.png`). If you're iterating on just JS/HTML, always use `docker cp` — a full rebuild for a 1-line JS change wastes 5 minutes.

If you MUST do a full rebuild and don't need PNGs (e.g. JS-only changes), you can speed it up with a `.dockerignore`:

```gitignore
# In /mnt/tb/Sea-knowledge/#MedSea/.dockerignore
chapters/**/diseases/*/topic.png
chapters/**/diseases/*/topic.html
site/**/topic.png
site/**/topic.html
```

This drops ~80% of the build context size. Don't use this for production builds (you need the PNGs for the website), but useful for JS-only iteration.
