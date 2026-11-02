# Meridian Python Days — sponsorship activation plan

## 0. First, a staffing reality check

You're asking two people to: staff a table for the full show, run a 90-minute workshop, deliver a stage pitch, and host a 20-person dinner — on top of everyone's day job. That's not a discount problem, it's an arithmetic problem: a table needs continuous two-person coverage, and the workshop pulls both of you off the floor for its entire slot. Per the skill's own effort rule, a workshop "takes your two best engineers off the floor for its whole slot" — with only two of you, that means **the table goes dark during the workshop.** Plan around that gap rather than pretending it won't happen (see §4).

Nothing here is a reason to cut anything — it's a reason to sequence it deliberately instead of trying to run all four in parallel.

## 1. Primary objective: Adoption, not Pipeline

Ferrite is self-serve, $99/month, card payment. That puts you in the "developer-purchased product" category, where the skill is explicit: *"Success is measurable in-product... Awareness and adoption are the realistic mandates."* Pipeline/CRM framing doesn't fit — there's no sales cycle to feed.

Pick **Adoption** as the one metric this event is judged on: hands-on product use during the event, cohort still active at 30/60/90 days. The stage pitch and table presence generate Awareness as a free byproduct — don't measure that as the goal, just let it happen.

## 2. What your €9,000 actually buys — and your badge-scan question

Table + six passes + a timed pitch between talks is, line for line, the skill's **"Community / volunteer conference"** package model — not a foundation/vendor-conference package. That model's own definition:

> What it never buys: **attendee contact data, badge scanning, purchased talks.**

This is confirmed by both real-world price ladders the skill tracks (PyCon US, DjangoCon): *"Community and foundation events do not sell contact data or main-stage content at any price."* A volunteer-run 1,100-person conference almost certainly has no badge-scanning system to plug into at all — this isn't a negotiating gap, it's a different product category from a vendor-run mega-conference.

**So: stop trying to get data off the table.** Build your own consented capture instead — this is the standard substitute the skill uses whenever scanning doesn't exist:

- An opt-in QR code at the table to a landing page with an **event-specific URL/promo code** (e.g. `ferrite.dev/meridian`, or a coupon like `MERIDIANPY`) — never reuse a code across events, it makes the number unattributable.
- Workshop **signup itself is your cleanest list** — anyone who registers for a 90-minute hands-on session has already opted in and self-selected as a real prospect. Run that signup through your own form, not the organizer's system.
- An opt-in prize draw at the table (framed honestly, not "scan for a t-shirt").

A smaller, real, consented list beats a larger invented one, and it beats what a badge scan would have given you anyway (name/title/company, no context).

## 3. The main-stage ask: don't make it

Direct answer: no, and don't offer to trade tier money for it. The skill treats this as a bright line, not a negotiation:

> "Never buy... an implied speaking slot at an event that runs a CFP. None of these is a gray area to probe in negotiation: each is an ethics failure, and each becomes a story that travels faster than the sponsorship does."

Two reasons this specifically bites here:
1. Community/volunteer events structurally don't sell stage content at any tier — your two-minute pitch *is* the sponsor-content allocation this event sells. Asking for more, even by offering to upgrade, reads as trying to buy what a CFP is supposed to gate.
2. It's the exact "Community backlash" failure mode this skill names: *"trade-show mechanics at a community event"* — at a volunteer-run conference, this is the fastest way to burn the goodwill the sponsorship bought you, and it's the kind of thing that gets tweeted.

The legitimate path to a main-stage slot is the CFP, on the talk's own merits, like any other speaker — treat it as a completely separate track from the sponsorship. If your engineer has a real talk (e.g., "what actually breaks in Postgres CDC at scale"), submit it — ideally for next year, since CFPs for this edition are likely long closed. Don't mention the sponsorship in the submission.

Make your two minutes on stage count instead: script it as a signpost, not a company pitch — *"we're at the table with a live demo, and running a 90-minute hands-on CDC workshop at [time/room], come build something."* That converts stage attention directly into table/workshop traffic instead of spending it on brand awareness alone.

## 4. Activation plan for two people

