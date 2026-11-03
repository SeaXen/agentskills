# ZenMux — free models and rate limits (research snapshot)

## `z-ai/glm-4.7-flash-free` (and other `*-free` slugs)

- Listed on https://zenmux.ai/models as free-tier models; availability can change.
- Third-party summaries (StudentOffers, search snippets): free models are **rate-limited** and offered for a **limited time** — not unlimited production tier.

## Subscription free plan (ZenMux pricing docs / search)

| Limit | Typical value cited |
|---|---|
| Rate limit | **~10–15 RPM** (requests per minute) |
| Quota window | Rolling **5-hour** refresh |
| Weekly cap | Mentioned on subscription pricing page; exact number not confirmed in static fetch |

**Pay As You Go** (prepaid credits): docs claim **no rate limits** / production-grade — different billing path.

## Operator takeaway

- Fine for light chat / occasional agent turns; **not** for parallel PONG sweeps or multi-agent bursts.
- When smoke-testing ZenMux free models, run probes **sequentially** with backoff on 429 (same as other rate-limited providers in `ai-model-smoke-test`).

Re-verify limits on https://zenmux.ai/pricing/subscription when planning heavy use.