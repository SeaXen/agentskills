# B.AI Provider Setup for Hermes Agent

## Key Configuration Facts

| Parameter | Correct Value | Common Mistake |
|-----------|---------------|----------------|
| Base URL | `https://api.b.ai/v1` | `https://api.b.ai/v1/chat/completions` |
| Model ID format | lowercase hyphenated: `deepseek-v4-flash` | PascalCase: `DeepSeek-V4-Flash` |
| Auth header | `Authorization: Bearer sk-xxx` or `x-api-key: sk-xxx` | — |

## Available Models (from `/v1/models`)

All models support both OpenAI and Anthropic endpoints unless noted:

- `deepseek-v3.2`, `deepseek-v4-flash`, `deepseek-v4-pro`
- `minimax-m3`, `minimax-m2.5`, `minimax-m2.7`
- `kimi-k2.5`
- `glm-5`, `glm-5.1`
- `gpt-5.2`, `gpt-5.4`, `gpt-5.4-pro`, `gpt-5.4-mini`, `gpt-5-mini`, `gpt-5.4-nano`, `gpt-5-nano`, `gpt-5.5`, `gpt-5.5-instant`
- `claude-opus-4.6`, `claude-opus-4.5`, `claude-sonnet-4.6`, `claude-sonnet-4.5`, `claude-haiku-4.5`, `claude-fable-5`, `claude-opus-4.7`, `claude-opus-4.8`
- `gemini-3.1-pro`, `gemini-3-flash`, `gemini-3.5-flash`

**Note:** Some models (e.g., `deepseek-v4-flash`, `deepseek-v4-pro`, `gemini-3.5-flash`) return empty `supported_endpoint_types: []` — may not work with all endpoint types.

## Critical Limitation: Deposit Required

**All chat completions return HTTP 403** with message:
```
"Access restricted. Deposit required to unlock premium models."
```

This applies even to models that appear "free" in the UI (e.g., `deepseek-v3.2`). The `/v1/models` endpoint works without deposit, but `/v1/chat/completions` requires account credits.

### Workaround
Add credits at B.AI dashboard before using any model for chat completions.

## Hermes `custom_providers` Config

Add to `~/.hermes/config.yaml` under `custom_providers:`:

```yaml
custom_providers:
- name: "Api.b.ai"
  base_url: "https://api.b.ai/v1"
  model: "deepseek-v3.2"        # or any available model ID (lowercase)
  api_key: "sk-xxx"             # or use key_env: BAI_API_KEY
```

Then restart Hermes or `/reset` in CLI.

## Testing the Setup

```bash
# 1. Verify models endpoint
curl -H "Authorization: Bearer sk-xxx" https://api.b.ai/v1/models

# 2. Test chat completion (requires deposit)
curl -H "Authorization: Bearer sk-xxx" -H "Content-Type: application/json" \
  -d '{"model":"deepseek-v3.2","messages":[{"role":"user","content":"hi"}],"max_tokens":10}' \
  https://api.b.ai/v1/chat/completions
```

## API Documentation

Official docs: https://docs.b.ai/llmservice/api/