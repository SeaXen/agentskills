# Ollama runtime benchmarks on 8 GB DietPi laptop

Condensed findings from a live session on an Asus X455L-class machine:
- 8 GB RAM
- no discrete GPU
- DietPi / Debian
- Ollama with `qwen3.5:2b`, `llama3.2:3b`, `gemma4:e4b`

## Measured generation speed (`num_predict: 80`, temperature 0)

- `llama3.2:3b`
  - generation speed: ~4.85 tok/s
  - total time: ~19.5 s
  - load duration: ~0.31 s
- `qwen3.5:2b`
  - generation speed: ~3.58 tok/s
  - total time: ~24.8 s
  - load duration: ~0.63 s
- `gemma4:e4b`
  - generation speed: ~3.12 tok/s
  - total time: ~31.1 s
  - load duration: ~1.42 s

Practical takeaway:
- `llama3.2:3b` was the smoothest daily-use model by speed
- `qwen3.5:2b` remained competitive but slower
- `gemma4:e4b` was clearly the slowest and heaviest

## First-token latency and loaded RAM

Prompt used:
- `Write one short sentence about tea.`

Measured while stopping Open WebUI temporarily so Gemma could fit.

- `qwen3.5:2b`
  - first visible output: ~11.07 s
  - first output type: `thinking`
  - approx loaded RAM use: ~3.7 GB
  - `ollama ps` size: ~4.1 GB
- `llama3.2:3b`
  - first visible output: ~24.95 s
  - first output type: normal response text
  - approx loaded RAM use: ~2.5 GB
  - `ollama ps` size: ~2.5 GB
- `gemma4:e4b`
  - first visible output: ~217.48 s
  - first output type: normal response text
  - approx loaded RAM use: ~5.8 GB
  - `ollama ps` size: ~10 GB

Interpretation:
- `qwen3.5:2b` appears faster to start only because it emits reasoning text early
- `llama3.2:3b` is the lightest true chat model of the three
- `gemma4:e4b` is usable only as an occasional model on this hardware

## Open WebUI interaction with model loading

Observed on this machine:
- Open WebUI can stay Docker-`unhealthy` while still serving `HTTP 200`
- that health flag should not be treated as proof the UI is down
- however, keeping Open WebUI running can consume enough RAM that `gemma4:e4b` fails to load
- temporarily stopping Open WebUI can free enough memory for heavy-model benchmarking or occasional runs

## Selective HDD offload technique

Goal achieved in the session:
- keep `qwen3.5:2b` on SSD for fast daily use
- move `llama3.2:3b` and `gemma4:e4b` to HDD under `/mnt/tb/ollama`

Working approach:
1. Inspect model manifests under `/usr/share/ollama/.ollama/models/manifests/...`
2. Identify all referenced blob digests per model
3. Stop `ollama` service
4. Move the chosen models' manifests and blobs to `/mnt/tb/ollama`
5. Replace originals with symlinks
6. Restart `ollama`
7. Verify with `ollama list` and at least one test generation

Post-move result from the session:
- SSD Ollama store shrank to ~2.6 GB
- HDD store held ~11 GB
- all models remained usable through Ollama

Important caution:
- verify the mount path first; the real HDD path was `/mnt/tb`, not `/tb`
- blindly creating `/tb` would have placed data on SSD instead of HDD
