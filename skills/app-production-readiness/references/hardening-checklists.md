# Gates E-M — Hardening Checklists

Each gate lists the **script that proves it** and the **evidence artifact** it produces.
A checklist item that no script or artifact backs is a claim, not a check.

> Before running any of these, scope the gates to the app:
> `python scripts/gate_scope.py --root <app_root>` — a gate the app cannot have
> is reported as skipped, never as a failure and never as a pass.

## Gate E — Security (scripts: security_scan.py, dep_audit.py, security_audit.py)
- [ ] Zero HIGH findings; MEDIUM reviewed and justified
- [ ] No secrets in repo; `.env` gitignored; `.env.example` has no real values
- [ ] No `eval` / `new Function` / shell exec in request paths
- [ ] TLS verification never disabled
- [ ] Cookies: httpOnly + secure + sameSite
- [ ] CORS explicit origins on authed routes (not `*`)
- [ ] Auth/authz checked server-side, not only client
- [ ] Inputs validated/sanitized; file uploads size+type limited
- [ ] Rate limiting on public/auth endpoints
- [ ] Dependency CVEs clean at or above the `--fail-on` threshold (default `high`)
- [ ] CVE scan actually **ran** — `dep_audit.py` exit 2 means "tool unavailable", i.e. UNVERIFIED

```bash
python scripts/security_scan.py <root>          # exit 1 on HIGH
python scripts/dep_audit.py <root>             # exit 1 on findings, 2 when the audit tool is missing
python scripts/security_audit.py --root <root>  # deep mode: qa/security/findings.json + coverage-ledger.json
```

Deep mode (`security_audit.py`) writes the security-audit schema: every finding is `confirmed`
(a credential committed to the source) or `needs_validation` (a pattern match that still has to be
traced to a boundary), and the coverage ledger records what was inspected. Both artefacts are
validated. Playbooks: [security/](security/README.md).

`security_scan.py` also covers the patterns that used to be missed: disabled signature
verification (`verify: false`, JWT `alg: none`), unsafe deserialisation (`pickle`, `yaml.load`),
`subprocess(..., shell=True)`, `exec()` on a string, MD5/SHA1 hashing, `innerHTML`/`document.write`,
string-built SQL, plain `http://` endpoints and `X-Powered-By`.

## Gate F — Accessibility (script: a11y_audit.py)
- [ ] Full keyboard-only pass, no traps
- [ ] Visible focus indicator on every interactive element
- [ ] Heading hierarchy h1 -> h2 -> h3, no skips
- [ ] Landmarks: header/nav/main/footer
- [ ] Contrast: text 4.5:1, large text 3:1, UI components 3:1
- [ ] Every input labeled; errors announced
- [ ] Images have meaningful alt (decorative = empty alt)
- [ ] `prefers-reduced-motion` respected
- [ ] axe/Lighthouse: no critical or serious violations

```bash
python scripts/a11y_audit.py --url <APP_URL> --routes /,/pricing --browsers chromium,firefox,webkit
```

Writes `qa/a11y/a11y-report.json` — axe-core violations (WCAG 2.1 A/AA + best practice) **plus** a
keyboard pass (focus visibility, tab order, accessible names, heading order, landmarks, skip link).
Exit `1` on critical/serious violations, `2` when Playwright/axe is unavailable.
If axe could not be injected (for example a strict CSP), the audit **fails** instead of reporting
zero violations.

## Gate G - SEO (scripts: runtime_check.py, seo_static.py)
- [ ] Unique title + meta description per route (title 10-70 chars)
- [ ] Open Graph + Twitter card tags
- [ ] Canonical URL; `lang` attribute set
- [ ] Exactly one `h1` per page; viewport meta present
- [ ] robots.txt + sitemap.xml present and correct
- [ ] 404 page returns a real 404 (not a soft 404); SPA fallback returns 200 HTML for deep links
- [ ] No console errors; no mixed content
- [ ] No wildcard CORS on `/api`
- [ ] Every page in the repository (not only the routed ones) has a description, OG tags and alt text

```bash
python scripts/runtime_check.py --url <APP_URL> --routes /,/pricing --healthz /healthz
python scripts/seo_static.py --root <app_root>          # static pages; exits 1 on a metadata gap (--strict also fails on GEO advice)
```

## Gate H — Tests (script: the app's own test command)
- [ ] `<PKG> test` passes, zero skipped, no `.only`
- [ ] Unit tests cover core logic
- [ ] API/integration tests for each route
- [ ] Build-output smoke test
- [ ] Critical paths covered
- [ ] CI workflow runs **both** build and test (preflight check)

`preflight.py` fails on `.only` / `.skip` / `xfail` and on a CI workflow that does not build and
test. `verify_claims.py` gate H **executes** the detected test command — a claim that the suite is
green is only accepted when the suite actually ran green.

