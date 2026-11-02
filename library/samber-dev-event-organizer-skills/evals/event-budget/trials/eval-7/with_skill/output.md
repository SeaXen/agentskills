# PortScan Summit: budget model, first pass

**Format and posture:** ticketed conference, **sponsor-led** (assumed; confirm). Sponsorship carries the bulk and tickets cover per-attendee cost. Sponsors from three countries and a fiscal host taking a cut on both rails make this the right default.

No ticket price, sponsor price, quote or expected-show-up figure was supplied. Nothing below invents one. Every number is a formula, a placeholder, or labelled published or self-set.

## 1. ⚠️ The fee assumption is probably stale

You budgeted 5% on card payments and 8% on bank transfers. That is the legacy fee schedule of one open-source funding platform. The reference this skill relies on marks it **superseded**:

- The platform moved to a subscription model in **March 2026**. Hosts that still charge a host fee pay the platform a 15% share of that fee revenue. Verify current terms before relying on this.
- Its associated 501(c)(3) fiscal sponsor **dissolved on 31 December 2024**, displacing 600+ collectives. The platform continues under a separate 501(c)(6).

Consequences:

- **Do not carry 5%/8% as the deduction.** Published fiscal-sponsor fees typically run 7-14%, and the legacy split was cheaper than all of that. Using it understates what comes off the top.
- **Ask the host in writing:**
  1. What is the current fee, per rail?
  2. Which legal entity holds our money today?
  3. What is the realistic time from funds landing to funds spendable?
  4. Which payment processor fees apply on top, on the ticket rail and on the sponsor rail?
- Treat the answer to question 2 as a continuity risk as well as a price. If you signed up under the old structure, you may have been migrated.
- Hold the 5%/8% and any quoted 7-14% figure as placeholders until the host's reply is dated and filed.

