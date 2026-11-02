**Next action:** run the census on the Fernhill docs repo. Every number below is your estimate, not a measured count.

```
scripts/sample-audit.py <docs-dir> --format json --ext .md,.mdx > inventory.json
```

I have no access to Fernhill's repo, so I ran nothing. The plan rests on the assumptions listed under Assumptions and branches.

# Fernhill Cloud: plan to test 1,400 code samples

## Core finding

Test fewer samples by hand, and let mechanics cover the rest.

- **700 one-liners** are the ROT "trivial" class (redundant, outdated, trivial). Hand-testing them is the wrong move.
- **120 auth copies** are the "redundant" class. Collapse them to one canonical auth sample per tier-1 language, run in CI, and link every other page to it.
- **About 580 hand-written scenario samples** are where the real work is.

## What 80% means in arithmetic

Baseline: 1,400 samples, of which 700 are one-liners, 120 auth copies and about 580 other.

| Step | Corpus | Tested | Share |
|---|---|---|---|
| Collapse 120 auth to ~10 | 1,290 | 0 | 0% |
| Type-check 700 one-liners (Compile-only), run ~10 auth | 1,290 | ~710 | ~55% |
| Needed for 80% | 1,290 | 1,032 | 80% |

- Reaching 80% needs about 322 of the 580 scenario samples tested, which is about 55% of them.
- Cutting 100 trivial scenario samples lowers that to about 242 of 480 (50%).
- Mechanical work gets you to about 55%. The last 25 points need real work on the scenario samples.

**Report three numbers, not one.** Otherwise the headline is mostly compile-checked one-liners.

1. The 80% headline: share of samples at tier Run or Compile-only, executed by CI.
2. 100% of adoption-path samples (quickstart, auth, first call) at tier Run and green. This is a skill baseline.
3. Share of the ~580 scenario samples tested. Propose a floor with the team; I have no evidence for a specific number.

## Definition to get signed before work starts

> "Tested" = tier Run or Compile-only, executed by CI, last successful run inside the freshness window. Measured against an inventory dated `<date>`. Illustrative samples stay in the denominator.

- Without that clause, relabelling samples as "Illustrative" would raise the score without testing anything.
- Collapsing 120 auth copies shrinks the denominator. Show leadership both views: against the 1,400 baseline and against the new corpus.
- "80% tested" and "80% passing" are different numbers. Report both.
- 80% is this skill's baseline, not an industry standard. Do not present it as one.

## Methods used

- **Inventory before audit** (Nielsen Norman Group): mechanical census first, judgement second.
- **ROT triage** (redundant, outdated, trivial) as the first cut.
- **Docs as Tests** (Manny Silva): every documented step becomes a test.
- **Google Cloud ranked principles**: clarity → idiomaticity → consistency → simplicity → portability → maintainability. This settles whether the auth variants differ legitimately per language.

## Tier plan

Each sample gets one tier. Untiered samples default to Run, so silence fails loudly.

| Group | Tier | Mechanism |
|---|---|---|
| ~10 canonical auth + quickstart + first call | Run | Extract from tested source, published as a marked region |
| 700 one-liners | Compile-only | One extractor wraps each in a stub (client setup + call) and type-checks. They are uniform, so one job covers all |
| Destructive, billing or third-party scenario samples | Compile-only | Never Run, whatever the pipeline can do |
| Remaining scenario samples | Compile-only first, Run if copy-button counts are high | Test the embedded Markdown, with tier and fixture in the fence info string |
| Pseudocode, fragments, anti-patterns | Illustrative | Visible label on the rendered page |

- **Type-check caveat.** If a language's SDK is untyped, Compile-only for it only catches syntax errors. Say so in the report instead of counting it as strong.
- **Option for the 700.** If an OpenAPI spec and codegen exist, generate the snippets from the spec and type-check the output. That also gives free parity across languages.
- **Route out.** Endpoint-by-endpoint completeness of the reference pages belongs to `samber/developer-platform-skills@api-reference-quality`, not this plan.

## CI shape

