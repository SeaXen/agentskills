**Do this first:** send both PMs one message today asking for a named owner of "status decisions" on the portal. The ask is 20 minutes a week, starting at launch. Draft is in section 6.

Your plan assumes the PMs will come around once requests are organised and voted on. I wouldn't count on it. A voting board with no one setting statuses turns into a graveyard. Your 4,000 members vote, see "New" for months, and stop trusting you. Everything below makes it cheap for the PMs to engage, and includes a fallback if they don't.

## 1. Rules that shape the design

- DevRel owns intake, dedupe, and evidence. PM owns priority and the statuses `Planned`, `In progress`, `Not planned`. You never set those.
- Votes are signal, not priority. Rank by distinct accounts and by blocking impact. Discord loudness is not demand.
- Bugs stay in GitHub or support. Only requests and improvements go to the portal.
- One record per request. Search before you create. Merge duplicates and carry the voters over.
- Budget is about 3 hours a week for you. If a step needs more, cut it.

## 2. Intake pipeline

Volume is about 30 Discord posts a week, plus a few tickets and a few GitHub issues. That is roughly 40 items a week, so manual triage with light automation is enough. Don't build bots yet.

**Discord (#feature-requests)**
1. Pin a post template: problem, what you tried, SDK language, workaround.
2. Run a sweep twice a week (Tue and Fri, 30 minutes). Log real requests into the portal.
3. Mark each logged post with ✅ and reply with the portal link. Reply "needs more info" and ask one question for posts that are unclear.
4. Questions and bug reports are not requests. Redirect them to support or GitHub, and don't log them.
5. Record the reaction count in the portal item's note as "Discord: N reactions". Do not import reactions as votes.
6. Later, if volume grows, convert the channel to a Discord forum so each request is a thread.

**Support tickets**
1. Ask support to add a `feature-request` tag in their tool and keep forwarding. Ask for ticket link, account name, and plan.
2. Create or find the portal item, and add the customer as a voter on their behalf if the portal allows it.
3. Mark the item's source `support`. Keep customer names in private fields or notes only.
4. Never paste ticket text publicly. Rewrite it as a problem statement.

**GitHub (Node and Go SDK repos)**
1. Maintain one label on SDK issues: `enhancement`. Bugs keep their own labels.
2. For each `enhancement`, create a portal item linking the issue URL, and comment the portal link on the issue.
3. GitHub stays the source of truth for SDK implementation. The portal tracks demand. The sync is one-way and manual, once a week.
4. If your portal has a GitHub integration, use it only after the manual flow works for four weeks.

**Item template** (portal description, for every item)
```
Problem: what the user is trying to do (not the solution)
Current workaround: none | describe
Blocking: yes (can't adopt / at risk) | no
SDK/language: Node | Go | API | Console | n/a
Evidence: Discord link / ticket # / GitHub issue
```

**Dedupe rule:** search by 2 keywords before creating. If a match exists, add the voter and the evidence link. Don't create a near-duplicate.

## 3. Label taxonomy

Five facets. Each item gets exactly one Type, one Area, one Source, plus optional flags.

**Type (pick one)**
- `feature`: new capability
- `improvement`: change to existing behaviour
- `docs-gap`: docs or examples missing (route to docs backlog)
- `integration`: connector or framework support

**Area (pick one)**
- `publish-consume`
- `delivery-retries`
- `dead-letter`
- `auth-security`
- `observability`
- `limits-billing`
- `sdk-node`
- `sdk-go`
- `console`

**Source (pick one):** `discord`, `support`, `github`, `sales-other`. If an item has several sources, keep the first and add the rest as evidence links.

**Flags (optional)**
- `blocking`: user says they can't adopt or may leave
- `no-workaround`
- `paying-account`: at least one paying account asked
- `quick-win`: your guess of small effort, with no PM sign-off needed

**Status**

DevRel can set:
- `New`
- `Needs info`
- `Under review` (means a PM has seen it, not DevRel)
- `Duplicate`

PM only:
- `Planned`
- `In progress`
- `Shipped`
- `Not planned`

Treat `Under review` as PM-owned too. Until a PM owns it, items stay `New`. Honest statuses protect your credibility.

Don't add more labels in the first six weeks. Review the set at week 6 and merge any label that holds fewer than 3 items.

## 4. Weekly digest to PMs

Send every Friday morning. Cap at 250 words. It must be readable in five minutes and answerable with a one-word reply.

```
Subject: Fernhollow feedback, week N: 1 decision needed

DECISION NEEDED (reply with A or B)
[Item title] — N accounts, M votes, blocking: yes/no.
  A) Mark Planned/Under review  B) Mark Not planned (I'll tell users why)
  Default if no reply by Tue: stays New, appears again next week.

TOP 5 BY DISTINCT ACCOUNTS (this quarter so far)
1. Title — accounts, votes, flags, link
...

NEW THIS WEEK
N new, M merged as duplicates. Notable: title, title.

BLOCKING / AT-RISK
Item — who said what, link. (Omit section if none.)

SHIPPED / CLOSED
What we told users this week. (Closing the loop.)

STATS: logged N | by source: discord/support/github | untriaged by PM: N
```

Rules for the digest:
- One decision ask a week, maximum. A long list of asks gets ignored.
- Top 5 ranks by distinct accounts first, votes second.
- Never put customer names in it if the digest goes beyond the PMs.
- Track whether they open it and reply. That is your adoption metric.

## 5. Timeline

**Weeks 1 to 2 (before portal is live): about 8 hours total**
1. Ask PMs for the owner (section 6). 5 minutes.
2. Set up the taxonomy in a spreadsheet and test it on the last 4 weeks of #feature-requests. About 2 hours.
3. Backfill the top 30 items so the portal doesn't launch empty. About 3 hours.
4. Write the launch post: "We read this weekly. Voting is a signal, not a commitment. Statuses are set by product." About 30 minutes.

**Weeks 3 to 6: about 3 hours a week**
- Run the sweeps, send the Friday digest.
- Week 4: first label review.

**Week 6: Q3 planning brief (about 3 hours)**
- One page for the PMs: top 10 by distinct accounts, all blocking items, quick wins, and what users said in their own words.
- Hand it over a week before planning, as the input they can use directly.

## 6. Ownership ask (send today)

```
Hi [PM1], [PM2],

The feedback portal goes live in about two weeks. I'll handle intake,
dedupe and a Friday digest (250 words max). What I need from product:
one named person who sets statuses (Planned / Not planned / Shipped)
once a week, about 20 minutes.

Without that, every item sits at "New" and users lose trust in the
board. Who can be that person, even as a delegate until Q3 planning?
```

**If both decline:**
1. Launch anyway, but say so in the launch post: statuses are `New` only until product reviews.
2. Send the digest anyway, and raise the lack of replies to their manager or the head of engineering after three digests.
3. Use the week 6 brief as the lever. Q3 planning is the moment they will read it.

## 7. Risks

- **Loud-minority bias:** Discord skews to hobbyists and free users. The `paying-account` flag and account-based ranking counter this.
- **Public promises:** `Planned` is read as a date. Only PMs set it, and the launch post says it is not a commitment.
- **Your time:** if sweeps pass 3 hours a week, drop the Discord reaction counts first, then the GitHub sync.
- **Data in public:** no customer names, ticket text, or internal pricing in public items.

**Next:** paste the section 6 message to the two PMs, and ask for a reply by Friday.