# Tuulikko sponsor plan: where sponsors come from, and the ZoomInfo export

**Short answer:**
- Don't use the export as a contact list. The skill deletes purchased or scraped lists from the channel menu outright.
- Your real sponsor source is people: speakers, the Rust community, and Rust events nearby that already have sponsors.
- Use the export's description of who you want (DevRel at infrastructure vendors in the Nordics) as your target profile.
- You are about a month past the usual start point, so move this week.

I did not research the web, so I name no scored leads below. The skill requires a source URL and date for every claim, and I won't invent them. The "where to look" lists are hypotheses to check against real sponsor pages.

## Assumptions to confirm

These are my assumptions. Each answer re-ranks parts of the plan.

| # | Assumption | If wrong |
|---|---|---|
| Q1 | Community-run: volunteers, sponsors cover costs, no pipeline promises | A company-run event can promise pipeline and use heavier sequences |
| Q2 | No prospectus, rate card or value proposition yet | Build them first (see "Before you send anything") |
| Q3 | No renewals, so everything is net-new | n/a |
| Q4 | Event in mid-May 2027, about 7 months out | See "Timing" |
| Q5 | Revenue goal unknown | Send me the goal and I'll size the list |
| Q8 | Volunteers with a few hours a week | A dedicated sponsorship lead unlocks the heavier sequence |
| Q9 | Not part of a franchise or series | n/a |

## Timing

- Outreach belongs at roughly T-8 months. For a May event that was mid-September, so you are about 5 weeks late.
- Large companies lock next year's budget in the prior financial year. Expect anchor-tier money at big vendors to be mostly gone.
- Weight the plan toward targets whose budget cycle is still open:
  - startups and midsized companies,
  - hiring-driven buyers,
  - smaller packages.
- Ask every target "when do you plan next year's budget?" in the first call.
- Start this week. The first touches go out before you finalise the program, because outreach is the first external motion.

## Is the export worth using? No, not as a contact list

1. **Policy.** Purchased or scraped lists are "deleted, not demoted." The rule is public business contact channels only, with a source URL and date for each contact. A friend's export has neither a source nor a date.
2. **Compliance.** Cold email to 4,000 named people is the highest-compliance-cost channel. It falls under consent and e-marketing law (GDPR and similar). Names and emails whose collection chain you can't show are exactly what that review looks for. I'm not a lawyer, and the policy above settles it anyway.
3. **Licence.** Vendor exports are usually licensed to one customer. Passing one to a free event is likely outside that licence. That is another reason to leave it closed.
4. **Fit versus channel.** The segment is right, since DevRel at infrastructure vendors fits a Rust systems conference well. The 4,000-person blast is wrong:
   - A sponsorship decision involves one to three people per company.
   - A blast burns a first edition's reputation in a small ecosystem.
   - The follow-up cap is 3 pings and "just checking in" bumps are banned.
   - Your sending domain is also the one you need for attendee mail.

**What to do with the friend's offer:**
- Ask him to make personal introductions to people he actually knows in that list. That is a warm intro, the best first-touch channel.
- Ask him for the company names that match your profile, without people's details. Then find the right person yourselves from public pages.
- Decline the file itself.

## Where sponsors come from

This is the skill's menu re-ranked for a first edition with no roster and no useful employers.

**1. Organizer network (low yield, but do it first, one afternoon).**
- "Nobody works at a sponsor-capable employer" doesn't mean no paths. List former colleagues, LinkedIn contacts, customers of the organizers' employers, and speakers' employers.
- Write down every name, even weak ones. Each is a potential warm intro.

**2. Adjacent-event sponsor scan (promote to default).**
- Use the sponsor pages of recent Rust and systems conferences and large Nordic or European developer events. These are public evidence of budget and fit.
- Note which companies sponsor at what tier.
- Note who sponsors regional events, since those are your price range.
- Check that each has hired or is hiring Rust engineers.

**3. Attendee-stack vendor mapping (promoted because the warm lists are empty).**
- Map vendors whose products Rust systems engineers use or evaluate:
  - cloud, databases and storage,
  - observability,
  - embedded and safety-critical tooling,
  - networking,
  - WebAssembly.
- Target their DevRel teams. This is the product-feedback segment, and the export profile points the same way.

**4. Institutional channels, Tampere-specific hypotheses to verify.**
- Tampere universities and career services, for recruiting buyers.
- The city or regional convention bureau, which may offer event support or venue help.
- Large local engineering employers hiring systems engineers. Check whether they use Rust.
- Local startup communities.

**5. Inbound broadcast, always on.**
- Publish a "sponsor Tuulikko" post on your own site and social channels.
- Expect low yield. Never make it the plan.

**6. In-kind sponsors.** Venue, food and coffee help a volunteer-run first edition. Treat them as sponsors with limits on their conduct, not as a footnote.

## First-touch channel per target

Run each rung in order. Move down only when the one above has no path.

1. **Warm intro.** Ask on Rust community channels and in your own networks: "Who knows someone at X?"
2. **Referral ask.** Email someone senior at the target, above the likely decision maker. Ask only "who is the right person to talk to about sponsoring Tuulikko?" Don't pitch in that email.
3. **Cold email, limited.**
   - Use it only for targets with no path above it.
   - Send to a named business contact from a public page, and record the URL and date.
   - Send no links, attachments or images in the first email. Corporate filters auto-trash them.
   - Honour any opt-out immediately.
