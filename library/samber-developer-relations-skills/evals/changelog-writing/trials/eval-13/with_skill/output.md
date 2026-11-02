Two things worth flagging before the deliverable, both straight from the skills' own scope checks:

- `changelog-writing`'s scope check explicitly routes "before/after code, a deprecation timeline, and codemods" to `version-migration-guide`, and routes "bump versions, cut tags" to release-automation tooling — "not this skill" in both cases. So below I ran the six breaking-change entries through `version-migration-guide`'s six-part anatomy (verb heading, affected-if, what/why, before/after, fix, escape hatch) and kept `changelog-writing` for the Added/Fixed/Changed body — that's exactly the split both SKILL.md files describe.
- I could not find a Ferrymill repository, commit history, or `pyproject.toml` anywhere in this workspace (`grep -r ferrymill` across the repo returns nothing). Per changelog-writing's rule "never stall because the repository is unreachable, state which mode is in use" — the mode here is **no source material**: everything below is a fully worked, self-consistent example built to spec, not sourced from a real diff. Swap in your real PR links, error text, and command output before publishing. I did not bump or tag anything real — there's no file to bump — but the exact diff and command are included at the end, ready to run once you point me at the actual repo.

---

# Ferrymill 4.0.0

**Tier:** 2 — requires user action for six of you. Earns changelog, release body, hosted page (per the tiering table; email/in-product note not built here since scope was notes + guide only).
**Path shape:** single hop, 3.8.0 → 4.0.0. All six changes already carried a deprecation runway inside the 3.x line (see timeline table below), so no additional interim warnings-only release is needed — the runway already shipped.
**Voice:** technical-writing school, imperative present, consistent throughout.

## CHANGELOG.md entry

```markdown
## [4.0.0] - 2026-09-18

### ⚠ Breaking Changes
Full detail, before/after code and codemods in the [Migration Guide](#migration-guide-38--40) below.

- **[Removed]** `Model.save()` no longer auto-commits — [#removed-model-save-autocommit](#removed-model-save-autocommit)
- **[Removed]** String-based `filter()` lookups — [#removed-string-filter](#removed-string-filter)
- **[Renamed]** `ferrymill.connect()` → `Engine.create()` — [#renamed-connect](#renamed-connect)
- **[Changed]** `ForeignKey` default `on_delete` is now `RESTRICT`, was `CASCADE` — [#changed-fk-default](#changed-fk-default)
- **[Removed]** Python 3.8 and 3.9 support; floor is now Python >= 3.10 — [#removed-py38-py39](#removed-py38-py39)
- **[Changed]** Migration files are YAML, not Python scripts — [#changed-migration-format](#changed-migration-format)

### Added
- Add `AsyncSession` for native `async`/`await` query execution alongside the existing sync `Session`.
- Add `Model.bulk_upsert()` for single-statement upsert of a batch of rows on PostgreSQL and SQLite.
- Add partial-index support for PostgreSQL `JSONB` columns via `Index(..., where=...)`.

### Fixed
- Fix a connection-pool leak when a transaction block raised before the first `commit()`, which left the connection checked out until pool exhaustion.
- Fix eager-loading (`joinedload`) issuing one query per polymorphic subclass instead of a single query with `UNION ALL`.
- Fix migration checksum mismatches on Windows caused by CRLF normalization of migration files before hashing.
```

## Migration Guide: 3.8 → 4.0

**Scope:** this single version pair only, no multi-hop jump supported — 3.7 and earlier must upgrade to 3.8 first to pick up the deprecation warnings, then to 4.0.
**Floors:** Python >= 3.10 (was >= 3.8). Check with `python -c "import sys; assert sys.version_info >= (3,10)"`.

---

<a id="removed-model-save-autocommit"></a>
### Removed: `Model.save()` no longer auto-commits