## Gate I — Reliability (script: runtime_check.py)
- [ ] Every fetch/API call has error handling + timeout
- [ ] Retry/backoff on transient failures
- [ ] Error boundary at route level
- [ ] No unhandled promise rejections
- [ ] Loading / error / retry UI on async surfaces
- [ ] Graceful degradation if KV/R2/DB unavailable
- [ ] 404 + 500 pages styled
- [ ] Health endpoint returns 2xx with a small body; unknown route returns a real 404

## Gate J — Docs & DX (scripts: check_readme.py, preflight.py)
- [ ] README follows `readme-standard.md` exactly
- [ ] `.env.example` matches code usage **in both directions** (preflight cross-check)
- [ ] CONTRIBUTING.md, LICENSE present
- [ ] Clear commit/branch conventions

## Gate K — Observability (script: verify_claims.py gate K)
- [ ] Structured JSON logs in production
- [ ] Request IDs / correlation
- [ ] Error tracking (Sentry free tier or equivalent)
- [ ] `/healthz` (or `/api/health`) returns 200
- [ ] No secrets/PII logged
- [ ] Uptime check documented

Gate K needs **>= 3 independent source signals** (structured logging, request/correlation id, error
tracking, metrics, health endpoint, alerting, audit trail) before the verifier accepts the claim.
Fewer signals -> `CONTRADICTED`, and the missing signals are named in the evidence.

## Gate L — Free-tier cost (script: verify_claims.py gate L)
- [ ] Every service has a free tier; no paid-only API
- [ ] Documented limits with the date they were checked
- [ ] What breaks at limit + fallback documented
- [ ] Sleep/hibernation behavior noted for Railway/Render/Fly
- [ ] Cold-start impact measured and stated

Details: [free-tier-limits.md](free-tier-limits.md).

## Gate M — README & screenshots (blocking delivery gate)
Scripts: `check_readme.py <root>`, `capture_screenshots.py --root <root> --url <APP_URL> --routes ... --out docs/screenshots --browsers chromium,firefox,webkit`

### M1 — README structure
- [ ] Title + one-line pitch + who it's for
- [ ] Screenshots section near the top
- [ ] Features / highlights
- [ ] Quick start with one copy-pasteable command
- [ ] Environment variable table (every var in code present, and vice versa)
- [ ] Architecture overview
- [ ] Deploy instructions for every supported platform
- [ ] Scripts table
- [ ] Troubleshooting section
- [ ] Contributing, License, Support
- [ ] Free-tier limits + fallback table
- [ ] No `create-next-app` / scaffold boilerplate
- [ ] `check_readme.py` exits 0

### M2 — Screenshots (real, not placeholders)
- [ ] >= 3 real screenshots of the running app
- [ ] Hero/home shot at 1440px, 2x scale
- [ ] At least one feature-in-action shot
- [ ] Mobile shot at 390px
- [ ] `contact-sheet.png` generated and present
- [ ] `docs/screenshots/manifest.json` present, listing the engines that rendered the shots
- [ ] Every local image path in README resolves on disk
- [ ] Alt text describes the screen content
- [ ] Captions under each image
- [ ] No secrets, personal data, or fake placeholder art
- [ ] Screenshots regenerated after any UI change (no stale UI in docs)

### M3 — Multi-app consistency (workspace mode)
- [ ] All apps use the same README section order
- [ ] Same screenshot directory + naming convention
- [ ] Same env var naming for shared concepts
- [ ] Same deploy platform coverage
- [ ] Aggregate report lists every app, including skipped ones with reasons

## Depth gates N-U

Gates N-U (business rules, load/soak, migrations, privacy/GDPR, i18n/RTL, screen-reader contract, payment/email, code quality) are specified in [depth-gates.md](depth-gates.md). Each gate is proved by its own script and re-derived by `verify_claims.py`.

Three of them (C, N, Q) have a **human half** that no script can replace. Each needs a
fingerprint-bound sign-off record before the gate can be reported VERIFIED:

| Gate | Script | Sign-off record | Bound to |
|---|---|---|---|
| C design polish | `design_polish.py` | `qa/signoff/design.json` | the rubric measurement |
| N business rules | `business_logic_check.py` | `qa/signoff/business-rules.json` | the scenario spec + the rule docs |
| Q privacy/GDPR | `privacy_check.py` | `qa/signoff/privacy.json` | the policy file + the live policy route |

- [ ] `qa/signoff/design.json` exists, reviewer is named, verdict is `approved`, fingerprint matches the current rubric
- [ ] `qa/signoff/business-rules.json` exists and its fingerprint matches the current `qa/scenarios.json` + rule docs
- [ ] `qa/signoff/privacy.json` exists and its fingerprint matches the current policy
- [ ] The sign-off is a **human decision**, recorded with `--reviewer`, not a machine-generated default
