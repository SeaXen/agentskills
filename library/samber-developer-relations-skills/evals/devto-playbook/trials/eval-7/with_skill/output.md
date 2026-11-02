# Vaultline dev.to plan

## Assumptions

I could not ask the interview questions, so I filled the gaps. Correct me and I'll re-rank.

| # | Question | Assumed answer | What it moves |
|---|---|---|---|
| 1 | Who posts? | The one content marketer, with 1-2 named engineers as organization members. No DEV organization exists yet. | Setup needs an organization, with member accounts that are real people. |
| 2 | Goal and date | A standing channel, started to match a competitor. Start date is Mon 2 Nov 2026. | A standing goal promotes comments and tutorials. There's no launch, so #showdev and #news drop. |
| 3 | Where the original lives | Vaultline blog with RSS. Backlog size unknown. | RSS import into the organization, with canonical ticked. |
| 4 | Hours per week | About 3 for the whole channel. | Under 4 hours a week, so the plan keeps comments and new-post syndication only. Series, #showdev, challenges and paid placements drop. |

## 1. Fit verdict: syndicate only, not invest

- **No try-alone product.** Vaultline has no developer free tier, so there's nothing for a developer to try. The "Invest" case needs a product one developer can try alone.
- **Wrong audience.** Your buyers are bank CISOs and data architects, which is the "enterprise-buyer audience" case.
- **Syndicate-only costs reach.** With weekly comment answers you give up most of the four-day ranking window **[code default]**.

**3 posts a week doesn't fit this skill.** The skill allows one full post every 1-2 weeks, after two weeks of earn-first comments.
- **Reputation.** At 3 a week (about 24 in 8 weeks) a new, link-heavy vendor account looks like a backlink farm. Backlink-purpose posts risk suspension **[platform]**.
- **Spam labeler.** It weighs account age, badges and history **[platform, staff post; code default]**, and domain reputation is shared. One flagged post taints vaultline.com for every later post **[code default]**.
- **Comment capacity.** Nobody can answer comments for two days after each of 3 weekly posts. Unanswered posts earn nothing and cost reputation, which is the skill's "Skip" condition.
- **Rate limits aren't the issue.** 3 a week is far below the caps **[code default]**. The constraint is reputation and capacity.

**Proposal for the CMO:** 3 posts in the first 8 weeks, then reassess at the week-8 gate. Treat the competitor's volume as unverified until someone reads their reactions and comments. Reactions on a dev.to post are not buyer reach for a $220k contract.

## 2. Setup (week 1, about 1.5 h, marketer)

1. **Organization.** Create it from the marketer's personal account. Members join with their own accounts.
2. **Branding.** Add logo, description and links.
3. **Sidebar call-to-action.** Link it to one vendor-neutral canonical page, not a demo form. Clicks on it are your referral metric. The organization setup and its sidebar CTA are the cheapest permanent link DEV gives you.
4. **Engineer accounts.** Each engineer uses a real profile with a bio. Reaction weight ramps from zero to full over an account's first 10 days **[code default]**, so create accounts now.
5. **RSS.** Don't wire it yet (week 3). When you do, tick "Mark the RSS source as canonical URL", because it is opt-in.
6. **No gated content.** DEV bans posts that "merely reference an external link that contains the full post". Syndicated posts must be complete on DEV, with no PDF gate or teaser.

## 3. Ranked surfaces, and what moved

| Rank | Surface | Status for Vaultline | Moved by |
|---|---|---|---|
| 1 | Substantive comments in your tags | **Do, weeks 1-8** | Answer 4: fits under 3 h a week. |
| 1 (tie) | Organization with sidebar CTA | **Do, week 1** | Answer 4: one hour, keeps paying. |
| 3 | Full tutorial under the organization | **Do, 3 posts only** | Answer 4 limits the count. |
| 4 | #discuss question | **Do, once, week 5** | Answer 2: cheap, and you can run it without a launch. |
| 5 | Series | Drop | Answer 4: low effort rating. |
| 6 | #showdev / #news | Drop | Answer 2: there's no launch and no try-alone product. |
| 7 | DEV Challenge entry | Drop | Answer 4. |
| 8 | Billboard, Ads, Takeover, sponsored challenge | Drop | The order starves it. A sponsored challenge needs a free tier a weekend builder can use, and you have none. |

## 4. Per-post tags and rules

- Each post gets a max of 4 tags **[platform]**. Read each tag's sidebar before you pick it. A tag moderator can remove a tag and you can't re-add it.
- **Candidate tags, to verify live:** #security, #dataengineering, #architecture, plus a language or framework tag if the post has code. I haven't checked the current sidebars.
- **Avoid:**
  - **#showdev:** this is not a project or company launch.
  - **#news:** same reason.
  - **#opensource:** project promotion is banned there.
  - **#beginners:** this audience isn't beginners.
