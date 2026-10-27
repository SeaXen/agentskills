# Verification — re-deriving every claimed PASS

A review is only worth as much as its evidence. `scripts/verify_claims.py` ignores the prose in a
report and **re-derives each claimed gate** from artifacts on disk and from a fresh run of the
relevant check. It is the last step of the workflow and the reason the skill's output can be trusted.

> **One command does the whole thing:** `python scripts/review.py --root <app> --serve` runs the
> gates, then judges them with *these same verifiers* and writes `qa/report.md`. A report produced
> that way can never contain a PASS the tooling did not prove.

## Usage

```bash
# 1. write down what you are claiming
#    qa/claims.json
#    { "gates": { "A": "PASS", "B": "PASS", ... } }
#    (a flat { "A": "PASS" } mapping is accepted too)

# 2. let the verifier re-check every claim
python scripts/verify_claims.py --root <app_root> --claims qa/claims.json --url <APP_URL>
```

The markdown report format is also accepted directly, so a written report can be verified as-is:

```
GATES      : A visual PASS | B perf PASS | C polish PASS | D lighthouse PASS | ...
```

| Flag | Meaning |
|------|---------|
| `--root <path>` | The app under review (default `.`) |
| `--claims <file>` | JSON claims file or the markdown report to verify |
| `--url <url>` | Live base URL — required for the runtime gates (G, I) |
| `--routes /,/a` | Routes to re-check |
| `--healthz /healthz` | Health endpoint for the reliability gate |
| `--skip-tests` | Do not re-run the test command (gate H becomes UNSUPPORTED) |
| `--test-timeout 600` | Seconds before the test run is killed |
| `--artifact-dir <dir>` | Extra directory to read review artefacts from (repeatable). Also `QA_ARTIFACT_DIRS` (path-separator separated) |
| `--json` | Machine-readable payload on stdout |

Exit `0` = every claimed PASS is supported. Exit `1` = at least one claimed PASS is contradicted or
unsupported.

### Where artefacts are read from

Artefacts are read from the **reviewed app root** (`docs/screenshots/manifest.json`,
`qa/lighthouse/lighthouse-summary.json`, `qa/a11y/a11y-report.json`).

The current working directory is deliberately **not** an implicit fallback: a stale report left over
from a different project would otherwise be able to "verify" a gate for an app it has nothing to do
with. If the evidence genuinely lives outside the repo (a separate review workspace), name it
explicitly:

```bash
python scripts/verify_claims.py --root <app_root> --claims qa/claims.json \
    --artifact-dir D:/reviews/my-app
```

Write the artefacts **into the app repo** whenever you can (`qa/` is git-ignored in the skill repo but
should be committed in the app) — it keeps the evidence next to the code it describes.

## Verdict vocabulary

| Verdict | Meaning | Ship? |
|---------|---------|-------|
| `VERIFIED` | The evidence re-derived from scratch supports the claim | yes |
| `CONTRADICTED` | The evidence exists and **disproves** the claim | no — fix it |
| `UNSUPPORTED` | There is **no evidence** for the claim (artifact missing, tool unavailable, checks skipped) | no — a claim without evidence is not a pass |
| `UNVERIFIABLE` | The gate needs a human decision (design polish, business rules, legal wording) | only with a valid human sign-off record (`qa/signoff/design.json`, `qa/signoff/business-rules.json`, `qa/signoff/privacy.json`) |
| `NOT_APPLICABLE` | The app has no such surface (no database, no payments, no UI) - see gate scoping below | n/a - it was never a gate for this app |
| `NOT_CLAIMED_PASS` | The gate was not claimed as PASS — nothing to verify | n/a |

### UNSUPPORTED vs CONTRADICTED (the rule that keeps the review honest)

`CONTRADICTED` means **the evidence exists and disproves the claim**. `UNSUPPORTED` means **there is
no evidence either way**. A measurement that could not be taken (the app was unreachable, the server
died mid-run, Lighthouse hit an npm lock race, the build produced no output, the audit tool is
missing) is `UNSUPPORTED` — never `CONTRADICTED`. The gates implement this:

