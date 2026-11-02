# Fixing dev.to reach for a 2-person DevRel team

I followed `devto-playbook` and its `references/templates-and-limits.md`. Your message answered only part of the playbook's interview, so I made assumptions where noted and listed what would change the plan.

Labels follow the playbook: **[platform]** is DEV's own pages and staff posts, **[code default]** is open-source Forem defaults that DEV can override, and **[practitioner]** is community judgement.

## Diagnosis: what is suppressing reach

| # | What you do | Why it hurts | Source |
|---|---|---|---|
| 1 | 300-word summaries ending in "continue reading in the docs" | The terms ban posts that "merely reference an external link that contains the full post". A teaser is also link-heavy, which raises the spam-labeler score. Canonical URLs don't fix this, because canonical covers duplication, not the substantial-content rule. | platform |
| 2 | No cover image | The featured slot requires one, and Top 7 picks rest on editorial feedback, traffic and engagement. | code default, platform |
| 3 | Asking Discord for unicorns | All public reactions score the same, so unicorns don't outrank hearts. Your Discord members' new accounts also get zero reaction weight, ramping to full over 10 days. A group sending 80% of 50+ reactions a quarter to the same few authors gets its reputation halved. A recurring Discord ask to react to your org's posts matches that pattern. | code default |
| 4 | Judging at the end of the month | Default hotness gives recency bonuses for 96 hours, then cuts reaction points to half after 4 days and an eighth after 7. Day 30 shows only what the first four days did. | code default |
| 5 | Probably no comment engagement (unconfirmed) | Weekly publishing with no two-day comment coverage wastes the ranking window. An author's reaction to a comment on their own post counts five times. | code default |
| 6 | Docs-derived content with a docs link | Links to a domain that drew downvotes share reputation across the whole domain. Links from a new or low-badge account weigh heavily in the spam labeler. | code default |

**Stop the unicorn ask today.** Replace it with a request that is allowed and effective: "If this helped, comment with your setup or a question." Substantive comments help ranking, and they carry no manipulation risk.

## 1. Fit verdict

- **Docs-site content is the "Syndicate only" archetype.** At 300-word summaries you currently get the cost of that mode (most of the four-day window given up) with none of the upside.
- **Recommended: Invest, if** a developer can try your product alone in under an hour and someone can answer comments within 24 hours. That is probably true for a 2-person DevRel team, but I haven't confirmed it.
- **Fallback: Syndicate only, if** your buyers are enterprise and the product can't be tried alone. Then import new blog posts only, drop the docs summaries, and answer comments weekly.
- **Skip** if nobody can answer comments. Unanswered teasers cost reputation and earn nothing.

## 2. Setup

1. **Organization.** Keep the org account, but check that both of you are members with your own personal accounts and that the branding is set. Publish under the org byline from the editor's author menu.
2. **Sidebar CTA.** Set the org's sidebar call-to-action and track its clicks.
3. **Personal accounts do the earning.** Reach on the org account comes from the members' standing, so earn-first comments come from your personal accounts.
4. **Syndication.** If you have a blog with RSS, wire the import. Tick "Mark the RSS source as canonical URL", because it is opt-in. Imports land as drafts and keep the original date, so delete the `date:` line before publishing any old post.
5. **Disclosure.** Set the AI tier on every post. Keep product-naming posts human-written (`no_ai`). Don't use AI-written comments.

## 3. Ranked surfaces, and what moved

Your answers moved these rows:

- **Weekly cadence, 2 people:** this implies low hours. If it is under 2 hours a week, keep comments and new-post syndication only.
- **Docs-derived content:** this demotes teasers to last place and promotes full tutorials.

Ranked by value per hour:

1. **Substantive comments in your tags (earn-first).** Compounding, cheap, and you are probably doing none.
2. **Organization setup with sidebar CTA.** One hour, and it keeps paying.
3. **Full tutorial or build log under the org byline.** Replaces your teaser. Highest value, higher effort.
4. **#discuss question your users argue about.** Cheap and one-shot.
5. **Series** (front matter `series:`). Compounding once you have 3+ related posts.
6. **#showdev or #news launch post.** Reserve it for real launches.
7. **DEV Challenge entry.**
8. **Paid placements** (Billboards, Ads, Takeover). Skip for now.

## 4. Fix the post format

Turn each docs page into a **full post** that stands alone on DEV:

1. Problem in one paragraph.
2. The complete working steps, with the code, in the post itself.
3. One trade-off, plus what it doesn't do.
4. One question for readers.
5. A single docs link at the end, as "full reference", not as the point of the post.

Length is roughly 800-1,500 words, and a post is only a summary of the docs if you can delete the link without losing it.

Per-post checklist:

