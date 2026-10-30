# Question sets by format and role

## Contents

1. Conference and meetup core
2. The hackathon layer
3. Role modules: attendee, speaker, sponsor
4. Closed-versus-open balance
5. Anonymity
6. Worked question pairs
7. Named frameworks and who publishes them

## 1. Conference and meetup core

Published across the event industry by PCMA, ASAE, SurveyMonkey, Bizzabo and Formbricks. These are the questions the field converges on:

- Overall satisfaction, or a 0-10 likelihood-to-recommend.
- Session and speaker ratings: relevance, delivery, depth.
- Networking quality.
- Venue and logistics: registration, audio-visual, food, wifi.
- Content value relative to time and cost spent.
- Likelihood to return next edition.
- One open-ended "what should we change".

For a meetup, simplify by keeping the likelihood-to-recommend and the open box, dropping the rest. A 40-person room has no networking programme, registration desk or cost to justify, and asking about them collects polite noise.

## 2. The hackathon layer

Published by MLH's organizer guide, Brightidea's hackathon retrospective framework, SuperSurvey's hackathon template, and two academic hackathon studies. The first, a COVID-19 health hackathon in April 2020, fielded 17 items plus 5 optional ones and a separate mentor survey; the second, a Brazilian affirmative-action hackathon, ran three surveys across event stages. These dimensions are absent from ordinary conference surveys, yet academic instruments treat them as first-class measures:

- **Team dynamics** - how easily teams formed, collaboration quality, whether they would work with those teammates again.
- **Mentor and coach quality** - availability, and whether on-the-spot feedback was useful.
- **Judging** - fairness, clarity of criteria, transparency of the decision.
- **Tooling** - quality of APIs, SDKs, documentation and office hours, especially sponsor-provided ones.
- **Outcomes** - project completion, intention to continue, skills learned, connections built.
- **Format-specific logistics** - food and overnight arrangements, wifi under sustained load, and whether an "I need help now" path existed.

The multi-stage, multi-role pattern in both academic instruments is itself the finding: a hackathon is not surveyed once. The main instrument fields at demo day or closing; the continuation question fields one to two weeks later, because asked on the day it only ever collects intention.

## 3. Role modules

### Attendees

Same as the conference core above. Listing them as a separate role only matters once a second role exists.

### Speakers

Published by Cvent, Whova and Formgrid question banks. These measure organizer performance, not session quality:

- "How would you rate our communication and supply of information pre-event?" - finds speaker-management gaps.
- "How would you rate the venue and presentation equipment?" - audio-visual and logistics, all organizer-controllable.
- Audience engagement, and whether the speaker achieved what they came to do.
- Whether they would recommend qualified peers as future speakers.

Some organizers argue a speaker gains more from a personalized follow-up note than from a formal survey. Where a conference has six speakers, a short personal message collects more than a form does, and the delivery choreography for it belongs to `samber/dev-event-organizer-skills@event-speaker-experience`.

### Sponsors

Published by Bizzabo, Formbricks, SurveyMonkey, Cvent:

- Satisfaction with meaningful traffic to the booth or stand.
- Quality of leads generated - the primary return-on-investment metric.
- Whether the specific goals set for this sponsorship were met.
- **Audience fit for their brand and business goals - this predicts renewal better than raw lead count.** The single most useful non-obvious finding in this block: an instrument over-indexed on lead volume misses why a sponsor leaves.
- Logistical support: booth setup, signage, communications.
- Likelihood to sponsor again.

When a sponsor answers "no" to sponsoring again, treat it as a trigger for an immediate phone call, not as a spreadsheet row to analyze later - run it through `samber/dev-event-organizer-skills@event-sponsor-renewal`'s rescue path.

### Attendees, about sponsors

Asked of attendees, feeding each sponsor's post-event report (`samber/dev-event-organizer-skills@event-sponsor-fulfillment`). Constructed on IEG's aware-vs-unaware logic, not a published set:

