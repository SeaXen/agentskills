---
name: free-ai-api-tiers
description: Research and compare free AI API provider tiers, rate limits, credit systems, and cheap compute alternatives. Use when the user asks about free LLM API access, provider rate limits, API credits, free inference endpoints, cheap VPS for self-hosting, or wants to compare free tiers across providers.
tags: [ai, api, free-tier, rate-limits, credits, vps, self-hosted, inference]
triggers:
  - "free AI API"
  - "rate limit"
  - "API credits"
  - "free tier"
  - "NVIDIA NIM limits"
  - "Cloudflare Workers AI"
  - "Groq free"
  - "cheap VPS"
  - "free inference"
  - "provider limits"
---

# Free AI API Tier Research

## When to load this skill

- User asks "is X provider free/unlimited?"
- User wants to compare free tiers across AI API providers
- User asks about rate limits, credits, or token caps
- User wants cheap compute for self-hosted inference
- User is evaluating providers for cost-sensitive or high-volume use

## Research methodology

### Where to look (in priority order)

1. **Official docs/pricing page** — source of truth for current limits
   - `developers.cloudflare.com/workers-ai/platform/pricing`
   - `docs.api.nvidia.com`
   - `build.nvidia.com` (model pages, dashboard)
   - Provider-specific pricing/docs URLs

2. **Official forums/support** — reveals actual enforcement, credit mechanics
   - NVIDIA Developer Forums (`forums.developer.nvidia.com`)
   - Cloudflare Community
   - Provider Discord/GitHub issues

3. **Third-party analysis** — cross-check, get comparison context
   - LowEndBox for VPS deals
   - Reddit (r/VPS, r/selfhosted, r/LocalLLaMA)
   - Tech blogs with 2026-dated articles

### Key concepts to verify for each provider

| Concept | What to check |
|---|---|
| **Rate limit** | RPM/RPD, per-model vs per-account, hard cap vs soft |
| **Credits/tokens** | One-time allocation? Resets daily/monthly? Consumed per request? |
| **Trial vs permanent** | "Free trial" = time-limited; "free tier" = ongoing |
| **Production allowed?** | Many free tiers are "prototyping only" per ToS |
| **Overage policy** | Hard stop (402 error) vs soft throttle vs pay-as-you-go |
| **Account limits** | Single account or multi-account allowed? (usually not) |

### Common pitfalls

- **"Unlimited" in marketing ≠ unlimited in practice** — always check rate limits
- **Credits ≠ RPM** — some providers cap BOTH (NIM: credits + 40 RPM)
- **Daily resets vs one-time allocation** — CF Workers AI resets daily; NIM credits don't reset
- **Dashboard may not show all limits** — NIM dashboard shows RPM but not credits for all accounts
- **"Free" often means "for prototyping"** — production use may require paid license
- **Forum posts are often outdated** — verify against current official docs

## Known providers (as of mid-2026)

### NVIDIA NIM (build.nvidia.com)

- **Rate limit**: ~40 RPM (varies by model/account/traffic)
- **Credits**: 1000 on signup, up to 5000 total (need business email for +4000)
- **Credit behavior**: One-time allocation, does NOT reset
- **Production use**: NOT allowed — requires NVIDIA AI Enterprise ($4,500/GPU/yr)
- **How to check credits**: Profile icon on build.nvidia.com; some accounts only show RPM
- **Status when exhausted**: 402 Payment Required / "Cloud credits expired"
- **Official framing**: "Trial experience of NVIDIA NIM"
- **Forum staff quote**: "Rate of requests will vary per model queried and may vary based on concurrent users"
- **Self-host option**: Downloadable NIM containers, free for dev/test on up to 16 GPUs

### Cloudflare Workers AI

- **Rate limit**: 300 RPM default for text generation (varies per model, some up to 1500 RPM)
- **Credits**: 10,000 Neurons/day (free), resets at 00:00 UTC
- **Overage**: Not available on free plan (hard stop); Paid plan: $0.011/1K Neurons
- **What's a Neuron**: GPU compute unit; different models cost different neurons per token
- **Production use**: Yes, on paid plan ($5/mo base)
- **How far 10K neurons go**: ~4M input tokens/day on llama-3.2-1b, ~375K on 70b models
- **Model availability**: 100+ models including Kimi, DeepSeek, GLM, Llama 4 Scout, GPT-OSS
- **IP/account policy**: Limits are per-account; multi-accounting from same IP is risky

### Groq

- **Free tier**: Available with rate limits (varies by model)
- **Speed**: Ultra-fast inference (LPU-based)
- **Check**: `groq.com/pricing` for current limits

### Together AI

- **Free credit**: $5 on signup
- **Paid**: Very cheap per-token after free credit
- **Models**: Wide selection of open models

### Hugging Face Inference API

- **Free tier**: Available for many models
- **Limits**: Rate-limited, varies by model
- **Serverless endpoints**: Some models have dedicated pricing

### OpenRouter

- **Free models**: Several free models available (marked with $0 pricing)
- **Paid models**: Pass-through pricing from providers
- **Use case**: Aggregator — pool multiple providers

## Cheap VPS for self-hosted inference / proxy

### Best deals found (LowEndBox, mid-2026)

| Provider | Price | Specs | Notes |
|---|---|---|---|
| **RackNerd** | $16.88/yr (~$1.40/mo) | 1.5GB RAM, 1 vCPU, 30GB SSD, 3TB BW | Best reputation, KVM, multiple DCs |
| **RackNerd** | $20.98/yr (~$1.75/mo) | 2GB RAM, 2 vCPU, 25GB SSD, 4TB BW | Good for proxy box |
| **ServerHost** | $21.88/yr (~$1.82/mo) | 2GB RAM, 1 vCPU, 30GB NVMe, unmetered | Coupon: 2LEBA |
| **CloudServer** | $23.88/yr (~$1.99/mo) | 2GB RAM, 1 vCPU, 50GB SSD, 5TB BW | NY location |
| **BuyVM** | $2/mo | 512MB RAM, unmetered | Monthly billing available |
| **IONOS** | $2/mo | 512MB, NVMe, unlimited traffic | Monthly billing |

### Pitfalls for cheap VPS

- **$1/mo claims** usually require annual prepay ($12-18/yr upfront)
- **IPv6-only plans** (e.g. VPS1Dollar) are useless for most proxy/API use cases
- **"Unlimited" bandwidth** on budget VPS often has hidden fair-use caps
- **OVZ vs KVM** — always prefer KVM for full isolation and kernel control
- **Location matters** for latency to API endpoints

## Comparison framework

When comparing providers, evaluate:

| Dimension | Question |
|---|---|
| **Sustainability** | Is the free tier permanent or trial-only? |
| **Volume** | How many tokens/requests per day can you realistically do? |
| **Speed** | RPM limits and actual latency |
| **Models** | Which models are available on free tier? |
| **Production use** | Can you use it in production or only prototyping? |
| **Exit cost** | What happens when you outgrow free tier? |

## User preferences (this user)

- Interested in sustained free/cheap inference, not just testing
- Running OmniRoute gateway — pools multiple providers
- Has Bynara accounts (10x) for subscription-based access
- Self-hosts on DietPi server (192.168.0.222)
- Prefers concise answers; asks for "one-line answer" when needed
- Willing to combine multiple free tiers for aggregate capacity
