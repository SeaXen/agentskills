Using the `oss-contributor-onboarding` skill. This matches its "someone opened their first PR and I don't know what to reply" case: Step 6 only — a drafted reply plus the two-clock playbook for next time. I don't have the actual Harborlight repo to run the audit script against, so the reply below uses placeholders (`<...>`) for your real commands — swap those in before posting.

---

## 1. Reply to post on the PR now

Post this today. It's four days late, which the two-clock rule (below) exists to prevent — say so plainly rather than pretending it wasn't.

> Hi @nreddy — sorry this sat quiet for four days, I was heads-down on a release, not ignoring it. That's on us, not a sign of how we normally handle a first PR.
>
> I read through it: nice, clean implementation, and I can tell it took real effort — but a Redis backend isn't something we're looking to take on. We've deliberately kept this SDK's core dependency-free, and adding a network-backed storage adapter changes that shape for everyone, not just Redis users. That's a scope call, not a quality one, and it should have been said in an issue before you wrote 340 lines — that gap is ours to fix, not yours.
>
> A few smaller things, independent of the scope question, in case you want to keep this or reuse it elsewhere:
>
> - CI shows red on `lint`. Run `<your lint command>` locally — it should reproduce and tell you exactly what's flagged.
> - The other two red checks need repository secrets and can't run on a fork — that's expected, not something you did wrong. Ignore them.
> - A few variable names don't match our convention (`<example>` → `<example>`); not blocking anything, just flagging for if this becomes a separate package.
>
> Given the scope mismatch I'm going to close this rather than let it sit — but I'd rather you leave with something than nothing:
>
> 1. This would work well as a standalone Redis adapter package. If you publish it, tell me and I'll link it from our README under "community adapters."
> 2. If you want a first contribution that *is* in scope, `<link a real good-first-issue>` is open and could use exactly this level of care.
>
> Either way, thanks for taking the time — genuinely, and I'd like to see you on something else here.

Swap in a real good-first-issue link before sending — closing without one turns this from "redirect" into "rejection," which is the outcome you're trying to avoid.

---

## 2. First-PR playbook — for the three of you

Share this as a pinned doc (issue, wiki page, or top of `CONTRIBUTING.md`). It exists because this PR's real failure wasn't @nreddy's — it's that nothing told them the Redis backend was out of scope, nothing let their checks pass on a fork, and nothing forced an acknowledgment before four days passed. Fix the path, not just this one reply.

**Rule 1 — Acknowledge and review are two different clocks.**
Whoever sees a new PR first posts *something* within one business day — not a review, just "seen, here's when." Silence is the expensive failure here, not slowness; contributors who get a response inside ~48 hours come back at a much higher rate than ones who don't (GitHub's Open Source Guides — practitioner figure, no published dataset behind it, but the direction is the whole point). Pick a full-review target you three can actually hit given real hours-per-week, publish it in `CONTRIBUTING.md`, and hold it — a stated 5 business days that's met beats a stated 48 hours that's missed.

**Rule 2 — Scope gets stated before code, not after.**
Add an explicit "out of scope" list to `CONTRIBUTING.md` (start it with: *alternative storage backends — the SDK stays dependency-free; publish adapters as separate packages*). For anything architectural, ask contributors to open an issue first; say so in the PR template. This is the actual fix for "340 lines we never wanted" — it stops the PR before it's written, not after.

**Rule 3 — Fix the fork-CI gap once, structurally.**
Split the pipeline into a credential-free lane that runs on every fork PR (lint, unit tests, build) and a privileged lane one of you triggers manually for anything needing AWS secrets. Right now every external PR shows red on checks a contributor can't fix, which reads as "this is broken" instead of "this is normal" — document in `CONTRIBUTING.md` that it's expected and who runs the privileged lane before merge.

**Rule 4 — Review in a fixed order, and label blocking vs. optional.**
Scope → correctness & tests → design (with reasoning) → style (only what the formatter missed — anything a machine can fix never appears as a human comment). Mark every comment **Blocking** or **Optional**; an unlabelled wall of comments reads as a wall of failures. This isn't just tidiness — Terrell et al. (PeerJ CS 3:e111, 2017; 3M+ PRs) found outside contributions reviewed with reasoning attached and consistent process score more evenly across contributors than impression-based review does. Same fixed order, every PR, whoever's reviewing.

**Rule 5 — Decline fast and kindly, with a next step.**
Thank them, name the scope rule (link where it's published), offer an alternative issue, close. Do this inside your review-target window — a PR rotting for months is worse than a same-week no.

**Rule 6 — Credit at merge, invite the next one.**
On anything you *do* merge: keep them as commit author, name them in release notes, and explicitly point at a named next issue. This is the step that turns a one-off PR into a contributor, and it basically never happens by itself.

**Rule 7 — Write down what happens when a PR stalls.**
Before a bot or anyone closes it: offer to finish it yourself (with edits-on, contributor stays author), or convert it to an issue. Default to "life happened," not "lost interest."

Re-check this quarterly: is there still a standing stock of ≥3 claimable good-first-issues, is the response target still being met, did the fork-CI split actually ship. If any of those slip, that's the next thing to fix — not the wording of this doc.