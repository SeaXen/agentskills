# FenConf email plan: send map, cadence and copy

**Next action:** answer the six open facts at the bottom, then approve the map. Nothing is scheduled. I couldn't run the skill's one-question-at-a-time interview, so every unanswered item is an assumption, and each one is marked.

I designed this from `event-attendee-email-sequences`. It rejects the nurture sequence you proposed, so I explain that first and then give the replacement.

## 1. Why I'm not building the 8-10 touch branching nurture

Your instinct is right for a product. It doesn't fit a dated event.

- **The send moments are dates, not behaviours.** The arc is fixed and ends on one day, so every send fires on a calendar date, never on an open or a click. The skill deletes the behaviourally-branched drip outright.
- **Open data is unreliable for branching.** Since 2021, mail clients pre-load images and register an "open" with no human reading. A branch on "quiet" would misclassify a large share of the list.
- **"Gone cold" would send more mail to people already ignoring you.** On a 1,200-address list, that turns a soft registration curve into a burned list. A soft curve is a problem for the marketing plan to solve, not a reason for another send.
- **The sourced norm is about 2 to 4 reminder sends.** That is what organizers who run these events actually send. An 8-10 touch drip is roughly triple that.
- **Your tooling isn't the constraint.** You have lifecycle tooling, so the skill's "volunteers lack automation" argument doesn't apply to you. The three reasons above still hold.

**What replaces it:** a thin, dated arc, split only by registration state (registered vs not yet). Behavioural segments and a re-engagement branch are deleted. There is no win-back either, because this is the first edition and there is no prior-year list.

## 2. Inputs I'm taking as given

| Input | Value |
|---|---|
| Event | FenConf, Lyon, 18-19 June |
| Announcement (registration opens) | 2 April |
| Agenda live | 6 May |
| Doors | 18 June |
| Ticketing | Paid |
| List | About 1,200 addresses |
| Pole | Vendor-run. Every adjustment below assumes that. |

⚠️ **Year assumption.** You gave no year and today is October 2026, so I assumed 2027. That makes 2 April a Friday, 6 May a Thursday, and 18-19 June a Friday and Saturday. Confirm, because every weekday below depends on it.

## 3. Dated send map

| # | Send | Date | Segment | One job |
|---|---|---|---|---|
| 1 | Announcement | Fri 2 Apr | Whole list that passes the consent check | FenConf exists, here are the dates, here is the page |
| 2 | Registration confirmation | On purchase (transactional) | The individual registrant | Registration worked, a practical email arrives about a week before |
| 3 | Agenda release | Thu 6 May | Not-yet-registered (registrants may get it as information) | Concrete reasons for the undecided |
| 4 | Last call | Day before the early-bird or tier cutoff (**date TBD**) | Not-yet-registered only | One dated fact |
| 5 | Know-before-you-go | Fri 11 Jun | Registered attendees, attendee variant | Everything needed to arrive prepared |
| 6 | Day-before nudge | Thu 17 Jun, evening | Registered attendees | When and where |
| 7 | Post-event thank-you | Mon 21 Jun | Everyone who registered, no-shows included | Thanks, recordings, feedback link |

**Last call (send 4) exists only if a real cutoff exists.** `event-ticket-pricing` owns that date, and I wasn't given one. If there is no cutoff, delete send 4. Never invent a deadline.

**Held slot.** Non-registrants may get at most two follow-ups beyond the announcement. The agenda release uses one. The last call uses the second, or, if there is no cutoff, that slot stays in reserve. Spend the reserve only if registrations are behind the checkpoint on the plan's spine around Fri 28 May. It is a plain "register by X" note, sent once, to non-registrants. After that, nothing more.

## 4. Cap check, per segment

| Segment | Sends | Count |
|---|---|---|
| Not yet registered | 1, 3, then 4 or the held slot | 3 |
| Registered | 2, 5, 6, 7 (plus 1 and 3 only if they arrived before registering) | 4 |

