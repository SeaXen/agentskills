# OpenRouter Free Models — May 2026 Reference

## Top Free Models (`:free` suffix or $0 pricing)

These are the best free models available on OpenRouter as of May 2026, verified $0 input/output cost.

### Tier 1 — Best All-Rounders (use these first)

| Model ID | Context | Vision | Strengths |
|----------|---------|--------|-----------|
| `qwen/qwen3.6-plus:free` | **1M** | ✅ Multimodal | SWE-bench 78.8, agentic coding, reasoning, hybrid MoE, 376B weekly usage — **best overall free model** |
| `openrouter/owl-alpha` | 1.05M | ❌ Text only | Agentic workflows, tool use, code generation, 480B weekly usage, but proprietary + logs prompts |
| `nvidia/nemotron-3-super-120b-a12b:free` | 1M | ❌ Text only | Complex multi-agent, reasoning, 120B MoE (12B active) |

### Tier 2 — Multimodal (text + images)

| Model ID | Context | Modalities | Strengths |
|----------|---------|------------|-----------|
| `nvidia/nemotron-3-nano-omni-30b-a3b-reasoning:free` | 256K | **Text + Image + Video + Audio** | Best free omni-modal; MoE 30B-A3B, reasoning support, ~2× throughput |
| `google/gemma-4-31b-it:free` | 256K | Text + Image | 30.7B dense, configurable reasoning, 140+ languages, Apache 2.0 |
| `google/gemma-4-26b-a4b-it:free` | 262K | Text + Image | Strong vision + tools |
| `nvidia/nemotron-nano-12b-v2-vl:free` | 128K | Text + Image | Compact vision + language |

### Tier 3 — Specialized / Lightweight

| Model ID | Context | Strengths |
|----------|---------|-----------|
| `inclusionai/ring-2.6-1t:free` | 262K | 1T params (63B active), adaptive reasoning, agents, tool use |
| `minimax/minimax-m2.5:free` | 197K | SWE-Bench 80.2%, productivity, coding, token efficient |
| `openai/gpt-oss-120b:free` | 131K | 117B MoE (5.1B active), high-reasoning, agentic, Apache 2.0 |
| `openai/gpt-oss-20b:free` | 131K | 21B MoE (3.6B active), lightweight agentic |
| `nvidia/nemotron-3-nano-30b-a3b:free` | 256K | Efficient agentic, open weights |
| `z-ai/glm-4.5-air:free` | 131K | Hybrid thinking, agent-centric, MoE |
| `nvidia/nemotron-nano-9b-v2:free` | 128K | Compact agent tasks |
| `poolside/laguna-m1:free` | 131K | Coding agent, fp8 quantized |
| `baidu/cobuddy:free` | 131K | Code generation, AI agent workflows |

### Tier 4 — General Purpose (less tested)

| Model ID | Notes |
|----------|-------|
| `openrouter/elephant-alpha:free` | General purpose |
| `openrouter/polaris-alpha:free` | General purpose |
| `openrouter/sonoma-dusk-alpha:free` | General purpose |
| `openrouter/sonoma-sky-alpha:free` | General purpose |
| `tencent/hy3-preview:free` | General purpose |

### Auto-Router

| Model ID | Notes |
|----------|-------|
| `openrouter/free` | Auto-routes to best free model per request. Convenient but unpredictable. |

---

## Quick Decision Guide

| Use Case | Best Free Model |
|----------|----------------|
| **Default all-rounder** | `qwen/qwen3.6-plus:free` |
| **Vision / image input** | `nvidia/nemotron-3-nano-omni-30b-a3b-reasoning:free` or `google/gemma-4-31b-it:free` |
| **Audio + video + images** | `nvidia/nemotron-3-nano-omni-30b-a3b-reasoning:free` (only free omni-modal) |
| **Long context (1M+)** | `qwen/qwen3.6-plus:free` or `openrouter/owl-alpha` |
| **Agentic coding** | `qwen/qwen3.6-plus:free` or `minimax/minimax-m2.5:free` |
| **Multilingual (140+ langs)** | `google/gemma-4-31b-it:free` |
| **Maximum throughput** | `nvidia/nemotron-3-nano-omni-30b-a3b-reasoning:free` (MoE, ~2× speed) |

---

## Important Caveats

- **All free models may log prompts/completions** — providers may use them for training. Never send sensitive data (patient info, API keys, private data) through free endpoints. Owl Alpha explicitly states this.
- **Free models can be rate-limited, rerouted, or changed** — not suitable for production-critical work without fallback.
- **Pricing can change** — always verify current pricing at `https://openrouter.ai/models` before relying on free status.
- **No benchmarks ≠ bad model** — Newer models like Qwen3.6 Plus and Nemotron Omni lack AIbench ranking data but are community-validated as top-tier.

## How to Use These Models

### One-shot CLI
```bash
hermes chat -m qwen/qwen3.6-plus:free -q "your question"
```

### Set as default (direct config edit)
Edit `~/.hermes/config.yaml`:
```yaml
model:
  default: qwen/qwen3.6-plus:free
  provider: openrouter
```
Then start a new session (or `/reset`). Changes don't apply mid-conversation.

### Set as default (CLI)
```bash
hermes config set model.default qwen/qwen3.6-plus:free
hermes config set model.provider openrouter
# New session picks up the change
```

### Override model catalog to show ONLY free models in picker
In `config.yaml`, the `model_catalog.providers` field overrides the remote catalog. Setting `providers.openrouter.models` to a curated list means ONLY those models appear in the dashboard and CLI `/model` picker.

**Critical distinction:**
- `model_aliases` = CLI shortcuts only, does NOT affect dashboard picker
- `model_catalog.providers` = controls what appears in dashboard + CLI picker

Both should be updated together for a consistent experience.

### Per-Cron-Job Model Override
Cron jobs can specify their own model independently of the default:
```
cronjob(action='create', model={provider: 'openrouter', model: 'qwen/qwen3.6-plus:free'}, ...)
```

---

## Model Comparison Notes (session 2026-05-17)

### Qwen3.6 Plus vs Owl Alpha vs Nemotron Omni

| Feature | Owl Alpha | Qwen3.6 Plus | Nemotron Omni |
|---------|-----------|-------------|---------------|
| Text | ✅ | ✅ | ✅ |
| Vision | ❌ | ✅ | ✅ |
| Video/Audio | ❌ | ❌ | ✅ |
| Context | 1.05M | 1M | 256K |
| SWE-bench | No data | 78.8 | No data |
| Open source | ❌ Proprietary | ✅ Apache 2.0 | ✅ Open |
| Data logging | ⚠️ Yes | Standard | Standard |
| Weekly usage | 480B | 376B | 17.9B (new) |

**Verdict:** Qwen3.6 Plus is the new default best all-rounder. Nemotron Omni is best when you need audio/video. Owl Alpha keeps value for its 1.05M context + massive community usage, but the data logging and no-vision limitations make it a weaker default.
