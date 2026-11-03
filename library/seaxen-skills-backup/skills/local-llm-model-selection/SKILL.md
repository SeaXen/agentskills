---
name: local-llm-model-selection
description: Recommend realistic local LLMs for a user's hardware, with emphasis on low-RAM CPU-only laptops and verifying model identifiers before suggesting commands.
version: 1.0.0
author: Hermes Agent
license: MIT
metadata:
  hermes:
    tags: [local-llm, model-selection, ollama, llama.cpp, cpu-inference, low-ram, benchmarking]
---

# Local LLM Model Selection

Use this skill when a user asks whether their machine can run local LLMs, which model to choose, or which benchmark numbers matter for their hardware.

## When to use

- The user gives laptop/desktop specs and wants a local model recommendation
- The user asks whether CPU-only inference is realistic
- The user asks which model family/size/quant to use in Ollama or llama.cpp
- The user asks which benchmarks matter more than leaderboard scores
- The user mentions Gemma/Qwen/Llama/Phi variants and wants a practical pick

## Core principle

Recommend for **fit and usability first**, not headline benchmark scores.

Order of importance:
1. Fits in RAM / VRAM reliably
2. Usable speed on the user's hardware
3. Quality is good enough for the actual task
4. Only then compare benchmark scores

## Minimum discovery checklist

Before recommending a model, gather:
- RAM
- CPU
- GPU / VRAM, or confirm CPU-only / integrated graphics
- OS
- Intended workload: chat, notes, coding, summarization, offline/privacy, etc.

If the user already supplied enough to make a safe recommendation, act immediately.

## CPU-only / low-RAM guidance

For older laptops with **8 GB RAM and no discrete GPU**:

- Recommend **small models only**, usually **1B-4B**
- Frame them as **usable but not impressive**
- Prioritize **Q4**-class quantizations when applicable
- Avoid promising smooth daily use from **7B+** models on old CPU-only hardware
- Explain that local models are good for:
  - short chat
  - rewrite/summarize/draft
  - lightweight note help
- Explain that they are weak for:
  - heavy reasoning
  - long context
  - fast coding workflows
  - cloud-model replacement

### Safe starting recommendations for 8 GB RAM CPU-only laptops

First-pass candidates:
- Qwen 2.5 3B Instruct, Q4
- Qwen 3.5 2B when the runtime offers a small, practical artifact size
- Llama 3.2 3B, Q4
- Gemma 2 2B, Q4
- Gemma 3 1B or Gemma 3n e2b for extra speed
- Phi small/mini class models, Q4

For Ollama specifically, a live-checked 8 GB CPU-only comparison showed:
- `qwen3.5:2b` was the best general-purpose fit
- `qwen2.5-coder:3b` was the best coding-focused fit
- `llama3.2:3b` was a safe low-friction fallback
- `gemma4:e4b` had stronger benchmark claims but was a poor fit because the artifact was much larger than the machine's RAM budget

Models to describe as experimental / likely annoying rather than recommended:
- Mistral 7B Q4 on old CPU-only hardware
- Gemma/Gemma-class 4B on very old CPUs if the user expects responsiveness
- 8B+ as a main daily model on 8 GB RAM

## Gemma-family guidance

Distinguish carefully between **family names**, **runtime tags**, and **parameter labels**.

- Do not assume a model name exists just because the family naming sounds plausible
- Verify the exact tag in the target registry before suggesting a command
- Example pitfall: Gemma naming changes across releases and runtimes; verify live before answering. As of one verified Ollama check, both `gemma3n:e2b/e4b` and `gemma4:e2b/e4b` existed, so stale memory could easily produce the wrong correction.

When the user specifically wants Gemma on weak hardware:
- Best first try: smallest practical Gemma-family variant available in their runtime
- On CPU-only 8 GB RAM machines, prefer `e2b`/`1b`/`2b`-class options before `4b`
- Treat `gemma4:e4b` cautiously on 8 GB CPU-only laptops even if it exists; a live Ollama library check showed it as a 9.6 GB model artifact, making it a poor practical fit despite stronger benchmarks

