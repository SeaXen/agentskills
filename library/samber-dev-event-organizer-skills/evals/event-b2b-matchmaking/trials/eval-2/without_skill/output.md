# TapStack Conf sponsor directory: what it shows and how requests flow

## Fix this first: the data can't go straight in

Declining a request happens after a sponsor has already seen the person's name, title, company and interests. "They can always decline" doesn't cover that disclosure.

Registration data was collected to sell tickets. Showing it to sponsors is a new purpose, so:

- **Under GDPR/UK GDPR, this applies if any attendee is in the EU or UK, wherever the conference is held.** Sponsor visibility needs a separate, specific, opt-in consent, not bundled with ticket purchase. Ticket purchase can't depend on it.
- **Check what your checkout privacy notice said about sponsors.** Even if it mentioned them, an explicit opt-in is the safer base. Have counsel or your DPO confirm, because I'm not giving legal advice.
- **Sponsors become recipients, and likely independent controllers, of whatever they receive.** You need sponsor terms covering use, retention and no resale.

**Recommended model: opt-in directory plus blind matching.**

1. **Opt-in directory.** Attendees choose to be listed and see exactly what sponsors will see.
2. **Blind matching for everyone else.** A sponsor describes who they want to meet, such as role bucket and interest tags. They see only an aggregate count, for example "about 40 attendees match". Their request goes to the matching pool. Attendees who accept reveal themselves; nobody else is exposed.

Blind matching gives sponsors reach without exposing the other attendees. It also removes the bulk-browsing and scraping risk.

## What the directory shows

Treat every field as opt-in, and let each attendee hide any field.

| Show | Notes |
|---|---|
| Name | Full name, or first name plus last initial if the attendee prefers |
| Job title | As entered. Optionally also a seniority bucket (IC, lead, manager, exec) as a filter |
| Company | Attendee can hide it, since it can reveal a competitor relationship |
| Tech interests | Tags from registration, editable |
| "Happy to talk about" | Optional one-line field the attendee writes |
| Availability | Time windows chosen by the attendee |

Never show:

- Email, phone, or any contact detail. Contact is revealed only on acceptance, and only what the attendee picks.
- Ticket type, order data, payment info, dietary or accessibility needs, or anything else from registration.
- LinkedIn or other links, unless the attendee adds them.

**Sponsor-side controls**

- Filters only: interest tag, role bucket, company-size bucket. No free-text name search, because that enables enumeration.
- No export, no bulk download, paginated results, and rate limits.
- Named sponsor reps log in individually, with an audit log.
- Each sponsor gets a request quota, for example 30 total and 10 per day, so quality beats volume.

## Request flow

1. **Sponsor drafts a request.** Use a structured form, not free text:
   - rep name and company
   - one-line reason ("why you")
   - topic
   - 15 or 30 minutes
   - 2–3 proposed slots and a location (booth, meeting area)
   - no links and no attachments
2. **Platform relays it.** The attendee gets an in-app notification and an email through your relay address. The sponsor never sees the attendee's real email at this stage.
3. **Attendee picks one of four responses:**
   - **Accept.** They choose a slot and which contact details to share. Both sides get a calendar invite.
   - **Decline.** No reason is required. The sponsor sees "not available".
   - **Not now.** The request expires quietly.
   - **Block or report this sponsor.** Reports go to your team.
4. **Expiry.** Unanswered requests lapse after 7 days. Send one reminder at most.
5. **Sponsor view.** Statuses are only pending, accepted, or unavailable. Decline and expiry look identical, so sponsors can't pressure anyone.
6. **Global switch.** "Pause all sponsor requests" is available at any time.

**Guardrails**

- Throttle or suspend sponsors whose decline or report rate is high.
- An accepted meeting gives the sponsor that person's lead record. Everyone else is not a lead.
- Badge scanning at booths needs its own consent. Don't merge it into this flow.

**After the event**

- Delete the directory and unaccepted requests within about 30 days.
- Sponsors keep only people who accepted a meeting, and only what those people shared.
- Contractually bar sponsors from adding directory data to marketing lists beyond the meeting follow-up.

## Rollout

1. Email all 800 attendees: "Want sponsors to be able to request a meeting? Preview your profile and opt in."
2. The profile preview shows exactly what sponsors will see, with an edit button.
3. Open sponsor access once the opt-in window closes, and keep the blind-match path running for non-listed attendees.
4. Tell sponsors honestly that the opt-in pool will be a subset of 800. Don't promise a number.

## Build or buy

For 800 people and three sponsors, a custom build is probably more work than it's worth. Event platforms such as Swapcard, Brella and Grip already include opt-in profiles, meeting requests and sponsor quotas. Check what they do with the data and what DPA they offer. A small custom build still makes sense if you want the blind-match model or tight control of the data.

## Questions that would change this

1. Where are your attendees located? Is anyone in the EU or UK?
2. What did the checkout privacy notice say about sharing with sponsors?
3. Do the sponsor agreements already promise meetings or a lead count?
4. Do you prefer to build this yourself or use an event platform?