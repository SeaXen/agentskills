# Together AI Fabric Training Pitfalls

## What We Learned (2025-05-23)

User's Together AI account had two problems that made `fabric_train` non-functional:

### Problem 1: Wrong Model ID in Config

- **Configured:** `meta-llama/Llama-4-Scout-Free` (with `-Free` suffix)
- **Actual Together AI ID:** `meta-llama/Llama-4-Scout-17B-16E-Instruct` (no suffix)
- Hermes config had the wrong name. The model doesn't exist under that ID.
- **Fix:** Query `/v1/models` to find the correct ID, update config with `hermes config set model.model "meta-llama/Llama-4-Scout-17B-16E-Instruct"`

### Problem 2: Zero Credits

- API key was valid (returned 200 on `/v1/models`)
- But inference returned: `"Credit limit exceeded, please add credits"`
- Free tier credit was fully consumed
- **Fix:** Either add payment at Together AI dashboard, or switch to local training

### Diagnostic Steps

```bash
# Extract key from config
KEY=$(grep -oP 'tgp_v1_\S+' ~/.hermes/config.yaml | head -1)

# Check API key validity
curl -s -o /dev/null -w "%{http_code}" "https://api.together.xyz/v1/models" -H "Authorization: Bearer $KEY"
# 200 = key valid

# List available models (save to file first, then parse)
curl -s "https://api.together.xyz/v1/models" -H "Authorization: Bearer $KEY" > /tmp/together_models.json
python3 -c "
import json
with open('/tmp/together_models.json') as f:
    data = json.load(f)
matches = [m['id'] for m in data if 'scout' in m['id'].lower() or 'free' in m['id'].lower()]
for m in matches: print(m)
"

# Test inference
curl -s "https://api.together.xyz/v1/chat/completions" \
  -H "Authorization: Bearer $KEY" \
  -H "Content-Type: application/json" \
  -d '{"model":"meta-llama/Llama-4-Scout-17B-16E-Instruct","messages":[{"role":"user","content":"OK"}],"max_tokens":10}'
```

### Key Constraint

`fabric_train` hardcodes Together AI as the **only** training backend. No config option exists to use OpenAI, SambaNova, OpenRouter, or any other provider for fabric fine-tuning. If Together AI is unavailable, use local training skills instead:
- `unsloth` — fastest local LoRA/QLoRA (needs GPU)
- `axolotl` — YAML-based local fine-tuning
- `fine-tuning-with-trl` — TRL/HuggingFace ecosystem
