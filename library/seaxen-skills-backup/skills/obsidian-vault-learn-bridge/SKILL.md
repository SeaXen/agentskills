---
name: obsidian-vault-learn-bridge
description: "Umbrella workflow linking Dr. Sagar's Obsidian vault to Hermes skills and /learn: session start, recall verify, skill refresh from canonical vault notes, no noisy duplication."
version: 1.2.4
author: Hermes Agent
license: MIT
metadata:
  hermes:
    tags: [obsidian, learn, skills, recall, vault]
    related_skills: [obsidian-memory-vault, obsidian, hermes-agent, sagar-hermes-ops]
---

# Obsidian Vault ↔ Learn Bridge

## When to use

- User asks about vault + `/learn`, skill refresh from Obsidian, or "perfect" memory setup.
- Starting any task that should use vault context (MedSea, Hermes ops, dashboard recall).
- After changing canonical vault notes — refresh this skill or child skills.

Vault path (spelling): `/mnt/tb/hermes/obsedianvault`  
vault: Knowledge/Hermes Vault and Learn Bridge.md

After major ops (Mnemosyne upgrade, third-party eval): write **facts** to vault Knowledge + `decisions.md` / `issues-fixes-log.md`; keep **procedures** in skills (`sagar-hermes-ops`, `obsidian-memory-vault` references). See `obsidian-memory-vault` → `references/vault-audit-sessions-and-mnemosyne.md`.
Dashboard: `http://127.0.0.1:6065` — recall uses `?query=`

## Three layers (do not confuse)

1. **Vault** — durable facts, wikilinks, daily high-signal.
2. **Mnemosyne / MEMORY.md** — hot agent memory; cross-link durable writes to vault.
3. **Skills** — procedures; load `obsidian-memory-vault` for write/routing detail.

## Capture & survival (CyrilXBT pattern)

- **Single inbox:** `Inbox/Capture.md` — append one line per item; **no** folder/tag decisions at capture.
- **Tag budget:** max **5** active tags (`#project` `#knowledge` `#decision` `#daily` `#inbox`). New tags only after one line in `Knowledge Index`.
- **Weekly triage (~5 min):** each Sunday (with `obsidian-vault-weekly-health` or on user ask):
  1. Process [[Capture]] → `Work/` / `Knowledge/` / `Memory/decisions.md` / delete.
  2. Dashboard review queue → target **pending 0** (reject scanner noise per `obsidian-memory-vault`).
  3. If stale/orphan notes are flagged, classify them before editing: **active project → keep in `Work/` and strengthen links/indexes; durable setup/reference → move to `Knowledge/`; dead note → archive/delete**.
  4. Re-run live health after cleanup. The weekly report can name stale `Work/*.md`, but the **actual remaining orphans may be different notes** (often missing daily-note index entries in `AGENT.md`).
  5. At most **one** structural vault change if the week failed — no full reorganize.
- Canonical: `Knowledge/Obsidian Survival Design.md`
- **Dashboard:** Home `:6065` → **Open Capture.md** (or Quick links **Capture**) → Notes reader for `Inbox/Capture.md` via `openCaptureInbox()`.
- **Dashboard Learn tab:** Header **Learn** — three layers, canonical note mtimes (click to open), `obsidian-vault-learn-bridge` version/stale vs `context.md`, vault↔skill matrix, click-to-copy `/learn` prompts, weekly triage shortcuts. Data: `GET /api/learn-bridge` (`learn-bridge-v1`). Lazy-load on tab switch (`loadLearnBridge()`).
- **Dashboard themes:** Header **Theme** → **Classic** (default) or **Premium** (CSS-only polish). Persists in browser. Detail: `obsidian-memory-vault` → `references/dashboard-dual-theme-2026-06.md`.
- **Dashboard perf:** `scan_notes` cache, parallel `loadAll`, pause graph sim off Notes/Graph — `references/dashboard-perf-scan-cache-2026-06.md`.

## Session start (mandatory for vault work)

1. `read_file` `/mnt/tb/hermes/obsedianvault/AGENT.md`
2. `read_file` `.../System/Assistant/context.md` and `preferences.md`
3. Today + yesterday `Daily/YYYY-MM-DD.md` if present
4. `search_files` with tight pattern; then `read_file` smallest relevant notes
5. Optional: `curl -sS 'http://127.0.0.1:6065/api/recall?query=ENCODED&limit=5'`