No segment goes over the sourced caps. Anyone who registers drops out of the promotional sends immediately. Cross-reference the registered list before every send, so nobody who has paid gets "register now".

**Gap to expect.** There are five quiet weeks between 2 Apr and 6 May. That is correct. Do not fill the gap with nurture touches.

## 5. Consent check (do this before send 1)

⚠️ **Your 1,200 addresses are almost certainly product-lifecycle contacts.** That list was collected for the product. Under the skill's rule, an event announcement is promotional, and promotional mail needs its own recorded opt-in. This is the one failure here that can't be undone.

Per address source, answer:

- Did the sign-up form include a box that covers event or marketing mail?
- What does the privacy policy and the jurisdiction (EU, since the event is in Lyon) require for this use?
- Can you suppress anyone who unsubscribed from marketing in the product?

Addresses without a documented opt-in don't get send 1. Get legal or compliance sign-off first. Ticket buyers are different: sends 2, 5, 6 and 7 are transactional because they cover the event they bought. Keep promotional content out of them, or the transactional exemption stops applying.

Every promotional send needs a working unsubscribe that is honoured immediately.

## 6. Copy

I wrote these to the skill's craft rules. I did not run a humanizer skill, and the skill requires that pass, so run one before anything sends. Square brackets are facts I wasn't given. Do not guess them.

### Send 1: Announcement (Fri 2 Apr)

> **Subject:** FenConf: Lyon, 18-19 June, tickets open
> **Preview:** Our first developer conference. Dates, venue and tickets inside.
>
> FenConf, Fenlock Systems' first developer conference, takes place in Lyon on 18-19 June.
>
> It's for [one line: who it's for, e.g. engineers who run X]. Tickets are on sale today. The agenda follows on 6 May.
>
> [See dates and get a ticket]
>
> - [Name], Fenlock Systems
> [unsubscribe link]

**Optional forwardable paragraph.** Put it inside the same email, not as a second send:

> If you need approval to attend: FenConf runs 18-19 June in Lyon. Ticket price is [price]. You get [two concrete things, e.g. two days of talks on X, a workshop on Y]. Travel and hotel are extra.

### Send 2: Registration confirmation (on purchase)

> **Subject:** You're registered for FenConf, Lyon, 18-19 June
> **Preview:** Your ticket reference is inside, plus what arrives next.
>
> You're in. Ticket: [type], reference [ref], for FenConf on 18-19 June in Lyon.
>
> About a week before, you'll get one practical email: where to check in, times, food, how to get there. It's not marketing.
>
> If you need accessibility support or have dietary requirements, tell us by [date, at least two weeks before doors] at [address]. Some of it needs lead time.
>
> - [Name]

No promotional block in this email.

### Send 3: Agenda release (Thu 6 May)

> **Subject:** FenConf agenda is live: [one named talk], [track]
> **Preview:** [Speaker] on [topic], plus [workshop]. Full program inside.
>
> The FenConf program is published. Three things now confirmed:
>
> - [Speaker], on [specific topic]
> - [Track or workshop, with a specific detail]
> - [Third specific item]
>
> [See the full agenda]
>
> - [Name]
> [unsubscribe link]

### Send 4: Last call (day before the cutoff, only if a real cutoff exists)

> **Subject:** FenConf early-bird pricing ends [weekday, date]
> **Preview:** Standard pricing starts [date]. Nothing else changes.
>
> Early-bird tickets for FenConf close on [weekday, date] at [time, timezone]. After that, standard pricing applies.
>
> Same program, same venue, same dates: 18-19 June in Lyon.
>
> [Get a ticket]
>
> - [Name]
> [unsubscribe link]

If you want to add a seats-taken figure, use it only if it's true at send time.

### Send 5: Know-before-you-go (Fri 11 Jun)

I can't fill this one. The skill requires every on-site fact to come from `event-attendee-experience`, and I didn't receive any. The structure is below. Fill each slot from that source, or mark it "not applicable" explicitly.