## Response-style / reasoning-trace caveat

Do not assume that a recommended small model behaves like a clean chat model in every runtime.

- Some local models or runtime presets may expose visible `Thinking...` / reasoning traces before the final answer.
- If the user explicitly wants a normal chat experience with direct final answers, call that out and suggest a cleaner-feeling alternative when available.
- In one verified Ollama session on a low-RAM laptop, `qwen3.5:2b` answered successfully but printed a visible thinking trace on a simple compliance prompt. That made `llama3.2:3b` a better recommendation for users who prioritize a no-thinking, uncluttered chat UX over raw capability.
- Treat this as runtime- and model-build-specific behavior: verify by running a tiny prompt if the distinction matters.

## Benchmark guidance

When a user asks "which benchmark is good?", answer in two layers:

Also separate three different meanings of "best":
- **best benchmark score**
- **best fit for this hardware**
- **best chat UX / least annoying runtime behavior**

Make that distinction explicit when the user compares models like Gemma vs Qwen vs Llama on an 8 GB CPU-only laptop, because the model with the best published benchmarks may be the worst lived experience on that machine.

### Quality benchmarks
- **MMLU**: broad knowledge / general capability
- **ARC-C**: reasoning/science-style multiple choice
- **HellaSwag**: commonsense completion
- **GSM8K**: basic math reasoning
- **HumanEval / MBPP**: coding

### Hardware-reality benchmarks
For local inference decisions, emphasize:
- **tokens/sec** on similar CPU/GPU
- **first-token latency**
- **RAM usage after the model is actually loaded**
- **load reliability / swap behavior**
- **their own real prompts**
- **whether the machine is collecting history at all** — if the user asks for past-24h CPU/RAM analysis and `sar`/`sysstat` is missing, install a lightweight collector first so future sessions can answer with real data instead of guesses

If the machine lacks historical metrics collection, a good default on Debian/DietPi-class systems is:
```bash
apt-get update
apt-get install -y sysstat
sed -i 's/^ENABLED=.*/ENABLED="true"/' /etc/default/sysstat
systemctl enable --now sysstat
systemctl enable --now sysstat-collect.timer sysstat-summary.timer
```
Then verify with `sar -u 1 1`, `sar -r 1 1`, and `/var/log/sysstat/saDD` files.

Teach explicitly: for weak local hardware, a slightly worse model that responds at tolerable speed is often better than a benchmark-winning model that crawls.

Important nuance from verified 8 GB CPU-only Ollama sessions:
- `llama3.2:3b` had the best steady generation speed at about **4.85 tok/s** and the lowest observed loaded RAM footprint at about **2.5 GB**
- `qwen3.5:2b` had slower generation at about **3.58 tok/s** and a higher loaded RAM footprint at about **3.7 GB**, but showed a faster first visible output because it streamed a reasoning trace
- `gemma4:e4b` was much heavier at about **5.8 GB loaded RAM**, about **3.12 tok/s**, and extremely slow to first visible output on that machine
- In a later 2-prompt live safety check on the same DietPi laptop, `llama3.2:3b` completed without crash; baseline available RAM was about **5.5 GB**, the low point was about **3.0 GB**, and extra swap usage was only about **17 MB**. Treat that as evidence that `llama3.2:3b` is one of the safer local choices on this hardware class, though still slow and still vulnerable to charger/battery instability.
- In a later Open WebUI troubleshooting session, the user-described symptom "local LLM crashes after answer completes" turned out not to be an observed service crash at check time: `open-webui` had restart count `0`, `ollama.service` had `NRestarts=0`, current-boot kernel logs showed no OOM kill, and Open WebUI SQLite `chat_message` rows showed `done=1` with `error=null`. The practical lesson is that on low-RAM laptops this complaint often means **post-answer memory pressure / heavy-runner behavior**, not literal Open WebUI container failure.

