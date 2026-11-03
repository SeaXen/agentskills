# AceRoute CPU bursts (DietPi host)

**App path:** `/mnt/tb/1Apps/AceRoute`  
**Container:** `aceroute` · `network_mode: host` · `uvicorn app:app --port 8866`  
**Related skill:** `learnables/aceroute-system`

## Symptom

User reports Python/uvicorn “always” using 10–30% CPU. Reality on this host:

- **Always-on** yes
- **Steady 10–30%** no
- **Bursty**: 1s samples often `0 0 0 45 100 99 0…`

Also watch logs for repeating:

```text
Bitwarden Secrets Manager: applied 25 secrets
```

## A/B stop/remeasure

Only when the user asks:

```bash
# baseline sample (prefer Python /proc — shell lines with "uvicorn" may be blocked)
docker stats --no-stream aceroute
docker stop aceroute
# remeasure host top CPU 8–12s
docker start aceroute   # or: cd /mnt/tb/1Apps/AceRoute && docker compose up -d
```

Note: if you sample between bursts, stop may look like “no effect.” Use 10–20×1s samples on the container PID.

## Root causes

1. **Dashboard warm loop** (`app.py` `_background_refresh_loop`) every `ACEROUTE_DASH_REFRESH_SECONDS` (default **60**): warms **8 dashboards × 4 windows** against large Hermes `state.db`.
2. **Tools analytics sync** every `ACEROUTE_TOOLS_SYNC_SECONDS` (default **120**).
3. **Journey item prefetch** (`JourneyItemCache`): up to **12** `hermes journey edit <id>` subprocesses every 5 min. Each Hermes CLI start loads `~/.hermes` + Bitwarden Secrets Manager (~25 secrets) → multi-second core pin.
4. Docker healthcheck `/api/healthz` every 30s is cheap — not the main issue.

## Fix applied on this host (2026-07-23)

`docker-compose.yml` env:

- `ACEROUTE_DASH_REFRESH_SECONDS=300`
- `ACEROUTE_DASH_CACHE_TTL_SECONDS=300`
- `ACEROUTE_TOOLS_SYNC_SECONDS=300`
- `ACEROUTE_SKILLS_REFRESH_SECONDS=900`
- `ACEROUTE_JOURNEY_REFRESH_SECONDS=900`
- `ACEROUTE_JOURNEY_PREFETCH_LIMIT=4`
- **`ACEROUTE_JOURNEY_CLI_PREFETCH=0`** (main BWS spam kill)

`collectors.py`:

- Skills/journey intervals env-configurable
- Journey CLI background prefetch default **OFF** (on-demand API still works)

Post-fix check: aceroute ~**0–1%** avg over 20s; BWS line once at startup only.

## Do not

- Confuse host DietPi with a physical laptop
- Leave Aceroute stopped after diagnosis unless user wants it off
- Run multi-minute host network tests while debugging CPU (Discord offline risk)
