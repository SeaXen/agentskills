# Sustainability plan: Saffronbridge, 2026-10-23

**Short answer: no, that sequence doesn't fit your clock.** Automate the releases now, publish a contract, and pause on a dated notice. Build the contributor program after you're back.

I read the skill and its references. Two parts of its process couldn't run in a single reply. It asks six interview questions one at a time and validates the plan section by section. I inferred the answers from your message instead. The assumptions are listed below, and I marked any numbers I made up.

## Why the sequence fails

- **A program, cohort and steering group is the slowest, most expensive move.** The skill calls recruiting co-maintainers "net negative for the first months": mentoring costs more hours than it saves. You have 12 hours a week for 7 weeks, then nothing. The program would be half-built when you leave and would stall while you're away.
- **Contributors don't appear on request.** Saffronbridge is the shape Nadia Eghbal calls a "stadium": many users and very few contributors. Cut the load before you wait on people.
- **Handing releases to "whoever emerges" is the event-stream pattern.** In that 2018 incident, publish rights went to a volunteer who asked, and the package was compromised. The skill grants rights in stages: triage, then review, then merge. Registry publishing comes last, after a supervised release.
- **Your biggest drain is a day of work, not a program.** Changelog, tagging, wheels and PyPI upload can all run from CI. After that, releases take about 15 minutes and no longer need a trusted person holding a token.
- **The earliest date is the deadline.** Seven weeks to the baby beats a six-month horizon. That promotes moves that land in a day.

## Destination

Same project, 4 hours a week, from about 2027-03-15. The baby is due around 2026-12-11. I assumed you're offline from then until about 2027-03-11.

## Ledger (assumed where marked)

| Item | Value |
|---|---|
| Hours | 12 a week now; target 4 |
| Top drain | Release chores, every 2 weeks |
| Inflow, backlog | Unknown. I need monthly counts of issues, PRs and discussions. |
| Capacity at 4 hours | 4 × 60 × ½ ÷ 15 min = 8 first replies a week, about 30 a month (self-set defaults) |
| Transition hours | About 3 days over the next 6 weeks. This fits inside your current 12 hours a week, and it ends 2026-12-04. |
| Publish rights | Assumed you alone hold them. Confirm. |
| Dependents | 2M downloads a month, and a handful of OSS projects depend on it |

If monthly inflow exceeds about 30, cut intake before publishing a response window.

## Moves, with dates

1. **Publish the contract, by 2026-10-30 (1 hour).** Commit the README block below.
2. **Declare a maintenance tier, by 2026-10-30 (an afternoon).** I recommend maintenance-only until about April: security fixes, compatibility with new Python releases, and bug fixes. Feature requests close by pointer to an "Out of scope" list. That list is your call.
3. **Automate releases, by 2026-11-13 (about 1 day, plus a dry run).**
   - Generate the changelog from merged PRs or commit messages.
   - Build wheels in CI (cibuildwheel is the usual route).
   - Publish to PyPI through a tag-triggered workflow using trusted publishing, so no personal token is needed.
   - Rehearse on TestPyPI.
   - Check each tool's current docs before you start.
4. **Cut intake, by 2026-11-20 (an afternoon).** Add issue forms that require a reproduction and version, a `SUPPORT.md`, and Discussions for questions. Don't restrict PRs to collaborators. You'll want that pipeline open when you recruit later.
5. **Prove the pipeline, 2026-11-20 and 2026-12-04.** Run both real releases through CI. If a vetted candidate exists (see People), have them push the tag on one release while you watch.
6. **Announce the pause, by 2026-12-04 (10 minutes).** The notice must name who reads security reports, or say plainly that nobody will.
7. **Defer until you're back:** backlog reset, co-maintainer recruitment, the contributor program, funding. A backlog reset floods every subscriber with notifications, which you don't want in your first weeks as a parent.

## Contract

Commit now. The 4-hour numbers are the ones you can keep after you return.

```markdown
## Project status

**Maintenance-only**

- Maintained by one person in their spare time, about 4 hours a week.
- Expect a first reply to issues within 30 days; many will wait longer. Security reports: see SECURITY.md.
- In scope: security fixes, bug fixes, compatibility with new Python releases. Not in scope: <your list>.
- Questions go to GitHub Discussions, not the issue tracker.
- Releases are cut on demand, at most monthly.
```

Replace it on 2026-12-04:

```markdown
**Paused until 2027-03-15.** I'm on leave. Issues and PRs stay open but won't be read until then. Security reports go to SECURITY.md and are read by <name> during the pause, or: "will not be read until 2027-03-15". If the pause becomes permanent, this notice will say so.
```

## People

- **No co-maintainer is needed to survive the leave.** The pipeline plus a named security reader covers it.
- **Ask the dependents once, in November.** Send one short message to the maintainers of the projects that depend on Saffronbridge. Ask whether any of them can give a named person a few hours a week for the first half of 2027. Employer-funded hours are the best source of maintainers.
- **Trust ladder if someone says yes.** Start with triage and review rights. Merge comes after a release made together. Publish rights come last, after a supervised release. That is months, not weeks.
- **If you have no vetted person by 2026-12-04, nobody holds publish during the leave.** Put that in the README: "no releases until <date>; emergency fix path: none". Don't give keys to a volunteer to buy relief.
- **Red flags:** pressure to move faster, a newcomer asking for publish rights first, or third parties naming who should take over. Decline in writing and keep reviewing their PRs normally.

## After you return

- **March:** read the backlog only after two weeks back. Then announce and run one backlog reset.
- **April:** if you still want shared maintenance, start `oss-contributor-onboarding` at its smallest version. A steering group stays a one-page GOVERNANCE.md until a second maintainer exists.
- **Handover of releases:** it happens only after a supervised release with that person, and only if you want to hand them off.

## Review

- **Re-read the ledger on 2027-04-12, four weeks after you return.**
- **Look earlier if any of these happens:** a security report arrives during the pause, monthly inflow exceeds 30, or a release takes more than an hour of your time.
- **Health check:**
  1. Hours stayed within 4 a week.
  2. The 30-day window was met for most items.
  3. Every publish right has two holders, or the plan names an end date.
  4. The README states the current status.
  5. Someone reads security reports, or the README says no one does.

## Questions that would change this plan

1. How many issues, PRs and discussions arrive a month, and who else can merge or publish?
2. Who owns the PyPI name and the GitHub org? Are you paid for any of this?
3. Do you maintain other packages? If so, triage them first.

If the answer to question 1 shows heavy inflow, intake cuts move ahead of release automation.

Congratulations on the baby. For nine weeks of work you'll get three months of fully paused leave.