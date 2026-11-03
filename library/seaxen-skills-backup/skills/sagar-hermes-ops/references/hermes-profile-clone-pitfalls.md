# Hermes Profile Cloning — Pitfalls and Correct Flags

## The Trap

`hermes profile create <name> --clone-all` **sounds like "clone my whole setup"** but actually copies **all runtime state**:
- `state.db` (session database — can be 1GB+)
- `cache/`, `logs/`, `backups/`, `state-snapshots/`
- `analytics/`, `repos/`, `scripts/`, `vendor/`
- Telemetry files, history, PID files, gateway state

**Result:** 3+ GB profile that includes stale runtime files, not a clean clone.

## The Correct Flag

```bash
hermes profile create <name> --clone
```

**Copies only:**
- `config.yaml` (model, providers, tools, agent settings)
- `.env` (API keys, secrets)
- `SOUL.md` (personality)
- `skills/` manifest (bundled skills reference, not full copies)

**Size:** ~100 MB (mostly skills manifest references)

## When to Use Each

| Flag | Use Case |
|---|---|
| `--clone` | New profile with same config/keys/skills — clean slate for a different role (e.g., `coder`, `researcher`, `medicine`) |
| `--clone-all` | Almost never. Only if you truly need identical runtime state (active sessions, caches, DB) — e.g., debugging a specific session replay. |
| (none) | Fresh empty profile — you'll run `setup` and configure from scratch |

## Verification After Cloning

```bash
# Check size — should be ~100 MB, not GB
du -sh ~/.hermes/profiles/<name>/

# Verify config copied
cat ~/.hermes/profiles/<name>/config.yaml

# Verify keys present
cat ~/.hermes/profiles/<name>/.env | head -5

# Verify skills manifest
ls ~/.hermes/profiles/<name>/skills/
```

## Common Mistake Pattern

User says: *"I want a new profile with all my current setup"*  
→ They mean: same model, same API keys, same skills  
→ They run: `--clone-all` (thinking "all" = "my complete setup")  
→ They get: massive profile with stale DB/cache  
→ They need: `--clone`

**Always clarify:** "Do you want a clean profile with your config/keys/skills (`--clone`), or a byte-for-byte runtime clone including session DB and cache (`--clone-all`)?"

## Related

- `sagar-hermes-ops` skill: throwing away profiles for experiments (step 6)
- `memory-hygiene`: keeping profiles clean
- `hermes-agent` bundled skill: profile management commands