# Channel menu and budget allocation

The sourced channel taxonomy behind the ranked menu, the campus-scale tactic catalog, the owned/earned/paid framing, the four budget postures, and a positive/negative allocation pair.

Contents: The five sourced channels · Campus-scale tactics · Owned/earned/paid · Message discipline across channels · Budget postures · The percentage allocation table · Worked allocation pair.

## The five sourced channels (conference scale)

Source: DevOpsDays organizing guide (`devopsdays/devopsdays-web`, `content/page/organizing.md`), "Visibility" section. The section opens by naming the problem the plan exists to solve: "With the dispersal of tech communities from Twitter, a lot of community events are struggling to reach people."

1. **Mailing lists** - "Use your mailing list to announce ticket availability, early bird offers, agenda releases, and event countdowns. Keep emails informative and limit their frequency to maintain engagement." Framed as "a powerful tool for ticket sales" - the only channel the guide labels that way - and worth building from scratch if the event has none. The send moments this implies are the campaign calendar's anchors. The emails themselves belong to `samber/dev-event-organizer-skills@event-attendee-email-sequences`.
2. **Engage locally** - attend local meetups and networking events, collaborate with local employers on promotions, engage local business associations. Two explicit instructions:
   - "Avoid the misconception that a great agenda alone will attract attendees. Actively promote your event."
   - Be "proactive early in the ticket sales phase and maintain visibility until the event."
3. **Collaborate with other events** - "Partner with local events that align with your theme. Offer mutual promotions." For an established event, "nurture relationships with local meetups" since "a thriving community is an active one." Executed by the `samber/dev-event-organizer-skills@cross-event-promotion` and `samber/dev-event-organizer-skills@event-media-partnerships` siblings.
4. **Centralize communication** - "Create a hub for all your communication channels, from mailing lists to social media profiles. Consider using QR codes for easy sharing." A single link hub, named explicitly rather than left implicit.
5. **Active social media presence** - "Post regularly across all your social media platforms. Vary your posting times to maximize reach... Building an early presence can significantly boost your event's visibility."

## Campus-scale tactics (free / student events)

Source: MLH hackathon organizer guide (`MLH/mlh-hackathon-organizer-guide`, `general-information/marketing-your-event/promoting-your-event/README.md`). The guide instructs organizers to scope the target community first - local, then city, then state or country, then abroad - before choosing tactics.

- **Physical flyering** - explicitly framed as under-rated: "People underestimate how much flyers can help... more flyers means you are more likely to get people to actually read it."
- **In-person pitches** - "Speak in-person during the first 5 minutes of relevant classes and student group meetings," covering what, why, when and where, and how to learn more.
- **Student groups and departments**:
  - Named student-group examples: ACM, IEEE, SWE, SHPE.
  - Named department examples: CS, Design, Engineering, Applied Math, Physics, Business.

  Professors may share with students or offer extra credit. A second-order tactic: invite those groups to run a workshop or volunteer, which makes their own members self-market the event.

- **Invite other schools** - a concrete radius rule, **"at least 3 schools within 6 hours of your campus,"** with an explicit reminder not to overlook community colleges.
- **Tabling** - a staffed table with swag previews, an explainer for people unfamiliar with the format, and a QR code or URL handout.
- **Social campaign**:
  - Platform list: TikTok, Facebook, Twitter, Instagram, Reddit, LinkedIn.
  - Cross-promotion asks inside relevant community groups.
  - Targeted paid social ads, flagged as "cheap and effective" (a campus-audience claim, not a general one).
  - Developer-ambassador programs (campus-expert, student-ambassador and developer-group programs) as cross-promotion channels.
- **Pre-event press** - school newspaper, local outlets, startup or media agency partnerships. Named as lighter-weight than a full press campaign.

Reusable asset: the guide ships a short fill-in-the-blank marketing email template with:

- A subject line naming the location.
- A one-paragraph body naming dates, location and concrete perks (workshops, prizes, food, swag).
- A registration link.
- A social-proof pointer to the event's own channels.

Hand it to `samber/dev-event-organizer-skills@event-attendee-email-sequences` rather than expanding it here.

## Owned / earned / paid

