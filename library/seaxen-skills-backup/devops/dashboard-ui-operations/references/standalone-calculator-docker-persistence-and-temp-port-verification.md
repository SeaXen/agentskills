# Standalone calculator: Docker persistence and temporary-port verification

Use this when extending a small Dockerized trading/calculator dashboard that already has a user-known primary port.

## Durable rules

### 1) Keep the configured primary port stable
If the app normally lives on a known host port (for example `8788`), treat that as the operator-facing truth.

Verification shape:
- inspect `docker-compose.yml` or the service definition for the published host port
- confirm the live listener with `ss -ltnp`
- confirm the serving container/process with `docker compose ps` or equivalent
- in the final report, state clearly which port is the real one

### 2) Temporary verification ports are fine — but must stay temporary
It is valid to run a direct Python/server process on an alternate port (for example `8091`) to test features without disturbing the Docker service.

But:
- label it explicitly as a temporary verification port
- do not leave it running as an apparent second app
- kill it after testing
- verify that the intended main listener is still the original configured port

This avoids confusing the user into thinking the app was migrated to a second port.

### 3) Do not call persistence complete until Docker storage is real
If the app stores saves/backups under an internal app path like `/app/data` but Docker has no bind mount or named volume, rebuild/recreate can wipe the data.

Before claiming saved positions / backups are durable:
- inspect compose for a volume mapping
- if absent, warn plainly that container-local storage is not persistent across rebuild/recreate
- recommended minimum fix: bind-mount the app data directory (for example `./data:/app/data`)

### 4) Rich saved-state features should share one payload model
If the app adds:
- per-position coin logo
- exchange/source badge
- folders/tags
- CSV export
- backup/restore snapshot archives

keep them all derived from the same saved-position payload rather than inventing separate portfolio/export models.

Minimum good shape:
- saved positions persist full metadata
- portfolio view renders from those saved positions
- CSV export includes metadata columns such as `exchange`, `folder`, and `tags`
- backup creation writes timestamped archives
- restore reads those same archives back into the live saved-position store

### 5) For compact dashboard passes, verify visually on the live primary port
For layout cleanup work:
- verify the live served page, not only the edited files
- check that the oversized header/hero is actually gone
- check that the main workflow reads clearly left-to-right/top-to-bottom
- note any remaining imbalance honestly instead of calling it perfect too early

## Good final-report shape
- explain why two ports appeared
- restate the real permanent port
- confirm the temporary test port is no longer running
- summarize layout improvements
- state whether persistence is truly durable or still container-local
