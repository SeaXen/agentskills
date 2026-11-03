# MedSea live browser verification (`:8855`)

Use when Dr. Sagar asks "did you verify in browser?" or before claiming exam/flashcards/header polish is done.

## Minimum probe (exam + topic URL)

1. **curl** (ground truth on server):
   - `grep CACHE_VERSION` in live `sw.js`
   - `curl -w '%{http_code} %{size_download}\n'` on `/assets/exam-engine.js`, `/assets/topic-bank-index.json`
   - `curl /exam/` includes `medsea-chapter-filter.js` and `exam-engine.js?v=N` if cache-bust deployed

2. **Browser** (after SW unregister or hard refresh):
   - Navigate to **`/exam/index.html?topic=…&authored=1`** (not only `/exam/?…` — SW may serve stale HTML shell).
   - `browser_console` expression:
     ```javascript
     JSON.stringify({
       MedSea: !!window.MedSea,
       MedSeaDB: !!window.MedSeaDB,
       chapterFilter: !!window.MedSeaChapterFilter,
       topicBank: !!window.MedSeaTopicBank,
       topic: document.getElementById('topic-filter')?.value,
       avail: document.getElementById('avail-count')?.textContent,
       summary: document.getElementById('setup-summary')?.textContent,
       authored: document.getElementById('authored-only')?.checked,
       ch16: !!document.querySelector('#ch-chips .chip[data-ch="16"].selected'),
       scripts: document.scripts.length
     })
     ```
   - **Pass:** `MedSea: true`, `chapterFilter: true`, `topicBank: true`, topic filled, avail not `—`, summary mentions `Topic · … · Ch N`, scripts ≥7.
   - Click **Start Exam →** — runner shows `Q 1 · Ch N`.
   - If `btn-start.textContent` becomes `Loading Ch 16…` then stays stuck, the shard fetch is failing — see *Shard fetch failure diagnosis* below.

3. **Flashcards:** same URL shape on `/flashcards/index.html?topic=…&authored=1` — topic field + matching count + Start → runner.

4. **Home stats:** navigate to `/?_cb=N`, check:
   ```javascript
   JSON.stringify({
     ch: document.getElementById('stat-chapters')?.textContent,
     mcq: document.getElementById('stat-mcq')?.textContent,
     sba: document.getElementById('stat-sba')?.textContent,
     flash: document.getElementById('stat-flash')?.textContent,
     quality: document.getElementById('stat-quality')?.textContent
   })
   ```
   Expect: `32`, `11,314`, `8,318`, `14,723`, `75.5%` (or current).

5. **Chapter page:** navigate to `/16-cardiology/?_cb=N`, click a topic link, verify mindmap renders:
   ```javascript
   JSON.stringify({
     topic: document.querySelector('.topic-detail') ? 'loaded' : 'not loaded',
     mindmap: !!document.querySelector('.mindmap'),
     mmRoot: document.querySelector('.mm-root')?.textContent
   })
   ```

## P0 runtime trap: `exam-engine.js` throws before `window.MedSea`

If `MedSea` is false but scripts loaded, eval the engine in console:

```javascript
fetch('/assets/exam-engine.js?v=N').then(r=>r.text()).then(t=>{
  try { eval(t); return 'ok MedSea='+!!window.MedSea; }
  catch(e) { return e.message; }
})
```

**Known bug (2026-06):** `Format: { … fmtDateTime: fmtDateTime … }` without defining `fmtDateTime` → ReferenceError → **exam and flashcards entirely dead**. Fix: add `function fmtDateTime(iso) { return fmtDate(iso); }` before export.

## Stale HTML in container (2026-06-27)

**Symptom:** Browser shows only 4 scripts (not 7+), `MedSea: false`, old placeholder (`Search 4,000+ topics…` instead of `Search 2,957 topics…`).

**Cause:** You deployed JS/CSS but forgot to include the updated HTML files in the tar. Container still serves old `exam/index.html` without `<script src="/assets/medsea-chapter-filter.js">` etc.

