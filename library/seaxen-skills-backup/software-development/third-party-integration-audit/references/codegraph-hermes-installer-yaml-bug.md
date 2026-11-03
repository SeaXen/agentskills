# CodeGraph Hermes installer YAML bug

## Context
While auditing CodeGraph installation into Hermes, the installer reported success and added the expected MCP server block, but Hermes then behaved as if no MCP servers were configured.

## Verified failure mode
CodeGraph v0.9.4's Hermes installer inserted `mcp-codegraph` into `platform_toolsets.cli` with broken YAML indentation.

Broken shape observed:

```yaml
platform_toolsets:
  cli:
    - mcp-codegraph
  - hermes-cli
  discord:
  - hermes-discord
```

That made `config.yaml` unparsable. Hermes then fell back to default config, which masked the install as a runtime/config problem instead of a plain syntax error.

## Symptoms
- `hermes config check` warns that `config.yaml` failed to parse and says Hermes is falling back to defaults
- `hermes mcp list` shows no configured servers or misses the new server
- feature appears "installed" on disk but inert at runtime

## Verification pattern
1. Back up `config.yaml` before running a third-party installer that edits Hermes config.
2. After install, parse the file directly with YAML parser.
3. Run `hermes mcp list`.
4. If Hermes claims no servers or default behavior, inspect recent diff around `mcp_servers` and `platform_toolsets`.

Minimal parser check:

```bash
python3 - <<'PY'
import yaml, pathlib
p = pathlib.Path('/mnt/tb/hermes/config.yaml')
yaml.safe_load(p.read_text())
print('YAML OK')
PY
```

## Manual repair used
Correct the indentation so list items stay under each key.

Repaired shape:

```yaml
platform_toolsets:
  cli:
    - mcp-codegraph
    - hermes-cli
  discord:
    - hermes-discord
  homeassistant:
    - hermes-homeassistant
```

After repair, re-run:

```bash
hermes mcp list
```

Expected result: `codegraph` appears enabled.

## Durable lesson
For Hermes integrations, installer success is not enough. If a tool edited `config.yaml`, always verify both:
- parser-level validity
- live Hermes feature visibility (`hermes mcp list`, `hermes config check`, or equivalent)
