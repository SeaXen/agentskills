# Hermes telemetry dashboard 5-minute spike fix

**Plugin path:** `~/.hermes/plugins/hermes-telemetry/dashboard/serve.py`
**Service:** `hermes-telemetry-dashboard.service` (port **8009**)
**DB:** `~/.hermes/telemetry/telemetry.db` (`endpoint_payload_cache`, `tool_calls`)

## Symptom

CPU + temp spike every ~5 minutes while the host is otherwise idle.
Dynamic evidence (30-second samples over 6 minutes, single process):

```
t+30s   84.5%
t+180s  20.9%
t+360s  99.6%
```

`ps -o pcpu` shows the dashboard sitting at a high lifetime average
(e.g. 23% over a day) because these periodic bursts are concentrated
into one tick.

## Lesson: the FIRST fix is rarely complete

My initial fix (PR #82) bounded the SQL in **one** cache subclass
(`ModelEfficiencyCache`) and added a re-entrancy guard. That addressed
*that one cache's* runaway, but **four sibling caches still had the
same `DEFAULT_REFRESH_SECONDS=300` loop**:

- `ProvidersCache`
- `ProviderHealthCache`
- `DailyTokenChartCache`  ← includes `window_hours: 0` (10-year all-time)
- `DailyModelChartCache`  ← includes `window_hours: 0` (10-year all-time)

All five caches wake on the same wall-clock minute and hammer the
same `self._conn`. Worse, the daily-chart caches carry an all-time
key (`window_hours: 0` / `limit_days: 3650`) that **rescans the
entire `tool_calls` history** every tick. The user's continued
"5-min spike" complaint was the signal I had shipped an
incomplete fix the first time.

**Take-away:** when fixing a periodic CPU bug in a class hierarchy
with N subclasses, enumerate every subclass for the same loop
pattern. `rg -n "DEFAULT_REFRESH_SECONDS|CACHE_NAME|DEFAULT_KEYS" dashboard/serve.py`
will surface every cache quickly.

## Root causes

1. **All 5 `_BackgroundPayloadCache` subclasses share `DEFAULT_REFRESH_SECONDS = 300`.** Each runs its own background thread; all wake at the same wall-clock minute.
2. **All-time keys inside `DEFAULT_KEYS`** — `daily-token-chart` and `daily-model-chart` include `{"window_hours": 0, "limit_days": 3650}` which scans the full `tool_calls` table.
3. **No initial-stagger** — at startup all 5 caches warm simultaneously and again on every tick.
4. **Synchronized write to one `self._conn`** — each cache holds its own SQLite connection but they all hit the same DB file at the same instant, contending for WAL locks.

## Comprehensive fix (PR #91)

Two changes in `dashboard/serve.py`:

### 1. Skip all-time keys from background warm

```python
def _refresh_all(self):
    if self._refreshing:
        return {"skipped": "already refreshing"}
    self._refreshing = True
    started = time.monotonic()
    try:
        for kwargs in self.default_refresh_kwargs():
            # Skip all-time/zero-window keys from the background cadence —
            # those scan the entire history and dominate the 5-min spike.
            # On-demand refresh()/get_rows() still computes them when the
            # UI actually asks for the all-time window.
            if self._is_all_time_kwargs(kwargs):
                continue
            try:
                self.refresh(**kwargs)
            except Exception:
                logger.exception("%s refresh failed for %s", self.CACHE_NAME, kwargs)
        ...
```

```python
@staticmethod
def _is_all_time_kwargs(kwargs) -> bool:
    """Return True for kwargs that ask for the full history window."""
    if not kwargs:
        return False
    if "window_hours" in kwargs:
        try:
            if int(kwargs["window_hours"]) == 0:
                return True
        except (TypeError, ValueError):
            pass
    if "limit_days" in kwargs:
        try:
            if int(kwargs["limit_days"]) >= 3650:
                return True
        except (TypeError, ValueError):
            pass
    return False
```

### 2. Stagger initial refresh across caches

```python
def _run(self):
    # Stagger initial refresh across caches so the 5 cache loops (each
    # DEFAULT_REFRESH_SECONDS=300) don't pile onto the same SQLite
    # connection at startup and again on every tick. The offset is a
    # deterministic function of CACHE_NAME so it survives restarts.
    try:
        offset_seed = sum(ord(c) for c in self.CACHE_NAME)
        jitter = (offset_seed * 37) % 30
    except Exception:
        jitter = 0
    if jitter:
        with self._cond:
            if self._stop.wait(timeout=jitter):
                return
    ...
```

The offset is `0–29s` per cache and deterministic on `CACHE_NAME`, so
restarts don't reshuffle timing.

## Verification

### Dynamic (CPU watch)

```bash
# Watch the dashboard for 7 minutes, sampling every 30s
# Pre-fix: t+300s spikes to 80-100%
# Post-fix: t+300s stays at ~0-10%, then drops back to 0%

PID=$(systemctl show -p MainPID hermes-telemetry-dashboard.service | cut -d= -f2)
python3 - <<PY
import time, os
clk = os.sysconf("SC_CLK_TCK")
prev = None
for _ in range(14):                       # 14 * 30s = 420s = 7 min
    time.sleep(30)
    j = open(f"/proc/$PID/stat").read().split()[13:15]
    j = int(j[0]) + int(j[1])
    if prev is None: prev = j; continue
    pct = ((j - prev) / clk) / 30 * 100
    prev = j
    print(f"{pct:5.1f}%")
PY
```

### Static (DB-level, more reliable)

This is the **better** verification — it proves the fix at the source
without needing a full 5-min wait:

```bash
sqlite3 ~/.hermes/telemetry/telemetry.db "
SELECT cache_name,
       substr(cache_key, 1, 30) AS key,
       datetime(built_at)      AS built,
       rows_count
FROM endpoint_payload_cache
WHERE cache_name IN (
  'daily-token-chart','daily-model-chart',
  'providers','provider-health','model-efficiency'
)
ORDER BY cache_name, built_at DESC;
"
```

After restart, the **bounded** keys (24h / 168h / 720h) show fresh
`built_at` timestamps; the **all-time** keys (`window_hours: 0`,
`limit_days: 3650`) show old `built_at` timestamps from before the
restart and are NOT updated by the background loop. If they get
refreshed, the skip is not working.

### Unit tests

```python
def test_refresh_all_skips_all_time_kwargs(...):
    """Background warm must skip window_hours=0 and limit_days>=3650."""

def test_run_stagger_offset_is_deterministic_per_cache(...):
    """The per-cache stagger offset is stable across restarts."""
```

## Files / commits / PRs

- Initial partial fix: PR #82 (only bounded `ModelEfficiencyCache`)
- **Comprehensive fix: PR #91** (skip all-time keys + stagger)
- Tests added: `test_refresh_all_skips_all_time_kwargs`,
  `test_run_stagger_offset_is_deterministic_per_cache`

## Why this lesson matters elsewhere

The **synchronized-wake-up-on-same-interval** pattern is not unique
to hermes-telemetry. Watch for it anywhere you see:

- Multiple background threads sharing a `DEFAULT_REFRESH_SECONDS`
- A base class with subclasses that each define their own `DEFAULT_KEYS`
- Cache/database keys that include "all-time" or `0` / `>=3650` literals
- A polling loop that doesn't add initial jitter

When you find one, the fix is always the same shape:

1. **Skip the heavy/all-time keys from background warm** — on-demand paths still serve them
2. **Stagger initial start** — deterministic offset from class name is best
3. **Verify at the data layer** — DB timestamps beat CPU samples for this kind of fix
