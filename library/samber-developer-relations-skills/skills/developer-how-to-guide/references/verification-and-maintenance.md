# Verification and maintenance

How to prove a how-to works before it ships, keep it working after, and what the evidence says about task-oriented docs. Read this when running the pass threshold, writing the run list, setting up CI, or defending the work to a sceptical team.

Contents: cold-run protocol · run list · docs as tests · drift metadata · evidence base · sourced vs. baseline

## Cold-run protocol

A how-to is run by someone who matches the competence floor, on a setup shaped like a real reader's. That differs from a quickstart or tutorial run, which starts from a blank machine on purpose.

1. **Pick the runner.** Someone who meets every prerequisite and has not seen the draft. The author is the worst runner: they fill gaps from memory.
2. **Build the starting state from the prerequisites block only**, on a disposable account or environment seeded to the competence floor. Never the runner's production system. If the runner needs anything the block does not list, log it as a hidden prerequisite and stop.
3. **Run the recommended path end to end.** Record per step: what the page said, what happened, elapsed time, and any hesitation. Wait out any stated propagation delay before judging a check.
4. **Run each documented variant at least once.** A variant you cannot run leaves the page as a one-line out-of-scope note, and goes in the hand-over with the team that must test it.
5. **Re-run every step marked safe to re-run, on the finished state.** Each one that fails or does damage gets a "do not re-run" note or an idempotent command. Never re-run past the point of no return.
6. **Exercise the roll back section**, when the page has one, before and after the point of no return.
7. **Classify every defect**: hidden prerequisite, missing variant, unsafe step, no verification, teaching or reference inline, wrong scope. Fix, then rerun the affected steps.

## Run list

Hand this to the author whenever the page leaves your hands with `UNVERIFIED` markers. One list per page:

```
Environment:   <disposable account/cluster/project seeded to the competence floor>
Runner:        <who, matching the floor, has not seen the draft>
Capture:       <every UNVERIFIED block, by step number, with what to paste back>
Variants:      <each documented variant, with the environment it needs; run or drop>
Re-run:        <steps marked safe to re-run; repeat them on the finished state>
Roll back:     <exercise the section, before and after the point of no return>
Fill:          owner, tested_with, last_verified, every UNVERIFIED-LINK target
Product gaps:  <anything the page could not verify because the product lacks it>
```

## Docs as tests

Manny Silva's docsastests.com introduction frames the target: "Each doc is a test suite, each procedure a test case, each step an assertion," run "against your product. Not against mocks."

- Extract each copyable block and run it in CI against the released product, on a schedule as well as on docs commits: how-tos break when the product changes, not when the docs repo does.
- Assert the documented output, not just the exit code.
- Use a disposable account and fixture data; tear it down after the run.
- Mark any block CI cannot run (paid-only, hardware, third-party approval) as manually verified, with the date and version.
- Tools in this space parse procedures out of Markdown and run shell, HTTP and browser steps; language doctest frameworks cover SDK snippets. Pick whatever the docs stack already runs. Set-wide sample policy belongs to samber/developer-relations-skills@docs-code-sample-standards.

## Drift metadata

Stamp each page so staleness is visible without reading it:

- `owner`: a team, never a person.
- `tested_with`: the product or SDK version the steps last passed against; for a continuously deployed hosted product, the API version or the run date.
- `last_verified`: date of the last full run.

Then wire:

- A job that flags stale pages. This skill's baseline: two or more minor versions behind for versioned software; for unversioned hosted products, `last_verified` older than one quarter. Tune both to the release cadence.
- A path-based code-owner rule so changes to CLI flags, API schemas or config keys request a docs review.
- A re-run of every how-to at each minor release; the Good Docs Project's rule is "re-test instructions after every notable product release".
- A periodic cull: merge or delete pages with neither traffic nor an owner. Google's engineering documentation best practices ("Minimum Viable Documentation"): "A small set of fresh and accurate docs is better than a large assembly of 'documentation' in various states of disrepair."

## Evidence base

Use these when a team asks why a how-to should be stripped to action, or why it needs testing. Most of the evidence comes from learning material, so cite it for brevity and action-first writing, never as proof of a how-to-specific rule.

- **Carroll et al., "The Minimal Manual" (Human-Computer Interaction, 1987).** A task-oriented training manual under a quarter the length of the commercial one, tested on novices learning a word processor. Learners needed 40% less learning time and completed 2.7 times as many performance subtasks (experiment 1, N=19); 58% more subtasks in experiment 2 (N=32). In experiment 2, learners spent almost half their time recovering from errors, and the manual trained error recognition and recovery inline, though its error-recovery effects were mostly not significant in experiment 2. Cite it as consistent with a one-line failure branch, not as proof of one. Small lab studies: cite the direction, never the magnitude.
- **Scoring method worth copying.** Carroll scored success per subtask: correct if the learner used the right function to achieve the desired effect. That is a ready rubric for a moderated how-to test.
- **Lazonder and van der Meij (1993).** A randomised replication with 64 students; manual type did not interact with prior computer experience.
- **OASIS DITA 1.0 architectural specification.** Traces topic-oriented authoring for task and concept information to minimalism, and lists the principle "Document tasks, not tools or functions."
- **Aghajani et al. (ICSE 2020), two practitioner surveys (146 responses in total).** In Survey-I (78 respondents), clarity was rated important by 88% and erroneous code examples by 59%. Inappropriate installation instructions was the issue respondents encountered most often, which matters for standalone install how-tos. These are perceived-importance ratings, not measured outcomes.

## Sourced vs. baseline

| Item | Status |
| --- | --- |
| One goal per page; 8-10 step range | Sourced - Good Docs Project how-to guide |
| Title says what the guide shows; no gerund | Sourced - Diátaxis ("How to…"); Google, GitLab, Good Docs, Cloudflare (bare imperative) |
| One recommended path | Sourced - Google ("give only the best way"), Good Docs ("pick and only document the most common or recommended method") |
| Others via headings, tabs, pages or links | Sourced in part - Google ("separate them in different pages, headings, or tabs"), GitLab (most likely method first); the shape table is this skill's baseline |
| Conditional imperatives for forks | Sourced - Diátaxis |
| Verification before an irreversible closing step; warning before a destructive step | Sourced - Cloudflare how-to standard ("End in a fixed order: verification, then the irreversible closing step if there is one, then optional blocks, then Next steps") |
| A result or outcome block on task pages | Sourced - GitLab task result (optional); DITA `<result>` |
| Closing every page on a verification step; a separate checkpoint before the point of no return | This skill's baseline |
| Independent-read-path rule for verification | This skill's baseline |
| Variant-shape decision table and its ranking | This skill's baseline |
| Idempotency marking, preview-before-destroy, no bypass flags, roll back through system history, clean up section | This skill's baseline |
| Safeguard sub-step outside the step count | This skill's baseline |
| Seven-criterion pass threshold | This skill's baseline |
| Drift thresholds (two minor versions, one quarter) | This skill's baseline |
| KPI wiring costs | This skill's estimates |

Say which kind a rule is when you quote it to a team. A baseline offered as an industry standard gets the whole page discounted when someone checks.