## `/learn` prompts (when slash command exists)

Run in Hermes chat (CLI/gateway/dashboard). Each should produce a tested `SKILL.md`:

```text
/learn file:/mnt/tb/hermes/obsedianvault/Knowledge/Hermes Vault and Learn Bridge.md
focus: session start, recall verify, skill↔vault matrix only
```

```text
/learn file:/mnt/tb/hermes/obsedianvault/AGENT.md
focus: routing table and session protocol — output skill agents load before vault edits
```

```text
/learn file:/mnt/tb/hermes/obsedianvault/Knowledge/Memory System Architecture.md
focus: hot vs warm vs cold, cross-link protocol, failure modes
```

MedSea / ops: point `/learn` at `Work/` project note or existing `medsea-chapter-audit` SKILL.md — do not duplicate MedSea content here.

## Without `/learn` on CLI (current host)

This install may lack `hermes learn` subcommand. Equivalent:

- Patch umbrella: `skill_manage(action='patch', name='obsidian-vault-learn-bridge', ...)`
- Re-read canonical vault files and update `obsidian-memory-vault` when routing/recall rules change
- Vault note `Knowledge/Hermes Vault and Learn Bridge.md` stays the human-readable map

## Skill refresh matrix

| Vault canonical | Action |
|-----------------|--------|
| `Memory System Architecture.md` | Patch `obsidian-memory-vault` cross-link section if layers change |
| `Hermes Operations.md` | Patch `sagar-hermes-ops` or bridge skill ports/verify |
| `AGENT.md` Daily index | After new `Daily/YYYY-MM-DD.md`, add `[[date]]` to index same turn |
| Recall ranking changes | Document in `issues-fixes-log`; run recall-eval + 3 live queries |
| Vault maintenance ("do best", refresh vault) | Follow `obsidian-memory-vault` → `references/vault-maintenance-and-review-queue.md`; run `scripts/flush_memory_review_noise.py` after edits |

## Verification (required before "done")

```bash
systemctl --user is-active obsidian-vault-dashboard
curl -sS 'http://127.0.0.1:6065/api/recall-eval'   # hit_at_k & mrr
curl -sS 'http://127.0.0.1:6065/api/memory-health'  # broken_links, orphans
curl -sS 'http://127.0.0.1:6065/api/recall?query=hermes%20dashboard%20port&limit=3'
curl -sS 'http://127.0.0.1:6065/api/recall?query=Say%20only%20OK.&limit=3'
```

Pass bar: eval MRR/hit@k at baseline; health orphans `[]`; noise query does not surface irrelevant daily spam.

## Write policy (bridge-specific)

- **Promote to skill:** repeatable checklists (deploy, recall verify, session start).
- **Keep in vault only:** dated decisions, one-off fixes, narrative, medical content.
- **Never:** `/learn` entire vault or raw Discord transcripts.

## Cron (maintenance)

- **Weekly:** `obsidian-vault-weekly-health` (`00c43f437829`) — Sundays 10:00, script `obsidian_vault_weekly_health.py`, `deliver: origin`. Reports eval, stale `Work/*.md`, bridge-skill staleness vs `context.md`.
- **4h watchdog:** `obsidian-dashboard-watchdog` — recall degradation, `deliver: local`.
- Nightly daily stub: `obsidian-nightly-high-signal-log` — unchanged.

## Pitfalls

- `?q=` on recall API returns empty — always `?query=`
- Restart dashboard via systemd after Python edits — not bare `python3` on :6065
- **Home / Learn links dead on click:** use `openNoteByPath(JSON.stringify(path))` + real `openNote()` — see `obsidian-memory-vault` → `references/obsidian-dashboard-note-links.md`
- **Quick links:** bind **paths** (`Dashboard.md`, `Knowledge/…`) not URL-encoded titles; `encodeURIComponent` in `openNoteByTitle` breaks spaces/`&`
- User may ask to **remove header tagline** — tabs-only header; no `hermes-obsidian … vault telemetry` `<h1>`
- "Improve Obsidian not via Mnemosyne" means method scope — do not delete Mnemosyne mirror without explicit user ask
- Vault edits spawn memory-review false positives — flush queue before claiming health 10/10 (`obsidian-memory-vault` pitfall 40)