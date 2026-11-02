# Migration guide: `transactions.amount_cents` → `amount_minor`, and `transactions.status` varchar → enum

**Audience:** the six service teams that read `transactions`, plus the DB owner who runs the DDL.
**Database:** Postgres 16, about 180M rows, rolling deploys, no downtime.

I wrote this without access to the real schema. Fill in or confirm the items in section 1 before publishing. Every SQL block is a reference implementation. Rehearse it on a production-sized copy first.

## 0. The plan in one table

| # | Phase | Owner | Gate to start the next phase |
|---|---|---|---|
| 1 | **Expand:** new columns, sync trigger, indexes, backfill | DB owner | Zero mismatches. Backfill finished. |
| 2 | **Release R1:** read `amount_minor`. Tolerate both status vocabularies. | Every service team | 100% of pods, workers, and cron jobs on R1. |
| 3 | **Flip:** rewrite the two renamed status values inside the varchar column | DB owner | Zero rows with old values. |
| 4 | **Release R2:** new vocabulary only. Enum-safe SQL. | Every service team | 100% of pods, workers, and cron jobs on R2. |
| 5 | **Swap:** the enum column becomes `status`, in one short transaction | DB owner | Error rates are flat after a rolling pool restart. |
| 6 | **Soak**, then **Contract:** drop the old columns, trigger, and indexes | DB owner | No reader of the old columns for one full release cycle (at least 7 days). |

Elapsed time is dominated by the slowest team's release cadence and the soak. Plan for roughly 5–6 weeks. The DB work itself is mostly the backfill, which runs for hours.

**Why this shape:**
- A direct `RENAME COLUMN` breaks every old pod the instant it commits.
- `ALTER COLUMN ... TYPE` to an enum rewrites 180M rows under an `ACCESS EXCLUSIVE` lock.
- Postgres also gives no way to make a renamed enum value readable by old code. So the vocabulary change gets its own phase, inside a column that holds either vocabulary, before the type changes.

## 1. Fill in before publishing

| Item | Value |
|---|---|
| Old → new status values (the two renamed ones) | `<old_1>` → `<new_1>`, `<old_2>` → `<new_2>` |
| Full enum value list, in the order you want it sorted | `<new_1>, <new_2>, …` |
| Primary key (the guide assumes `id bigint`) | |
| Type of `amount_cents` (the guide assumes `bigint`) | |
| `NOT NULL` and `DEFAULT` on `amount_cents` and `status` | |
| Does the value of `amount_cents` stay identical under the new name? | The guide assumes yes. This is a rename, not a change of unit. |
| Who writes the table? You said six services read it. | |
| Is `transactions` partitioned? | If so, `CREATE INDEX CONCURRENTLY` must be done per partition and then attached. |
| Are there CDC, logical replication, a warehouse feed, BI tools, or dbt on this table? | |

**Check before anything else. These queries are read-only.**

```sql
-- Dirty status values (trailing spaces, case variants, NULL, '') will make the enum cast fail.
SELECT status, count(*) FROM transactions GROUP BY 1 ORDER BY 2 DESC;

-- Dependencies on either column.
SELECT indexdef FROM pg_indexes WHERE tablename = 'transactions';
SELECT conname, pg_get_constraintdef(oid) FROM pg_constraint WHERE conrelid = 'transactions'::regclass;
SELECT * FROM information_schema.view_column_usage WHERE table_name = 'transactions';
SELECT proname FROM pg_proc WHERE prosrc ILIKE '%amount_cents%' OR prosrc ILIKE '%status%';
SELECT tgname FROM pg_trigger WHERE tgrelid = 'transactions'::regclass AND NOT tgisinternal;
```

If the distinct-values query shows anything outside the known set, clean it up first.

## 2. Rules for everyone

1. Only the DB owner runs DDL on this table. Turn off ORM auto-migration and schema diffing for it.
2. Every service sets `application_name` to `<service>@<release>`. The gates are checked against it.
3. Never `SELECT *` from `transactions`. Name the columns.
4. Every DDL statement runs with `SET lock_timeout = '3s'` and is retried on timeout. A queued `ACCESS EXCLUSIVE` lock blocks all traffic behind it. Check for long-running and idle-in-transaction sessions first.
5. Do not merge a release that mixes this migration's changes with unrelated schema changes.

## 3. Phase 1: Expand (DB owner)

**1.1 Type, mapping function, columns.** These are all metadata-only changes.

