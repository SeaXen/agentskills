# LatchConf: what to publish Monday

I read the skill and its three references. I couldn't ask the interview questions one at a time, so I list my assumptions at the end. Nothing was built or run.

## Verdict on your co-organizer's draft

Publish roughly a third of it. Six items go.

| Draft item | Call | Why |
|---|---|---|
| "The future of platform engineering starts here" | ❌ Replace | It's a generic aspiration and exactly the thought-leadership tone your positioning rejects. The agreed sentence goes in verbatim. |
| Speakers: coming soon! | ❌ Remove | A dateless placeholder advertises an absence and answers nothing. |
| Schedule: coming soon! | ❌ Remove | Same reason. |
| Testimonial from "a happy attendee" | ❌ Remove | It's a first edition, so the quote can only be fabricated. |
| "Trusted By" greyed-out logos | ❌ Remove | Your sponsors are still in talks, so this is borrowed proof. Publish a logo only after signature and written permission. |
| Stock photos of a packed keynote room | ❌ Remove | They show a room that isn't yours and cut against "not the people on stage". Use a typographic hero instead. |

Do not add a "Tickets", "Pricing" or "Register" section, and no price or rung. The ladder doesn't exist until July, so its absence is correct.

## Page shape and why

**Front door plus practical annexes.** That means:
- one home page;
- Code of Conduct, Accessibility, and Location as their own addressable pages.

Third parties and employers link to those three, and an anchor on a scrolling page can't be cited.

Do not build Program or Speakers pages yet. They have no content, and the reveal is a dated moment that will need somewhere to land later.

**Fallback.** If one volunteer has only a few hours and can't edit by date, collapse to one page and use the manual CTA checklist below.

## Home page, in order

**1. Hero.** It answers what, who, when, where and cost in one phone screen.

> **LatchConf**
> Leeds, UK · 24–25 September YYYY · 250 people
>
> **A platform engineering conference for the people on call, not the people on stage.**
> There are many thought-leadership events. This is not one of them.
>
> Tickets go on sale in July. Prices are announced then.
>
> **[ Get notified ]** · or email [contact address]

Rules for the hero:
- The positioning is verbatim, as the sibling skill requires.
- There is exactly one primary action.
- No Register, Propose, Sponsor or Newsletter row.
- "Prices announced in July" is a true statement and not an invented number.

**2. Who it's for and what it is.** Two or three lines, taken from the positioning rather than composed fresh. I only have the sentence, not the full audience definition, so write this from `event-positioning`'s output.

**3. Who's organising it, and why.** Names, the on-call-first reason this conference exists, and any real organiser track record. For a first edition this is the honest replacement for social proof. I can't write it, because I don't know your people or history.

**4. Key dates (named with a date).** This answers "when will I know enough to book".

| Date | What happens |
|---|---|
| Today (Monday) | Announced |
| **12 May** | Call for talks opens |
| *[CFP close date]* | Call closes |
| **30 June** | Talk selections complete |
| July, *[exact day]* | Tickets on sale |
| 24–25 Sept | LatchConf, Leeds |

List only dates you will hit. Leave a row out until you can fill it.

**5. For your manager.** This is a short, linkable block to forward to whoever approves travel. It covers:
- what the event is;
- the dates and the city;
- the cost ("announced in July");
- two or three lines on why it's worth the time away, written from the positioning.

**6. Notify-me capture (email field).** Put a privacy line right beside it. It needs a consent basis, a privacy notice, and a deletion path before it ships, because it's the only element on the page that collects personal data.

**7. Footer practical cluster.**
- Code of Conduct, Accessibility, Location and Contact, as one block.
- A plain line such as "Interested in sponsoring? Email [address]." Sponsorship is a conversation, not a button.
- If the Code of Conduct doesn't exist yet, it blocks launch.

**Omitted until real:** Speakers, Schedule, Sponsors, Testimonials, Trusted by, Tickets and Pricing, and an archive. This is a first edition, so there's nothing to substitute.

## CTA transition table (single date-gated primary)

The CFP window (opens 12 May, closes before 30 June) and the on-sale window (July) don't overlap. One primary button is enough.

| From | Phase | Primary | Sections added or removed | Owner |
|---|---|---|---|---|
| Monday | Announced | Get notified | Everything above | *[name]* |
| 12 May | CFP open | **Propose a talk** (links out to the CFP page, which `event-cfp-design` owns) | Add CFP block; Notify-me becomes secondary | *[name]* |
| *CFP close* | CFP closed | Get notified | **Remove** the CFP block entirely. A "submissions closed" notice is a placeholder in disguise. | *[name]* |
| July on-sale | On sale | **Register** (links out to ticketing) | Add the ladder and refund policy exactly as `event-ticket-pricing` sets them | *[name]* |
| Speaker reveal | Program building | Register | Add Speakers | *[name]* |
| Agenda release | Program live | Register | Add Program and schedule banner | *[name]* |
| 24 Sept | Live | Practical info | Add on-the-day details | *[name]* |
| After 25 Sept | Archived | Contact | Add status line, recordings and photos | *[name]* |

