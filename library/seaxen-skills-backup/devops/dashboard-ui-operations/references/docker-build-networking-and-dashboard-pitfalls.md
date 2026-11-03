# Docker Build-Time Networking Pitfall

When a Dockerfile's `RUN pip install` or `RUN npm install` fails with `Network is unreachable` or `Connection refused`, but `network_mode: host` is already set in docker-compose.yml — the problem is that **`network_mode: host` only applies at RUNTIME, not during `docker build`**.

**Fix:** Add `network: host` to the build context in docker-compose.yml:
```yaml
services:
  myapp:
    build:
      context: .
      network: host    # ← Forces build-time network to use host networking
    network_mode: host  # ← Runtime (already set)
```

This passes `--network=host` to `docker build`, so pip/npm can reach PyPI/npmjs during the build phase.

**⚠️ PITFALL: `--mount=type=cache` requires BuildKit.** If the Docker daemon doesn't have BuildKit enabled, `RUN --mount=type=cache,target=/root/.cache/pip pip install ...` fails with "the --mount option requires BuildKit". Either enable BuildKit (`DOCKER_BUILDKIT=1`) or use plain `RUN pip install --no-cache-dir -r requirements.txt`.

## Favicon Cache-Busting

When updating a favicon/logo in a Dockerized web app, **browsers aggressively cache favicons** even after container restarts. Adding `?v=2` (or any version param) to favicon `<link>` hrefs forces the browser to re-fetch:

```html
<link rel="icon" type="image/png" href="/static/icons/favicon-32.png?v=2">
<link rel="shortcut icon" href="/static/favicon.ico?v=2">
<link rel="apple-touch-icon" href="/static/icons/favicon-192.png?v=2">
```

Increment the version number each time you change the logo. Also update any `<img src="...">` references in the page body.

## Free Tier Cost Calculation Pattern

When building analytics dashboards that show cost per provider/API, **never blindly multiply `queries × cost_per_query`**. Most API providers have free monthly tiers. The correct pattern:

```python
# Count monthly usage per provider
current_month = datetime.utcnow().strftime("%Y-%m")
monthly_counts = Counter(log["provider"] for log in logs if log["timestamp"][:7] == current_month)

for provider, count in monthly_counts.items():
    cost_info = PROVIDER_COSTS[provider]  # {"cost_per_query": 0.008, "free_monthly": 1000}
    free_tier = cost_info["free_monthly"]
    
    if count <= free_tier:
        cost = 0.0  # Within free tier
    else:
        billable = count - free_tier
        cost = billable * cost_info["cost_per_query"]
```

Apply this in ALL cost display paths (overview card, cost breakdown, per-provider table, daily chart). Missing even one path causes confusing "$0.008" displays when the user is on free tier.
