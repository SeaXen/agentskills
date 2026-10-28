# Free-tier limits and fallback behaviour (Gate L)

Every service an app depends on must have a free tier, and the README must say **what breaks when
the limit is hit** and **what the app does instead**. A limit without a fallback is not a plan.

> **Limits change.** The numbers below are the commonly documented free-plan quotas. Re-check the
> official pricing page before publishing them, and state the date you checked (`as of YYYY-MM-DD`)
> so the README can be audited later. If a limit has moved, update this file — not the README alone.

## Limits table (verify before shipping)

| Service | Free tier (typical) | What breaks at the limit | Fallback the app must implement |
|---------|---------------------|--------------------------|----------------------------------|
| Cloudflare Workers | 100k requests/day | Requests rejected (HTTP 1014/429) | Serve the static build from Pages/Netlify; cache aggressively; queue non-critical work |
| Cloudflare Pages | 500 builds/month, 20k files/page | Build quota exhausted | Build in CI and deploy the artefact; keep the Pages build optional |
| Cloudflare D1 | 5M rows read/day, 100k writes/day | Queries fail | Cache reads; batch writes; fall back to the local/SQLite store |
| Cloudflare KV | 100k reads/day, 1k writes/day, 1k deletes/day | Latency spikes / write failures | TTL cache, write-behind, in-memory fallback |
| Cloudflare R2 | 10 GB stored, 1M writes/month | Uploads rejected | Store locally; degrade to a placeholder asset |
| Vercel | Hobby: 100 GB bandwidth/month, 1000 build minutes (approx.) | Build blocked / bandwidth exceeded | Self-host the build output; Netlify or Cloudflare Pages as a second target |
| Netlify | 300 build minutes/month, 100 GB bandwidth | Build blocked | Build in CI, deploy the `dist/` output; keep Pages as a second target |
| Railway | Trial credits, then usage-based | Service sleeps or is suspended | Fly.io/Render target; local fallback path; document a cold-start impact |
| Render | Free web services sleep after inactivity | First request is slow (cold start) | Warm-up ping, health check, or accept and document the delay |
| Fly.io | Allow-list / trial allowances | Machine scaled to zero or removed | Local Docker compose path documented in the README |
| GitHub Actions | 2,000 minutes/month (public repos are free) | CI stops running | Run the same commands locally; keep the workflow reproducible |
| Sentry (free) | 5k errors/month, 1 user | Error events dropped | Log to stdout/stderr and read the platform logs; keep the hook optional |
| Supabase / Neon (if used) | Free tier row/connection limits | Queries rejected | In-memory or SQLite store for local/dev; degrade reads |
| Stripe test mode | No live fees in test mode | n/a | Keep payments behind a flag so the app runs without them |

## README requirements (Gate L checklist)

- [ ] A table listing every external service, its free-tier limit, and the fallback
- [ ] The fallback column is filled in with a **real** behaviour of the app, not "upgrade to paid"
- [ ] Cold-start / sleep behaviour stated for Railway, Render, Fly
- [ ] Cloudflare bindings documented as optional, with the portable default
- [ ] No paid-only SDK is required to run the app
- [ ] The date the limits were checked is stated

Template:

```markdown
## Free-tier limits

| Service | Free limit | When it breaks | Fallback |
|---------|-----------|----------------|----------|
| Cloudflare Workers | 100k req/day (checked 2026-01-15) | Requests rejected | Static build served from Pages; API calls degrade to read-only cache |
| Netlify | 300 build min/mo | Builds blocked | Builds run in GitHub Actions; `dist/` is deployed as an artefact |

Sleeping/cold start: Render free services sleep after 15 min idle; first request takes ~30 s.
```

## How this is verified

`scripts/verify_claims.py` gate **L**:

- `VERIFIED` — the README documents free-tier limits **and** the fallback behaviour
- `CONTRADICTED` — limits are documented but the fallback is missing
- `UNSUPPORTED` — no free-tier limits are documented at all

Treat a paid-only dependency as a **blocking** finding for this skill: the app must run on a free
account, end to end.
