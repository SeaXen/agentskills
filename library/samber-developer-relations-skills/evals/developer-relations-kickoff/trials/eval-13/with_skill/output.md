Read the kickoff skill and its routing reference in full, then the two sibling skills it points to (`developer-quickstart-guide`, `developer-tutorial`) and their page templates, since the described problem is the textbook case their own routing table names: *"The reader is new to the problem space and needs concepts explained → getting-started guide or teaching tutorial"* vs *"Has never run the thing; needs one verified success fast → quickstart guide"* — two reader states that must never share one page. Splitting is the fix, not better prose on the existing page.

Below is the rewrite: a short forking hub (the page at the current URL), plus the two pages it forks to.

---

## What changed and why

- Old page tried to be quickstart + concept explainer at once — exactly the conflation both sibling skills warn against by name.
- New shape: one hub page that forks in one sentence, a **quickstart** (own infra, ≤10 min, zero theory) for the CDC-experienced half, and a **tutorial** (sandbox, ~20 min, zero production risk) for the CDC-new half.
- I don't have your real CLI syntax, sample-data counts, or latency numbers — everything below is written to the exact shape your engineering owner needs to cold-run and correct before publish (verification list at the end). Per both skills' own pass threshold, an uncold-run page is a draft, not a deliverable — treat every command block below as unverified until someone runs it.

---

# Page 1 — `/docs/getting-started` (the hub)

```markdown
# Getting started with Wolfsbane

Wolfsbane replicates rows from your database into your warehouse the moment they change — no polling, no nightly batch. Pick the path that matches what you need right now.

## I've run change data capture before

**[Replicate your first table →](/docs/getting-started/quickstart)**
Your own Postgres and Snowflake. One table, streaming, in under 10 minutes. You'll walk away with a row in your warehouse you can show your lead.

## I'm new to change data capture

**[See exactly what Wolfsbane does to your data →](/docs/getting-started/how-replication-works)**
A free sandbox, no credit card, nothing pointed at your systems. ~20 minutes. You'll walk away able to explain to your team what happens to a row from commit to warehouse — and why that's safe to trust with production.

Not sure which one? Start with the sandbox. It's the fastest way to trust a pipeline before you point it at anything real.

---

Already mid-pipeline and stuck on something specific? → [Troubleshooting](/docs/troubleshooting)
Need the full list of supported sources and destinations? → [Reference](/docs/reference)
```

---

# Page 2 — `/docs/getting-started/quickstart` (developer-quickstart-guide)

```markdown
# Replicate your first table in 10 minutes

By the end, a row you insert in Postgres will show up in your Snowflake warehouse — streamed, not batched.

## Before you start

- A Postgres database (12+), reachable from Wolfsbane, with logical replication on: check with `SHOW wal_level;` — must return `logical`. Not set? `ALTER SYSTEM SET wal_level = logical;` and restart Postgres (this requires a restart; do it before you start the clock).
- A Postgres role with `REPLICATION` privilege on that database.
- A Snowflake account with a warehouse, database and schema you can write to, plus a personal access token.
- A Wolfsbane account: run `wolfsbane login` (opens your browser, no credit card required).

## 1. Connect your Postgres source

wolfsbane source add postgres orders-db \
  --host db.internal.acme.com \
  --port 5432 \
  --database sales \
  --user wolfsbane_reader \
  --publication wolfsbane_pub

You'll be prompted for the password (it isn't taken as a flag, so it never lands in your shell history).

You should see:

✔ Connected to postgres source "orders-db"
✔ wal_level=logical confirmed
✔ Publication "wolfsbane_pub" created
Source ID: src_4k2m9x

Connection refused? Your database isn't reachable from Wolfsbane's replication IPs yet — see [Network access](/docs/reference/network-access).

## 2. Connect your Snowflake destination

wolfsbane destination add snowflake warehouse-prod \
  --account <YOUR_SNOWFLAKE_ACCOUNT> \
  --warehouse WOLFSBANE_WH \
  --database ANALYTICS \
  --schema RAW \
  --role WOLFSBANE_LOADER

You'll be prompted for a personal access token.

You should see:

✔ Connected to Snowflake account "<YOUR_SNOWFLAKE_ACCOUNT>"
✔ Write access to ANALYTICS.RAW confirmed
Destination ID: dst_9j1p3q

Access denied? The role you passed needs `USAGE` on the warehouse and `CREATE TABLE` on the schema — see [Snowflake permissions](/docs/reference/snowflake-permissions).

## 3. Replicate one table

wolfsbane pipeline create \
  --source orders-db \
  --destination warehouse-prod \
  --table public.orders

You should see:

✔ Pipeline "orders-db.public.orders → warehouse-prod.ANALYTICS.RAW.ORDERS" created
Starting initial snapshot…
✔ Snapshot complete — 48,210 rows copied in 34s
Streaming changes…

Snapshot stuck at 0%? The replication role is missing `SELECT` on `public.orders` — grant it and rerun.

## 4. See it work

In Postgres:

INSERT INTO public.orders (customer_id, item, amount, created_at)
VALUES (482, 'Trail Mix 12-pack', 18.50, now());

In Snowflake, a few seconds later:

SELECT customer_id, item, amount, created_at, _wolfsbane_synced_at
FROM ANALYTICS.RAW.ORDERS
ORDER BY _wolfsbane_synced_at DESC
LIMIT 1;

You should see:

CUSTOMER_ID | ITEM              | AMOUNT | CREATED_AT          | _WOLFSBANE_SYNCED_AT
482         | Trail Mix 12-pack | 18.50  | 2026-09-19 14:02:11 | 2026-09-19 14:02:16

## What just happened

Wolfsbane copied your existing 48,210 rows once — the snapshot. Your insert after that was never queried for; Wolfsbane read it straight off Postgres's write-ahead log and applied it to Snowflake as an upsert.

## Next steps

- [Replicate the rest of your tables](/docs/reference/bulk-tables)
- [See exactly how updates, deletes and schema changes are handled](/docs/getting-started/how-replication-works)
- [Get help](/docs/support)
```

