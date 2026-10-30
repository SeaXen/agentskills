# Co-maintainer recruitment

Finding, inviting and vetting someone to share the load or take it over. The governance skill owns the trust ladder and credential inventory; this file is about the person.

## Contents

- Where candidates come from
- The invitation
- Vetting checklist
- Red flags

## Where candidates come from

Ranked by how much trust already exists:

1. People who reviewed PRs or answered issues well in the last year. Reviewing shows judgement; merged PRs alone show interest.
2. Authors of several good PRs who stayed through review.
3. Companies whose product depends on the package and could give an employee's hours. Ask for a named person and hours, not money.
4. Maintainers of adjacent projects with a public track record.
5. Custodian organizations (a foundation, a collective, an ecosystem org) when no individual fits. Check they have more than one admin.

A public "seeking maintainers" status widens the pool but also attracts strangers; treat any stranger who answers it as a candidate for triage rights only.

## The invitation

```markdown
Hi <name> - you've reviewed and fixed a lot here over the past year, and your judgement on <example> was spot on. I'm cutting my own time on <project> to about <N> hours a week and want a co-maintainer.

The role: triage new issues and review PRs, about <M> hours a week, starting with triage rights. After a couple of release cycles together we'd add merge, and later release rights. No obligation, and it's fine to say no or to try it for a month.
```

Spell out the role, the hours and the staged path; a vague "want to help maintain?" attracts the wrong people and scares the right ones.

## Vetting checklist

- [ ] Public track record of months, not weeks, on this project or a comparable one.
- [ ] Reviews given, not only PRs merged.
- [ ] Reachable through more than one channel, and responsive.
- [ ] Their interest predates your call for help, or comes through a person you trust.
- [ ] Comfortable with a staged path (triage, review, merge, then publishing after a supervised release), months apart. Say in the invitation that the pace is policy, not distrust.
- [ ] For key-holder roles: a verifiable identity or an established public history, stated as policy in the governance file.

## Red flags

- Pressure to speed up the stages, especially from accounts with little history.
- Third parties complaining that the project is dead and naming who should take over.
- A newcomer asking for publish rights or organization ownership before review rights.
- Requests to move releases or signing off the existing pipeline.

Any of these is a reason to pause the process, not to explain it. A legitimate co-maintainer can wait a release cycle.

Reply to an early request for publish rights, and keep reviewing their pull requests normally:

```markdown
Thanks for offering to help. Publish and release rights on this project are granted in stages, after review and merge work together and one supervised release. That applies to everyone. If you'd like to start, triaging and reviewing open issues is the most useful thing right now.
```
