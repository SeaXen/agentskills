# OpenCircuit Fest inclusion fund: recommended structure

**Verdict:** Build the fund, but not as proposed. Four things change:

- Publish it on a dedicated page.
- Pay for costs directly or in advance, so receipts-after-the-event is not the only path.
- Describe it by what it funds and who qualifies, not only as a "diversity program".
- Settle the data handling and the sponsor's role before applications open.

Labels: **[sourced]** comes from the skill's references. **[self-set]** is my recommendation, not an established standard.

## Why the current plan doesn't work

1. **"Quietly add a line to the FAQ … we'll see what we can do" is the rung this skill deletes outright.** It reads: "an unpublished 'email us and we'll see' hardship promise with no budget behind it." **[sourced]**
   - You do have a budget, so the fix is to publish the terms. They are eligibility, amount, what's covered, timeline, who decides, and what happens to the data.
   - A hidden line mostly reaches people who already read FAQs closely. Those who most need money are the least likely to ask unprompted.
   - The page needs to be live before attendees book travel. A page published after people have booked reached nobody it was for. **[sourced]**

2. **Reimbursing flights and hotel after the event, against receipts, has a known access limit.** Anyone who can't front a flight and a hotel can't use it.
   - The skill says to publish that limit on the page. If you can advance funds instead, say what control replaces the receipt. **[sourced]**
   - Better: pay the vendor yourselves. Book the flight and hotel for approved recipients, or advance part of the grant against a signed agreement. Keep receipts-after-the-event only as the fallback for people who can front the cost. **[self-set]**
   - Whichever you pick, state it plainly on the page.

3. **"Diversity program" branding alone reads as optics.** PyCon's financial aid named three goals instead of one **[sourced]**:
   - Fund speakers and notable contributors who couldn't otherwise attend.
   - Support diversity as one goal among several.
   - Support lower-income attendees generally.
   - Do the same. Name the goals, then name the criteria. How the fund is worded and positioned belongs to `event-cultural-identity`. This skill decides whether it exists, its eligibility, and what it covers.

4. **Hardship and diversity disclosures are sensitive data.** If applicants describe hardship, disability, or identity, the channel needs a handling posture first. See "Data posture" below.

## Recommended structure

Menu 4's travel and registration grant is the right rung. You hold the sponsor budget (Q1) and a legal entity able to disburse (Q4, you said you're an incorporated association). Both are the conditions that promote it. **[sourced]**

| Element | Decision | Label |
|---|---|---|
| **Name and framing** | "Inclusion Fund", with the stated goals above. "Diversity program" can sit as one goal, not the whole label. | self-set |
| **Scope** | One application covers travel, hotel and registration. Add childcare only if it is actually provided. PyCon bundled everything so nobody applies twice. | sourced |
| **Ticket cost** | Don't build a second application. If a need-gated ticket route exists, it lives in `event-ticket-pricing`. Link to it and fold the request into one form. | sourced |
| **Payment model** | Preferred: you book or pay vendors directly. Second: partial advance. Fallback: receipts, paid at the event. Name the control that replaces receipts (signed agreement, booking confirmation, ID check at badge pickup). | self-set |
| **Published access limit** | If any recipient has to front costs, say "reimbursement-only grants exclude people who can't front the cost". | sourced |
| **Timeline** | PyCon opened about 7 months out, closed about 11 weeks out, and decided within 2 weeks of close. Adapt this to your date, and publish before the travel-booking window. | sourced pattern, dates self-set |
| **Decision** | One named owner. A small panel decides, and no panel member is the sponsor or has a conflict. Written reasons for each decline. Decline early and offer what does exist. | self-set |
| **Sizing** | 18k covers a number of grants, not a number you can state now. It depends on origin cities and how many nights each recipient needs. Don't copy a currency figure from another event. Cap per person, publish the cap, and keep a reserve for late requests. Don't promise a headcount. | self-set |
| **Overspend stance** | PyCon's stance is to over-invest in aid when it makes a better conference. Decide in advance whether unspent funds roll over or return to the sponsor. | sourced stance, decision yours |

