# Meridian Forge — triage, license policy, maintainer ladder, and the first-contribution fix

Built this against four skills: `oss-issue-triage` (rota + labels), `oss-license-strategy` (CLA/DCO), `oss-governance` (ladder + voting), `oss-contributor-onboarding` (the "where do I start" fix). `oss-contributor-onboarding` explicitly routes (a), (b), (c) to the other three — it only owns (d) — so this stitches all four into one policy set for one project.

**What I don't have**: repo access. Baselines that require running commands against the real Meridian Forge repo (the audit script, a cold clone-to-tests run, reading the last 10 outside PRs, `gh issue list` exports) are marked below with the exact command and what to plug the output into. I did not fabricate numbers for those.

**Assumptions**, stated so you can override them — each is flagged where it changes the design:

1. ~30 issues/week ≈ 130/month inflow, mix unknown (assumed majority bug reports + feature requests, some usage questions).
2. 5 maintainers, spanning more than one employer, ~2-3 hrs/week each for triage+review in a normal week. Replace with your real number — the arithmetic below scales to it, the rota doesn't.
3. A CLA exists today (given). No confirmed business model requiring relicensing/dual-licensing was stated.
4. Outbound license unstated — matters for the CLA call (see B).
5. No foundation deadline or election history mentioned.

---

## A. Triage rota + label taxonomy

