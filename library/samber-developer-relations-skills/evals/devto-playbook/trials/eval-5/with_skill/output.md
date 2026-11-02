# tidepool v1.0 on dev.to: launch plan

Three parts of the request don't work on dev.to as asked:

1. **#opensource is the wrong tag.** It bans project promotion, announcements and contributor requests, and this post is all three. A tag moderator can remove it, and you can't re-add it. I swapped it out (see the tags section).
2. **You can't pay to pin a post to the homepage.** The playbook documents no such product. The paid options are DEV Ads, Takeover, sponsored Challenges (partners@dev.to) and promoted Billboards (Pro Tools, org admin). Those are labelled ads, not your article pinned as featured. Featured placement is editorial and ranking-driven **[code default]**, and it requires a cover image. The weekly #top7 picks rest on editorial feedback, traffic and engagement **[platform]**. Ask partners@dev.to if a paid featured slot exists today. I haven't verified that one way or the other.
3. **Listings are gone.** Billboards replaced them. They're free beside your own organization's posts and paid when promoted **[platform]**. Contributors come from the #contributorswanted tag and a free Billboard on your org's posts.

## Assumptions to correct

I answered these myself so the plan could be complete. Tell me which are wrong, because they move the plan.

- **Launch:** Tuesday 2026-11-03. It's Friday 2026-10-30 now, so you have 4 days.
- **Poster:** a named maintainer under a new `tidepool` DEV organization.
- **Original post:** it lives on your blog, and you'll cross-post with `canonical_url`.
- **Hours:** about 5 per week, with someone able to answer comments within 24 hours for 4 days.
- **Language:** unknown. I left a slot for the language or framework tag.

## 1. Fit verdict

**Invest.** A CLI one developer can try alone suits dev.to, as long as someone answers comments daily.

If nobody can answer comments Tuesday through Friday, skip the launch post. Unanswered posts cost reputation and earn nothing.

## 2. Setup (do today)

1. Create the `tidepool` organization from a personal account. Members join with their own accounts.
2. Set org branding and a sidebar call-to-action that links to the repo or install page, so you can see its clicks.
3. Don't run RSS import for this post. Write it natively, and copy the blog URL into `canonical_url` if a blog version exists. For later imports, tick "Mark the RSS source as canonical URL" and delete the `date:` line from old drafts.
4. Check each account's age. Accounts under 3 days old are limited to 1 article and 1 comment per 300 s **[code default]**.
5. Reaction weight ramps over an account's first 10 days **[code default]**. New teammate accounts add almost nothing on launch day.

## 3. Ranked surfaces, and what moved

The launch date and the budget changed the order.

| Rank | Surface | What moved it |
| --- | --- | --- |
| 1 | Substantive comments in your tags, link-free, Fri–Mon | Earn-first is compressed to 4 days. It's shortened, never skipped. |
| 2 | Organization with sidebar CTA | Takes one hour and keeps paying. |
| 3 | **#news release post** (the deliverable below) | The launch date promoted it. |
| 4 | **#discuss question** in launch week | The launch date promoted it. |
| 5 | Full tutorial under the org, weeks 3–8 | Your hours per week keep it to one post every 1–2 weeks. |
| 6 | Promoted Billboard, DEV Ads, Takeover | Paid ranks last on value per hour and compliance cost. |

**Budget:** hold the few thousand dollars. Nothing the playbook documents justifies spending it before the post has day-4 numbers.

- If you still want paid reach after day 4, test one promoted Billboard via Pro Tools. Cap the test at a small slice of the budget.
- Only consider a sponsored Challenge if tidepool has a free tier a weekend builder can use.
- The playbook gives no prices, so get quotes from partners@dev.to.

## 4. Tags for the post (max 4)

| Tag | Rule | Verdict |
| --- | --- | --- |
| #news | A launched or updated product, with a brief summary and the source. | Keep. |
| #contributorswanted | Contributor requests. | Keep. |
| #opensource | Running projects, licensing, advocacy. Project promotion, announcements and contributor requests are banned. | **Drop.** |
| #productivity | The playbook doesn't cover it. | Keep only if its sidebar rules allow product-release posts. Check the tag's about page first. |
| Language or framework tag | Focused content. | **Add** (e.g. `go`, `rust`, `node`). |

Final set: `news, contributorswanted, <language>, productivity`.

If #productivity's sidebar excludes launch posts, use `showdev` instead. #showdev fits a project launch if the tone is "not overly corporate or salesy."

## 5. The post (human-written)

The post names your product, so keep it human-written. AI-assisted posts that promote your own business are barred under the live guidelines. Use full content on DEV, not a teaser. Titles and numbers below are placeholders, so fill in real ones.