| Situation | Verdict | Example evidence |
|-----------|---------|------------------|
| app unreachable during the load run | `UNSUPPORTED` | "the app was not reachable during the load run - the measurement was skipped" |
| Lighthouse could not measure a route | `UNSUPPORTED` | "the Lighthouse run could not be measured - npm error code ECOMPROMISED" |
| scenario spec could not be executed | `UNSUPPORTED` | "no executable contract to verify - the app was not reachable" |
| the test command ran 0 tests | `CONTRADICTED` | "npm test exited 0 but ran 0 tests - the project has no effective test suite" |
| the measurement succeeded and the app is wrong | `CONTRADICTED` | "p95 1441 ms > 1000 ms" |

If you see a gate contradicted by a message about reachability, an error string from the toolchain or
a missing score, that is a **bug in the review**, not a defect in the app — fix the tooling, do not
"fix" the app.

## Gate scoping (why a gate can be NOT_APPLICABLE)

Before a claimed PASS is checked, `gate_scope.py` classifies the app from repository evidence
(frameworks, dependencies, source files, database folders) and decides, per gate, whether it
`applies`, is `conditional`, or `not_applicable`:

```bash
python scripts/gate_scope.py --root <app_root>       # the scope table
python scripts/gate_scope.py --root <app_root> --json
```

A claimed PASS on a `not_applicable` gate comes back as `NOT_APPLICABLE` - a skip, not a failure
and not a pass. `--no-scope` turns the scoping off (every claimed PASS is then verified).
Scoping never hides a contradiction: the classification comes from the code, not from the report.

## How each gate is re-derived

