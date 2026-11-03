# Card Templates for Personal Dashboard

## Alert Card Template (Budget / Threshold)

```json
{
  "id": "stable-topic-id",
  "domain": "alerts",
  "title": "Topic: 🔴 STATUS - key metrics",
  "summary": "Human-readable summary with key numbers and context.",
  "priority": "critical|high",
  "status": "active",
  "source_label": "Source system name",
  "why_shown": "Why this matters to the user — connects to their goals/config.",
  "valid_until": "2026-06-11T07:30:00Z",
  "payload": {
    "section": "now",
    "ai_curated": true,
    "relevance_score": 75-90,
    "metrics": [
      {"label": "Metric Name", "value": "value", "unit": "unit"},
      ...
    ]
  }
}
```

## News/Feed Card Template (Model Changes / Updates)

```json
{
  "id": "stable-topic-id",
  "domain": "news",
  "title": "Topic: N update(s) - brief description",
  "summary": "What changed and why it matters.",
  "priority": "medium",
  "status": "active",
  "source_label": "Source system name",
  "why_shown": "User watches this domain.",
  "valid_until": "2026-06-11T07:30:00Z",
  "payload": {
    "section": "today",
    "ai_curated": true,
    "relevance_score": 50-60,
    "news_items": [
      {"title": "Change title", "summary": "Why it matters", "source": "Source", "time": "ISO8601"},
      ...
    ]
  }
}
```

## Project/Backup Card Template (Success / Status)

```json
{
  "id": "stable-topic-id",
  "domain": "projects",
  "title": "Topic: ✅ Key metrics",
  "summary": "What completed, key numbers, retention policy.",
  "priority": "medium|low",
  "status": "active",
  "source_label": "Cron job name",
  "why_shown": "Operational verification user expects.",
  "valid_until": "2026-06-11T07:30:00Z",
  "payload": {
    "section": "today",
    "ai_curated": true,
    "relevance_score": 50-60,
    "metrics": [
      {"label": "Size", "value": "2.02", "unit": "GiB"},
      {"label": "Files", "value": "52311", "unit": ""},
      {"label": "Status", "value": "✅ SUCCESS", "unit": ""},
      {"label": "Retention", "value": "Keep last 3", "unit": ""}
    ]
  }
}
```

## Summary Card Template (Cron Health / Multi-section)

```json
{
  "id": "stable-topic-id",
  "domain": "projects",
  "title": "Topic: N active, M paused",
  "summary": "One-line overview with key categories.",
  "priority": "low",
  "status": "active",
  "source_label": "Configuration source",
  "why_shown": "Operational visibility.",
  "valid_until": "2026-06-11T07:30:00Z",
  "payload": {
    "section": "watching",
    "ai_curated": true,
    "relevance_score": 40,
    "metrics": [
      {"label": "Active", "value": "9", "unit": ""},
      {"label": "Paused", "value": "1", "unit": ""},
      {"label": "Total", "value": "10", "unit": ""}
    ],
    "sections": [
      {"label": "Category 1", "items": ["Item 1 (detail)", "Item 2 (detail)"]},
      {"label": "Category 2", "items": ["Item 3 (detail)"]}
    ]
  }
}
```

## Domain → Section Mapping

| Domain | Default Section |
|--------|-----------------|
| alerts | now |
| calendar | now |
| family | today |
| news | today |
| planning | week |
| projects | watching |
| sports | week |
| stocks | watching |
| weather | now |

## Stocks/Crypto Card Template (Real-time Market Data)