**Mechanism.** If the site can't render by date, use the manual fallback:
1. Copy each date into the campaign calendar as a dated task.
2. Name one owner per transition.
3. Write each target state as a checklist item.
4. Set the reminder one day before.

The 12 May switch is the first test of this mechanism.

## The risk the page can't fix

Travel budgets close at end of June. Selections finish on 30 June and tickets open in July. Your visitors may therefore be unable to book before the program or price exists.

The page can only host the answer. The decision belongs upstream:
- **`event-ticket-pricing`:** can it publish an indicative price range before the end of June, so people can request budget?
- **`event-marketing-plan`:** can anything land before end of June, such as a confirmed theme or a first confirmed speaker? Two things carry this risk: how early the first speakers are announced, and how well the manager-forward block works as an approval document.

If either says yes, add it to the Key dates table as a dated line. Don't invent a number to fill the gap.

## Structured data

Put this on the front door. Fill the year. It will fail validation until you do, which is what the gate wants.

```json
{
  "@context": "https://schema.org",
  "@type": "Event",
  "name": "LatchConf",
  "description": "A platform engineering conference for the people on call, not the people on stage. 250 attendees, Leeds.",
  "startDate": "YYYY-09-24",
  "endDate": "YYYY-09-25",
  "eventStatus": "https://schema.org/EventScheduled",
  "eventAttendanceMode": "https://schema.org/OfflineEventAttendanceMode",
  "url": "https://[your-domain]/",
  "image": "https://[your-domain]/og-image.png",
  "location": {
    "@type": "Place",
    "name": "Leeds (venue to be announced)",
    "address": { "@type": "PostalAddress", "addressLocality": "Leeds", "addressCountry": "GB" }
  },
  "organizer": { "@type": "Organization", "name": "[organiser]", "url": "https://[your-domain]/" }
}
```

Rules for the block:
- Omit `offers` until the ladder exists.
- Add the venue name and street address once it is confirmed.
- The `image` must be a real asset, not a stock crowd.
- Update it whenever a date moves.

## Accessibility

- **Target.** I'm assuming WCAG 2.2 AA from `event-accessibility-inclusion`. Confirm it and its scope.
- **Build order:** structure first, contrast at palette time, a real button for the CTA, labelled form fields (the notify-me field must not rely on its placeholder), alt text, and a check at 200% zoom and on narrow screens.
- **Scope.** This covers the website only. It is not accessibility coverage for the event itself, which that sibling owns.

## Pre-launch gate (all four must pass, or the page stays down)

1. **Every CTA transition has a date, an owner, and a reminder.**
   - Status: ⚠️ not yet passing.
   - Owners are blank.
   - The CFP close date, the on-sale day, the speaker reveal and the agenda date are unconfirmed.
2. **What, who, when, where and cost are readable on a phone in one screen.**
   - Status: ⚠️ test it.
   - Hand the phone to someone who has never heard of LatchConf.
3. **The JSON-LD validates with real dates, location and URL.**
   - Status: ⚠️ blocked until the year is filled.
   - A script can check this.
4. **The form flow completes by keyboard alone.**
   - Status: ⚠️ test it.
   - On Monday that means the notify-me form.
   - The CFP form must pass the same test before 12 May.

None of the four has been run, so I can't say any passes.

## Hand-offs

- **`event-attendee-email-sequences`:**
  - the notify-me confirmation;
  - the 12 May "call is open" email to the list.
- **`event-marketing-plan`:** tracked per-channel links for Monday's announcement.
- **`event-cfp-design`:** the CFP page, its form, and the real close date.

## Assumptions and decisions needed

- I assumed a priced event, a first edition, and no archive.
- I don't know the venue, the year, the ladder, or who builds and edits the site.
- I haven't seen your accessibility target, your positioning beyond that one sentence, or your Code of Conduct.
- I don't know whether you collect email at all. The capture needs a privacy notice, so decide that before Monday.
- Section order and hero length follow observed practice, not a standard.
- I quote no conversion rate, because none exists for event pages.

**Your next steps, in order:**
1. Confirm the year and the CFP close date.
2. Name the transition owners.
3. Confirm the Code of Conduct exists.
4. Write the "who's organising and why" block.
5. Raise the end-of-June budget gap with pricing and marketing.