# Meridian Forge — Triage, CLA/DCO, Maintainer Ladder, and First-Time-Contributor Fix

Scope: ~30 issues/week (~4-5/day, ~130/month). Sized for a small rotating triage pool (3-6 people), not a dedicated triage team.

---

## A. Triage rota + label taxonomy

### Label taxonomy

Six orthogonal axes. Every issue gets exactly one `type/*`, one `status/*`, zero-or-more `area/*`. Priority and entry-level labels are triage-only additions.

| Prefix | Values | Applied by | Purpose |
|---|---|---|---|
| `type/` | `bug`, `feature`, `docs`, `question`, `chore`, `regression`, `security` | Reporter (via issue template, auto-applied) | What kind of issue this is |
| `area/` | `engine-core`, `scheduler`, `triggers`, `connectors`, `cli`, `sdk-go`, `sdk-py`, `ui-dashboard`, `docs`, `infra-ci` | Triager | Which component owns it — maps directly to CODEOWNERS, drives routing |
| `status/` | `needs-triage`, `needs-repro`, `needs-design`, `confirmed`, `in-progress`, `blocked`, `needs-info`, `stale` | Triager / assignee | Where it sits in the pipeline |
| `priority/` | `P0-urgent`, `P1-high`, `P2-normal`, `P3-low` | Triage captain only | SLA driver, not a popularity contest — reserve P0 for data-loss/crash/security |
| `entry/` | `good-first-issue`, `help-wanted` | Triage captain | Feeds part D directly |
| `meta/` | `duplicate`, `wontfix`, `upstream`, `needs-maintainer-call` | Triager / maintainer | Closing/escalation reasons |

