---
name: obsidian-memory-vault
description: "Use when working with Dr. Sagar's Hermes Obsidian memory vault: recall context, write high-signal daily logs, maintain decisions/issues, and avoid noisy chat dumps."
version: 1.4.6
author: Hermes Agent
license: MIT
metadata:
  hermes:
    tags: [obsidian, memory, vault, daily-notes, recall]
    related_skills: [obsidian, hermes-agent]
---

# Obsidian Memory Vault

## Overview

This skill governs Dr. Sagar's Hermes + Obsidian memory system.

Reference: `references/vault-capture-inbox-and-survival-2026-06.md` — `Inbox/Capture.md`, 5-tag rule, Cyril survival note, Yan vs curated vault (`External KB Patterns`), dashboard **Open Capture.md** on Home :6065, weekly health script capture count.

Reference: `references/dashboard-learn-bridge-tab-2026-06.md` — **Learn** tab on :6065, `GET /api/learn-bridge`, matrix + `/learn` copy prompts + skill staleness; verify with `scripts/verify_dashboard_learn_tab.py`.

Reference: `references/dashboard-perf-scan-cache-2026-06.md` — server `scan_notes` mtime cache, client graph sim pause off Notes/Graph, parallel deduped `loadAll`; honest ~33MB RSS idle.

Reference: `references/dashboard-dual-theme-2026-06.md` — header **Theme** select **Classic** | **Premium** (`obsmemory.dashboard.theme.v1`); premium is CSS-only polish on same pages.

Reference: `references/dashboard-review-scanner-and-quality-gate-2026-06-25.md` — when health is 98–99 with recall 100 but **quality-gate** fails on `review_queue`: expand `MEMORY_REVIEW_SKIP_PATHS`, add `_memory_review_line_is_noise()`, reject false positives, enrich git sync from live `git` head; accept with `/api/quality-gate` `ready: true` score 10.

Reference: `references/vault-maintenance-and-review-queue.md` — when the user asks to improve/update the vault without folder sprawl: refresh `context.md`, clear review-queue false positives (`scripts/flush_memory_review_noise.py`), one `Work/*.md` per active project.

Reference: `references/vault-audit-sessions-and-mnemosyne.md` — when the user asks \"anything to add to the vault?\": cross-check `session_search` + `mnemosyne_recall` against canonicals; supersede stale `decisions.md` entries instead of leaving contradictions; route Mnemosyne upgrade facts to `Knowledge/Mnemosyne Operations.md` (procedural detail stays in `sagar-hermes-ops`). Ad-hoc post-audit check: `python3` on skill path `scripts/vault-audit-verify.py`.

Reference: `references/vault-knowledge-note-verify.md` — ad-hoc checks after adding `Knowledge/*.md` (recall API, samefile, daily log when user says learn/add).

Reference: `references/dashboard-redesign-phases.md` — phased workflow for dashboard redesigns: audit the live UI first, back up before each phase, implement in narrow passes, then verify syntax, service, APIs, and browser-visible results after every pass.

The vault is the warm/cold memory layer. It is not a dumping ground. Use it to preserve durable project context, decisions, technical fixes, medical knowledge, and WordPress pipeline state without bloating Hermes hot memory.

Vault path:

```text
/mnt/tb/hermes/obsedianvault
```

Important spelling: the directory is `obsedianvault`, not `obsidianvault`.

Primary entry point:

```text
/mnt/tb/hermes/obsedianvault/AGENT.md
```

Vault ↔ skills ↔ `/learn` umbrella (load first for repeatable ops):

```text
skill: obsidian-vault-learn-bridge
vault: Knowledge/Hermes Vault and Learn Bridge.md
```

Web dashboard:

```text
http://<server-ip>:6065/
```

## When to Use

Use this skill when:

- The user asks about Hermes memory, Obsidian, vault, dashboard, graph, recall, daily notes, decisions, or logs.
- The user asks about old work that may exist in vault notes.
- You need project context for mdsagar.com, medical study workflow, Hermes operations, or vault setup.
- A session produced a durable result worth preserving.
- You are about to ask the user to repeat context that may already be in the vault.

Do not use this for trivial one-off answers that do not need persistent context.

## Scope interpretation — "improve X, not via Y" means method, not deletion

When the user phrases a request as "improve X, if need not [via] Y" or "make X stronger without going through Y", the default reading is **scope of method, not scope of existence**. They mean: the *work* should not use Y as a dependency. They do NOT mean: remove Y. The cheaper mistake is to over-read and start deleting working integrations (mirror crons, vault files, routes, skill instructions) — that is expensive to undo and breaks whatever else depends on Y.

Practical rule:

1. If the request is ambiguous, ask **one** precise clarifying question before touching any working integration. Example: "Do you want me to (A) keep Mnemosyne running and just stop Obsidian from depending on it, or (B) fully detach Mnemosyne from the picture?"
2. If you default to the narrower reading, leave Y in place. The cost of leaving Y untouched is zero; the cost of restoring Y after the user said "no, keep it" is high.
3. If you do remove something, do it in a single easy-to-revert batch and surface it explicitly in your next message. Don't drip-destroy across multiple turns.

Real example from 2026-06-17: user said "I want improve obsidian memory if need not mnemosync" and the first interpretation shipped deleted the Mnemosyne mirror cron, the mirror files, the `query_mnemosyne_recall()` function, the unified-recall route, and added 3 Mnemosyne-file entries to `MEMORY_REVIEW_SKIP_PATHS`. The user immediately corrected: "Obsidian improvements only, don't touch Mnemosyne at all keep it as it with obsidian." All deletions had to be reverted manually.

## Recall Feedback — Make It Actually Used

The dashboard exposes `POST /api/recall-feedback` and ranking already consumes
`get_recall_feedback_adjustments()` from the `recall_feedback` table. The
`obsidian-auto-recall` plugin exports `submit_recall_feedback(vote, query, result)`.

**Rule:** whenever `/api/recall` (or the plugin) surfaces vault notes into a turn
and you can judge whether a specific result was **useful** (`up`) or **wrong /
irrelevant** (`down`), submit exactly one feedback row per result that
influenced the answer.

