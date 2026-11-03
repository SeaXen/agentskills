# Budget Config File Watcher (Hot-Reload)

## Problem
Dashboard budget editor writes to `budget.yaml` but plugin only loads config at startup or via `/budget set` slash command. Changes from dashboard didn't propagate to running plugin.

## Solution: watchdog File Watcher

### 1. Add Dependency
```toml
# pyproject.toml
dependencies = [
    "watchdog>=3.0",  # budget.yaml file watcher for hot-reload
]
```

### 2. Watcher Implementation (in `budget.py`)

```python
# Module-level state
_budget_observer = None
_budget_watcher_started = False

def start_budget_watcher() -> None:
    """Start background file watcher on budget.yaml → auto-reload config on changes."""
    global _budget_observer, _budget_watcher_started
    if _budget_watcher_started:
        return
    try:
        from watchdog.observers import Observer
        from watchdog.events import FileSystemEventHandler, FileModifiedEvent
    except Exception as exc:
        logger.debug("budget watcher unavailable (watchdog not installed): %s", exc)
        return

    class BudgetConfigHandler(FileSystemEventHandler):
        def on_modified(self, event: FileModifiedEvent) -> None:
            if not event.is_directory and event.src_path.endswith("budget.yaml"):
                logger.info("budget.yaml modified — hot-reloading budget config")
                reload_config()

    path = _budget_path()
    path.parent.mkdir(parents=True, exist_ok=True)
    _budget_observer = Observer()
    _budget_observer.schedule(BudgetConfigHandler(), str(path.parent), recursive=False)
    _budget_observer.daemon = True
    _budget_observer.start()
    _budget_watcher_started = True
    logger.info("Budget file watcher started on %s", path)

def stop_budget_watcher() -> None:
    """Stop budget file watcher (for cleanup/tests)."""
    global _budget_observer, _budget_watcher_started
    if _budget_observer:
        _budget_observer.stop()
        _budget_observer.join(timeout=2)
        _budget_observer = None
    _budget_watcher_started = False
```

### 3. Call on Plugin Load

In `__init__.py` `register(ctx)`:

```python
def register(ctx) -> None:
    # ... existing setup ...
    from . import budget
    budget.start_budget_watcher()  # NEW
    # ... rest of register ...
```

### 4. Reload Config Must Clear Caches

```python
def reload_config() -> None:
    """Drop cached config so next read re-parses."""
    global _config_cache
    with _config_lock:
        _config_cache = None
    with _verdict_lock:
        _verdict_cache.clear()  # Critical: clear verdict cache too
```

### 5. **Atomic YAML Write Required** (Critical for Watchdog Correctness)

Both dashboard API (`serve.py`) and slash command (`budget.py::_set_budget`) **must** write atomically. Standard `write_text()` / `open(path, "w")` truncates then writes — watchdog fires `IN_MODIFY` on first byte written to truncated file → `safe_load("")` returns `None` → config resets to "no limits" for milliseconds → budget gate misses enforcement.

```python
import os
import yaml

# In api_budget_update() AND _set_budget():
tmp = path.with_suffix(".yaml.tmp")
with open(tmp, "w") as f:
    yaml.safe_dump(cfg, f, default_flow_style=False, sort_keys=False)
os.replace(tmp, path)  # POSIX atomic — watchdog only ever sees complete file
```

**Why `os.replace` works:** On POSIX, `rename()`/`replace()` is atomic — the filesystem swaps inodes instantly. Watchdog sees either the old complete file or the new complete file, never a partial/truncated one.

### 6. Flow

```
Dashboard Edit → POST /api/budget → atomic write to budget.yaml
    → watchdog on_modified fires on COMPLETE file
    → reload_config() called
    → _config_cache = None + _verdict_cache cleared
    → Next budget.check() re-parses YAML
    → New limits enforced immediately
```

## Key Points
- **Daemon thread** → doesn't block shutdown
- **Non-recursive** → only watches telemetry directory
- **Graceful fallback** → logs debug if watchdog unavailable, continues without hot-reload
- **Clears verdict cache** → prevents stale 5s TTL verdicts from using old limits
- **Atomic write** → eliminates race where watchdog reads partial YAML (critical!)
- **Logs info** → visible in telemetry.log for debugging