# Lintfold Community Day, Ghent: email program

**Event:** Sunday 7 February 2027, Ghent. Free, open doors, no tickets, no registration.

Placeholders like `[venue]` are facts I don't have. Fill them in before anything goes out.

## 1. Decide first: the 4,000-address list

People joined that list for release notes. An event promotion is a different purpose. Under GDPR and Belgian ePrivacy rules, that is a consent risk, and the people on the list are likely EU-based. I'm not a lawyer, so the call is yours. My recommendation:

1. Check the wording on the original signup form.
   - It says "release notes and project news": one short mention of the event is defensible.
   - It says "release notes only": don't promote the event to this list.
2. Don't merge the 4,000 into the event list, and don't import them.
3. Reach them in a lower-risk way instead. Add a 2-line "Community Day" item with a link to the signup page in the next regular release email. Use the same item in the footer of later release emails. Each person then chooses to join the event list.
4. Reach everyone else through the site, GitHub README and Discussions, the community chat, and social posts.

The event list is a separate list, with its own unsubscribe. Unsubscribing from it must not touch release notes, and the reverse.

## 2. Signup form

**Placement:** a `/community-day` page with the form, plus a banner linking to it on the homepage and docs.

**Headline:** "Lintfold Community Day, Ghent: Sunday 7 Feb 2027"

**Subline (put the no-registration point first):**
"Free, and you don't need to sign up to come. Just turn up. Join the list if you'd like the programme, travel tips and a reminder."

**Fields:**
- Email (required).
- "Where are you coming from?" Optional, free text. It helps us write travel advice.
- Consent checkbox, unticked: "Email me about Lintfold Community Day only."

**Under the button (privacy line):**
"We'll send about 5 emails before the event. Your address is used only for this event, is kept separate from the release-notes list, and is deleted within 30 days after 7 Feb unless you tick 'keep me posted about future community days' in any email."

**Mechanics:**
- Use double opt-in.
- Put an unsubscribe link in every email.
- The confirmation page repeats the date and venue and says again that no registration is needed.
- Don't treat signups as headcount. People who sign up are a small, keen subset of those who show up. Use signups only as a rough signal, and plan venue capacity and catering from other data.

## 3. Send schedule

Sends skip the 19 Dec to 2 Jan dead zone. Times are CET, Tuesday mornings (about 10:00), except the last email.

| # | Email | Send date | Time to event |
|---|---|---|---|
| 1 | Announcement | Tue 24 Nov 2026 | 10.5 weeks |
| 2 | Reminder 1: what's planned | Tue 12 Jan 2027 | 3.5 weeks |
| 3 | Reminder 2: last chance to add a talk or topic | Tue 26 Jan | 12 days |
| 4 | Know before you go | Mon 1 Feb | 6 days |
| 5 | Day-before nudge | Sat 6 Feb, 09:00 | 1 day |
| 6 | Thank-you (optional) | Tue 9 Feb | after |

Segment rules:
- Anyone who joins late gets the latest reminder, then the remaining emails.
- Everyone gets email 5, whenever they joined.
- Unsubscribes stop all sends immediately.
- Send email 6 only to people who haven't opted out.

## 4. The emails

### 1. Announcement (24 Nov)

**Subject:** Lintfold Community Day: Ghent, 7 February (free, just turn up)
**Preheader:** No tickets, no registration. Here's the plan.

> Hi,
>
> On **Sunday 7 February 2027** we're hosting a free community day for Lintfold in **Ghent**, at `[venue]`.
>
> There are no tickets and no registration. Doors open at `[time]`. Walk in whenever suits you.
>
> **What it is:** `[2 or 3 lines: talks, hacking tables, office hours with maintainers, whatever is true]`.
>
> **Who it's for:** anyone who uses, contributes to, or is curious about Lintfold. You don't need to be an expert.
>
> You're getting this because you joined the Community Day list. We'll write about five times before the day, and that's it.
>
> See you there,
> `[Name]`, for the Lintfold team
>
> `[Unsubscribe]` · `[Privacy]`

### 2. Reminder 1 (12 Jan)

**Subject:** Lintfold Community Day is 4 weeks away
**Preheader:** Sunday 7 Feb, Ghent. Here's what's planned.

> Happy new year. A reminder that Community Day is **Sunday 7 February, Ghent, `[venue]`**, free, with no registration.
>
> **The schedule so far:**
> - `[time]` Doors open
> - `[time]` `[Session]`
> - `[time]` `[Session]`
> - `[time]` `[Open hacking and maintainer office hours]`
>
> Want to give a short talk or bring a topic? Reply to this email, or `[link]`.
>
> `[Unsubscribe]`

### 3. Reminder 2 (26 Jan)

**Subject:** 12 days to Lintfold Community Day
**Preheader:** Last call for talks and topics.

> Community Day is on **Sunday 7 Feb**. Last call: send us a talk, a question or something you'd like to hack on by `[date]` and we'll fit it in. `[link]`
>
> Coming from outside Ghent? Travel tips arrive next week.
>
> `[Unsubscribe]`

### 4. Know before you go (1 Feb)

**Subject:** Know before you go: Lintfold Community Day, Sunday
**Preheader:** Address, getting there, what to bring.

> **When:** Sunday 7 Feb, doors `[time]`, wrapping up around `[time]`.
> **Where:** `[venue, full address]`, `[map link]`
>
> **Getting there:**
> - Train: `[station, e.g. Gent-Sint-Pieters]`, then `[tram/bus/walk and duration]`.
> - Bike: `[parking]`.
> - Car: `[parking options]`.
>
> **What to bring:** a laptop if you want to hack. Nothing else is required.
> **Food and drink:** `[what's provided or not]`.
> **Accessibility:** `[step-free access, quiet space, etc.]`
> **Language:** `[English]`
> **Code of conduct:** `[link]`. Be kind. `[Contact for concerns]`.
> **Photos/recording:** `[policy]`
> **Can't make it?** No need to tell us. `[Will talks be recorded/shared?]`
>
> `[Unsubscribe]`

### 5. Day-before nudge (Sat 6 Feb, 09:00)

**Subject:** Tomorrow: Lintfold Community Day, Ghent
**Preheader:** Doors open at `[time]`.

> Tomorrow, **Sunday 7 Feb**, doors open at `[time]` at `[venue]` (`[map link]`).
>
> No registration needed. Just come.
>
> Day-of contact: `[phone or chat link]`. Update: `[any last-minute changes]`.
>
> See you tomorrow.
>
> `[Unsubscribe]`

### 6. Thank-you (optional, Tue 9 Feb)

**Subject:** Thanks for a great Community Day
**Preheader:** Photos, slides, what's next.

> Thanks to everyone who came. `[Slides/recordings link]`. `[Short feedback form, 3 questions]`.
>
> Want a note when we run the next one? Click here to stay on the list: `[link]`. Otherwise your address will be deleted within 30 days.

## 5. What to measure

- **Signups per week** against the announcement spike and each reminder. This shows whether the release-email mention and social posts bring signups.
- **Open and click rates.** Treat opens as unreliable, since Apple Mail privacy protection inflates them. Click on the form and the "know before you go" map link is a better signal.
- **Actual attendance.** Count at the door. No registration means no show-rate data, so a one-question tally ("how did you hear about this?") on arrival is the only way to learn which channel worked.

## 6. Questions for you

1. What does the original release-list signup form say? That decides section 1.
2. Do you have the venue, doors time and schedule? Emails 2 to 5 depend on them.
3. Do you prefer the Saturday 09:00 day-before send, or Friday evening so people can plan Sunday travel?