- **Disclosure:** set `ai_disclosure_level`. Any post that names Vaultline must be human-written, since AI-assisted business promotion is barred. Use `no_ai` for those. Put the affiliation line in the first paragraph.
- **Content type:** vendor-neutral technical content for data architects (data-lineage patterns, classification trade-offs, retention-policy pitfalls). It shows firsthand experience, with a trade-offs section stating where the approach fails. Product mentions go in the affiliation line and at most one link at the end.
- **Cover image** on every post. The featured slot requires one **[code default]**.

## 5. Eight-week cadence

| Week | Dates | Owner | Hours | Work |
|---|---|---|---|---|
| 1 | 2 Nov | Marketer | 2.5 | Organization and CTA setup. Start earn-first: 3-5 substantive comments in target tags. No links. |
| 2 | 9 Nov | Marketer, engineers | 1.5 | Earn-first continues. Engineers add 1-2 comments each. Choose the best 3 backlog posts. |
| 3 | 16 Nov | Marketer | 3 | Wire the RSS import. Review the drafts it creates. Publish **post 1**, one draft at a time, under the organization. Delete the `date:` line on any old post. Answer every comment within 24 h. |
| 4 | 23 Nov | Marketer | 1.5 | Comments only. Check the dashboard. A US holiday week for bank readers, so no post. |
| 5 | 30 Nov | Marketer, engineer | 3 | **Post 2.** Plus the **#discuss** post, for which an engineer answers. Teammates comment with substance and never react on cue. This is the skill's "launch week, week 5 at the earliest" slot, used for a discussion, not a launch. |
| 6 | 7 Dec | Marketer | 1.5 | Comments, and replies to the #discuss thread. |
| 7 | 14 Dec | Marketer | 3 | **Post 3.** Reply within 24 h. |
| 8 | 21 Dec | Marketer | 1 | Read the dashboard, write the gate memo. No post, because of the holiday week. |

Totals: about 17 hours over 8 weeks, which fits the assumed 3-hour weekly budget. If the marketer can't commit comment answers within 24 hours in weeks 3, 5 and 7, don't publish that week. That is the skill's "Skip" condition.

## 6. Filled templates

**Front matter (post 1)**
```markdown
---
title: Where data-lineage graphs break in a bank's batch estate
published: false
tags: dataengineering, security, architecture
canonical_url: https://vaultline.com/blog/lineage-batch-estate
cover_image: https://vaultline.com/img/lineage-batch-cover.png
ai_disclosure_level: no_ai
description: Three places lineage tooling loses the trail, and what we did about each.
---
```
Publish under the organization from the editor's author menu. If the post is an import of an old one, delete the `date:` line first.

**Affiliation line, first paragraph**
"I work on Vaultline; this post uses it in one example, and the trade-offs section covers where it falls short."

**Earn-first comment**
```text
// ✓ Good
Useful breakdown. One thing that bit us with a similar setup: the
classifier ran on the replica, so a column was tagged "internal" for
about an hour after the schema change. Did you see that lag in your
audit trail?

// ✗ Bad
Great post! Vaultline solves exactly this, check it out: {url}
```

**#discuss post (week 5)**
```text
Title: How do you prove who accessed a column six months ago?
Body: Three approaches we've seen: warehouse query logs, an access
proxy, and policy-as-code with signed decisions. What broke with each
when an auditor asked, and which one survived an actual audit?
```

**Reply to a tag-moderator removal**
```text
Thanks for the note - you're right, this belongs under a different tag.
I've removed it. Is there a tag you'd suggest for the compliance part?
```

**Not used:** the #showdev skeleton, because there's no launch.

## 7. Metrics

DEV publishes no vendor benchmark, so every target is self-set. I have not invented numbers.

- **Monthly:** organization and author followers, CTA clicks, and referral sessions to the canonical page.
- **Per post, at day 4 (not day 30):** reactions and comments.
- **Hygiene, pass threshold zero:** removed tags, spam labels, moderator comments, AI-disclosure notes. A nonzero count in any means stop and fix before the next post.
- **Business gate, week 8:** at $220k per contract, a handful of qualified accounts matters more than reactions. Match referral sessions to target-account domains (see `devrel-analytics`) and have sales say whether any dev.to-referred visitor appeared in a pipeline conversation. If none did, stop and put the hours into a channel where CISOs actually read (my practitioner judgement, not a platform claim).

## 8. If a post is flagged or buried

1. Stop re-posting.
2. Check for a removed tag or a moderator comment, and fix the post against that tag's rule.
3. Appeal once, at dev.to/appeal (signed in) or support@dev.to, describing the fix.

## Open questions for you

1. Is the competitor's dev.to traffic known? Reactions there aren't evidence of buyer reach.
2. Can the engineers commit to 1-2 comments a week each?
3. Is the blog backlog vendor-neutral enough to publish in full, with no gated assets?

I didn't run the sidebar tag checks or the humanizer pass. Run the humanizer on every real draft before publishing.