| Gate | Evidence the verifier looks for |
|------|----------------------------------|
| A visual | `docs/screenshots/manifest.json` with **>= 2 browser engines**; one engine only → CONTRADICTED ("not cross-browser") |
| B perf | re-runs `bundle_report.py`; any budget failure → CONTRADICTED |
| C polish | re-runs `design_polish.py`; a failing rubric → CONTRADICTED. A passing rubric is `UNVERIFIABLE` **unless** a valid human sign-off exists in `qa/signoff/design.json` (reviewer, `approved`, date, matching score, matching rubric fingerprint) — then it is VERIFIED |
| D lighthouse | re-reads `qa/lighthouse/lighthouse-summary.json` and re-applies the thresholds (90/95/95/90) |
| E security | re-runs `security_scan.py`; any HIGH finding → CONTRADICTED; a CVE scan whose **tool** was unavailable (`npm audit`, `pip-audit`, … missing or offline) → the gate is UNSUPPORTED, because "zero HIGH vulnerabilities" could not be re-derived; a project with **no dependency manifest at all** → VERIFIED with the note "no dependency manifest to audit" |
| F a11y | re-reads `qa/a11y/a11y-report.json`; any critical/serious violation → CONTRADICTED |
| G seo | re-runs the live SEO/metadata checks **and** the static page audit (`seo_static.py`); missing title/description/og/canonical → CONTRADICTED |
| H tests | **actually executes** the detected test command (`npm/pnpm/yarn test`, `pytest`, `go test`, `cargo test`); no test command at all → CONTRADICTED ("the project ships no detectable tests"); non-zero exit → CONTRADICTED; exit 0 with **0 tests executed** → CONTRADICTED ("a green command that ran nothing is not evidence"); only an *unparsable* test count → UNSUPPORTED |
| I reliability | prefers `qa/deploy-smoke.json` (the app was started with the platform's own start command and probed); otherwise hits the live health endpoint; non-2xx or unreachable → CONTRADICTED |
| J docs | re-runs `check_readme.py`; failing checks → CONTRADICTED |
| K observability | counts the source signals it actually finds — structured logging (a log sink **and** a structured payload in the same file), request/correlation id, error tracking, metrics, health endpoint, alerting, audit trail; **>= 3** required; fewer → CONTRADICTED and the missing signals are named, so the evidence and the advisory can never contradict each other |
| L cost | README must document free-tier limits **and** the fallback behaviour; limits without fallback → CONTRADICTED |
| M readme+shots | >= 3 screenshots **and** `contact-sheet.png` present in the README assets |
| N business rules | re-runs `business_logic_check.py` (static smells + executed `qa/scenarios.json` + API contract) **and** requires a valid domain sign-off in `qa/signoff/business-rules.json` (reviewer, `approved`, date, fingerprint matching the current scenario spec + rule documents). Machine half ok, no/stale sign-off → UNVERIFIABLE; the sign-off is what turns it into VERIFIED |
| O load & soak | re-runs `load_check.py` against the live URL; adds the soak time series from `qa/load.json` (worst drift) as evidence |
| P migrations | prefers `qa/migrations.json` (a real apply → rollback → re-apply on a throwaway database); otherwise re-runs the static `migration_check.py` |
| Q privacy | re-runs `privacy_check.py` (policy, consent, PII in logs/storage/analytics) **and** requires a valid legal sign-off in `qa/signoff/privacy.json` (reviewer, `approved`, date, legal basis, fingerprint matching the current policy file + route). Machine half ok, no/stale sign-off → UNVERIFIABLE |
| R i18n | re-runs `i18n_check.py` (locales, missing keys, i18n mechanism, RTL) |
| S assistive tech | re-runs `at_check.py` (labels, live regions, landmarks, titles, alt text) |
| T payment & email | prefers `qa/payment-email-live.json` (a live test-mode round-trip); otherwise re-runs the static `payment_email_check.py` |
| U code quality | re-runs `code_quality.py` (complexity, duplication, dead code, AI-risk markers + lint/type signals) |

### The deep modes behind those gates

Gates C, I, O, P and T can be proven by running something, not by reading
something. The scripts that do it are documented in
[deep-modes.md](deep-modes.md): `deploy_smoke.py`, `migration_apply.py`,
`load_check.py --soak`, `payment_email_live.py`,
`design_polish.py --record-signoff`,
`business_logic_check.py --record-signoff` and
`privacy_check.py --record-signoff`. Their artefacts live in the app under
review (`qa/deploy-smoke.json`, `qa/migrations.json`, `qa/load.json`,
`qa/payment-email-live.json`, `qa/signoff/design.json`) and are read by the
verifier from the app root only — the same anti-stale rule as every other
artefact.

## Identity cross-check

The verifier fetches the live URL and checks that it actually mentions the project name from
`package.json`. If the running app is *not* the app under review (wrong port, wrong service,
stale deployment), gates **G** and **I** are forced to `CONTRADICTED` and the report prints:

```
identity: MISMATCH - live URL does not mention project 'my-app' - it is probably not the app under review
```

This catches the most common false PASS of all: auditing the wrong running service.

## What the verifier does NOT cover

Be honest about these in the report — they need a human or another tool:

- business-logic correctness, load/stress behaviour, migration safety
- privacy/GDPR/retention policy, licensing of bundled assets
- i18n/RTL correctness, real screen-reader testing (axe covers much, but not all)
- payment, email and third-party OAuth flows end-to-end
- design polish (Gate C) and copy quality

Mark these as `SKIPPED (reason)` or attach manual evidence — never silently PASS them.

## Anti-grade-inflation rules

1. Every gate in the final report must point at an artifact or a script run.
2. A tool that could not run (`exit 2`) means the gate is `SKIPPED`, never `PASS`.
3. A gate verified only by re-reading your own report is `UNSUPPORTED`.
4. If a claim cannot be verified, downgrade the claim — do not downgrade the verifier.
## The absorbed doc-skill families (advisory vs blocking)

Some sibling skills had no runnable script, only documents. Their checkable rules were turned into
six families in `scripts/absorbed_rules.py` and wired into the gates that already own the topic:

| Family | Source skill | Runs in | Effect on the verdict |
|--------|--------------|---------|----------------------|
| `api_contract_findings` | api-contract-testing | `business_logic_check.py` (Gate N) | MEDIUM/HIGH -> the gate can fail |
| `api_hardening_findings` | security-hardened-api | `security_scan.py` (Gate E) | MEDIUM/HIGH -> the gate can fail |
| `ai_debt_findings` | ai-debt-detector | `code_quality.py` (Gate U) | MEDIUM/HIGH -> the gate can fail |
| `observability_findings` | observability-and-instrumentation | `review.py` (Gate K) | LOW -> **advisory**, evidence only |
| `resilience_findings` | microservices-resilience | `review.py` (Gate I) | LOW -> **advisory**, evidence only |
| `test_quality_findings` | property-based-testing, mutation-testing | `review.py` (Gate H) | LOW -> **advisory**, evidence only |

Advisory means: the observation is printed in the report, but the gate keeps the verdict its own
adversarial verifier produced. The reference material behind each family is copied into
`references/knowledge/<skill>/` (see `references/knowledge/README.md`).

`scripts/web_guidelines.py` adds the Web Interface Guidelines (29 machine rules + 12 human-only
checks) to Gate C through `design_polish.py`. High-severity violations can fail Gate C; medium ones
are warnings; the 12 human-only checks are printed as a checklist because no script can judge them.
