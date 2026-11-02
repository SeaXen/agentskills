## Framing the win — and what to verify before you hit send

The engineering result is real and worth featuring. The framing of *what it proves* is where this needs a pass — "4 → 261 attributed signups" reads as "we grew signups 65x," but what you almost certainly shipped is an **identify() gap closure**: users were already converting across domains, and the stitching now lets you *see* where they came from instead of dumping them into "direct/unknown." Those are two different claims, and only one of them is proven by the number you have. Conflate them and the update overclaims — worse, it's the kind of overclaim a sharp reader (or a future you, three months from now when growth doesn't show up in total signups) will catch.

### The one number that decides the whole framing

**Pull total signups (attributed + unattributed) for both weeks, before writing another word of the update.**

- **Total flat, mix shifted** → this is a *measurement accuracy* story: "we can now see the true source of signups that were already happening." Frame it as visibility, not growth. Still a great win — just a different one.
- **Total also jumped** → now you have two things happening at once (better attribution *and* more signups) and need to explain the second one separately — it's not caused by an identity-stitching fix, so something else drove it that week.

This single check is the difference between an honest update and a metric that gets walked back next month.

### Checklist before you send

**1. Reconcile against the system of record.**
A green analytics debugger and a tag manager showing everything firing only proves client-side events fired — it says nothing about whether the *count* is right. Pull actual signups for this week from the product DB or CRM and confirm it matches (or reasonably relates to) the 261. "Everything fired" and "the number is correct" are independent facts.

**2. Check for a backfill/catch-up spike, not a new run rate.**
Cross-domain stitching often retroactively resolves identity for sessions that started *before* the fix shipped. If any of the 261 are backlog getting cleared in one batch, this week is a one-time bump, not a new baseline — you don't know that yet. Hold the "this is our new normal" language until you see next week's number too.

**3. Rule out double-counting from the identity merge itself.**
Merging anonymous IDs into known people at conversion is exactly the kind of operation that can fire twice — once on the original event, again on merge replay — or split one person's activity across profiles that later re-merge. Check that 261 is unique *people*, not events, and spot-check a handful for duplicate merges.

**4. Confirm the anonymity guard didn't leak identity, corrupting the merge.**
If the passthrough between domains ever carries a real email/UUID instead of the anonymous ID (even briefly, even in one code path), profiles can fold into the wrong person — which can inflate or misattribute counts in ways that look like a clean win. Worth one explicit check on the merge logic, not just the dashboard.

**5. Exclude self-referrals and auth redirects from "cross-domain."**
If referrer classification isn't excluding OAuth/login/checkout hosts and your own subdomains, some of the 261 could be the *same* user bouncing through your own login flow, not a genuine second domain in their journey. This would make the stitch look more powerful than it is.

**6. Sample-audit 5–10 of the 261 by hand.**
Trace the actual session: first touch on domain A → identify() → signup on domain B. This is the only check that confirms *correctness*, not just presence of a number. Everything else above is a plausibility check; this is the real proof.

**7. Sanity-check that "4" was a fair baseline, not an artifact of the bug.**
If 4 is what the identify() gap made possible — i.e., almost everything was misattributed before — that actually *strengthens* the "measurement fix" framing and weakens any "this is 65x growth" framing. Say so; it's a more credible story than implying last week was a normal week.

### Suggested copy for the update (once the above checks out)

> **Cross-domain identity stitching shipped Monday.** Previously, users who moved between [domain A] and [domain B] before signing up lost their source — they landed in "direct/unknown" no matter where they actually came from. Now that journey is stitched end-to-end.
>
> Result: attributed signups went from 4 to 261 this week. **Total signups [were flat / grew X%]** — this is a visibility win, not (yet) a conversion-volume win: we can now see where our signups actually come from, which [unblocks channel-level budget calls / lets us stop guessing on paid vs. organic / etc — pick the real downstream unlock]. We'll watch next week's number to confirm this is the new baseline rather than a one-time backlog clear.

If total signups *did* also jump, add a second, separate paragraph for that — don't let the stitching fix take credit for it without its own explanation.

The honest version is still a good update: closing an identify() gap is real, valuable work, and "we finally know where our signups come from" is a legitimate headline on its own. It just shouldn't borrow growth's headline.