```python
from hermes_plugins.obsidian_auto_recall import submit_recall_feedback
submit_recall_feedback("up",   user_query, result)   # helped
submit_recall_feedback("down", user_query, result)   # misled
```

Submission is best-effort, never blocks the turn, and silently no-ops on
network failure. The signal compounds: the next time the same query shape
fires, `get_recall_feedback_adjustments()` nudges ranking, which makes the
right canonical surface faster.

A query is **probably useful** if it was the top hit AND its content
contributed to the answer. A query is **probably wrong** if the result was
off-topic, stale, or contradicted by a higher-ranked result that you actually
used.

## Session Start / Recall Protocol

When vault context may matter:

1. Read `AGENT.md`.
2. Read `System/Assistant/context.md`.
3. Read `System/Assistant/preferences.md`.
4. If debugging or setup-related, read `System/Assistant/environment.md` and `System/Assistant/issues-fixes-log.md`.
5. If project-specific, search `Work/` and `Knowledge/` for relevant notes.
6. If asking about recent events, read today's and yesterday's notes under `Daily/` if they exist.

Use `search_files` first for broad recall, then `read_file` for the smallest relevant notes. Do not load the whole vault.

## Write Policy — Strict Low Noise

Only write to the vault when there is durable value.

For historical backfill, use the selective import protocol in `references/selective-past-session-import.md`: search past sessions by topic cluster, import only durable items into `Daily/YYYY-MM-DD.md` by original session date, prefix imported bullets with `Imported —`, update aggregate notes, then verify dashboard/search counts.

Save:

- verified decisions
- verified fixes and root causes
- research conclusions
- project state changes
- reusable medical knowledge
- WordPress publishing pipeline changes
- environment/config changes that will matter later

Skip:

- generic chat summaries
- transient TODOs
- raw tool output
- failed guesses without a useful lesson
- full conversation dumps
- stale artifact IDs that will not matter in a week

## File Routing

| Content | File / Folder |
|---|---|
| Daily high-signal timeline | `Daily/YYYY-MM-DD.md` |
| Durable decisions | `Memory/decisions.md` |
| Technical fixes / root causes | `System/Assistant/issues-fixes-log.md` |
| Current operating state | `System/Assistant/context.md` |
| Stable preferences | `System/Assistant/preferences.md` |
| Project state | `Work/<project>.md` |
| Reusable knowledge | `Knowledge/<topic>.md` |
| Unclassified incoming | `Inbox/Capture.md` (append-only); promote on triage |

## Daily Note Format

Use this format:

```markdown
# YYYY-MM-DD

#daily

## Focus
- ...

## Log
- HH:MM — high-signal event with [[links]]

## Decisions
- [[decisions]]: short decision title

## Fixes
- [[issues-fixes-log]]: short fix title

## Next
- durable next action only if still relevant
```

Daily notes are append-only unless fixing obvious errors.

## Decision Entry Format

Append to `Memory/decisions.md`:

```markdown
### YYYY-MM-DD — Title
- **Decision:**
- **Reason:**
- **Alternatives rejected:**
- **Status:** active/superseded/done
- **Outcome:**
- **Links:** [[related note]]
```

## Issue/Fix Entry Format

Append to `System/Assistant/issues-fixes-log.md`:

```markdown
### YYYY-MM-DD — Title
- **System:**
- **Issue:**
- **Root cause:**
- **Fix:**
- **Verified:**
- **Risk / follow-up:**
- **Links:** [[related note]]
```

## Nightly high-signal cron pattern

When the user wants a nightly **high-signal** Obsidian log but broad agentic recall is too quota-heavy, prefer a **hybrid cron**:

- use a small collector `script` to prefilter last-24h vault changes into compact candidate signals
- then let a cheap/available AI model read only minimal canonical files plus the collector output
- keep toolsets minimal (often just `file`)
- avoid broad `session_search` / wide vault browsing in the scheduled path unless truly necessary

**Write bias — choose explicitly and confirm with the user.** The default below is appropriate for **personal vaults where cadence matters**; for **shared work vaults** where every entry has a review cost, flip it.

- **Default (personal vault):** *always write a minimal daily stub.* Quiet days get a thin honest stub (Focus + Log derived only from collector evidence + recent session titles). The point is cadence, not perfection. A thin honest stub beats no record. This is the policy for Dr. Sagar's vault.
- **Strict mode (work / shared vault):** *no write over weak write.* Skip the day if the collector shows nothing durable. Use this when false entries are costly to review.

When in doubt, ask the user which policy they want — don't silently ship strict mode on a personal vault, it will produce 10+ days of silence and the user won't notice until they check.

- See `references/hybrid-nightly-high-signal-cron.md` for the concrete pattern, including the **3-tier Bitwarden key loading fallback** (bws CLI → env var → .env file) and the two pitfalls that break naive implementations:
- `no_agent: false` cron jobs do **not** apply per-job `provider:` overrides — the runner falls back to the default config and fails with `No LLM provider configured`.
- `no_agent: true` script subprocesses do **not** get env vars injected — `OPENROUTER_API_KEY` will be empty and OpenRouter returns HTTP 401 `Missing Authentication header`. Detailed reproduction and fix: `references/hybrid-nightly-cron-pitfalls-2026-06.md`.
- `collect_sessions()` must skip non-dict entries in `sessions.json` (string `_README` key) or the nightly job crashes with `AttributeError` before OpenRouter — see Pitfall 4 in the same reference.
- See `references/hybrid-nightly-cron-pitfalls-2026-06-pitfall4.md` for **Pitfall 4 — free-tier OpenRouter models share a quota pool**: a 4-model fallback (1 paid + 3 free) still fails on tier-wide 429s because all free models share one bucket. Includes the paid-first/two-free/one-paid-last shape and the "RATE_LIMITED sentinel" recovery pattern.

**Multi-model fallback (2026-06 addition).** A single-model cron is at the mercy of one provider's quota. Use an ordered `OPENROUTER_MODELS` list (primary + 3 free-tier fallbacks from different model families), 2 attempts per model, 2/5/10s backoff, and **skip the rest of the model's attempts on HTTP 401/403/400** (same key will fail on every model — burning attempts is wasted). Pattern + working code in `references/hybrid-nightly-cron-pitfalls-2026-06.md` (Pitfall 3).

