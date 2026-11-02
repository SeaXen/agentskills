# Wrenfield: feedback page and all-hands slide

I read `developer-feedback-loop` in full, plus its references and the sibling `public-roadmap-strategy` skill it points to. I did not build your plan as written. Four parts of it conflict with the skill, so below is a version that makes the same case without those problems.

## What conflicts with your plan

| Your plan | What the skill says | Consequence |
|---|---|---|
| Mark the top five "coming soon" | Only product sets `planned`. DevRel never publishes dates or "coming" (Steps 2 and 6, "Promise leak"). "Coming soon" reads as a date to every buyer and sales rep. | You'd be committing your head of product publicly. For an API gateway, sales will quote it in deals. |
| Public roadmap next week | A roadmap starts only after two review cycles have produced statuses. Before that it's "a list of hopes". | Nothing has been decided yet, so no roadmap item can honestly be marked `planned`. |
| "480 upvotes" as the argument | Votes are a separate signal. Count distinct requesters, segment mix and severity. A spike from one outside link counts as one event. | Product will ask who the 480 are. If they're mostly free users, or came from one HN or Reddit link, the slide fails. |
| "The community wants X" to force the issue | Failure mode "feedback as ammunition". It also skips the one thing product turned down, which was a standing review. | Product reads it as an ambush and discounts your records afterward. |

The skill also says what to do when product declines a standing review. Don't build the pipeline. Run the leak trace, send it as a one-page finding to the product lead's manager, and offer the smallest version: one review per quarter on the top five records. The plan below follows that.

## 1. The public page: a feedback tracker, not a roadmap

Launch it next week, but use only statuses that promise nothing: `received`, `under review`, `duplicate`. Leave `planned`, `not planned` and `shipped` out of the page until product has set them.

**Page title:** What you've asked for, and where it stands

**Intro (copy):**
> This page tracks the problems you've told us about most. It is not a roadmap. A status here says what stage a request is at, never when, or whether, we'll build it. Product reviews these requests every [cycle] and decides. We post each decision here.

**Table layout** (one row per problem; top five to start):

| Problem (in your words) | Area | Distinct requesters | Status | Next review |
|---|---|---|---|---|
| [Problem title, not the feature name] | [API / dashboard / CLI / docs] | [N people, N orgs] | received | [date or "not scheduled"] |
| ... | | | | |

Write the problem in the developer's words, e.g. "Fetching X takes N round trips", not "Add feature X". The requested fix goes in the record, in its own field.

**Status definitions** (shown under the table):

| Status | Means |
|---|---|
| received | We captured it and linked it to a record. Nothing more. |
| under review | On the agenda of a product review. You get a decision, not a delivery date. |
| duplicate | Merged into another record. Follow that one. |
| planned / not planned / shipped | Set by product after a review. Not used until then. |

**"How we decide" box (policy page, linked from every row):**
- **Where to post:** [the tracker or Discussions link]. Chat is for conversation. Requests posted there get linked here.
- **What happens next:** we merge duplicates, and product reviews requests every [cycle]. Every reviewed request gets a status.
- **What decides priority:** [only factors product confirms, e.g. problem severity, number of developers and teams affected, fit with direction]. Votes are one input, not a ballot.
- **What we can't take here:** bugs go to [issue path], security reports to [private path], support questions to [support path].
- **What we won't do:** give dates before we're sure, or leave a request open once we've decided against it.

**Page rules:**
- Rows are read-only. Debate happens in one linked discussion thread.
- No dates, no "soon", no "on our radar".
- No account names or revenue figures.
- Name a maintainer and a "last reviewed" date on the page.
- Get your head of product's explicit OK on the page text before it goes live. They aren't reviewing; they are approving that nothing on it speaks for product.

## 2. The all-hands slide

Ask for a decision, not a mandate. Show who is asking, not how many.

**Slide title:** Five problems developers keep hitting. We have no decision on any of them.

**Slide body:**

| # | Problem | Distinct requesters | Orgs | Segment mix | Worst case |
|---|---|---|---|---|---|
| 1 | [problem, developer's words] | [N] | [N] | [free N / paid N / ent N] | [blocker N] |
| 2–5 | ... | | | | |

Beside the table, in one line: *"[N] upvotes on #1 — [N] of them from [N] distinct people. [Note any link-driven spike.]"*

**The ask, bottom of slide:**
> One 60-minute product review per quarter. Five records, each leaves with a status. We send the evidence ahead. We tell the developers who asked.

**Speaker notes (about 90 seconds):**
1. "These are the five problems developers raise most. Each row is a problem, not a feature we're asking for."
2. "The vote count on #1 is [480], from [N] distinct people. I'm showing both because votes alone don't tell us who needs it."
3. "I'm not asking to build any of them. Product decides that. I'm asking for a decision on each one, even if the answer is no."
4. "Developers who asked in public are waiting. A clear no with a reason does less damage than silence."
5. "Smallest version: one review a quarter, five records, one hour. We do the prep."

**Backup slide (if challenged):** a record in the template, with its private fields (accounts, revenue) hidden, to show you've separated evidence from opinion.

**Do not show:**
- Account names or revenue.
- A "coming soon" label or any date.
- A claim that the page "forces" anything.

## 3. Before Thursday: the one-page finding

This is the skill's prescribed step when product declines a standing review. Send it to your head of product's manager, or at least to your head of product, before the all-hands, so the slide isn't a surprise.

**Leak trace** (take 20–30 of the most recent requests from the last 60–90 days, at least three per channel, not the memorable ones):

| Stage | Count | Ratio | Lost here |
|---|---|---|---|
| Asked | [N] | 100% | |
| Captured durably | [N] | [%] | [N] |
| Reached product | [N] | [%] | [N] |
| Got a decision | [N] | [%] | [N] |
| Requester told | [N] | [%] | [N] |

Pitch it as: one hour per quarter, already deduplicated, plus discovery contacts product would otherwise have to recruit. The cost of not deciding is that every unanswered request is a public thread where the company looks like it isn't listening.

## 4. What I'd want answered first

1. **Who are the 480?** Distinct people, how many orgs, free vs paid vs enterprise, and did a spike come from one external link? Without this, I'd cut the vote count from the slide.
2. **Is feature X part of the top five, or just the one you care about most?** If it's the second, say so on the slide. Hiding that is how this reads as ammunition.
3. **Does the MSA carry a "purchases not contingent on future functionality" clause, and do self-serve terms?** If not, the roadmap version of this page should wait for legal.
4. **Will your head of product approve the page text?** If they refuse even that, I'd keep the page private and use the leak trace alone.
5. **Can you give me the trace data?** I haven't seen any Wrenfield data. Every bracketed number above is yours to fill in; I haven't made up figures for it.

If you answer 1 and 2, I'll fill the table and the speaker notes with your real numbers.