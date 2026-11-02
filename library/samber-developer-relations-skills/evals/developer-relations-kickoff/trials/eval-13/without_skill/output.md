The core problem is architectural, not tonal: one page is trying to do "teach a concept" and "prove a result fast" at once, and neither reader gets what they came for. The fix is a fork — a short landing page that splits immediately, feeding into two purpose-built pages that never make one audience wade through the other's content. Here's the full rewrite, ready to paste into the docs.

---

## `/docs/getting-started` — Getting Started

# Getting Started with Wolfsbane Analytics

Wolfsbane replicates tables from your production databases into your warehouse in near real time, using log-based change data capture — no batch jobs, no query load on your primary.

Where do you want to start?

### → I've never used CDC before
[**How Replication Works**](/docs/getting-started/how-replication-works) — what change data capture actually does, how Wolfsbane reads your database without touching production traffic, and what happens when something breaks. 8-minute read, no account required.

### → I already run CDC somewhere else
[**Replicate Your First Table in 10 Minutes**](/docs/getting-started/quickstart) — connect a source, pick one table, watch rows land in your warehouse. No background reading required.

Not sure which one? Start with *How Replication Works* — you can jump into the quickstart from there at any point, and nothing in it assumes you've read the concepts page first.

---

## `/docs/getting-started/quickstart` — Quickstart

# Replicate Your First Table in 10 Minutes

Connect one source table to your warehouse and watch a live change propagate. No reading required — if you want the "why" behind any step, each one links to the relevant page in [How Replication Works](/docs/getting-started/how-replication-works).

| | |
|---|---|
| **Time** | 10 minutes |
| **Result** | One table, streaming, visible in your warehouse |

## Prerequisites

| Requirement | Notes |
|---|---|
| A source database | PostgreSQL, MySQL, SQL Server, or MongoDB. This guide uses PostgreSQL; MySQL steps are noted inline. |
| Admin access to that database | To create a replication role once. |
| A warehouse | Snowflake, BigQuery, Redshift, or Databricks. |
| A Wolfsbane account | [Sign up free](/signup) — no card required for the trial. |

## Step 1: Create a replication user on your source

Wolfsbane reads your database's transaction log directly — it never polls tables with `SELECT` queries. That requires a dedicated, low-privilege user.

**PostgreSQL** (run once, as a superuser):

```sql
CREATE ROLE wolfsbane_replicator WITH REPLICATION LOGIN PASSWORD 'use-a-strong-password';
GRANT SELECT ON ALL TABLES IN SCHEMA public TO wolfsbane_replicator;
```

If `wal_level` isn't already `logical`, set it and restart:

```sql
ALTER SYSTEM SET wal_level = logical;
```

(On RDS or Cloud SQL, set `rds.logical_replication` / the equivalent parameter group flag instead — no server restart needed on RDS.)

You don't need to create a replication slot or publication yourself — Wolfsbane creates a dedicated one per connection in Step 2.

**MySQL:** enable `binlog_format=ROW`, then:

```sql
CREATE USER 'wolfsbane_replicator'@'%' IDENTIFIED BY 'use-a-strong-password';
GRANT REPLICATION SLAVE, REPLICATION CLIENT, SELECT ON *.* TO 'wolfsbane_replicator'@'%';
```

## Step 2: Connect your source

In Wolfsbane, go to **Sources → New Source**, pick your database type, and enter:

- Host, port, database name
- The `wolfsbane_replicator` credentials from Step 1
- Network path: direct, SSH tunnel, or private link

Click **Test Connection**. Wolfsbane verifies it can reach the transaction log and creates its replication slot at this point — nothing streams yet.

## Step 3: Connect your destination warehouse

Go to **Destinations → New Destination**, choose your warehouse, and provide a service account or role with `CREATE TABLE` and `INSERT`/`MERGE` privileges on one target schema. Wolfsbane writes only to that schema.

## Step 4: Pick one table and start the sync

Go to **Pipelines → New Pipeline**, select the source and destination you just created, and pick a single table — something small (under 100k rows) makes the initial backfill finish inside a minute or two.

Click **Start**. Wolfsbane runs an initial snapshot of the table, then switches to streaming from the log automatically — you don't trigger that switch manually.

## Step 5: Checkpoint — watch it land

Once the pipeline status reads **Streaming**, query the table in your warehouse:

```sql
SELECT count(*) FROM your_schema.your_table;
```

The count should match your source table.

Now make the moment that actually proves it: go back to your source database and update one row.

```sql
UPDATE your_table SET status = 'shipped' WHERE id = 1;
```

Re-run the count/select in your warehouse. The change typically appears within 30–60 seconds — no re-sync, no manual trigger.

🎉 **That's it.** You have one table streaming from production into your warehouse, and you just watched a real change move end to end.

## Troubleshooting

**"permission denied for replication slot"** — the `wolfsbane_replicator` role is missing the `REPLICATION` attribute, or `wal_level` isn't `logical`. Re-check Step 1.

