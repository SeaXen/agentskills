## Is the 78.7% vs 74.6% claim right?

The numbers are real, but the conclusion drawn from them inverts what the paper itself found.

The source is Terrell et al., *"Gender differences and bias in open source: pull request acceptance of women versus men"* (PeerJ Computer Science 3:e111, 2017, DOI 10.7717/peerj-cs.111) — 3,064,667 pull requests analyzed, with gender inferred for 35.3% of users via name/Google+ linkage.

**78.7% vs 74.6% is the overall, aggregate acceptance rate** — insiders and outsiders mixed together. That's the wrong slice to answer "is there a bias problem in how we review outside contributions," because it's dominated by contributors who already have standing in a project (established track record, known identity, prior trust) — a population that says nothing about how a *stranger's* first pull request gets treated.

The same paper breaks that population apart, and the breakdown is the actual finding the authors built their conclusion on:

- **Restricted to outside contributors with an identifiable gender** — the exact population your good-first-issue queue and cold-review process serve — **women's merge rate drops to 58% against men's 61%.** Lower, not higher.
- **Contributors whose profiles were gender-neutral scored highest of all** (70% women, 65% men) — i.e., when identity isn't visible, judgment is closer to pure merit, and women's work does *better*, not worse.
- The authors' own conclusion: *"although women on GitHub may be more competent overall, bias against them exists nonetheless."*

So the pattern is: women's *work* is good (that's what pushes the aggregate number up), but when a reviewer can see the contributor is a woman *and* that contributor is an outsider without established standing, acceptance drops below men's. The pushback took the number that reflects the first fact and used it to deny the second, which is the opposite of what the paper's authors did with their own data.

**Caveat to hold onto, and to say out loud in the meeting**: gender was inferred, not self-reported, only 35.3% of users were linkable, and this is 2017 data on a platform that's changed since. Treat the *direction* (outside-contribution bias against identifiably-female contributors, mitigated when identity is invisible) as robust; don't defend the exact percentages as precise.

One more thing worth naming directly: even a correctly-read version of this study only measures the merge decision on PRs that were *already opened*. It says nothing about the steps before that — whether women find your project, find a way to start, or make it through setup — which is where most of the newcomer literature (Steinmacher et al.'s five-category barrier taxonomy: social interaction, prior knowledge, finding a way to start, documentation, technical hurdles) says attrition actually concentrates. "No bias at merge time" — even if true — wouldn't settle "no diversity problem," because most people never get far enough to have a PR judged at all. Quoting one outcome number as if it closes a broader question is exactly the failure mode this area warns against: measure your own funnel (external contributors per quarter, second-contribution rate, time to first response, external merge rate — tracked separately from maintainer PRs) rather than importing someone else's statistic as a verdict on Halyard.

## Does it change how you handle outside PRs?

Yes — but not because this study proves Halyard has a problem. It's because the fix is cheap, applies regardless of which way any given study cuts, and is good review hygiene on its own:

1. **Review against a written scope rule and a fixed order, never against an impression of the contributor**: scope first, then correctness and tests, then design (with reasoning attached), then only the style a formatter missed. This is the cheapest available control on reviewer bias precisely because it removes the reviewer's read of *who* submitted the patch from the decision path.
2. **Answer scope in the first comment.** Finding out a PR is out of scope after three rounds of review is the worst outcome for everyone, and it's also where discretion (and bias) has the most room to creep in silently.
3. **Label every comment blocking vs. optional**, so a review doesn't read as a wall of failures shaped by tone rather than substance.
4. **Acknowledge on a separate clock from reviewing** — silence, not slow review, is what actually drives people away, and it hits everyone before any gender effect would even be visible in your numbers.

Practically: if Halyard doesn't already have a written scope statement and a fixed review order that maintainers actually follow, build that now — it's the direct, evidence-backed response to "contributor diversity," and it doesn't require resolving the debate about the study to be worth doing. If you want to know whether Halyard specifically has a bias or drop-off problem, that's a separate, answerable question: pull your own last ten external PRs, note where each stalled and what the first reply said, and track your own external merge rate and time-to-first-response going forward — the paper someone quoted at the meeting describes GitHub in 2015–2017 in aggregate, not your repo.