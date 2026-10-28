# Multi-App / Workspace-Wide Review

Use when the skill must run across **every app in a workspace**, not one project.

## Scope detection

Scan the workspace root for app roots. An app root = a directory containing any of:
`package.json` | `pyproject.toml` | `requirements.txt` | `go.mod` | `Cargo.toml` | `Dockerfile` | `wrangler.toml`

Skip: `node_modules`, `.git`, `dist`, `build`, `.next`, `out`, `coverage`, `.agent`, `.claude`, `.agents`, `docs`, `vendor`.

```bash
# list every app root under the workspace (POSIX shell)
for d in */ ; do
  if ls "$d"package.json "$d"pyproject.toml "$d"requirements.txt "$d"go.mod "$d"Cargo.toml >/dev/null 2>&1; then
    echo "$d"
  fi
done
```

PowerShell equivalent:

```powershell
Get-ChildItem -Directory | Where-Object {
  Test-Path (Join-Path $_.FullName "package.json") -or
  Test-Path (Join-Path $_.FullName "pyproject.toml") -or
  Test-Path (Join-Path $_.FullName "requirements.txt") -or
  Test-Path (Join-Path $_.FullName "go.mod") -or
  Test-Path (Join-Path $_.FullName "Cargo.toml")
} | Select-Object -ExpandProperty Name
```

Or simply: `python scripts/scan_workspace.py <workspace>` (JSON, cross-shell).

## Per-app pipeline

For each app root, run the full skill independently — the app may use a different port, framework, and package manager.

**Fastest path** — the orchestrator does the whole per-app pipeline (scope → fix → measure → judge → report) and starts the app itself:

```bash
for app in <roots>: do
  python scripts/review.py --root "$app" --serve --fix
done
```

Each app gets its own `qa/report.md` and `qa/summary.json`.

**Step by step** (when you want to drive the gates yourself):

```
for app in <roots>:
  1. DETECT    -> scripts/detect_env.py <app>      # port, pkg, framework, routes, healthz
  2. PREFLIGHT -> scripts/preflight.py <app>       # required vs warning (up to 30 checks)
  3. SECURITY  -> scripts/security_scan.py <app>   # HIGH findings
  4. DEPS      -> scripts/dep_audit.py <app>        # dependency CVEs (exit 2 = tool missing)
  5. DEPLOY    -> scripts/deploy_verify.py <app>    # are the claimed targets really wired?
  6. BUDGET    -> scripts/bundle_report.py <app>    # route JS / asset budgets
  7. RUNTIME   -> scripts/runtime_check.py --url ... --routes ... --healthz ...
  8. A11Y      -> scripts/a11y_audit.py --url ... --browsers chromium,firefox,webkit
  9. LH        -> scripts/lighthouse_run.py --url ... --routes ...
  10. SHOTS    -> scripts/capture_screenshots.py --root <app> --url <detected> --browsers ...
  11. README   -> rewrite per references/readme-standard.md; verify check_readme.py
  12. GATES A-M -> visual, perf, polish, lighthouse, security, a11y, seo, tests, reliability, docs, observability, cost
  13. VERIFY   -> scripts/verify_claims.py --root <app> --claims qa/claims.json --url <detected>
```

Apps whose server cannot start (no deps installed, missing env, external DB) are marked **SKIPPED (reason)** — not silently passed. The same applies to a gate whose tooling was missing: a skipped audit is `UNSUPPORTED`, never a pass.


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

| App | Port | Stack | Pre | Sec | Deps | README | Shots | Verified | Blockers |
|-----|------|-------|-----|-----|------|--------|-------|----------|----------|
| Lumen | 8807 | Vite | 11/30 | 4 med | clean | TODO | 0 | 9/13 | 2 |
| crypfeed | 9986 | Express | 18/30 | 0 | skipped | OK | 0 | 11/13 | 3 |

## Per-app findings
### <App>
- **Blockers**: ...
- **Fixed**: ...
- **Gates**: A PASS | B ... | L ...
- **Verification**: VERIFIED 12 | CONTRADICTED 0 | UNSUPPORTED 1 (gate L — no fallback documented)
- **Skipped**: gate I — health endpoint not reachable (app requires an external DB)
```

Report every app — including ones skipped, with the reason. A silent app is a hidden risk.


## Rules

- Never modify one app's config to satisfy another app's convention.
- Keep app-local changes inside that app's folder.
- The aggregate report lives at the workspace root, not inside apps.
- Re-running the sweep must be idempotent: detect existing screenshots and README sections before overwriting.
