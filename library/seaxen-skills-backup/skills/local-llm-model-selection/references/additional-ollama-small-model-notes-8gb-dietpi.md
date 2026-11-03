# Additional Ollama small-model notes on 8 GB DietPi laptop

Session-specific notes extending the baseline comparison for an Asus X455L-class machine:
- 8 GB RAM
- no discrete GPU
- DietPi / Debian
- primary daily model kept on SSD
- secondary models offloaded to HDD via symlinks

## Additional models successfully installed
- `qwen2.5-coder:3b`
- `gemma4:e2b`
- `phi4-mini`

All three were:
- pulled successfully with Ollama
- moved to HDD-backed storage under `/mnt/tb/ollama`
- kept usable by leaving symlinks in the default Ollama model store
- verified with `ollama run`

## Practical positioning
- `qwen2.5-coder:3b`
  - best candidate here for coding-oriented local help
  - good secondary model when the user wants code completion/refactoring more than general chat polish
- `gemma4:e2b`
  - smaller Gemma-family option that fits this hardware better than `gemma4:e4b`
  - better first Gemma try on 8 GB CPU-only hardware than jumping straight to `e4b`
- `phi4-mini`
  - compact extra option worth testing for short tasks
  - should not be assumed to obey exact-format prompts perfectly

## Behavioral quirks observed
- `gemma4:e2b` showed visible `Thinking...` style output during a simple verification prompt, similar to the earlier `qwen3.5:2b` behavior.
- `phi4-mini` passed a smoke test but added extra text after the requested exact string, so it is weaker for strict output-format compliance checks.

## Storage pattern that worked
The machine used a split-storage strategy:
- keep `qwen3.5:2b` on SSD for faster day-to-day startup
- move larger or less-primary models to HDD at `/mnt/tb/ollama`
- preserve Ollama compatibility by symlinking manifests and blobs back into `/usr/share/ollama/.ollama/models`

## Recommendation impact
On this class of hardware, keep recommendations separated by task:
- general chat quality: `qwen3.5:2b`
- cleaner no-thinking chat feel / daily default: `llama3.2:3b`
- coding-focused local help: `qwen2.5-coder:3b`
- Gemma-family first try: `gemma4:e2b`
- avoid as default on 8 GB RAM: `gemma4:e4b`

## Caution
Do not over-read a single smoke test:
- these notes captured install success and quick behavior quirks
- they are not full TPS / latency / RAM benchmarks for the three newly added models
- if the user asks for a final ranking among them, benchmark them on-device instead of guessing
