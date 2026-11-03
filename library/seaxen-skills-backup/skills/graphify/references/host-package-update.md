# Graphify — host CLI + Hermes skill update

## This host (Dr. Sagar / DietPi)

| Item | Value |
|------|--------|
| Git clone | `/mnt/tb/1Apps/graphify` |
| Track branch | `v8` |
| PyPI name | `graphifyy` |
| CLI install | `uv tool` → `/root/.local/bin/graphify` |
| Hermes skill | `~/.hermes/skills/graphify/` (via `graphify install --platform hermes`) |

## Update sequence

```bash
cd /mnt/tb/1Apps/graphify
git fetch origin
git pull --ff-only origin v8

# PEP 668: do NOT use bare `pip install` on system Python
uv tool install -e /mnt/tb/1Apps/graphify --force

graphify --version
graphify install --platform hermes
```

## Version mismatch warning

After upgrading the package, the CLI may warn:

> skill is from graphify X.Y.Z, package is A.B.C. Run 'graphify install' to update.

Always run `graphify install --platform hermes` (or the user’s platform) so `SKILL.md` and `references/` match the installed package.

## Optional

- Re-run `/graphify <path> --update` on large repos to pick up new extractors without a full rebuild.
- `graphify-mcp` is installed alongside `graphify` when using `uv tool install`.