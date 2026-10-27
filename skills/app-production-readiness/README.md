# App Production Readiness

[![CI](https://github.com/SeaXen/app-production-readiness/actions/workflows/tests.yml/badge.svg)](https://github.com/SeaXen/app-production-readiness/actions/workflows/tests.yml)
[![Python](https://img.shields.io/badge/python-3.10%2B-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)

**An agent skill that takes any app — TypeScript, Python, Go, Rust, or a static site — and proves it is ready to ship, then makes it portable to localhost, Docker, Vercel, Netlify, Railway, Render, Fly.io and the Cloudflare free tier.**

It runs **21 quality gates**, and then does the thing most review skills skip: **it re-derives every claimed PASS from the evidence on disk.** A gate you forgot to run, an artifact you never produced, a claim you made from memory — all of it comes back as `CONTRADICTED`.

```
claimed 21 | verified 21 | contradicted 0 | unsupported 0 | unverifiable 0
```

---

## Why this exists

Most "production readiness" checklists are prose. You tick the boxes yourself, and the report says what you wanted it to say. This skill is different:

| | Typical review skill | This one |
|---|---|---|
| Gates | prose checklists | 21 gates, each with a script, an artifact and a proof line |
| Scoring | self-graded | adversarial re-verification from artifacts |
| A missed check | invisible | `UNSUPPORTED` / `CONTRADICTED` |
| Tool missing | silently "passes" | exit code `2` = **SKIPPED**, never a pass |
| Wrong app | undetected | identity cross-check against the live URL |
| Irrelevant gates | forced on everything | adaptive scoping per app type |

> A green run means **"no rule fired"**, not "the app is perfect". It is the strongest automated gate you can put in front of a release — and it tells you exactly which parts still need a human.

---

## Install

### As an agent skill (recommended)

```bash
git clone https://github.com/SeaXen/app-production-readiness.git \
  ~/.claude/skills/app-production-readiness        # Claude Code
# or
git clone https://github.com/SeaXen/app-production-readiness.git \
  ~/.agents/skills/app-production-readiness        # OpenCode / agent skills
```

Then ask your agent:

```
/app-production-readiness APP_URL=http://localhost:3000 ROUTES=/,/pricing
```

The skill is fully self-contained — it needs no other skill installed.

### As a standalone CLI

```bash
git clone https://github.com/SeaXen/app-production-readiness.git
cd app-production-readiness
python scripts/bootstrap_env.py                 # audit environment (Playwright, browsers, Node, Lighthouse)
python scripts/bootstrap_env.py --install       # auto-install missing dependencies
python scripts/skill_check.py --root .          # health-check the package itself
python -m pytest scripts/ -q                    # run the test suite
```

### Requirements

| Need | Used for | If missing | Auto-installer |
|---|---|---|---|
| Python 3.10+ | everything | required | — |
| Node.js 18+ | app builds, `npm audit` | gates degrade to SKIPPED | — |
| `playwright` (pip) + browsers | screenshots, axe audit | those gates SKIP, honestly | `python scripts/bootstrap_env.py --install` |
| Chrome/Chromium | Lighthouse | Lighthouse SKIPs (or uses `npx lighthouse`) | `python scripts/bootstrap_env.py --install` |
| Docker | container deploy mode | static/runtime mode is used instead | — |
| `psql` | Postgres migration round-trip | sqlite round-trip is used instead | — |

---

## Quick start

### 1. One-command review (The Orchestrator)

```bash
# Start the app, measure it, judge every gate with adversarial verifiers,
# and write qa/report.md + qa/summary.json
python scripts/review.py --root . --serve

# Apply safe mechanical fixes first (.env.example, .dockerignore, robots.txt, LICENSE, security headers)
python scripts/review.py --root . --serve --fix

# Against an already running server
python scripts/review.py --root . --url http://127.0.0.1:3000
```

### 2. Autonomous Remediation (The Auto-Fixer)

```bash
# Automatically remediate detected blockers from qa/report.md
# Applies atomic codemods for XSS innerHTML, CORS, touch targets, focus outlines,
# empty catch blocks, and generates AI agent recipes for complex function refactoring
python scripts/remediate.py --root .

# Revert changes if needed
python scripts/remediate.py --root . --rollback
```

`--serve` starts the app with the platform start command, falls back to the dev
server when there is no production build, and says so in the report - a dev
server means every live number is a dev measurement.

### Step by step

```bash
# 0. What kind of app is this? Which of the 21 gates even apply?
python scripts/gate_scope.py --root .

# 1. Environment discovery (port, URL, package manager, framework, routes, healthz)
python scripts/detect_env.py .

# 2. File/config preflight (up to 30 checks)
python scripts/preflight.py .

# 3. Security + dependency CVEs
python scripts/security_scan.py .
python scripts/dep_audit.py .

# 4. Bundle budgets
python scripts/bundle_report.py .

# 5. Live checks (start your app first)
python scripts/runtime_check.py --url http://127.0.0.1:3000 --routes /,/pricing --healthz /healthz

# 6. Browser gates
python scripts/a11y_audit.py   --url http://127.0.0.1:3000 --routes /,/pricing --browsers chromium,firefox,webkit
python scripts/lighthouse_run.py --url http://127.0.0.1:3000 --routes /,/pricing
python scripts/capture_screenshots.py --root . --url http://127.0.0.1:3000 --routes /,/pricing --out docs/screenshots --browsers chromium,firefox,webkit

# 7. Write your report (qa/claims.json), then have the skill audit you
python scripts/verify_claims.py --root . --claims qa/claims.json --url http://127.0.0.1:3000
```

`verify_claims.py` is the heart of the skill: it re-runs the gates itself and compares them to what you claimed.

```json
{ "gates": { "A": "PASS", "B": "PASS", "C": "PASS" } }
```

---

## The 21 gates

| Gate | What it proves | Script |
|---|---|---|
| **A** | Cross-browser visual QA (Chromium, Firefox, WebKit) + manifest | `capture_screenshots.py` |
| **B** | Performance: route JS ≤ 200 kB gz, no asset > 50 kB, no shipped source maps | `bundle_report.py` |
| **C** | Design polish: 7-dimension measured rubric **+ named human sign-off** | `design_polish.py` |
| **D** | Desktop Lighthouse: Perf ≥ 90, A11y ≥ 95, BP ≥ 95, SEO ≥ 90 | `lighthouse_run.py` |
| **E** | Security: zero HIGH findings, dependency CVEs, deep security-audit mode | `security_scan.py`, `dep_audit.py`, `security_audit.py` |
| **F** | WCAG 2.1 AA: axe-core + a keyboard pass, multi-engine | `a11y_audit.py` |
| **G** | SEO/meta on every page + live header/SEO/health checks | `seo_static.py`, `runtime_check.py` |
| **H** | Tests actually exist and actually run | `verify_claims.py` (Gate H verifier) |
| **I** | Reliability: the app **boots the way the platform boots it** and `/healthz` answers | `deploy_smoke.py` |
| **J** | Docs & DX: README vs production standard, env table, screenshots | `check_readme.py` |
| **K** | Observability: structured logging, request ids, error tracking, health | `verify_claims.py` (Gate K verifier) |
| **L** | Free-tier cost: documented limits **and a fallback** | `check_readme.py` + `references/free-tier-limits.md` |
| **M** | README + ≥ 3 real screenshots + contact sheet | `check_readme.py` |
| **N** | Business rules: executed contract **+ domain sign-off** | `business_logic_check.py` |
| **O** | Load & soak: p95, error rate, **soak time series + drift** | `load_check.py` |
| **P** | Migrations: **apply → roll back → re-apply** on a throwaway DB | `migration_apply.py` |
| **Q** | Privacy/GDPR: policy, consent, PII handling **+ legal sign-off** | `privacy_check.py` |
| **R** | i18n & RTL: locales, key parity, mechanism, `lang`, logical CSS | `i18n_check.py` |
| **S** | Assistive-tech contract: labels, live regions, landmarks, titles | `at_check.py` |
| **T** | Payment & email: card data, webhook signature, currency, idempotency | `payment_email_check.py` |
| **U** | Code quality & AI-risk debt: complexity, duplication, dead code, empty catches | `code_quality.py` |

### Adaptive scoping — not every app has every gate

`gate_scope.py` classifies the app from repo evidence and decides what applies:

| App kind | Gates that run |
|---|---|
| Static site | 13 run · 5 conditional · 3 skipped (no migrations, payments, privacy surface) |
| API / backend service | 10 run · 2 conditional · 9 skipped (no visual, a11y, Lighthouse, SEO, AT gates) |
| Full-stack app | 21 run |

A skipped gate is reported as `NOT_APPLICABLE` — a skip, never a silent pass and never a failure. Use `--no-scope` to run everything anyway.

---

## Deep modes (the part most skills skip)

Static analysis tells you a Dockerfile *exists*. These modes prove it *works*.

```bash
# Boot the app exactly like the platform does (runtime / static / docker) and probe it
python scripts/deploy_smoke.py --root . --healthz /healthz

# Apply, roll back and re-apply every migration on a throwaway database
python scripts/migration_apply.py --root . --pg-url postgres://...

# A real test-mode Stripe charge and a real email — live keys are refused
python scripts/payment_email_live.py --root .

# A soak time series with drift and error-rate-growth detection
python scripts/load_check.py --url http://127.0.0.1:3000 --duration 10 --soak 60 --soak-interval 10
```

See [`references/deep-modes.md`](references/deep-modes.md) for the full runbook.

---

## Human sign-offs (fingerprint-bound)

Three gates involve things a machine cannot judge — design taste, business intent, legal wording. Instead of waving them through, the skill requires a **named human decision that is bound to the exact content reviewed**:

```bash
python scripts/design_polish.py --root . --record-signoff \
  --reviewer "Ada Lovelace" --verdict approved --notes "typography and spacing reviewed"

python scripts/business_logic_check.py --root . --url http://127.0.0.1:3000 --record-signoff \
  --reviewer "billing-owner" --verdict approved --rules-ref "docs/rules.md#R1-R4"

python scripts/privacy_check.py --root . --url http://127.0.0.1:3000 --record-signoff \
  --reviewer "dpo@example.com" --verdict approved --legal-basis "GDPR Art.13"
```

Records land in `qa/signoff/*.json` and carry a **fingerprint** of what was reviewed. Edit the rules, the scenario spec, the policy or the rubric and the approval is void — the gate drops back to `UNVERIFIABLE` until someone signs off again. You cannot rubber-stamp a stale review.

---

## Report format

```
APP      : https://my-app.example.com
SCOPE    : 21 gates apply · 0 conditional · 0 skipped
GATES    : A visual PASS | B perf PASS | C design PASS | ... | U quality PASS
EVIDENCE : qa/lighthouse/lighthouse-summary.json, qa/a11y/a11y-report.json, docs/screenshots/manifest.json, qa/security/findings.json
SUMMARY  : 21/21 gates pass · 0 blocking findings
```

The `GATES` line is machine-readable — feed it straight back into `verify_claims.py`.

---

## Workspace mode

```bash
python scripts/scan_workspace.py D:\my-monorepo     # discover every app root
```

Then run the per-app pipeline for each one and roll the results up into a single table (Pre / Sec / Deps / Verified).

---

## Self-test

The skill ships its own test suite and a package health-check:

```bash
python -m pytest scripts/ -q     # 346 tests
python scripts/test_preflight.py # 30 preflight checks
python scripts/skill_check.py --root .            # package health
python scripts/absorbed/verify_manifest.py        # absorbed-code integrity
```

---

## Absorbed skills

This package **contains** the functionality of these skills — you do not need them installed:

`frontend-design` · `mobile-design` · `i18n-localization` · `api-patterns` · `database-design` · `seo-fundamentals` · `geo-fundamentals` · `webapp-testing` · `lint-and-validate` · `nextjs-react-expert` · `performance-profiling` · `testing-patterns` · `vulnerability-scanner` · `review-team` (reviewer prompts in `references/panel-review/`) · `security-audit` (schema, validators and playbooks in `references/security/`)

They live in `scripts/absorbed/` with a sha256 manifest (`scripts/absorbed/MANIFEST.json`) proving exactly what was taken and from where.

---

## Repository layout

```
SKILL.md                  the skill definition (gates, workflow, report format)
README.md                 this file
assets/                   README template for the app under review
references/               depth gates, checklists, deploy matrix, free-tier limits,
                          verification, deep modes, panel review, security playbooks
scripts/                  50+ stdlib-only tools (review, remediation, bootstrap, gates)
scripts/absorbed/         14 third-party engines + sha256 manifest
scripts/security_audit_pack/  security-audit schema + validators
scripts/fixtures/         sample app generator (good + deliberately broken variants)
```

Everything runs on the Python standard library. Nothing is fetched at runtime except the optional axe-core CDN download (cached locally).

---

## Exit-code contract

| Code | Meaning |
|---|---|
| `0` | pass |
| `1` | fail — blocking findings exist |
| `2` | **skipped** — the tool could not run (missing dependency, nothing to measure) |

Exit code `2` is never a pass. If a gate could not be measured, the report says so.

---

## License

MIT — see [LICENSE](LICENSE).
