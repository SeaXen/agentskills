# Migration guide: `transactions.amount_cents` → `amount_minor`, and `transactions.status` varchar → enum

I did not run anything for this. The SQL is untested, nothing here was checked against your schema, and no cold run was done, so no duration is claimed anywhere. The rehearsal in §5 is the acceptance test before this guide goes to the six teams.

## 1. Assumptions and open questions

Placeholders are in `<angle brackets>`. Fill them in or correct the assumptions before publishing.

**Assumptions**
- **Consumers.** The six consuming services are internal. Under the Churn Rule you control them, so the DB owner should open the service PRs from the patterns in §4. I wrote the guide because you asked for one.
- **Writers.** At least one service also writes to the table, and batch jobs, BI tools and CDC may read it.
- **Types.** `amount_cents` is `bigint`, and `amount_minor` keeps the same numeric value. If any currency is not 2-decimal, such as JPY or BHD, stop. The rename then needs a semantic review, not a column copy.
- **Primary key.** The table has a monotonic `bigint` primary key `id`.
- **Rolling deploys.** Old and new pods of the same service run side by side during every rollout.

**Open questions only you can answer**
1. What are the two renames (`<OLD_A>→<NEW_A>`, `<OLD_B>→<NEW_B>`)? Does any new label equal another existing old label? If so, the mapping is ambiguous and needs redesign.
2. Is `status` exposed outside the DB, in an API response, an event payload or a warehouse? If so, the label rename is a second breaking change for those consumers. It is out of scope here, so decide it before Release 2.
3. Is there CDC or logical replication on the table? The backfill emits one change event per row, about 180M of them.
4. Do you have telemetry on query shapes? I ranked by estimate, not measurement.
5. Who owns the migration tooling after cutover?

## 2. Inventory

| Change | Type | Blast radius | Evidence |
|---|---|---|---|
| `status` varchar → `transaction_status` enum | type change | All six services. Fails on typed params, `varchar = enum` comparisons and cached prepared statements | Estimate; verify with `pg_stat_statements` |
| Two `status` labels renamed | behavior change | Every `WHERE status = '<label>'`, every switch on the label, every exported payload | Estimate |
| `amount_cents` → `amount_minor` | rename | All readers and writers of the column | Estimate |
| Partial indexes, CHECKs and views that name old labels or columns | hidden dependents (Hyrum) | Unknown until the §3 preflight | Preflight queries |

The guide orders `status` first because it fails in more ways, and some of them are silent, such as a filter that quietly matches nothing.

## 3. Path shape

**Path shape: staged expand/contract, as a runbook.** An in-place rename or `ALTER COLUMN … TYPE` cannot work, for two reasons:
- During a rolling deploy, old and new code run together, so the old code would query a column that no longer exists.
- `varchar → enum` rewrites all 180M rows under an `ACCESS EXCLUSIVE` lock.

Two properties of Postgres shape the design:
- **Enum labels cannot be dropped.** The final enum must be created with only the new labels, so a temporary "union" enum is not an option.
- **The name `status` is taken.** The new column has to be swapped into that name, and the services must survive the swap.

## 4. The guide

> **Scope.** Postgres 16, `transactions` (~180M rows), six reading services, rolling deploys.
> **Floors:** PostgreSQL >= 16; every service sets `application_name` to its own name; you have `CREATE` on the `transaction_status` type, which the implicit-cast shim needs.
> **Release gates, not dates.** Each step starts when the previous gate is green. The owner sets dates in the §4.8 table.

### 4.0 Plan at a glance

| # | Step | Owner | Type | Rollback |
|---|---|---|---|---|
| 0 | Preflight | DB owner | read-only | n/a |
| 1 | Expand | DB owner | additive | drop the new objects |
| 2 | Backfill pass 1 | DB owner | **writes 180M rows** | re-runnable, nothing to undo |
| 3 | **Release 1** (all six) | service teams | deploy | redeploy previous release |
| 4 | Relabel (trigger v2, backfill pass 2) | DB owner | **writes rows** | `CREATE OR REPLACE` back to v1; stored labels may stay new |
| 5 | **Release 2** (all six) | service teams | deploy | redeploy Release 1 |
| 6 | **Swap** `status` | DB owner | metadata, seconds | reverse swap (§4.6) |
| 7 | Soak | everyone | wait | n/a |
| 8 | Contract | DB owner | **irreversible** | restore from backup only |