```json
{
  "id": "stable-topic-id",
  "domain": "stocks",
  "title": "Topic: Symbol $Price (Change%)",
  "summary": "Concise snapshot with key prices, 24h/7d changes, and context metrics.",
  "priority": "high|medium",
  "status": "active",
  "source_label": "CoinGecko live data (or provider)",
  "why_shown": "User trades/watches these assets (per MEMORY.md or session context).",
  "valid_until": "2026-06-11T05:00:00Z",
  "payload": {
    "section": "now",
    "ai_curated": true,
    "relevance_score": 75-90,
    "tickers": [
      {
        "symbol": "BTC",
        "price": 61462.02,
        "change_24h_pct": 0.3,
        "change_7d_pct": 6.4,
        "market_cap": 1231000000000,
        "volume_24h": 26940000000,
        "ath": 126080,
        "vs_ath_pct": -51.3,
        "dominance_pct": 55.99
      },
      {
        "symbol": "ETH",
        "price": 1618.7,
        "change_24h_pct": 1.6,
        "change_7d_pct": 9.0,
        "market_cap": 194990000000,
        "volume_24h": 12410000000,
        "ath": 4946.05,
        "vs_ath_pct": -67.3,
        "dominance_pct": 8.97,
        "gas_standard_gwei": 0.134
      }
    ],
    "updated_at": "2026-06-11T04:03:30Z"
  }
}
```

**Use when**: User trades crypto/stocks and hourly refresh is configured. Fetch live data from CoinGecko or similar. Set `valid_until` to next refresh (typically 1h).

## Alert Card Template — Silent Health Check (Watchdog)

```json
{
  "id": "stable-topic-id",
  "domain": "alerts",
  "title": "Service: healthy (last check HH:MM)",
  "summary": "Watchdog silent = healthy. Last check timestamp, schedule, and that no alert means success.",
  "priority": "medium",
  "status": "active",
  "source_label": "Watchdog cron job name (Job ID)",
  "why_shown": "Critical dependency (secrets, auth, infra) monitored by watchdog; silent = success.",
  "valid_until": "2026-06-11T05:00:00Z",
  "payload": {
    "section": "now",
    "ai_curated": true,
    "relevance_score": 50-60,
    "schedule": "every 15m",
    "status": "healthy",
    "last_check": "2026-06-11T09:49:40+06:00",
    "updated_at": "2026-06-11T04:03:30Z"
  }
}
```

**Use when**: A watchdog cron runs frequently and only alerts on failure. Silent = healthy. Update card on each run with latest check time. On failure, change priority to `critical`, status to `alert`, and include error details.

## Planning Card Template (Cron Schedule / Daily Timeline)

```json
{
  "id": "cron-schedule-today",
  "domain": "planning",
  "title": "Today's scheduled cron jobs",
  "summary": "N automated jobs run HH:MM–HH:MM local: brief descriptions.",
  "priority": "low",
  "status": "active",
  "source_label": "Hermes cron jobs.json",
  "why_shown": "Inferred from cron jobs.json — user's daily automated workflows.",
  "valid_until": "2026-06-12T04:00:00Z",
  "payload": {
    "section": "today",
    "ai_curated": true,
    "relevance_score": 40-50,
    "timezone": "Asia/Dhaka (+06:00)",
    "updated_at": "2026-06-11T04:09:33Z",
    "items": [
      {"label": "18:00", "summary": "Job description"},
      {"label": "18:30", "summary": "Job description"}
    ]
  }
}
```

**Use when**: User has daily/weekly cron schedules in jobs.json. Parse and present as a timeline for today. Update daily.

## Domain → Section Mapping

## Priority Guidelines

| Situation | Priority |
|-----------|----------|
| Budget exceeded, service down, critical threshold breached | critical |
| Important watched items missing, high-severity alerts | high |
| Routine success with user-facing metrics, notable changes | medium |
| Background health checks, verbose operational data | low |

## Required Fields Checklist

- [ ] Stable `id` (kebab-case, unique per topic)
- [ ] Domain from known set
- [ ] Concise `title` (user-facing, descriptive)
- [ ] One-sentence `summary` with key facts
- [ ] Appropriate `priority`
- [ ] `status`: active (default)
- [ ] `source_label`: where data came from
- [ ] `why_shown`: connects to user intent/context
- [ ] `valid_until`: next refresh time (ISO8601 UTC)
- [ ] `payload` with `ai_curated: true`
- [ ] `payload.relevance_score`: 0-150 for ranking
- [ ] `payload.section`: matches domain mapping
- [ ] `payload.metrics` OR `payload.news_items` OR `payload.sections` with actual data