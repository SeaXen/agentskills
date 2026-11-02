# Follow-up plan: Berlin Go meetup sheet and GopherCon EU talk

**Short answer:** don't put the sheet in the newsletter. Do send the talk people a note, but not a blanket demo invite. The 200-seat pricing question gets a reply this week.

I followed the `developer-event-followup` skill. The interview questions are open, so the plan below runs on stated assumptions. The answers to those questions at the end could change it.

## 1. Record inventory

| Source | Count | Grade | Notes |
|---|---|---|---|
| Meetup door sheet (name + email) | unknown | C | The organizer collected it. You didn't. Nothing in it can be personalized. |
| GopherCon EU talk, people who came up after | about 10 | A or B | The pricing asker is A (stated buying need). The others are A or B depending on your notes. |
| Talk attendee list | none | n/a | A talk produces no list. Don't build one from the room. |

Dedupe on email. Check both groups against the CRM first. An existing customer goes to the account owner. An earlier unsubscribe wins over anything these events produced.

## 2. Gate table

| Source | What they heard or read | Jurisdiction | Requested reply allowed? | Marketing allowed? |
|---|---|---|---|---|
| Meetup sheet | "name + email, for the pizza headcount next time" | Germany | nothing was requested | **No.** Berlin means German UWG s.7: prior express consent, business recipients included. The purpose line covers pizza headcount only, so it is narrower than the law needs. |
| Talk conversations | what you said or promised, per person | assumed Germany or EU, unknown per person | yes, for the exact thing they asked for | no, unless the person agreed to a named next step, or you have a consent you can show |

Three consequences for the sheet:

- **The organizer's registration consent doesn't cover you.** At most it covers the organizer sharing data with you, within its own notice. Your messages need your own basis.
- **Sheet verdict: no import.** The notice told attendees nothing about sharing with sponsors. The skill's rule is to return or delete the list and tell the organizer.
- **If anyone emails them anyway,** the newsletter would be a third purpose after pizza and sponsorship. That is unsolicited advertising, and a "confirm your subscription" email to people who never asked is itself advertising under German rules. The risk lands on your sending domain and on your standing with the organizer.

## 3. Routing (A records)

| Person | Destination | Owner | Send by |
|---|---|---|---|
| 200-seat pricing asker | Sales handoff, same thread as the personal note | a named account owner (you pick) | within 2 working days of the talk |
| Anyone with a bug or missing-feature comment | Engineering | triage owner, link the note | with the personal note |
| Anyone who wanted to contribute, speak or host | Community | community lead | with the personal note |
| Others with a problem and a next step | Product path | the staffer who spoke to them | within 2 working days |

If you're already past two working days, send anyway. Say plainly when you met. Don't skip the note.

Only the pricing asker gets a sales handoff, because only they said it in their own words. Company size is not a buying signal.

## 4. Tracks

Ranking line: **personal note > sales handoff (pricing asker only) > public recap > promised-item message.** Nurture and the newsletter are deleted for both sources.

What moved the ranking:

- **Q3, the purpose line.** The sheet's line is narrower than marketing, so nurture is deleted for those records.
- **Q4, Berlin.** Germany is prior-consent, so every marketing track is deleted for records without a consent you can show.
- **Q5, the 200-seat ask.** This promotes the sales handoff, for that one record only.

**Meetup sheet:**
- Don't email anyone from it.
- Publish a **public recap** where the Go community already reads: slides, repo, and a newsletter signup link on that page. Anyone who wants the newsletter signs up themselves, and you get a clean consent.
- Ask the organizer to add a separate, unticked box at the door next time. Suggested wording: "Also send me [company] product news". It must name your company. "Sponsors" or "partners" wording is not valid consent in the EU.
- Thanking the organizer for the pizza-headcount list and returning it is fine.

