## Both moves you're describing are the exact two things this framework's evidence base was built to warn about. Here's the breakdown.

## Move 1 — pulling SSO and audit-log export into the paid tier

This isn't a "what to open source" decision. It's the *reversal* case — moving an already-open feature into a paid tier — which the skill's own evidence table (HashiCorp, Elastic, Redis, Red Hat, Docker, Chef) treats as the single most expensive move a company can make, independent of how small it looks from the inside.

**Why this one is worse than the average reversal, not better:**
- The code has been MIT for two years. There's no license to walk back — anyone can already legally fork the last open commit that has SSO and audit-log in it and keep shipping it. Unlike HashiCorp/Elastic (which had to *relicense* to make the old code inaccessible going forward), you have zero legal lever here. A community fork restoring these two features is a cherry-pick, not a re-implementation — the lowest possible bar a reversal has ever had in your own case table.
- "Enterprise buyers are the only ones who care" is the claim GitLab's persona test exists to stress-test, not accept at face value. SSO and audit-log export are also exactly the features a security-conscious solo self-hoster or a small team going through their first compliance review wants — not because they're buyers, but because they're operators. Check your own issue tracker/support history for who's actually asked for these before you commit to that framing publicly; if it turns out an individual contributor cohort cares, you've picked the one persona-test failure mode GitLab explicitly built its rule to avoid.
- Name the value-capture mechanism now, in writing, before you announce: what stops a fork from maintaining those two features indefinitely and staying current? If the honest answer is "nothing, we're hoping nobody bothers" — that's the gap. If it's "managed hosting, support SLA, the rest of the enterprise tier, the trademark" — write that down, it's your answer when someone asks what you still hold.

**Concrete mitigations:**
- Don't retroactively break already-running self-hosted deployments. Gate the removal at a future version boundary, not by disabling it under existing installs — the closest analogue to GitLab's "no artificial limits added to the open edition" promise, applied to a feature you're taking away instead of a cap you're adding.
- Announce before it lands, with the reasoning and the effective version — the cheapest of the five commitments in this framework's list, and the one you're currently skipping.
- Turn this into a durable, published line (buyer-tiered: "individual/single-org self-hosted stays open forever; identity-federation and compliance-reporting features for regulated buyers are enterprise") rather than a one-off feature pull. Feature-by-feature judgment is explicitly the least durable boundary shape — it invites the reading that more features get pulled next quarter, which is worse for trust than this one move alone.

## Move 2 — solventlabs/solvent → solventflow/solventflow

Docker/moby is not a loose analogy here, it's the same event: no license change, no code withdrawn, "purely cosmetic" — and it drew a PR sitting at 7 upvotes against 110 downvotes. The lesson the skill draws from that case is specific: **communities price governance surprise on its own, independent of what actually changed.** "Nothing legal changed" is not a defense against that, it's Docker's own belief going in.

What "purely cosmetic" undersells:
- Anything that referenced the old path breaks or needs redirecting: package registry provenance, CI badges, security-advisory records, SBOM/attestation chains if you publish any, docs links, existing forks' upstream remotes. GitHub redirects the repo itself, but downstream references don't fix themselves.
- This is a real engineering and comms lift wearing a "just a rename" label — which is worse than admitting it's a lift, because when people hit the breakage, the mismatch between "purely cosmetic" and "my CI broke" reads as either incompetence or spin.

**Mitigation:** pre-announce the rename on its own — why, when, what redirects you're keeping, and explicitly that nothing legal or code-level changes — rather than letting people discover it as a fait accompli the week it happens.

## The real risk is doing both in the same week

Each of these individually is a trust event this framework treats as expensive. Landing them simultaneously, under cover of a brand launch, is the shape of the worst-case reading available to you: *"they used the rebrand to bury the paywall."* That narrative doesn't require either move to be unreasonable on its own merits — it only requires the timing to look convenient, and right now it does.

If the brand-launch date is fixed, don't let that force the tier change into the same week by default:
- Decouple the announcements even if both ship in the same release. Two clearly separate posts, not one bundled changelog entry.
- If you can't decouple the dates, say explicitly and early that they're unrelated decisions with independent timelines — the earlier this is said, the less it looks like something you'd only mention if asked.

## Before you execute, name two things you haven't mentioned

1. **Who can approve pulling a feature back**, by role — and whether that person is also the one who'll answer for it publicly when a fork or a GitHub issue thread shows up. If this hasn't been decided explicitly, decide it before the announcement, not after the backlash.
2. **A commitment for what happens next.** Right now this reads as the first of possibly several take-backs. One sentence closing that door — e.g., "this is the last feature we move out of community edition without a stated notice window, and here's the line going forward" — is what converts this from "they're narrowing the free tier" into "they drew a line, once, and published it." That's the GitLab move, not the HashiCorp one, and it's available to you for the cost of a paragraph.

If you want help drafting the actual rollout communications for either change, that's `oss-launch`'s job, not this skill's — happy to bring that in once the line itself is settled.