# Cron jobs with custom providers: use `no_agent: true` + direct API

## The problem
When a cron job specifies `model` + `provider` different from the Hermes default config, the **agent-mode** cron (`no_agent: false`) often fails at LLM call time:

```
RuntimeError: No LLM provider configured. Run `hermes model` to select a provider...
```

Even though the job JSON records `model: "openrouter/owl-alpha"` and `provider: "openrouter"`, the cron runner spawns an agent using the **default config** (e.g. `provider: nous`), not the job's override.

## Root cause
The cron scheduler re-uses the base Hermes config for agent initialization and does not apply the per-job `model`/`provider` fields before the LLM is called.

## Solution
Make the cron job **pure `no_agent: true`** with a self-contained Python script that:

1. Collects/transforms data (vault scan, session list, etc.)
2. Calls the target provider API **directly via HTTP** (e.g. `urllib.request` to `https://openrouter.ai/api/v1/chat/completions`)
3. Reads `OPENROUTER_API_KEY` (or other) from environment — **Bitwarden Secrets Manager injects this at runtime**
4. Writes results to the vault via `file` operations (no agent tools needed)

## Pattern
```json
{
  "job_id": "...",
  "script": "my_collector_and_llm.py",
  "no_agent": true,
  "model": null,
  "provider": null,
  "enabled_toolsets": []
}
```

The script is a single Python file doing everything: collection → LLM call → vault writes.

## Why this works
- Bitwarden injects `OPENROUTER_API_KEY` (and other keys) into the cron subprocess environment automatically
- No Hermes agent initialization → no provider resolution → no fallback to default config
- Total control over model, parameters, prompt, retries
- Lower overhead, fewer moving parts

## Tradeoffs
✅ Reliable provider selection
✅ Lower latency (no agent startup)
✅ Works even if main Hermes config points to a different provider
❌ Script must be self-contained (no agent tools like `session_search`, `web_search`, etc.)
❌ More Python to maintain
❌ LLM call logic duplicated in script

## When to use
- Any cron job that needs a specific provider/model
- Nightly distillation jobs (Obsidian, memory, analytics)
- Any scheduled LLM task where quota/cost requires a cheaper model than the default

## Example scripts in this vault
- `/root/.hermes/scripts/obsidian_nightly_hybrid_full.py` — collector + OpenRouter call + vault writes
- `/root/.hermes/scripts/obsidian_nightly_signal_collector.py` — collector only (for agent-mode use)

## Anti-pattern to avoid
Do **not** keep `no_agent: false` and expect `model`/`provider` fields to work. They are stored but not honored by the cron runner's agent bootstrap.