**Affected if:** grep for `\.save\(\)` with no `session.commit()` in the same request/handler. At runtime on 3.8 you'd have seen `DeprecationWarning: Model.save() will stop auto-committing in ferrymill 4.0; wrap calls in session.begin() or call session.commit() explicitly`. On 4.0 with no fix, rows are staged but never persisted — no error, just silent data loss on process exit.

**What changed and why:** `save()` used to open and commit its own transaction per call, which made multi-row writes N round-trips instead of one and made it impossible to roll back a partial write. It now only stages the object; the surrounding session owns the transaction boundary.

```python
# Before (3.x)
user = User(name="Ada")
user.save()  # committed immediately

# After (4.0)
user = User(name="Ada")
user.save()
session.commit()  # required — or wrap both lines in `with session.begin():`
```

**Fix:** no safe automated rewrite exists — inserting a blind `session.commit()` after every `.save()` would reintroduce the exact per-call-transaction cost this change removes. Ship the search pattern instead:

```bash
ferrymill-codemod scan --rule autocommit-audit ./src
# flags every .save() call not already inside a `with session.begin():`
# or followed by session.commit() in the same function, for manual review
```

**Escape hatch:** `Session(autocommit_compat=True)` restores per-call commits, emits a `RuntimeWarning` on each use, and is removed in 5.0.

---

<a id="removed-string-filter"></a>
### Removed: raw-string `filter()` lookups

**Affected if:** grep for `\.filter\(\s*["']` (a string literal as the first positional argument to `.filter`). On 3.8 this logged `DeprecationWarning: string filter expressions are removed in ferrymill 4.0, use Q() expressions`. On 4.0 it raises `TypeError: filter() takes no positional string arguments`.

**What changed and why:** raw-string filters were parsed into SQL fragments with light escaping, which was the source of two reported injection vectors when the string embedded unsanitized user input. `Q()` expressions build parameterized SQL from Python operators instead, closing that class of bug structurally rather than by convention.

```python
# Before (3.x)
User.query.filter("age > :age", age=18)

# After (4.0)
from ferrymill import Q
User.query.filter(Q.age > 18)
```

**Fix:** partial automation — simple single-comparison strings convert automatically, anything with `AND`/`OR`/subqueries is flagged, not rewritten:

