# AceRoute SearXNG engine panel — empty /stats fallback

## Symptom

Search tab → **🌐 SearXNG Engines** shows **Unavailable** (or empty), while SearXNG search works and `curl http://127.0.0.1:8080/stats` returns 200.

## Diagnose

```bash
curl -s 'http://127.0.0.1:8080/stats' | grep -i 'no data'
curl -s 'http://127.0.0.1:8866/api/health' | python3 -c "
import sys,json; d=json.load(sys.stdin)
print('source', d.get('searxng_source'), 'count', len(d.get('searxng_engines',[])))
print('note', (d.get('searxng_note') or '')[:200])
"
```

If `/stats` contains **no data available** and `searxng_source` is **`config`**, behavior is expected until traffic exists.

If `searxng_source` is **`disabled`**, AceRoute is in **Hermes-only Search** mode (`ACEROUTE_SEARCH_SOURCE=hermes`). Card is hidden in UI; set `ACEROUTE_SHOW_SEARXNG=1` to show it again.

## Backend contract (post-fix)

`collect_searxng_engines()` returns:

```json
{
  "engines": [...],
  "source": "stats" | "config" | "error" | "none",
  "note": "human-readable",
  "searxng_url": "http://127.0.0.1:8080"
}
```

Config fallback rows: `status: "listed"`, `score: "—"`, `result_count` = engine shortcut or `general`.

## UI

- `#searxngEngineNote` shows `searxng_note` when present.
- LISTED badge (blue) for config-sourced rows.
- Do not append `s` to `response_time` when value is `—`.

## Git reference

AceRoute commit `37a8659` — `fix: SearXNG engines fallback when /stats has no data`.