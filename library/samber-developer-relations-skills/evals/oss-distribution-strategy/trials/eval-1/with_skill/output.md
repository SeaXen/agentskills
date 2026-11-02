Assumptions I made because I don't have live access to your registry page, repo, or download analytics (WebFetch/WebSearch aren't available in this session) — correct these and I'll adjust:

- **Ecosystem**: npm only, no CLI/binary. If slipstream ships a companion CLI, downstream packaging re-enters the mix.
- **Adopter**: individual developers self-selecting a library for scripts/pipelines. If you know of company-owned repos depending on it, this shifts toward "both," and trust signals (§ Foundation ring) become worth adding.
- **Goal**: compounding growth (no funding/procurement deadline mentioned).
- **Team**: solo, 5h/month, no co-maintainer to hand off relationship-heavy channels.
- **March Show HN** = March 2026, so the plateau has held for ~6 months.

---

# Distribution plan — slipstream

## Position today

**Known:**
- Show HN, March 2026: ~900 GitHub stars, downloads peaked ~11k/week, settled at 3,400/week (~31% of peak), flat for ~6 months.
- One acquisition event (the launch), no compounding channel built since — that's the mechanism behind the plateau, not bad luck. Stars measure the spike travelling, not distribution (Borges & Valente 2018: stars correlate with promotion reach as much as merit). A single-source spike decaying to a stable core, then going flat, is what happens when nothing new feeds the top of the funnel after launch.

**Unknown — run this before touching any new channel** (30–60 min, do this first):
- npm page: is the description written in problem vocabulary ("streaming CSV parser/transform for Node.js", not just the brand name), are all keyword slots filled with terms an evaluator would search ("csv", "stream", "etl", "transform", "parser"), are docs/repo/funding links present, does the README render cleanly on npmjs.com?
- Days since last release, and the longest gap in the last year.
- Any existing listings from the Show HN wave (blog mirrors, aggregator cross-posts) that are now stale or point at an old URL.
- Dependents count (npm "Dependents" tab, or deps.dev) — an order of magnitude, not a precise number.
- Name collision check: "slipstream" is a common project name across ecosystems (WebRTC libs, game servers, etc.). Confirm npm/GitHub search for "slipstream csv" actually surfaces you first — if not, that's a findability problem no amount of new channels fixes.

Expect the same finding this skill expects by default: a half-filled registry page, not a missing channel. Fix what the audit finds before adding anything below.

## Adopter

Individual developers, npm-search/GitHub/word-of-mouth path (assumption above). Optimize registry findability and a zero-friction install, not procurement legibility — trust signals (signing, SBOM, Scorecard) don't enter this plan; nothing here suggests a company-adoption goal.

## Foundation ring (this month, ~2h, then minutes per release)

- Rewrite the npm description and fill every keyword slot in the problem's vocabulary, not slipstream's own naming.
- Add missing links (docs, repo, funding) to the npm page.
- Fix or remove any stale Show HN-era listing found in the audit.
- Add a one-line "maintained, current release cadence" statement to the README — the cheap fix against a flat download graph reading as abandonment, whether or not it's true.
- Check GitHub repo topics and social-preview image match current positioning.

## Sequence

**Stage 1 — weeks 1–2 (to 2026-10-08).** Foundation ring above.

**Stage 2 — months 1–3 (to 2026-12-15), passive discovery.** The two moves below, not fifteen:
- Find the 1–2 curated, real lists your target developer actually browses (search "awesome csv", "awesome streaming", "awesome nodejs", ETL/data-engineering tool lists on GitHub), read each one's `contributing.md`, and submit in-format after one unrelated fix to each first.
- Identify the highest-fan-in Node.js ETL/data-pipeline project or stream-processing framework in your niche and pitch a first-class adapter or a documented example inside its docs — this is where a stranger discovers slipstream while solving an unrelated problem, which is a fundamentally different arrival than a listing someone has to already be looking for.