**Net-revenue formulas (replace the placeholders with the host's answer):**

- Net ticket revenue = gross × (1 − host fee − processor fee on the card rail)
- Net sponsor revenue = gross × (1 − host fee − processor fee on the rail that sponsor uses)
- To net a target T, invoice T ÷ (1 − fee). A 10% total deduction means invoicing about 11.1% more than T, not 10% more.

Sponsors in Germany and Japan will often pay by bank transfer. Budget them on the bank-transfer rail, which was the expensive one even under the legacy schedule. Also ask the host about currency: in what currency are Japanese and US payments received, and who bears conversion?

## 2. Cost lines

The taxonomy follows the conference model. Each line is split fixed, per-head or per-speaker. That split is this skill's own construction, not measured event data. Every quote status is "no quote yet" until you attach a dated quote.

| Line | Character | Driver | Quote status |
| --- | --- | --- | --- |
| Venue | Fixed (deposit and attrition risk) | Venue tier | No quote yet |
| Internet | Fixed | Venue | No quote yet |
| Media (livestream, recording, captions) | Fixed, from `event-production` pre-split by tier | n/a | No quote yet |
| Signage | Fixed | n/a | No quote yet |
| Admin: insurance, accounting, tax handling | Fixed | n/a | No quote yet |
| Catering | Per-head | **Expected show-up**, not registrations | No quote yet |
| Badges and lanyards | Per-head | Expected show-up | No quote yet |
| Merchandise | Per-head | Expected show-up | No quote yet |
| Evening event | Discretionary | Best tier only | No quote yet |
| Speaker expenses | Per-speaker | Speaker count | No quote yet |
| Expo booths (if any sold) | Fixed per booth, plus power and furniture | Booths sold | No quote yet |
| Parent-community contribution (if PortScan is under a parent program) | Fixed | At least one full-price ticket, if the rule applies to you | Check |
| Host fee and processing | Off the top, see section 1 | Revenue | Awaiting host reply |
| Tax handling (line, see section 5) | Fixed | n/a | Awaiting accountant |

Rules applied:

- Per-head lines use the expected-show-up number. The registration count over-orders catering by construction.
- Cost per head = (per-head lines) ÷ expected show-up. Keep this on hand for any "tickets are too expensive" complaint.

## 3. Revenue targets

All of these are self-set formulas.

- **Sponsorship target** = share × total net expenses. Hand it to `event-sponsor-pricing` for the tier split.
- **Ticket target** = total net expenses − net sponsorship. Hand it, with paid capacity after comps, to `event-ticket-pricing`. Count comps only from agreements actually held: signed sponsor allotments, confirmed speakers, organizers and volunteers.
- Do not re-derive a ticket or sponsor price to make the model balance. Change the target and hand it back.
- Published splits disagree almost completely: roughly 90/10 sponsor-led in one actual, roughly 3% sponsor in another. They bound the possible postures and are not a target.

Concentration check: with sponsors in three countries, say what happens if the largest two do not pay. The ladder below answers that.

## 4. Bundled sponsorship + booth

**Recommendation: do not sell one blended line. Sell sponsorship and booth as two itemized lines, and give the bundle discount as a visible discount on the total.**

Why:

- The reference describes a bundle as taking the tax treatment of whichever element an authority judges to dominate it. Space and sponsorship are taxed on different bases in at least one major system. A blended line makes your VAT treatment a guess.
- With three sponsor countries, a single blended line could be treated differently in each.
- Itemizing also keeps the budget clean. The booth has its own costs (floor space, power, furniture) and the sponsorship has none of those.

The price split between the two lines is a pricing decision for `event-sponsor-pricing`. This model needs two revenue lines with an agreed split, and the invoice, contract and host record must show both. Put the one-price promise in the contract as a total with itemization beneath it. The treatment still needs your accountant's sign-off (section 5).

## 5. Tax: the open question, written as a question

⚠️ I'm not stating a rate, threshold, registration requirement or form. The skill forbids it, and the answer depends on facts I don't have. The reference gives only contrasts:

- **Tickets (admission):** in one large bloc, admission to events and conferences is taxed where the event physically takes place, regardless of attendee or organizer domicile.
- **Sponsorship:** taxed on a different basis entirely, the payer's jurisdiction under the general business-to-business rule. Sponsors in Germany, Japan and the US could therefore each produce a different treatment.
- **A federal system without a national sales tax:** admissions taxation is set state by state, and non-profit status does not settle it. Sponsorship revenue for a charity is usually an unrelated-business-income question, a different mechanism from sales tax.
- The treatment of virtual and livestreamed access changed on 1 January 2025 in at least one system.
- Any of this may be out of date.

So I can't tell you yet whether you must charge VAT on tickets, or on sponsorships. The honest answer is "it depends on three things we haven't pinned down."

**What I need from you before this can be answered:**

1. In which country, and for the US in which state, is PortScan Summit physically held?
2. Which legal entity sells the tickets and invoices the sponsors: the fiscal host, or you?
3. Is any part livestreamed to paying remote attendees?
4. Where are attendees and each sponsor invoiced from, and do sponsors have VAT or tax IDs?

**Budget line plus open item to carry:**

- **Line:** Tax handling, fixed, amount unknown.
- **Question:** "Who confirms the VAT and sales-tax treatment of (a) ticket revenue, (b) sponsorship revenue from German, Japanese and US payers, and (c) booth space, and by what date?"
- **Owner:** the fiscal host first, because they may be the invoicing entity and the party liable. Then a local accountant or counsel for the event's jurisdiction.
- **Date:** before the first ticket is sold. The ticket price, the invoice templates and the sponsor contracts all depend on it. Retrofitting VAT onto prices already published is the audit risk you're worried about.
- **Recording:** when the answer comes back, write it into this budget as a line item with the date and the person who gave it.

An accountant who sees this model and these four answers can reply in one email. Ask them to confirm the bundle itemization too. If you're also asked about cross-border registration, note one organizer guide's warning that obtaining a tax identifier abroad can take a significant share of a small event's money. That cost belongs in the budget if it applies.

## 6. Three costed tiers

Each tier is fully costed with its own break-even. The numbers are formulas, not amounts.

| Tier | Contents | Break-even (attendees) |
| --- | --- | --- |
| **Good** | Runs at all: venue, internet, core Media, catering, badges, speaker expenses. No evening event, minimal merch, no expo. | (Fixed + speaker) ÷ (net ticket − per-head cost), after sponsorship |
| **Better** | Good plus expected niceties: fuller Media, merch, expo floor if booths sell. | Same formula with Better's costs |
| **Best** | Better plus evening event, upgraded swag, headroom. | Same formula with Best's costs |

Break-even per tier = (fixed + speaker costs − net sponsorship) ÷ (net ticket price − per-head cost per attendee). If sponsorship alone exceeds fixed costs, break-even is zero on the ticket side and the per-head cost is covered by tickets.

## 7. Contingency: three tools, stacked and not ranked

All three are self-set. None is an event-industry convention, and I won't present any as one.

- **Floor:** an absolute minimum cash reserve held regardless of budget size. A published hackathon guide uses a flat floor of $1,000-$3,000, scaled to event size. That is one organizer's recommendation. Set the PortScan floor once, label it self-set, and fill in the amount.
- **Pad:** a percentage added to estimates before summing. The one available figure, 20%, is borrowed from startup financial modelling and not measured on events. Use it only if you label it that way. Protects against line underestimation, not revenue shortfall.
- **Downgrade ladder:** the three tiers above with dated checkpoints, driven by revenue received. This is the only one that absorbs a whole-event shortfall.

**Cut order inside the ladder:**

1. Discretionary extras: evening event, swag upgrades, sponsored add-ons.
2. Per-head quantities, only before the catering guarantee locks.
3. Fixed structural lines last. Attrition and F&B minimums are owed on the commitment, so cutting late can cost more than keeping.

## 8. Cash flow: lowest point to compute

I can't compute the trough without dates and amounts. The shape to watch:

- **Outflows:** venue deposit typically 25-50% at signing and the balance 14-30 days out (generic industry-guide mechanics). Large venues are booked 9-18 months ahead.
- **Inflows:**
  - **Sponsors:** published terms skew to large upfront payments (50-100% at signing), but those are one organization's terms each. Use your own contracts' dates. The Japanese and German sponsors may have slower payment processes.
  - **Tickets:** the latest-arriving and most uncertain line.
  - **Host release timing:** money landing in the host account is not money you can spend. Ask the realistic delay.
- **Failure shape to rule out:** the model is profitable on paper yet fails because deposits leave before sponsor invoices are paid. Read the lowest cash point, not the bottom line.
- **Commitment posture:** default to the **latest safe date** for each commitment. Stage a room block or catering guarantee in steps only if it carries a threshold owed regardless of turnout and someone holds a standing tracking job through the sale window. Any counterparty offering a genuine early-payment discount would justify paying earlier. Ask Q11.
- **Checkpoints:** hand the dates to `event-planning-timeline` and `event-risk-management`.

**Gate before the first go/no-go date:** every line carries a dated quote or an explicit "no quote yet", and the cash-flow schedule has a computed lowest point.

## 9. What I need from you, in priority order

1. **Host reply on fees and entity** (section 1). It changes every net figure.
2. **Event location, invoicing entity, livestream** (section 5). It decides the tax question.
3. Expected show-up number, who produced it, and whether it is a show-up figure or a registration count.
4. Which lines already have dated quotes.
5. Commitments already signed, with the date each stops being recoverable.
6. By what date sponsor and ticket money must be in the account.
7. One-off edition or one year of a recurring event.
8. Who approves spend, and who is the second approver.
9. Who can run a standing tracker through the sale window.
10. Do the venue or vendors offer genuine early-payment discounts?

I'd start with items 1 and 2. Everything else can be filled in while you wait for those two replies.