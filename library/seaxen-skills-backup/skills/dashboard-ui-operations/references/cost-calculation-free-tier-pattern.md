# Analytics Dashboard: Cost Calculation with Free Tiers

When building analytics dashboards that show costs, don't blindly multiply `queries × cost_per_query`. Most API providers have free monthly tiers.

## Problem

Dashboard showed $0.021/day cost even though all usage was within free tiers (e.g., Tavily: 2/1000 free, Brave: 1/1000 free).

## Fix

Three code paths need the same logic:

### 1. Provider table cost
```python
# Count monthly usage per provider first
current_month = datetime.utcnow().strftime("%Y-%m")
monthly_counts = Counter(l["provider"] for l in logs if l["timestamp"][:7] == current_month)

# Only charge for queries exceeding free tier
free_tier = cost_info.get("free_monthly", 0)
monthly_used = monthly_counts.get(provider, 0)
billable = max(0, monthly_used - free_tier)
if monthly_used > 0 and billable > 0:
    cost = searches * (billable / monthly_used) * cost_per_query
else:
    cost = 0.0
```

### 2. Cost breakdown (daily/provider aggregation)
Same pattern — check `monthly_used > free_tier` before applying cost.

### 3. Overview `cost_today`
Same pattern — don't sum raw `cost_per_query` for today's logs.

## Additional fields to expose

```python
{
    "cost": 0.0,
    "cost_per_query": 0.008,
    "free_monthly": 1000,
    "free_remaining": 998,      # max(0, free_tier - monthly_used)
    "within_free_tier": True,   # monthly_used <= free_tier
}
```

## Provider cost reference (search APIs)

| Provider | Cost/query | Free/month |
|----------|-----------|------------|
| searxng-search | $0 | unlimited |
| duckduckgo-free | $0 | unlimited |
| serper-search | $0.001 | 2500 |
| brave-search | $0.005 | 1000 |
| exa-search | $0.007 | 1000 |
| tavily-search | $0.008 | 1000 |
