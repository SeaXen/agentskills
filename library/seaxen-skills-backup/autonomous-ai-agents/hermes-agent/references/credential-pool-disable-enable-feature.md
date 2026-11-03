# Credential Pool Disable/Enable Feature

## Summary
Added `disabled` field to `PooledCredential` dataclass with CLI commands `hermes auth disable|enable` so users can temporarily hold credentials out of rotation without deleting them.

## Files Modified
- `agent/credential_pool.py` — `disabled: bool = False` field, `from_dict`/`to_dict` handling, filtered in `_available_entries()`
- `hermes_cli/auth_commands.py` — `auth_disable_command`, `auth_enable_command`, updated `auth_list_command` with `[DISABLED]` marker, interactive helpers
- `hermes_cli/main.py` — subparser registration for disable/enable

## Behavior
- Default `disabled=False` for backward compatibility with existing `auth.json`
- All rotation strategies (`fill_first`, `round_robin`, `least_used`, `random`) skip disabled entries automatically via `_available_entries()`
- Uses existing `resolve_target()` for index/ID/label lookup (consistent with `remove`)
- Interactive menu shows disabled entries for disable action, only disabled for enable action

## CLI Usage
```
hermes auth disable <provider> [target]  # target = index|id|label
hermes auth enable <provider> [target]
hermes auth list  # shows [DISABLED] marker
hermes auth       # interactive menu options 3 & 4
```

## Implementation Commit
`9f82d59be` on branch `feat/auth-disable-enable` (in `/root/hermes-agent-pr`)

## Status
- Local implementation complete, syntax checks pass
- Cannot push to upstream (no write access to NousResearch/hermes-agent)
- User must fork repo, apply changes, and open PR

## Use Case
Particularly useful for Codex OAuth accounts:
- When one Codex account hits rate limits but another is available
- User can disable the rate-limited account instead of removing it
- Re-enable later after quota resets
- Avoids losing OAuth tokens / re-authenticating