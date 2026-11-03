# Free-tier-aware cost calculation for analytics dashboards

When building analytics dashboards that track per-query costs (search APIs, LLM tokens, etc.), **never** blindly multiply `count × cost_per_query`. Most providers have free monthly tiers. If usage is within the free tier, cost must be **$0.00**.

## The bug

```python
# WRONG — shows phantom costs even when all usage is free
cost = searches * PROVIDER_COSTS[name]["cost_per_query"]
```

## The fix

```python
# RIGHT — respects free monthly tiers
free_tier = cost_info.get("free_monthly", 0)
monthly_used = monthly_counts.get(provider, 0)

if monthly_used > free_tier and free_tier > 0:
    billable_ratio = (monthly_used - free_tier) / monthly_used
    cost = cost_info["cost_per_query"] * billable_ratio
elif free_tier == 0 and cost_info["cost_per_query"] > 0:
    cost = cost_info["cost_per_query"]  # truly no free tier
else:
    cost = 0.0  # within free tier
```

## Apply to ALL cost paths

A single missed path shows phantom costs. Every one of these needs the free-tier check:
1. **Overview** `cost_today` — sum of today's queries
2. **Provider breakdown** `cost` — per-provider total
3. **Cost analysis** `daily_costs` — daily aggregation
4. **Cost analysis** `provider_costs` — per-provider aggregation  
5. **Monthly projection** — extrapolated from daily average

## Expose free tier info to the UI

Return per-provider:
```python
{
    "cost": 0.0,
    "cost_per_query": 0.008,
    "free_monthly": 1000,
    "free_remaining": 998,
    "within_free_tier": true,
}
```

## UI display

- `$0.00` in green when within free tier
- Actual cost in accent/amber when over free tier
- Show "free remaining" count in provider table

## Common free tiers (search providers)

| Provider | Cost/query | Free/month |
|----------|-----------|------------|
| SearXNG | $0.00 | unlimited |
| Serper | $0.001 | 2,500 |
| Brave | $0.005 | 1,000 |
| Exa | $0.007 | 1,000 |
| Tavily | $0.008 | 1,000 |
| DuckDuckGo | $0.00 | unlimited |

## Pitfall: check current month, not all-time

Use `datetime.utcnow().strftime("%Y-%m")` to scope monthly counts. If you sum all-time searches, you'll always exceed free tiers eventually and show costs retroactively.
