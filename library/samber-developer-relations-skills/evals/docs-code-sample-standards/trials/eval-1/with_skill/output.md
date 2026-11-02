I read the skill and its references. I didn't write the report you asked for, because two things in the brief fail the skill's own rules. The deliverable below is the honest version.

**Your conclusion.** Your spot-check is the negative example in `audit-method.md`. The twelve most-visited pages are also the most-maintained, so they are the healthiest part of the corpus. Nothing was compiled, so reading catches only visible defects. A corpus-wide verdict from a convenience sample is the error the skill exists to prevent. Four broken samples in the healthiest region is also a warning sign, not reassurance.

**Your opener.** The skill lists "94% of developers consider API documentation quality a key factor" under claims to never repeat. It is attributed to SlashData but not confirmed in any SlashData report. In a leadership document, an unsourced stat can discredit the whole report and the budget ask with it. I replaced it with a sourced one.

---

# Code Sample Quality: Status and Request

**Halyard Data Docs · 2026-10-30 · Draft for leadership**

## Why this matters

Uddin and Robillard surveyed 323 professional developers (IEEE Software, 2015). They found ambiguity, incompleteness and incorrectness to be the most severe API-documentation problems, and six of the ten problem types they documented were rated outright blockers. Code samples are where those defects get executed instead of read. A reader pastes a broken sample into their own codebase.

## What we know

- **Scope checked.** Last Thursday I read every code block on our 12 most-visited docs pages.
- **Result.** I found and fixed 4 clearly broken samples.
- **Limits of this check.**
  - These are our most-maintained pages.
  - Nothing was compiled or run, so only defects visible to the eye were caught.
  - It did not cover the API reference, the examples repo, or the less-visited pages.
- **The storage pages.** I have no evidence that the issues are confined to them. I haven't compared them against other areas.

## What we don't know

- How many samples we publish, in which languages and on which surfaces.
- What share compiles or runs.
- Whether any sample contains a credential-shaped string or an unguarded destructive command.
- How many samples call APIs we have since removed or deprecated.
- Who owns a sample when it breaks.

**Conclusion.** Sample quality is unmeasured. The one check we did found real defects in our best-maintained pages. I can't tell you the corpus is in good shape, and I can't tell you it isn't.

## Proposed measurement (about one week)

1. **Census of 100% of samples.** Run `scripts/sample-audit.py <docs-dir> --format summary` across the docs site, API reference and examples repo. Record the file, language, surface and last-commit date for each sample. Compile or run each sample and scan for secrets.
2. **ROT triage.** Mark samples that are redundant, outdated or trivial. Cutting some is a valid outcome.
3. **Scored sample.** Score about 40 samples against the 20-point rubric, stratified by language, product area and age. Record each dimension separately.
4. **Severity ranking.** P0 harms the reader who copies it. P1 does not work as written. P2 works but violates policy. The fix queue is ranked by (readers affected × severity) ÷ effort. P0 items are reported immediately.

## How results will be judged

| Gate | Threshold | Source |
|---|---|---|
| Deprecated-API rate | below 43% | Measured: Zhou & Walker, FSE 2016, Stack Overflow posts. Using it as a gate is this skill's choice. |
| P0 findings | zero | Skill baseline |
| Primary adoption path (quickstart, auth, first call) | 100% tested and green | Skill baseline |
| Compile/run pass rate | at least 90% | Skill baseline, not a vendor standard |
| Corpus executed by CI | at least 80% | Skill baseline |

Only the first is backed by a measured comparator. The others are targets we set, and I will label them that way in the final report.

## Budget ask

To be filled in after the census. For now it is two requests:

- **Engineering time.** Roughly a couple of days for a compile-only CI job that catches removed symbols and missing imports. Promoting the quickstart and auth samples to full execution needs a standing job with fixtures and credentials.
- **Ownership.** One named owner and a code-owner rule for each sample surface. Today I can't say whose queue a broken sample lands in.

## Next steps

1. Run the census (1–2 days).
2. Return with real numbers: pass rate, P0 count and a ranked fix queue.
3. Decide on CI investment with data in hand.

---

**What I need from you to finish**
1. The docs directory paths for all three surfaces, so I can run the census.
2. Whether any CI or test suite exists that samples could live inside.
3. The languages you publish, and which one readers arrive with most.
4. Who owns a broken sample today.
5. Your deadline, and whether you want a one-off cleanup or a standard enforced every release.

I haven't saved anything to memory, since the project context isn't settled yet.