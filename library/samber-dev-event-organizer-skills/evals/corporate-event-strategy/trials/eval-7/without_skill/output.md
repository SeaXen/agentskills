# Recommendation: commit to pipeline, report adoption as a secondary readout

## The goal

**Commit to one measure: qualified sales opportunities created from HaloForge Summit registrants within 60 days of the event.**

Write the target number down before the event. Set it from the spend: `target = spend ÷ the pipeline-to-spend ratio your board expects`. I don't have your spend or ratio, so those two inputs are yours.

Adoption becomes a directional readout with no target. Nobody is held to it.

## Why pipeline

1. **It is the cheapest link to build.**
   - The registration-to-CRM link is a list upload. Match on email and tag each registrant as a campaign member.
   - Sales then records opportunities as part of their normal job. Nobody has to keep that going after the analyst leaves.
2. **Adoption costs more and is harder to defend.**
   - It needs identity stitching between registrations and product analytics.
   - It also needs a pre-event baseline and a comparison group. Without those, any rise could be coincidence.
   - Someone has to run all of that after October.
3. **It matches the pilot decision.**
   - The board wants to know whether to repeat the event.
   - "Cost per opportunity" answers that directly. An adoption lift for one cohort does not.
4. **It satisfies the CFO and mostly satisfies the CEO.**
   - The CFO wanted the cheapest thing to measure, and this is it.
   - The CEO still sees adoption movement, just labeled as directional.

## Why not commit to both

- Two committed goals means two unbuilt integrations, two sets of definitions, and one analyst with weeks left.
- A first event gives a small sample. Splitting attention across two targets guarantees neither is measured well.
- Reporting adoption without committing to it still gets the CEO the story without the risk.

## How to keep the adoption readout cheap

Do these now, before the analyst leaves.

1. **Take a baseline snapshot.** Export the product-usage state of every known account and user before the event, and store it somewhere permanent.
2. **Do one email match.** Run a one-time join of registrant emails to product users, with no live integration. Save the SQL and the output.
3. **Compare once at day 30 and day 60.** For matched registrants, count activations or key actions against their own baseline. Label the result "directional, not attributable."
4. **Write a one-page handover.** It should cover the queries, the definitions, and where the files live, so a non-analyst can rerun it.

## Pre-commit the definitions this week

- **Qualified opportunity:** use the stage name your sales process already has. Do not invent a new one.
- **Registrant vs. attendee:** decide which counts. I suggest attendees plus registrants who had a meeting booked.
- **Existing opportunities:** exclude any opportunity open before the event. Count only new ones created after it.
- **Decision rule:** decide now what "repeat" and "don't repeat" mean in numbers, so the result can't be argued afterward.

## Risks to say out loud

- **Sales cycles may be longer than 60 days.** Platform-engineering deals often are. Opportunity creation is a fair early signal, but closed revenue won't show up in this window.
- **The sample will be small.** Treat the result as a go/no-go signal, not a statistically proven return.
- **Registrations that skip the CRM link don't count.** Check that every registration path feeds the upload, including walk-ins and partner lists.

## Questions that would sharpen this

1. What is the spend and the board's expected return?
2. How many registrants do you expect, and how many are already in the CRM?
3. What is your typical time from first meeting to opportunity?