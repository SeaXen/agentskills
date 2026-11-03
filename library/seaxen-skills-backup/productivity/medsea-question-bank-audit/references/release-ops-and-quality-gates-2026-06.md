# MedSea release ops & quality gates (2026-06-24, updated 2026-06-27)

Live: `:8855` / container `medsea`. Repo site root: `/mnt/tb/Sea-knowledge/#MedSea/site`.

## Pre-deploy gate (required)

```bash
cd /mnt/tb/Sea-knowledge/#MedSea/site
bash scripts/medsea_release_check.sh
```

Runs: `verify_medsea_bank.py`, shard count ≥70, `questions-index.json` has `quality` + per-chapter `authored_mcq` / `authored_sba`, then `rationale_coverage_report.py`. Also `find assets -type d -exec chmod 755` + `find assets -type f -exec chmod 644` on host before tar.

## Rebuild + quality metrics

```bash
python3 scripts/rebuild_question_bank_v5.py   # auto-runs verify_medsea_bank.py at end
python3 scripts/rationale_coverage_report.py  # 80% SBA/MCQ rationale target
python3 scripts/sample_authored_answer_audit.py  # optional: 40-sample answer letter vs topic.md
```

`index.quality` after rebuild:

- `sba_explanation_pct`, `mcq_explanation_pct`, `fc_explanation_pct`
- `sba_autogen`, `sba_authored`, `mcq_authored`
- `sba_expl_from_option`, `mcq_expl_from_option`

Exam setup shows this via `#quality-hint` when index loads. Rebuild writes **`assets/quality-snapshot.json`** for cron/home.

## Content sprint scripts

```bash
python3 scripts/chapters_needing_rationales.py
python3 scripts/suggest_rationale_stubs.py
bash scripts/medsea_weekly_quality.sh   # manual; same output shape as weekly cron
```

Optional Hermes cron (Sundays 09:00): run `medsea_weekly_quality.sh` + terse summary for user — read-only, no deploy unless asked.

## Host thermal pacing

On DietPi / hot laptop: pace **multi-minute** `rebuild_question_bank_v5.py` with `sleep 45–90` between heavy steps if the user's machine thermal-shutdowns mid-rebuild (killed reindex once). Not a correctness rule — ops courtesy.

## Deploy when `docker build` times out

```bash
chmod -R a+rX site
tar cf - -C site . | docker exec -i medsea tar xf - -C /usr/share/nginx/html/
docker cp docker/nginx.conf medsea:/etc/nginx/nginx.conf
docker exec medsea nginx -t && docker exec medsea nginx -s reload
docker exec medsea find /usr/share/nginx/html -type f -exec chmod 644 {} \;
docker exec medsea find /usr/share/nginx/html -type d -exec chmod 755 {} \;
```

**Pitfall:** host `site/assets/*` mode **600** → nginx **403** on `site-db.js`. Always `chmod -R a+rX` before tar.

**Pitfall:** partial tar (only `exam/`) leaves stale monolith JSON — ship `assets/questions-*.json` + `questions-by-chapter/` when bank changed.

**Pitfall (2026-06-27): directory perms `644` → silent JSON corruption.** If you run `find -type f -exec chmod 644` but forget `find -type d -exec chmod 755`, nginx **can't traverse** the `questions-by-chapter/` directory. The `try_files $uri $uri/ /index.html` fallback returns **200 `text/html`** (the site index.html) instead of the JSON file. Browser `fetch().then(r=>r.json())` fails with `Unexpected token '<', "<!DOCTYPE "... is not valid JSON`. The HTTP status is **200**, not 403 — so `curl -w '%{http_code}'` looks fine. **Always check `content_type` not just status code**, and always run **both** chmod commands.

**Pitfall (2026-06-27): stale HTML in container.** Deploying updated JS/CSS (e.g. `exam-engine.js?v=17`) but forgetting to include the updated `exam/index.html` in the tar means the container still serves old HTML without the new `<script>` tags. Browser loads only 4 scripts, `window.MedSea` is false, exam/flashcards dead. **Always include ALL changed files in tar** — HTML, JS, CSS, JSON — not just the last asset you patched.

Bump `sw.js` `CACHE_VERSION` after JS/bank deploy; tell user hard refresh.

## Post-deploy verification (comprehensive)

After tar deploy, run this 27-asset check to catch both missing files AND content-type corruption:

```bash
for url in \
  / /exam/ /flashcards/ /16-cardiology/ \
  /assets/questions-index.json \
  /assets/questions-mcq.json /assets/questions-sba.json /assets/questions-flashcard.json \
  /assets/topic-bank-index.json /assets/quality-snapshot.json \
  /assets/questions-by-chapter/16-sba.json \
  /assets/questions-by-chapter/16-mcq.json \
  /assets/questions-by-chapter/16-flashcard.json \
  /assets/questions-by-chapter/1-sba.json \
  /assets/questions-by-chapter/32-flashcard.json \
  /assets/exam-engine.js /assets/site-db.js /assets/site-header.js \
  /assets/site-header.css /assets/site-header-polish.css \
  /assets/chapter.css /assets/chapter.js \
  /assets/medsea-chapter-filter.js /assets/medsea-topic-bank.js \
  /assets/medsea-header-stats.js \
  /sw.js /manifest.json; do
  code=$(curl -sS -m 5 -o /dev/null -w '%{http_code} %{content_type}' "http://127.0.0.1:8855$url")
  echo "$code $url"
done
```

Every line should show `200` + correct content-type (`application/json` for JSON, `application/javascript` for JS, `text/css` for CSS, `text/html` for HTML). If JSON shows `text/html`, the directory perms bug is present.

## Git hook (optional)

```bash
bash site/scripts/install_git_hooks.sh   # from #MedSea repo root
```

Pre-push runs release check when `site/assets/questions-*` or rebuild script changes.

## Exam UX additions (same deploy)

- `MedSea.showModal` — submit/quit (exam), finish session (flashcards)
- `MedSea.Flagged` — weak queue (`medsea_flagged_v1`); auto-flag misses on submit; **Weak queue only** chip
- `pastest_style_ok` required for `pastest-autogen` in final `choice_ok` filter

## Honest 10/10 ceiling

- Mechanical + deploy verification: **~9** on bank/ops
- Rationale % and clinical truth: **content + expert panel**, not more UI
