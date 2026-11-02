# ByteWorks Conf: speaker survey and the "71% vs 83%" report

## Short answer

1. **No, don't bolt the speaker questions onto the attendee form.** Run two instruments: a short attendee survey and a separate, small speaker survey.
2. **Don't report "speaker satisfaction: 71%" and compare it to 83%.** With 5 of 7 responding, report counts. Treat the year-over-year comparison as unsafe until you've checked the points below.

## 1. Why one form with 10 extra questions fails

| Problem | Effect |
|---|---|
| **Length.** The attendee core is 3-5 questions, and 10 more brings it to 13-15. | Survicate (267,564 responses, credible): surveys of 2-3 questions have a 15.97% median response rate, and surveys of 7+ questions drop to 6.87%. You'd cut the response rate for 240 attendees to serve 7 people. |
| **Wrong audience.** Speaker questions are about organizer performance: pre-event communication, AV, and whether they'd recommend peers. | Attendees can't answer them, so they skip them or abandon the form. Speakers wade through attendee questions that don't apply to them. |
| **One link means no role identity.** | You can't compute a response rate per role. The skill says to work that out before reading any answer. Speakers' answers also blend into attendee data, and a speaker may rate their own session. |
| **Anonymity conflict.** An attendee form that rates named speakers needs anonymity. | A 7-person speaker group can't be anonymous. You'd be making two incompatible promises on one form. |

Your own invocation example matches this case: the skill's guidance is that a role's instrument differs from the attendee one rather than just being longer.

## 2. What to field instead

**Assumptions to confirm (see the last section).** The event is already over, so in-room capture is off the table. I'm assuming no sponsors, no hackathon, and no anonymity promise yet made.

### Attendees (240 people): short core, 5 questions

Email plus one reminder is the default channel. Expect roughly 24-72 responses at the 10-30% emailed band (Explori, credible).

1. How likely are you to recommend ByteWorks Conf to a colleague? (0-10)
2. How likely are you to attend next year? (definitely / likely / unsure / unlikely)
3. Which sessions did you attend, and which did you leave before the end?
4. Was anything about the venue or logistics hard for attending or concentrating?
5. What is the one thing we should change for next edition? (open)

- **Anonymous.** If you add per-speaker ratings, anonymity becomes mandatory, because a respondent who suspects the speaker will read their name gives you an unusable rating.
- **No prize draw.** A draw needs an identity, which breaks the anonymity promise.
- **Expect to chase it.** The 24-48h send window (practitioner consensus, not measured) has probably passed. Send now anyway, with one reminder 3-5 days later and at most one final reminder. More than two reminders causes fatigue.

### Speakers (7 people): core plus role module, about 5 questions

From the published speaker bank (Cvent, Whova, Formgrid). Keep only questions that map to a decision and a named owner.

1. How would you rate our pre-event communication and information? (1-5)
2. How would you rate the stage, AV and equipment? (1-5)
3. Did you achieve what you came to do? (yes / partly / no, plus one line)
4. Would you speak at ByteWorks Conf again? (separate from satisfaction)
5. What is the one thing we should change for speakers next time? (open)

Optional: "Who would you recommend as a future speaker?"

- **Seven people are known by name.** Make a confidentiality promise, not an anonymity promise, and say who reads the answers. With n=7, anonymity is impossible.
- **Consider a personal message instead of a form.** At this size, a short personal note often collects more than a form. The delivery choreography belongs to `event-speaker-experience`.
- **Route sensitive free text correctly.** A code-of-conduct allegation goes straight to `event-code-of-conduct`. It is never a survey finding.

## 3. Why "speaker satisfaction: 71%" can't stand

1. **71% may be your response rate, not satisfaction.** 5 of 7 is 71.4%. If that's where the number came from, it's the wrong quantity. Check how it was computed.
2. **The number is almost unreadable at n=5.** As a share of respondents, satisfaction can only take values in steps of 20 points (0, 20, 40, 60, 80, 100). One speaker moving changes it by 20 points.
3. **The 12-point gap is smaller than one respondent.** A drop from 83% to 71% is less than the swing from a single person's answer. Treating it as a trend would be reading noise.
4. **Missing responders may be the unhappy ones.** Two of seven silent could change the picture entirely. Say so beside the number.
5. **Last year's 83% may not be comparable.** Check its denominator (83.3% is exactly 5 of 6). Also check whether the question wording, scale, and definition of "satisfied" match this year's. If not, it isn't comparable.
6. **Cross-edition comparison isn't this skill's job.** `event-continuous-improvement` owns trends. This skill produces one edition's findings and a comparable instrument.

### What to report instead

> **Speakers: 5 of 7 responded (71% response rate), by email.**
> - Satisfaction with communication: [x] of 5 rated 4-5.
> - Satisfaction with AV: [x] of 5 rated 4-5.
> - Would speak again: [x] of 5 yes.
> - Themes from free text: [theme, count, redacted quote].
> - What this can't tell us: 2 speakers did not respond; n=5 is too small for percentages.

Keep one number per thing, and never blend satisfaction with "would speak again" into a composite. For last year's figure, put "83%, definition and denominator not recorded" in the hand-off to `event-continuous-improvement`. Record this year's instrument as fielded so the next edition has a comparable one.

## 4. Closing the loop

- **Attendees:** send a "you said, we changed" note: thanks, the headline number, and 2-3 changes you're making.
- **Speakers:** reply personally to each. Per-speaker material and framing go through `event-speaker-experience`.
- **Don't publish** unless you asked for publication consent at collection time. Anonymous respondents can't be asked afterwards.

## 5. Hand-offs

- **`event-debrief`:** the whole findings summary, before the debrief meeting.
- **`event-market-fit`:** the qualitative read only (satisfaction, return intent, themes), as a signal, never a verdict.
- **`event-speaker-experience`:** per-speaker material.
- **`event-continuous-improvement`:** nothing directly. It receives findings through the debrief's log.

## Open questions

These could change the plan above:

1. What decision is waiting on the speaker answers, and who owns it? Any question without one gets cut.
2. Are there sponsors or other roles I haven't been told about? A sponsor module would be a separate question set.
3. Have you already promised anonymity to anyone?
4. When must findings be in someone's hands?
5. Is there a prior attendee response rate? If it was at or below the band floor and the event is over, an incentive becomes worth considering.
6. How was "71%" computed, and what were last year's 83% and its denominator?

## Evidence labels

- **Published or credible:** the Survicate length figures, the Explori emailed band, the speaker question bank, and the two-reminder ceiling.
- **Directional:** vendor-reported figures.
- **This skill's own judgment:** the 24-48h window (consensus, unmeasured), the choice of which 5 questions to keep, and the advice against percentages at n=5.