- Cover image (add one every post).
- All four tag slots, each chosen against its sidebar rule.
- AI tier set. First paragraph states affiliation: "I work on {product}; this post uses it, and the trade-offs section covers where it falls short."
- Distinct title (the same title a third time in a day gets an automatic spam label).
- `canonical_url` set only if the original lives elsewhere.

## 5. Tags, with rules

- **#showdev**: your project launch; not overly corporate or salesy.
- **#news**: a launched or updated product, with a brief summary and the source.
- **#discuss**: a question or prompt that starts a discussion.
- **#beginners**: only for beginners to programming or a language, not "new to our tool". A 1-2 sentence plug at the end is allowed.
- **#opensource**: bans project promotion, announcements and contributor requests. Don't use it for product posts.
- **Language and framework tags**: add the framework tag.

A tag moderator can remove a tag and you can't re-add it. If one is removed, check the sidebar rule and reply politely. Use the playbook's reply template.

## 6. Eight-week cadence

Owners are A and B (your two people). Total is about 3 hours a week each; adjust if your real budget is lower.

| Week | Action | Owner | Hours |
|---|---|---|---|
| 1 | Stop the unicorn ask. Fix org setup and CTA. Each person comments substantively on 3-5 posts in your tags, with no links. | A+B | 2 each |
| 2 | Same comments. Pick 3 docs pages to rewrite as full tutorials. Make cover images. | A+B | 3 each |
| 3 | Publish tutorial 1 (full, with cover). Answer every comment within 24 hours for 4 days. Comment on others' posts as in weeks 1-2. | A | 3 |
| 4 | Publish a #discuss post. Continue comments. | B | 2 |
| 5 | Publish tutorial 2. Read day-4 numbers for posts 1 and 2. | A | 3 |
| 6 | Publish tutorial 3 and start a series. | B | 3 |
| 7 | Publish tutorial 4. Drop tags that drew nothing. | A | 3 |
| 8 | Launch week if you have a real launch: one story-led #showdev plus one #discuss question. Teammates comment with substance and never react on cue. Review all metrics. | A+B | 4 |

Post one full piece every one or two weeks, not weekly. Quality at 2-week intervals beats teasers at 1-week intervals, because you can cover each post's four-day window.

## 7. Templates

**Earn-first comment** (no link, adds a fact):

```text
Nice write-up. One thing that bit us with the same setup: the pool
closes idle sockets after 60 s, so the first request after a quiet
period pays the TLS handshake. Did you see that in your p99?
```

**Bad** (don't do this): `Great post! We built {product} to solve exactly this, check it out: {url}`

**Front matter** for each tutorial:

```markdown
---
title: <concrete outcome in the title>
published: false
tags: <4 tags, each checked against its rule>
cover_image: <absolute URL>
series: <series name, once you have 3+ posts>
ai_disclosure_level: no_ai
description: <one sentence>
---
```

**Replacement for the Discord ask:** "We posted a walkthrough of X on dev.to. If you've hit this problem, comment with what you did, and we'll answer."

**#discuss post** (use as a pattern):

```text
Title: How do you test webhooks locally without exposing your laptop?
Body: Three approaches we have tried (tunnel, replay from logs, local
mock server), what broke with each, and the question: which one
survived contact with your CI?
```

**Reply to a tag-moderator removal:**

```text
Thanks for the note - you're right, this is a project announcement, not
an open-source practice post. I've kept #showdev. Is there a tag you'd
suggest for the release notes part?
```

## 8. Metrics

DEV publishes no vendor benchmark, so targets are self-set.

- **Per post, at day 4, not day 30:** reactions and comments. Your baseline is about 3 reactions a post, read at day 30. Re-baseline at day 4 on your next posts, then set the target from that.
- **Monthly:** organization and author followers, CTA clicks, and referral sessions to the docs page. Attribute signups with `devrel-analytics`.
- **Hygiene, pass threshold zero:** removed tags, spam labels, moderator comments, AI-disclosure notes.
- **Read monthly** from the org dashboard, and drop tags that drew nothing.

## 9. If a post is flagged or buried

1. Stop re-posting, because a repeat makes it worse.
2. Check for a removed tag or moderator comment, and fix the post against the tag rule.
3. Appeal once, at dev.to/appeal (signed in) or support@dev.to, describing the fix.

## What would change this plan

- **Hours per week.** Under 2 hours: comments plus new-post syndication only.
- **Who answers comments within a day.** If nobody can, the verdict becomes Skip.
- **Whether the product is tryable alone.** If not, the verdict becomes Syndicate only.
- **Your goal and date.** A launch date promotes #showdev, #news and #discuss, and moves the launch to week 5 at the earliest.
- **Whether your current posts used AI drafting.** If they did and the tier wasn't set, set it now. Product posts need to be human-written.

Run the finished drafts through your preferred humanizer skill. For writing the tutorials themselves, use `engineering-blog-post`.