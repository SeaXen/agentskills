# Dashboard review scanner + quality-gate (2026-06-25)

## Problem

Recall can be 10/10 while **quality-gate** fails on `review_queue` only. The
memory-review scanner treats keyword hits in bridge notes, daily logs, and
markdown tables as durable "decision/fix" candidates. Symptom: `review_flow`
94, health 98.8, recommendation "Review N memory candidates".

## Fix pattern (code)

In `obsidian_dashboard.py`:

1. Expand `MEMORY_REVIEW_SKIP_PATHS` for canonical/meta notes:
   - `AGENT.md`, `Memory/decisions.md`, `System/Assistant/issues-fixes-log.md`,
     `System/Assistant/preferences.md`, `Knowledge/Hermes Vault and Learn Bridge.md`

2. Add `_memory_review_line_is_noise(path, clean, low)` and call it inside
   `generate_memory_review_candidates` before classifying:
   - Table rows (`|`, `|---`)
   - Daily log lines (`HH:MM —`), `[[decisions]]:` bullets
   - Acceptance boilerplate (`hand-picked` + `recall`, `read system/assistant`)
   - Bridge map lines (`vault = source of truth` + `skills`)

3. **Git sync gate:** After reading `obsmemory-sync-state.json`, enrich from live
   git when `@{u}..HEAD` count is 0 — set `last_sync_utc` from `git log -1 --format=%cI`
   so manual pushes do not leave quality-gate showing stale sync dates.

Restart: `systemctl --user restart obsidian-vault-dashboard` (same inode as
`/root/.hermes/obsidian_dashboard.py` on this host).

## Ops (same session)

- Append real decisions to `Memory/decisions.md` manually; reject scanner hits
  via `POST /api/memory-review` with `status: rejected` or
  `scripts/flush_memory_review_noise.py`.

## Acceptance

```bash
curl -s http://127.0.0.1:6065/api/quality-gate | python3 -c "
import json,sys; d=json.load(sys.stdin)
assert d['ready'] and d['score']==10.0, d
assert not d['blockers'], d
print('OK')
"
curl -s http://127.0.0.1:6065/api/memory-health  # pending 0, overall 100
```

## Weekly fleet report

Script: `/root/.hermes/scripts/obsidian_vault_weekly_health.py`  
Cron: `obsidian-vault-weekly-health` — `0 10 * * 0`, `no_agent: true`, deliver `origin`.

Complements 4h `obsidian-dashboard-watchdog` (degradation only, `deliver: local`).