**Stage 3 — ongoing, capacity-permitting.** One newsletter pitch (Node Weekly or JavaScript Weekly — both cover exactly this ecosystem) timed to your next real release, not a routine post. That's the highest-leverage version of what "Dev.to cross-post" was reaching for, at the same cost, with an editor who already has the audience.

## Test ring (ends 2026-12-15, ~2h/month)

- **T1 — curated lists.** 2 lists selected per the criteria above. Signal: referral arrivals >20–30/month per listing by end date (self-set — calibrate against your own current arrival numbers once the audit gives you a baseline, not this number). Cost: ~1h to submit each + a 15-min quarterly sweep.
- **T2 — one integration target.** Pitch or build one adapter/example for the highest-fan-in host project. Signal: adapter installs, or one dependent that's a repo you don't recognize as your own launch-week crowd. Cost: 2–4h upfront, near-zero to hold once merged.

## Core channel (decided 2026-12-15)

Whichever of T1/T2 produces real arrivals. Bet on T2 winning long-run: integration position is the one family here that keeps generating discovery with zero recurring cost once earned — the structural fix for a plateau, versus a list entry that only pays while people are actively browsing that list.

## Refused

- **15–20 directory submissions.** This is the named failure mode, not a judgment call: "twenty submissions in a weekend, all stale a year later." A quarterly sweep of 20 listings alone would burn most of a month's 5-hour budget, forever. Two maintained listings outperform twenty stale ones. Reopens only if a contributor volunteers to own the sweep.
- **Ongoing subreddit presence.** Not a compounding channel — it's recurring relationship-and-moderation work, and at 5h/month that competes directly with everything above. A single post timed to a real milestone (next release, a 1.0) is fine as a one-off; a maintained presence is not. Reopens if capacity grows or someone else owns it.
- **Standalone Dev.to cross-posting.** Same cost as the newsletter pitch above, worse leverage — no editor, no existing audience, competes with T1/T2 for the same hours. Reopens around a real milestone as a "why we built this" piece, not a routine cross-post.
- **Downstream packaging (Homebrew/apt/etc.).** slipstream is a library installed via npm inside someone else's project, not a standalone binary — zero benefit, and packaging is the one irreversible commitment in this catalog. Reopens only if a CLI ships.
- **Another Show HN / Product Hunt relaunch now.** Novelty is spent 6 months out; a repost reads as noise. Reopens at a genuine 1.0 or rewrite.

## Release rhythm

Audit the actual cadence first (unknown above). State a maximum interval publicly (e.g., "a fix lands within 6–8 weeks") — never a minimum. Batch small changes into readable releases; ship security fixes out of band. Every release is a broadcast to existing dependents whether or not you add a single new channel — a silent repo reads as abandoned even when it isn't, which directly undercuts everything else in this plan.

## Review

Listing and metadata sweep quarterly, first pass 2027-01-05. Test-ring decision 2026-12-15, with authority to kill T1, T2, or both and pick a different core channel.

## Threshold check

- Registry metadata 100% filled — **pending**, run the audit above first.
- Total recurring cost ≤60% of 5h capacity (≤3h/month) — Stage 2/3 as scoped above lands around 2–2.5h/month. ✓ by design, verify once T1/T2 are running.
- Every channel has owner (you), cost, signal, review date — set above. ✓
- No harmful-decay channel without a scheduled sweep — curated lists get the quarterly sweep; directories-at-scale and subreddit presence, the two harmful-decay traps at this budget, are refused rather than adopted. ✓
- Stale listings fixed before new ones added — **pending audit**, do this in Stage 1 before submitting anywhere new.

---

Two things worth checking on your end before you start: whether slipstream competes for search attention with an unrelated same-named project on npm/GitHub, and whether any of your 3,400 weekly downloads are coming from a company-owned repo you didn't know was depending on you — either finding would change the adopter-type assumption this whole plan rests on.