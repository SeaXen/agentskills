# HackZurich follow-up plan

I read `developer-event-followup` and both its reference pages. I had no capture details, so every gap below is a stated assumption. Nothing was saved to a memory file.

## Answer for the VP Sales and the recruiter

**Don't have the SDRs call every participant.** There are three reasons.

1. **The "5 minutes" figure doesn't apply.** It comes from studies of inbound web leads (HBR 2011, the InsideSales/MIT 2007 study), co-authored with a lead-response software vendor. No study sampled hackathon contacts. It is also moot, because the event ended days ago.
2. **Most of this list is students.** Sales calls to students and hobbyists come back to DevRel as complaints, and they cost the next sponsorship.
3. **Some participants are under 18.** They get no marketing of any kind without the privacy owner's sign-off.

**The speed that matters:** the people who talked to our mentors get a personal note by end of Tuesday. They will remember the conversation until then. That is the reason to be fast. It has nothing to do with the 5-minute figure.

**The recruiter does not get the list.** Recruiting contact needs its own basis. An opt-in talent page on the public recap gives it one (see track 6). Under-18s are excluded.

## 1. Record inventory

| Source | Count | Grade |
|---|---|---|
| Teams | 61 | n/a |
| Teams that used the payments API | 23 | A if a mentor note shows a named next step, else B |
| Teams that didn't | 38 | C unless a note proves more |
| Participants | unknown (see questions) | C unless noted |
| Mentor notes | unknown | read them first |

- **A grade:** a mentor note shows the problem now, a build in progress, and an agreed next step. Expect few.
- **B grade:** the 23 API teams without such a note. A doubtful record is graded B.
- **Dedupe:** match on email and against the CRM. An existing customer goes to the account owner. An earlier unsubscribe wins over anything from this event.
- **Organizer list:** use it only within what the organizer's notice said about sharing with sponsors. If the list came with no notice, don't import it. Return or delete it and tell the organizer.

## 2. Gate table

| Source | What they heard | Jurisdiction | Requested reply | Marketing |
|---|---|---|---|---|
| Mentor conversations | unknown: paste what mentors said | per participant | yes, for whatever was promised | only what the line covered |
| API sign-up and credit form | unknown: paste the form text | per participant | yes | no, unless the form said "updates" |
| Organizer participant list | unknown: paste the sharing notice | per participant | nothing was requested | no, unless the notice names us |
| Under-18 participants | any | any | winners and credit logistics only, via the route the privacy owner approves | none |

- **Switzerland is not in the reference table**, and participants arrive from the EU, UK and elsewhere. Treat all of them as prior-consent for marketing email until the privacy owner names the rule.
- **Germany and the EU:** consent is required even for business addresses.
- **Capture dates:** record them, because they are the proof of basis later.

## 3. Routing list

| Segment | Destination | Owner | Date |
|---|---|---|---|
| A teams (adult) | Product path, personal note | the mentor who met them | by end of Tuesday |
| Any participant who asked for pricing, procurement or a buyer conversation, in their own words | Sales, via an intro in the same thread | named account owner | after the note |
| Bug or missing feature raised | Engineering | triage owner | with the note linked |
| B and C students | Community | community lead | after the recap goes up |
| Under-18 | Requested reply only | privacy owner decides the route | n/a |
| Existing customer or open deal | Account or deal owner | account or deal owner | before any send |

Sales only gets a record when the buying signal is in the participant's own words. Team count or "used our API" is not a signal.

## 4. Tracks, with the ranking line

**Default order for this cohort:** public showcase → promised-item message → personal note → activation path → community invitation → sales handoff.

**What moved it:**
- **Event type** (hackathon) promoted the activation path. Everyone already started building.
- **Student-heavy cohort** pushed community above sales.
- **No known purpose line** deleted the nurture sequence.
- **Prior-consent default** deleted every marketing track for records without consent we can show.
- **Under-18 participants** get no marketing.

**Deleted tracks:**
- The SDR call program.
- The nurture sequence. It stays deleted unless a capture said "updates", and in Germany unless the participant confirms by double opt-in.

**Per segment:**
- **A:** personal note, then the activation path.
- **B:** promised-item message plus the activation path.
- **C:** public showcase only, plus any item the capture promised.
- **Students:** community invitation, only where the basis covers it.

## 5. Message drafts

Placeholders are in `<angle brackets>`. Fill them from mentor notes.

### Reply to the VP Sales (Slack or email)

> I'd hold the call list. The "respond in 5 minutes" figure comes from inbound web-lead studies, not events, and by now it's moot. Most of these people are students, and some are minors, so cold calls would hurt us at the next hackathon and could create a legal problem. Here's what I'd do instead: mentors write personal notes to the 23 API teams by Tuesday. Anyone who asks for pricing or a buyer conversation goes to your team in the same thread. Everything else goes to a public showcase and the community. I'll send you the 30-day activation numbers.

### Track 1: public showcase post (all 61 teams)

Publish it where the community already reads. Send the link to nobody. Use each team's project only with that team's permission.

> **HackZurich: what 61 teams built in a weekend**
>
> 61 teams, 23 of them building on our payments API. Here are the projects, the winners, and the repos: `<showcase list, with team permission>`.
>
> The questions we heard most at the booth, answered: `<3-5 Q&As>`.
>
> If you started something and want to finish it, here is the step-by-step page and extended sandbox credit: `<activation page link>`.
>
> Looking for a job or internship with us or with other companies? You can opt in to a talent list here, adults only: `<opt-in link>`.