Rules:
- Every new issue auto-gets `status/needs-triage` from the issue template (**not** a human step — wire it into the YAML issue form's default labels).
- `security` type never gets a public triage pass — see escalation below.
- Cap `area/*` at 2 labels per issue; more than that means the issue should be split.

Bootstrap the labels with a script rather than clicking through the UI:

```bash
gh label create "type/bug" --color d73a4a --repo meridian-forge/meridian-forge
gh label create "type/feature" --color a2eeef --repo meridian-forge/meridian-forge
# ...repeat per row above, or loop over a CSV of name/color
```

### Triage rota

- **Pool**: every Reviewer and Maintainer (role definitions in part C) is in the rota. At current volume, a pool of 4 covers 1 week on, 3 weeks off each.
- **Rotation**: 1 named "triage captain" per week, published in a pinned issue or a bot-posted weekly comment. Swap requests go through the captain pool directly, no maintainer approval needed for a swap.
- **Daily sweep** (15 min, async, captain's job): run a saved search (`is:issue is:open label:status/needs-triage`), assign `type/*` if missing, assign `area/*`, set `priority/*`, and either close/merge/comment or hand to `status/confirmed`.
- **SLA**:
  - First triage pass (label + response): 2 business days for `P2`/`P3`, same business day for `P1`.
  - `P0`: 4 hours, any hour — bypasses the rota entirely (see escalation).
- **Weekly bug scrub** (30 min, captain + 1 volunteer maintainer): sweep `status/needs-info` older than 14 days → close with a template comment if still unanswered; sweep `status/blocked` for unblock opportunities.
- **Stale handling**: automate with a stale-bot — `needs-info` issues get a "closing in 7 days" ping at day 14, auto-close at day 21. Never auto-stale `good-first-issue` or `P0`/`P1`.
- **Escalation path** (bypasses rota):
  - `type/security` → goes straight to the private security-report channel (`SECURITY.md` email/GitHub private vulnerability reporting), never triaged in public issues.
  - `P0` → pings the on-call maintainer (separate, smaller rotation than triage — 1 week at a time among Maintainers only) directly.
- **Auto-labeling**: wire issue-template → label mapping in the YAML form (`labels: ["type/bug", "status/needs-triage"]`) so the captain's sweep starts from `type/*` already set, not from zero.

---

## B. CLA vs DCO

**Recommendation: switch to DCO.** This directly serves goal (d) — a CLA is one of the biggest silent killers of first-PR conversion (a legal doc gate in front of a one-line typo fix is a real reason contributors bounce), while DCO is a single `-s` flag on a commit you were already making.

Why DCO clears the bar here:
- It still certifies provenance (the "Developer Certificate of Origin" text the contributor signs off on is the same legal function a CLA performs for IP-origin purposes) — it just doesn't require an out-of-band signature step, bot account linking, or corporate legal sign-off before a first PR can even be opened.
- Corporate contributors already have DCO sign-off baked into their internal process if they've ever touched the Linux kernel, Kubernetes-adjacent CNCF projects, Git itself, or Docker/Moby — it is the path of least resistance for them too, not just for individuals.
- Enforcement is a single free GitHub Action/App, not a CLA-bot subscription or a manually maintained signee list.

The one condition that flips this answer: **if Meridian Forge intends to relicense in the future (dual-license, move to BUSL, sell a commercial fork, do an "open core" split)**, a CLA (specifically one with a copyright assignment or broad relicensing grant) is the only mechanism that keeps that option open — DCO gives the project a license to use the contribution under the current OSS license, nothing more, and you cannot retroactively CLA your way out of that later without re-contacting every past contributor. Confirm the business/licensing roadmap before finalizing; if there's no relicensing plan, DCO is unambiguously correct.

Migration steps:
1. Announce the switch in a pinned issue/discussion with an effective date (new PRs only — **do not** require retroactive DCO sign-off on already-merged history).
2. Add DCO enforcement as a required status check:
   ```yaml
   # .github/workflows/dco.yml
   name: DCO Check
   on: [pull_request]
   jobs:
     dco:
       runs-on: ubuntu-latest
       steps:
         - uses: dcoapp/app@v1  # or the DCO GitHub App instead of a workflow
   ```
3. Update `CONTRIBUTING.md`:
   ```bash
   git commit -s -m "fix: correct off-by-one in scheduler window"
   # forgot -s on the last commit?
   git commit --amend -s --no-edit
   ```
4. Remove the CLA-bot config and webhook; archive (don't delete) the historical signee records for legal retention.
5. Drop a `## Developer Certificate of Origin` section in the README linking to `CONTRIBUTING.md`, so first-time contributors see the requirement before, not after, opening a PR.

---

## C. Maintainer ladder and voting rules

Five tiers, each with an explicit bar and an explicit granting mechanism. Lightweight process for low-stakes promotions, real vote only for merge-rights-and-above.

| Tier | Grants | Bar | Promotion mechanism |
|---|---|---|---|
| Contributor | — | 1+ merged PR | Automatic |
| Triager | Label/assign/close issues, no merge | 15+ triaged issues in a rolling 8 weeks, or equivalent sustained rota participation | Nominated by any Maintainer, **lazy consensus**: 72h public objection window on a tracking issue, silence = approved |
| Reviewer | `Approve` rights on PRs in 1+ `area/*`, listed in `CODEOWNERS` as reviewer | 10+ merged PRs or equivalent high-signal reviews in that area, demonstrated understanding of its design constraints | Nominated by any Maintainer owning that area, **lazy consensus**, 72h window |
| Maintainer | Merge rights, `CODEOWNERS` area ownership, votes in formal ballots | Reviewer for 3+ months, track record of sound review judgment and design-discussion input, not just volume | Nominated by any existing Maintainer, **formal vote**: all current Maintainers get +1/-1/abstain, 7-day window, 2/3 supermajority of votes cast, quorum = 50% of the Maintainer body |
| Core/Steering | Cross-project scope, admin rights, roadmap and governance authority, CoC escalation owner | Maintainer for 6+ months | Annual election by the full Maintainer body, same voting rule as Maintainer promotion |

Voting rules, summarized:
- **Lazy consensus** (default, low-stakes): open a tracking issue, 72h silence = approved. Used for Triager/Reviewer grants, routine label-taxonomy edits, doc changes.
- **Formal vote** (Maintainer+, governance changes, license changes, CoC decisions): explicit ballot, 7-day window, 2/3 supermajority of votes cast, 50% quorum of the body. Public by default; **private ballot for CoC enforcement matters specifically**, to protect the reporter and avoid a public pile-on.
- **Removal for inactivity**: 6 months with no merges/reviews/rota participation moves a Maintainer to **Emeritus** (listed, honorary, no active privileges) — automatic, not a vote, not punitive, and reversible on request (e.g., returning from leave).
- **Deadlock**: unresolved technical disagreement between Maintainers within one area escalates to a Core/Steering formal vote, not an endless thread.

Document this as `GOVERNANCE.md` (the ladder + voting rules) and `MAINTAINERS.md` (the actual roster, generated from/matching `CODEOWNERS` so the two never drift apart).

---

## D. Fixing "I don't know where to start"

Diagnosis: this almost never fails because `good-first-issue` doesn't exist — it fails because the label is a dumping ground (50 stale issues, half already fixed, none with enough context to start cold), and because there's no single page that says "start here."

Fixes, in priority order:

1. **Cap and curate the backlog.** Hard cap `entry/good-first-issue` at ~15-20 open at once. Curating it is an explicit weekly duty of the triage captain (part A) — seed 2+ new ones, retire claimed/stale ones, don't let it become archaeology.
2. **Require a fixed shape for every good-first-issue**: context paragraph (why this matters), exact file/function to start from, acceptance criteria, and an explicit "questions welcome in comments, no PR needed to ask" line. An issue that doesn't meet this bar doesn't get the label, full stop — a vague `good-first-issue` is worse than none, because it burns the exact trust it's meant to build.
3. **Add a "Start Here" section to `CONTRIBUTING.md`**, first thing after the title, five steps: clone → build → test → browse [this filtered search link] → open PR. One link to `is:issue is:open label:entry/good-first-issue no:assignee`, not a description of how to construct that search.
4. **Make claiming visible and non-colliding.** Convention: comment "I'd like to work on this," triager assigns within 48h via a `/assign` bot command. Auto-unassign after 14 days of inactivity so claimed-but-abandoned issues don't block a second contributor from ever finding them.
5. **Split the entry path by contributor type.** A workflow engine's core (`engine-core`, `scheduler`) is intimidating to a first-timer; docs, CLI, and SDK issues are not. Give `CONTRIBUTING.md` three short paths — "fix a bug," "improve docs," "add a connector" — instead of one generic wall of text, and bias the curated `good-first-issue` pool toward `area/docs`, `area/cli`, `area/connectors` for anything genuinely entry-level.
6. **Welcome-bot the first PR**, not the first issue comment: on a contributor's first-ever PR, auto-comment with links to `CONTRIBUTING.md`, the DCO sign-off instructions (part B), and a one-line "a Reviewer will look at this within 2 business days" — sets the SLA expectation instead of leaving it to silence.
7. **Measure it**, don't just ship it: track median days-to-first-merged-PR for new contributors, and % of `good-first-issue` claimed within 7 days of being labeled. Review both numbers at the same cadence as the weekly bug scrub — if the good-first-issue pool isn't converting, the curation bar in step 2 is the first thing to revisit, not the README copy.