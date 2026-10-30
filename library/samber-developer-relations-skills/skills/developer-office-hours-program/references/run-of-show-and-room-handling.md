# Run of show and room handling

## Contents

1. Run of show, 45-minute live session
2. Recording policy and notice script
3. Empty room protocol
4. Dominant, off-topic and hostile attendees
5. Promotion rhythm

## 1. Run of show, 45-minute live session

Adapted from the Kubernetes Office Hours run sheet, the only published one.

| Minute | Segment                                                                                                     | Owner                        |
| ------ | ----------------------------------------------------------------------------------------------------------- | ---------------------------- |
| -10    | Host and engineer in the room; test screen-share with a scrubbed demo environment; captions on if recording | Host                         |
| 0      | Welcome; recording notice; code of conduct; "we can't see your systems, so no live debugging"               | Host                         |
| 2      | Engineer introduces themself, one line on their area                                                        | Engineer                     |
| 4      | Pre-submitted questions, most widely useful first, 4-minute timebox each                                    | Host reads, engineer answers |
| 25     | Live questions from chat or the room                                                                        | Host moderates               |
| 40     | Parking lot read out: what goes to the write-up, what was logged for product                                | Host                         |
| 43     | Next session date, how to submit questions, thanks to the engineer and their team by name                   | Host                         |
| 45     | End on time                                                                                                 | Host                         |

Assign a notetaker who is not answering. GitLab rotates notetaker and timekeeper; the host cannot do both while moderating.

Log every question as Handle (only if the asker agreed) / Question / Answer / Links / Bucket. The log becomes the write-up. Copy consented handles onto logged feature requests, then delete the raw log once the write-up is published.

## 2. Recording policy and notice script

| Format                      | Policy                                                                                                                                |
| --------------------------- | ------------------------------------------------------------------------------------------------------------------------------------- |
| Livestream panel            | Record and publish with captions; announce destination and retention; offer camera-off, chat-only and anonymised reading of questions |
| Drop-in call                | Record only with notice, or publish the write-up instead                                                                              |
| Booked slots                | Never record; internal notes only                                                                                                     |
| Async thread, staffed queue | The text is the record; say so on the scope card                                                                                      |

Say it before recording starts and again when the recording begins, so late joiners hear it.

```
This session is recorded and published on [where] within [N] days, and kept [how long].
If you'd rather not appear, keep your camera off and use the chat; we read chat questions without names
if you ask. Don't share your screen if it shows tokens, customer data, or internal hostnames.
```

```
// ✗ Bad - consent assumed, nothing said about where it goes
"We're recording, hope that's OK!"

// ✓ Good - states destination and retention, offers a no-record path before anyone speaks
"We record this and post it on YouTube within three days. Camera off and chat-only keeps you out of it."
```

Before publishing:

- Watch every screen-share segment for tokens, keys, internal hostnames and customer names. Cut or blur.
- Revoke any token the hosts showed in a demo environment, as GitLab's token guidance recommends.
- Honour every "don't read my name" request from the intake form.

## 3. Empty room protocol

| Situation                                                              | Action                                                                                                                                          |
| ---------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------- |
| Drop-in call, empty queue                                              | Hold the slot. A slot that disappears teaches users it is unreliable                                                                            |
| Livestream panel, no pre-submitted question 24 hours before (baseline) | Cancel publicly on every channel the session was announced on, or switch to a planned segment: answer the top unanswered forum questions on air |
| Nobody joins in the first 10 minutes                                   | Answer the forum backlog for the write-up or the recording, then close. Log the session as held with zero askers                                |
| Rotation engineer drops out                                            | Named backup takes it. Engineer and backup both out: announce the cancellation. Never cancel silently                                           |
| Two empty sessions in a row                                            | Review slot and promotion before cadence: poll the audience, check the time zone split                                                          |
| Three sessions under the continue bar                                  | Bring the pilot review forward, and consider an async thread instead                                                                            |

The worst ending is a calendar entry still marked active after sessions stop. Announce pauses and closures in the same places as sessions. To end the program: publish a closure post, point to the async thread, remove every calendar entry.

## 4. Dominant, off-topic and hostile attendees

- **One attendee, many questions:** answer one, then "let's take others first and come back to you", and move the rest to the write-up or a booked follow-up.
- **One customer's account issue:** stop at the scope card. "That needs your account, which we can't open here. [Support link], and I'll mention it to them."
- **Live debugging request:** ask for a minimal reproduction in an issue, and offer to look at it in the write-up.
- **Sales or recruiting pitch from an attendee:** one warning, then remove from the stage.
- **Hostile or harassing behaviour:** apply the code of conduct and the moderation playbook. The host removes first and explains later.
- **Product complaint, civil:** acknowledge, log it in the feedback record with the attendee's words, say who decides and when they will hear back.

## 5. Promotion rhythm

Kubernetes posted about a week ahead, bumped about an hour before, and posted "going live in about 10 minutes".

- Pin the intake thread the moment the previous session's write-up is published.
- Announce the next rotation engineer by name and area. Users come for a person who knows their problem.
- Link the write-up of the last session in every announcement. It is the proof the session is worth attending.
