# AGENTS.md — Antigravity Agent Skills Vault & Skill.Sea

Operational runbook for AI coding agents (OpenCode, Claude Code, Cursor, Codex, Windsurf).

## What this repo is

`D:/Repo/.agents` **is** the git repo root (remote `SeaXen/agentskills`, branch `main`) — not a subfolder of a larger app. It holds a catalog of agent `SKILL.md` modules plus **Skill.Sea**, a zero-dependency web app deployed to Cloudflare.

## Ground-truth numbers — do not guess, read the file

Counts drift and the docs disagree. Trust these, in order:

| Fact | Source of truth |
|---|---|
| total skills / categories / repos / hot-set | `Skill.Sea/data/stats.json` |
| per-skill catalog records | `Skill.Sea/data/catalog.json` (~24.7 MB) |
| repo cards | `Skill.Sea/data/repositories.json` |

Verified 2026-11-06: **20,483 skills · 38 categories · 380 repositories · 130 hot-set**.

`README.md` (25,695 / 18,722 / 17,145), `update.py --help` ("364 repositories"), and this file's previous numbers are **stale**. Don't propagate them.

## The #1 gotcha: the hot-set is a UNION of two directories

`Skill.Sea/scripts/build-catalog.js` (lines 12–13) merges **both**:

- `D:/Repo/.agents/skills/` (90 dirs)
- `D:/Repo/.agent/skills/` (91 dirs — **parent workspace, outside this repo**)

→ `activeHotSetCount = 130`.

Adding a skill to `.agents/skills/` will **not** bump the count by 1 if the same skill already exists in `../.agent/skills/`. Edit or remove the parent-workspace copy too, or you'll get confusing diffs and counts.

Related: each `category/<name>/` holds only `README.md` + `skills_index.json`. `.gitignore` line 27 (`category/*/*/`) blocks anything nested deeper, so per-skill folders there are never committed. Confirm with `git ls-files category/<name>`.

## Layout (non-obvious parts only)

- `library/` — 381 dirs of full upstream clones. `upstreams.json` lists 379; `software-mansion-argent` and `__pycache__` are untracked extras. `opt_out.json` (`excluded_repositories` / `excluded_skills`) is honored by the catalog build.
- **Never `git add -A` here.** ~857 untracked dirs / ~6,900 files already sit under `library/` — re-clones create flat-named duplicates (`skills/core-tavily-search/`) beside the tracked nested layout (`skills/core/tavily-search/`). Stage explicit paths only.
- `skills/` — active workspace hot-set (tier 1).
- `workflows/` (18 files), `agents/` (20 personas), `rules/` (`GEMINI.md`, `brainsyncory.md`).
- `Skill.Sea/` — the web app. **See `Skill.Sea/AGENTS.md`: it is the frontend runbook and is more current than this file for anything frontend.**
- `scripts/` — `verify_all.py`, `checklist.py`, `session_manager.py`, `auto_preview.py`, `setup_hooks.py`.
- No `opencode.json`, `.cursorrules`, `.cursor/rules`, or `copilot-instructions.md` exists anywhere under `D:/Repo`.

## Commands

### `update.py` — manual `sys.argv` parsing, NOT argparse

**Bare `python update.py` is a full sync: it makes network calls to skills.sh and skillleaderboard.com, then commits and pushes to GitHub.** The flag list below is read from source; `--help` text is stale.

| Flag | Effect |
|---|---|
| *(none)* | full sync + discovery + commit + push + R2 sync |
| `--reindex` / `--index` | rebuild indexes/categories only |
| `--find <kw>` | search, no writes |
| `--tags` / `--list-tags` / `--tag <name>` | tag browsing |
| `--about` | repo metadata |
| `--no-push` | skip `git commit && push` |
| `--offline` / `--skip-discovery` | skip skills.sh + skillleaderboard network calls |
| `--skills-sh` / `--skillssh` | skills.sh only (`--check` / `--sync` / `--update` / `--min-installs N`) |
| `--skillleaderboard` / `--trending N` / `--starred N` / `--traction N` / `--newest` | leaderboard only (`--ingest`, `--push`) |
| `--deploy` | also `npx wrangler pages deploy . --project-name=skill-sea` |
| `--force` | override guards |

Safe local iteration: `python update.py --reindex --no-push --offline`

### `library/activate_skill.py` — the user-facing skill CLI (missing from old docs)

`search <kw>` · `activate`/`link <name>` (win32 junction/symlink) · `remove`/`deactivate <name>` · `activate-category <cat>` · `activate-repo <repo>` · `list`/`ls`/`active` · `update`/`sync`/`pull` · `move <name> --to <dest>` · `repos` · `categories` · `category <name>` · `info <name>` · `help`

Never activate >70 skills into `.agent/skills/` at once — prompt bloat (see `lessons.md`).

### npm scripts

Root `package.json`: `activate` / `link` / `remove` → `activate_skill.py`; `find` → `update.py --find`; `update`; `reindex`; `install-all` → `npx skills add SeaXen/agentskills --all`.

`Skill.Sea/package.json`: `start`/`dev` = `node server.js`; `build` = `build-catalog.js`; `sync` = build + sync-r2; `test` = `verify.js && python tests/test_webapp.py`; `deploy` = `wrangler deploy`.

## Testing & verification

```powershell
node Skill.Sea/scripts/verify.js        # 64 checks — the real gate (not 63)
cd Skill.Sea; npm start                 # separate shell; server must already be running
python Skill.Sea/tests/test_webapp.py   # Playwright; does NOT spawn the server
```