**Mnemosyne cross-link (2026-06 addition).** If the system also has a Mnemosyne hot-memory layer, see `references/mnemosyne-vault-crosslink-2026-06.md` for the full pattern: mirror script (idempotent, every 6h), unified recall endpoint, FTS5 join-aliasing pitfall, and the review-queue poisoning trap. The non-obvious lesson: **any new mirror / projection / architecture note must be added to `MEMORY_REVIEW_SKIP_PATHS`** in `obsidian_dashboard.py` or it will spam `/api/memory-candidates` with false positives (table rows classified as "decisions" and "fixes").

See `references/daily-note-bulk-backfill.md` for the safe pattern when backfilling N days of missing daily notes from `session_search` and `sessions.json` evidence (orphan-prevention via Daily Note Index, prefix convention, aggregate-note updates).

## Dashboard

Dashboard note:

```text
/mnt/tb/hermes/obsedianvault/Dashboard.md
```

Browser dashboard script:

```text
/mnt/tb/hermes/obsidian_dashboard.py
```

Port:

```text
6065
```

The browser dashboard is read-only at the UI layer and builds a graph from wikilinks, but it now also exposes a hybrid recall API used by Hermes integrations.

Recall architecture:

- `/api/recall` is the primary dashboard-side recall surface. It now accepts three additional query-string filters: `?since=YYYY-MM-DD&until=YYYY-MM-DD` (mtime window), `?tags=tag1,tag2` (require ALL of these tags, AND-match, case-insensitive), and per-result `source_kind` field (knowledge-canonical / work-canonical / memory-canonical / system-canonical / daily-note / mnemosyne-mirror / inbox-pending / imported / personal / other) for trust assessment.
- `/api/recall-unified` adds Mnemosyne results to `/api/recall` output. It tags Mnemosyne results with `source: "mnemosyne"` and `path: "mnemosyne://<table>/<id>"`. Use this when you want hot + warm in one shot.
- `/api/recall-eval` runs the curated eval and returns `summary.case_count`, `summary.hit_at_k`, `summary.mrr`. Curated 100/100 is necessary but not sufficient — always run a real-query stress test too.
- `/api/memory-health` returns the structural score (notes/links/orphans/broken/recall eval). 99.9/100 + empty `/api/recall?query=...` = the API is broken even though the dashboard looks green.
- It blends FTS/BM25, token overlap, trigram similarity, title overlap, graph-neighbor/folder/tag signals, recency, and feedback adjustments.
- When improving recall quality, prefer **incremental ranking patches** to `query_hybrid_recall()` over rewriting the whole recall path.
- For memory-critical intents like decisions, fixes, setup/config, and preferences, add small **intent-aware boosts/guardrails** so the canonical note families rank above generic but lexically-similar notes.
- Add **low-information query guardrails** so trivial prompts (for example `Say only OK.`) do not surface irrelevant recall.

- For nightly cron jobs needing a specific provider/model: use `no_agent: true` with a self-contained script that calls the LLM API directly. See `references/cron-no-agent-direct-api.md`.

Persistence pattern:

- Prefer a **user systemd service** over a loose background process when the user wants the dashboard to survive shell logout/reboot.
- Known service path: `/root/.config/systemd/user/obsidian-vault-dashboard.service`.
- Unit should run `/usr/bin/python3 /mnt/tb/hermes/obsidian_dashboard.py` with `OBSIDIAN_VAULT_PATH=/mnt/tb/hermes/obsedianvault` and `OBSIDIAN_DASHBOARD_PORT=6065`.
- Verify `systemctl --user is-enabled`, `systemctl --user is-active`, `loginctl show-user root -p Linger`, socket `:6065`, and `/api/graph`.
- For memory/recall readiness work, require live checks after restart: `/api/memory-health`, `/api/memory-candidates`, `/api/recall-eval`, a browser-rendered Memory Health panel, and representative `/api/recall` queries for **decision / fix / setup / preference / noise** cases.
  - **Critical gotcha:** `/api/recall` uses the query-string parameter `?query=`, not `?q=`. Wrong param returns `{"query": "", "mode": "idle", "results": []}` and looks like the API is broken when it isn't. Always test recall with the explicit `?query=` form during verification.
- After dashboard-side recall ranking changes, run an end-to-end fresh `hermes chat -Q` check for one targeted recall query and one noise query like `Say only OK.` to catch visible recall leakage.
  - A true 10/10 dashboard-side pass means: broken links `0`, orphans `0`, duplicate heading groups `0`, pending review candidates `0`, recall Hit@5 `1.0`, and MRR `1.0`.
  - **Strict gate:** `GET /api/quality-gate` must return `ready: true` and `score: 10.0` (nine gates including review queue, mnemosyne mirror cron, vault git sync). Use this when the user asks for dashboard "10/10" or "perfect" — not memory-health alone.
  - **Memory health score is necessary but not sufficient.** A 99.9/100 health score does NOT guarantee the live recall API returns useful results. Always run actual `/api/recall?query=<real question>` queries with real questions the user is likely to ask, and confirm the top hit is the right note. If only the health score is checked, you can ship a "perfect 10/10" dashboard that silently returns empty results to the user.
  - Do not count a review queue as processed until the persisted review state survives service restart / recall DB rebuild.
