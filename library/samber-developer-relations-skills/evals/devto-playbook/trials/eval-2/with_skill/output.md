# Ratchet on dev.to: what to change in the current workflow

**Verdict: yes, change four things.** Two of them (AI drafting, and posting from personal accounts with a pricing CTA) are the kind of thing that gets posts removed or accounts suspended. Volume at 3 a week is possible only if the rest of the workflow changes first.

I applied the `devto-playbook` skill and its limits reference. I did not check the live DEV guidelines. The AI rules change often, so re-read them before you roll this out.

## 1. AI drafts with PM approval don't count as AI-Assisted

- **[platform]** Every post needs an AI tier: Hand Written, AI-Assisted or Fully Autonomous.
- **[platform]** "Claude drafts, PM skims and approves" stays **Fully Autonomous**. Approval alone doesn't change the tier. Only a meaningful human rewrite makes a post AI-Assisted.
- **[platform]** The AI guidelines also bar AI-assisted posts that promote a business, including your own. Your posts name Ratchet and end with a pricing CTA, so they are promotion.
- **Change:** Engineers write product-naming posts by hand, with `ai_disclosure_level: no_ai`. Claude can still help with research, outlines, code checking and grammar. Don't let it produce the body.
- **Disclosure:** If an engineer uses AI help on a post, set `some_ai`. Add the closing line: "Drafted with AI help; code and numbers were run and checked by me."
- **Comments:** No AI-written comments. Translation and grammar tools are the only exception.
- **Why the tier matters:** Readers can down-rank AI tiers in their feed **[platform]**. Undisclosed or heavy AI risks suspension.

## 2. Post under a Ratchet organization, not personal accounts

- **[platform]** The AI guidelines exempt company-blog links only when the post sits under the company's DEV organization. Backlink-driven posts from personal accounts risk suspension.
- **[code default]** Spam scoring weighs account age, badges and history. Links from new or low-badge accounts score worse.
- **[code default]** Domain reputation is shared. If one engineer's post gets downvoted for ratchet.dev links, every teammate pays for it.
- **Change:**
  1. Create a Ratchet organization from one personal account. Other engineers join with their own accounts.
  2. Publish from the editor's author menu under the organization, with each engineer as the byline.
  3. Put the pricing link in the **organization sidebar CTA**. DEV shows it on every org post, so you don't need a per-post pricing pitch.
- **Why the org doesn't fix promotion:** The org exempts a backlink, not promotion. A post that exists only to sell still fails.

## 3. Take the pricing CTA out of the post body

- **[platform]** Terms ban content "designed primarily for the purposes of promotion or creating backlinks". They also ban posts that merely point to an external page for the full content.
- **Change:**
  - Every post must stand alone as a full tutorial, build log or lesson, with its code in the post.
  - The body can link to docs or the relevant product page where a reader needs it.
  - Drop the pricing link from the end of the post.
  - Use the first-paragraph affiliation line: "I work on Ratchet; this post uses it, and the trade-offs section covers where it falls short."
  - Include a "what it doesn't do" or trade-offs section.
  - Disclose affiliate links if you ever have any.
- **If you cross-post from your blog:**
  - Set `canonical_url`, and tick "Mark the RSS source as canonical URL" if you use RSS import.
  - Delete the `date:` line before publishing an old post. Otherwise it goes out back-dated and outside the signed-in feed, permanently.
  - Canonical doesn't excuse a teaser. DEV needs the full post.

## 4. Three posts a week is the weakest part of the plan

The skill's cadence is one full post every one or two weeks. I'm treating that as a practitioner guideline, not a platform limit. It doesn't prove 3 a week is forbidden, but three things argue for fewer:

