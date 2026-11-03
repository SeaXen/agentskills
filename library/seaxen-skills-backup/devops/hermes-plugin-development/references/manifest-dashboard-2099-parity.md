# Manifest :2099 vs Hermes manifest-history plugin

Self-hosted Manifest on **2099** is a SPA + NestJS APIs. Hermes **manifest-history** is a sidebar tab on **9119** with `plugin_api.py` + SQLite archive.

## Probed endpoints (LAN, no browser cookie)

| Path | HTTP | Notes |
|------|------|--------|
| `/api/v1/history` | 404 | Do not use for archive |
| `/api/v1/messages` | 401 | Wants `X-API-Key`; `mnfst_` Bearer invalid here |
| `/api/v1/overview` | 200 | `summary`, `cost_by_model`, `has_data` — often empty without dashboard login session |
| `/api/v1/providers` | 200 | `model_counts` = global vendor catalog sizes (not tenant connections) |

`POST /v1/chat/completions` + `Authorization: Bearer` + `mnfst_` works for routing; does **not** unlock dashboard analytics.

## Postgres (what :2099 uses)

| UI | Tables / fields |
|----|-----------------|
| Overview | `agent_messages` aggregations via `/api/v1/overview` |
| Providers | `tenant_providers` (+ `label`, `is_active`) |
| Models list | `tenant_providers.cached_models` JSON |
| Traffic | `agent_messages` |

Typical small install: 13 messages, 9 tenant_providers, 3 providers with traffic, ~447 model IDs in cached_models.

## Hermes plugin

| Action | Source |
|--------|--------|
| Cron / Fetch now | Postgres `agent_messages` → SQLite |
| Usage stats | SQLite |
| Providers tab | `tenant_providers` merge + usage |
| Models tab (v1.3.3+) | `cached_models` catalog + usage |
| Overview top models | By **token use**, usage-only top 8 |

## Gaps unless extended

- No `/api/v1/overview` timeseries without session cookie or SQL reimplementation
- `model_counts` on `/api/v1/providers` ≠ tenant `cached_models`
- Not real-time until Fetch now / cron

## Verify

```bash
docker exec mnfst-postgres-1 psql -U manifest -d manifest -c \
  "SELECT tp.label, COUNT(am.id) FROM tenant_providers tp LEFT JOIN agent_messages am ON am.tenant_provider_id = tp.id GROUP BY tp.id, tp.label;"
```

Distroless `mnfst-manifest-1` — SQL via postgres container; HTTP via host curl.