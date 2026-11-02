# What to build for Duneport DevOps Day

**Next action:** tell your co-organizer the answer is a 4-page site, not a 10-page one, and that Sponsors is not one of the four. The reasoning follows.

I read the skill and its three references, then ran the interview from what you gave me. Anything marked *(mine)* is my own estimate or construction, not a published standard.

## Inputs I used, and gaps

| Input | Value |
|---|---|
| Edition | First, one day, 150 people, Cardiff, small ticket price |
| Date | June 6. ⚠️ June 6, 2027 is a **Sunday**, and today is 2026-10-14. Confirm the year. |
| Builder | You alone, about 3 hours for the whole campaign, hosted page builder edited by hand |
| Date-based changes | None happen automatically, so every change is a manual edit |
| Archive | None. First edition. |

Four things arrive from sibling skills. I did not decide them, and the page must carry them unchanged:
- **Campaign dates.** Announcement, CFP open and close, speaker reveal, agenda release, on-sale and early-bird close come from `event-marketing-plan`.
- **Positioning and contrast sentence.** The "There are many [archetype] events. This is not one of them." line comes from `event-positioning`, and I carry it verbatim.
- **Ticket ladder.** Rungs, gates, dates and refund policy come from `event-ticket-pricing`. I invent no rung and no scarcity line.
- **Accessibility target.** `event-accessibility-inclusion` sets the target and scope. I assume WCAG 2.2 AA until you confirm.

If any of these don't exist yet, route to that sibling before building. The CTA table below needs real dates.

## Decision 1: page shape

The skill says that when one volunteer has a handful of hours and can't make the page change on a date, the two upper rungs are **deleted outright**, not parked. That removes "front door plus the program set" and "full multi-page site". The shape is **front door plus practical annexes**.

**Build 4 pages:**
1. **Front door.**
2. **Location.**
3. **Code of Conduct.** This covers your "diversity and conduct".
4. **Accessibility.** Its content is owned by `event-accessibility-inclusion`.

Location, conduct and accessibility get their own addresses because third parties cite them and attendees forward them to employers. A fragment on a scrolling page can't be linked that way.

**Do not build:** Program, Speakers, Sponsors, Registration, Propose, Contact. They fall into three groups:
- **Registration and Propose** are buttons linking to your ticketing tool and CFP tool, not pages. Don't design the CFP form (`event-cfp-design` owns it).
- **Contact** is an email link in the header and footer.
- **Program and Speakers** don't exist yet. A page per empty section is the "ten-page site with four empty pages" the skill warns against.

**When to revisit:**
- The program becomes real (talks accepted, speakers confirmed). Then add Program and Speakers, because the reveal is a dated campaign moment and needs somewhere to land.
- A contract grants a sponsor logo placement. Then add a Sponsors page.
- You decide the site will persist across editions. That is the only reason to pre-build the full structure.

## Decision 2: the Sponsors page

**Not now.** I'm departing from your co-organizer's request here, so the reasoning matters:
- **What it would show.** With zero sponsors signed, the page is empty slots or "coming soon". The skill rates "coming soon" the worst reveal option and calls greyed-out logo placeholders borrowed social proof.
- **Who it would reach.** A sponsor decides from a prospectus and a conversation, not from a public page. The skill's own negative example says "sponsorship is a conversation rather than a button".
- **Cost to you.** It spends part of your 3 hours on the lowest-value page.

**Do this instead:**
- Put one line in the footer and on the Location page: "Interested in sponsoring? Email [address]."
- Send sponsor prospects a direct one-pager or PDF in your outreach, not a webpage. The prospectus is outside this skill. Keep it to the facts the page already states: date, city, 150 people, the audience from the positioning statement, and the organizers.
- When the first sponsor contract grants logo placement, build the Sponsors page then. By that point it is a fulfilment item owned by `event-sponsor-fulfillment`.

**Line for your co-organizer:** "A sponsor page with no sponsors tells prospects nobody has signed. The first signed logo is what makes that page worth building. Until then, outreach goes by email with a prospectus."

## Decision 3: CTA posture

