# Fixing SearXNG Provider URL After Network Mode Changes

## Problem
When SearXNG's Docker networking changes (e.g., from port mapping to `network_mode: host`), the saved provider connection URL in OmniRoute's SQLite DB becomes stale. The dashboard shows:
- `Network error` / `fetch failed`
- `error` test_status

## Diagnosis
```bash
sqlite3 -header -column /mnt/tb/1Apps/omniroute/data/storage.sqlite \
  "SELECT id, provider, name, test_status, last_error, provider_specific_data 
   FROM provider_connections WHERE provider='searxng-search';"
```
Check `provider_specific_data` → `baseUrl` field. If it points to a dead port (e.g., `127.0.0.1:8888`), that's the problem.

## Fix
Update the `baseUrl` in `provider_specific_data` JSON using SQLite's `json_set`:
```bash
sqlite3 /mnt/tb/1Apps/omniroute/data/storage.sqlite \
  "UPDATE provider_connections 
   SET provider_specific_data=json_set(provider_specific_data, '$.baseUrl', 'http://127.0.0.1:8080/search'),
       updated_at=datetime('now') 
   WHERE provider='searxng-search';"
```

Verify the change:
```bash
sqlite3 -header -column /mnt/tb/1Apps/omniroute/data/storage.sqlite \
  "SELECT test_status, last_error, provider_specific_data, updated_at 
   FROM provider_connections WHERE provider='searxng-search';"
```

Test from inside OmniRoute container:
```bash
docker compose exec -T omniroute node -e \
  'fetch("http://127.0.0.1:8080/search?q=test&format=json",{signal:AbortSignal.timeout(8000)})
   .then(async r=>{console.log("status",r.status); const t=await r.text(); console.log(t.slice(0,400));})
   .catch(e=>{console.log("ERR",e.name,e.message); process.exit(1);});'
```

Then click "Retest" in the dashboard or restart OmniRoute. Status should change to `active` / `connected`.

## Current Working Endpoint
- SearXNG with `network_mode: host`: **`http://127.0.0.1:8080/search`**
- Old port-mapped endpoint (dead after host networking): `http://127.0.0.1:8888/search`
