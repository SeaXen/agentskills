# Redesign: documentation samples CI for Kestrel Analytics

## Diagnosis

The current job has four problems. Fixing only the quota would still leave the other three.

| # | Problem | Effect |
|---|---|---|
| 1 | It builds the SDK from the monorepo working tree. | Readers install the published SDK, so CI tests code they never run. Unreleased SDK changes can also fail docs PRs. |
| 2 | It runs all 240 samples against shared staging on every PR. | Concurrent PRs compete for the same quota, and runs are slow. A docs typo fix pays the full cost. |
| 3 | Leaked test projects are cleaned up by nothing. | This is the root cause of the March flakiness. Quota exhaustion looks like a sample failure. |
| 4 | `continue-on-error` has left the job red for four months. | It carries no signal, so nobody notices when a sample really breaks. Readers find the breakage first. |

## Target design: four tiers, each with one question

| Tier | Trigger | Question it answers | Blocks merge? | Target time |
|---|---|---|---|---|
| 1. Static and hermetic | Every docs PR | Do all 240 samples compile, type-check and run against a recorded or mock API? | Yes | < 5 min |
| 2. Live, changed samples only | Docs PR touching sample files | Do the samples I changed work against real staging? | Yes | < 10 min |
| 3. Full live, published artifacts | Nightly, plus on every SDK release and API deploy | Do all 240 work for a reader today? | No. A failure files an issue and pages the owner. | < 40 min, sharded |
| 4. Unreleased SDK canary | Nightly, and from the monorepo CI on SDK PRs | Will the next SDK release break samples? | Blocks the SDK release, not docs PRs | < 40 min |

**The core change:** the monorepo working tree moves out of the docs PR path. Docs PRs test against the pinned published SDK. Tier 4 covers "will the next SDK break docs", and it runs where the SDK changes.

## Tier details

### Tier 1: static and hermetic (required)

1. Pin the published SDK version in a lockfile in the docs repo. Renovate or Dependabot bumps it automatically, and each bump PR triggers Tier 2 for all samples.
2. Compile and type-check every sample. Lint it. Run it against a mock server generated from the OpenAPI spec, or against recorded fixtures. This is the only tier where all 240 run on every PR.
3. Verify that every code block in the docs comes from a tested sample file, using region markers such as `// docs:start quickstart` and `// docs:end quickstart`. CI fails on any hand-pasted code block. This removes drift between the docs page and the tested file.
4. Check links, and check that every sample has an ID, an owner, and an expected-output assertion.

### Tier 2: live, changed samples only (required)

1. Compute the changed sample set from the PR diff. If the lockfile or shared fixtures changed, run all samples.
2. Run them against staging with these isolation rules:
   - Namespace every resource as `ci-<run_id>-<sample_id>`, and label it `owner=docs-ci`, `expires=<now+2h>`.
   - Put the run in a `concurrency: group: staging-docs-ci` group so runs queue instead of exhausting quota together.
   - Put teardown in an `if: always()` step, so cancelled and failed runs still clean up.
3. Use a dedicated CI organization on staging with its own quota, separate from engineering's shared staging. This is the cheapest durable fix for the March incident.

### Tier 3: nightly full live run (the reader-facing truth)

1. Install the published SDK exactly as the quickstart tells readers to. Run at the minimum and latest supported language runtime versions.
2. Shard the 240 samples into about 8 shards. Retry each failed sample once. Report "failed then passed" as a flake metric rather than hiding it.
3. Open or update a single tracking issue per failing sample, labelled `sample-broken` with the sample ID. Close it automatically when the sample passes again.
4. Post a one-line summary to the team channel: `231/240 pass, 3 quarantined, 6 failing (new: 1)`.

### Tier 4: unreleased SDK canary

1. Run the same sample suite against an SDK built from the monorepo `main`, nightly.
2. Also call the suite from the monorepo's SDK PR pipeline as a required check on public-API changes.
3. A failure here means "fix the SDK or update the docs before release". It never shows up as red on an unrelated docs PR.

## Fixing the quota at the source

