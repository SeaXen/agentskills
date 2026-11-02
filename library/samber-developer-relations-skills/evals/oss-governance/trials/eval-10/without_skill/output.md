## Bottom line

Don't copy the Kubernetes SIG model wholesale — it's built for a scale you don't have. Six maintainers who all work across all six directories, plus four outside contributors, is not "six areas each needing their own SIG." It's one team that needs a cheaper way to stop requiring six people's attention on every change. Adopt the *decision-rights* idea from SIGs, skip almost all the ceremony.

## Why the full model breaks at this size

- A K8s SIG has enough contributors to hit quorum without everyone showing up. Your "SIG" would be ~1 person plus maybe one of the four outsiders. That's not a SIG, that's just an owner with a title.
- SIG charters, SIG leads, SIG meetings, plus a top-level council is *two meeting layers*. Budget check: 6 people × 2 hrs/week = 12 hrs/week of process, total, for the whole project. One weekly SIG meeting per area (6 meetings) already burns most of that before anyone reviews a PR.
- "All six of us work across all six directories" directly contradicts area-based governance. SIGs assume people specialize in their area. If nobody does, six SIGs just becomes six labels on the same six people doing the same thing they do now, plus paperwork.
- Council-above-SIGs only earns its keep when SIGs disagree and need arbitration by people *not* already in the room. With six people total, the council and the SIGs are the same six people — the escalation layer adds a second conversation about a decision already made in the first one.

## What's actually slowing you down

"Every change seems to need everyone's attention" is a **review/approval-rights problem**, not a missing-governance-structure problem. The fix is changing who has to say yes, not inventing new entities to say yes.

## Recommended structure

**1. Area ownership, not SIGs.** One `OWNERS`-style file at the repo root, one row per directory:

| Directory | Primary owner | Backup owner |
|---|---|---|
| core runtime | (assign) | (assign) |
| CLI | (assign) | (assign) |
| web dashboard | (assign) | (assign) |
| Terraform provider | (assign) | (assign) |
| Helm charts | (assign) | (assign) |
| VS Code extension | (assign) | (assign) |

Pick these by who already leans toward each area, even loosely — don't force new specialization. Owner ≠ "only person allowed to touch it," it means "person whose approval unblocks a merge."

**2. Approval rule replaces the SIG layer.**
- PR touches one directory → that directory's primary or backup owner approves. Done. No cross-review required.
- PR touches multiple directories → each touched directory's owner approves *their* part only, in parallel, async. Nobody reviews the whole diff just to be polite.
- This alone removes the "everyone needs to weigh in" bottleneck without creating a single new meeting.

**3. No separate council. Escalation = the whole team, informally.** If two owners disagree, default to the owner of the directory where the change actually lands. If it's genuinely cross-cutting and unresolved after 3 business days async, the six of you are already the council — no extra body needed.

**4. One lightweight `GOVERNANCE.md`, not six charters.** One page: the ownership table, the approval rule, the escalation rule. No mission statements, no SIG-specific charters, no election process for six people who already all know each other.

**5. Outside contributors get review rights, not SIG membership.** If one of the four regulars consistently contributes to, say, the Helm charts, make them backup owner there. That's it — no separate contributor ladder to design yet at this volume.

## What to explicitly drop from the K8s playbook

- Per-SIG charters and mission docs
- Per-SIG meetings
- SIG leads as a distinct role from "owner"
- Top-level steering council as a separate body
- Election process
- Separate comms channels per SIG

None of these pay for themselves under 12 hrs/week of total process budget.

## What to revisit later, and when

- If a directory gets a contributor base big enough to have real disagreements without you (roughly: 3+ regular non-maintainer contributors *in that one area*), give it a real owner rotation and slightly more process — still not a full SIG.
- If outside contribution grows past ~10–15 regulars total, revisit whether async-only escalation still scales, and consider a monthly (not weekly) sync instead of a permanent council.
- Until then, re-running this plan is wasted process spend — the trigger is contributor count, not calendar time.