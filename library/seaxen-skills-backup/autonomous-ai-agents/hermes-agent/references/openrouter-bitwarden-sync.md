# OpenRouter + Bitwarden Secrets Manager Sync

## Workflow
1. **Check `.env`**:
   ```bash
   grep OPENROUTER_API_KEY ~/.hermes/.env
   ```
   - If placeholder (`your_o...here`), proceed.

2. **Fetch key**:
   ```bash
   ~/.hermes/bin/bws secret get "OPENROUTER_API_KEY" \
     --project "56db2237-d1af-4366-9e26-b45900708add" \
     --output json | jq -r '.value'
   ```

3. **Update `.env`**:
   ```bash
   sed -i "s/OPENROUTER_API_KEY=.*/OPENROUTER_API_KEY=<fetched-key>/" ~/.hermes/.env
   ```

4. **Restart Hermes**:
   ```bash
   hermes gateway restart
   ```

5. **Verify**:
   ```bash
   hermes chat -q "test" -m openrouter/owl-alpha --provider openrouter -Q
   ```

## OpenRouter API Quirk
- **Invalid keys return `HTTP 401`**, not `403` or `404`.
- Always test with:
  ```bash
  curl -s "https://openrouter.ai/api/v1/auth/key" -H "Authorization: Bearer sk-or-..." | jq
  ```
  - `200` = valid key.
  - `401` = revoked/malformed key.