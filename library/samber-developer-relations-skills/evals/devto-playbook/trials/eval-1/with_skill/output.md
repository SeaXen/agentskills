# Flagpole dev.to plan: sanity check

**Verdict: ❌ don't run the Monday plan.** Each of its four parts either breaks a rule in the dev.to playbook or triggers a penalty. A slower version of the same goal works, and it's below.

Labels: **[platform]** = DEV pages and staff posts. **[code default]** = open-source Forem code, which DEV can override. **[practitioner]** = community judgement.

## 1. Fit verdict

**Invest, for a subset of the posts.** A TypeScript MIT SDK that one developer can try alone suits dev.to. The 40 marketing posts are probably not all a fit. Buyer-facing or docs-style posts belong in "syndicate only" mode.

I assumed these answers. Correct me where they're wrong, since each one re-ranks the plan:
- **Poster:** a named engineer (you or a maintainer) plus the 12 engineers under a Flagpole organization.
- **Goal:** a standing tutorial channel, with no hard launch date. A launch date would promote #showdev, #news and #discuss.
- **Backlog:** 40 posts on blog.flagpole.dev with RSS, including old ones.
- **Time:** under 2 hours a week, with comments answered within 24 hours. If nobody can do that, skip dev.to. Unanswered posts cost reputation and earn nothing.

## 2. What breaks in the Monday plan

| Plan item | Problem | Source |
|---|---|---|
| Fresh account `flagpole` | A brand-new account posting links gets weighed by the spam labeler, which looks at account age, badges and history. Create the organization from a personal account instead. | platform, code default |
| Import and publish all 40 on one day | A new account is limited to 1 article in its first 3 days. Forty links to one domain also share domain reputation: one spam flag poisons all of them. | code default |
| Publish imports unedited | Each draft keeps the original post's date. An old post published with its `date:` line goes out back-dated, outside the signed-in feed, permanently. | code default |
| Same 4 tags on all 40 | #opensource bans project promotion, announcements and contributor requests. #beginners means beginners to programming or a language, not "new to Flagpole". A tag moderator can remove a tag and you can't re-add it. | platform |
| 12 engineers heart and unicorn every post in hour 1 | That's about 480 reactions from 12 accounts to 1 author, so it matches the reaction-ring pattern (50+ reactions a quarter, 3+ accounts, 80% to the same few authors). Reputation gets halved. It also violates the engagement-manipulation rule. | platform, code default |
| Skipping earn-first | Posts with links from an account with no standing get buried. | practitioner |

Two more points on reactions:
- Reaction weight ramps from zero to full over an account's first 10 days, so day-one reactions from new accounts count for little.
- All public reactions score the same, so asking for unicorns buys nothing.

Also check these:
- **Full post on DEV.** Terms ban posts that merely reference an external link holding the full content. Teasers fail, and a canonical URL doesn't fix that.
- **AI disclosure tier.** Every post needs a tier: Hand Written, AI-Assisted or Fully Autonomous. If marketing used AI drafting on posts that name Flagpole, those posts are barred as promotion. Ask marketing which of the 40 were AI-drafted before importing any.

## 3. Setup

1. **Organization.** You create "Flagpole" from your own personal account. The 12 engineers join with their own accounts. Add branding and a sidebar call-to-action pointing at the SDK quickstart, not the pricing page.
2. **RSS import.** Point it at the feed, into the organization.
   - Tick "Mark the RSS source as canonical URL". It's opt-in.
   - Imports land as drafts, and the first four blog categories become tags.
   - On each draft, delete the `date:` line, set tags, add a cover image and set the AI tier.
3. **Pick 6-8 posts, not 40.** Take full tutorials and build logs about the SDK. Leave release notes, enterprise posts and pricing posts on the blog. Publish them one at a time.

## 4. Ranked surfaces, and what moved

Ranking by value per hour: substantive comments in your tags = organization setup, then full tutorials and build logs under the organization, then a #discuss thread, then series, then #showdev or #news, then a DEV Challenge entry, then paid placements.

- Under 2 hours a week moved me to **comments plus new-post syndication only**. Series and challenges drop out.
- No launch date means #showdev and #news wait. They come in the launch window, not now.

## 5. Tags per post

Pick the four slots per post, each by its rule. Don't copy one set across posts.

