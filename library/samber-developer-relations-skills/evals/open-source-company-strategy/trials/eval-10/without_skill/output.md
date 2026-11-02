## The question before "what's the metric": what exactly are you giving away?

Before you build a metrics slide, close the gap your CEO will spot in five seconds: *"if this engine is why we beat Booking and Expedia, why are we publishing it?"* That objection is correct, and the pitch as stated ("credibility + free contributors") doesn't answer it. Fix the scope first, then the metric follows naturally.

**The actual moat in a recommendation engine is rarely the algorithm.** It's:
- proprietary training data (click/search/booking history at your scale)
- the feature pipeline (which signals you've learned matter — seasonality, price elasticity, inventory freshness, commission economics)
- the live feedback loop (A/B infrastructure, ability to iterate against real traffic)
- integration depth (how ranking ties into pricing, inventory, personalization)

None of that ships in a GitHub repo of ranking code. So you can very likely open source the *ranking framework/algorithm* — the part that gets you credibility — without exposing the part that actually drives your conversion edge. That's the pitch to make to your CEO: **not "we're open sourcing the recommendation engine," but "we're open sourcing the ranking framework, keeping the data, features, and business logic that make it Pelago's proprietary."** This is standard open-core structure, and it defuses the IP objection instead of hoping nobody asks.

⚠️ If instead the plan is to publish the actual production repo — trained weights, feature definitions, commission-aware ranking rules, live config — that's a different, much riskier bet, and worth a separate, explicit CEO sign-off on the IP exposure, not something to fold into a metrics conversation.

## Treat the pitch as two separate, unequally plausible claims

**Claim 1 — "Credibility in the developer world."** Plausible, real, but it's a recruiting/brand play, not an engineering one. Don't dress it up as a technical bet.

**Claim 2 — "Free contributors improving ranking quality."** Be honest with your CEO: this is the weak part of the pitch, for a structural reason, not a motivation reason. External contributors can't run your online A/B tests, don't have your feature data, and won't be trusted with PRs that touch live ranking logic. What outside contributors are actually good at is: generic algorithmic components, the evaluation harness, tooling, docs, bindings, bug fixes in the open parts. That's real value — just don't sell your CEO on "the community will make our ranking smarter." Sell "the community will harden the framework, and that hardening is free engineering time we didn't have to pay for."

Say both of these to him directly. It's a stronger pitch than the current one because it survives the obvious follow-up questions.

## The metrics — one per claim, both instrumented before launch

**For credibility (primary, and the one your CEO actually cares about):**
- ✅ **Engineering hiring funnel, sourced/tagged.** Add "found us via [repo]" to every interview debrief and ATS source field. Track: qualified inbound applications/month attributable to the repo, offer-accept rate for those candidates vs. baseline, time-to-fill and recruiter-cost delta for senior roles you're currently struggling to fill.
- Secondary: analyst/press/conference mentions of Pelago's *engineering* (not the consumer app) — count and quality of outlet.
- **Explicit non-metrics:** GitHub stars, forks, Twitter followers, one-time HN front page. These correlate with nothing you can take to the board. Track them for your own curiosity, never report them as success evidence — this is the same mistake companies make reporting "500K users" from summed npm downloads: it measures reach, not outcome.

**For contribution quality (secondary, pre-register the bar so you can't retrofit success later):**
- ✅ Primary metric: **% of external PRs that (a) get merged, (b) ship to production, and (c) move a pre-defined offline ranking metric** (e.g. NDCG@k or precision@k against a held-out booking dataset) **or an online conversion metric in an A/B test.** Not PR count, not contributor count — those are activity, not value.
- Set the threshold and horizon before launch, in writing: e.g. "if by month 12, at least one external contribution clears all three bars, the technical claim is validated." If zero do, that's a legitimate, useful result — it means the value was 100% on the credibility side, which is fine, but should be reported as what it is rather than quietly reframed as "lots of engagement."

**Risk metric to monitor, not to promise the board:** whether a competitor's conversion gap to you visibly narrows post-release. You can't attribute this cleanly, but flag it as a watch item for the exec team, reviewed quarterly, so "we gave away the moat" isn't discovered by surprise a year later.

## What to actually tell your CEO

*"We open source the ranking framework, not the data, features, or business rules that make it ours. Success on credibility is measured in hiring funnel, not stars. Success on contribution quality is measured in shipped, metric-moving external PRs, with a pre-set bar we check at 12 months — and if that number is zero, we'll know the value was recruiting, not R&D, and can defund the initiative accordingly."*

That version gives him a real yes/no test instead of a vibe, and it survives him asking the obvious "aren't we giving away the thing that makes us win" question.