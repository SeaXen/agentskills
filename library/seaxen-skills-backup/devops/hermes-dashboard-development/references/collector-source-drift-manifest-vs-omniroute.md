# Collector Source Drift: stale named product DB vs real live traffic source

## When this matters
Use this when a dashboard/plugin archive job is named after one product (`manifest-history`, etc.) but the host's actual live inference traffic may now be flowing through another system.

## Symptom pattern
- Cron/script runs successfully but archived rows stop at an old date.
- The source DB is not just missing one table's writes — multiple core tables are stale.
- The dashboard/plugin name biases you into debugging the wrong backend.

## Concrete case
In this session:
- `manifest_history_archive` cron was fixed first by converting it to `no_agent=true`.
- The deeper issue was that local Manifest Postgres was stale overall:
  - `agent_messages` newest row: 2026-06-29
  - `session` newest row: 2026-06-29
  - `token_usage_snapshots`: 0 rows
  - `cost_snapshots`: 0 rows
- Hermes config still had a Manifest custom provider, but it pointed to cloud Manifest inference (`https://app.manifest.build/v1`), not the local self-hosted dashboard API/database.
- The host's real current request archive was OmniRoute call logs at:
  - `/mnt/tb/1Apps/omniroute/data/call_logs`

## Debug order
1. Verify the job wrapper first.
   - If an LLM-backed cron drifted, convert pure collectors to `no_agent=true`.
2. Verify the collector source freshness.
   - Check newest timestamps in the source DB/logs.
   - Check more than one table if using Postgres/SQLite.
3. Verify active traffic topology.
   - Compare current Hermes/custom provider config vs local services.
   - Check whether the named product is still the live path or just an old leftover deployment.
4. If the named source is stale overall, stop trying to repair it.
   - Repoint the collector to the system that actually has current traffic.

## Practical rule
If a data collector's source DB has stale timestamps across multiple core tables, assume source drift before assuming a broken query.

## Applied fix in this session
- Patched `/root/.hermes/scripts/manifest_history_fetch.py`
- Added `sync_source = "omniroute"`
- Read OmniRoute JSON call logs instead of stale local Manifest Postgres
- Updated `/root/.hermes/state/manifest_history_config.json` to use:
  - `sync_source: "omniroute"`
  - `omniroute_logs_dir: "/mnt/tb/1Apps/omniroute/data/call_logs"`

## Why this matters
The durable lesson is not "Manifest is broken".
The durable lesson is: collector jobs and dashboard plugins can outlive architecture changes, so always verify the live traffic source before debugging the old named backend.