```sql
SET lock_timeout = '3s';

CREATE TYPE transaction_status AS ENUM ('<new_1>', '<new_2>', '<unchanged_1>' /* … */);

-- Accepts both vocabularies. An unknown value raises an error on purpose.
CREATE FUNCTION txn_status_to_enum(s text) RETURNS transaction_status
LANGUAGE sql IMMUTABLE AS $$
  SELECT (CASE s WHEN '<old_1>' THEN '<new_1>'
                 WHEN '<old_2>' THEN '<new_2>'
                 ELSE s END)::transaction_status
$$;

ALTER TABLE transactions
  ADD COLUMN amount_minor bigint,
  ADD COLUMN status_new   transaction_status;
```

Do **not** set a `DEFAULT` or `NOT NULL` on the new columns yet. A default on `status_new` would be applied before the trigger runs and would conflict with the value the trigger derives.

**1.2 Sync trigger.** Any pod, old or new, can write either amount column. The trigger propagates whichever side changed. Nobody writes `status_new`. The trigger derives it from `status`.

```sql
CREATE FUNCTION transactions_expand_sync() RETURNS trigger LANGUAGE plpgsql AS $$
BEGIN
  IF TG_OP = 'INSERT' THEN
    IF NEW.amount_minor IS NULL THEN NEW.amount_minor := NEW.amount_cents;
    ELSIF NEW.amount_cents IS NULL THEN NEW.amount_cents := NEW.amount_minor;
    ELSIF NEW.amount_minor <> NEW.amount_cents THEN
      RAISE EXCEPTION 'amount_minor (%) and amount_cents (%) disagree', NEW.amount_minor, NEW.amount_cents;
    END IF;
  ELSE
    IF NEW.amount_minor IS DISTINCT FROM OLD.amount_minor
       AND NEW.amount_cents IS DISTINCT FROM OLD.amount_cents THEN
      IF NEW.amount_minor IS DISTINCT FROM NEW.amount_cents THEN
        RAISE EXCEPTION 'amount_minor (%) and amount_cents (%) disagree', NEW.amount_minor, NEW.amount_cents;
      END IF;
    ELSIF NEW.amount_minor IS DISTINCT FROM OLD.amount_minor THEN
      NEW.amount_cents := NEW.amount_minor;
    ELSIF NEW.amount_cents IS DISTINCT FROM OLD.amount_cents THEN
      NEW.amount_minor := NEW.amount_cents;
    END IF;
  END IF;

  IF TG_OP = 'INSERT' OR NEW.status IS DISTINCT FROM OLD.status OR NEW.status_new IS NULL THEN
    NEW.status_new := txn_status_to_enum(NEW.status);
  END IF;
  RETURN NEW;
END $$;

CREATE TRIGGER transactions_expand_sync
  BEFORE INSERT OR UPDATE ON transactions
  FOR EACH ROW EXECUTE FUNCTION transactions_expand_sync();
```

⚠️ The trigger raises on an unknown status. The enum would reject that value after the swap anyway. Finding it now is cheaper, but expect the writer that sends it to start failing.

**1.3 Indexes.** Duplicate every index, unique constraint, and partial-index predicate that involves `amount_cents` or `status` onto the new columns. Write predicates in the new vocabulary.

```sql
CREATE INDEX CONCURRENTLY transactions_status_new_idx ON transactions (status_new);
-- repeat per existing index
SELECT indexrelid::regclass FROM pg_index WHERE NOT indisvalid;  -- must return no rows
```

A failed concurrent build leaves an invalid index. Drop it and retry.

**1.4 Backfill, one pass for both columns.** The trigger fills `status_new`.

```sql
DO $$
DECLARE lo bigint := (SELECT min(id) FROM transactions);
        mx bigint := (SELECT max(id) FROM transactions);
        step constant bigint := 10000;  -- small enough to keep row locks and WAL bursts short
BEGIN
  WHILE lo <= mx LOOP
    WHILE (SELECT coalesce(max(extract(epoch FROM replay_lag)), 0) FROM pg_stat_replication) > 5 LOOP
      PERFORM pg_sleep(5);              -- pause while any replica is more than 5 s behind
    END LOOP;
    UPDATE transactions SET amount_minor = amount_cents
     WHERE id >= lo AND id < lo + step
       AND (amount_minor IS NULL OR status_new IS NULL);
    COMMIT;
    IF (lo / step) % 100 = 0 THEN RAISE NOTICE 'backfill at id %, of %', lo, mx; END IF;
    lo := lo + step;
    PERFORM pg_sleep(0.05);
  END LOOP;
END $$;
```

The loop is resumable and idempotent. If ids are not bigint-sequential, switch to keyset pagination.