So on weak laptops, separate three things clearly:
- fastest steady generation
- fastest first visible output
- best answer quality / best benchmark score

## Verification rule: check model identifiers before naming commands

Before giving an exact runtime command:
- Verify the model/tag exists in the runtime registry or upstream repo
- For Ollama, confirm the library entry and available tags
- For llama.cpp/Hugging Face, confirm the repo and actual GGUF filenames or labels

Do not invent model IDs such as `family4:variant` from memory.

## Open WebUI / local UI deployment notes

When a user wants a quick browser UI for Ollama on Linux, Open WebUI via Docker is a strong default, but verify startup instead of assuming the container is healthy.

Recommended verification flow:
1. Confirm Ollama API is live on `http://127.0.0.1:11434/api/tags`
2. Check Docker availability and port conflicts
3. Start Open WebUI
4. Verify with an HTTP request to the UI URL, not just container health status
5. If the UI hangs during first boot, inspect logs for Hugging Face embedding-model download failures

Important pitfall discovered in a real Ollama + DietPi setup:
- Open WebUI can stall on startup while trying to download the default sentence-transformers embedding model from Hugging Face
- In one session the logs showed repeated `Network is unreachable` errors to `huggingface.co`, while Docker itself could pull the main image
- The fix was to avoid the default local sentence-transformer path and force Ollama-backed embeddings instead

Practical Docker env workaround:
- `OLLAMA_BASE_URL=http://127.0.0.1:11434`
- `RAG_EMBEDDING_ENGINE=ollama`
- `RAG_EMBEDDING_MODEL=nomic-embed-text`
- `BYPASS_EMBEDDING_AND_RETRIEVAL=true`

If bridge networking cannot reach the host Ollama service reliably, retry with host networking and verify the actual bound UI port before finalizing.

Host-network nuance discovered in a real DietPi laptop setup:
- Some machines have chronically broken Docker bridge networking for app egress or host-service access even when image pulls work.
- In that case, do **not** keep trying to force bridge mode if the user already knows it is broken; prefer host networking and keep the working setup.
- Remember that host networking changes port strategy: `-p host:container` no longer applies. To change the exposed port, configure the app itself to bind a different listen port, or keep the default working port.
- Also note that Open WebUI's Docker healthcheck may remain `unhealthy` even while the UI is actually serving `HTTP 200`; verify from `curl http://127.0.0.1:8080` or `curl http://<host-ip>:8080`, not just `docker ps`.
- On 8 GB machines, a heavy model such as `gemma4:e4b` may fail to load while Open WebUI is running; temporarily stopping the UI can free enough RAM for benchmarking or occasional use.

### If the whole laptop powers off, don't misdiagnose it as an app crash

On weak 8 GB CPU-only laptops, distinguish carefully between:
- **Open WebUI crash**
- **Ollama/service crash**
- **full-machine power-off or thermal shutdown**

If the user says the entire laptop turns off after generation:
- treat it primarily as a **thermal/power stability** problem, not just a model-fit problem
- check whether `open-webui` and `ollama.service` actually show restarts; if both remain stable and there are no OOM/segfault logs, a hard power loss is more likely than an application crash
- verify the live CPU governor; a machine stuck on `performance` can make sustained Ollama inference much harsher thermally than `schedutil`
- reduce Ollama pressure with a systemd drop-in such as `OLLAMA_CONTEXT_LENGTH=2048` and optionally `OLLAMA_KEEP_ALIVE=30s`
- if logs disappear after reboot, enable persistent journald before further troubleshooting so `journalctl -b -1` and `journalctl -k -b -1` can capture the previous boot

A verified mitigation set on an Asus X455L-class DietPi laptop was:
- switch CPU governor from `performance` to `schedutil`
- set `OLLAMA_CONTEXT_LENGTH=2048`
- set `OLLAMA_KEEP_ALIVE=30s`
- enable persistent journald under `/var/log/journal`

See also: `references/open-webui-hard-poweroff-dietpi.md`.