| Tag | Use it when | Don't |
|---|---|---|
| `typescript` or `javascript` | The post is code-focused. Add the framework tag (React, Node) if it applies. | Add it to a non-code post. |
| `webdev` | The post is about web development. | Treat it as a catch-all. |
| `opensource` | The post covers running or licensing an open-source project, or advocacy. | Use it for SDK promotion or release announcements. |
| `beginners` | The post teaches beginners to programming or a language. A 1-2 sentence plug at the end is allowed. | Use it for "new to feature flags". |
| `discuss` | The post asks a real question. | Add it to a how-to. |
| `showdev` | It's your project or company launch, "not overly corporate or salesy". | Use it for a routine cross-post. |
| `news` | A launched or updated product, with a brief summary and the source. | Use it without the summary. |

## 6. Cadence (starts Monday 2026-11-02)

Hours are for the whole team and assume the under-2-hours constraint.

| Weeks | Action | Owner | Hours/wk |
|---|---|---|---|
| 1-2 (Nov 2-15) | **Earn first.** Each poster leaves substantive comments on 3-5 posts a week in the target tags. No links. Create the organization. | You + engineers | 1.5 |
| 3 (Nov 16) | **Wire syndication.** Set up RSS import, publish the best draft only. | You | 1.5 |
| 3-8 (Nov 16-Dec 27) | **Publish one full post every 1-2 weeks.** Answer every comment within 24 hours. | You + the post's author | 2 |
| 5 at the earliest (Nov 30) | **Launch week.** One story-led #showdev post and one #discuss question. Teammates comment with substance and never react on cue. | You | 2 |
| Monthly | Read the organization dashboard. Drop tags that drew nothing. | You | 0.5 |

Publish only when someone can answer comments for two days. Default ranking gives recency bonuses for 96 hours, then cuts reaction points to half after 4 days and an eighth after 7. Weeks 7-8 land around the holidays, so push those posts to January if nobody's around.

On reactions, do the legitimate version of your idea:
- Engineers write real comments with a fact the author can use.
- Heart good comments on your own post. An author's reaction to a comment there counts five times.

## 7. Templates

**Front matter for each syndicated post:**

```markdown
---
title: <original title>
published: false
tags: typescript, webdev, <framework>, <fourth tag by rule>
canonical_url: https://blog.flagpole.dev/<slug>
cover_image: <url>
ai_disclosure_level: no_ai
description: <one sentence>
---
```

`ai_disclosure_level` takes `no_ai`, `some_ai` or `fully_autonomous`. Publish under the organization from the editor's author menu. Remove any `date:` line first.

**Affiliation line, first paragraph:** "I work on Flagpole; this post uses it, and the trade-offs section covers where it falls short."

**Earn-first comment:**

```text
// ✓ Good - adds a fact the author can use, no link
Nice write-up. One thing that bit us with the same setup: <specific
detail from your experience>. Did you see that in <their metric>?

// ✗ Bad - praise plus product link
Great post! We built Flagpole to solve exactly this, check it out: {url}
```

**#showdev skeleton:**
1. The problem in one paragraph, from your own use.
2. What you built, with a screenshot or GIF and the install command.
3. How it works: one design decision and its trade-off.
4. What it doesn't do yet.
5. One question for readers. One link, at the end.

## 8. If a post is flagged or a tag is removed

1. Stop re-posting. A repeat makes it worse.
2. Check for a removed tag or a moderator comment, and fix the post against the tag rule.
3. Appeal once, at dev.to/appeal (signed in) or support@dev.to, describing the fix. A human reviews it.

## 9. Metrics

Targets are self-set, because DEV publishes no vendor benchmark.
- Organization and author followers, monthly.
- Sidebar call-to-action clicks and referral sessions to the canonical page.
- Reactions and comments per post at **day 4**, not day 30.
- Hygiene, pass threshold zero: removed tags, spam labels, moderator comments, AI-disclosure notes.

## 10. Questions that would change the plan

1. How many hours a week, and who answers comments within a day?
2. Which of the 40 posts were AI-drafted, and which name Flagpole?
3. Is there a launch date (for example SDK v-next) that should anchor the #showdev post?
4. Which 6-8 posts are developer tutorials or build logs rather than buyer-facing content?