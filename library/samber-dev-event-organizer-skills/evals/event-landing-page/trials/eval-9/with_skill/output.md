# Alloyfront Conf 2026: landing page plan

I read the skill and its three references and applied them. I didn't run the 11-question interview because you asked for the deliverable directly, so the open items sit in section 1.

**Short answer:** don't build the wall of headshots and embedded talks. Last year's evidence stays, but as a labelled, consent-cleared "last edition" section, not inside the Speakers and Schedule slots. Also build a forwardable manager block, which is the easiest win here.

## 1. Assumptions and open questions

⏳ Doors are in 22 days (14 Oct to 5 Nov), so the dates below drive everything.

| # | Assumption I made | Confirm |
|---|---|---|
| Q1 | Marketing-plan dates exist (CFP closed, on-sale, speaker reveal, agenda release). I have none of them. | Send me the dates. |
| Q2 | Ticketed. The manager request implies it. | Yes or no? |
| Q5 | Ticket ladder arrives from `event-ticket-pricing`. I invent no rung or price. | Send the ladder. |
| Q6 | Accessibility target is WCAG 2.2 AA, the skill's stated default. `event-accessibility-inclusion` owns the actual decision. | Confirm. |
| Q9 | The site persists across editions (fourth edition). | Confirm. |
| Q10 | One marketing volunteer with a few hours and no way to edit by date. This is the binding constraint. | How many hours, and who can edit? |
| Q11 | See section 4. This is the real blocker. | See below. |

⚠️ A program that isn't announced 22 days out is the biggest risk on this page. Find out whether "not announced" means undecided or confirmed-but-embargoed.

## 2. Page shape

- **Rung:** front door plus practical annexes (Location, Code of Conduct, Accessibility as their own URLs). This is the skill's default.
- **Delete the Speakers and Schedule pages.** With one volunteer and no date-based editing, a ten-page site with empty pages is worse than one honest page.
- **Promotion:** build Program and Speakers pages only when the program is real, as part of the speaker-reveal or agenda-release moment.
- **Editions list:** this is a recurring event, so the hero carries a list of past editions linking to each year's archive. It is a legitimate archive trace and costs nothing in consent.

## 3. Hero and positioning

- Show the event name, 5–6 November 2026, Munich, the venue with a map-linked address, and the price from the ladder.
- Carry the agreed line verbatim, with no rewrite: "The embedded systems conference where the hardware is in the room. There are many slideware events. This is not one of them."
- The marketing volunteer's idea fights this line. A wall of talk recordings is the slideware the line disclaims. The photos that prove the promise are hardware on benches, boards in hands and demo tables. That also happens to solve most of the consent problem.

## 4. Sections that don't exist yet

| Section | Posture | Why |
|---|---|---|
| **Speakers** | **Omit.** Promote to "Named with a date" only if you have a reveal date you will hit. | Last year's headshots under "Speakers" say these people speak this year. That is borrowed social proof and a false claim. |
| **Schedule** | **Named with a date** if one exists, otherwise omit. | The visitor's real question is "when can I book a flight?" The reveal date answers it. Never write "coming soon" with no date. |
| **Last edition (2025)** | **Substitute with the archive**, but only with cleared material (below). | The archive exists, so the marginal effort is low. It answers "what is this event like". Label it with the year and keep it out of the Speakers and Schedule slots. |
| **Sponsors** | **Omit** until this year's sponsors have signed. | Last year's logos presented as current is the "Trusted by" failure. If you reuse them, label "2025 sponsors" and confirm reuse permission. |
| **Manager block** | **Build now.** | See section 6. |

### Consent gates for the archive (the compliance cost the skill flags)

**Photos (600 total, about 15% opt-outs)**

- A crowd shot of 10 people has roughly an 80% chance of containing at least one opt-out (1 − 0.85¹⁰, assuming independence). Browsing 600 photos by eye will leak.
- Did the badge checkbox get recorded per person? If not, you cannot honor opt-outs for identifiable faces. Use only photos with no identifiable people: hardware, boards, bench close-ups, stage from behind.
- Identifiable people are allowed only if they are staff, volunteers, or speakers with a release, or attendees you have checked against the opt-out list.
- You need about 12–20 photos, not 600. My estimate for the cull is roughly 2 hours for one person.
- Check the photographer's contract for web-use rights too.
- Add a takedown contact next to the gallery.
- ℹ️ The opt-out policy and wording belong to `event-accessibility-inclusion`. Hand the Q11 gap to it.

**Speaker headshots**