Steps 1–2, 4 and 6 are DB-owner actions. Releases 1 and 2 are the only service work.

### 4.1 Preflight (read-only, run on a replica)

```sql
-- Every distinct label. Anything not in the mapping aborts the plan.
SELECT status, count(*) FROM transactions GROUP BY 1 ORDER BY 2 DESC;

-- Things that name the old shape and must be mirrored or rewritten.
SELECT indexname, indexdef FROM pg_indexes
 WHERE tablename = 'transactions' AND indexdef ~ '(status|amount_cents)';
SELECT conname, pg_get_constraintdef(oid) FROM pg_constraint
 WHERE conrelid = 'transactions'::regclass;
SELECT schemaname, viewname FROM pg_views
 WHERE definition ~ '\m(status|amount_cents)\M' AND definition ~ 'transactions';
SELECT schemaname, matviewname FROM pg_matviews
 WHERE definition ~ 'transactions';
SELECT * FROM pg_publication_tables WHERE tablename = 'transactions';
```

Also check:
- Disk headroom of roughly one extra table copy until autovacuum reclaims the bloat.
- Replica lag budget.
- Every non-service reader: BI, dbt, ETL, cron jobs, one-off scripts. They count as readers.

### 4.2 Expand (additive, safe in any deploy)

Run with `SET lock_timeout = '3s';` and retry on failure. A blocked `ALTER` queues all traffic behind it.

```sql
CREATE TYPE transaction_status AS ENUM ('<NEW_A>', '<NEW_B>', '<UNCHANGED_LABELS>');

-- Shim: lets old-style varchar/text parameters hit the enum column after the swap.
-- Verify on staging (§5) before relying on it.
CREATE CAST (varchar AS transaction_status) WITH INOUT AS IMPLICIT;
CREATE CAST (text    AS transaction_status) WITH INOUT AS IMPLICIT;

ALTER TABLE transactions
  ADD COLUMN amount_minor bigint,
  ADD COLUMN status_new   transaction_status;

CREATE FUNCTION txn_status_to_new(s text) RETURNS transaction_status
LANGUAGE sql IMMUTABLE STRICT AS $$
  SELECT (CASE s WHEN '<OLD_A>' THEN '<NEW_A>'
                 WHEN '<OLD_B>' THEN '<NEW_B>'
                 ELSE s END)::transaction_status   -- unknown label => loud error
$$;

CREATE TABLE migration_legacy_writes (
  at   timestamptz NOT NULL DEFAULT now(),
  kind text NOT NULL,
  app  text NOT NULL DEFAULT current_setting('application_name')
);

-- v1: bidirectional amount sync, status_new derived from status (either spelling).
CREATE FUNCTION transactions_dual_write() RETURNS trigger LANGUAGE plpgsql AS $$
BEGIN
  IF TG_OP = 'INSERT' THEN
    IF NEW.amount_minor IS NULL THEN
      NEW.amount_minor := NEW.amount_cents;
      INSERT INTO migration_legacy_writes(kind) VALUES ('amount_cents');
    ELSE
      NEW.amount_cents := NEW.amount_minor;
    END IF;
  ELSIF NEW.amount_minor IS DISTINCT FROM OLD.amount_minor THEN
    NEW.amount_cents := NEW.amount_minor;
  ELSIF NEW.amount_cents IS DISTINCT FROM OLD.amount_cents THEN
    NEW.amount_minor := NEW.amount_cents;
    INSERT INTO migration_legacy_writes(kind) VALUES ('amount_cents');
  END IF;
  NEW.status_new := txn_status_to_new(NEW.status);
  RETURN NEW;
END $$;

CREATE TRIGGER transactions_dual_write BEFORE INSERT OR UPDATE ON transactions
  FOR EACH ROW EXECUTE FUNCTION transactions_dual_write();
```

Then build, outside any transaction:
- For every existing index or partial index that mentions `status` or `amount_cents`, run `CREATE INDEX CONCURRENTLY` on the new column. Use new labels in partial predicates.
- Confirm `indisvalid` in `pg_index`. A failed concurrent build leaves an `INVALID` index, which you must drop and rebuild.

**Rollback:** `DROP TRIGGER`, `DROP FUNCTION`, `ALTER TABLE … DROP COLUMN` for both columns, `DROP TYPE`, `DROP CAST`.

### 4.3 Backfill pass 1 (**writes every row**)

