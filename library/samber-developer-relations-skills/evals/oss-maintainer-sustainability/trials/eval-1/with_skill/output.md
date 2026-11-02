**Do first (1 hour):** commit the README block below, **write to README.md**. Skip the 48-hour badge. Ship intake cuts before any sponsor page.

## Why no 48h badge

- You give 3h/week. Capacity = 3h × 60 × ½ on tracker ÷ 15 min = **6 first replies/week, about 25/month**. These figures are self-set baselines from the skill.
- Inflow is 45 issues/month plus about 8 PRs. That is roughly 2× what 3h covers.
- A 48h promise breaks in week 1. Each break then reads as a new broken promise.
- Money does not cut inflow. Donations rarely reach a salary: core-js got about $400/month at 250M downloads (Tidelift-era reporting, per the skill's findings file). Funding also adds load (sponsor expectations, reporting).
- Order that fits you: contract → maintenance tier → intake cuts → automation → backlog reset → co-maintainer → funding.
- Funding goes last, and it pays for a co-maintainer's hours, not yours. You said you want fewer hours total.

## Sustainability plan - Tessellate - 2026-10-23

**Destination.** Assumed from your 3h answer: lighter, then shared. Tell me if you want to leave instead.

**Ledger**

| Item | Value |
|---|---|
| Inflow | 45 issues + about 8 PRs/month |
| Backlog | 410 open (split into waiting-on-reporter / waiting-on-you / confirmed bugs / features: not yet done, first sweep task) |
| Hours | 10-12 now, 3 budget |
| Transition | about 15h over 4 weeks (2026-10-26 to 2026-11-27), dated bridge above budget |
| Top drain | Unknown. Which is it: volume, support questions, PR review, hostile comments, or backlog guilt? |
| Publish holders | Unknown. Check that PyPI and the GitHub org have 2 owners. You are likely the only one. |

**Moves, with dates**

1. Contract: README block (below), **write to README.md**. 1h, by 2026-10-26.
2. Maintenance tier: pick "Maintenance-only" (security fixes and compatibility with new Python and library releases). Add "Out of scope". 2h, by 2026-10-30.
3. Cut intake: issue forms with blank issues disabled, a bug form requiring version and reproduction, GitHub Discussions for questions, `SUPPORT.md`. 3h, by 2026-10-30. Do not restrict PRs to collaborators yet; that closes the pipeline you recruit from.
4. Automate chores: grouped Dependabot, release from CI with PyPI trusted publishing. 1 day, by 2026-11-20.
5. Backlog reset: announce 2026-11-02, run 2026-11-09. Close only old, unreproduced, inactive items; keep confirmed bugs. About 1 day.
6. Co-maintainer: invite from people who reviewed or answered well this year. Triage rights first. No publish rights for months.
7. Funding: open the sponsor page after moves 1-3 are live.

**Health check, 2026-11-27.** Hours within 3? Window met for most new items? If not, widen the window publicly. Do not work harder.

## Deliverable 1: README section

Replace the window if the 4-week check says otherwise. Use plain text, no badge image.

```markdown
## Project status

**Maintenance-only**

- Tessellate is maintained by one person in their spare time, about 3 hours a week.
- I read new issues about once a week. Expect a first reply within 30 days. A reply is not a promise of a fix.
- In scope: security fixes, bugs in supported tile formats, and compatibility with new Python releases.
- Not in scope: new tile formats, new output backends, async variants of the public API, and unsupported Python versions.
- Questions go to [GitHub Discussions](link), not the issue tracker. Nobody owes an answer there, but other users often help.
- Security reports: see [SECURITY.md](link).
- Looking for a co-maintainer. If you have reviewed or answered issues here and want to share the work, open a Discussion titled "Co-maintainer".
- Funding: see [Sponsors](link). Sponsorship pays for maintenance time. It does not buy support or priority.
```

Replies to paste:

- Scope decline: "Thanks for putting this together. New formats are out of scope (see 'Project status' in the README), so I'm closing this. A fork is welcome to carry it."
- Capacity: "I can't get to this, and I don't plan to in the future. Closing so it doesn't look like it's coming."

Backlog announcement, pinned a week ahead:

```markdown
**Backlog reset on 2026-11-09.** I can't work through 410 open issues with the time I have. On that date I will close issues with no reproduction and no activity in the last 12 months, with the label `backlog-reset`. Confirmed bugs stay open. If an issue still matters to you, comment with a current reproduction and I will reopen it. Security reports belong in SECURITY.md, not here.
```

## Deliverable 2: GitHub Sponsors page

Use GitHub Sponsors only for now. Open Collective doubles the admin and reporting load. Add it only when a company needs invoices or a fiscal host.

**Headline:** Keep Tessellate maintained.

**Introduction:**

> Tessellate parses GIS tile formats for Python. About 1.1 million downloads a month from PyPI. For five years I have maintained it alone, next to a day job.
>
> The project gets about 45 new issues a month and a couple of PRs a week. I can give it about 3 hours a week. That covers security fixes, bug fixes in supported formats, and compatibility with new Python releases. It does not cover new features or fast replies.
>
> **What your money does:** it pays for maintenance time, and for the hours of a second maintainer once one joins. More paid hours means fewer releases stuck on one person.
>
> **What it does not do:** it does not buy support, priority on issues, or features. Sponsors get the same queue as everyone else. If your company needs guaranteed answers, ask me about a support contract instead.
>
> If your team depends on Tessellate, a monthly sponsorship is the most useful gift, because it is predictable.

**Tiers:** set amounts yourself; I have no data on your audience.

| Tier | Monthly | Reward |
|---|---|---|
| Supporter | $[X] | Name in the SPONSORS list |
| Team | $[Y] | Logo in README, listed as a sponsor |
| Company | $[Z] | Logo and link in README. Tessellate stays maintained for your stack. |

Do not add response-time rewards. Do not add private channels or "priority issues"; each is new load.

**Goal text (optional):** "First goal: pay for a second maintainer's review hours."

**Open Collective** (later, if needed):

> Funds go to maintenance time for Tessellate: reviews, releases, security fixes. No feature promises. Expenses are listed publicly.

## Missing info

- Which drain is biggest? If hostile or entitled comments, I move moderation above the backlog reset.
- Who else can publish to PyPI or merge? If nobody, add that to the plan before funding.

**Next, 2 minutes:** paste the README block into `README.md` and commit. Then reply with your top drain from the ledger.