- The attendee badge opt-out says nothing about speakers. Their consent comes from the speaker agreement.
- A plain-text name list is lower risk if last year's program already published those names. Headshots need the agreement to cover them.

**Talk recordings**

- Embed none until the agreement is read. That is about 30 minutes, since there is likely one template. Then email the few speakers you want to feature for an explicit OK.
- If the agreement is silent, treat republishing as not granted. A recording republished without consent cannot be un-published.
- Link out to your channel's playlist rather than embedding.
- Embeds also need captions (WCAG 2.2) and, in the EU, third-party-cookie consent before load. Use a click-to-load facade.
- If you do feature talks, pick hands-on demos, not slide talks.

Not legal advice. If the agreement is ambiguous or you operate under German image rights, have someone qualified read it.

## 5. CTA and transition table

Rung: **single date-gated primary.** At most one primary button is on screen at a time.

| From date | Phase | Primary CTA | Sections added | Owner |
|---|---|---|---|---|
| Today | [Registration status?] | Register if on sale, otherwise Notify me, or Contact | Hero, dates, positioning, CoC, manager block, cleared archive | [name] |
| CFP window | **No Propose button.** Remove the CFP section rather than leave "closed". | none | none | [name] |
| [speaker reveal date] | Program building | Register | + Speakers | [name] |
| [agenda release date] | Program live | Register | + Schedule | [name] |
| [early-bird close] | Final push | Register | Rung update from `event-ticket-pricing` | [name] |
| 5 Nov | Live | Practical info | + on-the-day details | [name] |
| After 6 Nov | Archived | Contact | + status line on hero | [name] |

- **Mechanism:** manual, since a volunteer can't use date-gated rendering. Copy each row into the marketing-plan calendar as a dated task with a named owner and a reminder the day before.
- **Notify-me capture:** it is the only rung that collects personal data. It needs a consent basis, a privacy notice and a deletion path before it ships. If you can't do that in time, use Contact only.

## 6. Manager-forward block (the "convince my manager" ask)

Give it its own anchor, for example `/for-your-manager`. Write it from the positioning, not fresh copy. Fill the brackets with true facts only.

> **Alloyfront Conf: for whoever approves the trip**
> The embedded systems conference where the hardware is in the room. There are many slideware events. This is not one of them.
> **When:** 5–6 November 2026. **Where:** [venue], Munich. **Cost:** [rungs from the ladder]. [Invoice option: yes/no, as per the ladder].
> **Why it's worth two days:** [2–3 true lines, for example hands-on time with real hardware that a slide deck can't give]. Program announced on [date].

## 7. Structured data

```json
{
  "@context": "https://schema.org",
  "@type": "ExhibitionEvent",
  "name": "Alloyfront Conf 2026",
  "description": "[one line matching the hero]",
  "startDate": "2026-11-05",
  "endDate": "2026-11-06",
  "url": "[canonical URL]",
  "image": "[cleared hero image URL]",
  "location": {
    "@type": "Place",
    "name": "[venue]",
    "address": "[street, Munich]"
  }
}
```

Never let it carry a date the visible page contradicts.

## 8. Accessibility

- Take the target from `event-accessibility-inclusion`.
- Build in this order: structure, contrast, a real keyboard-reachable button, labelled forms, alt text on every kept photo, and 200% zoom.
- This is a digital-layer check only. It says nothing about on-site provision.

## 9. Pre-launch gate

All four must pass or the page doesn't go live. I can't run them yet because I have no built page.

1. ⬜ Every CTA transition has a date and an owner, and each one has fired.
2. ⬜ A stranger can answer what, who, when, where and what it costs in one phone screen.
3. ⬜ The structured data validates with the real dates and URL.
4. ⬜ Registration completes by keyboard alone on the real ticketing platform.

## 10. Handoffs

- **Post-click path** (confirmation and reminders): `event-attendee-email-sequences`.
- **Tracked per-channel links**: back to `event-marketing-plan`.
- **Opt-out wording and the Q11 gap**: `event-accessibility-inclusion`.
- **Sponsor logo placement**: `event-sponsor-fulfillment`, once contracts exist.

## 11. What to tell your volunteer

"Good instinct, wrong slot. We'll show last year as proof, labelled 2025, with photos of hardware and people we've cleared. Speakers and Schedule stay off the page until they're real. Your first job is to find out whether we recorded who ticked the opt-out box, and to read the speaker agreement."

**Next action:** send me the marketing-plan dates, the ladder, and the answers to the Q2/Q10/Q11 questions. I'll turn this into a filled transition table and final copy.