- **Comment load.** You should be able to answer comments for two days after each post. Default hotness gives recency bonuses for 96 hours, then halves reaction points after 4 days and cuts them to an eighth after 7 **[code default]**. At 3 posts a week, 6 or more posts are in their ranking window at once. Each needs an owner replying within 24 hours.
- **Signal dilution.** The signed-in feed matches readers' interests and followed tags **[platform]**. Three promotional-looking posts a week from one domain raise your odds of the downvotes that damage domain reputation.
- **Earn-first is missing.** The playbook starts with 1-2 weeks of substantive comments (3-5 per poster per week) with no links. The new accounts also carry the strictest rate limits in their first 3 days.

**Recommendation:**

- Publish **1 full post a week at first**, written by hand. Move to 2 once comment response stays under 24 hours.
- Fill the other slots with surfaces that cost less:
  - Substantive comments in your tags, which are the highest-value surface per hour.
  - A #discuss question your users argue about.
  - A series, once you have two posts that fit together.
- Keep the other posts on your own blog.
- If leadership still wants 3 a week, treat it as an experiment. Run it only if every post has a named human author and a named comment-answerer. Review the hygiene metrics after 4 weeks, and cut back if any of them is above zero.

## Revised eight-week plan

| Weeks | What happens | Owner |
| --- | --- | --- |
| 1-2 | Each engineer comments substantively on 3-5 posts a week in target tags, with no links. Create the org, add members, set the sidebar CTA to ratchet.dev/pricing. | Each engineer, plus the org admin |
| 3 | Wire RSS import if you have a blog backlog. Publish the best drafts one at a time, with canonical URL set and the `date:` line removed. | Content lead |
| 3-8 | Publish 1 hand-written post a week under the org. Answer every comment within 24 hours. | Post author |
| 5+ | Launch week at the earliest. One story-led #showdev post plus a #discuss question. Teammates comment with substance, never react on cue. | Product + DevRel |
| Monthly | Read the org dashboard. Drop tags that drew nothing. | DevRel |

## Rules for every post

- Use at most four tags, each chosen by its sidebar rule.
- Treat a tag-moderator removal as final. The author can't re-add the tag.
- **#showdev** is for your project or company launch, "not overly corporate or salesy".
- **#news** is for a launched or updated product, with a brief summary and the source.
- **#beginners** is for beginners to programming or a language, not "new to Ratchet".
- **#opensource** bans project promotion, so skip it for product posts.
- Add a cover image. The featured slot requires one.
- Don't ask for unicorns or coordinate reactions. All public reactions score the same.
- A heavy-reactor group sending 80% of its reactions to the same few authors gets its reputation halved **[code default]**. Don't have the team react to each other's posts on cue.
- Don't reuse the same title three times in a day. DEV labels that spam automatically.

## Front matter template

```markdown
---
title: <specific, problem-first title>
published: false
tags: <up to 4, each fitting its tag rule>
canonical_url: https://ratchet.dev/blog/<slug>   # only if cross-posting
cover_image: https://ratchet.dev/img/<cover>.png
ai_disclosure_level: no_ai
description: <what the reader will learn>
---
```

## Metrics

Targets are self-set, because DEV publishes no vendor benchmark.

- **Monthly:** org and author followers, sidebar CTA clicks, and referral sessions to ratchet.dev.
- **Per post, at day 4 (not day 30):** reactions and comments.
- **Hygiene, pass threshold zero:** removed tags, spam labels, moderator comments, AI-disclosure notes.
- **Stop rule:** If hygiene is above zero, stop re-posting. Fix the post against the tag rule, then appeal once at dev.to/appeal or support@dev.to.

## Questions that could change this

1. Do you already have a Ratchet organization on dev.to, and how old and established are the engineers' accounts?
2. How many hours a week can the team give this, and who answers comments within a day? Under 2 hours a week means comments and syndicating new posts only.
3. Is the goal adoption from a launch, a standing tutorial channel, or hiring? A launch date raises the priority of #showdev and #discuss.
4. Where do the originals live? If you can only post to dev.to, canonical and RSS don't apply.

If nobody can answer comments within a day, the skill's verdict is **skip**. Unanswered posts cost reputation and earn nothing.