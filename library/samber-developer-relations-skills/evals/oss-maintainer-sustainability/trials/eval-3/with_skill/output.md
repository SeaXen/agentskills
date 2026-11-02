**No. Do not add quartz_hollow as owner or transfer the repo this week.** Your goal is right: leave with a successor in place. The speed and the order are wrong.

Next action, today (15 min): post the reply under "Pressure replies" below. Then message quartz_hollow with the staged plan.

I could not read the fennelwick repo, so the ledger below is from your message only. Gaps are marked "ask".

## Why not this week

- **Short record.** quartz_hollow has 3 weeks and 5 PRs, and the PRs are solid. The skill ranks reviews given above PRs merged, and wants months of record, not weeks. Their reviews of other people's work are unknown (ask).
- **The offer skips the ladder.** "Take over completely" is full control at once. The skill grants triage and review rights first, merge after a joint release, and registry publishing last, after a supervised release.
- **Pressure from third parties.** Two accounts say "just give it to quartz_hollow". The skill names this as a red flag (the xz-utils pattern), alongside a newcomer asking for the keys. This is not proof of bad faith. They may be impatient users, and quartz_hollow may be fully legitimate. The test is whether quartz_hollow accepts a staged pace. A legitimate co-maintainer can wait a release cycle.
- **The stakes are high.** About 2,100 dependents include large logistics users. A bad handover is worse than abandonment (event-stream, 2018).
- **Crates.io owners are equals.** Any owner can add or remove other owners. Adding quartz_hollow gives them full control, including the ability to remove you.

## Plan: staged handover with a fallback

Your six-week date (about 2026-12-04) is the deadline.

### Destination
Ended for you by 2026-12-04, with a vetted successor if the gate passes. If it fails, fall back to freeze then archive.

### Ledger
- **Known.** Sole maintainer. About 2,100 dependents, some large. Hard date in 6 weeks. One candidate.
- **Ask.**
  - Hours per week now, and open issue and PR counts.
  - Whether you own the crates.io name and the repo namespace personally.
  - Whether you hold other crates.
  - Whether quartz_hollow has reviewed other people's PRs.
  - Whether they have an identity or history beyond these 3 weeks.
- **Transition hours** (my estimate), ending 2026-12-04:
  - About 1 h for the heads-up emails.
  - About 1 h for the announcement and README.
  - About 3 h for each joint release.
  - About 2 h per week of mentoring.
  - About 2 h for the transfer day.
  - Total: roughly 15–20 h over 6 weeks.
- **Concentration.** You are the only publisher. This is the main risk.

### Moves
1. **Publish the contract** (1 h, 2026-10-30). Use the README block below.
2. **Declare maintenance-only** (same day). Security fixes and compatibility only. This is also what makes the handover small.
3. **Cut intake** (skip PR limits). You need quartz_hollow's PR pipeline open.
4. **Staged access for quartz_hollow:**
   - **2026-10-30:** triage and review rights.
   - **About 2026-11-06:** joint release 1. They prepare it, you review and publish.
   - **After release 1:** merge rights.
   - **About 2026-11-20:** release 2. They publish through CI, using trusted publishing if crates.io supports it (check current docs). You watch.
5. **Gate, 2026-11-27.** Pass: hand over registry ownership first, then the repo, then the other credentials. Fail: Plan B.
6. **Recruit a second holder.** Ask the big logistics dependents privately for a named person or a custodian organization. One successor is still a single key holder.

The skill says track record earned before the invitation can compress the triage and review stages, but never the publishing stage. Your gate is a compressed schedule. If either release slips, Plan B applies. Do not rush the keys to hit the date.

### Contract (README, ready to commit)
Replace the placeholders. The 3 h figure and 30-day window are the skill's worked example, so fit them to your real hours.

