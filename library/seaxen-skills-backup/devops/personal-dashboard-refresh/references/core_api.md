# personal_dashboard_core API Reference

The Hermes Personal Dashboard plugin exposes its functionality via the `personal_dashboard_core` Python module, **not** via standalone CLI commands.

## Module Location
```
~/.hermes/plugins/hermes-personal-dashboard/personal_dashboard_core.py
```

## Usage Pattern
```python
import sys
sys.path.insert(0, "/root/.hermes/plugins/hermes-personal-dashboard")
import personal_dashboard_core as core

# All functions accept an optional `conn` parameter for transaction control
# (omit for auto-commit per call)
```

## Core Functions

### Context Scanning & Inference
```python
# Scan Hermes sources (memory, sessions, cron) and infer context signals
core.refresh_from_hermes_context(
    include_sessions: bool = True,
    include_cron: bool = True,
    create_cards: bool = False,
    conn: Optional[sqlite3.Connection] = None
) -> Dict[str, Any]

# List inferred context items
core.list_context_items(
    include_hidden: bool = False,
    limit: int = 100,
    conn: Optional[sqlite3.Connection] = None
) -> List[Dict[str, Any]]

# Manually upsert a durable context item
core.upsert_context_item(data: Dict[str, Any], conn) -> Dict[str, Any]

# Hide a context item (and dismiss auto-generated cards)
core.hide_context_item(context_id: str, conn) -> Dict[str, Any]
```

### Card Management
```python
# Create or update a card (full payload)
core.upsert_card(data: Dict[str, Any], conn) -> Dict[str, Any]

# Partial update of an existing card
core.patch_card(card_id: str, data: Dict[str, Any], conn) -> Dict[str, Any]

# Get a single card by ID
core.get_card(card_id: str, conn) -> Optional[Dict[str, Any]]

# List cards with filters
core.list_cards(
    status: Optional[str] = None,
    domain: Optional[str] = None,
    include_hidden: bool = False,
    include_scanner: bool = False,
    limit: int = 200,
    conn: Optional[sqlite3.Connection] = None
) -> List[Dict[str, Any]]

# Dismiss (soft delete) a card
core.dismiss_card(card_id: str, conn) -> Dict[str, Any]

# Expire a card (hard delete with valid_until = now)
core.expire_card(card_id: str, conn) -> Dict[str, Any]
```

### Evidence & Provenance
```python
# Attach evidence to a card
core.add_evidence(data: Dict[str, Any], conn) -> Dict[str, Any]

# List evidence for a card
core.list_evidence(card_id: str, conn) -> List[Dict[str, Any]]
```

### Refresh Tracking
```python
# Record a refresh run
core.record_refresh(data: Dict[str, Any], conn) -> Dict[str, Any]

# List recent refresh runs
core.list_refresh_runs(limit: int = 50, conn) -> List[Dict[str, Any]]
```
### Utilities

```python
# Dashboard status summary
core.dashboard_status(conn) -> Dict[str, Any]

# Preferences (persistent key-value)
core.get_preferences(conn) -> Dict[str, Any]
core.put_preferences(values: Dict[str, Any], conn) -> Dict[str, Any]

# Time helpers
core.utc_now() -> str  # ISO-8601 UTC timestamp with Z suffix (e.g., "2026-06-11T07:00:00Z")
core.normalize_time(value: str) -> str  # Validate & normalize ISO-8601 (accepts Z or +00:00)
```

## Timestamp Format Requirement

**Critical**: `valid_until` and `updated_at` fields MUST use ISO-8601 UTC with `Z` suffix:
- ✅ `2026-06-11T07:00:00Z` (correct)
- ❌ `2026-06-11T07:00:00+00:00` (fails validation — `normalize_time` rejects this)

Use `datetime.strftime('%Y-%m-%dT%H:%M:%SZ')` to generate correctly formatted timestamps.
Raw `datetime.isoformat()` produces `+00:00` which will cause `DashboardError: timestamp must be ISO-8601`.

## Current Dashboard Cron Jobs (All No-Agent)

As of 2026-06-11, all three personal dashboard cron jobs run **without AI tokens**:

| Job ID | Schedule | Script | Mode |
|--------|----------|--------|------|
| `1226201b634c` | Hourly (min 0) | `hourly_dashboard_refresh.py` | Patches existing cards, extends `valid_until`/`updated_at` |
| `766c28ecadaf` | Daily 07:30 | `smart_refresh.py` | Full refresh from cron outputs (clears + recreates) |
| `e6294690fee6` | Weekly Fri 15:00 | `planning_refresh.py` | 3 stable planning cards (2-week validity) |

Zero OpenRouter quota consumed by dashboard maintenance.

## Required Card Fields
```python
{
    "id": "stable-card-id",           # Required, slugified
    "domain": "alerts|news|projects|weather|calendar|family|stocks|sports|planning",
    "title": "Concise title",
    "summary": "1-3 sentence summary",
    "priority": "low|medium|high|critical",  # default: medium
    "status": "active|stale|dismissed|expired|pinned",  # default: active
    "valid_until": "2026-06-11T07:00:00Z",  # ISO-8601, optional
    "source_label": "Description of data source",
    "why_shown": "Why this card was created (points to Hermes context)",
    "payload": {
        "section": "now|today|week|watching",
        "ai_curated": True,
        "relevance_score": 0-150,  # optional boost
        "metrics": [{"label": "...", "value": "...", "unit": "..."}],
        "items": [{"title": "...", "summary": "...", "url": "...", "source": "...", "time": "..."}],
        "sections": [{"label": "...", "items": [...]}]
    }
}
```

## Key Patterns from This Session

### Refresh Alert Cards (Frequent Signal)
```python
# 1. Scan context
result = core.refresh_from_hermes_context(
    include_sessions=True,
    include_cron=True,
    create_cards=False
)

# 2. Read inferred context
items = core.list_context_items(include_hidden=False, limit=100)

# 3. Upsert stable cards for high-signal topics
#    Use stable IDs: alert-openrouter-budget, alert-openrouter-heartbeat, etc.
core.upsert_card(card_dict)

# 4. Record refresh
core.record_refresh({
    "job_key": "autonomous-alert-refresh",
    "status": "success",
    "summary": "...",
    "payload": {"cards_updated": N}
})
```

### Deduplication Strategy
- Always use stable IDs for the same user-facing topic
- Before creating new cards, check existing with `list_cards()`
- Dismiss duplicates with `dismiss_card()` if accidentally created
- Prefer updating existing stable cards over creating new ones