1. **Janitor job.** It runs hourly and deletes every resource labelled `owner=docs-ci` whose `expires` is in the past. It also runs after each Tier 2 and Tier 3 run. This backstops teardown that never ran.
2. **Preflight.** Before any live run, check remaining quota. If it is below the threshold, run the janitor once and re-check. If it is still low, fail with a distinct status, `INFRA: quota`, and a different exit code from sample assertion failures.
3. **Failure classification.** Samples and the harness report one of `PASS`, `SAMPLE_FAIL` or `INFRA_FAIL`. Only `SAMPLE_FAIL` blocks a PR. `INFRA_FAIL` is retried, then alerts the platform owner. This is what keeps one outage from erasing the signal again.
4. **Resource budget.** Each sample declares its quota use. Most should share one setup project per shard, created and deleted by the harness. Samples that need their own project are tagged and run serially.

## Restoring trust: migration plan

| Step | Action | Done when |
|---|---|---|
| 1 (day 1) | Remove `continue-on-error`. Move the current job to non-required, on a schedule only, so PRs stop seeing red. | PRs are no longer red by default. |
| 2 (week 1) | Run one baseline Tier 3 pass. Sort all 240 samples into passing, broken or flaky. | A table of 240 rows exists. |
| 3 (week 1-2) | Fix or delete every broken sample. Put anything unresolved in `quarantine.yml` with an owner and an expiry date of 14 days or less. | Every failure is fixed, deleted or owned. |
| 4 (week 2) | Ship the janitor, the CI org, the preflight and failure classification. | Quota failures no longer appear as sample failures. |
| 5 (week 2-3) | Ship Tier 1. Make it required once it has been green for 7 days. | Tier 1 is required. |
| 6 (week 3) | Ship Tier 2. Make it required once it has been green for 7 days. | Tier 2 is required. |
| 7 (week 4) | Ship Tier 4. Wire it into the SDK release checklist. | SDK releases are gated on the canary. |

Quarantine rules:

- Quarantined samples still run, but their result does not block anything.
- An expired quarantine entry fails Tier 1, so the list cannot grow silently.
- A quarantined sample on a published page gets a visible "may be out of date" banner until it is fixed or removed.

## Closing the loop with readers

1. Add a "Report a problem with this sample" link to every sample, prefilled with the sample ID, page URL and SDK version.
2. Use an issue template that asks for SDK version, runtime and the error. Triage maps each issue to a sample ID.
3. If the sample passes in Tier 3 but a reader reports a failure, the test is missing something. Add a regression sample or assertion. Treat this as a CI gap, not a closed-as-works-for-me issue.
4. Publish a "last verified" date and SDK version on each page, taken from the latest passing Tier 3 run.

## Targets and metrics

- Tier 3 pass rate is 98% or higher over a rolling 7 days, excluding quarantined samples.
- Median PR check time is under 5 minutes for Tier 1 and under 10 minutes for Tier 2.
- A broken sample is fixed, quarantined with an owner, or unpublished within 5 business days of the first nightly failure.
- Infra failures are under 2% of runs. Track the flake rate separately from the real failure rate.
- Count reader-reported sample issues per month. If the pipeline works, this should fall.

## Sketch of the workflow (GitHub Actions assumed)

```yaml
# .github/workflows/samples-pr.yml
on: pull_request
concurrency:
  group: samples-pr-${{ github.ref }}
  cancel-in-progress: true
jobs:
  static:                      # Tier 1, required
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - run: make samples-install   # published SDK, from lockfile
      - run: make samples-check     # compile, type-check, lint, snippet-sync
      - run: make samples-mock      # all 240 against the mock server
  live-changed:                # Tier 2, required
    needs: static
    runs-on: ubuntu-latest
    concurrency: { group: staging-docs-ci, cancel-in-progress: false }
    steps:
      - uses: actions/checkout@v4
      - run: make samples-install
      - run: make quota-preflight
      - run: make samples-live CHANGED_ONLY=1 RUN_ID=${{ github.run_id }}
      - if: always()
        run: make samples-teardown RUN_ID=${{ github.run_id }}
```

The nightly workflow uses `on: schedule` and `on: repository_dispatch`. The dispatch is sent by the SDK release job and the API deploy job. It shards with a `matrix` and runs the tracker-issue step last.

## Decisions I need from you

1. **CI system.** I assumed GitHub Actions. If you use something else, the structure carries over and the YAML does not.
2. **Mock fidelity.** Is there an OpenAPI spec accurate enough to generate a mock server? If not, Tier 1 needs recorded fixtures, which is more work up front.
3. **Staging quota.** Can you get a separate CI organization on staging? Without one, Tier 2 and Tier 3 need serialization and a stricter janitor, and they will be slower.
4. **Ownership.** Who owns each sample? The quarantine and issue-routing steps depend on a named owner per sample.