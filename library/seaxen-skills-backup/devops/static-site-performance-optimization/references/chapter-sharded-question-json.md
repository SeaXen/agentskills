# Recipe Q — Chapter-sharded question JSON (exam / flashcards)

**When:** static quiz app loads 5–15 MB JSON on "Start" but users usually pick 1–15 chapters.

**Rebuild (Python):**

```python
shard_dir = SITE / 'questions-by-chapter'
for kind, rows in [('mcq', mcq), ('sba', sba), ('flashcard', flash)]:
    by_num = defaultdict(list)
    for r in rows:
        by_num[r['chapter_num']].append(r)
    for num, chunk in by_num.items():
        (shard_dir / f'{num}-{kind}.json').write_text(
            json.dumps(chunk, ensure_ascii=False, separators=(',', ':')), encoding='utf-8')
```

**Loader heuristic:** `chapterNums.length > 0 && chapterNums.length <= 32` → parallel fetch shards; else monolith. (Raised from 15 so system-based ch 16–32 and all-chapter picks avoid monolith.)

**Topic without chapter chip:** infer `chapter_num` from `topic_slug` prefix (`16-…` / `16.…`) and pass `[16]` as `chapterNums` — see `references/topic-scoped-exam-flash-load.md`.

**Verify:**

```bash
wc -c site/assets/questions-flashcard.json
wc -c site/assets/questions-by-chapter/10-flashcard.json
curl -s -w '%{size_download}\n' -o /dev/null http://127.0.0.1:8855/assets/questions-by-chapter/10-flashcard.json
```

**Pitfall:** exam-engine caching full bank then filtering in JS still parses the whole file — shards must be selected at fetch time. Remove stale `DB._mcq` early-return when `chapterNums` differs.

## Deploy sync (when `docker build` times out)

Large `site/` trees often exceed build timeouts on DietPi/i3 hosts. Sync without rebuild:

```bash
chmod -R a+rX /path/to/site
cd /path/to/site && tar cf - . | docker exec -i CONTAINER tar xf - -C /usr/share/nginx/html/
docker cp docker/nginx.conf CONTAINER:/etc/nginx/conf.d/default.conf
docker exec CONTAINER nginx -t && docker exec CONTAINER nginx -s reload
docker exec CONTAINER find /usr/share/nginx/html -type f -exec chmod 644 {} \;
docker exec CONTAINER find /usr/share/nginx/html -type d -exec chmod 755 {} \;
```

**403 on assets after cp:** files landed as mode **600** (root-only). `chmod 644` on files / `755` on dirs inside container. Fix host perms before tar if source is `600`.

Cross-ref: `medsea-question-bank-audit` / `interactive-quiz-tools`.