# NorthStack Night, Nov 5: capacity math, reminder plan and emails

## Short answers

1. **You don't need to accept extra registrations.** At 500 registered and a 40% no-show rate, you expect about 300 attendees for 350 seats. You already have 150 more registrants than seats.
2. **Daily reminders in the final week are the wrong plan.** They can lift the show rate enough to erase your buffer, and they cost you unsubscribes. Send 4 emails and make one of them a confirm-or-release.
3. **Don't email the 2,800 until they register.** Send them one message at most, framed around a waitlist or the next event. You're nowhere near under-filled.

## 1. Capacity math

Treat each registrant as an independent coin flip with a 60% chance of showing (the number below is the share of registrants who show, not a margin of error).

| Registered | Expected attendees | Std dev | P(over 350) |
|---|---|---|---|
| 500 (today) | 300 | ±11 | about 0% |
| 530 | 318 | ±11 | about 0.2% |
| 540 | 324 | ±11 | about 1% |
| 560 | 336 | ±12 | about 11% |
| 583 | 350 | ±12 | about 50% |

Your pure break-even is 350 / 0.6 ≈ 583 registrants, but that is a coin flip on overflow. The independence assumption also hides three risks:

- **Reminders change the rate.** Your 40% history was measured under your old communication pattern. Good reminders typically cut no-shows noticeably. At a 70% show rate, 500 registrants already means 350 attendees. If you tighten the reminders and also over-accept, you stack the risks.
- **Show-ups are correlated.** Good weather, a headline speaker, or a free-food announcement moves everyone in the same direction. The real spread is wider than ±11.
- **350 is a safety limit.** If it's a fire or venue limit, going over is not a soft failure.

**Recommendation:**
- Close registration at about 540 and put everyone after that on a waitlist. That is about a 1% chance of overflow under the historical rate.
- Plan for the reminders to lift the show rate, so treat 70% as your pessimistic case. Then 500 registrants is already the full room, and 540 is the hard stop.
- Check your past data before deciding. If you have last year's check-in list, compute the no-show rate by registration date. Early registrants and last-minute registrants usually behave very differently, and that tells you how to weight the 500.

**Day-of fallback for the "too many" case.** Hold a standby line. At the start time plus 15 minutes, release unclaimed seats to it. That turns overflow into a queue.

**Fallback for the "too few" case.** At 300 in a room for 350 you're fine. The room reads as full, and you can't really under-fill from here. If the show rate collapses to 40%, you'd see 200 people, which is still a good event. Waitlist emails and a few extra personal invites to the speakers' networks cover that tail.

## 2. Reminder cadence

Seven emails in seven days is too many for a free event. The first two do the work and the rest mostly generate unsubscribes. Send four:

| When | Email | Purpose |
|---|---|---|
| Thu Oct 29 (T-7) | "You're in: logistics" | Calendar file, venue, schedule, what to bring |
| Mon Nov 2 (T-3) | "Still coming? Confirm or release your seat" | One-click yes / can't-make-it. This is the key email. |
| Wed Nov 4 (T-1), evening | "Tomorrow: arrival details" | Doors time, entrance, transit, who to find |
| Thu Nov 5, 8:00 | Short morning-of text | Only the essentials |

The T-3 email is the one that does most of the work:
- It frees seats for the waitlist before the event.
- It gives you a real headcount (confirmed yes) instead of a guess.
- It tells the "I'll probably skip it" group that the seat matters, because someone is waiting.

## 3. The 2,800-person community list

- Don't email the non-registrants repeatedly "until they do." They opted in for community news, not unlimited nudges, and repeated nagging burns the list you'll want for the next event. It's also a deliverability risk, since complaints and unsubscribes feed spam filters.
- You don't need them. The room is already oversubscribed on paper.
- Send at most one email to non-registrants, for one of two purposes:
  - **Waitlist invitation:** "Registration is full, join the waitlist." This builds a replacement pool for the no-shows and costs the list nothing.
  - **Next event or recording:** tell them how to catch the talks afterwards.
- Check what "opted in" covers. If the opt-in was for general community updates, an event invitation is fine, but each message needs a working unsubscribe link and honest targeting. For anyone in the EU, stay inside the scope they agreed to.
- Suppress current registrants and anyone who already unsubscribed from event mail.

## 4. The emails

Placeholders in [brackets]: fill in the venue, times and speaker details.

### Email 1: T-7, Thu Oct 29

