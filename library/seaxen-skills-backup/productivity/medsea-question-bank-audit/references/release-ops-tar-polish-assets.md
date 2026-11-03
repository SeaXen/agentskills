# Tar deploy — include header polish assets

When shipping UI-only changes without full `docker build`, extend the usual tar list:

```bash
chmod -R a+rX site/
cd site && tar cf - \
  sw.js index.html exam flashcards \
  assets/site-header.js assets/site-header.css \
  assets/site-header-polish.css assets/medsea-header-stats.js \
  assets/questions-index.json assets/exam-engine.js \
  | docker exec -i medsea tar xf - -C /usr/share/nginx/html/
```

Always bump `sw.js` `CACHE_VERSION` when HTML/JS/CSS changes. Run `bash scripts/medsea_release_check.sh` when bank JSON changed; for CSS-only deploy, still `node --check assets/site-header.js`.

403 on `site-db.js` or assets: host `chmod -R a+rX site/` before tar; container `chmod 644` on deployed files.