### Selective HDD offload for Ollama model storage

If SSD space is tight, a practical compromise is to keep the most-used small model on SSD and move infrequently used larger models to HDD.

Verified technique:
1. Inspect Ollama manifests under `/usr/share/ollama/.ollama/models/manifests/...` to identify the exact blob digests used by each model.
2. Stop the Ollama service before moving files.
3. Move the chosen model's manifest file and all referenced blobs to the HDD destination such as `/mnt/tb/ollama`.
4. Replace the original files with symlinks pointing to the HDD copies.
5. Restart Ollama and verify with `ollama list` plus at least one test run for SSD-kept and HDD-moved models.

Important caution:
- If the user names a target like `/tb/ollama`, verify it is a real mounted HDD path first. On one system the actual mount was `/mnt/tb`; blindly creating `/tb` would have placed data back on SSD.
- Expect slower model load/start time from HDD, but CPU inference may still dominate overall latency on old CPU-only laptops.

### Cleanup/uninstall after custom HDD offload

If Ollama/Open WebUI are later being removed, do not assume deleting the default Ollama paths is enough.

Required extra check:
- inspect any previously used custom model/data locations such as `/mnt/tb/ollama` and Open WebUI bind mounts such as `/mnt/tb/1Apps/open-webui-data`
- verify they are no longer referenced by live services or containers before deletion
- distinguish active runtime data from backup/docs/test-file search hits; report those separately instead of pretending they are still installed components

See also:
- `references/open-webui-ollama-dietpi.md`
- `references/open-webui-post-answer-crash-checklist-8gb-dietpi.md`
- `references/ollama-open-webui-uninstall-cleanup.md`

## Output pattern

Use a practical answer structure:

```text
Recommended first try: <model>
Why: <fit/speed/quality reason>
Also possible: <1-3 alternatives>
Avoid: <models likely too slow/heavy>
Benchmarks that matter: <quality + speed/RAM>
Expectation: <honest statement about likely responsiveness>
```

## Pitfalls

- Over-recommending 7B models for 8 GB CPU-only laptops
- Treating leaderboard scores as more important than responsiveness
- Confusing runtime tags with model-family versions
- Assuming yesterday's model/tag inventory is still current
- Naming unverified Ollama tags or GGUF variants from memory
- Recommending a model whose shipped artifact size already exceeds the user's RAM budget
- Confusing model quality with chat UX; some small models may expose visible reasoning traces that annoy users who want direct answers
- Saying a model is "good" without clarifying whether that means quality, speed, fit, or response style

## References

- **[references/dietpi-sysstat-monitoring-and-llama32-safety.md](references/dietpi-sysstat-monitoring-and-llama32-safety.md)** - How to enable lightweight `sysstat` CPU/RAM history on Debian/DietPi and a live `llama3.2:3b` two-prompt safety result on the user's 8 GB laptop
- **[references/gemma-runtime-tag-notes.md](references/gemma-runtime-tag-notes.md)** - Ollama Gemma/Gemma3n/Gemma4 tag verification notes and naming pitfalls
- **[references/ollama-small-model-fit-notes.md](references/ollama-small-model-fit-notes.md)** - Live-checked Ollama sizes and fit guidance for Gemma 4 E4B vs Qwen 3.5 2B vs Qwen 2.5 Coder 3B vs Llama 3.2 3B on 8 GB CPU-only laptops
- **[references/ollama-runtime-benchmarks-8gb-dietpi.md](references/ollama-runtime-benchmarks-8gb-dietpi.md)** - First-token latency, tokens/sec, RAM footprint, and HDD-offload notes from a real 8 GB DietPi laptop
- **[references/additional-ollama-small-model-notes-8gb-dietpi.md](references/additional-ollama-small-model-notes-8gb-dietpi.md)** - Install/behavior notes for `qwen2.5-coder:3b`, `gemma4:e2b`, and `phi4-mini`, plus split-storage recommendations on 8 GB CPU-only hardware