- `verify.js` = **64 checks**. This file and `Skill.Sea/AGENTS.md` previously said 63 — stale.
- `test_webapp.py` assumes a server is already listening on `http://127.0.0.1:8080` (`BASE_URL` env overrides). It will not start one.
- `Skill.Sea/scripts/verify-fixes.js` exists but is undocumented everywhere.

## Automation — git is never blocked

`.git/hooks/pre-commit` and `pre-push` are POSIX `sh`, both `exit 0` on any failure. Reinstall: `python scripts/setup_hooks.py`.

- **pre-commit**: staged paths matching `^(skills|library|category|\.agent/skills)/` → runs `node Skill.Sea/scripts/build-catalog.js` and `git add Skill.Sea/data/`. Requires `node` on PATH.
- **pre-push**: outgoing diff matching `^(skills|library|category|\.agent/skills|Skill\.Sea/data)/` → runs `node Skill.Sea/scripts/sync-r2.js --allow-offline`. Warns and skips if `node` is missing.

`.github/workflows/`:

- `auto-catalog.yml` — push to `main` touching `skills/**`, `library/**`, `category/**`, `.agent/skills/**`, or `build-catalog.js` → rebuild + auto-commit `Skill.Sea/data/*.json` (`[skip ci]`) + sync-r2 if the `CLOUDFLARE_API_TOKEN` secret is set.
- `update-vault.yml` — cron `0 0 * * 0` (Sun 00:00 UTC) + `workflow_dispatch` → `python update.py --no-push`, auto-commit to `main`.

## Data flow to production

`build-catalog.js` writes `Skill.Sea/data/*.json` → `sync-r2.js` uploads to R2 bucket `skill-sea-vault` → `worker.js` streams `/data/*` from R2 with ETag/304 support. **No redeploy needed for data-only changes**; redeploy only if `worker.js` or static assets change (`cd Skill.Sea; npm run deploy`).

- Endpoints: `https://skill.drsea.top` (primary) · `https://skill.drsea.eu.org` (mirror) · `https://skill-sea.drsea.workers.dev` (worker direct).
- `wrangler.toml`: worker `skill-sea`, `run_worker_first=["/data/*"]`, R2 binding `SKILLS_BUCKET`, `compatibility_date 2024-11-01`.
- `functions/data/[[path]].js` is the legacy Pages Function path (`_routes.json` still routes `/data/*`); the Worker is primary.
- `_headers` sets per-path cache: `stats.json` 60s, `catalog.json` 1h, other `/data/*.json` 24h — stale data right after a sync is expected, not a bug.

## Skill.Sea frontend invariants — violating these breaks mobile or the zero-dep build

- **Zero runtime deps.** No React/Vue/Svelte/Tailwind/Webpack/Vite. Pure HTML5 + CSS custom properties + vanilla ES6. `server.js` uses only Node stdlib (`http`, `fs`, `path`, `url`, `zlib`).
- `body { touch-action: pan-y }` is mandatory — prevents touch-freeze on mobile viewports.
- `overscroll-behavior-y: none` **only** on modal scroll containers (`.drawer-body`, `.comparator-body`, `.stack-items-list`) — never on `html`/`body`.
- `.agent-stack-tray` outer fixed wrapper: `pointer-events: none`; children (`.stack-dock-btn`, `.stack-panel`) get `pointer-events: auto`.
- Tokens: teal `#1d9e75` / strong `#0f6e56`; light surface `#f9f9f7`; dark `#0b0b0b`.
- `font-variant-numeric: tabular-nums` on all counts and table columns.
- Frontmatter descriptions containing `:` must be quoted or use a block scalar (`>-`). `build-catalog.js` handles folded scalars and has a regex fallback for malformed YAML — don't rely on the fallback.
- **Never auto-delete non-skill files** in `library/<repo>/`. Upstream READMEs, examples, and scripts stay intact unless the user explicitly instructs deletion.

## Other instruction sources in this repo

- `Skill.Sea/AGENTS.md` — frontend runbook (its own item counts are stale).
- `rules/GEMINI.md` — `trigger: always_on`; rule priority P0 (`GEMINI.md`) > P1 (agent `.md`) > P2 (`SKILL.md`); "selective reading" = read `SKILL.md` first, then only matching sections.
- `lessons.md` — win32 Python CLIs must call `sys.stdout.reconfigure(encoding='utf-8')` (cp1252 `UnicodeEncodeError` on emoji); quote YAML frontmatter colons; keep ≤70 active skills.
- `ARCHITECTURE.md`, `PRODUCT.md`, `SKILLS_PROVENANCE.md` — prose only, several stale numbers.

## Incident runbook

**Live site shows stale counts** → `node Skill.Sea/scripts/build-catalog.js`, then `node Skill.Sea/scripts/sync-r2.js`. Auth failure → `npx wrangler whoami` / `npx wrangler login`, or pass `--allow-offline` in CI/offline. Worker or static assets changed → `cd Skill.Sea; npm run deploy`.

**`build-catalog.js` produced corrupted JSON** → a newly pulled upstream has malformed frontmatter; the build prints the offending path. Fix the frontmatter — never hand-edit `catalog.json`.

**Python CLI crashes with `UnicodeEncodeError`** → add `sys.stdout.reconfigure(encoding='utf-8')` at entry.
