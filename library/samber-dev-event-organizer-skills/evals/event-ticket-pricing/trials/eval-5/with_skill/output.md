# Sablefish Summit: ticket structure and a way in for the three people between jobs

I read the skill and all three references. The skill wants a one-question-at-a-time interview, and you asked for the full deliverable, so I made assumptions instead. Each assumption is marked, and the open questions are at the end. Every number is labelled **sourced** (published by a real event) or **self-set** (your call).

## Do this week (about 2 hours)

1. Reply to the three people who emailed. Use the template in section 4. Answer them first: they have already disclosed hardship, and silence now would contradict your "accessible" claim.
2. Create `access@<your domain>` and a one-page application form (fields in section 4).
3. Add the access route to the tickets page (copy in section 4). The page names the route but shows no code and no discount price.
4. Answer the four decisions in section 6 before any ticket sells.

## 1. Target and capacity (provisional)

The skill says to stop if no budget exists. I can't see yours, so treat the ladder below as provisional until this arithmetic is done:

- Ticket revenue target = total expenses − sponsorship share (**self-set**; the community-conference target is 75–80%+ from sponsorship, **sourced**, devopsdays).
- Paid seats = 260 − committed comps. Count sponsor allotments, speakers, organizers and volunteers from the agreements you hold. No percentage rule exists for this.
- Scholarship seats also come off the 260. I propose a cap of 10 (about 4% of capacity, **self-set**). The most they can cost you is 10 × £145 = **£1,450** of forgone revenue at the individual price.
- Posture: **community price**. £145 is well above a nominal fee, so tickets carry a real share of the budget. This assumes sponsorship carries the bulk.

## 2. The public ladder

| Rung | Price | Ratio |
| --- | --- | --- |
| Company | £310 | company : individual = 2.14 : 1 |
| Individual | £145 | individual : student = 3.22 : 1 |
| Student | £45 | company : student = 6.89 : 1 |

- The published range is 1.7:1 to 6.5:1 (**sourced**: EuroPython 2026 and PyCon US 2026). Your top-to-floor ratio of 6.9:1 sits just above it.
- That is fine for a community event if the student rung is deliberate. Check the £310 top rung against what an employer in your market approves without a purchase order. I have no comparable pages with dates, so I couldn't do that check.
- Keep the public price points to two per persona at most.
- **Date gate:** publish one dated step from day one, and make it a late surcharge on the regular price. EuroPython's step was 1.5x (**sourced**). Your size is **self-set**. I recommend keeping the student price flat. Never announce an increase buyers couldn't have seen coming.

## 3. The access rungs

You have two rungs, and they sit side by side:

- **Student £45.** This is a published price, self-service, with no application.
- **Need-gated "access place".** This is for the unemployed, career-changers and anyone in hardship who isn't a student. A fixed student price doesn't reach them.

The skill ranks the need-gated route as the highest-effort option, and promotes it when review can be staffed or accessibility is a stated claim. Your website makes that claim, so the route is promoted. The route is not a free lunch. It costs organizer labour, and I would not call it free.

**What keeps it off Reddit:**

- The route is public, and the price and the codes are not. Anyone can read "email us if you can't afford a ticket". There is no code to screenshot.
- Never list it as a cheap public tier. The skill names this as a failure mode: it turns a reviewed decision into a checkbox and attracts the buyers it wasn't meant for.
- Issue one unique, single-use code per approved person, tied to their email. This is my inference, not a sourced practice. The sources show codes by email, but not single-use codes. A posted code is then useless to anyone else.
- State on the application page that access places are non-transferable. The checklist says to say this up front.

**Mechanic (the shape of devopsdays Austin and Halifax, **sourced**, sized for two people):**

