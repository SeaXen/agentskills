# Ollama small-model fit notes

Live-checked notes from a session comparing realistic CPU-only laptop choices.

## User hardware in that session
- Asus X455L
- 8 GB RAM
- no discrete GPU
- DietPi Linux

## Verified Ollama library observations

### Gemma 4
- `gemma4:e2b` — 7.2 GB, 128K context, text+image
- `gemma4:e4b` — 9.6 GB, 128K context, text+image
- `gemma4:26b` — 18 GB
- `gemma4:31b` — 20 GB

Practical note: despite the "edge" label, `gemma4:e4b` is a poor fit for many 8 GB RAM CPU-only laptops because the shipped model artifact itself is 9.6 GB.

### Qwen 3.5
- `qwen3.5:0.8b` — 1.0 GB, 256K context, text+image
- `qwen3.5:2b` — 2.7 GB, 256K context, text+image
- `qwen3.5:4b` — 3.4 GB, 256K context, text+image
- `qwen3.5:9b` — 6.6 GB, 256K context, text+image

Practical note: `qwen3.5:2b` was the most realistic general-purpose recommendation among the compared models for 8 GB CPU-only use.

Behavior note: in one live `ollama run qwen3.5:2b` check, the model emitted a visible `Thinking...` / `Thinking Process:` trace before the final answer, even for a simple compliance prompt. That made it a weaker choice for users who want clean direct chat output.

### Qwen 2.5 Coder
- `qwen2.5-coder:3b` — 1.9 GB, 32K context, text only

Practical note: best coding-focused choice in that comparison because it is much lighter than Gemma 4 E4B while still specialized for code.

### Llama 3.2
- `llama3.2:3b` — 2.0 GB, 128K context, text only

Practical note: safe and light, but generally less compelling than newer Qwen choices unless the user specifically prefers Llama.

## Recommendation pattern derived from this comparison
- General everyday use on 8 GB CPU-only laptop: `qwen3.5:2b`
- Coding-first use on the same machine: `qwen2.5-coder:3b`
- Avoid recommending `gemma4:e4b` as the default on 8 GB RAM just because benchmarks are higher

## Reminder
These observations are runtime-specific and time-sensitive. Re-check Ollama before quoting exact tags, sizes, or defaults.