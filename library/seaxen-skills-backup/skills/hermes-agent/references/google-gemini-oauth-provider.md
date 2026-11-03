# Google Gemini OAuth Provider (`google-gemini-cli`) — v0.16.0+

## Overview
Hermes v0.16.0+ includes a **first-class OAuth provider** for Google Gemini via the `google-gemini-cli` provider ID. This uses Google's **Cloud Code Assist** backend (not the official AI Studio API).

| Provider ID | Auth Type | Backend |
|-------------|-----------|---------|
| `google-gemini-cli` | OAuth (PKCE + browser) | Cloud Code Assist |
| `gemini` | API key (`GOOGLE_API_KEY`) | Official AI Studio (`generativelanguage.googleapis.com`) |

## Setup
```bash
# Interactive picker
hermes model
# → Select "Google Gemini (OAuth)"

# Or direct auth add
hermes auth add google-gemini-cli
```
Opens browser → Google account authorization → tokens saved to `~/.hermes/gemini_oauth.json` (0o600).

## Credential Pooling (Multiple Accounts)
Multiple accounts work via **credential pools** — same pattern as `openai-codex`:

```bash
# Add 2nd account
hermes auth add google-gemini-cli --label account2

# Add 3rd account
hermes auth add google-gemini-cli --label account3
```

Result:
```
google-gemini-cli (3 credentials):
  #1  account1    oauth  ... ← (active)
  #2  account2    oauth  ...
  #3  account3    oauth  ...
```

### Rotation Strategy
Default: `fill_first` (uses first healthy credential until quota exhausted, then rotates).
```bash
# Round-robin instead
hermes config set credential_pool_strategies.google-gemini-cli round_robin
```

### Limitation
- **No manual switch command** (`hermes auth use` doesn't exist) within same session
- For manual switching: create separate profiles per account
  ```bash
  hermes profile create gemini-account2 --clone
  hermes profile use gemini-account2
  ```

## Quota / Usage
- Uses Cloud Code Assist quota (different from AI Studio limits)
- Check with slash command: `/gquota` (only works when `google-gemini-cli` provider is active)
- Free tier available

## Important Caveats
1. **Not the official AI Studio API** — different backend, different quota, different rate limits
2. **Data logging** — Google may use Cloud Code Assist data for training
3. **Account ban risk** (per implementation plan) — Cloud Code Assist is an internal API
4. For production/official API: use `provider: gemini` with `GOOGLE_API_KEY`

## Environment Variables (Optional Override)
| Variable | Purpose |
|----------|---------|
| `HERMES_GEMINI_CLIENT_ID` | OAuth client ID (defaults to Google's public gemini-cli client) |
| `HERMES_GEMINI_CLIENT_SECRET` | OAuth client secret |

## Files
- OAuth flow: `agent/google_oauth.py` (PKCE, localhost callback on port 8085)
- Provider registration: `plugins/model-providers/gemini/__init__.py`
- Auth commands: `hermes_cli/auth_commands.py` (`_OAUTH_CAPABLE_PROVIDERS` includes `google-gemini-cli`)
- Provider overlay: `hermes_cli/providers.py` (line 79, 313-314)

## Verification
```bash
# Check auth status
hermes auth list google-gemini-cli

# Test model
hermes chat -m gemini-2.5-flash -q "test" --provider google-gemini-cli
```