---

# Page 3 — `/docs/getting-started/how-replication-works` (developer-tutorial)

```markdown
# See exactly what Wolfsbane does to your data

By the end of this tutorial, you'll be able to predict what Wolfsbane does to a row — insert, update, delete, or a changed column — from the moment it commits at the source to the moment it lands in your warehouse.

|                       |                                                      |
| --------------------- | ---------------------------------------------------- |
| **Time**              | ~20 minutes                                          |
| **Level**              | New to change data capture                           |
| **You'll need**       | A browser and a free Wolfsbane account               |
| **Assumed knowledge** | Basic SQL (`INSERT` / `UPDATE` / `DELETE`)            |

## What you'll build

A running Wolfsbane pipeline on a sandbox database we provision for you — no credentials of yours involved. You'll watch it replicate into a sandbox warehouse view in real time, then deliberately break things to see how it recovers.

By the end, you'll be able to:

- Predict what a given change at the source does to the warehouse row, before you run it
- Explain why Wolfsbane doesn't need to rescan your table to catch one change
- Explain what happens to a pipeline during a disconnect — and why it doesn't lose or duplicate anything

## Background

Wolfsbane doesn't poll your database on a schedule and diff the results. It reads your database's write-ahead log — the same internal record Postgres itself uses for crash recovery — and turns every committed change into an event, in the order it committed. The first time a table is replicated, Wolfsbane also takes one snapshot of its current contents, so the destination starts complete instead of empty. Everything after that is streamed, one committed change at a time.

## Before you begin

| Requirement          | Check                                  |
| --------------------- | --------------------------------------- |
| Wolfsbane account (free, no card) | [Sign up](/signup)          |

No other setup. The sandbox source and destination are provisioned for you when you start.

## Step 1: Start your sandbox pipeline

From your dashboard, click **New pipeline → Sandbox source**, pick the `orders` sample table, and click **Start**. Wolfsbane provisions a sandbox Postgres database pre-loaded with an `orders` table, and a sandbox warehouse view — and starts replicating immediately.

You should see:

Pipeline pln_sandbox_x7k2
Status: snapshotting… → streaming
Snapshot: 250 rows copied in 4s

## Step 2: Make a change and watch it stream

Open the **Source SQL console** tab (built into the sandbox) and run:

UPDATE orders SET status = 'shipped' WHERE id = 118;

Switch to the **Change stream** tab. You should see:

UPDATE  orders.id=118
before: { "status": "processing", "updated_at": "2026-09-19T13:58:02Z" }
after:  { "status": "shipped",    "updated_at": "2026-09-19T14:01:47Z" }
lsn: 24/B3F1A208   committed_at: 14:01:47   synced_at: 14:01:52

And in the **Destination view**:

ID  | STATUS  | UPDATED_AT
118 | shipped | 2026-09-19 14:01:47

Notice that the event carries both the before and after value, and that `synced_at` minus `committed_at` is your real replication lag — not an estimate.

**Checkpoint: you've watched a single committed change flow through**

If the Change stream tab shows nothing after 30 seconds, see [Troubleshooting](#troubleshooting) below, or reset the sandbox from the pipeline menu.

## Step 3: Delete a row and see what survives

DELETE FROM orders WHERE id = 42;

In the default mode, row 42 disappears from the destination — it mirrors the source exactly. Now open **Pipeline settings → Keep deleted rows** and turn it on, then delete a second row. This time the row stays in the destination, flagged `_wolfsbane_op = 'DELETE'` with a `_wolfsbane_deleted_at` timestamp, instead of disappearing.

## Step 4: Change the schema and watch it propagate

ALTER TABLE orders ADD COLUMN gift_wrapped boolean DEFAULT false;

The destination view gains a nullable `GIFT_WRAPPED` column without the pipeline restarting. Wolfsbane never drops a column on the destination, even if you drop it at the source — a source-side mistake can't silently delete a warehouse column. Dropped-but-orphaned columns show up in the **Schema changes** log instead.

## Step 5: Disconnect and reconnect

Click **Pause** on the pipeline. With it paused, make two or three more changes in the SQL console. Then click **Resume**.

You should see every change made during the pause appear exactly once, in the order it committed — nothing missing, nothing duplicated. Wolfsbane resumes from the last position it acknowledged in the write-ahead log, not from "now."

## What you built

You started a real Wolfsbane pipeline and watched it snapshot, stream inserts and updates individually, handle a delete two different ways, propagate a schema change without a restart, and recover cleanly from a pause. You can now predict, for any change to a source table, what shows up on the warehouse side and roughly how fast.

## Troubleshooting

### No new events after 30 seconds

**Cause:** the sandbox SQL console session timed out.
**Fix:** reopen the console tab — the pipeline itself keeps running underneath it.

### Destination view shows the old value

**Cause:** the dashboard tab is showing a cached render.
**Fix:** refresh the page; the underlying table is already correct.

## Where to go next

- [Replicate one of your own tables in under 10 minutes](/docs/getting-started/quickstart)
- [Supported sources, destinations, and delete-handling modes](/docs/reference)
- [Why Wolfsbane reads the write-ahead log instead of polling](/docs/reference/replication-model)
```

