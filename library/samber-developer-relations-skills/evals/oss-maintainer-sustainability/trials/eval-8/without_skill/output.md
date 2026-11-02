Don't do it as written. Two of the three steps work against your goal, and the third is an irreversible one you can do later and more safely.

## Verdict

| Step | Call | Why |
|---|---|---|
| Restrict PRs to collaborators | ❌ Drop | It cuts the pipeline that produces your next maintainers. |
| SEEKING MAINTAINERS banner | ⚠️ Change | It recruits strangers, and you already have two candidates. |
| Full write plus org ownership to the first applicant | ❌ Never | It is the riskiest way to share the keys. |
| Ask Saltmarsh for a donation | ⚠️ Change | Ask what they will fund, not for a generic donation. |

## What to do instead

1. **Ask Ifeoma and Dusan this week.** They have already reviewed PRs and answered Discussions, so a banner is the wrong first move. Ask each one privately whether they want a maintainer role and how many hours a month they can give. Their answers decide everything else. If either says no, you need the banner after all, but run it on the ladder below.
2. **Give them merge rights now.** Write access to merge is cheap to grant and cheap to revoke. It also fixes your bus factor of 1 fastest. Protect the main branch and require 1 review, so you review each other.
3. **Hold the keys for a few months.** Org ownership, release signing, and registry or publish tokens are different. A bad release ships before anyone notices, and the xz-utils backdoor is the cautionary case. Be generous with the ladder and slow with the keys. Tell them the pause is policy, not distrust.
4. **Still get a second org owner.** One owner is a single point of failure, but pick a named person you know, not whoever applies first. Make it Ifeoma or Dusan after about 3 months. Also give two people each release credential.
5. **Fix the PR flood without closing the door.** Closing PRs to outsiders also closes your recruiting channel. Instead:
   - Require an issue first for anything non-trivial.
   - Add a PR template and a short CONTRIBUTING file.
   - Add a stale-PR auto-close.
   - Label `good first issue` for what you want.
   - Let Ifeoma and Dusan share first-pass triage.

   GitHub's temporary interaction limits are a fine pressure valve for a few weeks, not a policy.
6. **Write a one-page GOVERNANCE.md and a MAINTAINERS file.** Use a three-person council with these rules:
   - Routine changes go by lazy consensus.
   - Contested changes get a time limit, then a majority vote.
   - Adding or removing a maintainer needs a vote.
   - Include an inactivity rule, an emeritus path, and a named end state.

   It should cost about an hour a month. Don't build an elected committee for a project this size.
7. **Reshape the Saltmarsh ask.** The CTO asked how to "support the project", so find out what that can mean, then offer a menu:
   - **Money**, earmarked for maintainer time: triage, review, and release work. GitHub Sponsors to individuals is the simplest route. A fiscal host such as Open Source Collective makes sense if you want one entity to hold funds. Check taxes and contracts with counsel.
   - **Engineer hours**: a Saltmarsh engineer contributing as a normal contributor.
   - **Credit**: a sponsor listing, if they want it.

   Money buys time and review. It does not buy a maintainer seat, a vote, or a key. Say that upfront, and cap any one employer's seats. Also ask other big importers, since you have about 3,500 importing modules.

## Why the original plan backfires

- **Collaborator-only PRs** make "become a maintainer" the only path to contribute. Your current reviewers earned trust by working in the open, and this stops the next ones from doing the same.
- **A banner plus first-come, full access** selects for whoever is fastest, not whoever is trusted. A tired solo maintainer handing over everything is how takeovers happen.
- **Ownership on day one** is hard to undo and gives the new owner the power to remove you.
- **A donation first, structure second** means money arrives with no rule for who decides how it is spent. Write the council rules before the first payment.

## Timeline

| Task | Time |
|---|---|
| Talk to Ifeoma and Dusan | 2 chats, about 30 min each |
| Branch protection and merge rights | 15 min |
| PR template and CONTRIBUTING | about 1 hour |
| GOVERNANCE.md and MAINTAINERS | about 2 hours |
| Reply to Saltmarsh | 20 min |
| Second org owner and release keys | about 3 months from now |

## Open questions

- Do Ifeoma and Dusan work for the same employer, or for Saltmarsh?
- Who holds the repo owner role, the publish credentials, and the domain today?
- Is there an existing license or contributor agreement you want to keep as is? Questions about changing it go to counsel.

## Next action

Message Ifeoma and Dusan today: "I want to share maintainership. Would you take merge rights, and how many hours a month could you give?"