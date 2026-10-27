# Deep modes â€” turning judgement calls into evidence

The static gates read the code. The deep modes **run** it. Five gaps used to be
"a human has to trust this"; now each one has a script, an artefact, and an
exit code.

| Gap it closes | Script | Artefact | Feeds |
|---|---|---|---|
| "the deploy config looks right" | `scripts/deploy_smoke.py` | `qa/deploy-smoke.json` | Gate I |
| "the migrations look reversible" | `scripts/migration_apply.py` | `qa/migrations.json` | Gate P |
| "load is fine" | `scripts/load_check.py --soak` | `qa/load.json` | Gate O |
| "payments and email work" | `scripts/payment_email_live.py` | `qa/payment-email-live.json` | Gate T |
| "design looks good" | `scripts/design_polish.py --record-signoff` | `qa/signoff/design.json` | Gate C |
| "the rules are the intended ones" | `scripts/business_logic_check.py --record-signoff` | `qa/signoff/business-rules.json` | Gate N |
| "the policy is lawful" | `scripts/privacy_check.py --record-signoff` | `qa/signoff/privacy.json` | Gate Q |

All of them obey the skill-wide exit-code contract:

```
0 = the evidence says yes
1 = the evidence says no
2 = nothing could be attempted (SKIPPED - never a pass)
```

---

## 1. Deploy smoke â€” does the app actually boot?

`deploy_verify.py` parses `Dockerfile`, `vercel.json`, `netlify.toml`,
`fly.toml`, `render.yaml`, `Procfile` and the package scripts. This one
**starts the app the way the platform would** and probes it.

```bash
python scripts/deploy_smoke.py --root <app_root> --healthz /healthz
```

Three modes, chosen from the repo:

| Mode | When | What it does |
|---|---|---|
| `runtime` | a start command exists (package.json `start`, Procfile `web:`, `render.yaml` `startCommand`, `fly.toml` `[processes]`, Dockerfile `CMD`) | starts the command with `PORT` set to a free port, waits for the port, then requests the health endpoint and every main route |
| `static` | the platform only serves a build output (`vercel.json` `outputDirectory`, `netlify.toml` `publish`) | serves the directory and requests the routes |
| `docker` | a Dockerfile exists **and** Docker is installed | `docker build` + `docker run` with the exposed port mapped |

A runtime server always wins over a static directory: that is what the
platform will actually run.

Options:

```bash
--port 8080            # use a fixed port instead of a free one
--boot-timeout 60      # how long the app may take to open the port
--build "npm run build" # run an explicit build step first
--remote --remote-url https://my-app.vercel.app   # probe a real deployment
```

`--remote` uses the platform CLI when it is installed and authenticated.
Without one the mode reports **SKIPPED**, never a pass.

---

## 2. Migration apply â€” do the migrations really run?

```bash
python scripts/migration_apply.py --root <app_root>            # SQLite (default)
python scripts/migration_apply.py --root <app_root> --pg-url postgresql://...
```

It discovers the migration folder (`db/migrate`, `migrations`,
`db/migrations`, `sql/migrations`, `database/migrations`, `src/db/migrate`),
pairs `NNN_x.sql` with `NNN_x.down.sql` (also `.rollback.sql`, `_down.sql`,
and the `.up.sql` spelling), and then:

1. applies every migration in order on a throwaway database,
2. rolls them back in reverse order,
3. re-applies the whole chain on a **fresh** database (it must work from zero),
4. runs the chain a second time to report idempotency.

Steps 2-4 are what a static SQL review cannot tell you.

* SQLite is the default because it is always available and needs no server.
* PostgreSQL is used when `--pg-url` is given **and** `psql` is installed; a
  throwaway database is created and dropped again.
* A missing rollback file is a blocking failure, not a warning.

---

## 3. Soak â€” is the tail still healthy after the run?

```bash
python scripts/load_check.py --url http://127.0.0.1:3000 --routes / \
    --duration 10 --soak 120 --soak-interval 10 --soak-drift 50
```

The soak is a **time series**, not two runs: the window is measured
repeatedly, and the verdict compares the average p95 of the first third with
the average p95 of the last third. The error-rate trend is checked as well.

