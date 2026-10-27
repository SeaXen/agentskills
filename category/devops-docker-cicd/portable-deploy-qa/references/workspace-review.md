# Multi-App / Workspace-Wide Review

Use when the skill must run across **every app in a workspace**, not one project.

## Scope detection

Scan the workspace root for app roots. An app root = a directory containing any of:
`package.json` | `pyproject.toml` | `requirements.txt` | `go.mod` | `Cargo.toml` | `Dockerfile` | `wrangler.toml`

Skip: `node_modules`, `.git`, `dist`, `build`, `.next`, `out`, `coverage`, `.agent`, `.claude`, `.agents`, `docs`, `vendor`.

```bash
# list every app root under the workspace
for d in */ ; do
  if ls "$d"package.json "$d"pyproject.toml "$d"requirements.txt "$d"go.mod "$d"Cargo.toml >/dev/null 2>&1; then
    echo "$d"
  fi
done
```

## Per-app pipeline

For each app root, run the full skill independently — the app may use a different port, framework, and package manager.

```
for app in <roots>:
  1. DETECT    -> scripts/detect_env.py <app>      # port, pkg, framework, routes
  2. PREFLIGHT -> scripts/preflight.py <app>       # required vs warning
  3. SECURITY  -> scripts/security_scan.py <app>   # HIGH findings
  4. SHOTS     -> scripts/capture_screenshots.py --root <app> --url <detected>
  5. README    -> rewrite per references/readme-standard.md
  6. GATES A-L -> visual, perf, polish, lighthouse, security, a11y, seo, tests, reliability, docs, observability, cost
```

Apps whose server cannot start (no deps installed, missing env, external DB) are marked **SKIPPED (reason)** — not silently passed.

## Priority order

Review highest-value first when time is limited:
1. Apps with the largest README/feature surface (most user-facing)
2. Apps with production deployment configs
3. Apps with detected HIGH security findings
4. Apps with no README or boilerplate README

## Cross-app consistency

After individual passes, check workspace-wide:
- [ ] Same README structure across all apps (or each uses readme-standard.md)
- [ ] Same screenshot naming convention (`docs/screenshots/<slug>.png`)
- [ ] Same env var naming for shared concepts (`DATABASE_URL`, `PORT`, `APP_URL`)
- [ ] Same deploy instructions and platform coverage
- [ ] Same CI workflow shape
- [ ] Consistent license + contributing docs
- [ ] No app still ships `create-next-app` boilerplate

## Aggregate report (write to `PRODUCTION_REVIEW.md` at workspace root)

```markdown
# Workspace Production Review

Reviewed: <date> | Apps: <N>

| App | Port | Stack | Pre | Sec | README | Shots | Gates A-L | Blockers |
|-----|------|-------|-----|-----|--------|-------|-----------|----------|
| Lumen | 8807 | Vite | 11/24 | 4 med | TODO | 0 | - | 2 |
| crypfeed | 9986 | Express | 18/24 | 0 | OK | 0 | - | 3 |

## Per-app findings
### <App>
- **Blockers**: ...
- **Fixed**: ...
- **Gates**: A PASS | B ... | L ...
```

Report every app — including ones skipped, with the reason. A silent app is a hidden risk.

## Rules

- Never modify one app's config to satisfy another app's convention.
- Keep app-local changes inside that app's folder.
- The aggregate report lives at the workspace root, not inside apps.
- Re-running the sweep must be idempotent: detect existing screenshots and README sections before overwriting.
