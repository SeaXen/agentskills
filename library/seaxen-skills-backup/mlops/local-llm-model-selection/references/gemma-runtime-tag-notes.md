# Gemma runtime tag notes

Session-derived reminder for local-model recommendation tasks.

## Ollama observations captured from live library view

At time of capture, Ollama search results showed:

- `gemma3n` tags included `e2b` and `e4b`
- `gemma3` tags included `270m`, `1b`, `4b`, `12b`, `27b`
- `medgemma` included `4b` and `27b`

## Important naming pitfall

A user may ask for `gemma4:e2b` or `gemma4:e4b` because the naming sounds plausible. Do **not** confirm from memory.

Instead:
1. Check the runtime registry actually in use
2. Confirm the exact family and tag name
3. Only then provide an `ollama run ...` command

## Recommendation pattern for weak laptops

For 8 GB RAM, CPU-only machines:
- First try: `gemma3n:e2b`
- Possible heavier try: `gemma3:1b` or `gemma3n:e4b`
- Warn clearly before suggesting `4b`-class variants on old CPUs

## Scope note

These notes are runtime-specific and may age. Re-verify before quoting exact tags.