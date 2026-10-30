# Publishing precedents and the findings hand-off

Two things live here: the real precedents behind the public rung of the closing-the-loop menu, and the shape of what leaves this skill. Source attribution is stated per block.

## Contents

1. Published post-event reports that actually exist
2. Weaker evidentiary tier
3. The findings summary shape
4. What each receiving sibling is handed
5. What never leaves this skill

## 1. Published post-event reports that actually exist

Published reports with verifiable sample sizes:

- **WordPress (Make Community), 2021-2022 annual meetup survey.** Fielded 2 August to 15 October 2022, key findings published May 2023. **2,867 member responses plus 128 organizer responses, across 14 languages.**
  - Headline: 94% very likely (61%) or somewhat likely (33%) to recommend WordPress meetups.
  - Half of respondents were fully satisfied; among the rest, 46% cited a lack of in-person events, 29% lack of promotion, 25% content.
  - Top attendance factors: topic 29%, time of day 26%, day of week 24%, location 21%.

  **The most useful part is the methodology self-critique** - the post itself recommends dropping free-text fields, translating into fewer languages, and asking fewer questions next time. A published retrospective that admits its own survey-design mistakes is the model to copy, not the headline number. `make.wordpress.org/community/2023/05/02/2021-2022-wordpress-meetup-survey-key-findings/`

- **CNCF, KubeCon + CloudNativeCon transparency reports.** KubeCon EU 2020 (virtual): **87% overall average satisfaction**; 35% of surveyed attendees attended a maintainer-track session.

  CNCF's stated satisfaction across all events is 4.2/5. These reports carry demographics, session counts and diversity data as well - a wider transparency scope than a satisfaction survey. `cncf.io/reports/`

- **MLH hacker survey, 11 August 2014.** **920 student hackers.**
  - 85% wanted to participate in another hackathon.
  - 69% continued working on their projects afterwards.
  - 20% had a non-computer-science major.
  - 52% said their school had no hacking club.

  This is MLH's own published research, distinct from the single organizer-guide line about emailing a survey. `news.mlh.io/hackathon-experience-lasts-beyond-weekend-08-11-2014`

- **GitHub Blog / MLH learning-outcomes survey.**
  - 70% of students met or worked with people they had not worked with before.
  - Nearly 90% learned something new from a peer.
  - 80% explored a new technology.
  - Over 90% reported learning skills not covered in class.

  Useful as the precedent for asking learning-outcome questions at all.

- **PyCon 2008 feedback.** Raw feedback-form results published publicly on the Python wiki, **497 respondents** - the earliest instance of this norm found in developer communities, predating the others by well over a decade.
- **Write the Docs Prague 2017, "Recap and Retrospective".** One public post combining the attendee survey, the team's own retrospective, and a code-of-conduct transparency report. Note the boundary: the artifact is `samber/dev-event-organizer-skills@event-debrief`'s to decide on and to write; this skill supplies the survey half of it.

## 2. Weaker evidentiary tier

**Organizer-reported, not independently verified.** Useful as evidence that organizers publish outcome data, not as evidence of what the data means.

- **AngelHack / Discover "Innovation Hack" (2021)**: an organizer case study reporting 614 participants across 35 states and 196 cities, with over 65% having worked with colleagues they had never met. No survey instrument or methodology disclosed - marketing content.
- **Atlassian ShipIt**: an internal-data retrospective rather than a satisfaction survey - a reported 12% lift in a product's usage among hackathon participants, across 2,500+ participants and 1,200+ teams. A genuinely different data type: organizer-published outcome data drawn from product telemetry, not from asking anyone anything. Distinguish it when citing.

## 3. The findings summary shape

WordPress's own report (§1 above) is the closest published precedent for the shape below: it states response counts up front before any finding, keeps member and organizer findings in separate sections rather than blending them, and closes with a section naming what the survey design itself would change next time. No published report combines that structure with a per-role response rate, a themed free-text breakdown carrying its own count and a redacted quote, and an explicit line on what the collection could not answer - that fuller combination stays this skill's own construction, extending the real precedent rather than inventing one from nothing:

Per role surveyed:

- Population, responses, response rate, and the channel used.
- The headline number and what it is (satisfaction, return intent, recommendation) - one number per thing, never a composite.
- Themes from free text: the theme, how many responses carried it, and one representative quote, redacted of names.
- What the instrument failed to ask, inferred from what open answers kept raising unprompted. This is the highest-value line in the summary and the one most often left out.
- Everything the collection could not answer, said plainly: which roles under-responded, which questions were abandoned, what the response rate does to the confidence of everything above.

## 4. What each receiving sibling is handed

Hand off findings as follows, aligned with the boundaries each sibling sets:

- `samber/dev-event-organizer-skills@event-debrief` - the whole findings summary, as one document, before the debrief meeting rather than during it. It reconciles the summary against the team's own view; it does not want raw responses.
- `samber/dev-event-organizer-skills@event-market-fit` - the qualitative read only: satisfaction, return intent, and the themes. It owns the behavioural signals (return rate, sponsor renewal, sellout speed) and the go/no-go. Hand over a signal, never a verdict.
- `samber/dev-event-organizer-skills@event-speaker-experience` - per-speaker material: attendance, session ratings, written comments passed through in full minus abuse. It owns the timing, the framing and the never-bundle-with-a-request rule.
- `samber/dev-event-organizer-skills@event-sponsor-fulfillment` - each sponsor's own verdict, and immediately rather than at the end of the analysis where a "no" to renewing sits unread for a week.
- `samber/dev-event-organizer-skills@event-continuous-improvement` - nothing directly. Findings reach it through the debrief's log. Sending it a summary in parallel creates two versions of one edition's record.

## 5. What never leaves this skill

These rules are absolute:

- **A free-text allegation of a code-of-conduct violation** goes to `samber/dev-event-organizer-skills@event-code-of-conduct`'s reporting pipeline and nowhere else. It is not a finding, it is a report that arrived through the wrong door, and forwarding it to a debrief or a speaker is a serious failure.
- **A verbatim quote naming a person** does not get published, forwarded or quoted in a summary. Redact the name and keep the substance.
- **Raw response exports.** Whoever was promised anonymity was promised it against every downstream reader, including the sibling skills above. Hand over the summary, not the file.
- **A quote you did not ask permission to publish.** Publication consent is requested at collection time or the quote stays internal. An anonymous respondent cannot be asked afterwards.
