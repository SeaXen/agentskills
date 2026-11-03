# Core App Port Moves and Graphify Serving Conventions

## Durable conventions from live ops

- Primary Graphify instance: `6080`
- Additional Graphify instances: `6082`, `6083`, and upward

## What must be changed for SeaDash core apps

Changing the visible dashboard link is **not** a one-file edit.

Patch all of these:

1. `index.html` `APPS_CORE`
2. `index.html` runtime `state.core` / initial core array
3. `server.py` `CORE_APPS`

If you change only one of them, the UI and API can disagree and the dashboard may show stale ports.

## What must be changed for Graphify serving

Graphify itself generates static output in:

- `graphify-out/graph.html`
- `graphify-out/graph.json`
- `graphify-out/GRAPH_REPORT.md`

Serving Graphify on a port requires a separate HTTP server rooted at `graphify-out/`.

Typical temporary serve pattern:

```bash
cd /path/to/folder/graphify-out
python3 -m http.server 6080
```

The URL path usually stays:

- `/graph.html`

Changing the dashboard link to a new port does nothing unless:

1. `graphify-out/graph.html` exists
2. something is actually listening on that port
3. that port is serving the correct `graphify-out/` folder

## Verification checklist

After any port move:

```bash
curl -I http://127.0.0.1:6080/graph.html
```

Confirm:

- new ports return `200`
- old ports are closed unless intentionally kept
- SeaDash content/API show the new ports

## Common pitfall

If a service is supervised by systemd, killing the process alone is not enough. The unit may respawn it on the old port. Update the unit file, reload, and restart the service.
