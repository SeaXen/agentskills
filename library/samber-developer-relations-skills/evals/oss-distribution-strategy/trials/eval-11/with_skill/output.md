Here's the deliverable, grounded in `oss-distribution-strategy`'s code-host discovery surfaces family and its evidence base.

## 1. Why cloudferry is invisible on the devops Collection and the kubernetes/gitops topic pages

These are two different mechanisms — you've fixed the one that doesn't gate visibility and left the one that does untouched.

**The devops Collection page — this is the actual blocker.**
GitHub Collections (`github.com/collections/*`) are hand-curated, not auto-populated from tags. Getting listed requires a pull request to `github/explore` (a folder named for the slug, an `index.md`, and where applicable a 288×288px PNG under 75KB). The PR template explicitly requires the submitter to attest they are **neither the sole author of the entry nor an employee of the company behind it**. Adding topics to your repo has zero effect on Collection membership — nothing you did was going to work here. You need a third party — a user, contributor, or community advocate who isn't you or your employer — to open that PR on cloudferry's behalf. Find someone who already uses it and ask them to nominate it, or find whoever maintains the devops collection and pitch them directly; self-submission gets the PR closed on sight.

**The kubernetes/gitops topic pages — this should already be working.**
Unlike Collections, topic pages for established topics list every repo tagged with that topic automatically — there's no curation gate on membership, only on the topic's own descriptive page (which kubernetes and gitops already have). So if cloudferry genuinely doesn't show up at all, check the mechanical stuff first, in this order:
- Confirm the topics actually saved: Settings → repo topics, or `curl -s https://api.github.com/repos/<org>/cloudferry/topics -H "Accept: application/vnd.github+json"`.
- Confirm you used the canonical slugs exactly — `kubernetes` and `gitops`, no typos, no `k8s` substitute (GitHub doesn't alias them).
- Confirm the repo is public.
- Search directly rather than trusting the browse page: `github.com/search?q=topic%3Agitops&type=repositories` — if cloudferry shows up here but not on the pretty topics page, it's a caching/indexing lag, not a real absence.

Most likely outcome once you check: cloudferry *is* in the topic listing, just buried — these pages default-sort by relevance/stars, and `kubernetes` alone has tens of thousands of tagged repos. At 1,900 stars you're competing for page 1 against projects with 10-50k+. That's a ranking problem, not a listing problem, and there's no lever in this channel family to fix it beyond what already drives your star count elsewhere (dependency position, curated lists, creator seeding) — topics aren't a channel you can tune directly.

## 2. Star velocity to re-trigger Trending: there's no number to give you

I'm not going to hand you a figure, because none exists to hand you. This is the honest, evidence-based answer, not a hedge:

- **GitHub has never published the Trending algorithm.** Every "N stars in 24h" figure circulating online is folklore, reverse-engineered by third parties from incomplete data.
- **The data those estimates were built on no longer exists.** GitHub's public events firehose stopped emitting most star events. OSSInsight — the tool that used to model trending from that firehose — pulled its own trending feature rather than keep publishing numbers it could no longer trust. If the best-resourced third-party tracker gave up on this specifically because the ground truth disappeared, there is no reliable velocity target for you to aim at either.
- Treat any external "trending calculator" or blog-post number you find as noise, not a target.

What I'd do instead of chasing a number:

1. **Pull your own June data point** — it's the only ground truth you actually have. Look at the repo's traffic/referrer panel (short rolling window, so if you haven't already, export it now before it ages out) and reconstruct the actual daily star delta that day. That's a real, cloudferry-specific reference — worth more than any published folklore figure.
2. **Reframe the target.** Trending is a byproduct of a stars spike, not a channel you drive directly — treating it as one is exactly the trap this skill flags. What you actually want back is the clone spike, and stars are "the loudest and least informative number" for getting there on their own — track them paired with clones, not as the goal.
3. **Re-create the cause, not the symptom.** A concentrated stars spike like June's is typically produced by a real trigger (a release milestone, a newsletter/podcast pickup, a Show HN-style moment) landing inside a tight window, not by an organic accumulation. Tie your next push to an actual trigger — a named release (v-next, a notable integration, a case study) — and pitch it to 3-5 newsletter/podcast curators on a calendar with something concrete to try (a demo, a sandbox, a sample repo), timed to land in the same 24-48h window rather than trickling out. That's the lever that's actually in your hands; hitting a star count isn't.