**Expect these costs:**
- **Time.** Unthrottled, 180M rows takes a few hours. Throttled, assume most of a day. Use your rehearsal number.
- **Disk.** Most updates will not be HOT, so every index gets new entries. Budget at least one extra copy of the heap, plus index bloat and WAL retention, until vacuum catches up. Check headroom before starting.
- **Autovacuum.** Lower `autovacuum_vacuum_scale_factor` on this table for the duration.
- **CDC.** The backfill emits about 180M update events to any CDC or logical-replication consumer. Warn those owners, or throttle harder.
- **Replica lag.** The loop above pauses on lag. Also watch your own alerts.

**1.5 Verify.** Run these in id slices, or against a replica. Don't run them as a single 180M-row scan on the primary.

```sql
SELECT count(*) FROM transactions
 WHERE id >= :lo AND id < :hi
   AND (amount_minor IS DISTINCT FROM amount_cents
        OR status_new IS DISTINCT FROM txn_status_to_enum(status));   -- must be 0
```

If the original columns are `NOT NULL`, prepare the constraints without a long lock:

```sql
ALTER TABLE transactions ADD CONSTRAINT amount_minor_nn CHECK (amount_minor IS NOT NULL) NOT VALID;
ALTER TABLE transactions VALIDATE CONSTRAINT amount_minor_nn;
ALTER TABLE transactions ADD CONSTRAINT status_new_nn CHECK (status_new IS NOT NULL) NOT VALID;
ALTER TABLE transactions VALIDATE CONSTRAINT status_new_nn;
```

## 4. Phase 2: Release R1 (every service team)

R1 must be backward-compatible with the current schema. Rolling it out must not require anything from the DB.

- [ ] Read `amount_minor`. Write `amount_minor`. The trigger keeps `amount_cents` correct for pods still on the old release.
- [ ] Read `status` and accept **both** vocabularies. Any filter on a renamed value lists both, for example `status IN ('<old_1>','<new_1>')`.
- [ ] Keep **writing the old vocabulary**. Old pods are still running and cannot read the new one.
- [ ] No `SELECT *`. `application_name` carries the release.
- [ ] Cover workers, cron jobs, consumers, admin scripts, and reporting queries, not only the web pods.

**Gate A:** every team confirms R1 is at 100% for every deployable. Cross-check against live sessions. The inventory is the gate, and the query is only a sanity check, because intermittent jobs won't show up:

```sql
SELECT application_name, count(*) FROM pg_stat_activity
 WHERE datname = current_database() GROUP BY 1 ORDER BY 1;
```

⚠️ **Point of no return for service code.** After Phase 3, rolling a service back below R1 breaks it.

## 5. Phase 3: Flip the vocabulary (DB owner)

**3.1 Replace the trigger function** so the varchar column is normalised to the new vocabulary on every write. Add this just before `RETURN NEW`; the rest of the function is unchanged:

```sql
  IF NEW.status_new IS NOT NULL THEN NEW.status := NEW.status_new::text; END IF;
```

**3.2 Rewrite the existing rows, in batches.** Use the same loop and throttle as the backfill, with this statement:

```sql
UPDATE transactions SET status = txn_status_to_enum(status)::text
 WHERE id >= lo AND id < lo + step AND status IN ('<old_1>', '<old_2>');
```

If `status` has a `CHECK` constraint listing the old values, widen it first. Add a new `NOT VALID` check that allows both vocabularies, and drop the old one after the flip.

**Verify:** `SELECT count(*) FROM transactions WHERE status IN ('<old_1>','<old_2>');` must return 0.

## 6. Phase 4: Release R2 (every service team)

R2 must work against the varchar column **and** the enum column. The swap lands under live traffic, so each team's CI must run the service's test suite against both schema states.

- [ ] Use the **new vocabulary only**. Remove every old literal. After the swap, `WHERE status = '<old_1>'` is an error, not an empty result.
- [ ] Bind status parameters **untyped**, so the server infers the column's type. A parameter typed `varchar` or `text` fails against an enum with `operator does not exist`. Fix this at the driver level (for example, pgjdbc `stringtype=unspecified`). Do not add `::text` casts on the column.
- [ ] Remove SQL that treats `status` as text. These all break on an enum:
  - `LIKE` and `ILIKE`
  - `lower()`, `upper()`, `||`
  - `COALESCE(status, '')`, or any fallback literal that is not an enum label
  - `status::text` on indexed filters, which defeats the index
- [ ] Check ordering. `ORDER BY status`, `min()`, `max()`, `<` / `>`, and keyset pagination on `status` now sort by **enum declaration order**, not alphabetically.
- [ ] Confirm your driver decodes enum columns into your string or enum type. Some drivers need the type registered.
- [ ] Read the old amount column nowhere. Write nothing to `amount_cents`.

**Gate B:** R2 is at 100% for every deployable, confirmed the same way as Gate A.

## 7. Phase 5: Swap (DB owner, with every team on standby)

Pick a low-traffic window. Check for long transactions first. All six teams must be ready to do a rolling pool restart right after.

