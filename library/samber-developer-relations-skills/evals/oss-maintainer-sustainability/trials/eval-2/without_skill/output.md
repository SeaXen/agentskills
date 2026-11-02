# Plan: cut @brindlewood/ledgerkit from 60% to 20% of your time

**First action (10 minutes):** open a note and start a time log. Use 4 buckets: `escalation`, `triage`, `release`, `feature/fix`. Log for 5 working days. Step 1 depends on this data.

## Diagnosis

- 20% is 8 h/week. 60% is 24 h/week. You must remove about 16 h/week.
- Timeboxing alone fails. Your manager's rule caps your hours but not the inflow, so the queue still grows. Escalations come from about 40 customers, and those customers push back through account managers, so you absorb the work at night.
- Escalation work is company support work. It is not OSS maintenance. The company should fund it and own it. The fix is to move that work out of your 20%, not to ignore it.
- Single point of failure: you publish from your personal npm account. That is a credential held by one person, and it makes you the release bottleneck. This is a risk to the company too, and it is your strongest argument for a staffing conversation.

## Lever ranking

Ranked by hours returned per hour of effort:

1. **Cut intake.** Route escalations away from the public tracker. This is the biggest and most permanent cut.
2. **Shorten the promise.** Publish a response target you can actually meet.
3. **Add people.** Get a second triager and a second releaser. This is slowest to pay off, but it is the only lever that adds capacity.

Skip a stale bot for now. It touches little of the 16 h you need to cut.

## Steps

### Step 1. Measure (week 0, about 3 h total)

1. Log your time for 5 days, as above.
2. Export the issues: `gh issue list --state all --limit 2000 --json number,title,state,createdAt,closedAt,labels,author,comments > issues.json`
3. Tag each open issue by source: `customer-escalation`, `community bug`, `usage question`, `feature request`.
4. Write down one number: what share of your hours goes to customer escalations. I expect it is more than half. If it is not, tell me and I will rework the plan.

### Step 2. Get a written agreement with your manager (week 1, 1 meeting of 30 minutes)

Take the numbers from step 1. Do not argue "I'm overloaded". Argue "the company has an unfunded support duty". Ask for these 4 decisions in writing:

1. **A named escalation path for customers.** Customers go through Brindlewood support or their account manager, who file one structured ticket. They no longer open ad-hoc issues for you to chase. You are the L3 engineer behind the path.
2. **A support budget split.** Escalation work is logged against a separate support or customer-success budget. Your 20% covers only the OSS work: triage, review, release.
3. **A response promise.** Suggested wording: public issues get a first human reply within 5 working days. Customer tickets through the escalation path get a reply within 2 working days. Adjust to what your log supports.
4. **A second engineer.** You need one co-maintainer and one backup releaser from the company, with about 4 h/week each.

If your manager refuses item 2, that is useful information. The 60% load is then a staffing decision, not your failure. Write that down.

### Step 3. Cut intake (weeks 1-2, about 1 day)

1. Add `.github/ISSUE_TEMPLATE/config.yml` with `blank_issues_enabled: false`.
2. Add contact links for usage questions (GitHub Discussions or Slack) and for customer escalations (the support path from step 2).
3. Replace the markdown templates with a bug form. Require the fields that change the outcome: SDK version, Node version, a minimal reproduction, and expected versus actual behavior.
4. Add a customer-facing page, `SUPPORT.md`. It states the response targets and where to go. Link it from the README.
5. Put security reports on a private channel. Enable GitHub private vulnerability reporting.
6. Pre-announce the change once to the 40 integrations through their account managers. They should hear it from Brindlewood, not from a bot.

Expected return: a large share of escalations stop landing on the tracker. I do not have a measured figure for your repo. Take it from your step 1 data.

### Step 4. Add labels and a triage rhythm (week 2, about 2 h setup)

1. Use 4 label axes, one value per item per axis:
   - type: `bug`, `feature`, `question`
   - state: `needs-triage`, `needs-info`, `confirmed`, `blocked`
   - priority: `p1` (data loss or security), `p2`, `p3`
   - source: `customer`, `community`
2. Triage in 2 fixed sessions per week, 30 minutes each. End at the time box, not at inbox zero.
3. Session order: newest untriaged first, then items where the reporter replied, then 5 old items.
4. Auto-close only items in `needs-info` after 21 days of reporter silence. Warn first and run a dry run first. Never auto-close `confirmed` or `blocked` items.

### Step 5. Fix the npm risk (weeks 2-4, about 3 h)

1. Check what you own: `npm org ls brindlewood` and `npm owner ls @brindlewood/ledgerkit`.
2. Move the `@brindlewood` scope into an npm organization owned by the company. Add at least 2 owners. Keep yourself as one of them.
3. Set up publishing from GitHub Actions with npm trusted publishing (OIDC), so no personal token is needed.
4. Gate releases with a protected branch and a required reviewer.
5. Write `RELEASING.md` and have your backup releaser publish one release while you watch.
6. Do not deprecate or republish the existing package. Test the whole change on a throwaway package first.

Result: you stop being the only person who can release, and the company stops depending on your personal account.

### Step 6. Bring in a second pair of hands (weeks 3-8)

1. Give the co-maintainer triage-level permissions first, not write access. Add write access after about 4 weeks of good judgment.
2. Alternate weekly triage duty. Name a backup.
3. Hold back release rights until step 5 is done.

### Step 7. Review and adjust (week 8, then monthly)

Re-run the export and compare against step 1. Targets (my own baselines, not industry standards):

- Your total repo time is at or below 8 h/week for 4 weeks in a row.
- Untriaged issues are below 10% of open issues.
- First-response target met on at least 90% of items.
- Issues opened per month by customers go down, and tickets through the support path go up.

If you miss them, lower the promise from step 2 item 3 instead of working more hours.

## Risks

- **Customers keep opening issues anyway.** Reply once with a template that points to the support path, then close. Your manager and the account managers must back this up.
- **No second engineer is approved.** Then 20% is not reachable at current inflow. Say so in writing and ask your manager which promise gets cut.
- **A big customer demands an exception.** Route it through your manager, not through you.

## What I assumed, and what I need to know

- I assumed you can edit repo settings and that Brindlewood has a support or account-management function. If not, step 2 item 1 needs a different owner.
- I did not look at the repo, so every number above is something you measure in step 1.
- Do you own the `@brindlewood` npm scope personally, or does the company already have an org on npm? Step 5 depends on that.

**Next action:** start the 5-day time log now. Send me the results, and I will turn step 2 into a one-page proposal for your manager.