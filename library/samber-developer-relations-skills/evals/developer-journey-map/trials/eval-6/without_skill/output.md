## Reality check before the fix list

Your instinct — "developers aren't motivated enough" — doesn't hold up against the numbers you gave me. Two structural problems make the 3% look worse than it is, and neither is about motivation.

**The comparison is apples-to-oranges.** Onboarding, Integration, and Production are all bounded-window conversions ("within 30 days," "within 14 days"). Advocacy is an unbounded "ever" metric with no time box and no defined action ("mention" — a tweet? a GitHub star? a conference talk? a Slack shoutout?). You can't rank a lifetime cumulative rate against three 30-day sprint rates on the same chart and call it "worst by miles." It's not instrumented the same way, so it isn't comparable.

**"Ever" metrics get worse as you succeed, not better.** An account that reached production yesterday hasn't had time to ever mention you. If Production is growing quarter over quarter (which it should be, if fixes #2 and #3 below work), the denominator of "ever mentioned us" keeps refilling with fresh accounts that haven't had a chance yet — mechanically dragging the ratio down even while real advocacy is flat or rising. This is cohort-maturity bias, not developer apathy.

**Even a "true" 3% may be close to normal.** Public, unprompted technical advocacy is a rare behavior everywhere — most B2B infra products live in this range. You don't have a benchmark to compare against yet (worth getting one before declaring a crisis).

None of this means ignore Advocacy. It means: fix the instrument before you fix the behavior, and don't assume the lever is "make people want to talk about us more."

## Top 3 fixes for next quarter

**1. Redefine and re-instrument the Advocacy metric.**
Replace "ever mentioned us" with a rolling window (e.g., % of production accounts that produce any public/community signal in a trailing 90 days) and a tiered definition instead of one vague bucket:

| Tier | Example signal |
|---|---|
| Low-effort | GitHub star, upvote, retweet |
| Medium | Blog comment, community answer, review site entry |
| High | Blog post, conference talk, case study participation |

Without this you can't tell whether any advocacy work you do this quarter actually moved anything — you'd be optimizing against noise. Cheap, fast, does itself in a quarter.

**2. Fix Onboarding's 47% first-success rate.**
This is the single largest absolute leak in the entire table — 53% of quickstart starters never get a first success, more than double the drop at any other stage. It already has an owner (docs team). Every account that dies here also dies as a future Integration account, Production account, and advocate — fixing this multiplies every downstream number, including the one you actually care about. Improving Advocacy while Onboarding leaks over half your funnel is optimizing the wrong end of the pipe (classic bottleneck error: the constraint isn't where you're staring).

**3. Build minimum-viable advocacy enablement — not an incentive program.**
Detailed below. This is the piece that answers your original ask, reframed to what will actually work for this audience.

*Worth flagging, not spending a slot on:* Awareness has no owner and no instrumentation. You're running the whole funnel blind on the input side — you don't know channel mix or volume, so you can't ever attribute an advocacy lift to a specific acquisition source. Fine to leave unowned for one more quarter, not two.

## The Advocacy stage: enablement and recognition, not incentives

Your instinct to want a program here is right. The lever is wrong. A cash-for-mentions or bounty structure specifically backfires with backend engineers, for three converging reasons:

- **Quillbore is infrastructure, not something end users ever see.** A GraphQL gateway has no natural exposure loop — nobody outside the engineering org encounters it, so there's no product-embedded virality to amplify. The ceiling on organic public sharing is structurally lower than for a consumer-facing tool, no incentive changes that.
- **Paid/incentivized technical content reads as inauthentic to other developers** — the audience you want to influence is the most skeptical one for this exact tactic. It also creates a disclosure obligation you don't want to manage at scale.
- **Behavior = Motivation × Ability × Prompt — all three have to be present.** Your production accounts likely have moderate motivation already (they shipped something that works). What's missing is Ability (do they have something shareable, and know where) and Prompt (is there ever a moment that cues sharing). Fixing motivation alone, with the other two still at zero, changes nothing.

Build for Ability and Prompt instead:

**Prompt — attach the ask to a real moment, not a broadcast.**
The natural trigger is the account's own "aha": the day they cross 14-day sustained production traffic. That's a graduation moment, not a random newsletter blast. Trigger a request there — for a review, a case study conversation, or a referral — while the win is fresh (peak-end effect: people remember and act on the peak, not the average).

**Ability — remove the "what would I even say" barrier.**
- Pre-written, editable LinkedIn/X post templates and a one-page architecture diagram they can drop into their own internal docs or talks.
- A "Powered by Quillbore" badge for internal architecture pages and READMEs — visible to the audience that actually matters here (other backend engineers at scale-ups), even though it's invisible to end users.
- A lightweight case-study process: you write the first draft from an interview, they approve — most developers won't write 800 words unprompted, but will greenlight a good draft about their own work.

**Recognition, not cash — the currency developers actually value.**
- Public credit: named case study, spotlight post, co-presented conference slot. This builds *their* reputation, which is worth more to a senior backend engineer than a gift card.
- Direct access: a private channel to your engineering team, early access to roadmap items, input on the API surface. Insider status is a stronger motivator than money for this audience segment.
- Skip: bounty payments, tiered swag ladders, referral commissions. All three read as feeling transactional or MLM-like to this crowd, and can actively suppress the authenticity that makes advocacy valuable in the first place.

**Channel strategy — bias toward team-to-team, not public broadcast.**
Given the low natural virality of infra tooling, a colleague-to-colleague referral (double-sided credits: they get credits, referred teammate gets credits) will outperform "please post about us" for pure volume. Treat public mentions as a bonus outcome of a good referral program, not the primary mechanism.

**Start small.** Seed this from 8–10 production accounts who already show organic signals — answered a community question, filed a sharp bug report, referred a colleague informally. Invite-only beats broadcasting an offer to your whole production base; it keeps the group genuinely engaged instead of attracting people chasing the perk.

## What this buys you next quarter

- A trustworthy Advocacy number to actually manage against, instead of a metric that's structurally guaranteed to look bad.
- A materially larger Production base feeding the top of the Advocacy funnel (via the Onboarding fix), which compounds every quarter after.
- An Advocacy program built on prompts and assets developers will actually use, instead of an incentive structure this specific audience tends to distrust.