**Default: single date-gated primary button.** At most one primary button shows at a time. Contact is always present. There is **no persistent multi-CTA row** (Register, Propose, Sponsor and Newsletter all showing at once), because half those buttons would be dead on any given day.

**Promote to a dual row (Propose and Register together) if either holds:**
- The CFP and registration windows overlap for more than a couple of weeks.
- The CFP is running short of submissions.

For a first edition, the second condition is likely. If it applies, check with `event-cfp-design`.

**Notify-me capture: include it.** The owned mailing list is the top channel in the marketing plan, and the pre-launch stretch has nothing else to click. It is the only rung that collects personal data, so before shipping it needs:
- A stated reason for collecting the email address.
- A privacy line on the form.
- A way to delete a subscriber.

Hosted builders usually offer a form block. If you can't add those three things, cut the capture and leave Contact only.

## Decision 4: reveal posture, per section

| Section | Posture | Why |
|---|---|---|
| Hero, dates, location, positioning, CoC, contact | Live from announcement | Answers what/who/when/where/cost |
| Ticket ladder, refund policy | Omit until on-sale | Appears exactly as `event-ticket-pricing` sets it |
| Propose | Show only while CFP open | Remove at close; don't leave "closed" |
| Speakers | Omit until reveal date | Never publish 3 of 20 |
| Program | Omit; **named with a date** only if the date is firm | Use the date from the talk-selection schedule, and only if you'll hit it |
| Sponsors | Omit (see Decision 2) | |
| Past-edition archive | **Deleted.** First edition, nothing to substitute. | No stock photos of generic crowds |
| Testimonials, "trusted by" logos | Never | Can only be fabricated |

Use "named with a date" for Program only if travel or budget approval is a real blocker for visitors.

## The front door

**Hero.** The visitor should answer what, who, when, where and cost in about five seconds on a phone, without scrolling. That five-second target is borrowed from landing-page practice, not measured on events. Contents:
- Event name.
- Date and city.
- Venue name and map-linked address (or "venue to be announced").
- The positioning promise and the contrast sentence, verbatim.
- The price, as set by `event-ticket-pricing`.
- One primary button from the table below.

Leave out the "other editions in this city" field. A first edition has none, and the absence is correct.

**Below the hero:**
1. Who is organizing it and why. For a first edition this is the honest social proof, in place of borrowed atmosphere.
2. **Manager-forward block** *(mine)*. A short, linkable block an attendee forwards to whoever approves their travel budget. It covers what the event is, date, city, cost, and two or three lines on why it's worth a day away, written from the positioning statement. Include it because the ticket is paid for by an employer for many attendees.
3. Link to the Code of Conduct and Accessibility pages. Put the practical cluster (Location, CoC, Accessibility, Contact) in the footer as one block.
4. A short FAQ on procedural worries only: what happens if I can't attend after buying, what the refund policy is, what the CoC process is. Skip "what is this event".

## CTA transition table (manual, one owner)

Your builder can't evaluate dates, so enforcement moves from the renderer to you with a calendar. This is the skill's manual fallback, and it suits a one-person site. Fill in the real dates from `event-marketing-plan`.

| Date | Phase | Primary CTA | Edit to make | Owner |
|---|---|---|---|---|
| Now | Announced | Notify me (or Contact) | Publish hero, dates, positioning, CoC, Location, Accessibility, structured data | You |
| `cfp_date_start` | CFP open | **Propose** (link out) | Swap button; add speaker-benefits lines | You |
| `cfp_date_end` | CFP closed | Notify me (or Contact) | **Remove** the Propose button and CFP section. No "closed" notice. | You |
| Registration opens | On sale | **Register** (link out) | Add ladder and refund policy exactly as given | You |
| Speaker reveal | Program building | Register | Add Speakers page | You |
| Agenda release | Program live | Register | Add Program page | You |
| Early-bird close | Final push | Register | Update ladder as `event-ticket-pricing` directs | You |
| June 6 | Live | Practical info | Add on-the-day details | You |
| After | Archived | Contact | Add a status line on the hero: "This edition has ended." | You |