```sql
BEGIN;
SET LOCAL lock_timeout = '3s';
ALTER TABLE transactions RENAME COLUMN status     TO status_legacy;
ALTER TABLE transactions RENAME COLUMN status_new TO status;
ALTER TABLE transactions ALTER COLUMN status SET DEFAULT '<default_label>';  -- only if the old column had one
ALTER TABLE transactions ALTER COLUMN status_legacy DROP DEFAULT;
ALTER TABLE transactions ALTER COLUMN status SET NOT NULL;        -- instant; uses status_new_nn
ALTER TABLE transactions ALTER COLUMN status_legacy DROP NOT NULL;
-- Replace the status block of the trigger function. The enum is now the source of truth,
-- and status_legacy is kept filled so the swap can be reversed:
--   NEW.status_legacy := NEW.status::text;
-- The amount block is unchanged.
CREATE OR REPLACE FUNCTION transactions_expand_sync() ... ;
COMMIT;
```

If it times out, nothing is applied. Retry later.

⚠️ **Expect `cached plan must not change result type` errors** from prepared statements after the swap. The column keeps its name but changes type. Every team does a rolling restart or pool recycle immediately, and watches error rates for 30 minutes.

## 8. Phase 6: Soak, then Contract

**Soak for at least one full release cycle** (7 days minimum, longer if month-end jobs matter).

1. At swap time, run `SELECT pg_stat_statements_reset();`. Pre-swap history would otherwise pollute the check.
2. At the end of the soak, search the statement texts for the old names:

```sql
SELECT query, calls FROM pg_stat_statements
 WHERE query ILIKE '%amount_cents%' OR query ILIKE '%status_legacy%';   -- must return no rows
```

3. `pg_stat_statements` does not see everything. Also confirm with the owners of:
   - BI tools
   - dbt models and warehouse ETL
   - CDC consumers
   - ad hoc analyst queries
   - views and materialized views
   - replicas used for reporting

**Contract.** This is **irreversible**; recovery means restoring from backup. Each statement needs the same `lock_timeout` and retry discipline:

```sql
DROP TRIGGER transactions_expand_sync ON transactions;
DROP FUNCTION transactions_expand_sync();
DROP FUNCTION txn_status_to_enum(text);
ALTER TABLE transactions DROP COLUMN amount_cents, DROP COLUMN status_legacy;  -- metadata-only, but needs a brief ACCESS EXCLUSIVE lock
ALTER TABLE transactions ALTER COLUMN amount_minor SET NOT NULL;               -- instant with the validated check
ALTER TABLE transactions DROP CONSTRAINT amount_minor_nn, DROP CONSTRAINT status_new_nn;
-- Add amount_minor's DEFAULT here if amount_cents had one.
DROP INDEX CONCURRENTLY <each index on the old columns>;
ALTER INDEX <new_index> RENAME TO <canonical_name>;
```

`DROP COLUMN` does not reclaim space. Autovacuum reclaims the backfill bloat for reuse, but not for the filesystem. If `pgstattuple` shows heavy bloat, plan a `pg_repack` in a maintenance window. It needs roughly 2× the table's disk.

Going forward, enum values can be added with `ALTER TYPE ... ADD VALUE`. They cannot be removed, and reordering is painful.

## 9. Rollback by phase

| Phase | Rollback |
|---|---|
| 1 | Drop the trigger, then the columns, function, and type. Nothing reads them yet. |
| 2 | Redeploy the previous release. This is safe because the trigger keeps `amount_cents` and `status` correct. |
| 3 | Reverse the `UPDATE` back to the old vocabulary, and restore the previous function. Only possible while no R1-or-later code is needed. After this phase, the floor for services is R1. |
| 4 | Roll R2 back to R1 only **before** the swap. After the swap, R1's old literals error, so the floor is R2. |
| 5 | Run the reverse swap in one transaction, in the same shape as the forward swap. It works because `status_legacy` was kept in sync. |
| Contract | Irreversible. This is why the soak exists. |

## 10. Stop conditions during DB phases

Pause the backfill or flip and tell the DB owner if any of these happens:
- replica replay lag stays above 5 s
- free disk drops below the headroom agreed in rehearsal
- p99 latency or lock waits rise on `transactions`
- the trigger raises an error in any service's logs
- CDC consumer lag grows without recovering

## 11. Who does what

**DB owner:**
- run Phases 1, 3, 5, and Contract
- publish the Gate A and Gate B status
- own the rehearsal and its timings

**Each service team:**
- ship R1 and R2 for **every** deployable (web, workers, cron, consumers)
- run CI against both schema states
- report to the DB owner when each release is at 100%
- be on call for the swap and the pool restart