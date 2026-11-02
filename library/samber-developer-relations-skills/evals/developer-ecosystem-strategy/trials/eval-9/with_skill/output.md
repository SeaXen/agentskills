## What's actually going on at Ravensworth

Three quarters in, the program has one metric moving up (partners signed) and at least three metrics nobody is tracking that would tell the board the truth: activation, concentration, and adoption. That gap is exactly the failure mode this framework calls **ecosystem theatre** — a partner logo wall and a directory nobody installs from — and "partners signed" going "up and to the right" is the textbook symptom, not evidence of health. Announced partners measure your BD team's ability to get a signature. They say nothing about whether a customer's business changed.

Before picking board metrics, name what the current numbers already tell you:

- **34 announced → 6 live is an 18% activation rate.** Two-thirds of the pipeline the VP is reporting monthly has never shipped anything. That's a conversion problem sitting between "signed" and "built" — most likely a staffing/review-queue bottleneck (the skill's staffing gate) or a supply problem in disguise: partners who signed because it cost them nothing, not because their own arithmetic said build this.
- **Top 2 of 6 live integrations = 81% of ecosystem usage.** With only 6 shipped, that's not "concentration risk," that's the finding: you have two partnerships that work and four that are barely used. Report it as such to the board rather than folding it into an aggregate "6 integrations live" line.
- **~4% of 620 accounts (≈25 accounts) have any integration active.** This is the number that should have been on every board update since quarter one — it's the one that funds or kills the program — and it appears to have never been reported.

## Numbers to put in front of the board

Replace "partners signed" as the headline. Use it, if at all, as a footnote input metric, not the story. Bring this table instead, baseline-today / target-with-date, the same shape a credible ecosystem memo uses:

| Metric | Today | Why it's the real number |
|---|---|---|
| **Customer adoption (attach rate)** — accounts with ≥1 active integration | ~4% (≈25/620) | The number that determines whether the program pays for itself. This replaces "partners signed" as the headline metric. |
| **Concentration** — share of usage held by top integrations | 81% in top 2 of 6 | High concentration means you're running two partnerships with a directory around them, not an ecosystem. Report it as a diagnostic every quarter, not a vanity stat, and don't let it hide inside a blended "6 live" count. |
| **Activation** — live integrations ÷ announced partners | 18% (6/34) | Shows the signed→shipped bottleneck the VP's metric currently hides. If this doesn't move, adding more announced partners just grows the backlog. |
| **Time to first working integration** | Unknown — get this before the board meeting | Tells you whether the bottleneck is review capacity, partner engineering, or your own docs/API surface. |
| **Retention/expansion delta**, accounts with an active integration vs. without | Unknown — pull this before the board meeting | This is the number that actually justifies the program's cost. If it doesn't exist yet, say so and commit to a date, don't skip it. |
| **Cost** — engineering hours and support tickets tied to the 6 live integrations, plus the size of the review backlog behind the other 28 | Unknown | Tells the board what "34 announced" is actually costing you in unshipped queue, independent of what it's returning. |

If you can only add one number to the existing board deck this cycle, add the attach rate and put concentration directly underneath it — a rising attach rate next to an 81%-in-two-partners concentration line tells a very different story than either number alone.

## "What's a good attach rate for a program this age"

There isn't an industry figure to hand the board here, and reaching for one would be a mistake — any benchmark you'd cite is a vendor's marketing number for a differently-shaped program, not a measured norm for yours, and presenting it as external validation is how a board stops asking the harder question. The correct move is to set your own baseline and commit to your own target with a date, then hold the program to that, not to a cross-industry number.

Concretely:

- **Today's baseline is 4%.** That's the number to put in front of the board, not a percentage you found somewhere.
- **Don't set the target off the blended number.** Set it per-archetype if you can — the top 2 integrations that are already earning 81% of usage clearly found a real complementor business case; the other 4 (and the 28 unshipped) may not have. Before committing to a board-facing target, run the complementor arithmetic on the two winners: who built them, what's their reachable customer overlap, what do they earn — then check whether that arithmetic is even available to the other 32. If it isn't, more announced partners won't move the attach rate; it'll just grow the 18%-activation backlog.
- **Treat "3 quarters in at 4%, with adoption riding on 2 of 34 partners" as a signal to slow recruiting, not accelerate it.** The cheapest next step is closing the signed-but-unshipped gap and understanding why the two winners work, not adding a 35th logo.
- **Give the board a dated commitment, not a percentage.** For example: "we will not add new announced partners until activation (live/announced) crosses some threshold you set, e.g. 40%, by a specific quarter" or "top-2 concentration must drop below some ceiling before we call this an ecosystem rather than two partnerships" — a threshold with a date is a real deliverable; an attach-rate percentage borrowed from nowhere is not.

## One reframe worth saying in the room

The VP's "partners signed" trend line and the board's real question — is this program working — are not the same chart. Recommend the board's take-away from this meeting is: adopt attach rate + concentration + activation as the standing metrics, retire "partners signed" as a headline (keep it only as a pipeline input alongside activation rate, which shows what fraction of it converts), and set one dated threshold — either an activation-rate floor or a concentration ceiling — that triggers a real re-decision (freeze new signings and clear the backlog, or double down on the two integrations that are actually working) rather than another quarter of the same slide with a bigger logo wall.