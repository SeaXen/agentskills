# Absorbed reference knowledge

This folder holds the **reference material** of sibling skills that have no runnable script, copied in
so that `app-production-readiness` can review an app on its own. Every file carries a provenance header
("Absorbed from the sibling skill '<name>' ...").

**The sibling skills themselves were not deleted.** The copies are additive: if you remove
`D:\Repo\.agents\skills\<name>`, this skill keeps working (the copies are the source of truth here).

`MANIFEST.json` lists every copied file with its source skill, the original path and the size.

## What is here

| Skill | Copied | Used for |
|-------|--------|----------|
| `api-contract-testing` | 1 file | the API-contract family (Gate N) |
| `security-hardened-api` | 1 file | the API-hardening family (Gate E) |
| `observability-and-instrumentation` | 1 file | the observability family (Gate K) |
| `microservices-resilience` | 1 file | the resilience family (Gate I) |
| `ai-debt-detector` | 1 file | the AI-debt family (Gate U) |
| `property-based-testing` | 1 file | the test-quality family (Gate H) |
| `mutation-testing` | 1 file | the test-quality family (Gate H) |
| `web-design-guidelines` | 1 file | `scripts/web_guidelines.py` (Gate C) |
| `incident-postmortem`, `red-team-tactics`, `prisma-expert`, `typescript-expert`, `nodejs-best-practices`, `python-patterns`, `docker-expert`, `tailwind-patterns`, `site-specification`, `vercel-composition-patterns`, `vercel-react-view-transitions`, `sentry-cli`, `frontend-design`, `mobile-design` | 1-27 files | review reference material |

## How the rules are wired

`scripts/absorbed_rules.py` turns the checkable parts of those documents into six rule families that
run inside the existing gates:

| Family | Source skill | Where it runs | Severity |
|--------|--------------|---------------|----------|
| `api_contract_findings` | api-contract-testing | `business_logic_check.py` -> **Gate N** | MEDIUM |
| `api_hardening_findings` | security-hardened-api | `security_scan.py` -> **Gate E** | MEDIUM / HIGH |
| `observability_findings` | observability-and-instrumentation | `review.py` (advisory on **Gate K**) | LOW |
| `resilience_findings` | microservices-resilience | `review.py` (advisory on **Gate I**) | LOW |
| `ai_debt_findings` | ai-debt-detector | `code_quality.py` -> **Gate U** | LOW / MEDIUM / HIGH |
| `test_quality_findings` | property-based-testing, mutation-testing | `review.py` (advisory on **Gate H**) | LOW |

The K / I / H families are **advisory**: they are appended to the gate's evidence in the report but they
never change a verdict, because those gates have their own adversarial verifiers in `verify_claims.py`.

`scripts/web_guidelines.py` implements the machine-checkable subset of the Web Interface Guidelines
(29 rules over the UI files + 12 human-only checks). It fetches the upstream document, caches it under
`scripts/.cache/`, and falls back to the bundled snapshot in
`references/web-interface-guidelines.md` when the network is unavailable - in that case the rules that
are still available are applied and the run is reported honestly, never as a silent pass.

## Refreshing

```bash
python scripts/web_guidelines.py --refresh        # re-fetch the upstream guidelines
python scripts/absorbed/verify_manifest.py        # the copied *scripts* are still byte-identical
```

The copy in `references/knowledge/` is a snapshot; refresh it from the sibling skill when that skill
changes.
