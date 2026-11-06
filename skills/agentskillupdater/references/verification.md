# Post-run verification protocol

Run this after **every** update.py run, and after any manual change to `library/`, `skills/`, `category/`, or `Skill.Sea/data/`. A run is not "done" until all five gates pass.

## Gate 1 — push confirmed

```powershell
git rev-parse HEAD
git rev-parse origin/main
```

Both must print the same hash. If they differ, the push failed (check network / auth) — do not proceed to other gates.

## Gate 2 — the 64-check suite

```powershell
node Skill.Sea/scripts/verify.js
```

Expected: `🎉 ALL 64 VERIFICATION CHECKS PASSED`. (Older docs say 63 — stale.) The suite covers the data files, worker routing, SPA routes, cache headers, traversal/dotfile blocking, and schema consistency. A failure here means either a corrupted data file (rebuild, never hand-edit) or a frontend regression.

## Gate 3 — live site matches local

```powershell
# local
Get-Content Skill.Sea/data/stats.json
# live (stats.json CDN cache is 60s — wait a minute after a sync before comparing)
node -e "fetch('https://skill.drsea.top/data/stats.json').then(r=>r.json()).then(j=>console.log(JSON.stringify(j)))"
```

`totalSkills`, `totalCategories`, `totalRepositories`, `activeHotSetCount` must match. A mismatch usually means the pre-push hook's R2 sync did not run (offline?) — fix by running `node Skill.Sea/scripts/sync-r2.js`.

## Gate 4 — stale-number sweep

```powershell
Select-String -Path AGENTS.md, README.md, PRODUCT.md, Skill.Sea/README.md, Skill.Sea/PRODUCT.md, Skill.Sea/AGENTS.md, Skill.Sea/package.json, Skill.Sea/manifest.json, Skill.Sea/index.html -Pattern '18,722|20,483|17,145|25,695|20\.30|\b339\b|\b370\b' | Select-Object Path, LineNumber, Line
```

Expected: **zero genuine hits**. One legit remainder may exist: README.md's category table has a real per-category count (`**380**` for backend-api-design) — that is data, not staleness. `Select-String -Path` shows only the basename in `.Filename`; use `.Path` to see which file a hit came from (Skill.Sea subdirectory docs have their own copies of these numbers).

If genuine hits remain, the doc auto-sync (`sync_frontend_doc_numbers()` in update.py) is missing a pattern — add a number-agnostic regex rule for the exact phrasing, then re-run.

## Gate 5 — clean tree

```powershell
git status --porcelain --untracked-files=no
```

Expected: empty (no tracked modifications pending). Untracked entries are acceptable only if they are known junk (orphan `library/` dirs not in `skills_index.json`, historical review artifacts under `docs/review/`) — the staging filter intentionally skips them.

## What a healthy run's log looks like

```
[0/6] Automated Discovery ...          (full runs only)
[1/6] ... Checked N remotes in ~61s    → Updating K repositories in parallel
[2/6] Active workspace skills ...      (or "protected and up to date")
[3/6] Re-indexed Master index (N skills across M repos: X cached, Y parsed)
[4/6] lockfiles up to date
[5/6] SKILLS_PROVENANCE.md: M repositories / N skills
[5.5/6] Catalog: Total skills N · Total repositories M · Active Hot-Set 130
       ✓ Refreshed hardcoded counts in docs/frontend: <9 files>
[6/6] Staged N paths (M untracked junk entries skipped)
       [main <hash>] chore(skills): automated update of skills & library (<ts>)
       📦 Uploading ... (pre-push R2 sync)
       🎉 SUCCESS: All repos, new skills, categories, and docs updated and pushed!
EXIT CODE: 0
```

Out-of-order `[3/6]`/`[5/6]` lines before `[1/6]` are the discovery sub-scripts doing their own reindex — cosmetic, not an error.

## Quick health check without a run

```powershell
python update.py --about                    # hot-set count, library stats
python skillssh/skillssh.py --check --min-installs 500k   # coverage of the popular tier
```

`--check` prints "Installed / Missing / Coverage" for the tier; ≥100K coverage should stay near 100%. A sudden jump in "Missing" means either new repos appeared on skills.sh or (historically) the install-count parser regressed — verify a couple of repos against the live site before trusting the number.