**Talk people:**
- Send each person a **personal note** from the speaker. It answers what they asked and delivers the promised item: the config, the slides, the answer you owed.
- Don't make the demo invite a blanket email. Under German rules an unsolicited demo invite is advertising, and a "here are the slides" email carrying a demo pitch is the disguise the skill warns about.
- A demo link is fine only for someone who asked for a demo or agreed to one. For them it is the next step they requested.
- For everyone else, put the demo link on the public recap page.

## 5. Message drafts

These are plain-text drafts. Run them through your humanizer skill before sending. Replace anything in angle brackets.

**A. Personal note (talk person, with a promised item)**

```
Subject: <their problem, in their words>

Hi <first name>,

We talked after my talk at GopherCon EU about <problem as they said it> on <their stack>.
As promised: <the item, one link or attached>.
<Next step agreed in the room: "I'll ping you Thursday to see if it ran" or "Here's a 30-minute slot with <name>, who built that part">

<speaker name>
```

**B. Pricing asker (same thread, once the personal note is sent)**

```
Hi <first name>, you asked about pricing for 200 seats after the talk.
I'm adding <account owner>, who handles that, so you don't repeat yourself.
I'll stay on the thread for the technical side.
```

If they want a call, the account owner proposes slots. No cold sequence follows.

**C. Public recap (publish, send nobody the link)**

A post or page with:
- the slides
- the repo
- the recording, if there is one
- answers to the questions people asked most
- one line: "Want occasional updates? Sign up here" (an unchecked form that logs the consent)
- a demo link, where a person has to choose to open it

**D. Message to the organizer**

```
Hi <organizer>, thanks for passing us the door sheet. The notice said the emails were for pizza headcount,
so we won't use them for anything else. We've deleted our copy and would like to return it if you want it back.
For next time, if you'd add an optional box "Also send me <company> product news", we'd be glad to get
a list that people opted into. Thanks again for running the meetup.
```

## 6. Stop rules and suppression

- Each recipient gets at most one message unless they reply or click an opt-in.
- Honour unsubscribes and objections at once and add them to a permanent suppression list. Name the suppression owner before the first send. In the EU the right to object is absolute.
- Load the talk contacts into the CRM as non-marketing contacts. Record the source ("GopherCon EU talk"), the grade, the purpose line as spoken, and the capture date. Don't enroll anyone in a marketing flow without the gate's yes.
- Don't load the meetup sheet at all.
- Stop sending and review the gate if there are two complaints, or if unsubscribe and "who are you" replies run above your last event.

## 7. Measurement sheet

| Field | Value |
|---|---|
| Events | Berlin Go meetup (sponsor), GopherCon EU talk |
| Cohort tag | `evt-gopherconeu-<year>` on signup links and credit codes |
| Activation event | **your answer to Q6** (first successful API call, or similar) |
| Counts by grade | talk: A _, B _; meetup: C _ |
| Messages sent per track | personal _, handoff 1, recap published |
| Replies to A notes | track per owner |
| Activated by day 30 / 60 / 90 | per grade, beside a non-event baseline |
| Complaints, unsubscribes, days to suppression | guardrails, not goals |
| Opportunities sourced / influenced | the 200-seat deal is influenced unless the talk was its first touch |
| Threshold | self-set, from your own last event. No published benchmark exists. |

Read the 30-day numbers into your sponsorship review for the meetup.

## What I need from you

1. **How did the talk people give you details?** Cards, LinkedIn, a QR code, or your own notes? What did the speaker promise each one? Without this I can't grade them or draft a precise note.
2. **Where is each of the ten based?** Germany and the EU default to prior-consent. If some are in France or the UK, the rules differ.
3. **Do you have an activation event and a cohort tag?** If not, the activation path can't be measured and the promised-item message ships instead.
4. **Who owns the 200-seat conversation?**
5. **Did the meetup organizer say anything in writing about sharing the sheet with sponsors?** If they did, the answer to the sheet could change. The notice quoted "for pizza headcount" suggests they didn't.

This frames questions for your privacy owner and is not legal advice. Confirm the current German and EU rules with them before the first send.