The full series is written to `qa/load.json` (`soak[].series`), so a reviewer
can see the shape of the run, not just the verdict.

---

## 4. Live payment and email â€” does it work end to end?

```bash
export STRIPE_SECRET_KEY=sk_test_...          # test mode only
export RESEND_API_KEY=re_...
export QA_TEST_EMAIL=you@example.com
python scripts/payment_email_live.py --root <app_root>
```

* Stripe: creates a PaymentIntent (100 cents, USD) through the Stripe API.
* Email: sends one real message through Resend to `QA_TEST_EMAIL`.
* A **live** key (`sk_live_`, `rk_live_`) is refused â€” the script must never
  move real money. That refusal is a blocking failure.
* Without credentials nothing is sent and the mode is **SKIPPED** (exit 2).

Never commit these keys: put them in the environment, not in `.env`.

---

## 5. The design sign-off â€” where the human decision lives

The rubric can only measure what a machine can see. Taste is not
machine-checkable, so the human decision is **recorded**, not forgotten in a
chat transcript:

```bash
python scripts/design_polish.py --root <app_root> --record-signoff \
    --reviewer "Ada Lovelace" --verdict approved \
    --notes "hierarchy and rhythm are good, contrast is fine"
```

That writes `qa/signoff/design.json`:

```json
{
  "reviewer": "Ada Lovelace",
  "date": "2026-10-21",
  "verdict": "approved",
  "notes": "hierarchy and rhythm are good, contrast is fine",
  "rubric_score": 0.92,
  "rubric_threshold": 0.85,
  "fingerprint": "0a6b8ff08b0c8eeef0541a45b93432a1",
  "tool": "app-production-readiness design_polish.py"
}
```

The record is **bound to the measurement**: the fingerprint is a hash of the
score and the per-dimension scores. A sign-off is rejected when

* the reviewer is missing,
* the verdict is not `approved`,
* the date is missing, unparsable or in the future,
* the recorded score does not match the current rubric score (Â±0.02),
* the fingerprint does not match the current measurement.

So a sign-off can never be carried over to a version of the UI it never saw.

Effect on the report:

| Situation | Gate C verdict |
|---|---|
| rubric fails | CONTRADICTED |
| rubric passes, no sign-off | UNVERIFIABLE (with the exact command to record one) |
| rubric passes, valid sign-off | VERIFIED |
| rubric passes, invalid sign-off | UNVERIFIABLE, with the reasons listed |

---

## 6. The domain and legal sign-offs â€” gates N and Q

Two gate questions are *not* software questions:

| Gate | The machine half proves | The human half proves |
|---|---|---|
| **N** business rules | the code implements the written rules (scenarios executed against the running app + API contract + static smells) | the written rules are the **intended** ones (product owner) |
| **Q** privacy | the code respects consent, logging and storage rules, and a policy exists | the policy text is **lawful** and complete (legal/owner) |

Both halves are required for a PASS. Record them like the design sign-off:

```bash
python scripts/business_logic_check.py --root <app_root> \
    --record-signoff --reviewer "Product Owner" --verdict approved \
    --notes "rules match spec v3" --rules-ref "SPEC-42"

python scripts/privacy_check.py --root <app_root> \
    --record-signoff --reviewer "Legal" --verdict approved \
    --notes "Art.13/17 covered" --legal-basis "GDPR Art.13"
```

That writes `qa/signoff/business-rules.json` and `qa/signoff/privacy.json`:

```json
{
  "reviewer": "Product Owner",
  "date": "2026-10-21",
  "verdict": "approved",
  "notes": "rules match spec v3",
  "fingerprint": "f523b574c30913e1233b6f3868218594",
  "subject": ["qa/scenarios.json", "docs/rules.md"],
  "rules_ref": "SPEC-42",
  "tool": "app-production-readiness/signoff"
}
```

The **fingerprint is a hash of the content that was reviewed**:

* Gate N â†’ the scenario spec (`qa/scenarios.json`) **and** the rule
  documents (`docs/rules.md`, `business-rules.md`, `domain-rules.md`, â€¦).
