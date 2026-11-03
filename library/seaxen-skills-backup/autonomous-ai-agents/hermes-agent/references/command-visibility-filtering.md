# Hermes Slash Command Visibility Filtering

When a user reports "command X doesn't show in my command line / autocomplete / picker", the issue is almost always one of the three visibility flags on `CommandDef` in `hermes_cli/commands.py`.

## The Three Flags

| Flag | Effect |
|------|--------|
| `cli_only=True` | Command works in CLI and TUI but NOT in gateway (Telegram/Discord/Slack command menus) |
| `gateway_only=True` | Command works in gateway surfaces but NOT in CLI autocomplete or TUI catalog |
| `gateway_config_gate="some.config.key"` | When set on a `cli_only` command, the command appears in gateway surfaces only when that config value is truthy |

There is also `_TUI_HIDDEN` in `tui_gateway/server.py` — a frozenset of command names hardcoded to be excluded from the TUI catalog regardless of other flags.

## Where Each Surface Gets Its Command List

### CLI Autocomplete (`hermes chat`, prompt_toolkit)
- Source: `COMMANDS` dict in `hermes_cli/commands.py` (line 252)
- Filter: excludes `gateway_only=True` commands only
- `cli_only=True` commands ARE included
- Also filtered by `_command_available()` which only special-cases `/fast`

### TUI Catalog (`hermes --tui`, Ink/React UI)
- Source: `commands.catalog` RPC in `tui_gateway/server.py` (line 4406)
- Filter: excludes `_TUI_HIDDEN` and `gateway_only=True` commands
- `cli_only=True` commands ARE included in the catalog
- TUI has its OWN execution registry (`SLASH_COMMANDS` in `ui-tui/src/app/slash/registry.ts`) — commands not in this registry fall through to `slash.exec` → `_SlashWorker` → CLI's `process_command()`

### Gateway Command Menus (Telegram bot menu, Discord slash commands)
- Source: `_is_gateway_available()` in `hermes_cli/commands.py` (line 400)
- Filter: returns `False` for `cli_only=True` commands UNLESS they have a `gateway_config_gate` that is truthy
- This is why `cli_only` commands don't appear in Telegram's `/` menu or Discord's slash picker

### Help Output (`/help` in CLI)
- Source: `COMMANDS_BY_CATEGORY` dict (line 260)
- Filter: excludes `gateway_only=True` only (same as CLI autocomplete)
- Further filtered by `_command_available()` per command

## Debugging Checklist

1. Check `CommandDef` for the command in `hermes_cli/commands.py`:
   - `cli_only=True` → won't appear in gateway menus (expected)
   - `gateway_only=True` → won't appear in CLI/TUI (expected)
   - `_TUI_HIDDEN` in `tui_gateway/server.py` → won't appear in TUI (expected)

2. If the command should appear in a surface but doesn't:
   - CLI: verify it's in `COMMANDS` dict (not `gateway_only`)
   - TUI: verify it's not in `_TUI_HIDDEN` and not `gateway_only`
   - Gateway: verify `_is_gateway_available()` returns True (needs `cli_only=False` or a truthy `gateway_config_gate`)

3. If the command appears in autocomplete but doesn't execute:
   - TUI: check if it's in the TUI's own `SLASH_COMMANDS` registry; if not, it falls through to CLI worker
   - CLI: check `process_command()` has a handler for the canonical name

## Current cli_only Commands (v0.14.0)

`/clear`, `/redraw`, `/history`, `/save`, `/handoff`, `/snapshot`, `/config`, `/gquota`, `/statusbar`, `/verbose`, `/skin`, `/indicator`, `/busy`, `/tools`, `/toolsets`, `/skills`, `/cron`, `/reload`, `/browser`, `/plugins`, `/platforms`, `/copy`, `/paste`, `/image`, `/quit`

## Current gateway_only Commands (v0.14.0)

`/topic`, `/restart`, `/platform`

## Current _TUI_HIDDEN Commands (v0.14.0)

`/sethome`, `/set-home`, `/update`, `/commands`, `/approve`, `/deny`
