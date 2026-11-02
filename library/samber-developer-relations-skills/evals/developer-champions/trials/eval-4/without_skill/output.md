**Verdict: the hard gate is defensible with a caveat; the 30-point follower weighting doesn't hold up, and the full public leaderboard creates more risk than transparency.**

## 1. Hard requirement — conference talk, no exceptions

Mostly fine as a floor, but "recognized conference" needs a definition before it's a rule, not after the first dispute. Two problems:

- **It's a privilege filter, not an expertise filter.** Speaking access correlates with travel budget, employer sponsorship, visa status, and confidence in public speaking — not with data expertise. You'll systematically exclude strong candidates who demonstrate expertise through OSS maintenance, published research, or high-signal technical writing instead.
- **"No exceptions" bites you on your best candidate.** The first time a brilliant applicant with a maintained data-tools repo and zero conference talks applies, you'll want to waive it — and then the rule wasn't actually hard, it just wasn't written honestly.

Fix: keep the gate, but define "recognized" now (a short allow-list or clear criteria) and widen the *proof*, not the bar — talk OR peer-reviewed publication OR maintainer of a widely-used data OSS project. Same signal (public, vetted technical credibility), fewer false negatives.

## 2. 30/100 points on X follower count — doesn't hold up

This is the real problem, for four separate reasons:

- **It's not a competence signal.** Follower count measures reach or luck (early account, one viral post, purchased/bot followers), not data expertise. Weighting it at 30% means three-tenths of "Data Expert" is actually "Popular on X."
- **It's trivially gamed, and you're publishing the incentive to game it.** A public, weighted leaderboard tells every applicant exactly how many followers close the gap. Expect follow-for-follow schemes and bought followers before the deadline — and you have no way to detect that from a raw count.
- **It contradicts your stated goal.** "Getting our name in front of more people" is a *distribution* goal for the program, not a *merit* criterion for the applicant. Baking it into the expert score means your most-published leaderboard entry could be your least expert one — and it will be visible, forever, next to the word "transparent."
- **X-specific reach is a shrinking, biased proxy.** Substantial dev/data audiences have moved to Bluesky, Mastodon, and LinkedIn since 2023. Weighting X followers specifically also skews toward English-language, US/EU-based accounts and penalizes experts big on GitHub or regional platforms instead.

If reach matters to you at all, cap it low (~10 points, not 30) and score it as *engagement quality* (do people cite/share their technical content) rather than raw follower count — which is roughly what mature advocate-scoring rubrics use: usage/expertise signals dominate, social presence is a minor modifier, not a third of the score.

## 3. Full public leaderboard — weakens rather than proves "no favouritism"

Publishing weights and process is good transparency. Publishing every applicant's exact numeric score, ranked against each other, is a different thing with different costs:

- It permanently and publicly ranks rejected applicants by name — a strong deterrent for exactly the senior, already-credible people you most want applying.
- A rigid formula doesn't prevent accusations of favoritism if the formula itself is biased (see #2) — it just relocates the argument from "who did you pick" to "why does your rubric reward followers," which is a harder argument to win.
- These are third parties' personal data (name + score + social metrics) published without their control over the comparison — worth a beat of thought given you're EU-based, even outside strict GDPR-triggering territory.

Fix: publish the rubric and weights, publish the selected cohort, publish an anonymized score distribution if you want proof against cherry-picking. Don't publish a named ranking of everyone who didn't make it.

## Net

Keep a hard, well-defined credibility gate. Score expertise signals (OSS work, technical writing, community answers, the conference talk itself) as the bulk of the 100 points. Cut follower count to a small modifier or drop it. Publish the method and the winners, not a named leaderboard of everyone who applied.