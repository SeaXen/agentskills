# Quillmark Hack rules page: draft copy

**Decision 1: API centrality.** Make it a pass/fail gate, not a scoring criterion. A criterion can be gamed with one clean call in the last hour. A gate with an early checkpoint and a removal test can't be.

**Decision 2: weights.** Publish the criteria, their rank order, and what a top score looks like. Keep the percentages private, and publish the full scorecards after the event. Keep every binary rule exact, because nobody can optimize a rule to the decimal.

Paste-ready copy follows. Brackets are values for you to set.

---

## Quillmark track: how it works

### The Quillmark requirement

To compete for any Quillmark track prize, your project must be built around the Quillmark API. Calling it is not enough: the project has to stop working at its core without it.

A project qualifies only if all three conditions hold:

1. **Core feature dependency.** The main thing your project does for its user depends on the Quillmark API. If you remove the API, that feature must break, not degrade gracefully into a mock.
2. **Early integration.** You hold a working integration at the midpoint check-in (see below).
3. **Survives the removal test.** Judges may revoke your API key during judging. With the key revoked, your core demo must visibly fail.

Projects that don't meet these conditions are still welcome. They compete for the general prizes but not for any Quillmark track prize.

### Midpoint check-in ([hour 24] of [48])

By the check-in deadline, every Quillmark-track team submits:

- A link to a commit that makes a real, working call to the API.
- One paragraph, "What breaks without Quillmark," naming the feature that depends on it.

We cross-check this against the usage logs for your team's API key. A team with no logged usage before the check-in is moved out of the Quillmark track. You can keep building and compete for general prizes.

Your plan may change after the check-in, but the core dependency may not move off the API.

### Final submission

Add an **API role statement** to your submission (150 words maximum):

- Which Quillmark capabilities you use.
- What the user would lose if each one were removed.
- What you built on top of them.

We compare this statement with your check-in paragraph, your commit history, and your key's usage logs. A project whose usage jumps from near zero to a handful of calls in the final [3] hours gets extra scrutiny from judges. That is a review flag, not an automatic disqualification, because late integration is sometimes legitimate.

### What judges look for in the track

Judges rate depth of integration, not number of calls. A high score looks like this:

- The API is the reason the product can exist.
- The project uses several parts of the API together, or uses one part in a way that suits it well.
- The team handles the API's limits and failures sensibly.

A low score looks like this:

- A single call whose result is displayed or logged but doesn't drive anything.
- The API could be swapped for a hardcoded value without the user noticing.

Call counts and endpoint counts are not scored.

---

## How projects are judged

Every project is scored on five criteria. They are listed from most important to least:

1. **[Criterion A: e.g., Usefulness / real problem solved].** Does it solve something a real person would care about?
2. **[Criterion B: e.g., Technical execution].** Does it work, and is it well built for a [48]-hour effort?
3. **[Criterion C: e.g., Originality].** Is the idea or approach fresh?
4. **[Criterion D: e.g., Demo and communication].** Can we understand and trust what you built in [5] minutes?
5. **[Criterion E: e.g., Polish].** Is it finished and pleasant to use?

For the Quillmark track, depth of integration is scored as part of criterion B and is also protected by the pass/fail requirement above.

**We don't publish exact weights.** Judges score each criterion against written descriptions of what a strong and a weak project looks like, then form an overall judgment. We don't want teams tuning a project to a formula. We want them building the best thing they can.

**What we commit to:**

- The order above is real. Earlier criteria matter more than later ones.
- No criterion is zero. A project strong on one and broken on another will not win.
- After the event, we publish the weights we used and every finalist's scorecard, with judge comments, so you can see exactly how results were reached.
- Pass/fail rules (eligibility, the Quillmark requirement, the code freeze) are exact and appear in full on this page. If a rule can disqualify you, we state it precisely.

Judges' decisions on scoring are final. Ties are broken by [a re-vote among the judges on the tied projects].

---

## Notes for you (not for the page)

- **Checkpoint timing.** Pick the check-in hour so a team can reasonably have an integration by then. [Hour 24 of 48] is a guess. Too early punishes teams that need to explore. Too late lets teams bolt the API on before the deadline.
- **Key logs.** The anti-bolt-on mechanism depends on Quillmark giving you per-team keys with usage logs. Confirm that with your sponsor before you publish. If they can't, drop the log language and rely on the check-in commit, the removal test, and commit history.
- **Scope of the gate.** Last edition's second-place team: did it place second overall or in the sponsor track? The draft applies the gate to track prizes only. If the problem was that a bolted-on project took a main-ranking podium spot, also add "or any overall placement claiming Quillmark integration as a strength."
- **If the Discord pushback continues.** The post-event publication of weights and scorecards is your answer. It gives the transparency they want without giving them a target to optimize beforehand. If you want to concede something, add a coarse tier ("criteria A and B together carry more than half the score") rather than exact percentages.
- **Tell sponsor judges the rubric.** The "depth, not call count" language only works if the Quillmark judges score the same way. Brief them before judging.

I can also draft the check-in submission form or the judge rubric anchors for each criterion if you want them.