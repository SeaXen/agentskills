# YantrikDB Hermes smoke test

## Scope
Throwaway-profile smoke test of `yantrikos/yantrikdb-hermes-plugin` on Hermes Agent v0.14.0 using the real Hermes runtime venv.

## What worked
- Installed cleanly into Hermes runtime venv with:
  - `yantrikdb-hermes-plugin 0.4.15`
  - `yantrikdb 0.7.19`
- Registered into throwaway profile with:
  - `HERMES_HOME=/root/.hermes/profiles/yantrikdb-smoke yantrikdb-hermes install --force`
- Activated with:
  - `hermes --profile yantrikdb-smoke config set memory.provider yantrikdb`
- `hermes --profile yantrikdb-smoke memory status` showed provider active and available.
- Real `yantrikdb_remember` write succeeded.
- Recall succeeded both:
  - in resumed session
  - in a fresh new session
- `yantrikdb_stats` and `yantrikdb_conflicts` tool calls both succeeded in-chat.
- On-disk SQLite DB matched observed behavior.

## Isolation/config pattern that mattered
Set explicit profile-local settings after install:

```bash
hermes --profile yantrikdb-smoke config set YANTRIKDB_MODE embedded
hermes --profile yantrikdb-smoke config set YANTRIKDB_DB_PATH /root/.hermes/profiles/yantrikdb-smoke/yantrikdb-memory.db
hermes --profile yantrikdb-smoke config set YANTRIKDB_NAMESPACE yantrikdb-smoke
```

Reason: avoid ambiguity about whether the plugin is using a shared default DB or the throwaway profile.

## Concrete smoke token used
Stored exact fact:
- `yantrikdb smoke token: YDB-SMOKE-20260526-ALPHA`

Observed chat results:
- write session: `20260526_001325_9b761c` → `STORED`
- resumed-session recall: returned exact token
- fresh-session recall: session `20260526_001421_588e0d` → returned exact token

## Storage verification
DB file:
- `/root/.hermes/profiles/yantrikdb-smoke/yantrikdb-memory.db`

Direct SQLite inspection showed:
- `memories = 5`
- exact token row present in `memories.text`
- related prompt rows also present

Example query pattern:

```sql
SELECT rid, text FROM memories WHERE text LIKE '%YDB-SMOKE-20260526-ALPHA%';
```

## CLI observability note
`yantrikdb stats` did not accept `--data-dir` in this install. The reliable way to inspect the profile-local DB from the CLI was to set `YANTRIKDB_DB_PATH` in the command environment:

```bash
YANTRIKDB_DB_PATH=/root/.hermes/profiles/yantrikdb-smoke/yantrikdb-memory.db yantrikdb stats
```

That returned sane counts:
- Active memories: 5
- Open conflicts: 0
- Pending triggers: 3

## Repo-quality caveats seen during audit
- Repo/docs version drift existed:
  - `pyproject.toml` at `0.4.15`
  - root `plugin.yaml` lagged at `0.4.12`
  - README current-version claims lagged further
- Open GitHub issue existed for: `YantrikDB is not active for this session.`
- That issue did **not** reproduce in this CLI smoke test.

## Practical verdict from this test
- Stronger practical result than Mnemosyne smoke test.
- Worked as a real Hermes memory provider in throwaway profile.
- Still treat as young software: keep main-profile adoption gated on whether gateway/platform path also behaves cleanly.