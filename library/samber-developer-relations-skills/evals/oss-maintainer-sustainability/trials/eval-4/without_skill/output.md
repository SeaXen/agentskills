**Next: don't install the bot as planned this weekend.** Do the dry run this weekend and the announcement today. Close nothing for 3 weeks.

You asked for a one-shot close of about 500 issues with a "closed as stale" reply. That will probably produce more "abandoned or lazy" comments, not fewer. The reply tells 500 people their report was worthless, and most of those issues are probably waiting on you, not on the reporter. A bot closing issues that wait on the maintainer is the weak point of a stale-bot policy.

A one-time backlog reset is defensible if it is announced, warned, reviewed and reversible. The plan below does that, and the whole thing takes about 90 minutes of setup.

## Plan

1. **Today (30 min):** pin the announcement below. Open it as a Discussion or issue.
2. **Saturday (30 min):** add the Phase 1 workflow with `debug-only: true`. Read the log. Check that the exempt labels catch what they should.
3. **Sunday (10 min):** set `debug-only: false`. This only labels issues `stale` and posts the warning. It closes nothing.
4. **+21 days:** the same workflow closes whatever stayed silent.
5. **After that:** swap in the steady-state workflow (Phase 2).

## Phase 1: one-time backlog reset

`.github/workflows/backlog-reset.yml`

```yaml
name: backlog-reset
on:
  workflow_dispatch: # manual only, so nothing fires by surprise
permissions:
  issues: write
  pull-requests: write
jobs:
  reset:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/stale@v9 # check the latest major version
        with:
          debug-only: true # set to false on Sunday after reading the log
          days-before-issue-stale: 90
          days-before-issue-close: 21 # warning period before any close
          days-before-pr-stale: -1 # leave PRs alone
          days-before-pr-close: -1
          stale-issue-label: stale
          close-issue-reason: not_planned
          # 500+ issues; each action costs API operations
          operations-per-run: 1000
          ascending: true # oldest first
          remove-stale-when-updated: true # any comment rescues the issue
          exempt-issue-labels: "security,confirmed-bug,help wanted,good first issue,pinned,has-pr,roadmap"
          exempt-all-milestones: true
          exempt-all-issue-assignees: true
          stale-issue-message: >
            This issue has had no activity for 90 days. I'm the only maintainer
            and I'm clearing the backlog so I can spend my limited time on issues
            that are still alive. If this still affects you on the latest
            release, comment with a minimal reproduction and the Pennyroyal
            version, and it stays open. If nothing changes in 21 days, I'll
            close it. See #XXXX for the full explanation.
          close-issue-message: >
            Closing this because there was no activity after the warning above.
            This is not a judgment on the report. If it still happens on the
            latest release, please open a new issue using the bug template and
            link this one. A reproduction on the current version gets it triaged
            first. See #XXXX for how I'm handling the backlog.
```

- **Labels:** the exempt labels are guesses. Replace them with your real ones. If you have none, label the 20-30 issues you know matter before Sunday.
- **Reopening:** a person who didn't author the issue can't reopen it, and the author may not be able to either once a bot closes it. That's why the closing comment says "open a new issue" and does not promise a reopen.
- **Before the close date:** read the list of issues that stayed silent, at the 21-day mark. Skim it for 15 minutes. Anything that is a real bug gets `confirmed-bug`.

## Announcement (pin it today)

> **Title: Backlog cleanup and how Pennyroyal is maintained**
>
> Pennyroyal has about 620 open issues and one maintainer, who has around 4 hours a week for it. I've been answering too slowly, and a long list of open issues that nobody will get to isn't honest. It makes it look like each one has been looked at.
>
> Starting this weekend, issues with no activity for 90 days get a `stale` label and a warning. If nobody comments within 21 days, they close. Security issues, confirmed bugs, and anything assigned or on a milestone are exempt.
>
> If your issue is still real, comment with a minimal reproduction on the latest release. That's all it takes to keep it open. If it gets closed, open a new issue and link the old one.
>
> What to expect from me from now on:
> - New issues get a first human reply within 7 days, usually sooner.
> - I triage in two fixed sessions a week. I don't reply outside them.
> - Please don't @-mention me on issues. It doesn't speed anything up, and I see every new issue anyway.
>
> If Pennyroyal matters to your company and you want faster turnaround, sponsorship or contributing triage help is the way to change the arithmetic. [link]

Adjust the 7-day promise to a number you can keep. At 4 hours a week and about 3 minutes per item (a placeholder, not a measured figure), you can triage roughly 80 items a week at the very most. If new inflow is under 40 issues a week, 7 days is safe. Time your first real session and replace the 3 minutes with your measured number.

## Phase 2: steady state (replace Phase 1 after the reset)

```yaml
name: stale
on:
  schedule:
    - cron: "17 3 * * *"
permissions:
  issues: write
jobs:
  stale:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/stale@v9
        with:
          only-issue-labels: needs-info # only issues waiting on the reporter
          days-before-issue-stale: 14
          days-before-issue-close: 7
          days-before-pr-stale: -1
          days-before-pr-close: -1
          close-issue-reason: not_planned
          stale-issue-message: >
            I'm waiting on the information requested above. If you can add it
            within 7 days, I'll pick this back up. Otherwise I'll close it,
            and you can open a new issue anytime with the details.
          close-issue-message: >
            Closing because the requested information didn't arrive. This is
            about what I can act on, not about the report. Open a new issue with
            the details and link this one and I'll look again.
```

- **Scope:** this bot closes only issues you tagged `needs-info`. It never closes an issue that is waiting on you. That is the rule that keeps it from feeding the "lazy" story.
- **Every first reply:** add `needs-info` when you ask the reporter for something. Add `confirmed-bug` when you reproduce one.

## The "closed as stale" comment

Don't use it. The close message above replaces it. It is longer, but it states the reason, links the explanation, and says how to get back in. The short version reads as dismissal, and the "abandoned" comments will quote it.

## The daily @-mention

That's a moderation problem, and the stale bot won't touch it. The first step is one reply, once:

> Hi, I read every new issue, and tagging me doesn't change when I get to it. I triage twice a week. Please stop @-mentioning me on issues. If it continues, I'll have to restrict comments on the thread.

If it continues after that, take these steps in order:

1. Lock the thread, or use GitHub's interaction limits on the repo.
2. Block the account.
3. Report it to GitHub if it crosses into harassment.

Add a `CODE_OF_CONDUCT.md` if you don't have one, so the line is already written.

## On "abandoned or lazy"

- **Don't answer individual comments.** The announcement and a short `STATUS` section in the README do that once, and you can link to them.
- **Add to the README:** "Maintained by one person, ~4 h/week. First reply within 7 days. Sponsors and triagers welcome."
- **Burnout stats:** I haven't verified the 59% and 35% figures, so I'm not building on them. They don't change the decision. The 4-hour cap does, and the plan is sized to it.

## Open question

How many new issues does Pennyroyal get per week? That number decides whether the 7-day promise holds. If it's above about 40, you need a second lever beyond the stale bot, such as issue forms that require a reproduction or a chooser that routes questions to Discussions.