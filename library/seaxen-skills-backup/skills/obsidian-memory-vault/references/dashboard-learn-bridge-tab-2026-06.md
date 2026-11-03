# Dashboard Learn-bridge tab (2026-06)

## UI

- Header tab: **Learn** (`data-page="learn-bridge"`), between Review and Capture.
- Panels: stat grid (skill version, stale vs context, tag budget, weekly cron), three layers table, canonical vault files (click → `openNoteByPath`), umbrella skill block, vault↔skill matrix, `/learn` prompts (click pre to copy), maintenance (5-tag, Capture triage, cron).

## API

```bash
curl -sS 'http://127.0.0.1:6065/api/learn-bridge' | python3 -m json.tool
```

Returns `learn-bridge-v1`: `skill`, `canonical` (per-path mtime), `skill_stale_vs_context`, `matrix`, `learn_prompts`, `weekly_cron`, `tag_budget`.

Backend: `learn_bridge_status()` in `obsidian_dashboard.py`.

## Deploy

After editing embedded HTML/JS or Python:

```bash
python3 -m py_compile /mnt/tb/hermes/obsidian_dashboard.py
systemctl --user restart obsidian-vault-dashboard
sleep 2
curl -sS http://127.0.0.1:6065/ | grep -c 'learn-bridge'
curl -sS http://127.0.0.1:6065/api/learn-bridge | python3 -c "import sys,json; d=json.load(sys.stdin); print(d['mode'], len(d.get('matrix',[])))"
```

## Ad-hoc verify

Run skill script: `scripts/verify_dashboard_learn_tab.py` (or equivalent under `/tmp/hermes-verify-learn-bridge-tab.py`).

## Related

- Umbrella skill: `obsidian-vault-learn-bridge`
- Home capture button: `references/vault-capture-inbox-and-survival-2026-06.md`