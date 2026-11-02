# PyForge Day: app rollout plan and announcement routing

## Recommendation

**Don't buy the $4,800 app as quoted.** Run the event on email, a mobile-friendly schedule page, and on-site signage. Spend about a tenth of the money, and keep the app as an optional pilot with the conditions below.

## Why

- **The 80% figure doesn't fit your event.** It's a vendor claim about "comparable events", with no definition of "install" and no named events. Apps do well at multi-day, multi-track, corporate conferences where the schedule shifts and people network in-app. You're one day, two rooms, and a schedule that never changes.
- **Your realistic install rate is much lower.** You have an email list and no existing audience in an app. Attendees would have to download it, on venue wifi, with 500 people competing for it. Plan on 15–30%, which is roughly 75–150 people. That is my estimate, not a measured figure, so test it (see the pilot gate).
- **Push notifications reach fewer people than that.** Only installers who also accept the notification prompt receive them. Email reaches every registrant.
- **Cost per reached attendee is high.** $4,800 over 500 attendees is about $9.60 each. Over 75–150 real installers it is $32–64 each, for a schedule that doesn't change.
- **Their strongest feature solves a problem you don't have.** Push is for schedule changes. A locked schedule means few announcements, and the ones that matter must reach everyone, including people who never installed.

## Recommended rollout (no app)

Dates are relative to event day (T). Fill in real dates once you have them.

| When | Action | Owner |
|---|---|---|
| T-30 | Schedule locked. Publish it as a single mobile-friendly web page: both rooms side by side, times, speaker names, venue map. Add an `.ics` calendar download. | Web volunteer |
| T-30 | Email 1: "Schedule is live", with the page link and calendar file. | Comms |
| T-14 | Email 2: practical info (venue, transport, doors, registration, food, accessibility, code of conduct). | Comms |
| T-7 | Email 3: "What to know before you come", with a pointer to the schedule page. | Comms |
| T-1 | Email 4: final logistics, doors time, check-in QR code, weather and transport note. | Comms |
| T-1 | Print signage: room schedules on each door, a big overall schedule at the entrance, a QR code to the web page. | Ops |
| Day of | MC announces room and session changes at every break. Volunteers wear a "ask me" marker. | MC and volunteers |
| T+2 | Thank-you email with feedback survey and slides or recordings. | Comms |

The schedule page needs no install, works on any phone, and reaches everyone. A static page can be done in an afternoon, so budget about $0–300 for printing.

## Announcement routing

If you do run an app pilot (next section), use this split. Without an app, everything in the "in-app" column goes to email, signage, or the MC.

| Announcement | Channel | Why |
|---|---|---|
| Schedule publication | Email, schedule page | Everyone needs it; it's the core content. |
| Venue, transport, accessibility, code of conduct | Email, schedule page, signage | Must reach everyone, and people re-read it. Never app-only. |
| Ticket and check-in details | Email | Needed before arrival. |
| Cancellation, date or venue change | Email, schedule page, social | Must reach non-installers. |
| Last-minute room or time change (rare) | Email to everyone, plus signage and MC; in-app push as an extra | Push only reaches installers who opted in, so it can't be the only channel. |
| "Session starts in 10 minutes" | In-app only (optional) | Nice to have, and nobody is harmed if it is missed. |
| Lunch and coffee ready, social event starting | In-app push, signage, MC | Low stakes. |
| Sponsor and prize messages | In-app or MC | Low stakes. |
| Weather or transport disruption on the day | Email, signage, MC; push as extra | Safety and logistics matter more than convenience. |
| Feedback survey, slides | Email (T+1 to T+2) | Email gets better response, and the app is often deleted by then. |

**Rule:** anything someone would be harmed by missing goes through email and on-site channels. Push is only an extra.

## If the committee still wants the app (pilot with gates)

1. **Ask EventPulse these questions before signing:**
   - Which events does the 80% come from? Provide three references with attendee counts and format.
   - How do they define "install" (download, first open, or active use)?
   - Is there a cheaper tier or a per-event price for 500 attendees?
   - Is there a web version with no install? If it's a PWA, much of the install problem goes away.
   - Who owns the attendee data, and is it GDPR-compliant? Can you export it and delete it after the event?
   - Is there a refund or reduced fee if installs fall below a stated number?
2. **Set the gate:** announce the app in the T-14 email. If installs are below about 40% of registrants by T-3, stop promoting it and don't rely on it at all. Install counts must come from the vendor dashboard, not from guesses.
3. **Never make it required.** Keep the web schedule, email and signage running in parallel.
4. **Use it for convenience only:** session reminders, the optional in-app agenda, and low-stakes announcements.
5. **Compare after the event:** actual installs, notification opt-ins, and push open rates against the vendor's claim. Record the result, so next year's decision rests on your own data.

## Collect the data you don't have yet

You have emails and nothing else. These cheap steps give you a base to decide on later:
- Add a question to the T-1 email or the check-in form: "How did you plan your day?"
- Count visits to the schedule page by device.
- Add a post-event survey question: "Would you have used a conference app?"

If a majority say yes and you grow past 500, revisit the app next year with real numbers.

## Open questions for the committee

1. What is the event date? The timeline above depends on it.
2. Did the registration form include consent for email updates? For UK attendees (GDPR/PECR), event-logistics emails to registrants are generally fine. Marketing or push messaging needs explicit consent. Please check before sending anything promotional.
3. How good is the venue wifi and mobile signal? That affects both the web page and the app.
4. Does the budget need to be spent, or can the saved $4,800 go to something attendees will notice, such as speakers' travel, food or accessibility?