* Gate Q â†’ the policy file(s) **and** the live policy route.

Change one of those files and the fingerprint no longer matches, so the
approval is rejected and the gate drops back to UNVERIFIABLE. That is the
whole point: *a sign-off can never drift onto content it never saw.*

Effect on the report:

| Situation | Gate N / Q verdict |
|---|---|
| the machine half fails (a scenario fails, PII in logs, â€¦) | CONTRADICTED |
| the machine half cannot run (no scenario spec, no --url) | UNSUPPORTED |
| machine half passes, no sign-off | UNVERIFIABLE, with the command to record one |
| machine half passes, valid sign-off | VERIFIED |
| machine half passes, stale sign-off | UNVERIFIABLE, "the fingerprint does not match" |

Rejection rules (same for all three sign-offs): no named reviewer, a
verdict other than `approved`, a missing/unparsable/future date, or a
fingerprint that does not match the current content.

---

## 7. `--serve` - the skill starts the app for you

Half of the gates need a running app.  Before, the operator had to start it by
hand - which meant the review silently could not finish exactly when the app
was broken, the case where you most want evidence.

```bash
python scripts/serve.py --root <app_root>            # start, print the URL, stop again
python scripts/serve.py --root <app_root> --wait     # keep it running until Ctrl+C
python scripts/serve.py --root <app_root> --dev      # force the dev server
```

How it chooses:

| Situation | What it runs | `dev_mode` |
|-----------|--------------|------------|
| a production build exists | the platform start command (`package.json` `start`, `Procfile` `web:`, `render.yaml`, `fly.toml`) | false |
| no production build, a dev script exists | the dev server | **true** |
| neither | nothing - the result is a **SKIP**, never a pass | - |

The mode is recorded, because a dev server changes the numbers: a dev bundle
is bigger, the HMR client adds console noise, and hot-reload makes latency
look different.  The report says "DEV SERVER - every live number below is a
dev measurement" whenever that is true.

The server is always stopped again when the caller finishes, so a review never
leaves stray processes behind.

---

## 8. `--fix` - writing the mechanical fixes

A review that only complains is half a tool.  These fixes are the ones where
the correct answer is unambiguous and the change cannot alter behaviour the
author did not intend.

```bash
python scripts/fixes.py --root <app_root>                          # all fixes
python scripts/fixes.py --root <app_root> --only env-example,next-viewport
python scripts/review.py --root <app_root> --serve --fix            # fix, then review
```

| Id | What it writes | Guard |
|----|----------------|-------|
| `env-example` | `.env.example` with every variable the source actually reads | never overwrites an existing value; only missing variables are added |
| `gitignore-env-example` | `!.env.example` in `.gitignore` | only when the ignore rules really would swallow the template |
| `next-viewport` | `export const viewport` in the Next.js root layout | only for Next.js App Router, only when there is no viewport export |
| `vercel-framework` | the `"framework"` key in `vercel.json` | only when the framework was detected and the key is missing |
| `next-security-headers` | the standard security headers in `next.config.*` | only when the config shape is recognised and no `headers` exist |

Every rule is idempotent - running it twice changes nothing - and every edited
file is copied to `qa/fix-backup/<path>` first, so a fix can be undone
(`git diff` shows it too).

What `--fix` deliberately does **not** do: rewrite the README, pick a licence,
add tests, change logic, or decide anything about the design. Those stay
recommendations in the report, because a human has to own them.

---

## What the deep modes still cannot do

Honesty is part of the contract:

* `deploy_smoke.py` boots the app **locally**. A real free-tier deployment can
  differ (cold starts, provider env vars, DNS). Use `--remote --remote-url`
  against the deployed URL for that.
* `migration_apply.py` runs against SQLite or a throwaway PostgreSQL database.
  It does not validate your production data or your backup.
* `load_check.py` drives load from one machine. It is not a distributed load
  test.
* `payment_email_live.py` proves the integration works once, in test mode.
  It does not prove your retry, refund or dunning logic.
* The sign-off proves that a human looked. It does not make the design good.
