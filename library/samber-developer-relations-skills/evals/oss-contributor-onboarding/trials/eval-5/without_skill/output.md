Here's both pieces.

## 1. What to write back to @nreddy

Post this as a PR comment, then close the PR:

> Hey @nreddy, thanks for taking the time to put this together, and welcome — this is your first PR here, so I want to be upfront rather than let it sit.
>
> I'm going to close this one. The blocker isn't the lint failure or the checks — it's that a Redis backend isn't something we've wanted for Harborlight. We've kept the SDK deliberately backend-agnostic and adding a stateful store like Redis is a bigger architectural decision than a PR can settle on its own, so I don't want to ask you to keep polishing 340 lines toward something we're not going to merge.
>
> A couple of things so this doesn't feel like a black box:
> - The two checks failing on AWS access aren't something you can fix — we don't share those secrets with fork PRs, so they'll always fail until a maintainer runs them manually. Not on you.
> - The lint failure and naming are real, and would've mattered if we were merging this, but no need to chase them now.
>
> If you want to contribute again, the fastest path is to open an issue or a discussion first for anything beyond a small fix — that way we can tell you early if it fits before you sink hours into it. I'll link a couple of open "help wanted" issues that are actually on our roadmap, if you're interested. Appreciate the effort either way.

Adjust warmth/formality to your voice, but keep the three moves: thank, decline on scope (not on fixable nits), and name the AWS checks as a structural non-issue so they don't walk away thinking they failed at something fixable.

## 2. Process for the other two maintainers

The real bug isn't @nreddy's PR — it's that a 340-line scope-mismatched PR got as far as sitting unreviewed for four days with no signal it was dead on arrival. Fix the funnel, not the symptom.

**Add `CONTRIBUTING.md`** with three sections:
- **Scope / non-goals** — name what Harborlight explicitly won't do (e.g. "no bundled storage backends — Redis, DynamoDB, etc. are out of scope, see #issue-link"). This is the line that would've stopped @nreddy before they wrote code.
- **Before you code** — "Anything over ~50 lines or touching architecture: open an issue or discussion first. We'll confirm fit before you invest time." Small fixes/typos skip this.
- **Local checks** — exact commands to run lint/tests before opening a PR, and your naming/style conventions in one short list.

**Add a PR template** (`.github/PULL_REQUEST_TEMPLATE.md`) with a checkbox: "☐ Linked issue/discussion where this was agreed on (required for anything beyond a small fix)." A PR with an unchecked box and no linked issue is an instant, low-guilt "let's discuss in an issue first" close — no one has to make a judgment call under release pressure.

**Fix the CI false signal.** GitHub Settings → Actions → "Fork pull request workflows from outside collaborators" → require approval for first-time contributors. Right now those two AWS-secret jobs fail loudly on every external PR, which reads as "your code is broken" when it's really "we haven't decided to run this yet." With approval required, they sit pending instead of red until a maintainer opts in — much less discouraging, and it stops eating review time triaging failures that were never fixable.

**Split CI so the failure is honest.** If lint/unit tests don't need secrets, keep them on `pull_request` (they'll run and report truthfully on forks). Move anything needing AWS creds to a separate job/workflow gated by the approval setting above, so a contributor's checks tab shows "these passed, these are awaiting maintainer approval" instead of a wall of red.

**Rotate a triage duty.** Three maintainers, one release cycle where all of you are heads-down, is exactly when a PR goes four days silent. Pick a lightweight rule — e.g. weekly rotation, whoever's "on" replies (even just "thanks, will look properly next week") to any new external PR within 2 business days. Costs one person a few minutes; prevents every future first-time contributor from wondering if they've been ignored.

Priority order if you only do one thing now: **the fork-approval setting** — it's a five-minute GitHub settings change and it kills the "two failing checks they can't fix" problem outright for every future PR, not just this one.