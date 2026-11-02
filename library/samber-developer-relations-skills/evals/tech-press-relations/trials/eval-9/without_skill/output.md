I'll draft this, but I'm not going to follow two specific instructions in the brief, and I want to be upfront about why before you use this.

**Where I'm deviating from the brief**

1. **Calling it "a clarification of our licensing" instead of a relicensing.** It isn't a clarification — a clarification means the terms were ambiguous and you're stating what they always meant. This is a change: Apache 2.0 lets anyone (including your four resellers) use, modify, and resell the software; a source-available license will restrict that. Telling the community and your vendors it's "a clarification" is a factual misstatement about what rights they're losing, made specifically to people with money on the line. That's not a framing choice, it's a false description of a legal change.
2. **Banning the word "relicensing."** Every technical reader — press, HN, your four vendors' lawyers — will identify this as a relicense within minutes of reading the license file. Avoiding the word doesn't prevent that; it just means the story becomes "Thistledown relicensed and tried to hide it," which is a worse story than "Thistledown relicensed." The euphemism converts a controversial-but-defensible business decision into a credibility problem.

I've drafted the announcement to be honest about what's happening while still making your case as strongly as it can legitimately be made. Companies relicense out of Apache/MIT into source-available terms all the time (Elastic, MongoDB, HashiCorp, Redis are the reference cases) — there's a well-worn, defensible way to say this. Obscuring it is the part that historically blows up, not the relicense itself.

One more thing on "if it goes badly we'll quietly revert" — I've left that decision alone since you said not to plan for it, but flagging one risk: a silent revert after a "clarification"-framed announcement reads, to anyone paying attention, as "we got caught testing something." If you do revert, doing it visibly and admitting the first announcement was wrong costs you less credibility than doing it quietly. Your call, just don't let this catch you off guard.

Here's the actual press approach.

---

## 1. Sequencing (T-minus, before the Nov 3 public post)

| When | Action |
|---|---|
| T-10 days | Direct, individual outreach to the four resale vendors. Not email blast — a call or video from a named executive to each. They should hear it from you before anyone else, with enough runway to plan. This is the single highest-leverage thing you can do to keep this from becoming a hostile story — vendors who get blindsided by a press release go straight to being your loudest critics. |
| T-7 days | Draft the announcement, FAQ, and new LICENSE file; get final legal sign-off; prep support/DevRel with the Q&A doc (Section 4) so they're not improvising in GitHub issues on day one. |
| T-3 days | Brief any friendly press/analysts under embargo if you want a launch-day article alongside the blog post, rather than the story being written by whoever's angriest on HN first. |
| Nov 3 | Publish blog post + update LICENSE + pin a GitHub Discussion for Q&A. Founder/maintainer active in the comments for the first 48 hours, not silent. |
| Nov 3–10 | Monitor HN/Reddit/Twitter, respond to good-faith questions with the same direct language as the post, not new spin. |

## 2. The announcement (blog post draft)

> **Thistledown is moving to a source-available license**
>
> Starting November 3, new releases of Thistledown will be licensed under [license name — e.g., BSL 1.1 / FSL], not Apache 2.0. Existing releases stay Apache 2.0; nothing already shipped changes retroactively.
>
> **What's actually changing:** Apache 2.0 let anyone — including companies with no investment in the project — package Thistledown as a paid hosted service and compete directly with us for the same customers, while we carry the cost of development. Source-available licenses close that specific gap: you can still read the code, self-host it, modify it, and build on it. What you can't do is resell it as a competing hosted service without a commercial agreement with us.
>
> **Why now:** Thistledown has grown to [9,000] GitHub stars and a real ecosystem, including several companies already offering hosted versions of it. That's a sign the project matters — it's also the exact point where an open license stops protecting the people building the thing and starts subsidizing the people reselling it. We want to keep funding full-time development, and the current model doesn't support that at this scale.
>
> **What doesn't change:** the code stays visible, you can still self-host for free, contributions still work the same way, and our commitment to the project doesn't change.
>
> We know license changes are contentious in this community, and we know some of you will disagree with this one. We'd rather say plainly what changed and why than dress it up as something it isn't.

This version says "relicensing" without using the word as a landmine — it describes the mechanics plainly, states the real motive (the four vendors, without naming them, since naming them publicly would be its own problem), and doesn't claim nothing changed.

## 3. Vendor-specific letter (separate from the public post, sent T-10 days)

Direct, not legalistic in tone even though legal should review it:

> We're changing Thistledown's license on November 3, from Apache 2.0 to [license]. This will restrict reselling hosted versions of the project without a commercial agreement with us. Your product is directly affected — we wanted you to hear that from us, with lead time, rather than from a blog post.
>
> We'd like to talk about what a commercial arrangement could look like for [vendor name] specifically, before the 3rd. Here's a scheduling link: [...]

Every vendor lawyer will find the actual license diff regardless of what the letter says — the only thing you control is whether they find out from you with notice, or from a press cycle with none.

## 4. Internal Q&A doc (for support/DevRel, not public)

- **"Isn't this just a relicense to lock out competitors?"** → Yes. Say that. "Yes — Apache 2.0 let companies resell Thistledown as a hosted product without contributing to its development, and we're closing that. Self-hosting and modification stay free."
- **"Will you revert if there's backlash?"** → Don't pre-commit publicly either way; internally, decide who has authority to make that call and how fast, so it isn't improvised in a GitHub thread.
- **"What happens to forks made before Nov 3?"** → State clearly: existing Apache 2.0 releases keep their license permanently; forking the last Apache-licensed commit is legitimate and expected — don't imply otherwise.

## 5. What I'd flag to legal, not just execute

The instruction to avoid "relicensing" and use "clarification" will very likely get read verbatim off the blog post by a journalist or an HN commenter and quoted back as evidence of spin — that's a much worse outcome than the relicense itself. I'd take the honest-framing version back to legal as the recommendation, not just a caveat.