- When refreshing vault notes or fixing wikilinks, re-run `/api/graph` **after** the edits before writing counts into notes. Note/link totals can change immediately from the cleanup itself, so pre-edit counts become stale.
- For vault-health cleanup, verify `/api/memory-health` as well as `/api/graph` before updating state notes. A common pattern is: fix routing/link notes first, then re-check `broken_links`, `orphans`, and the remaining recommendation list.
- Folder-name wikilinks are not enough unless a real note title/stem exists. If you want `[[Imported]]` to resolve, create an actual canonical note such as `Knowledge/Imported/Imported.md`; a folder `README.md` alone may not satisfy the dashboard resolver.
- Verification artifacts should link by the **real note stem** the dashboard indexes, not a prettier guessed alias. Example durable pitfall: imported files like `knowledge_imported_verify-txt.md` and `obsidian_ingest_verify-txt.md` must be linked as `[[knowledge_imported_verify-txt]]` / `[[obsidian_ingest_verify-txt]]` or they still show up as orphans.
- For graph-polish work, see `references/graph-dashboard-force-layout.md` for the base bundle: animated force-layout, minimap, drag-to-pin nodes, browser-persistent saved positions, and label/collision improvements.
- For the next premium pass, see `references/graph-dashboard-advanced-polish.md` for focus-neighborhood mode, explicit pin/unpin UI, search-highlight pulse, preset layouts (`study/ops/memory/clean`), and zoom-based edge/label tuning.
- For the **cleanest pass** (type-ahead search input inside the graph area, fit-to-view button, clickable cluster labels with folder focus, cluster cohesion force, glassmorphism floating panel, faster alpha decay), see `references/graph-dashboard-cleanest-pass-2026-06.md`.
- See `references/dashboard-persistence-and-expanded-import.md` for the known-good unit and verification commands.
- See `references/local-document-ingestion-staging.md` for the low-risk local document → markdown → vault pattern using a dedicated converter venv and `Inbox/Imports/` staging.
- See `references/mnemosyne-vs-vault-architecture.md` for the crisp two-layer framing when the user asks "is the vault my true memory?" (vault = user truth, Mnemosyne = agent substrate, mirror is one-way).
- See `references/vault-dashboard-10-10-audit.md` for the live audit/rating pattern when the user asks whether the Obsidian vault/dashboard actually improves Hermes memory or deserves a 10/10 score. It covers file reality, service/API health, recall MRR/top-1 stress tests, review-queue pollution, cron-status contradictions, redaction, and the distinction between supporting vault memory and automatic hot memory.
- See `references/graph-dashboard-cleanest-pass-2026-06.md` for the **cleanest pass** (type-ahead search input inside the graph area, fit-to-view button, clickable cluster labels with folder focus, cluster cohesion force, glassmorphism floating panel, faster alpha decay).

## Dashboard Layout

The browser dashboard (`obsidian_dashboard.py`) uses a **2-panel layout**:

- **Left sidebar** (280px fixed): Notes list with search, folder/tag filters, saved searches. Always visible — no collapse toggle.
- **Right area** (flexible): Split vertically into:
  - **Graph canvas** (top ~55%): Force-layout graph with toolbar, minimap, legend, presets.
  - **Reader panel** (bottom ~45%): Tabbed panel (Overview, Links, Recall, Important) with note content, backlinks, cluster inspector, action buttons.

The old 3-column layout (notes | graph | reader) and workspace modes (workbench/explore/reader/recall) were removed because the graph was too small and the three panels didn't fit.

**When editing the dashboard:**
- The file is a single Python script with inline HTML/CSS/JS in a large `INDEX = r"..."` string.
- CSS and JS edits go inside the INDEX string. Python backend (API endpoints, data structures) must not change.
- After editing: `python3 -m py_compile file.py`, extract JS → `node --check`, restart service, verify HTTP 200.
- `agy --print` can attempt this but frequently **does not persist file changes** — always verify the file was actually modified with `grep`. Fall back to `patch` tool if agy fails.
- See `references/dashboard-layout-structure.md` for the full layout map, CSS pitfalls, and mandatory validation steps.
- See `references/dashboard-premium-redesign-pass.md` for the premium frontend redesign pattern, feature-preservation contract, graph label-density tuning, and QA checklist used for the 2026-05 dashboard pass.
- See `references/dashboard-phase3-decluttering-and-reader-promotion.md` for the next structural pass after the premium redesign: move graph chrome into a side rail, compact non-active notes, add a visible note excerpt, and verify with browser geometry/DOM checks.
- The reader panel uses `.readerMeta` as a single `overflow-y:auto` scroll container — all content (title, tabs, sections, action buttons) scrolls together. Do NOT add `overflow:hidden` to `.reader` or `.readerSections` — this clips content.
- If Root/Recall/Memory Health appears as a cut-off strip, treat it as a layout/scroll bug: increase reader row share, keep `.readerActions` static and before `.readerSections`, and auto-scroll active async tab panels after they render. Details: `references/dashboard-premium-redesign-pass.md`.

## Vault as Private Git Repo

When the user wants to back up the vault or version-control it, use git + GitHub:

```bash
cd /mnt/tb/hermes/obsedianvault
git init -b main
git config user.name "..." && git config user.email "..."
git add -A && git commit -m "..."
gh repo create obsmemory --private --source=. --remote=origin --push
```

**Required `.gitignore` for any Obsidian vault:**
```
# Per-device Obsidian config (can leak device IDs)
.obsidian/workspace*
.obsidian/cache
.obsidian/themes

# Trash
.trash/

# System / editor
.DS_Store
.Thumbs.db
*.swp
*.swo
*~

# Large binaries
*.pdf
*.zip
*.tar.gz

# Secrets (defense in depth)
*.key
*.pem
*.env
secrets.*
credentials.*

# Per-device layout cache, regenerable
.obsidian-dashboard-layout.json
```

**Verification after push:**
- `curl -s -o /dev/null -w "%{http_code}\n" https://api.github.com/repos/OWNER/REPO` returns 404 (private, no auth)
- `gh repo view OWNER/REPO --json name,isPrivate,description,url` returns `isPrivate: true`
- Repo URL: `https://github.com/OWNER/REPO` (visible to logged-in collaborators only)

**Daily auto-sync (recommended).** A one-time push drifts silently. For
continuous backup and cross-device sync, add a daily cron that re-pushes
the vault. See `references/vault-daily-git-auto-sync.md` for the full
pattern (script + Hermes cron job + state file + Cron tab visibility).
See `references/obsidian-dashboard-note-links.md` when fixing Home/Learn/quick-link clicks on `:6065`.

**Dashboard code in the same repo:** version the live server as
`dashboard/obsidian_dashboard.py` + `dashboard/README.md` inside
`SeaXen/obsmemory` (or equivalent). Exclude the legacy hidden
`.dashboard/` copy via `.gitignore` so you do not double-track the same
file. Redeploy live with `systemctl --user restart obsidian-vault-dashboard`,
not a second manual `python3` on port 6065 (systemd holds the port).

Two pitfalls baked into that reference are easy to miss and silently
break the first version:
- `git status --porcelain` does NOT show committed-but-unpushed
  changes; the script must also diff against the upstream branch
  (`git diff <upstream>..HEAD`).