| Activation | Effort (per skill) | Your move |
|---|---|---|
| **Table** | An hour of prep, then a standing job for hall hours | Both of you staff it help-desk style — technical people who debug a stranger's Postgres/CDC problem live, not pitch-first. Accept it sits **empty during your workshop slot**; put a sign there redirecting to the workshop/pitch rather than trying to cover it with a third person you don't have. |
| **Workshop (90 min)** | Normally a quarter of prep — collapses to about a week if you reuse an existing curriculum | Don't write this from scratch. Adapt an existing Ferrite tutorial/demo into the session. If you don't have one, this is the single biggest prep-time risk on your list — flag it now. |
| **Stage pitch (2 min)** | Already bought, low effort | Script it as a funnel to the table/workshop (see §3), not a company overview. |
| **Dinner (20 people)** | A week of guest-list/venue work, plus "an evening that also costs you the next morning" | Schedule it for the **last night** of the conference, not the night before your workshop or a heavy table day — protects your energy for the parts that actually move the objective. This is not covered by your €9,000 tier; it's a separate cost and a separate guest list you build yourselves. |
| **Scholarship/diversity fund** | Zero staffing cost | Fund it — it's off the value ladder by design (no leads, no conversations), but it's the cheapest goodwill line on this whole plan and needs no one's time. Decide the amount as a deliberate brand/goodwill line item, not an ROI line. |

## 5. Measurement and threshold (set this before you show up)

**Qualification bar** — a conversation counts if the person (a) actually runs Postgres and would plausibly need CDC, (b) can self-serve-decide to try a $99/month tool (usually true for the engineer in front of you — that's the point of self-serve), (c) agrees to a named next step ("will run the trial against their own DB this week," "wants a follow-up next Tuesday").

**Primary metric (Adoption)**: signups from the event cohort (workshop signups + table promo code) still active at 30/60/90 days. Do **not** claim activations from anyone who merely saw the pitch or walked past the table — the skill is explicit that this is the wrong thing to report.

**Threshold** — fill in before you sign anything else: a minimum number of workshop completions + table signups, and a target 30-day activation rate, both derived from Ferrite's actual signup→activation rate, not invented for this event. If you don't have that baseline number handy, pull it before the event — you need it to know afterward whether this was worth repeating.

**Log every conversation**, one row: name · company · role · problem discussed · qualified (y/n) · next step · owner · follow-up sent. Route by type, not all into one bucket: bug reports → engineering, feature/beta feedback → product, anything case-study-worthy → marketing. Log at the end of each shift, not at the end of the trip — you will not remember day-one conversations by day three.

**Follow up within 48 hours**, personal, referencing the actual conversation. No batch sequence — a generic nurture email to someone you talked to for five minutes is the exact failure pattern the skill calls out as producing "a full spreadsheet, zero opportunities."

## 6. Fully loaded cost — fill in the blanks before you commit further spend

| Line | Amount |
|---|---|
| Sponsorship fee | €9,000 (paid) |
| Workshop slot — confirm with organizers this week whether it's sold as an add-on or needs to be arranged informally | ? |
| Dinner venue for 20 | ? |
| Scholarship/diversity fund contribution | your call |
| Travel + accommodation, 2 people | ? |
| Staff time (loaded daily rate × [prep + travel + on-site + follow-up] days × 2 people) | ? — this line is the one teams routinely underestimate; a modest fee with two people traveling and a week of workshop prep can rival or exceed the sponsorship fee itself |

Get the workshop-slot and dinner-venue numbers this week — both sit outside the €9,000 and neither is guaranteed to exist as a bookable line item at a volunteer-run event; you may be arranging both informally with the organizers rather than buying them off a price sheet.

## 7. Confirm with organizers this week

1. Is there a workshop/tutorial track at all, or would your session be something you arrange with them ad hoc (room, time slot, capacity)?
2. Can workshop registrants' opt-in contact info be shared with you as the session host — a narrow, reasonable ask, unlike asking for general badge data?
3. Any restriction on hosting an evening dinner in the conference's name/branding, or is it fully outside their remit (assume the latter)?
4. Confirm the mechanics for the scholarship fund contribution — some organizers want it as a separate line, not folded into the sponsorship invoice.

## 8. After the event

Run the review within two weeks per the skill's step 8, while the conversation log is still accurate, and write the verdict — renew / renegotiate / drop — against the threshold you set in §5, not against "how it felt." Given this is a first edition for you at this event, judge it on awareness-stage expectations and reserve any pipeline-style verdict for a second year, if you do one.