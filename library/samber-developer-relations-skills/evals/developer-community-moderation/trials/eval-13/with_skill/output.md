## Framing

This isn't a gate case. The skill's severity gate is for harassment, threats, sustained targeting of one person — no ratio, no menu, straight to the top rung. What you're describing — "this is not how anyone writes Go," "did you read anything before opening this," aimed at whoever's PR is up that week — is explicitly a **menu case**: a hostile technical argument, recurring, no apparent malice. That's not a lesser problem. It's a different problem, with a different toolset.

Two things to name before the menu, because they change what "ranked" means here:

- **Casper is exactly the person the rule is written for.** The organizing principle behind this whole skill is: a policy that doesn't bind your most powerful contributor is worse than no policy. 40% of the codebase and almost every review makes him that person. Whatever you pick, ask afterward: would you have gone this easy on a newcomer who talked to *him* this way? If not, that gap is the real finding, not Casper's tone.
- **"Nobody's been harmed exactly" is the trap, not the reassurance.** Two first-timers didn't complain — they left. Silent attrition after a bad review is the same signal a complaint is, just one you don't get a second look at. Don't let the absence of a report read as absence of a problem.

One open question I can't answer for you, and it changes the bottom of the menu: **is Casper one of your three maintainers, or a top contributor without maintainer authority?** If he's one of three, any decision that needs the maintainer body to act has him recused down to two people deciding — thin, but workable. If he's outside the three, you have a clean decision body over him already. Settle this before you need the bottom rungs.

## Ranked menu

Ranked by recurrence prevented per hour of maintainer time and goodwill spent — not by what feels proportionate in the moment:

1. **Mentoring** (the co-maintainer's offer). Normally this loses on ratio — slowest, most relationship investment, least reliable. It jumps to the top here because all three conditions the skill sets for promoting it are true at once: Casper is load-bearing, the pattern reads as a skills gap ("he's like that in every technical thread, including with us" — not targeted, not malicious) rather than a values gap, and someone has already volunteered the hours. That's a rare alignment. Use it.
2. **Systemic fix** — a short, written review-tone expectation (CONTRIBUTING.md or the PR template): something like "critique the code, not the person; assume the contributor is new." Costs an hour, applies to all reviewers equally (this is what satisfies the "applies to your most powerful person too" test without singling Casper out by name), and it's the piece that survives even if the mentoring conversation doesn't land.
3. **Content correction going forward** — a maintainer softens or hides a comment that crosses the line, in the moment, on future PRs. Doesn't fix the pattern, but stops a specific newcomer's first experience from being the bad one.
4. **Public statement** — a line in CONTRIBUTING.md or a pinned note on what review tone the project holds itself to. Cheap, doesn't name anyone, tells the next newcomer the standard is real.
5. **Role removal** (pulling review/merge authority) — last resort, held in reserve, not exercised now. Two reasons: the read is skills-gap not values-gap, which is precisely the case mentoring is for, not sanction; and with only three maintainers this is close to an extinction-level decision for the project's velocity. It needs to exist as a *named* next step, not be taken off the table — see "what I'd pick" below.

## What I would not do

- **Don't extract an apology.** A compelled "sorry" to the newcomers tells you nothing — you lose the one signal worth having, which is whether Casper would apologize unprompted once he actually sees the effect.
- **Don't let the mentoring conversation stand in for a decision.** "Sit with him and talk about how he writes reviews" is good — as an add-on to an actual expected-behavior agreement, not instead of one. A friendly chat with no stated consequence is the same failure mode as a conciliatory notice: kind-sounding, nothing decided.
- **Don't treat "he's like that with us too" as exculpatory.** It explains the behavior (not targeted, probably not conscious), it doesn't excuse the outcome. Judge the impact on newcomers, not his intent toward them.
- **Don't leave this entirely verbal.** If it doesn't work and you need rung 5 later, you'll want a record that this was raised, when, and what was agreed — not three people's differing memories of a hallway conversation.

## What I'd pick

Run 1 and 2 together, not 1 alone:

- Let the co-maintainer have the conversation. But have it produce something concrete: not "be nicer," but a specific, observable standard Casper agrees to — critique the code, skip the "did you even read X" framing, assume unfamiliarity over incompetence. Write it down between the two of them even if nobody else ever sees it.
- In the same week, ship the CONTRIBUTING.md paragraph. It's the one piece of this that doesn't depend on Casper changing, and it's the answer to "would this apply to anyone else" — now it visibly does.
- Agree now, among the two maintainers who aren't Casper, what happens if a newcomer has the same experience again after this — a maintainer stepping in on that PR in real time, a second harder conversation, and at what point rung 5 is actually on the table. Decide this while nobody's upset, not while triaging the next case. That's the single most common way small teams fail at this: not underreacting, but taking too long to decide anything at all.
- Start tracking one number: whether a newcomer's first PR gets a second one. You already know the answer for two people. You don't yet for the rest — and that's the metric that will tell you if the fix worked, since nobody's going to file a complaint either way.

This is scoped smaller than a full code of conduct on purpose — three maintainers, no entity, one recurring pattern, doesn't need the whole apparatus yet. But you're now the team without one that just improvised an enforcement decision, which is exactly the moment most projects retrofit a rule after the fact and turn the next incident into a governance fight. If you want, the next thing worth twenty minutes is not a full CODE_OF_CONDUCT.md — just a one-line reporting channel (who a newcomer tells if a review crosses the line, that isn't Casper) and this ladder written down. Say the word and I'll draft both.