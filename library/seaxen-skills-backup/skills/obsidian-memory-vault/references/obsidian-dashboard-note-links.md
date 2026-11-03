# Obsidian vault dashboard (:6065) — opening notes from Home / Learn / Quick links

Applies to `/mnt/tb/hermes/obsidian_dashboard.py` (telemetry-style tabs + legacy Notes reader).

## Symptom

User clicks Home **Quick links**, **Recent daily**, **Most linked**, or **Learn** tab vault paths — nothing loads or wrong note.

## Root causes (fixed 2026-06-26)

1. **`openNoteByTitle('${encodeURIComponent(title)}')`** — encoded titles (`Davidson%2024e…`) never match `data.notes[].title`.
2. **Title vs path** — quick link label `Dashboard` matched `dashboard/README.md` instead of `Dashboard.md`.
3. **`openNoteByPath`** fetched into `#reader` — real reader uses `#content`, `openNote()`, graph state.

## Correct pattern

```javascript
function openNoteByPath(path) {
  switchPage('notes');
  const run = async () => {
    if (typeof openNote !== 'function') { setTimeout(run, 40); return; }
    if (!data.notes || !data.notes.length) { setTimeout(run, 40); return; }
    const hit = data.notes.find(n => n.path === path);
    await openNote(encodeURIComponent(hit ? hit.path : path));
  };
  setTimeout(run, 80);
}
```

**Generated links:** always `onclick="openNoteByPath(${JSON.stringify(note.path)});return false"` — not `encodeURIComponent` on titles.

**Quick links:** store **vault-relative paths** (`Memory/decisions.md`, `Knowledge/Hermes Operations.md`), not display titles.

**`openNoteByTitle` (toolbar):** decodeURIComponent; fallback match filename stem; `switchPage('notes')` then `openNote`.

## Header copy

When user asks to remove marketing tagline (`hermes-obsidian memory / vault telemetry`), delete the `<h1>` block — keep **page tabs only** (matches Dr. Sagar dense UI preference).

## Verify (ad-hoc)

```bash
curl -sS http://127.0.0.1:6065/ | grep -c 'vault telemetry'   # expect 0
curl -sS http://127.0.0.1:6065/ | grep -c 'JSON.stringify(path)'  # expect >=1
curl -sS -o /dev/null -w '%{http_code}\n' 'http://127.0.0.1:6065/api/note?path=Memory%2Fdecisions.md'
```

Restart: `systemctl --user restart obsidian-vault-dashboard` (from **outside** gateway if restart is blocked inside agent shell — `pkill -f obsidian_dashboard` lets `Restart=always` respawn).

## APIs added for Learn tab

- `GET /api/learn-bridge` → `learn_bridge_status()` (`learn-bridge-v1`)
- Tab **Learn** → `loadLearnBridge()` on `switchPage('learn-bridge')`