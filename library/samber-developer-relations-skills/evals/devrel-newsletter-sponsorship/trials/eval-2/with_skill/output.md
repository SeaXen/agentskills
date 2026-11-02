# Is $620 right? No. Don't quote it yet.

**$620 is not a defensible number, even though it lands inside the plausible range.** It comes from the wrong inputs. A provisional range is below, and the final price is blocked on facts only you have.

## Why the $50 CPM math fails

- **The $50 CPM is unsourced.** A Discord claim is not a rate card. Published developer-newsletter rates are dated and vary widely by list size and niche. Use the ratio, never another title's dollar figure.
- **12,400 is gross subscribers.** Pricing per gross subscriber is a refused method. The count that matters is delivered per issue, which you didn't give me.
- **Opens are not "real readers".**
  - Mail-privacy features have auto-opened mail since September 2021, so 52% overstates reading.
  - Opens would also give 12,400 × 52% × $50/1000 ≈ $322, a number that means nothing.
  - Sponsors measure clicks. A sponsor who gets fewer clicks than the price implied books once and leaves.
- **Your click data is unfiltered.** The bot-click toggle has never been on. Corporate mail gateways click links on arrival, so your current click counts include machines. This is the fix to make before any pricing.

## Provisional range (not a quote)

From published developer-newsletter cards (Q2 2024), a primary slot runs about 20–30 per 1,000 subscribers on big broad lists (JavaScript Weekly 20, Golang Weekly 28). Small niche lists run higher, up to about 73 (Postgres Weekly, 16k subscribers). Golang Weekly's card is the closest comparable to a Go list.

| Ratio | Applied to 12,400 |
|---|---|
| 30 per 1,000 | about $370 |
| 70 per 1,000 | about $870 |

- **This range only frames the price.** It never sets it.
- **Your list sits near the bottom.** You are a solo, unverified Go newsletter, and nothing about your readers is documented yet.
- **With no sponsor data, quote near the bottom (about $370) until the first report.** Re-price from measured clicks after that. A cap of about $1,150 applies to any quote before then.
- **Price clicks, not subscribers.** The final price is expected filtered human clicks on the sponsor unit × a cost per click, held between the cost-recovery floor and that cap. Every input you haven't measured gets labelled self-set.

## Gate result (the check that decides whether you can sell yet)

| Condition | Status |
|---|---|
| Measured engagement: 6 issues of per-link clicks with a named bot filter | **Fails.** The filter has never been on. |
| Describable reader: role, seniority, company size, how you know | **Blocked.** You haven't told me. |
| Seller with hours, plus an entity that can invoice | **Blocked.** You are the seller, but I don't know your hours or invoicing entity. |
| Readers told: signup form or privacy notice mentions labelled sponsor content | **Blocked.** Unknown. |

**The cheapest fixes, in order:**

1. **Turn on the bot-click filter.**
   - Export the last six issues' per-link clicks.
   - If the platform can't filter retroactively, strip clicks within about 10 seconds of delivery and sends where every link was clicked.
   - Name the filter you used.
2. **Check your signup text.**
   - If it doesn't say issues may carry labelled sponsor content, add that line now.
   - Announce sponsor content to the list in an issue before the first paid one, with the unsubscribe link prominent.
   - A failed "readers told" or "seller" condition blocks every sale.
3. **Add one signup question** (role) or run a short survey, so you can describe your reader to a sponsor.

**If the sponsor won't wait for the data, you have three choices:**

- **Pilot booking.** One issue at your cost-recovery floor, with the missing evidence disclosed to the sponsor in writing. Its report becomes your first data point.
- **Classified or job line.** A flat low price, about a twentieth to a sixth of a primary slot.
- **No sale** until the gate holds.

## Cost-recovery floor (blocked on your inputs)

Floor = (platform cost per issue + your sponsor hours × your hourly rate + any platform or host share) ÷ sellable slots. No sale goes below it. Give me three numbers: monthly hours you'll spend on sponsors, what an hour of your time is worth, and which entity invoices.

## Terms to hold now

- **One labelled primary slot per issue.** Position and word limit fixed, one link to the sponsor's own domain, flat price per issue.
- **Label.** "AD" before the copy, in the HTML part, the plain-text part and the web archive. Add "ANZEIGE" if you have German readers. Never "Sponsored by", "Presented by" or a logo alone. Mark archive links `rel="sponsored"`. Keep the sponsor out of the subject line.
- **Decline if asked:**
  - a sponsored review or "feature us in the news section too"
  - a raw-click guarantee
  - a dedicated send to your list
  - a list of companies whose engineers clicked
  - pay-per-signup as the only payment
- **Acceptance policy.** Write it before you see their cheque. It needs:
  - category vetoes
  - the right to edit or reject copy, with a reason
  - one link per unit
  - a refusal log
- **Booking terms:**
  - one named issue
  - copy due 2 working days before send
  - payment before the copy deadline
  - a pause clause that moves or refunds the slot
  - a make-good in the next slot
  - the sponsor warrants its claims
  - aggregate report only
- **Report within a week.** Delivered count, unique human clicks with the filter named, total clicks, and opens marked directional. No subscriber identities.

## What I need from you (blocked until supplied)

1. The company's request, pasted: product, slot, dates, budget, any extra asks.
2. Delivered count per issue, and per-link clicks for the last six issues with a bot filter applied. Include clicks on any past labelled units, such as job lines or house ads.
3. Who reads you: role, seniority, company size, region. Is that from a signup question, a survey or a guess?
4. Your sponsor hours per month, your hourly rate, and the invoicing entity.
5. Your readers' regions (US, UK, EU, Germany), what the signup text says about sponsor content, and what is off-limits (competitors, categories).

## Holding reply to the company

> Thanks for reaching out. I sell one labelled ad slot per issue at a flat price. I'm finalising my rate card from filtered click data and will send it by [date]. The slot carries an "Ad" label, covers one link to your domain and includes a report on filtered human clicks. I don't sell editorial coverage or reviews, and I don't share subscriber data.

Don't name a price in that reply. Once the filtered exports are in, I can turn the range into a quote.

**Pass-threshold status:** pricing, gate and floor are **blocked** on the facts above. Label, refusals and terms pass.