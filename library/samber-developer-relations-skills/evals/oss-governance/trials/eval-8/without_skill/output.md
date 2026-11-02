**Verdict: the contributor is more right, but "meaningless" overstates it. The document isn't empty — it's misleading about where power actually sits, and it's silent on the one scenario a 2-maintainer project can't avoid: you and Jonas disagreeing.**

Walk it through three concrete cases and the gaps show up precisely.

**Case 1 — a proposal splits the community.** The text promises discussion "until consensus is reached," then immediately says maintainers "make the best decision." Those are two different processes. If consensus is required, the second sentence is redundant. If maintainers decide regardless, the first sentence is theater — it invites a contributor to treat consensus-building as the actual mechanism, when the real mechanism is "you and Jonas decide, informed by whatever came up." That mismatch is what makes a contributor feel lied to, not the fact that maintainers hold authority. Maintainer-fiat-with-consultation is a completely normal model for a 2-person project — Jonas isn't wrong that heavy process would be overkill here. He's wrong to think the current wording *describes* that model. It describes something closer to community consensus and quietly overrides it.

**Case 2 — you and Jonas disagree.** The document has no answer. Not a vague one — none. For a project with exactly two maintainers, this isn't an edge case, it's the load-bearing scenario the whole document exists to cover, and it's the one place a written governance doc earns its keep over just winging it in DMs. This is the strongest part of the contributor's complaint even if they didn't phrase it this way.

**Case 3 — "maintainers feel someone is ready."** No criteria, no proposal path, no objection mechanism, nothing a contributor could point to and say "I meet the bar." This one actually is close to meaningless — it's not a process, it's a description of the status quo ("we'll know it when we see it"), dressed up as a policy.

So: Jonas's error is availability bias — it's "fine" because it has never yet been tested by a real dispute between the two of you, and informality has worked so far. The contributor's error is treating underspecification as equivalent to no governance at all; the doc does correctly convey "this is maintainer-led, not a democracy," which is legitimate and doesn't need to change.

**What actually needs fixing — small, not a rewrite:**
1. Collapse the contradiction: state plainly that maintainers decide after considering community input. Drop "until consensus is reached" unless you mean it as a hard gate.
2. Add a tie-breaker for maintainer-vs-maintainer disagreement (e.g., default to status quo if no agreement within N days, or split final say by domain, or alternate).
3. Replace "feel someone is ready" with one or two observable signals (sustained contribution over N months; proposed by one maintainer, no objection from the other within N days). Doesn't need a vote or a committee — just something a contributor can point to.

That's proportionate to a 2-maintainer embedded database, not a burden — closer to Jonas's instinct on scope, closer to the contributor's diagnosis on the actual defect.