- Unaided recall: which sponsors do you remember?
- Aided recall: the sponsor list plus one company that did not sponsor (the decoy's rate is the guessing baseline).
- Interaction: talked with staff / attended their session / used their API or prize track.
- Perception shift, 5-point.

Keep contact opt-ins for sponsors out of the anonymous survey: an opt-in needs an identity. At a many-sponsor event, rotate sponsors across respondents.

For a hackathon or event run specifically for hiring, add:

- API/SDK/documentation quality.
- Office-hours usefulness.
- Prize-structure effectiveness.
- Talent-pipeline value.
- Interview-conversion rate and cost-per-hire.

The last two are meaningless for a community event with no hiring purpose, so do not include them by default.

## 4. Closed-versus-open balance

Aim for 70-80% closed-ended questions and 20-30% open-ended, with open-ended questions capped at three to four (Formbricks' published design rule). Closed questions make results comparable across editions; open questions surface what the instrument failed to ask about. But unlike product research with a standing pipeline, an event's respondents disperse, so an open answer either gets acted on immediately or is lost.

## 5. Anonymity

Turn anonymity on specifically when asking about judging fairness, inclusion, or mentor quality (SuperSurvey's hackathon template, AAPOR best practice, ISO 10004). The same applies to any question rating a named individual's performance: a respondent who suspects the subject will read their answer gives you a rating you cannot use.

## 6. Worked question pairs

No organizer guide publishes worked post-event questions, so these illustrate the phrasing rules. The craft itself comes from customer-discovery interviewing: ask about specific past behaviour rather than hypothetical future behaviour, and never write a question that signals the answer you want. But unlike that discipline, nothing is being sold here.

| Weak                                                                                                               | Better                                                                                       | Why                                                                                                                                                                                  |
| ------------------------------------------------------------------------------------------------------------------ | -------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| "Did you enjoy our amazing lineup?"                                                                                | "Which sessions did you attend, and which did you leave before the end?"                     | The first is leading and unfalsifiable. The second collects behaviour, and an early exit is the strongest session signal available.                                                  |
| "Would you attend a workshop day next year?"                                                                       | "Have you paid for a workshop day at another event in the last two years?"                   | Predicted behaviour is imagination; past behaviour is evidence.                                                                                                                      |
| "How was the venue?"                                                                                               | "Was there anything about the venue that made it harder to attend or to concentrate?"        | The first collects "fine"; the second names accessibility, noise, temperature and wayfinding problems.                                                                               |
| "Rate your overall satisfaction (1-10). Rate the content (1-10). Rate the venue (1-10). Rate the catering (1-10)." | "How likely are you to recommend this event (0-10)? What is the one thing we should change?" | Four scales collect one blended impression, answered on autopilot. Two questions collect a comparable number and an actionable sentence, which is the short-core rung's whole shape. |
| "Any other comments?"                                                                                              | "What is the one thing we should change for next edition?"                                   | An unbounded box collects either nothing or an essay; a bounded one collects the respondent's top priority.                                                                          |

## 7. Named frameworks and who publishes them

These frameworks are published and cited when needed:

- **PCMA** (Professional Convention Management Association) - publishes the _Metrics That Matter Most_ benchmark set, developed by two measurement practitioners at an event agency and presented at its 2017 education conference.
- **ASAE** (American Society of Association Executives) - post-event survey guidance: the 24-48 hour window, plain language, a polite reminder days later.
- **MPI** (Meeting Professionals International) - an authority on event measurement; no figure from it is cited here.
- **Explori** - a UK event-survey research specialist, and the clearest source of event-specific rather than generic survey figures. Its senior research manager Charlotte Penn and its interview with Nicola Kastner (former Global VP of Event Marketing Strategy at SAP) supply the response-rate figures in the evidence reference.
- **Bizzabo's R.A.T.E. framework** - Role-specific, Actionable, Timed right, Easy to answer. A four-word design check worth running an instrument against; the acronym is the vendor's, the discipline is generic.
- **MLH (Major League Hacking)** - the definitive hackathon authority; its organizer guide names surveying in one line and it benchmarks member events against each other privately rather than publishing an open benchmark.
- **Brightidea's hackathon retrospective framework** - scorecard alignment, sponsor return on investment, participant skills and relationships, recommendation score, would-attend-again.