Run in throttled batches off the hot path.

```sql
CREATE PROCEDURE backfill_transactions(batch bigint, pause_s float8)
LANGUAGE plpgsql AS $$
DECLARE lo bigint; max_id bigint;
BEGIN
  SELECT min(id), max(id) INTO lo, max_id FROM transactions;
  WHILE lo <= max_id LOOP
    UPDATE transactions
       SET amount_minor = amount_cents, status_new = txn_status_to_new(status)
     WHERE id >= lo AND id < lo + batch
       AND (amount_minor IS NULL OR status_new IS NULL);
    COMMIT;
    PERFORM pg_sleep(pause_s);
    lo := lo + batch;
  END LOOP;
END $$;

CALL backfill_transactions(10000, 0.1);   -- starting values; tune against replica lag
```

Watch while it runs:
- Replica lag.
- WAL rate.
- Autovacuum and bloat.
- p99 write latency on `transactions`.
- CDC backlog.

Pause the loop when lag exceeds your budget. The procedure is restart-safe because it skips rows that are already filled.

**Gate G1.** All of these must hold before Release 1:

```sql
-- On a replica; expect 0 and 0.
SELECT count(*) FROM transactions WHERE amount_minor IS NULL AND amount_cents IS NOT NULL;
SELECT count(*) FROM transactions WHERE status_new IS DISTINCT FROM txn_status_to_new(status);
```

If the old columns are `NOT NULL`, add the same constraint without a full-table lock:
```sql
ALTER TABLE transactions ADD CONSTRAINT amount_minor_nn CHECK (amount_minor IS NOT NULL) NOT VALID;
ALTER TABLE transactions VALIDATE CONSTRAINT amount_minor_nn;
ALTER TABLE transactions ALTER COLUMN amount_minor SET NOT NULL;   -- skips the scan on PG 12+
ALTER TABLE transactions DROP CONSTRAINT amount_minor_nn;
```
Do the same for `status_new` with `status_nn`.

### 4.4 Service entries

#### Changed: `status` is an enum with two renamed labels {#changed-status-enum}

**Affects you if** your code reads, filters, writes or switches on `transactions.status`.
Search for: `status`, `'<OLD_A>'`, `'<OLD_B>'`, `SELECT \*`, and ORM models mapped to `transactions`.
During the migration you will see one of these errors if a step is skipped:

    ERROR:  operator does not exist: character varying = transaction_status
    ERROR:  column "status" is of type transaction_status but expression is of type character varying
    ERROR:  invalid input value for enum transaction_status: "<OLD_A>"
    ERROR:  cached plan must not change result type

`status` becomes a native enum, and `<OLD_A>`/`<OLD_B>` become `<NEW_A>`/`<NEW_B>`. Labels cannot be dropped from a Postgres enum, so the column is swapped in rather than altered. The new code must work with either type and either spelling, because the swap happens under live traffic.

**Release 1 (tolerate both spellings, write the old one):**
```sql
-- Before
SELECT id, status FROM transactions WHERE status = $1;
INSERT INTO transactions (id, amount_cents, status) VALUES ($1, $2, $3);

-- After (Release 1)
SELECT id, status::text AS status FROM transactions;          -- stable result type across the swap
-- filter on a renamed value: pass both spellings
SELECT id FROM transactions WHERE status = ANY($1);           -- $1 = ['<OLD_A>', '<NEW_A>']
-- writes: still the OLD spelling
```
In application code, map either spelling of `<OLD_A>`/`<NEW_A>` and of `<OLD_B>`/`<NEW_B>` to one internal value.

**Release 2 (new spelling only, shipped after step 4 relabels the stored data):**
```sql
-- After (Release 2)
SELECT id, status::text AS status FROM transactions WHERE status = ANY($1);   -- $1 = ['<NEW_A>']
-- writes: NEW spelling only
```
Drop the old spelling from filters and writes. Keep `status::text` on every `SELECT`, and never use `SELECT *`.

**Fix:** manual, 5 steps.
1. Find every query and ORM mapping that touches `status`.
2. Apply the Release 1 pattern.
3. Ship, and wait for G2.
4. Apply the Release 2 pattern.
5. Ship, and wait for G3.

**Escape hatch:** none after the contract step. Until then, redeploy the previous release.

#### Renamed: `amount_cents` → `amount_minor` {#renamed-amount-minor}