A general campaign-planning frame rather than an event-specific one. Useful as a completeness check when mapping segments to channels - it catches a plan that is entirely owned-channel and blind to everything else.

- **Owned** - website, mailing list, the event's own social accounts, the comms hub.
- **Earned** - press, community engagement, word of mouth, partner and ambassador mentions the event did not pay for.
- **Paid** - search and social ads, sponsored content, display.

One relabeling matters. The source lists "events/sponsorships" as a _paid_ channel. In this collection that slot is filled by reciprocal-visibility swaps with other events and media properties rather than a cash spend, so for an event marketing plan, that rung moves from paid to earned.

Channel-selection criteria from the same source are generic enough to reuse as-is:

- Where the audience already is.
- Buying-stage fit.
- Budget.
- Existing content assets.
- Past performance.

## Message discipline across channels

- Tailor messaging per audience or per school rather than reusing one generic block, while keeping the core message consistent across channels "to build momentum" (MLH).
- Required elements in any promotional asset: date, location, website URL, and concrete perks (MLH).
- The core message itself is not authored here - it comes from `samber/dev-event-organizer-skills@event-positioning`. This plan only decides which channel carries which segment's version of it.

## Budget postures

- **Barter-only.** Owned channels plus reciprocal-visibility swaps. No cash, no approvals, no reconciliation. The natural default for a community-run event whose budget is ~80%+ sponsorship-funded and where acquisition money competes directly with catering, venue and travel.
- **Fixed test budget.** One capped amount, one paid channel, one question decided in advance ("does targeted social bring registrations from segment X at a cost we would repeat?"). Small enough to clear under one organizer's discretion, structured enough to produce an answer rather than a spend.
- **Concentrated bet.** The bulk of available cash into the single highest-confidence channel. The general convention puts 60-70% into that channel, 15-20% reserved for testing new ones, and 10-15% contingency - a SaaS marketing figure, not an event-industry one.
- **Full spread.** The percentage table below, across every line at once. Highest coordination and approval load; only worth its overhead where the reporting is somebody's actual job.

## The percentage allocation table

These shares are generic B2B/B2C SaaS marketing-budget conventions, borrowed rather than measured on events. **Say so every time the table is shown.** Presented bare it reads as an events benchmark the reader will defend to a board that has no reason to accept it.

| Line                                        | Share  |
| ------------------------------------------- | ------ |
| Paid acquisition                            | 30-40% |
| Content production                          | 20-30% |
| Events / sponsorships (here: partner swaps) | 10-20% |
| Tools                                       | 10-15% |
| Testing                                     | 5-10%  |

## Worked allocation pair

**Good - a 320-ticket community conference, volunteer team of five, €2,000 available.**

Posture: barter-only plus a fixed test budget.

- €0 to owned channels (mailing list, comms hub, social): organizer hours only, ~1-2h/week across the cycle.
- €0 to partner channels (four swaps and two media partners, routed to `samber/dev-event-organizer-skills@cross-event-promotion` and `samber/dev-event-organizer-skills@event-media-partnerships`).
- €600 as a capped test on targeted social ads in the two weeks after the announcement, aimed at one named segment, with a tracked link.
- €1,400 held for the final-two-weeks push, released only if the one-month-out checkpoint lands below 40%.

Every channel carries the segment it was bought for and a tracked link decided before launch.

Why it works:

- The money sits behind a decision point instead of being committed on day one.
- The top-efficiency rungs cost nothing but hours.
- A checkpoint miss has a pre-agreed response.

**Bad - the same event, same money.**

Posture: full spread, because the percentage table looked authoritative. The whole budget committed in week one, before a single checkpoint:

- €700 to paid ads.
- €500 to "content production".
- €300 to partner activity that was already barter and needed no cash.
- €300 to tools.
- €200 to testing.

No tracked links, so the "how did you hear about us" field is the only attribution and it credits whatever the registrant saw last. The early-bird checkpoint misses at 9%. The response is to buy more ads, because nothing in the plan distinguishes an execution shortfall from a demand shortfall.

Why it fails:

- The table's shares were never measured on events.
- Cash was spent on a channel that trades in visibility rather than money.
- Attribution was made impossible before launch rather than after.
- The plan had no pre-decided response to a miss, so the miss was answered with reflex.
