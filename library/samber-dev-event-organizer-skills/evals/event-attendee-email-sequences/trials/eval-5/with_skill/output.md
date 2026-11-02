# NorthStack Night, Nov 5: attendee email plan

⚠️ **Nothing is scheduled or sent.** Every draft below needs your review first. Details marked `[ ]` are on-site facts I don't have, and I haven't invented them.

## Your three questions

| Question | Answer |
|---|---|
| Daily reminder for the final week? | **No.** Send 2 reminders, not 7. |
| How many extra registrations over 350? | **I can't give you a number.** It belongs to a different skill (see below). |
| Keep emailing the 2,800 until they register? | **No.** Send them no registration pushes. |

### 1. Seven daily reminders is the countdown chain

The skill deletes this pattern outright, not just trims it. Organizers who run these events send 2 to 4 emails across the whole pre-event arc. Seven sends in a week exceeds every sourced cap. Each one also trains people to ignore the one email that matters, which is the one carrying the check-in time and address.

Send these two instead:
- **Thu Oct 29:** the know-before-you-go email.
- **Wed Nov 4, evening:** a short day-before nudge.

Then send a thank-you on Nov 6 to 8. That is 3 sends in the remaining window.

The drop-off figure supports this. A 30 to 50% signup-to-attendance drop on free events is what makes these two reminders worth sending. It doesn't justify adding more of them.

### 2. Overbooking ratio: routed, not answered

Overbooking ratios, waitlists and seat release belong to `samber/dev-event-organizer-skills@event-no-show-management`. This skill answers "how do we stop no-shows" with the reminder emails and hands the structural fix to that one.

⚠️ That boundary was written from this side only. The no-show skill has not agreed the handoff from its side. Treat it as a pointer, not an agreed process.

One fact to carry into that conversation: you are **already at 500 registered against a 350-seat venue**. Your question is therefore about whether to cap or waitlist, and how, not about accepting more.

Your own 40% figure, applied to 500, is a data point to bring to that conversation. I'm not turning it into a ratio here.

### 3. The 2,800-person community list

- **"Email them until they register" is deleted.** The skill caps registration follow-ups at 1 or at most 2, and only to people who haven't registered.
- **The promotion condition for follow-ups is a registration curve that is behind.** You are over capacity, so the condition fails. Pushing registrations now adds to the problem you're worried about.
- **Consent decides who may get even one follow-up.**
  - Promotional mail needs its own recorded opt-in per address. You said the list is opted in, and I can't verify its provenance.
  - Check which form, which edition and which box each address came from.
  - A ticket purchase or a past-event list is not marketing consent.
- **Registered people must be excluded.** Cross-reference against the 500 so nobody is asked to register twice.

If you want to say anything to the unregistered, make it one informational note. For example, "registration is full, here is the waitlist or the next date". That depends on what the no-show skill decides, so hold it until then.

## Assumptions

I couldn't run the interview, so I assumed the following. Correct any that are wrong.

- Free, registration required, community-run.
- Doors are on Thursday Nov 5, and it's a one-day event.
- The announcement and confirmations already went out.
- The registration list was collected with consent to receive event information.
- No promotional use of that list beyond this event.
- You send the emails yourself, and you can filter a list per send.

## Send map

| Date | Send | Segment | Job |
|---|---|---|---|
| Thu Oct 29 | Know-before-you-go | 500 registered, attendee variant | Everything needed to arrive prepared |
| Wed Nov 4, evening | Day-before nudge | 500 registered | When and where, nothing new |
| Fri Nov 6 to Sun Nov 8 | Thank-you | All registered, including no-shows | Thanks, recordings, feedback link |
| None | Registration follow-up | 2,800 community list | Not sent, over capacity |

Cap check per segment: registered attendees get 3 more sends. Unregistered community members get 0 from this arc.

## Draft emails

I wrote these in plain organizer voice and checked them against the skill's humanizer checklist by hand. I didn't run a separate humanizer skill, so run your preferred one before sending.

### 1. Know-before-you-go (Thu Oct 29)

**Subject:** NorthStack Night, Nov 5: what to know before you come
**Preview:** Doors at [time], check-in at [entrance]. Full details inside.

> NorthStack Night is **Thursday, 5 November**. Doors open at **[time]**, talks start at **[time]**, and we finish around **[time]**.
>
> If you can't make it, please tell us. We have more registrations than seats, and someone is waiting for yours. [Mechanism: link or reply address. Hold this line until the no-show skill confirms how releasing a seat works.]
>
> **Code of conduct.** [Link]. Anyone who breaks it can be asked to leave, at our discretion. Report anything to [contact]. [If a separate tool will email you about this, name it and its timing here.]
>
> **Getting in.**
> 1. Go to [entrance], [floor].
> 2. Have [what to show: name, ticket] ready.
> 3. Wear your badge all evening.
>
> [Bag or coat-check rules, or "none apply".]
>
> **Where.** [Venue name, full address in text]. [Map link].
>
> **Getting there.** [Transit lines and stops, parking, or "not applicable"].
>
> **Accessibility.** [What the venue provides, for example step-free route and seating]. If you need something arranged, tell us by **[date]** at [contact].
>
> **Food and drink.** [What's provided, how dietary needs were handled, or "no food provided"].
>
> **Schedule.** [Link].
>
> **On the day.** WiFi: [details]. Parents' or quiet room: [location, or "none this year"]. Hashtag: [tag]. Organizers wear [colour]. During the event, reach us at [contact route].
>
> Thanks to [sponsors], who make this free. [Sponsor link]
>
> See you there,
> [Name], for the NorthStack Night team

Completeness check: every section has a placeholder or an explicit "not applicable". Fill the `[ ]` items from your event-attendee-experience source. Don't guess any of them.

### 2. Day-before nudge (Wed Nov 4, evening)

**Subject:** NorthStack Night is tomorrow, doors at [time]
**Preview:** Check-in at [entrance], [address].

> NorthStack Night starts tomorrow. Check-in opens at **[time]** at **[entrance, full address]**. Bring [what to have ready].
>
> Everything else, including the schedule, food and accessibility, is in [last week's email].
>
> [Name]

### 3. Thank-you (Fri Nov 6 to Sun Nov 8)

**Subject:** NorthStack Night: thanks, and what's next
**Preview:** Recordings, slides and a two-minute survey.

> Thank you to everyone who came, and to those who freed up their seat for someone else.
>
> Recordings and slides are [here / will be posted by DATE]. If you couldn't make it, they're yours too.
>
> We'd like to know how it went: [survey link]. [Survey is written by the event-feedback skill, not here.]
>
> [Next edition date, only if it's actually fixed.]
>
> [Name]

## Open items

1. **Overbooking and waitlist:** run `event-no-show-management` with the 500 registered, 350 capacity and about 40% historic no-show figures. Decide before Oct 29, because the seat-release line in email 1 depends on it.
2. **Community list provenance:** per-address source and opt-in box for the 2,800. Needed before any send to them.
3. **On-site facts:** every `[ ]` above comes from `event-attendee-experience`.
4. **Humanizer pass:** run on all three drafts, then I'd suggest tracking two signals this edition. Count desk questions the email already answered, and compare day-of arrival timing against your check-in window.