1. Install the published SDK, never the working tree.
2. Split hermetic checks (every PR) from integration runs (nightly), because service-side drift is what breaks samples.
3. Run against a dedicated test project with prefixed, run-id-named resources and a scheduled sweeper. Secrets come from the CI store, never the sample.
4. Report per sample (page, line, owner), not per suite.
5. **Ratchet from day one.** Block any new untested sample and any previously green sample that goes red. Known failures go in an exceptions list with expiry dates. Flip to fully blocking at W7, so red never becomes background noise.

## Schedule

Assumes the goal ends 2026-12-31, which leaves seven working weeks before the holiday gap. Estimates assume one engineer plus you; adjust once the census lands.

| Week | Work | Est. effort |
|---|---|---|
| W1 (Nov 2–6) | Census; secret scan (report P0 now); ROT cut; tier assignment; definition signed | 3 days |
| W1–2 | Auth consolidation: ~120 → ~10 | 2–3 days |
| W2 | Compile-only harness (skill estimate: a couple of days) | 2 days |
| W2–3 | One-liner type-check job (or spec-generated snippets, ~1 week if codegen exists) | 2–5 days |
| W3–4 | Fixtures: test project, sweeper, secrets | ~1 week |
| W4–6 | Adoption path to Run; scenario samples to Compile-only; fix failures | Unknown until census |
| W7 (Dec 14–18) | Re-measure; flip gate to blocking; report | 2 days |

- Failure cleanup is the unbounded item. If the first run passes under 90%, stop new authoring and run a remediation sprint. That 90% gate is a skill baseline, not a vendor standard.
- For calibration only: public Stack Overflow Java snippets compile 1.00% of the time (MSR 2016) and 24.4% of public Python gists run (Gistable). Fernhill's corpus is governed, but its hand-written core is years old.

## Fix queue

P0 goes first on harm. Everything below it is ranked by readers affected × severity ÷ effort. This ratio starves low-traffic samples that need a harness, so promote adoption-path items by hand.

1. P0: credential-shaped literals, disabled TLS, unguarded destructive commands. The 120 auth copies are the likeliest place for a leaked key. **Owner:** SDK/API team. **Due:** this week.
2. Auth consolidation. **Owner:** docs.
3. One-liner type-check job. **Owner:** SDK team.
4. Adoption-path Run, with fixtures. **Owner:** docs plus SDK.
5. Scenario samples to Compile-only. **Owner:** product engineers, by surface.

## Ownership

Question to answer in writing: when a sample goes red on a Friday afternoon, whose queue does it land in? Proposal, pending your answer:

- **Generated or wrapped one-liners:** the SDK team owns the extractor. A red result is usually one fix to the wrapper.
- **Auth and quickstart:** docs.
- **Scenario samples:** the product engineers who shipped the feature.
- Encode it as code-owner rules and blocking checks. Do this after samples live in compilable source, not before.
- Fix SLA per surface: to be set by you. Bug fixes outrank new samples.

## KPIs per release

- Tested share and parity coverage.
- Mean time from red CI to merged fix.
- Support tickets quoting a sample verbatim.
- Samples older than the freshness window. I suggest setting the window to a multiple of the run interval, but that is your call.
- Rubric score per dimension, not the total.

## Assumptions and branches

I can't answer these from the repo. The first four decide the tier ranking.

| Question | If the answer is... | Plan changes |
|---|---|---|
| CI exists and has hours for a harness? | No | Run and Compile-only are deleted from the menu. Building a pipeline becomes queue item 1, and every sample stays "unverified" until it exists |
| Deadline? | Earlier than Dec 31 | Compile-only ships first and Run slips |
| Standing enforcement or one-off cleanup? | Standing | Run on the adoption path is promoted |
| Existing test suite samples can live in? | Yes | Run becomes nearly free |
| Which languages are published, and which is tier 1? | Unknown | Parity matrix (`T`/`P`/`M`/`S`) can't be built. Tier from download and ticket share |

- I assumed the 700 and 120 counts hold and the SDK is published. Each unverified assumption moves the arithmetic above.
- One decision for you: report the three numbers, or only the 80% headline? I recommend the three.

**Next:** paste the first lines of `inventory.json` summary (corpus size, language split, secret-scan hits), and I'll rerun the arithmetic with real counts.