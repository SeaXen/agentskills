# Panel review - the human half of the gates

The scripted gates answer "does it work?".  A panel of focused reviewers
answers "is it the right thing?".  The prompts in this folder are the
review-team reviewer prompts, absorbed so this skill can run the panel
without the `review-team` skill.

Run them **after** the scripted gates pass, in parallel, one subagent per
reviewer.  Each reviewer gets the same context: the app root, the gate
report, and the diff or file list.

| Reviewer prompt | Looks at | Gates it can overturn |
|-----------------|----------|------------------------|
| `correctness-reviewer.md` | logic, edge cases, error paths | N, H, I |
| `architecture-reviewer.md` | structure, coupling, boundaries | N, U, B |
| `api-compatibility-reviewer.md` | REST shape, versioning, breaking changes | N, I |
| `security-abuse-reviewer.md` | authz, injection, abuse cases | E, Q, T |
| `performance-reliability-reviewer.md` | hot paths, retries, timeouts | B, O, I |
| `testing-strategy-reviewer.md` | what is covered, what is asserted | H, N |
| `telemetry-observability-reviewer.md` | logs, metrics, traces, alertability | K |
| `documentation-dx-reviewer.md` | README, setup, onboarding | J, M, L |
| `product-ux-accessibility-reviewer.md` | flows, copy, a11y, polish | C, F, S, R |
| `simplicity-scope-reviewer.md` | over-engineering, dead weight | U |
| `code-quality-conventions-reviewer.md` | conventions, naming, duplication | U |

## How to run the panel

1. Run the scripted gates first: every FAIL must be fixed before a human
   opinion is worth anything.
2. Give each reviewer its prompt file **verbatim** plus:
   - the app root path
   - the gate report (`qa/` artefacts)
   - what the reviewer may not do (it reviews, it does not rewrite the app)
3. Collect one verdict per reviewer: `PASS`, `CONTRADICTED` (with file:line)
   or `UNVERIFIABLE`.
4. A `CONTRADICTED` from any reviewer downgrades that gate to `FAIL` until
   the finding is fixed or explicitly waived in the report.
5. Record the waivers in the final report - a waived finding is still a
   finding.

## Rules for the panel

- Reviewers never invent evidence. If a claim cannot be checked from the
  code, the verdict is `UNVERIFIABLE`, not `PASS`.
- A reviewer may not mark a gate `PASS` when the scripted gate for it is
  `SKIPPED` - the scripts know what they did not measure.
- Findings need a file and a line. "Consider refactoring" is not a finding.
- The panel is a second opinion, not a second veto: one reviewer disagreeing
  with 10 scripts is a discussion, not a bug.

## Why these prompts live here

The `review-team` skill spawns a fleet of subagents.  This skill does the
same thing with the same prompts, so the panel is one step inside a single
review instead of a second tool the user has to remember.  The prompt files
are copied verbatim; the file names are unchanged so a diff against the
source skill stays readable.