---

## Before this ships (per each skill's own pass threshold — required, not optional)

**Quickstart — cold-run on a clean Postgres + Snowflake pair, fresh account, no cached creds, and confirm:**
1. Every `wolfsbane` CLI flag name above matches the real CLI (invented for this draft: `source add postgres`, `destination add snowflake`, `pipeline create`).
2. Real command output replaces every output block verbatim — none of it is real product output yet.
3. Elapsed time from `wolfsbane login` to the row appearing in Snowflake is actually ≤10 minutes; if not, cut scope rather than raise the stated budget.
4. `_wolfsbane_synced_at` is the real metadata column name Wolfsbane writes.

**Tutorial — run end-to-end as a learner who's never touched CDC, and confirm:**
1. The sandbox product surface described (sample `orders` table, Source SQL console, Change stream tab, Destination view, pause/resume) exists as named — if Wolfsbane has no such sandbox today, this tutorial can't ship until it does; that's a product gap this rewrite surfaces, not a docs one.
2. Real snapshot row count, real LSN format, and real lag numbers replace the placeholders.
3. Someone who's never seen the product can pass criterion 5 of the tutorial's pass bar: predict, unaided, what a change *not* walked through in the steps will do.

**Instrumentation to wire before publish:**
- Quickstart funnel: `source_connected` → `destination_connected` → `pipeline_started` → `first_row_verified` (the success event). Watch step-level drop-off first; it's the cheapest signal and names the exact step that's breaking the 10-minute promise.
- Tutorial funnel: one event per checkpoint (2 total) plus `tutorial_completed`. The metric that actually answers "did this build trust" is day-7 or day-30 conversion from `tutorial_completed` to a *real* (non-sandbox) pipeline started — track that once a baseline cohort exists.