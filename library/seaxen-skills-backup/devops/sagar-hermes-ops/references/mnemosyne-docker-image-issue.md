# Mnemosyne Docker Image Issue

## Finding (June 9, 2026)
The Mnemosyne (AxDSan/mnemosyne) GHCR image `ghcr.io/axdsan/mnemosyne-mcp:latest` is **private/denied** — `docker pull` fails with `Error response from daemon: error from registry: denied`.

## Implications
- Mnemosyne is primarily a **Python package** (`mnemosyne-memory` on PyPI), not a prebuilt Docker image
- The local `/root/.hermes/vendor/mnemosyne/` contains source to build from (has `docker-compose.yml` with `build: .`)
- The Docker Compose file expects to build locally, not pull a prebuilt image

## Local Source Structure
```
/root/.hermes/vendor/mnemosyne/
├── docker-compose.yml  # builds from . (local source)
└── ... (MCP server source)
```

## Update/Install Path
**Option 1: Build from local source**
```bash
cd /root/.hermes/vendor/mnemosyne
docker compose build --pull --no-cache
docker compose up -d
```
- Runs on port 8080 (per docker-compose.yml)
- Uses local source as build context

**Option 2: Install Python package directly**
```bash
pip install --upgrade mnemosyne-memory
mnemosyne-mcp --transport sse --host 0.0.0.0 --port 8080
```
- This is the primary distribution method per GitHub repo
- MCP server runs via CLI entry point

## Key Distinction
- **Mnemosyne core** = Python SDK (`pip install mnemosyne-memory`)
- **MCP server** = `mnemosyne-mcp` command from the package
- **Dashboard** = separate `mnemosyne-dashboard` (port 8765 default)
- **Docker image** = not publicly available on GHCR

## For Hermes Integration
- Hermes uses Mnemosyne via native plugin + MCP
- Prefer Python package upgrade over Docker image
- Verify all three version surfaces after upgrade:
  1. venv package/import version
  2. Plugin metadata in `~/.hermes/plugins/mnemosyne/plugin.yaml`
  3. Live runtime version (fresh process probe)