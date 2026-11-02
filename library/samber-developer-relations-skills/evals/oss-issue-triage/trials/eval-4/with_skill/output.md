## Short answer

Don't build it, and there's no threshold to give you — not because 500 dollars a report makes this touchy, but because there's no reliable ground truth to calibrate a threshold against. Build a volume-and-reputation gate on the bounty intake instead. Here's the full reasoning and the design.

## Why an AI-generation classifier doesn't work here

There is no reliable technical indicator for "this report was AI-generated." OpenSSF's working group on the problem records this plainly: detection currently rests on maintainer intuition, not a working detector. That's not a maturity gap you can close by picking a good model or a big enough training set — nobody has a validated signal to train against, so "what threshold" has no defensible answer. Any number you pick is a guess dressed up as a metric.

Two concrete failure modes if you ship it anyway:

- **It doesn't reduce inflow.** Generating a report costs the submitter pennies in tokens. If your classifier rejects one phrasing, they resubmit a slightly different one — free retries against an unvalidated filter is a fight you lose by construction.
- **It can silently eat your real findings.** You're already down to roughly a 1-in-15 valid rate. An auto-reject gate with no ground truth to check it against can misfire on exactly the report you exist to catch, and unlike a human dismissing a junk report, nobody will ever see that it happened. That's a worse failure than your current 90-minutes-of-annoyance problem — it's an invisible one.

If a reporter is ever told, even implicitly, "rejected as AI-generated" and they're a real person who used an LLM to help write up a real finding, that's a false accusation with no proof behind it — a conduct problem stacked on top of the triage problem, and now on your own paid bounty program.

## The arithmetic (why this isn't a labels or process problem)

Weekly capacity: 6 people × 4 hours = **24 person-hours/week**.

Cost per junk report, from your own numbers: 90 minutes × 2 reviewers = **3 person-hours per junk report**.

You didn't give me a raw weekly report count, but you don't need one to see the shape of it: at just **8 junk reports in a week, junk alone consumes your entire team's capacity** — before anyone looks at the one real finding statistically hiding in that batch. Given a live $500 bounty page and a valid rate that's already collapsed to 1-in-15 (6.7%), it would be surprising if you're meaningfully under that line already.

This is the same shape as curl's situation, not a coincidence — it's the same asymmetry RedMonk named for exactly this kind of program:

> "generating a plausible-sounding vulnerability report now costs pennies in tokens. Evaluating whether it's real still costs an hour of expert time."

No classifier changes that equation, because the classifier sits on your side of the cost line (expensive to build, expensive to validate, expensive to keep tuned) while the attacker's side stays at pennies regardless.

**No published response target survives this.** Don't try to hold one while this share persists — fix the intake economics first, then set a target against whatever capacity is left.

## What actually closes the gap: gate on volume and reputation, not content

This is curl's own precedent, and it's sourced, not a guess: curl's confirmed-vulnerability rate fell from above 15% to below 5%, and the fix that worked was removing the monetary reward entirely — not a better template, not a stricter form, not a faster rotation. It changed the economics of submitting, not the cost of evaluating. Reject those three options here for the same reason they didn't work there.

Options, in rough order of how reversible they are — pick from the top, since you can always tighten further if the first move isn't enough:

1. **Require a reputation or contribution-history threshold** before a submission is accepted — a linked identity with prior validated reports, or an account age/history check on your bounty platform.
2. **Cap open submissions per author** — one open, unresolved report per submitter at a time closes the "spray twenty variants and see what sticks" pattern outright.
3. **Restrict who can submit, or gate the channel** — require an invite or a vetting step before the public bounty form is reachable, rather than a fully open page.
4. **Raise the submission cost** — require a working reproduction against a specific tinderbox build, using tinderbox's own APIs, not a generic "a vulnerability may exist in header parsing" writeup. This is the one lever that also improves your real reports, since a real finder can produce a PoC in minutes and a template-generator usually can't.
5. **Change the incentive being farmed** — the $500 flat payout is very likely why you're being targeted at this volume specifically. You don't have to kill it like curl did; consider paying only on confirmed validity (if you don't already), or tiering it, or pausing it while you put 1–4 in place. This is the highest-value lever and also the one your leadership will feel, so flag it as a business decision, not just a triage tweak.

Gate on reputation and volume, never on "does this look machine-written" — there's no defensible signal for the latter, and accusing a contributor of it without proof is the conduct-incident risk above.

## Set the trigger now, in writing, since you're already past it

Decide this while nothing is on fire, not mid-crisis:

> **Trigger:** valid-report share below 10% over a rolling 4-week window, or junk volume at or above 8 reports/week (the point where junk alone saturates the team's 24 hours). **Action on trigger:** cap open submissions to one per author, require a reproducible PoC against a named tinderbox version, and move the $500 payout to confirmed-only.

Your current 6.7% valid share is already under that 10% line — this isn't a future policy, it's the one to put in place this week.

## What automation is actually fine to add

- Auto-fill the mechanical stuff: version/build field as a required dropdown, area label from the affected module, routing to the on-duty reviewer.
- If you want a lightweight "likely low-effort" signal to help two people *sort* the queue (review the sparse/generic ones last, or batch them), that's fine as a suggestion layer — sort order, never an autonomous reject. A human stays the one who dismisses a report, every time, which is also what protects you if a dismissed reporter ever pushes back.
- Don't build the classifier as a gate. If you build anything, build the intake constraints above — they're the ones with a documented track record of actually moving the valid-share number.