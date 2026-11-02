## Windlass DX Benchmark — Q4 Setup

Scope note upfront: I don't have verified, sourced data on these seven vendors' current SDKs, docs, or support quality — and I don't have live web access enabled in this session to go get it. What follows is the benchmark instrument itself (framework, scoring rubric, scorecard, methodology, timeline, owners) so your team can execute it in Q4 and produce numbers you can defend to the VP, rather than me guessing at scores for products I can't verify. If you want me to run the actual research pass once web access is enabled, say so and I'll fill the scorecard in.

### 1. Vendor tiering (based on what you already know)

| Vendor | Last raise | Tier | Treatment this quarter |
|---|---|---|---|
| Beacontree | $240M | A — full benchmark | Highest-funded, highest competitive priority |
| Larkspur | $180M | A — full benchmark | Full benchmark |
| Ashgrove | $95M | A — full benchmark | Full benchmark |
| Tidepool | $60M | A — full benchmark | Full benchmark |
| Greypine | $40M | B — discovery-only | No public docs/repo found → score it, don't skip it (see §4) |
| Sablefin | $22M | B — discovery-only | Same treatment as Greypine |
| Marlowe | $15M | C — monitor only | Acquired March, no shipping since → exclude from hands-on testing, track as a market-narrative signal |

Don't just drop Greypine, Sablefin, and Marlowe from the deck. "No discoverable docs" and "dead since acquisition" are DX data points in their own right — a VP slide that says "3 of the 7 best-funded players in the category have no self-serve DX story at all" is a stronger argument for Windlass's positioning than silently benchmarking 4.

### 2. Benchmark dimensions and weights

Built on the five DX stages (Discovery → Learning → Using → Debugging → Upgrading), adapted for feature-flag SDKs and weighted toward what a 900-MAU self-serve backend-tools vendor can actually win on. Score each 0–4 per vendor; weight reflects what should move the Q4 roadmap, not what's easiest to measure.

| Dimension | Stage | Weight | What "4" looks like |
|---|---|---|---|
| Time to first flag eval | Learning | 3 | Signed up, SDK installed, first flag evaluated in under 5 minutes, no sales call |
| Self-serve vs. sales-gated | Discovery | 3 | Free tier or trial usable with zero human contact |
| Backend SDK coverage & idiom | Using | 3 | Native Go/Java/Python/Node SDKs, idiomatic per language (not a thin REST wrapper) |
| Local evaluation latency | Using | 3 | In-process rule evaluation, no network call on the hot path |
| OpenFeature compliance | Using | 2 | Certified provider, not just "compatible" marketing copy |
| Testing/mocking support | Using | 2 | First-class local override / mock provider for unit tests |
| Error messages & failure modes | Debugging | 2 | Specific exception types, actionable messages, documented fallback behavior on SDK init failure or network loss |
| Docs quality | Learning | 2 | Runnable quickstart per language, not just a single curl example |
| Changelog/release cadence | Upgrading | 1 | Regular, dated releases with real changelogs (not silent patches) |
| Pricing transparency | Discovery | 2 | Self-serve pricing page with seat/MAU math, no "contact sales" wall |
| Support responsiveness | Debugging | 1 | Time-to-first-response on a real support ticket, mystery-shopped |
| GitHub/community health | Discovery | 1 | Issue response time, PR cadence, if an OSS component exists |

Max score: 25 per vendor. This weighting is a starting point — walk it past whoever owns the actual Q4 roadmap call before you lock it, since "what should move the roadmap" is a product call, not a research call.

### 3. Scorecard template

Fill this per vendor; use it as the literal working doc.

```
Vendor: _______________        Funding: _______
Evaluator: _____________        Date tested: ___

Discovery
  [ ] Self-serve signup, no sales gate            Score: _/4
  [ ] Pricing page is public and legible          Score: _/4
  [ ] GitHub org / community activity visible     Score: _/4

Learning
  [ ] Time to first flag eval: ___ min            Score: _/4
  [ ] Docs: runnable quickstart, our top 2 langs  Score: _/4

Using
  [ ] Backend SDK coverage: which langs, how idiomatic
  [ ] Local eval vs. network call on hot path
  [ ] OpenFeature: certified / claimed / absent
  [ ] Testing/mocking: how would our team unit-test a flag check?
  Score: _/4 each sub-item

Debugging
  [ ] Error message sample (paste one real error)
  [ ] Support ticket response time: ___ hrs
  Score: _/4 each

Upgrading
  [ ] Changelog cadence, last 2 quarters
  Score: _/4

Total: __/25
One paragraph: where would our 900 MAU dev actually get stuck that a Beacontree/Larkspur dev wouldn't, or vice versa?
```