```bash
ferrymill-codemod run --rule string-filter-to-q ./src
# Converts patterns matching `"<field> <op> :<param>"` → `Q.<field> <op> <param>`.
# Leaves a `# TODO(ferrymill-codemod): manual Q() rewrite needed` comment on
# any filter string containing AND/OR/LIKE/subselect — grep that marker for
# the residue list.
```

**Escape hatch:** none. String filters are a closed security hole, not a compatibility toggle.

---

<a id="renamed-connect"></a>
### Renamed: `ferrymill.connect()` → `Engine.create()`

**Affected if:** grep for `ferrymill\.connect\(`. On 3.8, `connect()` was a thin wrapper around `Engine.create()` emitting `DeprecationWarning: connect() is renamed to Engine.create(), same arguments`. On 4.0, `connect` is gone: `AttributeError: module 'ferrymill' has no attribute 'connect'`.

**What changed and why:** `connect()` returned a bare connection; the rename makes explicit that the return value is an `Engine` (a pool, not a single connection), which was a recurring source of confusion in support tickets about connections not being pooled.

```python
# Before (3.x)
engine = ferrymill.connect("postgresql://localhost/app")

# After (4.0)
engine = ferrymill.Engine.create("postgresql://localhost/app")
```

**Fix:** fully automated — pure rename, same argument order:

```bash
ferrymill-codemod run --rule rename-connect ./src
# equivalent to: grep -rl 'ferrymill\.connect(' src | xargs sed -i '' \
#   's/ferrymill\.connect(/ferrymill.Engine.create(/g'
```

**Escape hatch:** none needed — the codemod is exact and lossless.

---

<a id="changed-fk-default"></a>
### Changed: `ForeignKey` default `on_delete` is now `RESTRICT`

**Affected if:** grep for `ForeignKey(` calls with no `on_delete=` keyword. On 3.8+ these logged `DeprecationWarning: ForeignKey without on_delete will default to RESTRICT in 4.0, was CASCADE` at model-import time. On 4.0, deleting a referenced row now raises `IntegrityError: update or delete on table "..." violates foreign key constraint` wherever it previously cascaded silently.

**What changed and why:** implicit cascade deletes were the single most common cause of the "why did my child rows disappear" support ticket category — reported alongside three incidents of unintended bulk data loss in production. `RESTRICT` forces every deletion path to state its cascade intent explicitly.

```python
# Before (3.x) — implicit CASCADE
class Order(Model):
    customer = ForeignKey(Customer)

# After (4.0) — explicit, keeps old behavior verbatim
class Order(Model):
    customer = ForeignKey(Customer, on_delete=CASCADE)
```

**Fix:** fully automated — makes the previous implicit default explicit, so it is behavior-preserving by construction:

```bash
ferrymill-codemod run --rule explicit-fk-default ./src
# Inserts `on_delete=CASCADE` into every ForeignKey(...) call missing the kwarg.
# Review the diff before committing — this preserves old behavior, it does not
# pick RESTRICT for you; decide per-relationship whether CASCADE is still correct.
```

**Escape hatch:** `Model.Meta.legacy_fk_defaults = True` reverts an entire model's foreign keys to implicit CASCADE for a staged rollout. Emits a `DeprecationWarning`; removed in 4.2.

---

<a id="removed-py38-py39"></a>
### Removed: Python 3.8 and 3.9 support

**Affected if:** `pip install ferrymill==4.*` on Python < 3.10 fails at resolution with `ERROR: Package 'ferrymill' requires a different Python: 3.9.18 not in '>=3.10'`. On 3.8, running under 3.8/3.9 printed a `PendingDeprecationWarning` at interpreter startup starting in 3.6.0, escalated to `DeprecationWarning` in 3.8.0.

**What changed and why:** 4.0's connection-pool internals use PEP 604 (`X | Y`) union syntax and `TaskGroup` from `asyncio` for the new `AsyncSession`, both 3.10+ only. There is no runtime shim for a language-level floor.

```python
# Before: supported on 3.8, 3.9, 3.10, 3.11, 3.12
# After: supported on 3.10, 3.11, 3.12, 3.13 only
```

**Fix:** no codemod applies to an interpreter floor. Manual step: upgrade the running Python to >= 3.10 before installing 4.0.

**Escape hatch:** none. Pin to `ferrymill<4.0` if the interpreter cannot move yet — that branch keeps receiving security fixes only, until 2027-03-18 (18 months out, matching the project's stated old-major support window — confirm this date against your actual support policy before publishing).

---

<a id="changed-migration-format"></a>
### Changed: migration files are YAML, not Python scripts

**Affected if:** grep for `migrations/*.py` files containing `def upgrade(` / `def downgrade(`. On 3.8, the legacy `.py` loader still ran but logged `DeprecationWarning: python migration files are removed in ferrymill 4.0, run 'ferrymill migrate export-legacy'`. On 4.0, `.py` migration files are silently ignored by the migration runner — no error, migrations just don't apply, which makes this the entry most likely to bite someone quietly.

**What changed and why:** declarative YAML migrations can be diffed, linted and validated against a JSON schema before they ever run; arbitrary Python migration scripts could not be statically checked and were the source of two migration-runner sandbox-escape reports.

```yaml
# Before (3.x): migrations/0001_initial.py
# def upgrade(m): m.create_table("users", [m.Column("name", "text")])
# def downgrade(m): m.drop_table("users")

# After (4.0): migrations/0001_initial.yaml
operations:
  - create_table:
      name: users
      columns:
        - {name: name, type: text}
down:
  - drop_table: {name: users}
```

**Fix:** bounded automation — structural operations convert, custom data migrations do not:

```bash
ferrymill migrate export-legacy ./migrations
# Converts create_table/drop_table/add_column/drop_column/rename_column calls
# into the YAML operations list. Any migration containing a custom RunPython-
# style function block is NOT converted — it is written out as a stub with
# a `hooks:` section pointing back at the original .py file, which you must
# port into a registered hook function by hand. Run `ferrymill migrate verify`
# after conversion; it diffs the resulting schema against the pre-conversion
# schema and fails loudly on any mismatch.
```

**Escape hatch:** none — the `.py` loader is deleted, not deprecated-but-present, in 4.0.

---

### Deprecation timeline

| Change | First warned | Warning level | Escalated | Removed / took effect |
|---|---|---|---|---|
| `save()` auto-commit | 3.5.0 | `DeprecationWarning` | `RuntimeWarning` in 3.8.0 | 4.0.0 |
| String `filter()` | 3.6.0 | `DeprecationWarning` | — | 4.0.0 |
| `connect()` rename | 3.7.0 | `DeprecationWarning` | — | 4.0.0 |
| `ForeignKey` default | 3.7.0 | `PendingDeprecationWarning` | `DeprecationWarning` in 3.8.0 | 4.0.0 |
| Python 3.8/3.9 floor | 3.6.0 | `PendingDeprecationWarning` | `DeprecationWarning` in 3.8.0 | 4.0.0 |
| YAML migrations | 3.7.0 | `DeprecationWarning` | — | 4.0.0 |

## Traceability table

| Entry | Maps to |
|---|---|
| `save()` auto-commit | `<PR link — fill in>` |
| String `filter()` | `<PR link — fill in>` |
| `connect()` rename | `<PR link — fill in>` |
| `ForeignKey` default | `<PR link — fill in>` |
| Python 3.8/3.9 floor | `<PR link — fill in>` |
| YAML migrations | `<PR link — fill in>` |
| `AsyncSession` | `<PR link — fill in>` |
| `bulk_upsert()` | `<PR link — fill in>` |
| `JSONB` partial index | `<PR link — fill in>` |
| Pool-leak fix | `<PR link — fill in>` |
| Polymorphic eager-load fix | `<PR link — fill in>` |
| Windows checksum fix | `<PR link — fill in>` |

Left blank deliberately — no commit range was readable in this workspace. This table is not safe to publish until every row has a real link; that's the 100%-traceability gate this skill treats as non-negotiable.

## Exclusion list (illustrative)

- Dev-dependency version bumps (pytest, mypy) — no consumer surface.
- Internal rename of the query-planner module — no public symbol changed.
- CI workflow changes — not consumer-observable.

## Open items for a human

1. **Confirm the six changes above match your real diff.** They're a plausible, internally consistent worked example, not sourced from an actual commit range — verify each against the real 3.8→4.0 diff before publishing.
2. **Fill the traceability table** with real PR links.
3. **Confirm the security framing** on the string-`filter()` and YAML-migration entries (the "injection vectors" / "sandbox-escape" claims) against actual incident reports, or soften to "removed for defense-in-depth" if there were none.
4. **Confirm the 2027-03-18 old-major support end date** against your actual policy.
5. **Run the cold-upgrade verification** (skill's pass threshold): take a real project on 3.8, upgrade using only this guide, someone other than the author at the keyboard. Not done here — no real project was available.
6. **Version bump and tag** — see below, not executed.

## Version bump and tag (not executed — no `pyproject.toml` found)

Both are explicitly out of scope for `changelog-writing` and `version-migration-guide` ("release-automation tooling, not this skill"). No `pyproject.toml` exists anywhere in this workspace, so nothing was changed. Ready to run once pointed at the real repo:

```diff
 [project]
 name = "ferrymill"
-version = "3.8.0"
+version = "4.0.0"
```

```bash
git tag -a v4.0.0 -m "Ferrymill 4.0.0"
git push origin v4.0.0   # confirm before running — pushing a tag is shared, hard to unpublish cleanly
```