```markdown
## Project status

**Maintenance-only. A maintainer handover is under way; the decision is announced on 2026-11-27.**

- Maintained by one person in their spare time, about 3 hours a week, until 2026-12-04.
- Expect a first reply to issues within 30 days; a reply is not a promise of a fix. Security reports: see SECURITY.md.
- In scope: security fixes and compatibility with new Rust releases. Not in scope: new features.
- Questions go to GitHub Discussions, not the issue tracker.
```

### People
- **quartz_hollow.** Offer this role: triage and review, about 3 h a week, with the staged path above. Use the invitation from the skill's recruitment reference. Tell them the pace is policy and applies to everyone, not distrust.
- **Second holder.** Ask the 2–3 largest logistics dependents (see Exit).

### Exit
- **Plan A, gate passes.** Add quartz_hollow as crates.io owner yourself. Transfer the repo. Update SECURITY.md so reports reach them. Revoke your CI and personal tokens. Move your name to emeritus last.
- **Plan B, gate fails.**
  - Freeze, then archive.
  - Publish a final release whose README states the status.
  - Do not yank working versions.
  - Keep your GitHub and crates.io accounts with 2FA and a recovery contact. Never delete them, or the name can be claimed.
  - State in the README that no further security fixes ship after the archive date.
  - Plan B is short for 2,100 dependents. The skill suggests a quarter or more for a transitive dependency of large projects. That is why the dependent heads-up in step 1 below matters.

Announcement sequence:
1. **2026-10-26/27:** private heads-up to the largest dependents, using the template below.
2. **2026-10-30:** public dual-track notice (template below). It needs your gate date and archive date.

### Review
Re-read the ledger on 2026-11-27 (the gate). Look earlier if quartz_hollow pushes for publish rights before merge rights, asks to change the release pipeline, or the pressure accounts escalate.

## Pressure replies

On the issue thread. Short, no accusation, no timeline set by the crowd:

```markdown
Thanks for the nudge. Fennelwick is not dead: I'm stepping down in early December and arranging a handover. Registry and repo rights are granted in stages, after review and release work together, and that applies to everyone. The decision is announced on 2026-11-27. Meanwhile, triaging and reviewing open issues is the most useful way to help.
```

To quartz_hollow, privately:

```markdown
Hi quartz_hollow - your five PRs were solid, and I'd like you as a co-maintainer. I'm leaving the project in early December. The role: triage and review about 3 hours a week, starting with triage rights this week. After a release we make together you get merge rights, and after a supervised release you publish. The pace is policy, not distrust. The decision on a full handover is on 2026-11-27. Interested?
```

## Private heads-up to a large dependent

```markdown
Hi <maintainer> - <your project> depends on fennelwick, so you're hearing this before the public post on 2026-10-30: I'm stepping down by 2026-12-04. The plan is a staged handover to a contributor, with an archive fallback. If your team would consider custody, or a named person who could co-maintain, I'd like to talk this week.
```

## Public dual-track notice (2026-10-30)

```markdown
# fennelwick is moving to maintenance-only; a handover or archive follows by 2026-12-04

I'm stepping down from fennelwick by 2026-12-04. From today, only security fixes.
**Plan A:** quartz_hollow is joining as co-maintainer. If the handover is complete by 2026-11-27, they become the maintainer and nothing changes for users.
**Plan B:** otherwise the repository is archived on <archive date> and the package marked as unmaintained. Every published version stays installable.
I'll post which plan applies on 2026-11-27.
```

## Checks before you call this done

| Check | Status |
|---|---|
| No single key holder, or an end date | Not yet. Needs the second holder or the end date, as above |
| End state written in the README | Passes once the status block above is committed |
| Security path named | Passes once SECURITY.md names the reader |

Self-set budget and contract checks come at the review date.

## Questions that change the plan

1. Do you personally own the crates.io name and the repo namespace?
2. Has quartz_hollow reviewed anyone else's PRs?
3. Are the logistics dependents' maintainers reachable?

Next: commit the README status block today.