````markdown
---
title: tidepool 1.0 is open source: <one-line result, e.g. "one command replaces our 40-line deploy script">
published: false
tags: news, contributorswanted, <language>, productivity
canonical_url: https://<your-blog>/tidepool-1-0   # delete if DEV is the only home
cover_image: https://<your-host>/tidepool-1-0-cover.png   # required for the featured slot
ai_disclosure_level: no_ai
description: tidepool 1.0 ships under <license>. What it does, how it works, what it can't do yet, and where we want help.
---

I work on tidepool; this post uses it, and the "What it does not do yet" section covers where it falls short.

## The problem
<One paragraph from your own use. Specific, with a number.>

## What shipped in 1.0
<Install command. Screenshot or GIF of one real run.>

    <install command>
    <the one command that shows the value>

## How it works
<One design decision and its trade-off. Not a feature list.>

## What it does not do yet
<Three honest gaps. This section is what earns trust on dev.to.>

## Where we want contributors
<3-5 concrete, linked issues labelled `good first issue` or `help wanted`, each with an owner who will review within <N> days. Link CONTRIBUTING.md.>

## One question for you
<A real question, e.g. "Which of these three gaps would block you from using it?">

Repo: <one link, at the end>
````

Before you publish:

- Put one link at the end. The first-paragraph affiliation line is already there.
- Don't ask for unicorns or reactions, because all public reactions score the same **[code default]**.
- Run the draft through your humanizer skill.
- Use the same title only once, since a third same-title post in a day gets an automatic spam label.

### Companion #discuss post (Wednesday 2026-11-04)

```text
Title: What would make you trust a new CLI enough to put it in CI?
Body: Three things we weighed for tidepool (signed releases, a pinned
install script, a --dry-run default), what each cost us, and the
question: which one has actually changed your mind about a tool?
```

Don't link the repo in the body. Answer in comments with facts.

### Earn-first comment pattern (Fri–Mon)

```text
// ✓ Good: adds a fact the author can use, no link
Nice write-up. One thing that bit us with the same setup: <specific fact>.
Did you see that in <metric>?

// ✗ Bad: praise plus product link
Great post! We built tidepool to solve exactly this, check it out: {url}
```

### Reply to a tag-moderator removal

```text
Thanks for the note - you're right, this is a project announcement, not
an open-source practice post. I've kept #news. Is there a tag you'd
suggest for the contributor section?
```

## 6. Cadence

| When | Action | Owner | Hours |
| --- | --- | --- | --- |
| Fri 10-30 | Create the org, set the CTA, check the tag sidebars, and ask partners@dev.to about paid featured placement. | Maintainer | 1.5 |
| Fri–Mon | Leave 3–5 substantive, link-free comments in your language tag and #productivity. | Maintainer + 1 teammate | 1.5 |
| Mon 11-02 | Finish the draft, the cover image, and the contributor issues with owners. Stay in draft. | Maintainer | 2 |
| **Tue 11-03** | Publish at a time you can answer comments for 2 days. The hotness bonus lasts 96 hours, then halves at day 4 and drops to an eighth at day 7 **[code default]**. | Maintainer | 1 |
| Tue–Fri | Answer every comment within 24 hours. Heart good comments on your own post (an author's reaction counts five times **[code default]**). Teammates add substantive comments, never reactions on cue. | Maintainer + 1 teammate | 3 |
| Wed 11-04 | Publish the #discuss post. | Maintainer | 0.5 |
| Sun 11-08 | Day-4 read-out. Decide on the paid test. | Maintainer | 0.5 |
| Weeks 3–8 | One full tutorial or build log under the org every 1–2 weeks, plus a `series:` once you have 3 posts. | Maintainer | about 3 per week |

## 7. If the post is flagged, removed or buried

1. Stop re-posting, because a repeat makes it worse.
2. Check for a removed tag or a moderator comment, and fix the post against that tag's rule.
3. Appeal once at dev.to/appeal (signed in) or support@dev.to, describing the fix.

## 8. Metrics

Targets are self-set, because DEV publishes no vendor benchmark. Read them at day 4, not day 30.

- Reactions and comments on the post at day 4.
- Org and author followers, monthly. CTA clicks and referral sessions to the canonical or repo page.
- Contributor funnel: first-time contributors, PRs opened from the #contributorswanted section, and time to first review.
- Hygiene, pass threshold zero: removed tags, spam labels, moderator comments, AI-disclosure notes.

## Questions for you

1. Which of my assumptions are wrong? Especially the language, whether the accounts already exist, and the weekly hours.
2. Do you want me to draft the full post once you give me the real problem, numbers and gaps?