**Connection test times out** — your database isn't reachable from Wolfsbane's IP range. Add [Wolfsbane's IP allowlist](/docs/reference/ip-allowlist) to your firewall/security group, or switch to an SSH tunnel in Step 2.

**Pipeline stuck at "Snapshotting"** — normal for large tables; check **Pipelines → [your pipeline] → Logs** for progress percentage. For tables over a few million rows, expect minutes, not seconds — this quickstart intentionally uses a small table to stay inside 10 minutes.

**Destination write fails with a permissions error** — the warehouse role from Step 3 needs `CREATE TABLE` on the target schema, not just `INSERT`; Wolfsbane creates the destination table on first sync.

**Changes aren't showing up in the warehouse after the update test** — check **Pipelines → [your pipeline] → Status**. If it reads "Error: replication slot inactive," your source's WAL/binlog retention window is shorter than the pipeline's downtime — see [Replication Lag & Retention](/docs/reference/replication-lag).

## Next steps

- [How Replication Works](/docs/getting-started/how-replication-works) — the model behind what you just watched happen, including what happens on schema changes and failures.
- [Add more tables to this pipeline](/docs/guides/adding-tables)
- [Set up alerting on pipeline health](/docs/guides/monitoring)

---

## `/docs/getting-started/how-replication-works` — How Replication Works

# How Replication Works

If you've never run change data capture before, the two questions that matter before you point this at production are: *what does Wolfsbane actually do to my database*, and *what happens when something goes wrong*. This page answers both. If you'd rather see it run first and read this after, the [10-minute quickstart](/docs/getting-started/quickstart) doesn't require anything on this page.

## What change data capture is

Most tools that move data between systems work by querying your database on a schedule — "give me all rows changed since last time" — and re-running that query every few minutes or hours. This has two problems: it misses deletes (a `DELETE` leaves no trace for a `SELECT` to find), and every poll runs a real query against your production tables, competing with your application for locks and I/O.

Change data capture takes a different approach: instead of asking your database questions, it reads the transaction log your database already writes for every insert, update, and delete — the same log PostgreSQL uses for replication, or MySQL uses for its own replicas. Every change your application makes is already recorded there, in order, before CDC ever gets involved.

## How Wolfsbane reads your database

Wolfsbane attaches to that log the same way a read replica would — through PostgreSQL's logical replication slots or MySQL's binlog protocol — rather than running queries against your tables.

Concretely, that means:

- **No `SELECT` load on your primary during steady-state streaming.** The one exception is the initial snapshot (see below), which does read existing rows once.
- **No locks.** Reading the log doesn't block writes or other readers.
- **Typical source overhead is under 1% CPU** for the log reader itself, independent of your table sizes — the cost scales with your write volume, not your data volume.
- **The replication user needs read access and log-streaming privileges, nothing more.** The setup in the quickstart grants `SELECT` and `REPLICATION`, not admin rights.

## The two phases every pipeline goes through

**1. Initial snapshot.** The first time you replicate a table, there's no log history covering rows that already existed before you connected Wolfsbane — so Wolfsbane reads the table once, in parallel chunks, to seed the destination. This is the only phase that queries your table directly, and it's throttled to a configurable rate so it doesn't compete with production traffic.

**2. Streaming.** Once the snapshot catches up to the current log position, Wolfsbane switches to tailing the log continuously. Every subsequent insert, update, and delete arrives as an event, in the order it committed on the source, typically landing in your warehouse within 30–60 seconds.

Wolfsbane tracks exactly where it is in your source's log (its LSN, for PostgreSQL, or binlog position/GTID, for MySQL) as a durable checkpoint. If the pipeline restarts for any reason, it resumes from that checkpoint rather than the current log position — so a restart doesn't create gaps or duplicate a full re-snapshot.

## What guarantees you actually get in the warehouse

Log events can, in principle, be delivered more than once — that's an inherent property of resuming from a checkpoint after any kind of interruption. Wolfsbane doesn't pass that risk on to your warehouse tables: every change is merged into the destination keyed on the source table's primary key and ordered by log position, so a redelivered event overwrites itself with the same result rather than producing a duplicate row. What you query in the warehouse is exactly-once, even though what travels the pipe is at-least-once.

This does mean every replicated table needs a primary key. Tables without one can still be replicated, but only as append-only change logs rather than merged current-state tables — Wolfsbane tells you which mode a table will use before you start the pipeline.

## What happens when things go wrong

**Network interruption between Wolfsbane and your source.** The pipeline reconnects and resumes from its last checkpoint. Your source's log retention window (`wal_keep_size` on Postgres, `binlog_expire_logs_seconds` on MySQL) needs to cover the outage, or the checkpoint falls outside available history — Wolfsbane alerts you before that happens, not after.

**Source database restart.** Transparent. The log survives a restart; Wolfsbane reconnects and resumes.

**A column is added or dropped on the source.** Wolfsbane detects the schema change from the log itself and propagates additive changes (new columns) automatically. Anything that isn't safely additive — a column type change, a dropped primary key — pauses the pipeline and alerts you rather than guessing; nothing about how Wolfsbane resolves ambiguous schema changes is silent.

**Warehouse is unreachable.** Wolfsbane keeps consuming and buffering from the source log (bounded by your plan's buffer window) and retries delivery; it does not fall back to re-reading the source to catch up, since the checkpoint already tells it exactly where to resume.

## Security model

- Credentials are encrypted at rest and never appear in logs or the UI after entry.
- Connections use TLS in transit by default; SSH tunnel and private link (PrivateLink/VPC peering) are available where direct access isn't acceptable.
- The replication user Wolfsbane asks you to create has read and log-streaming access only — never write access to your source, and no requirement to be a superuser after the one-time `wal_level` setup.
- Wolfsbane's source IP ranges are published for allowlisting: [IP Allowlist Reference](/docs/reference/ip-allowlist).

## Ready to see it work

Everything above describes the model — the fastest way to trust it is to watch it. The quickstart connects one real table and shows you a change propagate end to end in under a minute.

[**Replicate your first table in 10 minutes →**](/docs/getting-started/quickstart)