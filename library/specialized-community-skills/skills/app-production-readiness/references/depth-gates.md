# Depth gates (N-U) - the ones that catch real incidents

Gates A-M ask "is this shippable?". Gates N-U ask "will this page when
something real happens to it?". Each gate has one script, a fixed set of
rules and a machine-readable verdict.

| Gate | Script | Verdict contract |
|------|--------|------------------|
| N business rules: executable contract + domain sign-off | `business_logic_check.py` | static smells + executed scenarios + `qa/signoff/business-rules.json` |
| O load & soak | `load_check.py` | p50/p95/p99, rps, error rate, drift |
| P migrations & schema | `migration_check.py` | rollback, destructive DDL, idempotency |
| Q privacy & GDPR: policy + legal sign-off | `privacy_check.py` | policy, consent, PII handling + `qa/signoff/privacy.json` |
| R i18n & RTL | `i18n_check.py` | locales, keys, language, RTL |
| S screen-reader contract | `at_check.py` | labels, live regions, landmarks, titles |
| T payment & email flows | `payment_email_check.py` | card data, webhook signature, mail safety |
| U code quality & AI risk | `code_quality.py` | complexity, duplication, dead code |

All of them follow the exit-code contract: `0` pass, `1` fail, `2` skipped
(the tool or the evidence was unavailable - never a pass).

## N - business logic & API contract

Declare the rules you actually care about in `qa/scenarios.json`:

```json
{ "scenarios": [
  { "name": "checkout rejects an empty cart",
    "method": "POST", "path": "/api/checkout", "body": { "items": [] },
    "expect_status": 400, "expect_json": { "error": "empty_cart" } }
]}
```

`expect_json` uses dotted paths (`0.name`, `error.code`). The gate also flags
empty catch blocks, swallowed promise rejections, `if (true)` without an exit,
`process.exit` inside a request handler, loose `== null`, and a missing
central error handler.

**Two halves, two owners.** The machine proves *the implementation matches the
rules you wrote down*. Only a domain owner can prove *those rules are the ones
the business intends*. So gate N has two halves:

| Half | Who | Evidence |
|---|---|---|
| executable contract | machine | `qa/scenarios.json` executed against a live app + static smells |
| domain sign-off | human | `qa/signoff/business-rules.json` |

Record the human half once the executable contract passes:

```bash
python scripts/business_logic_check.py --root . --url http://127.0.0.1:3000 \
    --record-signoff --reviewer "billing-owner" --verdict approved \
    --rules-ref "docs/rules.md#R1-R4"
```

The record is bound to a **fingerprint** of the scenario spec *and* the rule
documents. Edit either one and the approval is void - `verify_claims.py` drops
gate N back to `UNVERIFIABLE` instead of accepting a stale sign-off. A missing
sign-off is never a failure; it is an honest "a human still has to confirm
this".

## O - load & soak

```bash
python scripts/load_check.py --url <APP_URL> --routes /,/api/items \
    --duration 10 --soak 30 --p95 1000 --error-rate 1 --rps 20
```

Default thresholds: p95 <= 1000 ms, error rate <= 1 %, optional minimum
throughput. The soak phase compares the first and the last third of the run -
a p95 that grows by more than 50 % is a leak, a cold cache or a rate limiter
and it fails the gate.

## P - migrations & schema

Rules: every migration has a rollback path (a `down`/`rollback` file, a
`downgrade()` function or a paired `001_init.down.sql`); destructive DDL is
guarded; DDL is idempotent (`IF EXISTS` / `IF NOT EXISTS`); versions are
unique; a declared schema exists so drift is visible. A project **without**
migrations exits `2` - the gate was not checked, it did not pass.

## Q - privacy & GDPR

A privacy policy must exist as a file or a route and be linked from the app.
Non-essential trackers need a consent gate. Personal data (e-mail, phone,
name, address, card, token) must not be written to logs, cached in
`localStorage`/`sessionStorage`, or handed to an analytics call. A deletion or
export path must exist.

**Policy vs law.** The machine can see that a policy exists, that it is linked
and that the app does not leak PII. It cannot tell you whether the text is
*lawful*. That is a legal sign-off, exactly like gate N's domain sign-off:

```bash
python scripts/privacy_check.py --root . --url http://127.0.0.1:3000 \
    --record-signoff --reviewer "dpo@example.com" --verdict approved \
    --legal-basis "DPA-2026-04"
```

The record lands in `qa/signoff/privacy.json`, bound to a fingerprint of the
policy files and the live policy route, so editing the policy voids the
approval.

## R - i18n & RTL

More than one locale, catalogues with the same key set, a real i18n mechanism
(`t()`, `useTranslation`, `gettext`), a declared document language, and - when
an RTL language ships - `dir` switching plus logical CSS properties
(`margin-inline-start`, not `margin-left`).

## S - assistive technology contract

axe proves an element is technically accessible; a screen reader needs the
information, the order and the announcements. The gate checks programmatic
labels, errors wired to their field (`aria-describedby`), live regions for
async updates, DOM focus order, no focusable element hidden with
`aria-hidden`, a skip link, a `<main>` landmark, a unique `<title>` per page,
named buttons/links/images and table header scopes. E-mail templates are
documents, not pages, and are skipped.

## T - payment & email flows

Payments: no raw card data collected by your own code, webhook signatures
verified, integer minor units, an explicit currency, an idempotency key,
credentials from the environment. Email: a real provider, send failures
surfaced, no header injection through string concatenation, an unsubscribe path
for marketing mail, templates instead of inline HTML, no hardcoded keys.

## U - code quality & AI risk

Functions over 80 lines, over 5 parameters, nested deeper than 4 levels,
duplicated blocks, dead markers (TODO/FIXME/placeholder/mock) left in shipped
code, mutable default arguments, bare `except`, empty catch blocks,
commented-out code and files over 600 lines. The absorbed `lint_runner.py`,
`type_coverage.py` and `react_performance_checker.py` add a second opinion.

## The panel review

After the scripts are green, run the reviewer prompts in
[panel-review/](panel-review/README.md) - one subagent per reviewer. A
`CONTRADICTED` verdict from a reviewer downgrades the matching gate until it
is fixed or explicitly waived in the report.
