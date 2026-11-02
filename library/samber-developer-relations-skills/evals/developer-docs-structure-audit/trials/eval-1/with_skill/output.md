## Verdict

⚠️ Your own data says a full IA rebuild is the wrong spend. Don't hand leadership a new tree yet — hand them this reframe first, then a scoped fix.

The skill's validation reference has one load-bearing row, sourced from published tree-test interpretation heuristics:

| Reading | Diagnosis | Action |
|---|---|---|
| **>80% success and >60% direct-path across core tasks** | Structure is not the bottleneck | **Cancel the restructure; spend the budget on gap-filling and freshness instead** |

Your numbers: 84% success, 67% direct-path. You clear both bars. A Treejack study exists precisely to answer "is the tree the problem" — and for 5 of your 6 core tasks, the answer it gave you is no. Spending a quarter of writer time re-architecting a tree that already tests well is the exact waste the skill calls out: "a restructure that a tree test says is unnecessary costs a quarter of writing time and breaks every inbound link for nothing."

One task breaks that read: **webhook retry policy at 52%** sits below the 60% line — "structure fails on that task → restructure that branch." That's real, but it's a branch-level finding, not a site-level one. Diátaxis's own remediation loop rules out exactly what leadership is picturing: "Never propose a teardown. 'Rewrite the docs site' is not a recommendation, it is an abdication."

So the deliverable isn't a new tree. It's: **one scoped restructure of the webhooks section, plus the rest of the quarter redirected to gap-filling, freshness, and governance** — validated against evidence you already half-have, and re-tested with the tool you already have.

## What to tell leadership, verbatim

> "The Treejack study already answered whether the tree is broken: 84%/67% against 80%/60% benchmarks says it isn't, for 5 of 6 tasks. Rebuilding a tree that tests well burns the budget and breaks every inbound link and bookmark for no measured gain. One task — webhook retry policy — genuinely fails (52%), and that's a scoped fix: days, not a quarter. I want to spend the rest of the budget where the data says readers are actually losing: content that's missing, wrong, or stale, most of which your tree test never touched because it only covered 6 tasks against 210 pages."

## Start here — the webhook retry policy failure

This is the one confirmed structural finding, so it's the one thing to investigate before anything else:

1. Pull the per-task breakdown from the Treejack raw data, not just the headline number — first-click accuracy and direct-path rate *for this task specifically*. 90%-success-30%-direct-path means "fix the label, keep the tree"; 52% success outright means the category itself is wrong. Right now you only have the aggregate.
2. Find where the page currently lives and what section it's filed under. Read the participants' wrong first clicks — Treejack logs them — they tell you which wrong category readers expect it in.
3. Check whether the page mixes modes: retry policy is arguably reference (backoff schedule, max attempts, timeout values) wearing an explanation title ("How webhook delivery works") or buried inside a how-to ("Set up webhooks"). That's the single most common cause of a page a tree test can't find — it's classified as something the reader isn't looking for.
4. Cross-check with a real demand signal before committing: zero-result site searches for "retry," "backoff," "redelivery"; support tickets tagged webhooks; GitHub issues. A gap confirmed by two independent signals outranks one confirmed by none.
5. Fix per the mixing/placement finding you get from step 3 — most likely a **split** (a day: move the retry schedule into its own reference page, link it from wherever readers expect it) or a **rename** (an hour, but touches every child URL and deep link if this section is nested).
6. Re-test *that branch alone* with Treejack — you already have the design researcher and the tool; a 4-6 task, ~60-70 participant tree test on the new sub-tree confirms the fix before you call it done, per the same card-sort/tree-test method that produced your original numbers.

## Where the rest of the quarter goes — the actual audit

The skill's process, adapted to what you have and don't have yet:

**Answer these before anything gets classified** (the skill gates the whole pass on them):
- Repo or live Docusaurus site access, or neither? This decides whether you can run the inventory script or have to crawl the sitemap.
- Audience: self-serve individual developers, enterprise buyers evaluating a payments vendor, or both? A payments API almost always has both — and enterprise evaluators need explanation content (security model, compliance, limits) your tree test never asked about.
- Real product surfaces: which API areas, SDKs, webhooks, auth methods, payout flows, dispute/chargeback handling, self-hosting or on-prem options exist as things a user adopts one at a time.
- What demand signals can you reach — docs search analytics, support ticket tags, GitHub issues, community channels? This determines whether gap-filling work is evidence-backed or guesswork.
- Has a structure been imposed before, and did it decay? If yes, the problem is governance, not architecture, and the queue needs drift controls before more page surgery.
- Can you ship redirects? If URL stability is a hard constraint, moves and renames come off the table entirely.

**Then, in order:**

1. **Inventory** every page (not just the 6 tested tasks): `python3 scripts/docs-inventory.py ./docs --nav sidebars.ts --nav docusaurus.config.ts`. This gives you word counts, step/option-table signals, orphans against the nav, and last-modified dates — the raw material for triage across all 210 pages, most of which the Treejack study never touched.
2. **ROT-flag** every page — Redundant, Outdated, Trivial. This is where a quarter of budget actually moves the needle: an outdated page in a well-placed section still fails its reader, and your tree test can't see staleness at all.
3. **Classify** only what the evidence flags — pages above ~2,500 words, pages combining steps with option tables, everything on the adoption path, plus the webhooks branch from above. Don't classify all 210 pages by hand; that's exactly the "cheapest-first, comprehensive-looking" trap the skill warns against when the tree itself already passed validation.
4. **Build the coverage matrix** (surfaces × tutorial/how-to/reference/explanation) for the real surfaces from the interview. Confirm every empty cell against a demand signal before it becomes a "write this page" ticket — an unconfirmed gap is a question for the team, not committed writer time.
5. **Score twice**: CNCF TechDocs rubric (1-5, per section) as the number that travels to leadership and outside auditors; the structural scorecard (mode purity, orphans, dead nav entries, broken links, nav depth, staleness) as what actually drives the queue. Expect mostly 2s and 3s on a first honest pass — a first audit returning straight 4s means the rubric was graded too generously.
6. **Queue the work** ranked by reader need fixed per hour, not by finding count: splits and merges from ROT/mixing findings first, gap-fills only where a demand signal backs them, moves/renames last and only if redirects are viable.
7. **Ship governance alongside the fixes, not after them** — front-matter content-type validated in CI, a link checker (lychee) on a daily cron, CODEOWNERS per subtree, page templates so contributors stop inventing structure. Without this the webhook fix and every other one decays back within a year, same as whatever structure was imposed last time.
8. **Re-score quarterly** — 90-day-vs-prior-90-day analytics windows — so "is the tree still working" stays a measured question instead of reverting to leadership's gut sense next year.

## What not to do

- ❌ Don't design a new top-level tree for 210 pages on the strength of one weak task out of six.
- ❌ Don't create new empty sections to "make room" for gap-fill pages before they're written — Diátaxis calls this out by name: advertises the gap, forces readers to learn new vocabulary for nothing.
- ❌ Don't treat the quarter as a deadline for a rebuild; treat it as a budget for the ranked queue above, and report back what got deferred.