4. **Inbound broadcast,** running in the background throughout.

**Title targeting:**
- Product feedback: DevRel or Developer Advocate.
- Hiring: recruiting or talent acquisition.
- Brand awareness: marketing.
- Unknown: the CEO of a small company.

## Cadence

Use the sponsor-standard cadence: a gap of 1–2 weeks between pings and at most 3 follow-ups. Tighten to 3–4 days only close to the event. The angle-rotation sequence needs a dedicated lead and a large list, which you don't have.

Tie the final reminder to a real production date, such as a program lock or merchandise print cutoff. Don't invent a deadline.

## Before you send anything

1. **Objection answers.** Write these down first:
   - projected attendance (250),
   - audience composition in aggregate,
   - benefits per level,
   - logistics.
   A sponsor who has to chase these reads the event as badly run. For a first edition the real objection is organizer competence. Counter it with a confirmed date, venue and speakers.
2. **Honest program.**
   - Pitch only activities in the program. A hiring corner or demo space that doesn't exist on the day turns a yes into a lost renewal.
   - Never promise attendee lists or purchasable talk slots.
   - Sponsors buy access to a qualified audience through conversations attendees choose.
3. **Missing documents.**
   - Value proposition: `event-sponsor-value-proposition`
   - Prospectus: `event-sponsor-prospectus`
   - Rate card: `event-sponsor-pricing`
   First touch and the exploratory call run without the deck. The proposal step needs all three.

## Pipeline sizing

The formula works backward from the goal:

- sponsors needed = goal ÷ average package price
- prospects to pitch = sponsors needed ÷ close rate
- list size = prospects to pitch ÷ first-touch-to-call rate
- sourcing target = 2–3× the list size

The close and reply rates are self-set assumptions. Event sponsorship publishes no benchmark of its own, so the commonly quoted 9–15% reply and 20–30% close figures come from B2B SaaS sales. Write yours down as assumptions and replace them with your own observed rates after this edition.

Illustration only, with invented numbers: €24,000 ÷ €3,000 = 8 sponsors. At an assumed 25% close that is 32 prospects. At an assumed 33% call rate that is about 100 targets, sourced from roughly 200–300 names. With warm paths in the mix the list shrinks.

Tell me the real goal and I'll redo the math.

**Scoring.** Score each candidate Hot, Warm, Cold or Skip:
- fit,
- a visible buying signal (sponsored an adjacent event, hiring for Rust, a launch aimed at the stack),
- a reachable decision maker.

Keep a source URL, date and confidence mark per claim. Diversify across startups, midsized companies and enterprises.

## Call and close

1. **Exploratory call, before the prospectus.**
   - Pitch the event briefly, then let the sponsor talk.
   - Ask what they need: hiring, product feedback, brand, or community goodwill.
   - Ask what they spent before and how they measured it.
   - Silently qualify authority, need, urgency and money.
   - Book the next call before hanging up.
   - A need the event can't honestly carry is a polite no.
2. **Proposal.** Send it the same day, with the best-fitting package highlighted, why it fits, and a deadline.
3. **Track.** Use one shared pipeline with stages Identified → Qualified → First touch → Call → Proposal → Committed → Signed → Lost. Name one liaison per sponsor. Log every objection by segment.
4. **On a yes.**
   - Invoice immediately.
   - Confirm amount and payment method in writing.
   - Verify the receiving account works.
   - Hand off to `event-sponsor-agreement`.
   - Do a values check inside the team before finalising the largest tier.

## Draft first touches

Neither draft contains a link or an attachment.

**Referral ask (to someone senior):**

> Subject: Who handles developer-event sponsorship at [Company]?
>
> Hello [Name], we are four volunteers organizing Tuulikko, a Rust systems conference in Tampere in May 2027, with about 250 engineers. I'm not pitching anything here. Who at [Company] is the right person to talk to about sponsoring a developer event like this? A name or a forward would be great. Thank you, [Organizer]

**Cold email (to a DevRel contact):**

> Subject: Meet 250 Rust systems engineers in Tampere this May
>
> Hello [Name], I'm [Organizer], one of four volunteer organizers of Tuulikko, the first Rust systems conference in Tampere, 250 attendees, May 2027. I saw that [specific, sourced thing, such as a Rust hire, release or adjacent sponsorship]. Many of our attendees work on [relevant stack area], and I'd like to hear what your team wants from a developer event before proposing anything. Could we talk for 20 minutes on [specific day and time]? Thank you, [Organizer]

## Next 7 days

1. Write the organizer-network list (about 1 hour).
2. Reply to your friend: decline the file and ask for personal intros and company names only.
3. Draft the objection answers and confirm what the program actually contains.
4. Scan 3–5 adjacent Rust or Nordic event sponsor pages and note tiers (about 2 hours).
5. Build the first scored list of about 30 names with source URL and date.
6. Publish the "sponsor Tuulikko" post.
7. Send the first warm intros and referral asks.

**Open question for you:** what is the revenue goal, and when must it close? A near deadline promotes the warm rungs even more strongly.