Mechanics, from the skill's manual fallback:
1. Copy each row into the campaign calendar as a dated task, not a note.
2. Write each row's edit as a checklist item so you don't re-derive it.
3. Set the reminder **one day before** the date. A CFP that closes at midnight needs the button gone that morning.

If the CFP window overlaps registration, both buttons show during the overlap (the dual row).

## Structured data

Add this JSON-LD block to the front door. It uses the generic `Event` type and the source uses `ExhibitionEvent`. Either is fine, since the requirement is the fields, not the subtype. Every `[...]` is a placeholder for you to fill.

```json
{
  "@context": "https://schema.org",
  "@type": "Event",
  "name": "Duneport DevOps Day",
  "description": "[one-line description from the positioning statement]",
  "startDate": "[YYYY-06-06]",
  "endDate": "[YYYY-06-06]",
  "url": "[canonical front-door URL]",
  "image": "[absolute URL of the hero image]",
  "location": {
    "@type": "Place",
    "name": "[venue name]",
    "address": "[street, Cardiff, postcode, GB]"
  }
}
```

Rules:
- The block must never carry a date the visible page contradicts.
- Update it whenever a date moves.
- If your builder can't inject custom head code, check that before committing to it, because gate check 3 depends on it.

## Accessibility

I implement the target; I do not set it. A passing page audit is not accessibility coverage for the event. Physical, sensory and dietary provision belongs to `event-accessibility-inclusion`.

Build order, as far as a hosted template allows:
1. Real headings in order, one `h1`, landmark regions.
2. Contrast 4.5:1 for normal text and 3:1 for large text and UI components, decided when you pick the palette.
3. The primary button is a real link or button with visible focus and a label like "Register for Duneport DevOps Day", never "Click here".
4. Forms: visible labels, not placeholder-only, with errors described in words.
5. Alt text on informative images. Check hero text contrast against the busiest part of the photo.
6. Page stays usable at 200% zoom and on a narrow screen. Date ranges and addresses are long strings.

The key test is the **registration flow completed with the keyboard alone**, on the real ticketing platform. If it fails and you can't change it:
1. Raise it with the platform.
2. Publish an email route to register, with a named person.
3. Tell `event-accessibility-inclusion`.

## Time budget *(mine, rough estimates)*

| Task | Hours |
|---|---|
| Front door (hero, organizers, manager block, FAQ, footer cluster) | 1.0 |
| Location, CoC, Accessibility pages | 0.5 |
| JSON-LD, accessibility pass, keyboard test | 0.5 |
| About 6 manual transitions at roughly 10 minutes each | 1.0 |
| **Total** | **3.0** |

That is the whole 3 hours, which is why Program, Speakers and Sponsors pages are not in it. Adding any of them means dropping something else, or asking the team for more hours.

## Pre-launch gate

The skill sets **no numeric conversion target**. Published conversion rates describe SaaS and paid funnels, not event pages. These four binary checks replace one, and **all four must pass before the page goes live**:

1. **Every CTA transition has a date and an owner, and each one fires.** Walk the table against the calendar.
2. **What, who, when, where and cost are answerable on one phone screen.** Hand it to someone who has never seen the event.
3. **Structured data validates** and carries the real dates, location and URL. A script can check this.
4. **The registration flow completes with the keyboard alone**, including payment.

## Handoffs

- **To `event-attendee-email-sequences`:** what happens after someone clicks Register, starting with the confirmation. I don't write those emails.
- **To `event-marketing-plan`:** per-channel tracked links. You create them, and it reads them. Also the transition dates for the calendar.
- **To `event-cfp-design`:** the CFP page, form and timeline. The site links out to it.
- **To `event-accessibility-inclusion`:** the Accessibility page content, and any keyboard-test failure on the ticketing platform.

## Open questions for you

1. What are the CFP open and close dates, and the registration window? These fill the table and decide single versus dual CTA.
2. Is the year 2027?
3. What are the positioning statement and contrast sentence, word for word?
4. Which builder is it? I need to know whether it supports custom head code for JSON-LD and a consent-capable form block.
5. Is the accessibility target WCAG 2.2 AA?