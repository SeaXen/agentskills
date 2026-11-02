# Verdict: keep the goal, change the plan

Your goal is right: a shared project, led by someone who likes mentoring. Two of your three moves work against it, though, and the third is in the wrong order.

| Your move | Verdict | Why |
|---|---|---|
| Restrict PRs to collaborators | ⚠️ Skip for now | It closes the pipeline you want to recruit from. |
| SEEKING MAINTAINERS banner | ⚠️ Not yet | You already have two candidates. A banner draws strangers, and the xz-utils pattern started that way. |
| First applicant gets full write plus org ownership | ❌ Drop | This is the event-stream pattern: keys handed to the first volunteer. |
| Ask Saltmarsh for a donation | ⚠️ Reorder, and ask for something else | Money comes last and does not cut your workload. |

## Why each move changes

- **PR restriction.** It makes sense when inflow is mostly automated or unsolicited. You haven't told me that's your drain, and Ifeoma and Dusan are exactly the kind of people who arrive as PR authors and reviewers. If AI-generated or drive-by PRs really are the drain, use a softer cut first. Add a "please open an issue first" note in CONTRIBUTING and a PR template. Revisit the restriction only after Ifeoma and Dusan have their rights.
- **Banner.** A public "seeking maintainers" status widens the pool but attracts strangers. Treat anyone who answers it as a candidate for triage rights only. Invite Ifeoma and Dusan directly instead.
- **Keys to the first applicant.** Grant triage and review quickly, because they are cheap to revoke. Merge comes after a release you make together. Publishing and org ownership come last, after a supervised release, and never in the same act as merge. Prior track record can compress the early stages for Ifeoma and Dusan. Nothing compresses the publishing stage, and it applies to everyone.
- **Go-specific trap.** A Go module has no registry account. Whoever can push a tag has effectively published a release. "Full write access" is therefore already release power, so use tag protection or rulesets that limit tag creation to you for now.
- **Donation.** Donations rarely reach a salary. core-js reported about $400 a month at 250M monthly downloads. Money also doesn't shrink your inbox or fix who can publish.

## What to ask Saltmarsh for

Ask for a named engineer and hours, not money. Their CTO asked how to "support the project". A person doing 2–4 hours a week of review is worth more than a donation.

- Treat that engineer as a fourth candidate on the same ladder, with no shortcut because their employer is a big user.
- If they want to pay, ask for a support contract with service levels, or fund Ifeoma's or Dusan's hours. Funding someone else's hours stays useful even if you want fewer hours total.
- Hand the program design to `oss-sponsors-fundraising` once the contract and ladder exist. Funding adds load (reporting, expectations), so it comes last.

## Draft plan

I haven't confirmed three things with you. They are listed under "Please confirm" at the end. Treat the numbers as placeholders until then.

### Destination

Shared (b). Target date: six months, so about 2027-04-23.

### Ledger

Fill the blanks before you commit to anything:

- **Inflow:** new issues, PRs and discussions per month: ___
- **Backlog:** open issues split into waiting-on-reporter, waiting-on-you, confirmed bugs and feature requests: ___
- **Hours:** now ___ vs. budget ___
- **Transition hours:** invitations, mentoring and the supervised release are a one-time cost with an end date. Budget a dated bridge above your steady-state hours.
- **Publish rights:** you alone (to verify) → single key holder, which is the first thing to fix.
- **Shape:** 3,500 importers with two active helpers is Eghbal's "stadium". Contributors don't appear on request, so cut the contract before waiting on them.

### Moves, in order

1. **Publish the contract** (1 hour, this week). Commit the status block below.
2. **Invite Ifeoma and Dusan** (30 min each, this week). Use the invitation below.
3. **Cut intake softly** (an afternoon). Add issue forms, route questions to Discussions, and add a `SUPPORT.md`.
4. **Automate chores** (a day). Group dependency updates and cut releases from CI.
5. **Reach out to Saltmarsh** (reply to the CTO within the week). Ask for a named engineer and hours, and say the role is staged.
6. **Run the staged ladder** over the next 3–6 months, in the order shown in People.
7. **Funding** last, via `oss-sponsors-fundraising`.

### Contract (README, ready to commit)

```markdown
## Project status

**Active, growing the maintainer team**

- Maintained by <name> with help from Ifeoma and Dusan, about <N> hours a week combined.
- Expect a first reply to issues within <window>. Security reports: see SECURITY.md.
- In scope: <what gets fixed>. Not in scope: <what will be declined>.
- Questions go to GitHub Discussions, not the issue tracker.
- Want to help? Review PRs and answer Discussions. Rights are granted in stages, based on work done together.
```

Derive `<window>` from your budget, don't copy a norm. Replies per week = weekly hours × 60 × share of time on the tracker ÷ minutes per first reply. With no better numbers, assume half the time on the tracker and 15 minutes per reply. Those two defaults are the skill's own, not sourced. If monthly inflow exceeds about four weeks of replies, cut intake before you publish a window.

### People

**Invitation to Ifeoma and Dusan** (send separately):

```markdown
Hi <name> - you've reviewed and fixed a lot on Marrowbone this year, and your judgement on <specific PR or thread> was spot on. I'm cutting my own time on the project to about <N> hours a week and want co-maintainers.

The role: triage new issues and review PRs, about <M> hours a week, starting with triage and review rights. After a release or two together we'd add merge, and later release rights. The pace is policy for everyone, not distrust. It's fine to say no or to try it for a month.
```

**Access stages** (dates are mine, adjust them):

| Stage | Rights | Earliest |
|---|---|---|
| 1 | Triage + review | Now |
| 2 | Merge | After one release cut together (about 2–3 months) |
| 3 | Tag and publish | After one release they run while you watch |
| 4 | Org owner | Last, so the org has two owners and not one |

Stage 4 is the goal, so "ownership so they feel trusted" does happen, just last. Use `oss-governance` for the full credential inventory and the ladder wording in GOVERNANCE.md.

**Red flag:** if anyone asks for publish rights or org ownership early, or third parties start saying who should take over, reply with the stage policy and keep reviewing their PRs normally.

**Vet Ifeoma and Dusan once:** reviews given (not just PRs merged), reachable on more than one channel, and interest that predates your call for help. You already have that evidence.

### Review

- **Re-read the ledger on 2026-11-20** (four weeks). Check whether actual hours sit inside your budget, and whether the window held.
- **Earlier look if:** a candidate asks for speed, a security report arrives with nobody named to read it, or you go past budget twice.
- **Health checks to pass before calling this done:**
  - Every publish right has two holders.
  - The README states the status.
  - SECURITY.md names who reads reports.

## Please confirm

These change the plan:

1. **Hours.** How many a week do you want to give, honestly, and how many does Marrowbone take now?
2. **Drain.** What costs the most energy: PR volume, AI or drive-by PRs, support questions, release chores, security reports, or the backlog guilt? If it's AI-generated PRs, I'd move intake cuts up and the PR restriction becomes reasonable.
3. **Clock and money.** Is there a date (a new job, leave, a release)? Do you want to be paid, or just have fewer hours?

If any of the three is "I'm still mentoring and it's fine", the plan above stands unchanged.