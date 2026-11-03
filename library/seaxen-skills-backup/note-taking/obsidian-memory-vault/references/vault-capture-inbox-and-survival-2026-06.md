# Vault capture inbox, survival design, and external KB (2026-06)

## Capture inbox (`Inbox/Capture.md`)

- **Zero-friction capture:** append one bullet per item; no folder/tag/type at capture time.
- **Processing:** weekly triage or on user ask → `Work/`, `Knowledge/`, `Memory/decisions.md`, or **delete** (permission to delete is explicit).
- **Canonical:** `Knowledge/Obsidian Survival Design.md` (CyrilXBT week-2 survival patterns adapted for agent-operated vault).
- **Tag budget:** max 5 — `#project` `#knowledge` `#decision` `#daily` `#inbox`; new tags only after `Knowledge Index` line.

## Dashboard one-click (Home :6065)

After `obsidian_dashboard.py` edits:

- Home panel: **Open Capture.md** → `openCaptureInbox()` → `openNoteByPath('Inbox/Capture.md')` (Notes tab + reader).
- Quick links grid: highlighted **Capture** card (same handler).
- `homeCaptureMeta` counts unprocessed bullets under `## Captures` via `/api/note-content?path=Inbox/Capture.md` (split on `/\n/`, not literal `\\n`).
- Verify: `curl -s http://127.0.0.1:6065/ | grep -E 'Open Capture.md|openCaptureInbox'` then `systemctl --user restart obsidian-vault-dashboard`.

## External KB vs memory vault (Yan / llm-wiki)

- **Do not** merge Yan-style 1,100-file auto-wiki into `obsedianvault` — hurts low-noise recall on curated vault.
- **Optional:** separate `WIKI_PATH` (e.g. `/mnt/tb/hermes/research-wiki`) + skill `llm-wiki` for papers/URLs only.
- **Canonical note:** `Knowledge/External KB Patterns.md`.

## Weekly automation

- `~/.hermes/scripts/obsidian_vault_weekly_health.py` — reports eval, stale `Work/*.md`, **Capture line count**, bridge-skill vs `context.md` mtime.
- Cron: `obsidian-vault-weekly-health` Sundays 10:00, `no_agent: true`, `deliver: origin`.

## Bridge skill

Load `obsidian-vault-learn-bridge` for session start, `/learn` prompts, and weekly triage checklist.