# Driftwave: 12-week Medium distribution plan (revised)

## ⚠️ What to change before you start

Four assumptions in the plan won't hold. Fixing them is week 0 work.

1. **"Backlinks in days" won't happen.**
   - Medium links are generally nofollow, so they pass little or no ranking credit. Check this by inspecting the HTML of your first published post.
   - Medium's authority doesn't transfer to driftwave.io. A summary on Medium ranks, if at all, as a Medium page.
   - A new account's pages take weeks to index and rank. Page-1 rankings for observability terms, against Datadog, Grafana, New Relic and Honeycomb, take months and need real links.
2. **Summaries can compete with your own posts.**
   - Use Medium's "Import a story" tool, or set the canonical URL in story settings, so Google credits driftwave.io as the source.
   - Without that, a 300-word summary can outrank the full post for its own title.
3. **Unreviewed AI summaries are a risk, not a free lunch.**
   - Medium requires disclosure of AI-generated content and limits its distribution. Check the current policy before launch.
   - The cost is intern time plus an editor's review, not zero.
   - Thin, repetitive summaries with the same closing line, three times a week, look like spam to readers and to Medium's curation.
4. **Check your inventory.**
   - Three posts a week for 12 weeks is 36 summaries. If driftwave.io has fewer than 36 posts, you will run out, or you will summarize weak ones.

## What Medium can realistically do for you

- **Reach:** a small referral trickle, plus occasional distribution inside Medium's observability and DevOps topics.
- **Brand surface:** a channel your audience may already read.
- **Not:** a ranking shortcut or a backlink engine.

## Cadence

Run **2 posts per week** for the first 4 weeks, not 3. Your best 8 posts get a proper edit. Expand to 3 per week only if the pilot passes its gate.

## 12-week plan

| Week | Focus | Actions | Output |
|---|---|---|---|
| 0 (before wk 1) | Setup and baseline | Write down current organic clicks, top queries and signups from Google Search Console and your analytics. Rank the blog posts by traffic, by relevance to buyers and by evergreen value. Read Medium's AI, promotion and import policies. Build the UTM scheme: `utm_source=medium&utm_medium=syndication&utm_campaign=<post-slug>`. | Baseline sheet, post ranking, policy notes |
| 1 | Account | Create the "Driftwave" publication or profile. Add logo, bio, driftwave.io link, and a named human author. Do a test import of one post and confirm the canonical tag points to driftwave.io. | Account live, canonical verified |
| 2 | Pilot start | Publish 2 posts from your top-ranked list. Write them as standalone pieces, not teasers: a different intro, one key insight or code snippet, and then the link. Disclose AI assistance. Add the closing line and a signup link with UTMs. | 2 posts |
| 3 | Pilot | Publish 2 more. Compare views, reads and clicks to driftwave.io against the first 2. Check indexing in Search Console. | 4 posts total |
| 4 | Pilot | Publish 2 more. Add Medium to the engineering team's sharing routine, such as LinkedIn and X posts from named people. Review the intern's edit time per post. | 6 posts total |
| 5 | Gate review | Apply the go/no-go test below. Write a one-page readout. | Decision |
| 6–8 | Run the winner | If go, run 2–3 posts per week from the posts that performed. If marginal, stay at 2 per week and retarget topics. If no-go, stop and move the budget to the alternatives below. | 6–9 posts |
| 9 | Test a second channel | Syndicate the same top posts to dev.to or Hashnode with canonical tags, and to a LinkedIn newsletter. Compare cost per click and per signup against Medium. | Channel comparison |
| 10–11 | Optimize | Double down on the best-performing topics and formats. Drop the weakest 25%. Try one original Medium-native piece, such as a real incident postmortem. | 4–6 posts |
| 12 | Review | Report outcomes against the baseline. Decide whether to continue, resize or stop in Q2. | Q1 readout and Q2 recommendation |

## Go/no-go gate (week 5)

Set the numbers on the baseline sheet before you publish. Suggested starting thresholds, to be adjusted to your traffic:

- **Go:** Medium sends at least a few dozen qualified clicks per week to driftwave.io, and at least one signup traces to it by UTM.
- **Marginal:** clicks are present, but signups are zero. Fix the landing page and the call to action before scaling.
- **No-go:** under about 10 clicks per week after 8 posts, or intern edit time exceeds the value of the traffic.

## Quality rules for every post

- A human editor reads every summary before it goes out. The editor checks facts, product claims and tone.
- No two posts share the same intro structure.
- Each post stands alone and teaches one thing. The closing line stays: "Read the full post on driftwave.io" plus the signup link.
- Disclose AI assistance if Medium's policy requires it.
- Never publish customer names or unreleased product details.

## Measurement

- **Medium:** views, reads, read ratio, followers.
- **driftwave.io:** UTM sessions from Medium, signups from those sessions, and assisted signups.
- **SEO:** Search Console impressions and clicks for the canonical posts, plus whether Medium copies outrank them.
- **Cost:** intern hours plus editor hours per post.

## What moves rankings, if SEO is the real goal

Medium won't. These do:

- **Rewrite and refresh** the 10 blog posts that already rank on pages 2 and 3. Add internal links, examples and a clearer title.
- **Original data.** Publish a benchmark or "state of observability" report that journalists and newsletters link to.
- **Digital PR and guest posts** on sites that give followed links, such as DevOps newsletters and conference blogs.
- **Integration and comparison pages** for your highest-intent searches, such as "Driftwave vs <competitor>" and "<tool> monitoring".
- **Technical SEO audit** of driftwave.io (indexing, speed, structure).

Expect meaningful ranking movement in 3 to 6 months, not days.

## Risks

- ⚠️ Medium duplicates outranking driftwave.io if canonicals are missing.
- ⚠️ Low-effort AI posts hurting brand perception with engineers.
- ⚠️ Intern effort spent on a channel with little return. The week 5 gate caps this.
- ℹ️ Medium rules change, so recheck the policies at week 0 and again at week 6.

## Decisions I need from you

1. How many blog posts does driftwave.io have, and which rank today?
2. Who is the named human author for the account?
3. Is the primary goal signups, brand reach or SEO? The plan weights them differently.
4. Do you want me to draft the baseline sheet and a template for the first 8 posts?