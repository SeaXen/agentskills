# Voltmesh sample testing tiers

**Today CI can enforce nothing for any of the four.** You have no pipeline and no engineering hours for six weeks. The skill removes Run and Compile-only from the menu for a team in that position. Until a pipeline exists, all 160 samples are *unverified*, not passing. The tiers below are the commitments to publish now, and CI enforces them once the pipeline exists.

I did not run `scripts/sample-audit.py`, because I don't have your docs directory. I also never got answers to the interview questions on dates and standing enforcement (Q9 and Q10). I assumed no hard deadline and a standing standard, and I used the constraints you gave for Q4 and Q8.

## Tier per sample

| Sample | Tier | Why | What CI enforces once a pipeline exists |
|---|---|---|---|
| (a) Quickstart auth call | **Run** | It is on the primary adoption path. It is free, non-destructive and uses your own service, so nothing rules Run out. | Full execution against the real API with a dedicated test account. The key comes from the CI secret store, and the sample shows `<YOUR_API_KEY>`. It asserts the documented output. It runs per pull request (hermetic) and on a nightly schedule, because the service changes independently of the docs. It is a required check that fails the docs build. |
| (b) Transcription job at $0.90/min | **Compile-only** | A sample that bills has no Run tier, whatever the pipeline can do. | Build or type-check against the published SDK, never executed. No credentials and no spend. The page is labelled "valid; not run for you". |
| (c) `kubectl delete namespace voltmesh-dev` | **Compile-only** (see the P0 note below) | A sample that destroys has no Run tier. | Lint the shell syntax. Validate the command shape with `kubectl ... --dry-run=client` (no cluster needed). The CI job never gets cluster credentials. |
| (d) Post to a third-party partner webhook | **Compile-only** | A sample that depends on a third party has no Run tier. Automated traffic to their endpoint may break their terms, and a Run job would hold a secret to reach it. | Build or lint the request only, with no network call. |

**P0 note on (c):** a destructive command with no guard is a P0 finding on harm alone, outranking everything else in the queue. Before any tooling exists, add three things:
- a visible warning;
- a context check, for example `kubectl config current-context` before the delete;
- an explicit statement that the command is irreversible.

If the team won't maintain the dry-run check, relabel (c) **Illustrative**, which is excluded from CI and visibly labelled on the page. Don't leave it unlabelled.

## What the six weeks can do without engineering time

1. **Run the census (docs team, no CI needed).** Execute `scripts/sample-audit.py <docs-dir> --format summary` and then `--format json`. This gives the real corpus size, the secret-scan findings and the P0 candidates. Treat each flag as a candidate to confirm, not a verdict.
2. **Triage with ROT (redundant, outdated, trivial).** Cut dead and trivial snippets. Fewer samples means a smaller test job later, and a deleted sample costs a reader nothing.
3. **Tier all 160 samples on paper.** Anything you leave untiered defaults to Run, so classify explicitly. Label the unrunnable ones Illustrative on the page. Use the same rules as above:
   - Billing, destructive and third-party samples go to Compile-only.
   - Quickstart, auth and first-call samples go to Run.
4. **Fix the P0s by hand.** That covers credential-shaped literals, unguarded destructive commands, prompt characters and plausible fake keys.
5. **Put the policy in writing.** Name an owner for a red sample, because "whose queue does a Friday-afternoon red sample land in" needs a concrete answer. Set a freshness window measured from the last successful run.

## First engineering ask when hours free up (about a few days)

1. Stand up **one compile-only job** that installs the published SDK. It covers (b), (c) and (d), and it catches the whole class of removed symbols and missing imports with no fixtures or credentials.
2. Add **one Run job** for the quickstart and auth path only. It needs a test account, a CI secret, teardown and a nightly schedule.

I'd start with compile-only because it is cheap. The Run job is a standing cost: a red build every time the service moves. It earns its place on (a) because a wrong quickstart costs a reader their afternoon.

## Pass thresholds to report against

These are skill baselines, not industry standards. The 43% deprecated-API gate is the exception: it comes from a measurement by Zhou and Walker (FSE 2016).
- Zero P0 findings, and 100% of adoption-path samples at Run and green.
- A compile/run pass rate of at least 90%.
- At least 80% of the corpus tiered Run or Compile-only and executed by CI.

If the 80% target can't be met, cut samples rather than lowering the bar.