**Affects you if** you read or write `transactions.amount_cents`.
Search for `amount_cents`. After contract you will see:

    ERROR:  column "amount_cents" does not exist

The column is renamed to match the minor-unit meaning. A trigger keeps both columns in sync until contract, so old and new pods can mix.

```sql
-- Before
SELECT id, amount_cents FROM transactions;
INSERT INTO transactions (id, amount_cents, status) VALUES ($1, $2, $3);

-- After (Release 1)
SELECT id, amount_minor FROM transactions;
INSERT INTO transactions (id, amount_minor, status) VALUES ($1, $2, $3);
```

**Fix:** search and replace `amount_cents` with `amount_minor` in SQL and ORM mappings, then ship in Release 1.
**Escape hatch:** none after contract.

### 4.5 Gates and the relabel step

**Gate G2 (before step 4).**
- Release 1 is at 100% in all six services.
- Every non-service reader has been moved or confirmed tolerant.
- `SELECT max(at) FROM migration_legacy_writes WHERE kind = 'amount_cents'` is older than one full deploy cycle of every service.

**Step 4: relabel (trigger v2, then backfill pass 2).** This **rewrites stored labels**.

```sql
CREATE OR REPLACE FUNCTION transactions_dual_write() RETURNS trigger LANGUAGE plpgsql AS $$
BEGIN
  IF TG_OP = 'INSERT' THEN
    IF NEW.amount_minor IS NULL THEN
      NEW.amount_minor := NEW.amount_cents;
      INSERT INTO migration_legacy_writes(kind) VALUES ('amount_cents');
    ELSE NEW.amount_cents := NEW.amount_minor; END IF;
  ELSIF NEW.amount_minor IS DISTINCT FROM OLD.amount_minor THEN
    NEW.amount_cents := NEW.amount_minor;
  ELSIF NEW.amount_cents IS DISTINCT FROM OLD.amount_cents THEN
    NEW.amount_minor := NEW.amount_cents;
    INSERT INTO migration_legacy_writes(kind) VALUES ('amount_cents');
  END IF;
  IF NEW.status IN ('<OLD_A>', '<OLD_B>')
     AND (TG_OP = 'INSERT' OR NEW.status IS DISTINCT FROM OLD.status) THEN
    INSERT INTO migration_legacy_writes(kind) VALUES ('status_old_spelling');
  END IF;
  NEW.status_new := txn_status_to_new(NEW.status);
  NEW.status     := NEW.status_new::text;        -- stored spelling is now always new
  RETURN NEW;
END $$;
```

Then relabel the existing rows in batches, with the same loop shape as pass 1:
```sql
UPDATE transactions SET status = txn_status_to_new(status)::text
 WHERE id >= lo AND id < lo + batch AND status IN ('<OLD_A>', '<OLD_B>');
```

Verify on a replica, expecting 0:
```sql
SELECT count(*) FROM transactions WHERE status IN ('<OLD_A>', '<OLD_B>');
```

**Rollback:** `CREATE OR REPLACE` the v1 body. Relabeled rows are harmless because Release 1 tolerates both spellings.

**Gate G3 (before the swap).** All of these must hold:
- Release 2 is at 100% in all six services.
- Every non-service reader is on the new spelling.
- The relabel count above is 0.
- `migration_legacy_writes` has had no new rows for one full deploy cycle.
- The `status_new` and `amount_minor` indexes are valid.
- `NOT NULL` is in place where the old columns had it.
- The §5 rehearsal passed.

### 4.6 Swap (seconds, DB owner)

```sql
BEGIN;
SET LOCAL lock_timeout = '2s';
DROP TRIGGER transactions_dual_write ON transactions;
ALTER TABLE transactions RENAME COLUMN status     TO status_legacy;
ALTER TABLE transactions RENAME COLUMN status_new TO status;

CREATE FUNCTION transactions_legacy_sync() RETURNS trigger LANGUAGE plpgsql AS $$
BEGIN
  NEW.status_legacy := NEW.status::text;     -- one-way, keeps rollback possible
  NEW.amount_cents  := NEW.amount_minor;
  RETURN NEW;
END $$;
CREATE TRIGGER transactions_legacy_sync BEFORE INSERT OR UPDATE ON transactions
  FOR EACH ROW EXECUTE FUNCTION transactions_legacy_sync();
COMMIT;
```

On `lock_timeout` failure, retry in a quiet window. Do not raise the timeout.

