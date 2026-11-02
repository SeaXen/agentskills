## Kestrel Analytics: sample pipeline redesign

**First action:** run `scripts/sample-audit.py docs/ --format summary` on the docs repo. It gives the real census of the 240 samples and a secret scan. I had no corpus access, so every count below is unverified.

**Assumptions** (correct me if wrong): GitHub Actions, samples hand-pasted in Markdown, SDK on a public registry. I could not ask the interview questions. Q4, Q8, Q9 and Q10 would change the tier ranking, so answer those.

### Diagnosis: 4 defects, not 1 flaky job

1. **Builds SDK from monorepo working tree.** The job passes on code no reader can install yet. Readers get the published package. This is why the samples fail for readers while CI is red, and why CI would still fail them if it went green. Install the published artefact.
2. **One job mixes hermetic and integration checks, triggered on docs PRs.** Samples break when the service or SDK changes, not when the docs repo changes. Wrong trigger.
3. **`continue-on-error` since March.** An advisory job goes red and stays red. Four months of red means nobody has measured sample health since March.
4. **No teardown or sweeper.** Leaked test projects hit the quota. The skill names untended fixtures as the usual reason suites get disabled.

Root cause is leaked fixtures. Everything else (working-tree build, per-PR trigger, advisory status) made the failure invisible.

### New design: 4 jobs

| Job | Where | Trigger | Runs | Blocks |
|---|---|---|---|---|
| **A. Hermetic** | docs repo | every PR | Secret scan, metadata schema, referenced-file check, snippet-sync check, compile-only tier against the **pinned published SDK** from the registry. Run-tier samples run against a mock or local stub where one exists. | **Required check.** No staging, no quota. Target: minutes. |
| **B. Integration** | docs repo | nightly, SDK release published, staging deploy | Run tier against staging, with the **latest published SDK** installed from the registry | Docs deploy (see gating below) |
| **C. Pre-release canary** | SDK monorepo | SDK PRs | Samples against the **working-tree build** | SDK PR. This is where the working-tree build belongs. It tells the SDK team "this change breaks docs" before release. |
| **D. Sweeper** | docs repo | hourly | Deletes every resource named `docs-ci-<runid>-*` older than 2h | Nothing. Alerts if it deletes more than N, because that means teardown is broken. |

Optional extension to B: a PR that edits Run-tier samples also runs just those samples, capped at one concurrent run. Skip it until the quota is stable.

**Fixture rules** (fix the March cause first):
- Dedicated CI organisation or project per language, never a shared human account. Ask for a raised quota there.
- Every resource is named `docs-ci-<runid>-<sample_id>`, so the sweeper can identify it safely.
- Teardown goes in `finally`, and the sweeper catches what teardown misses.
- Preflight check: fail fast on quota with an `infra` label. Retry once on `infra` errors only, never on assertion failures. Quota errors then stop looking like sample failures.
- Secrets come from the CI secret store. The sample shows `<YOUR_API_KEY>`.

**Skeleton for B:**
```yaml
on:
  schedule: [{ cron: "0 3 * * *" }]
  repository_dispatch: { types: [sdk-released, staging-deployed] }
concurrency: { group: docs-samples-integration, cancel-in-progress: false }
jobs:
  run-samples:
    steps:
      - run: pip install kestrel-sdk   # registry package, never the monorepo path
      - run: ./ci/run-samples.sh --tier run --prefix docs-ci-${{ github.run_id }}
      # no continue-on-error anywhere
```
The monorepo release workflow and the staging deploy workflow send the `repository_dispatch` events.

### Tiers: classify all 240 before changing CI

Untiered samples default to Run, so today every sample claims "works as written". Assign exactly one tier each:

- **Run:** quickstart, auth, first call, and the samples readers copy most (use copy-button counts if the docs platform has them). Output is asserted.
- **Compile-only:** samples that bill, destroy data or call a third party, plus most of the rest. Compile-only needs no fixtures and no credentials, and catches removed symbols and missing imports.
- **Illustrative:** pseudocode and fragments. Label them visibly on the rendered page.

Apply ROT triage first (redundant, outdated, trivial) and delete what fails. A deleted sample costs a reader nothing. An untested one costs them an afternoon.

### Gating, ownership, freshness

- **PR gate:** job A is a required check. Nothing else blocks PRs.
- **Deploy gate:** the docs deploy fails if job B is red for a sample on a page in that deploy's diff. A red sample on an untouched page opens an issue instead, so one stale sample does not freeze all docs.
- **Reporting:** per sample, giving page, line and owner. Not "suite failed".
- **Owners:** the **SDK team owns Run-tier samples**, because SDK releases and service changes are what break them. The **docs team owns Markdown, Compile-only and Illustrative.** A Friday-afternoon red sample opens an issue assigned through CODEOWNERS and the sample's metadata owner. These owners are my proposal to confirm.
- **Fix SLA** (my picks, not standards): quickstart or auth path 2 business days, everything else 5. Bug fixes outrank new samples.
- **Freshness window:** a sample whose last successful run is older than 7 days gets a "not verified since <date>" badge on the page. 7 days is my starting point given a nightly run. Your release cadence decides the real number.
- **Flaky sample:** quarantine it with an expiry date and an owner. Never use `continue-on-error`.

### Rollout: 5 steps, each makes the next cheaper

1. **Census and secret scan** (about 1 hour to run; triage depends on findings). Fix any credential leak first.
2. **Fixture fix** (my guess: 1–2 engineer days): CI org, naming prefix, teardown, sweeper, preflight. Gate: **3 consecutive green nightly runs.**
3. **Split the job** into A and B, install from the registry, add the dispatch triggers. Measure the first real pass rate. Four months of red hides it.
4. **Turn on enforcement:** make A required, wire the deploy gate, and **delete `continue-on-error`.** Doing this before step 2 only makes everything red again.
5. **Move samples into compilable source**, published by transclusion with region tags and metadata. This is the highest-leverage step for the whole corpus, but it comes after the quick wins. Assign CODEOWNERS on those paths only once the paths are stable.

### Pass threshold

Skill baselines, not industry standards. Override them with your own data:

- Zero P0 findings, and 100% of adoption-path samples at tier Run and green.
- Compile/run pass rate of at least 90%. Below that, stop new authoring and run a remediation sprint.
- At least 80% of the corpus at tier Run or Compile-only and executed by CI.
- Deprecated-API rate below 43%. This one has a measured comparator (Zhou and Walker, FSE 2016), but using it as a gate is this skill's choice. Above 43%, build a deprecation-detection gate first.

**KPIs:**
- Mean time from a red sample to a merged fix.
- Reader issues quoting a sample verbatim. Count the last 4 months now as your baseline.
- Tested-sample share per release.
- Number of samples past the freshness window.

**Next:** run the census (step 1) and paste the summary. I will rank the fix queue and tier each sample from it.