# KPI shortlist and outcome log

Treat it as field testimony, not established practice. Everything unmarked is this skill's own construction.

## Contents

- Why a shortlist
- Candidate KPIs
- Shortlist card
- Local vs network split
- Impact-intensity score
- Who judges impact
- Outcome log

## Why a shortlist

Tracking many KPIs moves nothing: nobody owns them. Keep 2-3. A KPI earns its place only when it has an owner and an action that moves it.

## Candidate KPIs

Each row adds this skill's note on what the KPI can and cannot tell you.

| Candidate                                | Reads                          | Typical owner   | Caveat                                                                        |
| ---------------------------------------- | ------------------------------ | --------------- | ----------------------------------------------------------------------------- |
| Social followers                         | Reach                          | Comms           | Vanity unless tied to attendance; a demand read belongs to `event-market-fit` |
| Video views and subscribers              | Reach beyond the room          | Content         | Lags by months; compare edition to edition only                               |
| Satisfaction (survey sent automatically) | Experience                     | Program or ops  | Response rate decides confidence; collection owned by `event-feedback`        |
| Financials (surplus, cost per attendee)  | Sustainability                 | Treasurer       | Read with `event-budget`, never as a success score alone                      |
| Number of events and speakers            | Output                         | Program         | Output, not outcome; rises while quality falls                                |
| New vs returning attendee ratio          | Acquisition vs retention       | Comms + program | A demand signal; hand the trend to `event-market-fit`                         |
| Share of women (attendees, speakers)     | Inclusion                      | Program         | Count speakers and attendees separately                                       |
| Projects or companies spawned            | Impact                         | Whole team      | Needs the outcome log below; self-reported                                    |
| Self-rated "impact intensity" per event  | Impact, as organizers judge it | Lead organizer  | Organizer opinion; see who judges impact                                      |

## Shortlist card

One card per kept KPI. A card with an empty field is not kept.

```
KPI:            New vs returning attendee ratio
Owner:          <named person, not "the team">
Action:         <what this owner does when it moves the wrong way>
Source:         <ticketing export / survey / outcome log>
Cadence:        <per event / per season>
Threshold:      <self-set, declared before reading>
Scope:          <local / network>
```

Negative example: "KPI: engagement. Owner: everyone. Action: improve it." No owner, no action, no source - it will be reported every quarter and change nothing.

## Local vs network split

For a community that belongs to a peer network of independent communities (`samber/dev-event-organizer-skills@event-team-structure`):

- **Local KPIs** - one chapter owns and moves them: satisfaction, new vs returning ratio, events and speakers, share of women.
- **Network KPIs** - only the network can move them: active chapters, shared-asset use, cross-chapter projects or companies, combined reach.

Never add local numbers into a network league table without the chapters' agreement; a ranking between peers breaks the horizontality most peer networks state as a value.

## Impact-intensity score

Some teams assign each event a self-rated "impact intensity" score. To make it comparable across editions:

1. Fix the scale before the season (for example 1-5), with one written anchor per point.
2. Score within days of the event, in the debrief, by at least two organizers independently.
3. Record disagreement rather than averaging it away.
4. Read it beside attendee data, never instead of it.

## Who judges impact

Organizers disagreed: should the team judge impact, or attendee questionnaires? Record both and do not force a winner:

- **Team judgment** - sees outcomes attendees cannot (a company founded months later, a sponsor converted). Biased toward effort spent.
- **Attendee questionnaire** - sees the experience. Biased toward the evening's mood, and blind to outcomes that appear later.

Where the two diverge for two editions running, that gap is itself a finding to route to `samber/dev-event-organizer-skills@event-positioning` (the promise may not match what attendees get).

## Outcome log

A dated list of what happened _because_ the event happened, appended after each event and audited with the main log.

| Date found | Event and edition | Outcome type                            | What | Source                      | Consent to publish |
| ---------- | ----------------- | --------------------------------------- | ---- | --------------------------- | ------------------ |
|            |                   | Project / collaboration / company / job |      | Self-report / organizer saw |                    |

- Nearly every hackathon edition can produce at least one company. Treat that as a reason to keep the log, not as a benchmark to hit.
- Collect outcomes in the follow-up survey (`samber/dev-event-organizer-skills@event-feedback` owns the hackathon continuation instrument) and in a standing "tell us what came out of it" ask.
- Ask consent before naming a person or company publicly; the log itself can stay internal.
- Outcomes surface months later. Re-open the log at the kickoff audit pass, not only after the event.