**Subject:** You're in: NorthStack Night, Thursday Nov 5
**Preview:** Venue, schedule, and what to know before you come.

> Hi [first name],
>
> You're registered for NorthStack Night on Thursday, November 5.
>
> **When:** doors [time], talks start [time], wrap by [time]
> **Where:** [venue name, address], [entrance/floor]
> **Getting there:** [transit / parking, one line]
>
> **What's on:** [2-3 line schedule or headline talks]
>
> [Add to calendar]
>
> One thing: space is limited and this edition has a waitlist. If your plans change, please tell us (we'll send a one-click link next week) so someone else can have your seat.
>
> See you there,
> [Name], NorthStack

### Email 2: T-3, Mon Nov 2 (confirm or release)

**Subject:** Still coming Thursday? Keep or release your seat
**Preview:** One click. We have people on the waitlist.

> Hi [first name],
>
> NorthStack Night is in three days and we're at capacity, with a waitlist behind you.
>
> Please tell us which it is:
>
> **[Yes, I'm coming]**   **[I can't make it, release my seat]**
>
> If you can't come, no hard feelings. Releasing your seat lets someone on the waitlist in, and we'll share the talks afterwards. If we don't hear back, we'll hold your seat, but we'll start letting people in from the waitlist on Wednesday evening, and doors close for unclaimed seats 15 minutes after start.
>
> Thanks,
> [Name]

Note the last paragraph: it states the standby policy honestly. Don't promise that unconfirmed seats are safe if you will actually release them.

### Email 3: T-1, Wed Nov 4, evening

**Subject:** Tomorrow: NorthStack Night arrival details
**Preview:** Doors, entrance, and who to find.

> Hi [first name],
>
> Tomorrow evening, then:
>
> - Doors [time], talks start [time]
> - [Venue, entrance, one-line directions]
> - Bring: [ID / registration QR code: the ticket is attached/linked below]
> - Seats unclaimed at [start + 15 min] go to the standby line, so please arrive on time.
>
> [Your registration QR code / link]
>
> See you tomorrow,
> [Name]

### Email 4: Thu Nov 5, 8:00 (morning-of)

**Subject:** Tonight: NorthStack Night
**Preview:** Doors at [time].

> Tonight at [venue], doors [time]. Registration code: [link].
> Can't make it after all? [Release your seat] so someone on standby can come.

### Email 5: waitlist promotion (send as soon as a seat frees up)

**Subject:** A seat opened up: NorthStack Night, Nov 5
**Preview:** You have until [time] to claim it.

> Hi [first name],
>
> A seat opened up for NorthStack Night on Thursday. It's yours if you want it.
>
> **[Claim my seat]** (open until [time], then it goes to the next person)
>
> [Venue and time, one line]

### Email 6: one-time message to the non-registered list

Send this once, about Oct 20-22, only if you want to build the waitlist.

**Subject:** NorthStack Night is full: join the waitlist
**Preview:** Seats open up every year. Here's how to get one.

> Hi [first name],
>
> NorthStack Night on November 5 has filled up. Some registered people can't make it every year, so we're keeping a waitlist and will message you if a seat opens.
>
> **[Join the waitlist]**
>
> Not able to come? We'll share [slides / recordings] afterwards, and we'll tell you first when the next event opens.
>
> [Name], NorthStack
>
> [Unsubscribe from event emails]

### Email 7: after the event (Fri Nov 6), two versions

**For attendees**
**Subject:** Thanks for coming: slides and photos

> Thanks for joining us last night. Slides and photos: [link]. Two minutes of feedback would help us a lot: [link]. Next event: [date or "we'll tell you first"].

**For no-shows**
**Subject:** Sorry we missed you: here's what you missed

> We didn't see you last night, and that's fine. Here are the slides and the recordings: [link]. If you'd like to be first in line for the next event: [link].

## 5. Next steps

1. Pull last year's check-in data and compute no-show rate by registration date (about 30 minutes).
2. Close registration at about 540 and open the waitlist.
3. Build the one-click confirm and release links for Email 2, wired to the registration tool, so a release automatically promotes the next person on the waitlist.
4. Schedule Emails 1 to 4 now. Send Email 6 once, about Oct 20-22.
5. Track how many people confirm or release at T-3. If fewer than about 55% of the room confirms, your 40% no-show assumption is probably still right and you can safely promote a few more from the waitlist.

I made this up without your past data, so every figure in the table depends on the 40% history and the 60% show-up rate being roughly right. If last year's data shows a very different rate, rerun the table with the new number.