**Diagnose:**
```bash
docker exec medsea grep -c 'medsea-chapter-filter\|medsea-topic-bank\|medsea-header-stats' /usr/share/nginx/html/exam/index.html
# Should be 3+ if fresh; 0 if stale
docker exec medsea grep 'exam-engine.js' /usr/share/nginx/html/exam/index.html
# Should show ?v=17; if no ?v=, HTML is stale
```

**Fix:** Re-deploy ALL changed files including HTML:
```bash
cd /mnt/tb/Sea-knowledge/#MedSea/site && tar cf - \
  sw.js index.html exam/index.html flashcards/index.html \
  assets/site-header.js assets/site-header.css assets/site-header-polish.css \
  assets/medsea-header-stats.js assets/medsea-chapter-filter.js assets/medsea-topic-bank.js \
  assets/exam-engine.js assets/site-db.js assets/chapter.css assets/chapter.js \
  assets/topic-bank-index.json assets/questions-index.json assets/quality-snapshot.json \
  exam/app.js flashcards/app.js \
| docker exec -i medsea tar xf - -C /usr/share/nginx/html/
```

## Shard fetch failure diagnosis (2026-06-27)

**Symptom:** Exam Start button shows `Loading Ch 16…` and never switches to runner panel. No JS errors in console.

**Cause 1: shards missing from container.** The entire `questions-by-chapter/` directory was never deployed.

```bash
docker exec medsea ls /usr/share/nginx/html/assets/questions-by-chapter/ | wc -l
# Should be 77 (32 ch × 3 kinds + index); 0 = missing
```

**Cause 2: directory perms `644`.** Files exist but nginx can't traverse the directory. `try_files` serves `index.html` as fallback → 200 `text/html` instead of JSON.

```bash
docker exec medsea stat -c '%a %n' /usr/share/nginx/html/assets/questions-by-chapter
# Should be 755; if 644, nginx can't traverse
curl -sS -m 5 -o /dev/null -w '%{http_code} %{content_type}' \
  http://127.0.0.1:8855/assets/questions-by-chapter/16-sba.json
# Should be '200 application/json'; if '200 text/html', directory perms bug
```

**Browser-side diagnosis:**
```javascript
fetch('/assets/questions-by-chapter/16-sba.json')
  .then(r => r.json())
  .then(d => JSON.stringify({len: d.length}))
  .catch(e => 'ERR: ' + e.message)
// If ERR: "Unexpected token '<', ..." → serving HTML, not JSON
```

**Fix:**
```bash
# Deploy shards if missing
cd /mnt/tb/Sea-knowledge/#MedSea/site && tar cf - assets/questions-by-chapter | docker exec -i medsea tar xf - -C /usr/share/nginx/html/
# Fix directory perms
docker exec medsea find /usr/share/nginx/html -type d -exec chmod 755 {} \;
docker exec medsea find /usr/share/nginx/html -type f -exec chmod 644 {} \;
```

## Service worker stale assets

- Bumping `CACHE_VERSION` alone may not refresh `exam-engine.js` in automation until unregister:
  ```javascript
  navigator.serviceWorker.getRegistrations().then(r=>Promise.all(r.map(x=>x.unregister()))).then(()=>location.reload())
  ```
- Ship **`exam-engine.js?v=N`** on exam/flashcards HTML when fixing engine bugs.
- User: **Ctrl+Shift+R** until cache shows `medsea-vN`.

## Comprehensive 27-asset post-deploy check

Run after every tar deploy to catch missing files + content-type corruption:

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

Every line must show `200` + correct content-type. JSON showing `text/html` = directory perms bug.

## Honest report shape

| Claim | Requires |
|-------|----------|
| "Topic load fixed" | Browser topic URL + avail count + Start → runner panel |
| "Design polish done" | At least home + exam + one chapter route browsed |
| "Nothing broken" | `!!window.MedSea` on exam page + 0 JS errors + 27-asset check all 200 correct content-type |

Do **not** say "verified in browser" after curl-only or a snapshot with empty topic field. Do **not** say "nothing broken" without checking `window.MedSea` is true on the exam page.
