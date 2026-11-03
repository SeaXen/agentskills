# Portal Dashboard OAuth Registration — Manual Workaround

When `hermes dashboard register` fails with "Self-hosted dashboard registration is not available for this account" but the user has already created a dashboard on the portal website (portal.nousresearch.com), wire it manually:

## Manual OAuth Client ID Setup

1. Get the OAuth client ID from the portal dashboard page (shown as `agent:cmq6qle1e00mtl50dm8k1pryq` format)

2. Set it in Hermes config:
   ```bash
   hermes config set dashboard.oauth_client_id "agent:cmq6qle1e00mtl50dm8k1pryq"
   ```

3. Start dashboard on a port matching the portal's redirect URI allowlist:
   - Portal shows: `http://localhost:<port>/auth/callback` and `http://127.0.0.1:<port>/auth/callback`
   - Use `127.0.0.1:9120` (or whatever port matches the pattern)
   ```bash
   hermes dashboard --host 127.0.0.1 --port 9120 --insecure --skip-build --no-open
   ```

4. Open `http://127.0.0.1:9120` in browser → completes OAuth flow with portal

## Why this works

- The dashboard reads `dashboard.oauth_client_id` from config.yaml (not just .env)
- Portal's redirect URI allowlist already includes localhost patterns
- No need for `hermes dashboard register` CLI command to succeed

## Troubleshooting

| Issue | Fix |
|-------|-----|
| Port already in use | `ss -ltnp | grep 9120` → kill existing process |
| OAuth redirect fails | Verify portal redirect URI allowlist matches `http://127.0.0.1:9120/auth/callback` |
| Dashboard doesn't load | Check `hermes dashboard --status` and `curl http://127.0.0.1:9120/` |

## Reference
- Portal dashboard registration page shows OAuth client ID and redirect URI allowlist
- `hermes dashboard register --help` documents the CLI command that may not work for all accounts