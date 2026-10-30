# Reading failures and case studies

How demand reads go wrong, the frameworks that prevent it, and the sourced cases to calibrate against. The frameworks in the first two sections are not event-industry authorities; clearly label them as product-practice thinking tools when presenting to a team.

## The job statement and the four forces

Nobody "wants a conference" - an attendee or sponsor hires it to make progress on a job. A concept that can't fill in the pattern below has no demonstrated job yet - that finding alone can justify a hold verdict before any instrument runs.

Template: "When [circumstance], I want to [progress], so I can [outcome]."

Worked example: "When evaluating a new stack, between jobs, or the only X in their company, I want to validate my approach against peers or meet 20 relevant people in a day, so I can [outcome]."

Four forces on the ticket or sponsorship decision:

- **Push** - what currently frustrates the prospect (isolation, no local peer group, stale knowledge).
- **Pull** - what attracts them to this event over alternatives (a rare topic, a name speaker, a community they want into).
- **Anxiety** - travel cost, time off, "will this actually be good", first-edition credibility risk.
- **Habit** - the existing channels (blogs, a meetup, an online community) already doing the job well enough.

The decision moves only when push + pull outweigh habit + anxiety. Diagnostic value: a first edition with strong pull but no answer to anxiety sells slowly despite real demand underneath - which is why slow first-edition sales must be read against the checkpoint differential, not as a verdict on the concept.

Competition mapping: the real competitors include every other way to get the job done - the existing meetup, a Discord, recorded talks on YouTube, and staying home. Non-consumption is usually the biggest competitor for a first edition; read low early sales against that baseline, not only against rival events.

## Big Hire vs Little Hire

- **Big Hire** - the ticket purchase or sponsorship signature: one-time, driven by positioning, lineup, first impressions.
- **Little Hire** - showing up, staying through the day, returning next edition, renewing the sponsorship: driven by delivered value.

A sold-out first edition with poor year-two return is a Big Hire win and a Little Hire failure - an experience problem, not an acquisition problem, with a different owner and a different fix. This is why the skill's lagging signals are reported as separate numbers ("did they buy" / "did they come back") and never blended into one success score.

## The failure differential

A shutdown, a decline, or a soft sale is only demand evidence if the organizer's own account cites demand - sales, sponsors, attendance. Before a pivot or stop verdict, classify which story the evidence actually tells:

| Evidence pattern                                                              | Actual failure class      | Route                                           |
| ----------------------------------------------------------------------------- | ------------------------- | ----------------------------------------------- |
| Checkpoints at 25-30% and the visibility push was skipped or late             | Marketing execution       | Marketing sibling; re-read after the push       |
| Healthy page traffic, low conversion, first two weeks                         | Price misfit              | Pricing sibling                                 |
| Attendee signals green, sponsor renewal collapsing                            | Sponsor-side demand shift | Sponsor value-prop/fulfillment work; hold scale |
| Trust scandal, fraud, governance conflict in the record                       | Not a demand read at all  | Exclude from the market-fit evidence            |
| Organizer's own account cites saturation, demand shift, or falling attendance | Genuine demand signal     | This skill: pivot or stop                       |

## Sourced cases (calibration set)

- **RailsConf (ended 2025) - contested; carry all three readings, never cite one as "the" reason.**
  - Organizer (Ruby Central): cited slow return to in-person events plus "many new conference choices available" - an explicit saturation and demand-shift read - and consolidated onto one flagship.
  - Insider framing (DHH): healthy baton-passing to a successor event that sold out 1,000 tickets in under 20 minutes.
  - Competing organizer account (André Arko): attributes the wind-down to governance and open-source conflicts, not demand.
  - All three come from parties directly involved and contradict each other - a model case of why single-narrative shutdown evidence is unreliable.
- **XOXO (retired 2024) - sponsor-demand collapse, not attendee-demand collapse.** Co-founder Andy Baio: the festival scaled down "because there were fewer sponsors … the tech companies … stopped spending money on independent events." Attendee sentiment stayed positive to the end - the clearest real-world case of an event dying on one signal axis while another stayed green, the argument for tracking the axes independently.
- **Comdex (cancelled 2004) - category-level saturation/obsolescence.** From >200,000 attendees to cancellation after years of falling attendance, once major vendors moved to self-hosted shows: demand shifted away from the format itself, not from the topic.
- **GDC 2026 - macro decline, not an organizer post-mortem.** A 30% attendance drop (20,000 vs 30,000+) attributed by press coverage to industry layoffs and visa hostility - a macro data point to contextualize a soft year, not evidence any one event lost its fit.
- **Counter-examples to exclude:**
  - DevTernity (2023): collapsed over fabricated speaker profiles - a trust failure.
  - XO Music Festival (2018): cited "lower than anticipated ticket sales" but is fundamentally a fraud/logistics story.
  - Both look like demand stories in headlines and belong in the last-but-one row of the differential table.

## Worked composite read (illustrative - the structure is the point, every number is invented for the example)

**Setup:** community-run data-engineering conference, edition 2, 400 expected sales net of comps, one prior edition.

| Signal                            | Declared threshold                   | Actual        | Confidence                      | Read  |
| --------------------------------- | ------------------------------------ | ------------- | ------------------------------- | ----- |
| Attendee return                   | >30% (aim 45% for a tight community) | 41%           | threshold sourced; aim self-set | green |
| Sponsor renewal                   | ≥70% (practitioner aim)              | 58% (7 of 12) | self-set target                 | red   |
| Sales pace vs own edition-1 curve | pace ≥90 at day 30                   | 96            | method sourced; gate self-set   | green |

**Call:** hold-and-fix, not go - two of three green, but the red axis is the high-confidence one, and renewal money is deliberate. The differential shows attendee demand intact; the sponsor axis needs its own diagnosis (were the recap and the second-stage report sent? did logo retention hide downgrades in gross and net revenue retention? was the value proposition ever articulated beyond a logo?). Scale decisions wait one edition.

**Negative example** (the same data misread): "We're at pace 96 and attendees are returning - book the bigger venue." This blends the axes into one optimistic score, ignores that sponsors fund the budget, and repeats the documented pattern of an event dying on the sponsor axis while its watched signals stayed green. A composite read that cannot produce a hold verdict from mostly-green data is a rubber stamp, not an instrument.