> **Subject:** FenConf, 18-19 June: what to know before you arrive
> **Preview:** Doors [time], check-in at [location]. Everything for the two days.
>
> FenConf runs **18-19 June** at [venue name, full address]. Doors open **[time]** each day for registration, [breakfast], and sponsor tables.
>
> **Code of conduct.** [link]. [Enforcement consequence, per `event-code-of-conduct`.] Report to [contact].
> *(If a separate automated tool will email attendees, name it and its timing here.)*
>
> **Accessibility.** [Provisions, what to request, by when, who to ask.]
>
> **Check-in.** [Numbered walk: entrance, floor, route, what to have ready, badge rule.] [Bag or coat-check restrictions, or "none".]
>
> **Schedule.** [Link]. [How workshops or participatory formats work.]
>
> **Food and dietary.** [Meal schedule, how dietary needs were collected, or "food is not provided".]
>
> **Getting there.** [Transit lines and stations. Airport routes and times, if people fly in. Parking, or "not applicable".]
>
> **Health and safety.** [Policy, or "none this year".]
>
> **Evening events.** [Endorsed gatherings with RSVP links, or "none".]
>
> **Nursing or parents' room.** [Details, or state that there isn't one.]
>
> **WiFi, hashtag, handles.** [One line each.]
>
> **Contact on the day.** Organizers wear [colour]. Reach us at [address or number usable during the event].
>
> Thanks to our sponsors: [link].
>
> - [Name]

Completeness gate: all 14 sections must be present or explicitly marked not applicable. A partial pass is a fail.

### Send 6: Day-before nudge (Thu 17 Jun, evening)

> **Subject:** FenConf tomorrow: doors at [time]
> **Preview:** Check-in is at [location]. See you there.
>
> FenConf starts tomorrow. Check-in opens at **[time]** at **[address, entrance]**. Bring [what's needed for badge pickup].
>
> Everything else (schedule, food, transit, accessibility) is in [last week's email].
>
> - [Name]

Nothing new may appear here for the first time.

### Send 7: Post-event thank-you (Mon 21 Jun)

> **Subject:** Thanks for coming to FenConf (recordings and feedback inside)
> **Preview:** Slides and recordings are [here / coming on date].
>
> Thank you for spending two days at FenConf in Lyon. If you couldn't make it, you're getting this too, and the material is yours.
>
> Recordings and slides: [link, or "published by [date]"].
>
> Two minutes of feedback helps us plan the next one: [survey link].
>
> - [Name]

`event-feedback` owns the survey itself. Add a "save the date" only if the next edition's date is actually fixed.

## 7. No-shows and measurement

- **No-shows.** The reminder emails are the lever this skill owns. Paid tickets will drop off far less than the 30-50% a free event sees. The structural fixes (overbooking, waitlists, deposits) belong to `event-no-show-management`. The skill notes that boundary has only been agreed from this side, not from that sibling's.
- **No open-rate target.** The only event-specific benchmark is 21-30% open and 2.1-3% click. It is old and blends promotional and logistics sends. Use it as a sanity floor, never as pass/fail.
- **Two binary gates:** know-before-you-go completeness, and per-segment cap compliance.
- **Pick two self-set signals now and record them before the event.** Options are desk questions the emails already answered, late accessibility or dietary requests, unsubscribes per send, and arrival timing against the stated window. For each, write down what it would change next edition.

## 8. Facts still needed

1. **Year.** I assumed 2027.
2. **Consent provenance** of the 1,200 addresses, per source (see section 5).
3. **Any dated early-bird or tier cutoff**, and the registration checkpoint dates on the plan's spine.
4. **On-site facts** from `event-attendee-experience`: check-in, badges, food, accessibility, quiet or nursing room.
5. **Who else emails about FenConf** (speakers, sponsors, volunteers) and who owns those sends. I write the attendee variant only.
6. **Who writes and sends, how many hours they have, and whether they can filter per send.** Registration-state suppression is the one filter this plan needs.

Once you confirm these, I'll fill the placeholders and finalize the map before anything gets scheduled.