### Track 2: promised-item message (B)

Send it only if the capture promised an item. This is the only email they get from us about it.

> Subject: The `<item>` from HackZurich
>
> Hi `<first name>`,
>
> Here's the `<item>` you asked for at HackZurich: `<link>`.
>
> This is the only email you'll get from me about it.
>
> `<mentor or DevRel name>`

Add an opt-in line only where the gate's marketing column says yes. Otherwise leave the opt-in on the recap page.

### Track 3: personal note (A, from the mentor)

> Subject: `<their problem, in their words>`
>
> Hi `<first name>`,
>
> We talked at HackZurich about `<problem as they said it>` in your `<project name>`. As promised: `<item, one link>`.
>
> `<Next step agreed: "I'll check Thursday to see if the refund flow ran" / "Here's a 30-minute slot with <engineer>, who built that part">.`
>
> If you'd like your project featured in our showcase, tell me and I'll add it.
>
> `<mentor name>`

If the credit wasn't promised at the event, drop it from this note and leave it on the activation page.

### Track 4: activation path (A and B)

> Subject: Finish `<project name>`: credit is ready
>
> Hi `<first name>`,
>
> Your `<project name>` got as far as `<step they reached>`. This page restarts from there, with sandbox credit already on your key: `<link>`.
>
> If something blocked you, reply and tell me what. I read these myself.
>
> `<mentor name>`

### Track 5: community invitation

Send it once, to adults whose basis covers it.

> Subject: `<community>`: where people building payments flows compare notes
>
> Hi `<first name>`, you were building `<topic>` at HackZurich. `<N>` people working on the same kind of thing talk in `<community>`: `<link>`. Next office hours: `<date>`.
>
> `<sender identification + postal address + unsubscribe link>`

### Track 6: recruiter path

Recruiting runs through the opt-in on the showcase page, not through the list. Anyone who ticks the box and is 18 or over joins a separate recruiting list. A participant who replies to a mentor asking about jobs can be introduced to the recruiter in the same thread.

### Sales handoff

Only for a participant whose own words asked for pricing, procurement or a buyer conversation. Send it in the same thread as the personal note.

> Hi `<first name>`, you asked about `<pricing / procurement>` at HackZurich. I'm adding `<account owner>`, who handles that, so you don't have to repeat yourself. I'll stay on the thread for the technical side.

### Day-30 check-in

Send it only to teams whose repo still shows commits.

> Subject: `<project name>`: what's blocking you?
>
> Hi `<first name>`, I saw `<project name>` is still getting commits. What's the part that's slowing you down? Bugs go straight to our engineers.
>
> `<mentor name>`

## 6. Stop rules and suppression

- **Message cap:** B and C records get at most one message unless they reply or click an opt-in.
- **Batch stop:** stop on the second spam complaint. Also stop if unsubscribes or "who are you, remove me" replies run above the last event's rate. This is the skill's own threshold, not a published one. Count every observable negative.
- **CRM:** load records as non-marketing contacts carrying source, grade, purpose line and capture date. Enrolling anyone in a marketing flow needs the gate's yes.
- **Suppression:** `<name>` owns a permanent list. Unsubscribes and objections are honoured at once.
- **Retention:** agree it with the privacy owner. Unanswered scan-only records go after the period they set.
- **Organizer list:** if the notice doesn't cover sharing with sponsors, don't import it.

## 7. Measurement sheet

| Field | Value |
|---|---|
| Event, date closed | HackZurich, `<Sunday date>` |
| Cohort tag | `evt-hackzurich-2026` on API keys, credit codes and activation-page links |
| Activation event | first successful API call from a cohort-tagged key between day 8 and day 30 (**assumption**: the 23 teams already called during the weekend) |
| Counts by grade | A `<n>`, B `<n>`, C `<n>` |
| Messages sent per track | personal `<n>`, promised item `<n>`, showcase published |
| Replies to A notes | `<n>` of `<n>` |
| Activated by day 30 / 60 / 90, per grade | to fill |
| Non-event baseline | same-window organic signups |
| Complaints, unsubscribes, days to suppression | to fill |
| Sourced / influenced opportunities | report both. Hackathons mostly influence |
| Threshold | **self-set:** `<n>` of the 23 teams activated by day 60. Set it from your last hackathon or blended acquisition cost. No published benchmark exists |

Read the 30-day numbers into the sponsorship renew-or-drop review (`developer-event-sponsorship`).

## Schedule

1. **Monday:** pull mentor notes, grade, run the CRM match, fill the gate table with the privacy owner. Gate the A rows first.
2. **By end of Tuesday:** send the A notes and publish the showcase. If you're already past this, send anyway and say plainly when you met.
3. **Within the week:** send the activation path to A and B. Send the community invitation where the basis covers it.
4. **Day 30:** check-in to teams still committing, then read the cohort.

## Questions that change the plan

1. **What did mentors say, and what did the sign-up form say?** Paste the purpose lines and the organizer's sharing notice. Narrower than marketing deletes the invitation track for those records.
2. **How many participants, and which countries?** I can't say how many records are in scope without this.
3. **Does the organizer tell you who is under 18?** If not, ask for it, or the privacy owner picks a rule.
4. **Can you tag the cohort in product data?** If not, drop the activation path and send the promised-item message.
5. **How many hours can mentors give this week?** Under an hour each means they write only the A notes, and DevRel drafts the rest for their review.