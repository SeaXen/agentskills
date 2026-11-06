# Pipeline internals (update.py)

`update.py` lives at the repo root, uses manual `sys.argv` parsing (not argparse), and derives its own location from `__file__` — it works from any clone path.

## Entry points

- `update.bat` → `python update.py %*` then `pause` (Windows convenience wrapper).
- `python update.py` — full sync (network discovery + upstream sync + commit + push + R2 sync).
- `python update.py --offline` / `--skip-discovery` — skips [0/6] network discovery only; everything else (including the ls-remote check) still runs.
- `python update.py --reindex` / `--index` — rebuilds indexes + categories + lockfiles only (with `--push` also commits).
- Delegations: `--skills-sh`/`--skillssh` → `skillssh/skillssh.py`; `--skillleaderboard`/`--trending`/`--starred`/`--traction`/`--newest` → `skillleaderboard/skillleaderboard.py`.
- Read-only: `--find <kw>`, `--tags`, `--tag <name>`, `--about`.

## Step details

### [0/6] sync_embedded_ecosystems()
Runs two sub-scripts, each of which does its own ingest/reindex (their log lines can appear out of order relative to update.py's own steps — cosmetic):
- `skillssh/skillssh.py --sync --min-installs 100k` — audits skills.sh; clones missing repos into `library/<owner>-<repo>/`; saves `upstreams.json`. Uses `skillssh/.cache_skills_sh.json` with a 7-day TTL — delete the file to force a live refresh.
- `skillleaderboard/skillleaderboard.py --starred 150 --ingest` then `--trending 50 --ingest` — JSON API (`https://www.skillleaderboard.com/api/catalog`), sorts by `stars` / `stars7d` with null-safe `x.get('stars') or 0`.

### [1/6] sync_all_upstreams(force)
1. Loads `library/upstreams.json`; applies `library/opt_out.json` exclusions (deletes excluded repo dirs).
2. Parallel `git ls-remote <url> HEAD` check (36 workers, 5 s timeout).
3. Repos whose `.upstream_commit` differs are cloned `--depth 1 --filter=blob:none --single-branch` (45 s timeout) into `.temp_upstream_clones/`.
4. Only README/LICENSE are copied from the repo root; every dir containing a `SKILL.md` is extracted to `library/<repo>/skills/<name>/` (on collision, content-identical → refresh in place; content differs → parent-prefixed name).
5. `clean_skill_internal_junk()` strips dev-tooling junk inside the extracted skills.
6. Repo-root purge keeps only `skills/`, `skills_index.json`, `.upstream_commit`, `README*`, `LICENSE*`.
7. Watermark written; `.git` stripped; temp clone removed.
Returns the list of repo IDs actually updated — this list drives steps [2/6] and [3/6].

### [2/6] sync_active_skills(updated_repo_ids)
Workspaces: this repo (`agents_dir`), `D:\Gravity\Managment\.agents`, and the parent `.agent` workspace. Lockfile workspaces require both `skills/` and `skills-lock.json`; a skill updates only when its lockfile `source` (owner/repo → `owner-repo` slug) matches a repo updated this run. The lockfile-less parent workspace uses a unique-name fallback: update only when exactly one updated repo contains that skill name.

### [3/6] rebuild_all_indexes(updated_repo_ids, force)
Walks `library/<repo>/skills/` one level per repo; updated/new repos are re-parsed (regex `description:`/`category:` from the first 2,000 chars of SKILL.md), others reuse the cached per-repo `skills_index.json`. Writes the master `library/skills_index.json` (list of records: id, name, repository, category, description, path, activation_cmd).

### [4/6] sync_lockfiles()
Reconciles each workspace's `skills-lock.json` against the actual skills dirs; new skills get a `./local-library` source entry.

### [5/6] rebuild_categories_and_provenance()
Rebuilds the 38-category taxonomy (`category/categories_index.json`), regenerates `SKILLS_PROVENANCE.md`, then `sync_documentation_metrics()` rewrites the library-reserve measures in README/ARCHITECTURE/PRODUCT/AGENTS.

### [5.5/6] rebuild_skill_sea_catalog()
Runs `node Skill.Sea/scripts/build-catalog.js`, which:
- Reads `library/skills_index.json` (fsSkillMap + librarySkills), `library/upstreams.json`, `library/opt_out.json`.
- Scans `library/` to populate every repository in the repo map (this is why the site repo count can differ from `upstreams.json` by a few).
- Merges the hot-set union: `skills/` + `../.agent/skills/` (guarded by `existsSync`).
- Writes `Skill.Sea/data/{stats,catalog,categories,repositories}.json`.
Then `sync_frontend_doc_numbers()` refreshes ~28 hardcoded numbers across 9 files (AGENTS.md, README.md, PRODUCT.md, Skill.Sea/README.md, Skill.Sea/PRODUCT.md, Skill.Sea/AGENTS.md, Skill.Sea/package.json, Skill.Sea/manifest.json, Skill.Sea/index.html) using number-agnostic regexes, so the fix persists forever.
With `--deploy`: also `sync-r2.js --allow-offline` + `npx wrangler deploy`.

### [6/6] git_commit_and_push()
1. `git status --porcelain -z --untracked-files=all` (NUL-separated — C-quoting of non-ASCII paths would break pathspecs).
2. Staged: all tracked modifications/deletions/renames; untracked only if under `skills/`, `category/`, `Skill.Sea/data/`, a root doc, a library index/registry file, a repo-root file of an updated repo, or an ancestor prefix present in `index_prefixes` (from `skills_index.json`). Everything else is counted as skipped junk.
3. Staged in 20K-char chunks via `git add --pathspec-from-file=-` with `:(literal)` prefixes (Windows 32K command-line limit).
4. Commit + push; pre-commit rebuilds the catalog; pre-push syncs R2.

## Data flow to production

```
build-catalog.js → Skill.Sea/data/*.json → sync-r2.js → R2 bucket skill-sea-vault
    → Cloudflare Worker (worker.js) streams /data/* with ETag/304 → skill.drsea.top
```

No redeploy for data-only changes. `_headers` cache: stats.json 60 s, catalog.json 1 h, other `/data/*.json` 24 h — stale data right after a sync is expected. Redeploy (`cd Skill.Sea; npm run deploy`) only when `worker.js` or static assets change.

## Git hooks (local, POSIX sh, always exit 0)

- **pre-commit**: staged `^(skills|library|category|\.agent/skills)/` → runs build-catalog.js and `git add Skill.Sea/data/`.
- **pre-push**: outgoing `^(skills|library|category|\.agent/skills|Skill\.Sea/data)/` → runs `sync-r2.js --allow-offline`.
Reinstall with `python scripts/setup_hooks.py`.

## GitHub Actions

- `update-vault.yml` — cron Sunday 00:00 UTC + manual dispatch → `python update.py --no-push`, auto-commits to main.
- `auto-catalog.yml` — pushes touching skills/library/category/.agent/skills/build-catalog.js → rebuild + auto-commit `[skip ci]` + sync-r2 if `CLOUDFLARE_API_TOKEN` is set (forks without the secret degrade gracefully).

## Timing expectations

- `--offline` run: ~3 min (61 s of that is the ls-remote check when few repos changed).
- Full online run: ~6 min when discovery has little to ingest.
- Fresh skills.sh cache refresh (audit/--check): ~4–8 min for ~2,300 repo pages.
- Full 1,500-repo discovery: 12–24 h — never run this through the agent harness; use the user's own terminal.
