## What's off (and why it reads crisp anyway)

This sentence is almost a word-for-word match for the deliberately broken example in this GTM skill's own reference library (`developer-first-gtm/references/gtm-plan-example.md`), which uses the identical phrasing ("runs a PLG motion with an enterprise sales layer for larger accounts... pursue cloud marketplace and partner channels opportunistically") as the canonical *this reads well in a board deck and cannot be executed* case. Its own annotation:

> Three motions declared as one, no rejection stated, so every one of them gets re-proposed next quarter. "Opportunistically" is how a motion with no owner is written down.

That's exactly what's nagging you. It isn't a wording problem, it's that the sentence answers "what are we open to" instead of "what did we decide." Three things are wrong structurally, not stylistically:

1. **Three motions, presented as one.** PLG (bottom-up self-serve), an enterprise sales layer (developer-influenced sales, sometimes called product-led sales), and ecosystem-mediated (marketplace/partner) are three distinct motions in this framework. The rule for combining motions is one primary and *at most* one secondary — never three. The sentence doesn't pick.
2. **The PLG + enterprise-sales pairing is actually fine** — it's the textbook combination ("self-serve creates the base, assisted sales monetizes the accounts that outgrow it"). But the memo never names which one is primary, what the qualification rule is that hands an account from one to the other, or who owns that handoff. Without that, "enterprise sales layer" is just a label, not a motion.
3. **"Opportunistically" is the tell.** It's the word a team writes when marketplace/partner has no owner, no trigger, and no stated decision — is it deferred, is it staffed, is it a real Q4 priority? Nobody knows, so it will get re-proposed as new scope the moment someone asks "why aren't we on AWS Marketplace yet," regardless of what this memo says.

A board member who reads this sentence has no way to tell if you have one plan or three half-plans. That's the thing you're sensing and your head of revenue is reading as "concise" — it's concise *because* it's compressing an undecided question into six words.

## The fix isn't tighter prose, it's a decision

Before rewriting, Fernwake needs to answer one question the current sentence is dodging: **is marketplace/partner a resourced motion this year, or is it not happening yet?** The rewrite is different depending on the answer — pick whichever is true and use that block. Don't ship a version that still says "opportunistically" with better grammar; that ships the same ambiguity in a crisper font.

**If marketplace/partner has no owner and no budget this year (the likely reading of "opportunistically"):**

> Fernwake's primary motion is bottom-up self-serve: developers adopt free, and accounts that cross [usage/team threshold] hand off to developer-influenced sales — [owner/role] closes and expands from there. Cloud marketplace and partner listings are deliberately deferred: no partner-enablement capacity this year. We'll revisit if [specific trigger, e.g. "a marketplace listing becomes the procurement path buyers ask for"].

**If marketplace/partner is real and staffed, but "enterprise sales layer" is actually the *secondary* motion you're deprioritizing:**

> Fernwake's primary motion is bottom-up self-serve. [Owner] runs ecosystem-mediated distribution as the secondary, sourcing accounts through [named marketplace/partner]. Developer-influenced sales is not a standing motion yet — we handle enterprise inbound case-by-case until [trigger, e.g. "qualified-account volume clears the cost of a dedicated hire"].

Both versions are shorter than the original and say strictly more, because each one commits to exactly one primary and one secondary, and turns "opportunistically" into either a named owner or a stated rejection with a revisit trigger. Whichever motion doesn't make the cut still belongs in the memo — just under "Rejected motions" or "Revisit triggers," with the reason attached, not folded into the Motion sentence where it reads as a live commitment.

Send me which of the two is actually true for Fernwake (or tell me the real owner/trigger if it's a third variant) and I'll drop the specific numbers in before Friday.