- `git commit` fails with empty stderr when there is nothing to stage
  (because `git add -A` was a no-op); detect the no-op with
  `git status --porcelain` after add and skip straight to push.

**Important pitfall:** after creating `README.md` with vault documentation, always run `curl /api/memory-health` to verify `broken_links` is still 0. The dashboard's wikilink parser scans README.md and any `[[example]]` syntax inside backticks becomes a "broken link" candidate. See Pitfall 33 above.

**Gitignore for vault content with mirror/projection notes:** if your vault has auto-generated notes (Mnemosyne mirror, daily aggregates, schema dumps), those should be in `.gitignore` too — or they create noisy diffs on every cron run. Pattern:
```
# Auto-generated mirror notes
Knowledge/Mnemosyne Mirror.md
Knowledge/Mnemosyne Triples.md
```
Regenerate them on clone via `bash scripts/mnemosyne_to_vault.py` or equivalent.

- See `references/dashboard-recall-ranking.md` for the safe ranking-tuning pattern, canonical note-family boosts, noise suppression, and validation sequence used when improving `/api/recall`.
- See `references/recall-tuning-pitfalls-2026-06.md` for the 2026-06-17 recall pass that took the system from 9.0/10 → 10/10. Covers the **silent FTS5 result discard bug** (the highest-impact single-line fix in this codebase), the **MRR-driven improvement loop**, the **specific vs generic entity split**, the **title_match suppression for intent queries**, the **pure-tag-query daily-note boost**, and the **acceptance bar for 10/10** (`hit_at_k=1.0` AND `mrr=1.0`).
- See `references/hybrid-nightly-cron-pitfalls-2026-06.md` for nightly cron failure modes (no provider, missing API key, 429 quota, **`sessions.json` `_README` collector crash**) and the triage cheat sheet.
- See `references/recall-stress-testing-2026-06.md` for the **real-query stress test methodology** — pull actual user messages from `state.db`, run them through `/api/recall`, and judge top-1 by canonical-match rather than running only a curated eval. A 100/100 curated eval can still hide 80% real-world miss rate if the eval cases don't match what the user actually asks.
- See `references/recall-cross-block-guards-2026-06.md` for the **`effective_intents` override pattern** (Pattern A), the **study-workflow tie-breaker** between umbrella and domain-specific canonicals (Pattern B), and the **pattern-list iteration loop** — the meta-pattern for extending `fix_intent_strong` / `study_intent_strong` based on real-query miss data without over-tuning. Use these when the cross-block guard from Pitfall 28 fires correctly but the boost block below it does not.
- See `references/canonical-injection-pattern-2026-06.md` for the **canonical injection pattern** — when an intent is detected, force-inject the relevant canonical note into the candidate set even if FTS5 tokenization missed it (e.g. "stroke" in query but Medical Study System uses "cerebrovascular"). Guarantees canonical coverage without weakening FTS5 ranking.
- See `references/dashboard-watchdog-pattern-2026-06.md` for the **watchdog cron pattern** — script-only cron (`no_agent: true`) that pings `/api/memory-health` every N hours, alerts on degraded recall or unreachable service, and dedupes alerts to avoid spam. Use this to catch silent dashboard degradation that systemd's auto-restart doesn't surface.
- See `references/canonical-note-strengthening-2026-06.md` for the **canonical-strengthening workflow** — how to add a new domain canonical (e.g. AI Providers, Davidson, Backup/DR), register it in `RECALL_CANONICAL_NOTES`, add a dedicated intent bucket + boost in `recall_intent_signal()`, and validate with a real-query stress test before declaring it shipped.
- See `references/vault-capture-inbox-and-survival-2026-06.md` for capture inbox, survival design, external KB split, and Home-page **Open Capture.md** UX. Ad-hoc: `python3` on skill path `scripts/verify_dashboard_capture_home.py`.
- See `references/dashboard-learn-bridge-tab-2026-06.md` for the **Learn** tab (`loadLearnBridge`, `/api/learn-bridge`). Ad-hoc: `scripts/verify_dashboard_learn_tab.py`.

## Local document ingestion for RAG / Obsidian

When the user wants a **minimal local document → markdown → vault workflow without MCP**, prefer a filesystem-first pipeline:

- install `markitdown` in a **dedicated venv** instead of the main Hermes runtime
- keep a thin wrapper script plus a Python importer script
- write imported markdown into a staging area such as `Inbox/Imports/`
- create one markdown note per source file with frontmatter including source path, filename, extension, import timestamp, converter name, and tags
- use output filenames derived from **stem + extension** (for example `lecture-pdf.md`, `lecture-docx.md`) so different source formats with the same basename do not collide
- treat imported notes as **raw staging material**; promote distilled knowledge into `Knowledge/` or `Work/` only after review

Recommended shape:

- converter venv outside hot runtime, e.g. `/mnt/tb/hermes/venvs/markitdown`
- wrapper script, e.g. `obsidian-ingest.sh`
- importer script, e.g. `obsidian_ingest.py`
- staging note/folder documentation, e.g. `[[Imports]]`

Important verification rule:

- if the vault has both a display path and a resolved path (for example `/mnt/tb/hermes/obsedianvault` vs `/root/.hermes/obsedianvault`), verify they are the **samefile** before claiming imports landed in the wrong place. Path aliasing can make a successful import look misplaced when it is actually the same live vault.

## Common Pitfalls

