# Hermes dangerous-command approval mapping

Use this when the user asks what the approval buttons mean, where `Always Allow` is stored, or how to revoke it.

## Durable mapping
- `Allow Once` → approve only this single command invocation.
- `Allow Session` → ephemeral in-memory approval for the current Hermes process/session.
- `Always Allow` → persistent entry in `command_allowlist` inside `~/.hermes/config.yaml`.
- `Deny` → reject the request.

## Where to inspect
- Config file: `~/.hermes/config.yaml`
- Key: `command_allowlist`

Typical live state check:
```bash
python3 - <<'PY'
import yaml, json, pathlib
p = pathlib.Path('~/.hermes/config.yaml').expanduser()
cfg = yaml.safe_load(p.read_text()) or {}
print(json.dumps(cfg.get('command_allowlist', []), indent=2))
PY
```

## Operational rule
If the user wants to revoke `Always Allow`:
1. Edit or clear `command_allowlist`.
2. Restart Hermes / gateway or start a fresh session.

Reason: the permanent allowlist is loaded into memory at startup, so deleting the config entry alone may not change behavior in an already-running process.

## Answer shape
Lead with the mapping first, then the file/key, then the restart caveat.
Avoid hand-wavy phrasing like "it probably saves somewhere in config" — name `command_allowlist` explicitly.