**Rollback (valid until contract):**
```sql
BEGIN;
SET LOCAL lock_timeout = '2s';
DROP TRIGGER transactions_legacy_sync ON transactions;
ALTER TABLE transactions RENAME COLUMN status        TO status_new;
ALTER TABLE transactions RENAME COLUMN status_legacy TO status;
-- re-create the v2 transactions_dual_write trigger from §4.5
COMMIT;
```
No service redeploy is needed, because Release 2 works against both shapes.

### 4.7 Housekeeping

**Contract (irreversible):**
- Run it only after the soak window (§4.8), with the owner's sign-off.
- Take a backup first. After contract, rolling back means restoring from backup.
- Drop `transactions_legacy_sync`, the `status_legacy` and `amount_cents` columns, their old indexes, `txn_status_to_new`, `migration_legacy_writes` and `backfill_transactions`.
- Rename the new indexes to their canonical names.

**Optional Release 3:**
- Drop `::text` on `SELECT status` and the old-spelling mapping code.
- Run `DROP CAST (varchar AS transaction_status)` and `DROP CAST (text AS transaction_status)` only once nobody sends untyped string parameters.

### 4.8 Timeline

Dates are owner decisions. Windows are measured in deploy cycles, not days.

| Item | Warning signal | Removed at |
|---|---|---|
| `amount_cents` | `migration_legacy_writes` rows | Contract |
| Old label spelling | `migration_legacy_writes` rows (`status_old_spelling`) | Contract |
| varchar/text → enum implicit cast | none | Optional Release 3 |
| Legacy columns | none | Contract, after soak of `<N>` deploy cycles |

**Ownership.** The DB owner is `<name>`, and the tracking issue is `<link>`. The six services are `<svc-1> … <svc-6>`, each with an owner, a Release 1 PR and a Release 2 PR. The freeze date after which the old release is not deployable is `<date>`.

### 4.9 Troubleshooting (keyed by error text)

| Error text | Cause and fix |
|---|---|
| `operator does not exist: character varying = transaction_status` | The cast shim is missing, or the filter predates the swap. Re-run the §4.2 cast statements, or add an explicit `::transaction_status`. |
| `column "status" is of type transaction_status but expression is of type character varying` | A write sent a typed varchar after the swap with no shim. Check the casts exist. |
| `invalid input value for enum transaction_status: "<OLD_A>"` | A writer still uses the old spelling. Find it via `migration_legacy_writes.app`. Do not swap until it is fixed. |
| `cached plan must not change result type` | A query selects `status` without `::text`, or `SELECT *`. Apply the Release 1 pattern. |
| `canceling statement due to lock timeout` | A long transaction blocks the DDL. Find it with `pg_stat_activity` and retry. Never raise `lock_timeout`. |
| `column "amount_cents" does not exist` | You are past contract. Move to `amount_minor`. |

## 5. Verification plan

I could not run the cold upgrade, so this is the plan. The guide is not shippable until it passes.

1. **Rehearsal environment.** Restore a production copy with the real row count, the real indexes and the six services on Release 0.
2. **Cold run.** Someone who did not write the guide executes steps 0–8 using only §4, on top of a synthetic load that mimics each service's query shapes. The load must include prepared statements, typed parameters and an ORM path.
3. **Mid-rollout overlap.** Release 1 and Release 2 must each be rolled out with old and new pods mixed.
4. **Rollbacks.** Execute the swap rollback (§4.6) and one Release 1 rollback against the copy.
5. **Shim check.** Confirm that `WHERE status = $1` and `INSERT … status = $3` work with varchar and text parameters on both sides of the swap.
6. **Measurements.** Record the backfill duration, replica lag, WAL volume and p99 latency. These become the published effort, and no number is published without them.
7. **Acceptance.** There is no edit the guide does not describe, and no error outside the §4.9 table. Every residual is named.

## 6. KPIs

Listed in order of cheapest to wire first.
1. **Legacy writers.** The `migration_legacy_writes` rate by `app`, trending to zero before the swap. Free, because the trigger already records it.
2. **Migration tickets.** Tickets per service that quote one of the §4.9 errors, and which entry generates the most.
3. **Release adoption.** The pod share on Release 1 and Release 2 per service, taken from the deploy system.
4. **Stragglers.** A named list of non-service readers (BI, ETL, cron jobs) still on the old shape at G3.
5. **Backfill health.** Replica lag and bloat during steps 2 and 4.