### 4. Handling Greypine and Sablefin specifically

"No public docs or repos I can find" is worth 20 minutes of verification before it goes in the deck as a finding, because there are three different stories hiding behind that sentence and they lead to different conclusions:

1. **Docs exist but are gated behind a sales demo or logged-in dashboard.** Check Wayback Machine for a `/docs` subdomain, check npm/PyPI/Maven/pkg.go.dev for a published SDK package under the company name (a package can exist with no public doc site). A gated trial is itself a DX finding — "enterprise-only motion" — not an absence of a product.
2. **The product is real but genuinely has no self-serve trial or SDK at all** (pure enterprise sales-led). That's a legitimate DX score of near-zero on Discovery and Learning, and worth stating plainly.
3. **The funding number is stale or the company pivoted.** Recheck the raise date and what it says on their homepage today before citing $40M/$22M as current in front of the VP.

Whichever it is, put one sentence per vendor in the deck naming which of the three it is — "no docs found" alone reads as incomplete research, not a finding.

### 5. Marlowe

Acquired in March, nothing shipped since — don't spend hands-on testing time here this quarter. Do keep one line in the competitive section of the Q4 plan: an acquisition with no post-acquisition roadmap is a churn opportunity for their existing customers, and worth a note to whoever owns competitive displacement outreach, separate from the DX benchmark itself.

### 6. Methodology (source-quality order)

1. **Primary, hands-on**: your own signup, SDK install, and a real support ticket. This is the only source that produces the Discovery/Learning/Using/Debugging scores above — don't substitute a marketing page read for actually running the SDK.
2. **Primary, published**: their own docs, changelog, GitHub repo, OpenFeature conformance results if published.
3. **Secondary**: G2/Capterra reviews filtered to developer reviewers, not buyer/admin reviewers — for corroborating the "does the SDK actually work as documented" question, not for scoring.
4. **Tertiary**: Reddit/HN threads, blog posts. Useful for spotting known pain points to specifically go test yourself, not as a citable score input.

Test each Tier A vendor in the same two languages every time (recommend Go and TypeScript or Node, matching your own SDK's primary backend audience) so scores are comparable across vendors rather than each evaluator picking whatever language they know.

### 7. Q4 timeline and owners

| Week | Work | Owner |
|---|---|---|
| 1 | Verify Greypine/Sablefin status (§4); confirm Marlowe's post-acquisition state; lock the weighting table (§2) with roadmap owner | You |
| 1–2 | Signup + first-flag-eval timing, all 4 Tier A vendors, parallelized 1 evaluator per vendor | DX team, 4 people in parallel |
| 3 | Docs read + SDK idiom review, 2 languages each | Same 4, staggered so no one context-switches vendors mid-week |
| 3–4 | Mystery-shop support (submit a real question, time the response) | 1 person, sequential — don't burn 4 support tickets same day, looks like a bot sweep |
| 4 | GitHub/community health pull, changelog cadence pull | 1 person, can run in parallel with support shopping |
| 5 | Score consolidation, scorecard fill-in, write the one-paragraph "where would our dev get stuck" per vendor | You + evaluators |
| 6 | Synthesis: comparison matrix + one-pager per Tier A vendor + exec summary slide for the VP | You |

### 8. What the exec summary slide should argue

The honest framing for a 900-MAU vendor benchmarking $15M–$240M-funded competitors isn't "we're bigger" — it's "DX is the lever we can win on regardless of funding gap." Structure the final slide around: (a) where the big-funded vendors' size works against them (sales-gated trials, slower support, enterprise-first docs), (b) where Windlass already wins on the weighted scorecard, (c) the 1–2 gaps worth a Q4 roadmap slot, prioritized by weight × how many prospects have actually cited them as a blocker.

If you want a sales-facing battlecard version of this later (for competitive-displacement conversations, not roadmap planning), that's a different deliverable — flag it and I'll set that one up separately so the two don't get conflated.