# Brightpath user conference: ticket pricing review

**Verdict: ❌ Not signed off as proposed.** A single $1,200 ticket and a $2,200 "Supporter" tier fail the skill's checks for specific reasons. The fixes are below. They need five inputs from you before any price can be final.

## 1. Why I can't sign off

| Item | Status | Why |
|---|---|---|
| Revenue target | ❌ Missing | The skill makes the budget the starting point. A ladder built without a ticket-revenue target "under-prices tier by tier". Marketing owns the line, but I have no figure. |
| $1,200 for everyone | ❌ Wrong shape | Half your audience is employer-funded customers. The other half is practitioners you are trying to win over. The skill's main lever is one price per payer type, not one price for all. |
| $1,200 justified by "what big cloud-native conferences charge" | ⚠️ Weak evidence | The skill wants dated registration pages, not remembered numbers. It also says to transpose ratios, never amounts. |
| "Supporter" at $2,200 | ❌ Mislabeled | The skill's Supporter tier is a pay-more ticket whose premium funds accessibility for others, such as RailsConf's Scholars program. Yours buys the buyer something: front row, a CTO dinner, a jacket. That is a VIP upsell. |
| Refund and transfer policy | ❌ Not written | It must exist before the first ticket sells. |

## 2. What is fine

- ✅ **A commercial-price posture is defensible.** The skill's promotion condition is a vendor-run event priced against company budgets. Brightpath is the vendor, so you aren't stuck with a nominal fee.
- ✅ **An employer-funded tier at roughly $1,200 is plausible.** I can't confirm it without dated comparables, but it isn't unreasonable.

## 3. Proposed structure for you to validate

Every number is labeled **sourced** (published ladders, transposed by ratio) or **self-set** (my assumption, yours to override).

### Target and capacity (self-set, pending your inputs)

- **Ticket revenue needed** = total event expenses minus the share covered elsewhere. For a vendor event, that other share is marketing's budget plus any sponsors. I have none of these figures.
- **Paid seats** = 600 minus committed comps. Count comps from actual commitments: speakers, Brightpath staff, partners, invited guests, and Supporter-adjacent seats. The skill sets no percentage rule, so I won't invent one.
- **Open question:** is 600 the paid capacity or the total headcount? This changes the math.

### Posture

Commercial price for the employer-funded half. Free-by-design or nominal for customers is a legitimate alternative. A vendor can decide the event is a marketing expense and price it that way. That is a budget decision for Marketing, not a pricing one. Please tell me which one was made.

### Persona ladder (ratios sourced, amounts self-set)

Sourced corporate-to-individual ratios are about 1.9:1 (PyCon US 2026) and 1.67–1.78:1 (EuroPython 2026). EuroPython's lower ratio fits better here because half the room is being courted. If $1,200 holds for the employer-funded tier:

| Tier | Price | Basis |
|---|---|---|
| Business / customer (employer-paid) | ~$1,200 | Your VP's figure, once checked against dated comparables |
| Individual (self-funded practitioner) | ~$630–720 | $1,200 divided by 1.67–1.9 |
| Student / education (optional) | ~$185–325 | $1,200 divided by 3.7–6.5. Only if students are a real target. |

The skill says to set the floor from your own per-attendee cost, not from a comparable, so treat these as placeholders. Ask whether practitioners pay themselves or expense it. If most expense it, the individual tier collapses toward the business price.

### Gate (self-set)

- Use at most two public price points per persona.
- Announce one dated step from day one. Decide whether it is an expiring early-bird or a late surcharge (EuroPython's late step is 1.5x).
- Never announce a price rise the buyer couldn't see coming.

### Access rungs

- **Published student tier:** low effort, listed only if students matter to you.
- **Discretionary scholarship:** costs real review labor. It becomes worth it if you can staff the review, or if accessibility is a claim you must defend (Q8/Q10). Write the reviewer and response time before publishing, because an unanswered application is worse than no route.
- **Never list it as a cheap public tier.**

### Bulk mechanics

- **Pay-by-invoice:** this is probably the highest-value rung for you, since employer-paid customers often can't use a card checkout. It's a payment rail at full price, never a discount. It requires Brightpath finance to be able to invoice.
- **Group discount:** one flat percentage for a minimum head count in a single order, on the standard tier only. Don't stack it on early-bird.

### The $2,200 tier

The skill has no ranking for VIP upsells, so this is judgment, not sourced guidance:

- **Rename it** to VIP or Premium, or make it a true Supporter tier. For the latter, earmark the premium to a named scholarship or aid program. The skill says a Supporter tier needs that program to exist first.
- **Cap the count** to what the perks physically allow. Front-row seats and a CTO dinner have a hard limit, so set the number before you set the price.
- **Cost the perks in the budget.** The dinner, the jackets, and CTO time are expenses against the $2,200, not free.
- **Check it against your goal.** A reserved front row sold to the highest payer partly conflicts with courting practitioners. Decide whether the perks should go to customers, practitioners, or both.
- **Keep it a minor revenue line.** Uptake is small, and the skill ranks this rung last on value.

### Refund and transfer policy (decide each line)

The only point all four sourced events (PyCon US, EuroPython, RustConf, KubeCon) share is a single dated cutoff, not a sliding scale. Every other term is yours to choose:

- Cutoff date, tied to catering and badge deadlines.
- Administrative fee, flat or a percentage.
- Hardship rule, as either a waiver or a later deadline.
- Transfers: person to person, within a company, and a rule for when the two ticket prices differ. Without that rule, a $1,200 ticket becomes a resale of a $650 one.
- Whether the Supporter or VIP perks transfer.
- What happens if Brightpath cancels. That is a contracts and risk question, and this skill gives no legal advice.

Publish the policy next to the price.

## 4. What I need from you to finalize

1. **Budget:** the total expense figure and the ticket-revenue share. If it doesn't exist, run `event-budget` first.
2. **Free, nominal, or priced:** was it decided, and by whom?
3. **Comps:** counted seats for speakers, staff, partners, and guests. Also, is 600 paid capacity or total?
4. **Payer split:** do the practitioners pay themselves or expense it? And can Brightpath issue invoices?
5. **Comparables:** which big cloud-native conferences, and the dated registration pages. The $1,200 needs that evidence.

Two read-only inputs also help. A market-fit read (`event-market-fit`) tells you whether a slow sale means price, demand, or marketing. A no-show plan (`event-no-show-management`) covers seats that were bought but never used. Once the structure is validated, hand acquisition to `event-marketing-plan`.

**Bottom line:** I'd sign off on a payer-split ladder with an invoice rail and a written refund policy. A single $1,200 price plus a relabeled VIP tier I can't approve as is.