- **Reviewers:** both organizers.
- **Promise:** a reply within 5 working days (**self-set**, realistic for evenings).
- **Window:** open until [date, a few weeks before the refund deadline], then closed.
- **Eligibility:** framed on need ("financial hardship, including between jobs"), not on identity. Don't copy an identity list from another jurisdiction. This is not legal advice.
- **Evidence:** self-attestation, no proof required. That keeps review to about 10 minutes per application.
- **Decision rule:** approve everyone who qualifies until the cap is reached. If applications exceed the cap, treat it as a budget question for next edition. Don't stop answering.
- **Reward:** a complimentary pass.
  - Alternative: a flat low price, as devopsdays Amsterdam did with €20–50 (**sourced**).
  - A free seat carries the no-show risk of any seat nobody paid for. Route that risk to `event-no-show-management`; pricing doesn't fix it.
- **Funding the seats:** ask one sponsor to underwrite access places. That is set in `event-sponsor-pricing`.
  - Skip the "supporter ticket" rung. It is the highest-effort bulk mechanic for small cash, and two evening organizers shouldn't run it.

## 4. Copy to paste

**Tickets page line:**
> Can't afford a ticket? We hold [10] access places for people in financial hardship, including between jobs. Email access@… or use this short form by [date]. We reply within 5 working days. Access places are personal and non-transferable.

**Form fields:**
- Name
- Email
- A short sentence on your situation (no documents needed)
- Confirmation that you will attend or release the seat by [date]

**Reply to the three:**
> Thanks for writing, and for being open about it. We have a place for you. Here is your personal code: [unique code]. It works once, for you only. Please tell us by [date] if your plans change so we can give the seat to someone else.

If three codes go out now, the cap has 7 places left.

## 5. Bulk mechanics

- **Group discount:** 15% off for 5 or more tickets in the same order (**sourced**, devopsdays Halifax). Apply it to the regular tier only, never to a late tier. Without the "same order" wording, it becomes a code that circulates.
- **Invoice rail:** offer invoicing on request at full price, only if you have an entity that can issue invoices and reconcile payments. It is not a discount. If you can't invoice, delete this rung. The £310 company tier probably needs it, so check.

## 6. Refund and transfer policy (decide before the first sale)

There is no industry norm here. The four sourced policies only share one thing: a single dated cutoff. My proposed answers are **self-set**:

1. **Deadline:** one calendar date, aligned to your catering headcount.
2. **Fee:** none, or a small flat fee that is lower for students (PyCon's student fee was half the standard fee, **sourced**).
3. **Hardship:** waive the fee, or extend the deadline for health, visa or travel reasons.
4. **Late requests:** no refund. Say whether you offer a free transfer instead (KubeCon does, **sourced**).
5. **Transfers:**
   - Within a company: always allowed.
   - Person to person: allowed until the cutoff.
   - If the two ticket prices differ, the buyer pays the difference. This stops a company ticket being resold as an individual one.
6. **Access places:** non-transferable and non-refundable. If someone can't attend, they release the seat.
7. **If you cancel the event:** a different question, and it touches contracts. See `event-risk-management`. This is not legal advice.
8. **Where to publish:** beside the prices on the registration page, not in a confirmation email.

## 7. The claim on your website

"The most accessible data conference in the north" is a superlative, and the ticket structure is only one part of it. A claim like that has to survive someone checking it. Either list what you actually do or soften the wording. For costs beyond the ticket (travel, childcare, step-free access), see `event-accessibility-inclusion`.

## 8. What to track (set the thresholds before sale)

- **Paid share of the revenue target at the gate date.** If you're behind, split it into demand, marketing or price using `event-market-fit` before touching a price.
- **Applications received against places granted.**
- **Persona mix against plan.**
- **Refund requests against the deadline.**

## Open questions that would change this

1. **Budget:** what is the expense total, and what share is sponsorship? Without it, section 1 is a template.
2. **Comps:** how many seats are already committed?
3. **Payer mix:** how much of your audience is employer-funded?
4. **Dates:** what are the sale open date, the gate date and the refund cutoff?
5. **Invoicing:** can you issue invoices?
6. **Comparables:** which other events' ticket pages do you have, with dates?

I haven't written anything to disk or sent any email.