### Capacity check first
30/week × a 3-minute per-item placeholder (this skill's own planning default, not a measured constant — time your first real session and replace it) = 90 triager-minutes/week just for first-pass sorting. Against 10-15 hrs/week of team capacity (assumption #2), sorting isn't the bottleneck — unstaffed review and no written response target are. Design around that, not around the label scheme.

### Label taxonomy — orthogonal axes, one value per axis per item

| Axis | Values | Rule |
|---|---|---|
| **type** | `kind/bug`, `kind/feature`, `kind/question`, `kind/docs`, `kind/chore` | Auto-applied from the issue form. |
| **state** | `status/needs-triage` (default on open), `status/needs-repro`, `status/confirmed`, `status/blocked`, `status/waiting-on-reporter`, `status/in-progress` | Moves the queue; drives the stale sweep. |
| **priority** | `priority/critical`, `priority/high` — no third label | Absence of a label = normal priority. Two values only: PyTorch's rule is **never let automation apply the top priority level** — `priority/critical` is human-applied, always. A third tier invites the "priority theatre" failure mode (everything ends up `priority/high`). |
| **area** | `area/scheduler`, `area/executor`, `area/connectors`, `area/sdk`, `area/cli`, `area/ui`, `area/docs`, `area/ci-infra` | Split `area/sdk` by language only once you maintain more than one SDK as a separately-owned component. Apply at high/medium confidence only — at low confidence, leave it `status/needs-triage` rather than guessing; a wrong area label routes to the wrong owner and costs more than no label. |
| **contributor-facing** | `good first issue`, `help wanted`, `skills/<domain>` (e.g. `skills/go`, `skills/scheduling`, `skills/docs`) | Kubernetes' distinction: `good first issue` = a maintainer has committed to mentor it; `help wanted` = "we'd take a patch," no mentoring promise attached. Don't conflate them. `skills/*` matters more than difficulty — a 74-participant study (Steinmacher et al., arXiv:2103.12653) found newcomers pick issues by "can I already do this domain?", not by an assigned difficulty tier. |

**Security reports get no label and never touch this tracker** — private intake channel (GitHub private vulnerability reporting is the default with no dedicated list), a named size-capped response team, embargo for coordinated disclosure. Apache's rule: never put vulnerability details in the public tracker, ever.

**PR-only, not a label**: the DCO/CLA sign-off check and fork-CI-permission gate are automated preconditions, not something a human triages.

### Rota — Mozilla's two-tier model
- **Triage owner** per `area/*` — a named, long-term accountable maintainer per component. Not rotating.
- **Triage duty** — weekly rotation across the 5 maintainers, one on duty + one named backup. At ~6 new items/day (30/week ÷ 5 business days), one daily 15-minute session covers first-pass sorting; stop at the time box, not at zero — a session ends at its clock, not at inbox-zero, so a spike week doesn't blow the rota.
- **Session order**: newest untriaged first (protects the response target) → items where the reporter just replied → a fixed backlog quota.
- **A triager alone may**: apply type/area/priority-high labels, close duplicates/invalid, route usage questions off-tracker, ask for repro.
- **A triager alone may not**: apply `priority/critical` (pings the on-duty maintainer directly, real-time), make a scope/breaking-change call (routes to the area owner or the maintainer council — see C), close anything waiting on a maintainer rather than the reporter.
- **Permissions**: grant triage-level tracker permissions (label/close/assign, no merge) to triagers — most trackers have this role separate from write access, which is how the triage team grows past the 5 who can merge.

### Pull requests get their own gate order (not the issue process)
1. Sign-off + fork-CI-permission — automated, blocks nothing human touches yet.
2. **Direction check** — one maintainer comment, same day: is this in scope. Roughly two-thirds of rejected PRs never needed the code read at all (MSR 2026 mining study) — settle this before spending review minutes.
3. Size/risk label — computed from the diff, routes, decides nothing.
4. Correctness + tests review, by the area owner via CODEOWNERS.
5. Design review, reasoning attached.
6. Style — only what the formatter missed; a human should never type a spacing comment.

### Closing/staleness
Auto-close only `status/waiting-on-reporter` after a stated silence window; never sweep `status/confirmed` or `status/blocked` — a bot closing a confirmed bug tells the reporter their evidence was worthless. Warn before closing, run the first pass dry-run, every close states the reason and how to reopen.

### Baseline you need to run before locking any of this in
```
gh issue list --state all --limit 2000 \
  --json number,title,state,createdAt,updatedAt,closedAt,labels,author,comments > issues.json
python3 scripts/triage-baseline.py issues.json --triage-prefix "kind/,priority/"
```
Read back: open count, untriaged share, median time to first human response, created-vs-closed flow. If untriaged share or response time is already bad, that number — not this design — is what to lead with when you publish the change.

---

## B. CLA → DCO

**Not legal advice** — this is a distribution-and-friction decision, and the license-family question (what you're currently outbound-licensed under) changes the answer, so verify it before acting.

**Recommendation: switch to DCO**, conditional on assumption #3 holding (no confirmed dual-licensing/relicense plan, no foundation mandate, no employer forcing a corporate CLA).

Reasoning, Fogel's ladder (*Producing Open Source Software*) — nothing / DCO / CLA / assignment, ranked by what each buys per unit of contributor friction:
- A DCO is, in Fogel's words, "probably the minimum amount of CLA a free software project should adopt" — one commit trailer (`git commit -s`), one automated check, costs a contributor nothing beyond a flag.
- A CLA "probably offers the best tradeoff between safety and convenience" — but only *when the project genuinely needs the extra rights it grants*: relicensing later, dual licensing, selling a commercial license on contributed code. Move up a rung only for a right the license doesn't already grant you.
- The friction is not hypothetical: "someone who wants to fix a typo must first complete a signing workflow" (tenthirtyam.org, practitioner post) — and that's exactly the population part (D) is trying to stop losing.
- CNCF's own guidance: they "encourage projects to use DCO as it's easier to setup and use."

**What would flip this back to keeping the CLA**:
- A confirmed dual-licensing or open-core plan (charging a different set of terms to a specific buyer).
- A foreseeable relicense (e.g., a future move to a source-available term against a specific named competitor).
- A corporate contributor whose employer requires a CLA regardless of your policy.
- Joining a foundation that mandates one.
- **Patents**: check what your current outbound license already grants before treating "patent protection" as a reason to keep the CLA — Apache-2.0, GPL-3.0 and MPL-2.0 already carry a patent grant; MIT and BSD don't. If you're not on one of the patent-granting families, that's the one gap DCO alone doesn't close, and worth a real conversation before dropping the CLA.

**Mechanics if you proceed**: keep existing contributors' prior CLA'd contributions as-is (their license grant doesn't unwind), add a DCO bot/check (e.g. probot-dco) on all new PRs, require `git commit -s`, and put the sign-off requirement in CONTRIBUTING *before* the "find something to work on" section — announced once, in one place, not discovered at the merge gate.

---

## C. Maintainer promotion ladder + voting rules

**Model: maintainer council** (the default fit at 3+ maintainers who share no single-payroll majority) — reversible by one vote, an hour a month, no standing meeting, and it buys the two rules ad-hoc projects most visibly lack: deadlock resolution and a promotion path.

Escalate to an elected steering committee only if you cross one of: maintainers land on more than one payroll in a way that creates a visible conflict, a founder-departure is already on the horizon, the contributor base outgrows the 5 maintainers, or a foundation application states a governance bar. None of those are given — don't buy that model preemptively; it costs a quarter to install and is the least reversible option on the table.

### Ladder
| Rung | Grants | Bar | Granted |
|---|---|---|---|
| **Contributor** | credited as author | one merged PR | automatically |
| **Regular contributor** | requestable as reviewer, `skills/*` routing target | sustained activity (e.g. 3+ merged PRs or equivalent triage/docs work in 90 days) | by any maintainer noticing it |
| **Committer / triager** | triage-level permissions: label, close waiting-on-reporter items, request changes — **not** merge | nomination by any maintainer | fast — felixge's rule: be generous with review/triage rights, they're cheap to grant and cheap to revoke |
| **Maintainer** | merge to their `area/*`, CODEOWNERS entry, seat + vote on the council | nomination + lazy consensus (below) | slower — months of visible, reviewed contribution in one area |
| **Release/security key holder** | signing keys, publish tokens, org ownership | a subset of maintainers, by separate nomination | slowest — months of evidence; a signed release is downstream before anyone notices a bad one. State explicitly in the doc that the pause is policy, not distrust |
| **Emeritus** | credited permanently, fast-tracked back on return | 6 months of inactivity, or voluntary | automatic after notice |

Merge rights and release keys are **disaggregated on purpose** — the post-xz-utils lesson is exactly this: be generous with the ladder, slow with the keys. A maintainer heading toward burnout gets scope/triage/funding relief *first*; keys go last, to whoever has the longest track record, not to whoever is simply available.

### Voting rules
- **Lazy consensus** for routine work: announce, wait 72 hours (Node.js's own window — an example to borrow, not a standard), proceed if nobody objects.
- **Consensus-seeking** for anything contested: a reasoned objection gets a place to be answered, not just noted.
- **Explicit vote**, simple majority, quorum = majority of the council, only for: new maintainer, maintainer removal, scope change, governance-doc amendment. Fogel's own caution on why vote is last-resort, not first: "after a compromise, everyone is a little bit unhappy, whereas after a vote, some people are unhappy while others are happy."
- **Amendment to this document itself**: supermajority (2/3) and a longer window (2 weeks) — it should be harder to change than a routine decision.
- Every blocking objection must carry a technical justification — a veto is an argument, not a mood. Every path has a timer; an unbounded discussion is a silent veto for whoever benefits from the status quo.

Publish this as `GOVERNANCE.md`, cross-linked from CONTRIBUTING rather than duplicated into it (see D).

---

## D. Fixing "first-time contributors can never figure out where to start"

Steinmacher et al.'s newcomer-barrier taxonomy (a 20-study literature review, *Information and Software Technology* 59, 2015) names this exact failure mode: **"finding a way to start."** It's usually one or more of: no beginner queue, a beginner queue that's actually stale/claimed/unmentored, a CONTRIBUTING file that doesn't say where to look, or a setup that breaks before anyone gets far enough to try an issue.

### What you need to actually measure (I can't run these — you can)
```
scripts/contributor-path-audit.sh <meridian-forge-repo-root>
```
Reports: which community-health files exist and their display precedence, whether CONTRIBUTING mentions the 10 real topics (vocabulary check only — read the file, don't trust the grep), setup surface, how many CI workflows use secrets (can't run on fork PRs), contributor history (one-commit-only rate, absence factor).

Then a **cold run** (fresh container, no cached anything, reading only what a stranger reads) — timestamped friction log, don't fix mid-run, it hides the real size of the problem. Second pass: from the beginner-issue list, can a stranger find the file to change in under 15 minutes? If either run needs a step nobody wrote down, that step is the actual bug — not the CONTRIBUTING wording.

### The fix, in the order that pays off fastest
1. **Stop closing easy bugs yourself.** Each one you fix in 20 minutes is a recruiting opportunity spent. Kent C. Dodds' framing, the one this whole step rests on: "the hard part of getting into open source for the first time isn't the implementation of a feature, but figuring out how to actually contribute code."
2. **Rewrite every beginner issue to the 7-part shape** — observed behaviour, expected behaviour, exact file + test, `skills/*` domain required, a settled approach ("no design discussion needed" where true), the verification command, a named mentor. A one-line "should be better" issue is small only for someone who already knows the codebase.
   - Weak: `The config loader should handle errors better.`
   - Strong: current behaviour → expected behaviour → `internal/config/loader.go`, `Load()` → suggested fix, message text settled → `make test PKG=./internal/config` → `@maintainer-handle`, comment to claim.
3. **Publish a claiming convention + stale-claim expiry** (e.g., comment to claim, 14 days idle returns it to the pool) and actually enforce it — a queue that looks full but is entirely claimed by absent people is worse than an empty one.
4. **Keep a standing floor of 3+ unclaimed, valid beginner issues at all times.** Someone who finds zero doesn't come back later to check.
5. **Reserve non-code entry points explicitly** — docs, connector examples, SDK translation, triage-shadowing. This is the widest door and the first thing an all-code queue silently loses.
6. **Put the legal gate (DCO, per B) before the reader writes code** — stated in CONTRIBUTING's "before you open a PR" section, never discovered at the sign-off check itself.
7. **Fix the environment before the prose.** Documentation describing a broken setup is worse than none. Pick the cheapest tier the cold run's failures actually require — a `make setup` bootstrap command before a pinned toolchain before a full devcontainer; promote to devcontainer only if the stack needs real services (DB, GPU, paid API) that the cold run exposed.
8. **The two-clock rule on review**: acknowledge same-day, review by a stated date — silence is the expensive failure, not slowness. Post scope in the first comment; discovering "out of scope" after three review rounds is the worst outcome for both sides.
9. **Credit at merge, and invite the second contribution by name** — "merged, ships in v2.4, you're credited — if you want another, #388 is the same area." This is the moment a drive-by becomes a returning contributor, and it doesn't happen on its own.

### CONTRIBUTING.md — fill this in with your real numbers
```markdown
# Contributing to Meridian Forge

Thanks for being here. We take code, docs, tests, triage, and connector examples.
We do not take <your real out-of-scope list — new core dependencies, unreviewed
scheduling algorithm changes, etc.>.

## Set up
    git clone <fork> && cd meridian-forge
    make setup      # installs everything and runs the test suite
Expect: `<N> tests passed` in under <M> minutes.
Prerequisites: <runtime + version>, pinned in `<version file>`.

## Find something to work on
- Beginner-friendly: <link to the `good first issue` query>. Comment to claim;
  claims expire after 14 days.
- Nothing fits? Open an issue describing the change before writing code.

## Before opening a pull request
    make test lint
Target `<branch>`. Sign your commits: `git commit -s` (DCO — see B above).

## After you submit
A maintainer acknowledges within <your real, honest number> and reviews by the
date given in that reply. We squash-merge. You're credited in the release notes.

## Stuck?
Ask in <channel> (usually answered within <latency>) or comment on your PR.
```
Placement: root, `.github/`, or `docs/` — pick one, GitHub's display precedence is `.github/` > root > `docs/`; duplicates diverge silently. State conventions (branch naming, commit format, required reviewers) **literally, near the top** — a widely-installed contribution-agent skill reads exactly six things from this file before opening a branch, and anything unstated gets overwritten with its own generic default, not left blank.

---

## E. Order to actually do this in
1. Run the audit script + `gh issue list` export this week — every number above is a placeholder until you do.
2. Publish labels + rota (A) and the DCO switch (B) together — both are cheap, reversible, and the DCO change needs the rota's response-target line anyway.
3. Rewrite the top 10 beginner issues to the 7-part shape and set the 3-issue floor (D) — highest damage removed per hour of any single fix here.
4. Fix the setup path (D.7) before rewriting CONTRIBUTING prose around it — documented-but-broken is worse than undocumented.
5. Publish GOVERNANCE.md (C) last — it's the least urgent of the four unless a specific promotion or dispute is already live.

## F. How you'll know it worked
Re-run the audit + a fresh cold run quarterly. Track, without over-reading a low-volume signal as a trend: new external contributors/quarter, second-contribution rate within 90 days, median time to first human response (bots excluded) against your published target, external-PR merge rate tracked separately from maintainers' own PRs, and the contributor absence factor (should rise slowly — it's the only one of these that measures whether the project got less fragile).