# Cloudflare Workers AI — Pricing & Limits Deep Dive

## Official pricing

Source: https://developers.cloudflare.com/workers-ai/platform/pricing

### Free allocation
- **Workers Free plan**: 10,000 Neurons/day, no overage (hard stop)
- **Workers Paid plan**: 10,000 Neurons/day free + $0.011/1,000 Neurons overage
- Resets daily at **00:00 UTC**

### What are Neurons?
GPU compute unit representing the compute needed per request. Different models consume different neurons per token.

### Token pricing examples (per 1M tokens)

| Model | Input | Output | Neurons (in/out per M) |
|---|---|---|---|
| llama-3.2-1b-instruct | $0.027 | $0.201 | 2,457 / 18,252 |
| llama-3.1-8b-fp8-fast | $0.045 | $0.384 | 4,119 / 34,868 |
| llama-3.3-70b-fp8-fast | $0.293 | $2.253 | 26,668 / 204,805 |
| deepseek-r1-distill-qwen-32b | $0.497 | $4.881 | 45,170 / 443,756 |
| qwen3-30b-a3b-fp8 | $0.051 | $0.335 | 4,625 / 30,475 |
| gpt-oss-120b | $0.350 | $0.750 | 31,818 / 68,182 |
| glm-5.2 | $1.400 | $4.400 | 127,273 / 400,000 |

### How far does 10,000 free Neurons/day go?

| Model | Approximate free daily tokens (input only) |
|---|---|
| llama-3.2-1b | ~4M tokens |
| llama-3.1-8b-fp8-fast | ~2.4M tokens |
| llama-3.3-70b | ~375K tokens |
| deepseek-r1-32b | ~221K tokens |
| gpt-oss-120b | ~314K tokens |

Note: output tokens consume significantly more neurons than input on most models.

## Rate limits (per task type)

Source: https://developers.cloudflare.com/workers-ai/platform/limits

### Text Generation (the one that matters most)
- **Default**: 300 RPM
- Per-model overrides:
  - mistral-7b-instruct-v0.1-awq: 400 RPM
  - phi-2: 720 RPM
  - qwen1.5-0.5b-chat: 1500 RPM
  - qwen1.5-14b-chat-awq: 150 RPM
  - tinyllama: 720 RPM

### Other task types
- Automatic Speech Recognition: 720 RPM
- Image Classification: 3000 RPM
- Text Embeddings: 3000 RPM
- Text-to-Image: 720 RPM
- Translation: 720 RPM

### Important notes
- Beta models may have lower rate limits
- Local mode (Wrangler) also counts toward limits
- Limits are per-account, not per-IP

## Model availability (mid-2026)

Notable models available:
- Meta Llama 4 Scout, 3.3-70B, 3.1-8B, 3.2 variants
- DeepSeek R1 distill
- Mistral Small 3.1-24B
- Qwen3-30B, QWQ-32B
- OpenAI GPT-OSS-120B, GPT-OSS-20B
- GLM-5.2, GLM-4.7-flash
- Kimi K2.6, K2.7-code
- Gemma 4-26B
- IBM Granite 4.0
- Flux-2 (image gen), Whisper (audio)

## Comparison with NVIDIA NIM

| Dimension | CF Workers AI | NVIDIA NIM |
|---|---|---|
| Free daily limit | 10K Neurons (resets daily) | ~5K credits (one-time) |
| Rate limit | 300+ RPM | ~40 RPM |
| Production use | Paid tier OK | Requires AI Enterprise |
| Model variety | 100+ (open models) | 160+ (incl. proprietary) |
| Biggest free models | 70B (llama-3.3) | 550B (nemotron-3-ultra) |
| Billing unit | Neurons ($0.011/1K) | Credits (trial only) |

## Source URLs

| Source | URL |
|---|---|
| Pricing | https://developers.cloudflare.com/workers-ai/platform/pricing |
| Limits | https://developers.cloudflare.com/workers-ai/platform/limits |
| Changelog | https://developers.cloudflare.com/workers-ai/changelog |
| Dashboard | https://dash.cloudflare.com/?to=/:account/ai/workers-ai |
