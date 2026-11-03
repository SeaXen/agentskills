# Phoenix local backend for `hermes_otel`

Use this when `hermes_otel` is enabled but the dashboard shows errors like:
- `502 backend not enabled`
- `No trace backend configured`
- OTEL export failures to `127.0.0.1:6006`
- blank Phoenix UI on `localhost:6006`

## Key distinction

There are usually **two different web UIs** involved:

- **Hermes dashboard** — often on a Hermes port such as `9119` (sometimes via nginx/reverse proxy) or the direct app port (for example `9120`)
- **Phoenix OTEL UI** — the tracing backend on `6006`

Do not confuse a working Hermes dashboard with a working Phoenix backend.

## Durable diagnostic pattern

1. Confirm the plugin is enabled:
   - `hermes plugins list`
2. Check `~/.hermes/plugins/hermes_otel/config.yaml`
   - common local Phoenix config:
     ```yaml
     query_backend: phoenix
     backends:
       - type: phoenix
         endpoint: http://127.0.0.1:6006/v1/traces
     ```
3. Check whether anything is listening on `6006`
4. If exports/logs show `Connection refused` to `127.0.0.1:6006`, the plugin is configured but **Phoenix is not running**
5. If the Hermes dashboard OTEL tab errors, also remember that dashboard auth/proxy errors on the Hermes side are separate from the Phoenix backend health

## Start Phoenix locally

From the plugin bundle:

```bash
docker compose -f ~/.hermes/plugins/hermes_otel/docker-compose/phoenix.yaml up -d
```

The bundled compose file maps:

```yaml
services:
  phoenix:
    image: arizephoenix/phoenix:latest
    ports:
      - "6006:6006"
```

## Make it survive reboot / Docker restart

Prefer both of these:

1. Add restart policy in the compose file:
   ```yaml
   restart: unless-stopped
   ```
2. Apply it to the already-created container too:
   ```bash
   docker update --restart unless-stopped docker-compose-phoenix-1
   ```

Then recreate/start again:

```bash
docker compose -f ~/.hermes/plugins/hermes_otel/docker-compose/phoenix.yaml up -d
```

## Verification

Good checks:

```bash
curl http://127.0.0.1:6006/
curl -H 'Content-Type: application/json' \
  -d '{"query":"{ projects(first: 5) { edges { node { id name hasTraces } } } }"}' \
  http://127.0.0.1:6006/graphql
docker inspect -f '{{.HostConfig.RestartPolicy.Name}}' docker-compose-phoenix-1
```

Expected signals:
- root page responds (HTML is fine)
- GraphQL returns projects
- restart policy is `unless-stopped`

## Practical note

The first few seconds after startup may show connection resets while Phoenix finishes migrations. If the port is bound and logs show startup/migrations, retry after a short wait before concluding it failed.
