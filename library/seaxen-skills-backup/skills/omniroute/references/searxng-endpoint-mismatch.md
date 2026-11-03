# SearXNG endpoint mismatch after switching to host networking

Problem class: OmniRoute `searxng-search` provider shows `network issue` / `Network error` / `fetch failed` even though SearXNG itself is up.

## Symptom pattern

- SearXNG was changed from bridged Docker networking with a published port like `8888:8080` to `network_mode: host`.
- Search starts working again when queried directly on `127.0.0.1:8080`.
- OmniRoute provider page still shows an error.
- OmniRoute logs show `ECONNREFUSED 127.0.0.1:8888`.
- The saved provider connection still has `provider_specific_data.baseUrl = http://127.0.0.1:8888/search`.

## Quick proof steps

1. Test the old and new URLs from inside the OmniRoute container.
2. Query the provider record:

```bash
sqlite3 -header -column /mnt/tb/1Apps/omniroute/data/storage.sqlite \
  "select id, provider, name, test_status, last_error, provider_specific_data, updated_at
   from provider_connections
   where provider='searxng-search';"
```

3. Compare the saved `baseUrl` against the URL that really returns HTTP 200.

## Known-good fix

```bash
sqlite3 /mnt/tb/1Apps/omniroute/data/storage.sqlite \
  "update provider_connections
   set provider_specific_data=json_set(provider_specific_data, '$.baseUrl', 'http://127.0.0.1:8080/search'),
       updated_at=datetime('now')
   where provider='searxng-search';"
```

Then hit **Retest** in OmniRoute.

## Expected post-fix state

- DB record: `test_status = active`
- DB record: `provider_specific_data.baseUrl = http://127.0.0.1:8080/search`
- UI state: `connected`
- Old `127.0.0.1:8888` endpoint remains dead unless a separate port mapping is restored