1. **Do not auto-save everything.** It creates a noisy junk drawer and worsens recall.
2. **Do not load the whole vault.** Search first, read targeted notes.
3. **Do not confuse Obsidian graph with Hermes hot memory.** Graph helps navigation; hot memory is still `USER.md` / `MEMORY.md`.
4. **Do not use the old path `/root/obsidian-vault`.** The active path is `/mnt/tb/hermes/obsedianvault`.
5. **Do not assume wikilinks should include folder/path text.** In this vault the dashboard resolves links by note title/stem, so `Inbox/Imports.md` links cleanly as `[[Imports]]`, not `[[Inbox/Imports]]`.
6. **Do not treat daily notes as task manager.** Only durable next actions belong there.
7. **Do not ingest directly into polished knowledge folders by default.** Raw conversions belong in staging first.
8. **Do not name imported notes from stem alone.** `report.pdf` and `report.docx` will collide unless the extension is part of the output name.
9. **Do not assume two vault paths are distinct copies without checking samefile/symlink semantics.**
10. **Do not rely on `/api/memory-health` alone when verifying recall.** Health score 99.9/100 + empty `/api/recall?query=foo` results = the API is broken even though the dashboard looks green. Always run a live recall query as the final acceptance check.
11. **Do not bulk-create daily notes without a Daily Note Index.** Backfilling N daily notes in one batch spikes the orphan count to N (each new daily note has zero inbound links until something references it). Fix: in the same edit pass, add a "Daily Note Index" section to `AGENT.md` listing all daily notes as `[[YYYY-MM-DD]]` wikilinks. The index brings the orphan count back to 0. See `references/daily-note-bulk-backfill.md`.
12. **Do not silently ship "no write over weak write" on a personal vault.** That policy looks clean but produces 10+ days of zero captures on a quiet personal system, and the user will only notice when they check the vault. For personal vaults, default to "always write a minimal daily stub" and confirm the policy with the user before deploying the cron.
13. **Do not run FTS5 results into a throwaway cursor.** The single biggest recall-bug pattern (2026-06-17): `conn.execute(...).fetchall()` without assigning the result silently throws away the entire FTS candidate set. Symptom: `/api/memory-health` looks fine (96–99/100) but `/api/recall?query=...` never returns notes that exist in the vault. Always assign: `rows = conn.execute(...).fetchall()`. Full reproduction and fix in `references/recall-tuning-pitfalls-2026-06.md`.
14. **Do not judge "10/10" by `/api/memory-health` score alone.** A 99.4/100 health score with `mrr < 1.0` means recall is finding the right notes in the top 5 but not at position 1. Health score = structure/link/review-flow. Recall score = precision. Both must be 100. Run `/api/recall-eval` and check `hit_at_k` AND `mrr` — not just one.
16. **Do not let `title_match` win over intent-seeking queries.** When the query is "what did we decide about the dashboard redesign", `Dashboard.md` wins via `title_match=4.5` (because "dashboard" is in its title) instead of `Memory/decisions.md`. Suppress `title_match` when the query has an explicit intent pattern.
17. **Do not trust a systemd service file path without verifying samefile/bindmount.** `/mnt/tb/hermes/obsidian_dashboard.py` and `/root/.hermes/obsidian_dashboard.py` may be the same inode on this host. Verify with `stat -c '%i'` on both paths before debugging "edits didn't take effect".
18. **Do not let fresh-mtime dominate recall.** A newly created canonical note (e.g. `Memory System Architecture.md`) will have the freshest `mtime` in its folder and dominate recall results for any token it contains, because `recency = 1.0 / (1.0 + math.log1p(age_days))` gives nearly 1.0 to brand-new files. Symptom: a new architecture note wins over specific canonicals like Hermes Operations on generic queries. Fix: `touch -d "YYYY-MM-DD HH:MM" path/to/note.md` to backdate the new note to a realistic date before checking recall. The same risk applies to bulk-imported notes — backdate the whole batch.
19. **Do not blast a strong canonical boost without a competing-intent backoff.** When boosting a canonical (e.g. Hermes Operations +5.5 for ops queries), a query with both `ops` AND `decision`/`fix` intent (e.g. "what did we decide about the dashboard redesign") will give the wrong canonical the full boost and beat the right one. Always gate strong boosts with a competing-intent check: `boost = 3.0 if has_strong_competing else 5.5`. Pattern signals to look for: explicit `decision:` / `fix:` prefixes, "what did we decide", "what was the fix", "fix for", "decide about". When you need to gate against multiple intent families, **extract cross-block guard variables** (`fix_intent_strong`, `study_intent_strong`) at the **top** of `recall_intent_signal()` so every boost block can reference them. See `references/canonical-note-strengthening-2026-06.md`.
20. **Do not over-inject canonicals.** When the canonical injection pattern adds a note to the candidate set with neutral `bm25_rank=5.0`, it competes with the FTS5 top results. If the canonical is meta-architecture (e.g. "Memory System Architecture" instead of "Hermes Operations" for ops queries), remove it from `RECALL_CANONICAL_NOTES` and let it be retrieved via content match. Only domain-specific canonicals (one per detected intent) should be injected.
21. **Do not ship 100/100 on the curated eval alone.** A small hand-picked eval can pass while the user's real queries fail 80% of the time. Always run a stress test from real session queries (`SELECT content FROM messages WHERE role='user' AND length(content) > 30`) and judge top-1 by canonical-match before declaring victory. See `references/recall-stress-testing-2026-06.md`.
22. **Do not skip writing a memory-architecture note when you have two memory layers.** When the system has both hot memory (Mnemosyne / MEMORY.md) and warm memory (Obsidian vault), the cross-link protocol must be documented in a `Knowledge/Memory System Architecture.md` note AND wired into recall. Without it, knowledge drifts between layers and the agent re-derives facts every session.
23. **Do not ship a cron with a single model.** One provider's quota or 429 blacks out the whole job. Use an ordered multi-model list, 2 attempts per model, 2/5/10s backoff, and skip the rest of the budget on HTTP 401/403/400 (same key will fail on every model). Pattern: `references/hybrid-nightly-cron-pitfalls-2026-06.md` (Pitfall 3).
24. **Do not let FTS5 join columns shadow the source table's columns.** When you join a FTS5 virtual table to its source table, FTS5 re-exposes the indexed columns by name. If the source table also has those columns (it must — that's where the values came from), `SELECT id, content` fails with `ambiguous column name`. Symptom: the endpoint returns empty results and recall appears silently broken. Fix: alias every projected column on the source-table side (`working_memory.id AS wm_id`, etc.). Real example: `references/mnemosyne-vault-crosslink-2026-06.md` (FTS5 column-aliasing pitfall).
25. **Do not let a mirror/projection note generate review candidates.** Any note produced automatically by a script (Mnemosyne→vault mirror, daily aggregate, schema documentation) is a projection, not new memory. Without `MEMORY_REVIEW_SKIP_PATHS` covering it, the dashboard's candidate generator treats table rows as "decisions" and "fixes" and dumps 10+ false candidates per run, dropping `review_flow` to 94. Symptom: every review pass becomes a mass-reject of identical boilerplate. Fix: add the note path to `MEMORY_REVIEW_SKIP_PATHS` in `obsidian_dashboard.py` at the same time you create the script that produces it.
26. **Do not interpret "improve X, not [via] Y" as "delete Y."** When the user phrases scope as "improve X, if need not [via] Y" or "make X stronger without going through Y", they mean the *method* of the improvement should not use Y as a dependency — not "remove Y." Killing a working integration (mirror cron, vault files, route, skill instructions) is expensive to undo and breaks whatever else depends on Y. Default to the narrower reading; ask one clarifying question if scope is truly ambiguous; if you do remove something, do it in a single easy-to-revert batch and surface it explicitly. (See the "Scope interpretation" section above.)
27. **Do not use a Python variable in a block before assigning it later in the same function.** Python's `UnboundLocalError` triggers when any assignment to a name exists anywhere in the function body, even if that assignment is in a separate `if` branch that does not run for the current input. Symptom: the function works for one path and crashes with `cannot access local variable 'X' where it is not associated with a value` for another. Fix: define cross-block variables at the **top** of the function, immediately after the early-exit guards, BEFORE any `if` that may use them. Real example: `fix_intent_strong` and `study_intent_strong` in `recall_intent_signal()` are referenced by the `ops` block (top of function) AND defined again in the `medical`/`new-canonicals` block (bottom of function) — one local copy of the name shadows the other, and the order matters. Always define once, near the top, and reuse.
28. **Do not let a strong canonical boost outcompete a stronger specific intent.** When `Hermes Operations` gets +5.5 on any `ops` query, but the query is also about a specific bug ("what was the FTS5 bug fix"), the broader canonical wins over the correct specific one (`issues-fixes-log`). Fix: extract cross-block intent guards (e.g. `fix_intent_strong`, `study_intent_strong`) at the top of `recall_intent_signal()`, and gate strong canonical boosts on them: `boost = 2.0 if fix_intent_strong else 5.5`. The guard pattern list itself should be a small tuple of clear English fragments that appear in real user queries ("what was the fix", "the bug", "plugin fix", "notion fix", "this fix", "how to write a topic file", "study workflow", "chapter build", "viva", "mcq", "sba"). When the boost pattern list is missing a common phrasing ("the last" instead of "the fix"), the wrong canonical wins for the gap. After every ranking change, run a hand-picked stress test of 20+ real user queries and confirm the right canonical wins for each — not just that *some* canonical wins.
29. **Do not treat a real-query stress test "wrong" as a bug without inspecting.** When stress-testing `/api/recall` against real session queries, the top-1 mismatch may be a **legitimate alternative** ("Mnemosyne mirror every 6h" → Mnemosyne Mirror is the right answer, not Hermes Operations; "fcps/mrcp exam notes" → Davidson 24e wins over Medical Study System because the query IS Davidson). Always classify misses as one of: (a) real bug (canonical X should win but Y wins — fix boost), (b) content gap (the right canonical doesn't have the answer yet — write the content), or (c) acceptable disagreement (both are defensible — leave alone). Trying to force 24/24 wins when some of them are (c) just over-tunes the boost and breaks (a)s that were already correct.
30. **Do not assume the running service has your latest edits.** `systemctl restart` is the ONLY reliable way to load new code. The `python3 -m py_compile` check only proves the file parses — it does not exercise the HTTP path. The pattern that always works: `py_compile` → `systemctl restart` → `sleep 2` → live `curl /api/recall?query=...` query. If you skip the restart, you are testing OLD code, and any rank changes you make "didn't take effect" — exactly the trap that wasted an iteration when the `fix_intent_strong` was assigned at the bottom of `recall_intent_signal` but the `ops` block at the top referenced it.
30a. **Verify restart with a query that exercises the NEW code path.** The naive restart check (`curl /api/recall?query=hermes` → "Hermes Operations wins") passes equally well against the OLD code and the NEW code, so it gives false confidence that the restart succeeded. After every recall-boost change, run a hand-picked query that would have given a DIFFERENT result under the old boost (e.g. "what was the last plugin fix" — passes only when `fix_intent_strong` actually back-off'd the ops boost). If the new query gives the same result as before the change, either (a) the restart didn't actually load the new file, (b) the new boost clause isn't being reached, or (c) the pattern list is missing the phrasings you think it covers.
31. **Do not let `scan_notes()` extract fields that the recall candidate dict silently drops.** When `extract_frontmatter_tags()` / `TAG_RE.findall()` correctly populate `note["tags"]` inside `scan_notes()`, but the candidate dict in the recall outer loop (`candidate = { "path": ..., "title": ..., "source_kind": ..., }`) omits `"tags": note.get("tags", [])`, the tag-combo filter `?tags=foo` still works (it reads `note_lookup[row["path"]]` for filtering) but the API response never carries the tag list to the client. Symptom: filter works server-side, browser dashboard shows `tags=[]` for every note. Verification probe: `curl -s 'http://localhost:6065/api/recall?query=hermes&limit=1' | python3 -c "import sys,json; print(json.load(sys.stdin)['results'][0].get('tags', 'MISSING'))"` — if it prints `MISSING`, the field is being dropped. Rule: every field `scan_notes()` populates must appear in the candidate dict by the same name, or filter logic will silently mismatch UI/expectations.
32. **Do not gate intent boosts on `intents` membership when the guard variable is more permissive.** When `fix_intent_strong = any(p in query_low for p in (...))` is the broad guard (matching "gotcha", "workaround", "the last", etc.) and the boost block at the same function level uses `if "fix" in intents:` (a narrower check that depends on `detect_recall_intents` having matched), the two will disagree. The broad guard fires, but the boost block does not. Fix: define the broad patterns ONCE at the top of the function and inject the corresponding intent into `effective_intents` at the call site (`query_intents | ({"fix"} if fix_intent_strong else set())`), then pass `effective_intents` into `recall_intent_signal()`. Symptom: stress test shows the right canonical CAN win when you manually inject intent, but the live API does not. Pitfall 28 covers the cross-block guard variable; this is the matching rule for keeping `detect_recall_intents()` and the guard list from drifting.
33. **Do not write `[[wikilink]]` syntax inside README.md or other documentation files.** The dashboard's wikilink parser scans every markdown file in the vault (including `README.md`) and picks up `[[Title]]` patterns inside backticked examples. A `[[AGENT.md]]` example in your README will be flagged as a real broken link because the convention is title-only wikilinks (`[[AGENT]]`, not `[[AGENT.md]]`). Real bug from 2026-06-17: after committing a new `README.md` to the vault, `broken_links` jumped from 0 to 1 with source `README → AGENT.md`. Fix: use plain prose ("Wikilinks by title, not by path") or code fences without the `[[ ]]` brackets. Never write `[[Title]]` inside a doc file unless it is a real wikilink to a real note.
34. **Do not ship a vault without checking if a /README.md is being wikilink-scanned.** Whenever you add a new markdown file (README, CHANGELOG, CONTRIBUTING, etc.) to a vault that has a wikilink scanner, immediately re-run the scan and the broken-links check. A README with example `[[X]]` syntax can silently pollute the health score. For Obsidian dashboards: after creating any new top-level `.md`, restart the service and `curl /api/memory-health` to confirm `broken_links` is still 0.
35. **Do not assume `[[Title]]` vs `[[path/with/extension]]` is interchangeable.** The dashboard resolver looks up titles, not paths. `[[AGENT.md]]` and `[[AGENT]]` are not equivalent — only the title form resolves. Documentation that shows the path form as a "prettier" alternative is teaching users to write broken links. Either consistently use the title form for examples, or use prose like "the AGENT note" instead of wikilink syntax in documentation.
36. **Do not try to restart a systemd-managed service with a bare `python3 file.py` foreground command.** When a long-running service like `obsidian-vault-dashboard` is registered as a `systemd --user` unit, the unit auto-respawns the process when it dies. A manual `python3 /mnt/tb/hermes/obsidian_dashboard.py` started in a foreground terminal will bind to port 6065 fine, but the previous systemd-managed instance is still listening, so any second foreground start fails with `OSError: [Errno 98] Address already in use`. Killing the foreground process and trying again still leaves the systemd-managed one holding the port. Symptom: confusing port-in-use errors, attempts to restart seem to do nothing, and the user's edits to the script do not appear live because the systemd-managed instance is still running the OLD code. Fix: discover the service first (`systemctl --user list-units --type=service | grep <name>`), then `systemctl --user restart <name>` to load the new file. Verify with `systemctl --user is-active <name>` and `curl -s -o /dev/null -w '%{http_code} size=%{size_download}\n' http://127.0.0.1:6065/`. This is the only reliable restart for any user-service in this kind of setup.
37. **Strip accidental `read_file` line-number artifacts from vault markdown before declaring polish complete.** If prior agent work pasted tool output into notes, files may contain literal prefixes like `    81|- **Outcome:** ...`. The dashboard health score may still show 100 because links/recall pass, but the notes are visibly polluted and secret scanners can false-trigger on strings like `task-shaped` (`sk-`). Probe with `rg '^\\s*\\d+\\|' /mnt/tb/hermes/obsedianvault -g '*.md'`; if the pattern appears in real notes, strip `^\\s*\\d+\\|` from affected markdown files, then rerun `/api/memory-health`, `/api/recall-eval`, and `/api/quality-gate`.
38. **Do not assume every `sessions.json` value is a session object.** The file includes a string `_README` (gateway routing index text). Collectors that call `.get()` on each value without `isinstance(meta, dict)` crash with `AttributeError` and fail the nightly cron before any LLM call. Symptom looks like a broken AI job but the fix is a one-line type guard. See `references/hybrid-nightly-cron-pitfalls-2026-06.md` (Pitfall 4).
39. **After writing or backfilling any `Daily/YYYY-MM-DD.md`, update `AGENT.md` Daily Note Index in the same turn.** Orphans are computed from inbound wikilinks; a new daily without `[[YYYY-MM-DD]]` on `AGENT.md` drops `link_health` ~2 points per note even when recall works. Re-check `/api/memory-health` until `orphans: []`.
40. **Do not leave pending memory-review candidates after a vault edit pass.** Editing bridge notes, daily logs, or `decisions`-tagged lines re-triggers the scanner; most hits are false positives (tables, tag lists, protocol text). Append real decisions to `Memory/decisions.md` manually, then reject pending items via dashboard or `scripts/flush_memory_review_noise.py`. Prefer **code fix** (`_memory_review_line_is_noise` + skip paths) when the same false patterns recur — see `references/dashboard-review-scanner-and-quality-gate-2026-06-25.md`. Until `pending` is 0, `review_flow` stays below 100 and `/api/quality-gate` fails the review_queue gate.
41. **`session_search` FTS can return zero hits** for recent multi-word queries while browse mode and `mnemosyne_recall` still surface the thread. For vault audits, combine browse + Mnemosyne recall; do not conclude \"nothing happened\" from empty FTS alone.
42. **Do not merge Yan/llm-wiki auto-ingest into `obsedianvault`.** Curated memory vault (~70 notes, recall-tuned) beats 1,000-file compounding KB for this host. Optional separate `WIKI_PATH` + skill `llm-wiki` for research only — see `Knowledge/External KB Patterns` and `references/vault-capture-inbox-and-survival-2026-06.md`.
43. **Do not claim dashboard perf without cache + idle graph.** Before 2026-06-26, every API call re-scanned all markdown; graph RAF could run on Home/Learn. After edits, verify warm `/api/graph` and that switching to Home stops simulation (`references/dashboard-perf-scan-cache-2026-06.md`).
44. **Do not run `systemctl --user restart` from inside the Hermes gateway** when the tool blocks it — use an external shell or `pkill` + systemd `Restart=always`; otherwise you test stale Python while believing you deployed.

## Verification Checklist

- [ ] `OBSIDIAN_VAULT_PATH` points to `/mnt/tb/hermes/obsedianvault`.
- [ ] `AGENT.md` is readable.
- [ ] `Dashboard.md` exists.
- [ ] Daily note exists or is created only when useful.
- [ ] Writes are high-signal and linked with `[[wikilinks]]`.
- [ ] Browser dashboard on port `6065` responds if needed.
