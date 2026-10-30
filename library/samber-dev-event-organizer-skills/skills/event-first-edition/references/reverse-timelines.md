# Reverse timelines: decision to doors-open

Two sourced timelines, driven by format and footprint. Present them as named variants - never average them into one number. Both come from community-run organizations - for a company-run event, treat the sequencing as transferable and the volunteer-bandwidth assumptions as not.

## Conference-scale: ~12 months (source: DevOpsDays organizing guide)

The reverse timeline DevOpsDays publishes for a new multi-day community conference, from its `organizing` guide:

| Milestone                                                                                                                                                                                   | When         |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------ |
| Venue search kicks off (large venues book years out)                                                                                                                                        | T-12 months  |
| Budget discussions start (drives sponsorship targets and ticket price)                                                                                                                      | T-10 months  |
| Venue locked                                                                                                                                                                                | T-9.5 months |
| Organizing team confirmed; work distribution begins                                                                                                                                         | T-9 months   |
| Organizer kickoff dinner (deliberately social - "organizing will have ups and downs, start it off strong"); sponsor prospectus goes out (larger sponsors commit budget a fiscal year ahead) | T-8 months   |
| CFP opens (a longer CFP window raises both submission volume and program quality); semimonthly organizer check-ins start                                                                    | T-7.5 months |
| Marketing outreach running                                                                                                                                                                  | T-7 months   |
| Registration opens                                                                                                                                                                          | T-6.5 months |
| Organizers vote on submissions (speakers need lead time for employer approval and travel)                                                                                                   | T-4.5 months |
| Program launches publicly; early-bird pricing closes                                                                                                                                        | T-3.5 months |
| Day-of volunteer check-in                                                                                                                                                                   | T-1 month    |
| Doors open                                                                                                                                                                                  | Month of     |

## Hackathon-scale: 4-9 months (source: MLH hackathon organizer guide)

The same reverse-timeline pattern compressed for a single-day/weekend hackathon, from Major League Hacking's public organizer guide:

| Milestone                                                                                                                        | When              |
| -------------------------------------------------------------------------------------------------------------------------------- | ----------------- |
| Date and purpose fixed, leadership team built, venue locked (the three foundational steps a conference spreads over ~2.5 months) | 4-9 months before |
| Placeholder site live; budget drafted; sponsor prospectus assembled; sponsor outreach begins                                     | 4 months before   |
| Marketing starts; main site live; registration opens; logistics planning begins                                                  | 3 months before   |
| Judging and mentorship plans drafted; judge/mentor booking; vendor work (food etc.) begins                                       | 2 months before   |
| Detailed run-of-show; final headcount; dietary requirements; transportation                                                      | 1 month before    |
| Reminder emails; physical setup; emergency plan; full schedule run-through; judge/mentor follow-up                               | 1 week before     |
| Check-in, meals, judging, mentorship, ceremonies                                                                                 | Event day         |

## Why the gap is real

The ~12-month and 4-9-month figures differ because of event duration, venue size, and CFP cycle - a multi-day conference carries a 4-month CFP-to-program pipeline and venues that book a year out; a weekend hackathon carries neither. An organizer choosing a format (via `samber/dev-event-organizer-skills@event-format-selection`) is also choosing a runway. A first-time team that borrows the hackathon timeline for a conference discovers the venue and CFP math doesn't compress; one that borrows the conference timeline for a hackathon burns volunteer stamina on a launch that needed half the runway.

## Administrative first steps (sourced sequence, DevOpsDays)

Complete before any public announcement, in this order:

1. Team decided → contact the parent or mentor organization where one exists, for a kickoff call.
2. Get publicly listed with organizer names + city + "coming soon" - no date or venue required yet.
3. **Code of conduct published before that very first listing** - the earliest hard gate in the whole process, ahead of venue and date. A team treating the CoC as a later nice-to-have gets blocked at this step before anything else can proceed. Content of the CoC: `samber/dev-event-organizer-skills@event-code-of-conduct`.
4. A dedicated, neutral event email alias as the public contact - never a personal or company address, so no organizer's employer looks like the event's owner.
5. Shared credential vault once delegation starts - many vendor/social/ticketing logins need common secure access, not one organizer's password manager.
6. Join a peer-organizer network (DevOpsDays runs a global organizer Slack) - cross-event mentorship beats solving every problem from scratch.

## Delegation structures

**5-function leadership team** (source: MLH - "think like a startup CEO", complementary skills, one accountable owner per function, tasks in a shared task tracker):

| Function       | Owns                                                                                                    |
| -------------- | ------------------------------------------------------------------------------------------------------- |
| Lead organizer | All decisions across the team                                                                           |
| Logistics      | Venue, schedule, swag, prizes, food                                                                     |
| Finance        | Sponsorships secured, vendor payment timelines, cash flow                                               |
| Marketing      | Promotion, website, social                                                                              |
| Operations     | The attendee experience itself - named by the source as the team most likely to make or break the event |

**9-role delegated team** (source: DevOpsDays, stood up at the T-9-month "confirm organizers" milestone, one person or pair per role): talk proposals, short-format/ignite proposals, website, speaker relations, sponsorships, registration & invoicing, venue & local logistics, merchandise, evening-event logistics.

Same delegation principle at two granularities - the coarser one fits the smaller, shorter event. Not a contradiction between sources.