## Sponsor and money handling

- **Get the terms in writing before announcing.** Is the fund restricted to this purpose? Can it roll over? Does the sponsor get naming credit? **[self-set]**
- **The sponsor must not choose recipients.** It also shouldn't see applicant names or disclosures. A sponsor in the selection loop creates a conflict, and the applicants' data would leak to a third party. **[self-set]**
- **Keep the fund in a separate ledger line** so you can report spend against the 18k. **[self-set]**
- **Counsel questions (Q6), not answered here.** Ask counsel about:
  - Grants to individuals by an association.
  - Tax or VAT reporting on payouts.
  - Cross-border payouts.
  - How disability or hardship data may be held in your jurisdiction.
  - Whether accessibility duties apply to your event.
  - "Fine for an incorporated association" settles whether you can hold money. It doesn't settle these.

## Data posture

Decide these before the form opens and publish the first three. **[sourced]**

1. **Retention:** a date tied to the event, and actually delete at the debrief.
2. **Access:** which organizers read applications, shared only to arrange the grant. Not the sponsor.
3. **Turnaround:** how fast you reply, including declines.
4. **Where it lives:** an inbox or form you control, not a field in the ticketing platform's registration records.
5. **Who decides a decline:** one named person, with the reason written down.

Collect only what you need to decide. Don't ask applicants to prove hardship in detail or declare protected characteristics.

## Draft page copy

> **Inclusion Fund.** Thanks to our platinum sponsor, we can help people attend OpenCircuit Fest who otherwise couldn't. We fund speakers and contributors, people facing financial hardship, and people from groups underrepresented in our community.
>
> **What it covers:** travel, hotel and registration. One application.
>
> **How we pay:** we book flights and hotels directly for approved recipients where we can. If we can't, we reimburse against receipts. Receipt-based payment excludes people who can't front the cost, so tell us if that is you and we will look at an advance.
>
> **Who decides:** <named owner> and a small panel. The sponsor doesn't see applications.
>
> **Dates:** applications open <date> and close <date>. We reply within <M> days of the close, including declines.
>
> **Your data:** we use what you tell us only to decide this grant, share it only with the panel, and delete it by <date>.
>
> **What we can't promise:** the fund is limited, so we can't fund everyone who applies. If we can't help, we'll say so early and tell you what else exists.

## Handoffs

- `event-cultural-identity`: how the fund is worded and positioned.
- `event-ticket-pricing`: the ticket-side need-gated route, so there is no second application.
- `event-attendee-experience`: placement and wayfinding at the event.
- `event-venue-sourcing`: only if the fund affects venue criteria.
- Anything about code-of-conduct enforcement goes to `event-code-of-conduct`.

## Measurement **[self-set]**

- Applications received against grants made, with the reason for every decline.
- Lead time from page publication to the travel-booking window.
- Share of the 18k spent, and by which payment path (direct booking, advance, receipts).
- Repeat needs that should become standing provisions.

## Open questions before this is final

1. **Event date.** This sets the application window. Today is 2026-10-12, so the travel-booking window may already be near.
2. **Attendance and origins.** How many people, and from where? This sizes the per-person cap.
3. **Sponsor terms.** Is the fund restricted, and does the sponsor expect naming or recipient information?
4. **Named owner.** Who owns the fund from now through the debrief? A role inbox won't do.
5. **Childcare.** Do you provide it, or know of a caregiving population among attendees? If not, leave it out.
6. **Jurisdiction.** Has counsel looked at grants to individuals, payout reporting, and applicant data? If not, send the counsel list above.

I haven't run the one-question-at-a-time interview. The structure above rests on the assumptions you gave. If any answer differs, tell me and I'll re-rank the menus.