# Driftly Dispatch: Ostrander sponsorship plan

## Answer first

1. **Do not accept Ostrander's offer as written.** It fails two rules, so the answer is no even before the price is considered.
   - Pay-per-signup with no flat fee is a refused structure. We carry their conversion risk and cannot audit their tracking.
   - Ostrander's "product analytics" add-on competes with Driftly. Our written default refuses any product that competes with one we sell, including a module inside a broader product.
2. **Do not let Ostrander in, even on a flat fee.** The add-on makes this a competitor-rule refusal, whatever they pay. Our readers are Driftly's buyers, so a flat-fee Ostrander ad would sell them an alternative to our product.
3. **Do sell sponsor slots to non-competing sponsors.** That depends on the gate below, where three of the four conditions are blocked on facts I don't have.

**For the CEO, "no risk" is wrong.** The risk moves to us.
- We get nothing if their landing page, signup flow or tracking underperforms, and we can't check their numbers.
- We spend a slot on an issue and sponsor-review hours on four issues.
- Illustration (all inputs self-set): at $12 per signup, matching a $500 flat slot takes 42 signups per issue. With 100 human clicks, that is a 42% click-to-signup rate. Realistic rates are in the low single digits, so we would earn $12–60 per issue.

## Refused asks

| Ask | Basis | Offer instead |
|---|---|---|
| Pay-per-signup as the only payment | House rule: the publisher carries conversion risk and cannot audit the sponsor's tracking | Performance pay only on top of a flat fee above our floor, with the sponsor's tracking named and disputes settled on our filtered click count |
| Booking 4 issues | House rule: only book issues the owner has committed to | Name the four issues, add a pause clause (move the slot or refund), and take payment before the copy deadline |

Standing refusals for every sponsor:
- A review or editorial pick bundled with the slot.
- "Sponsored by", "Presented by" or a logo alone as the label.
- Pricing on opens or gross subscribers.
- A raw-click guarantee.
- Sharing subscriber or clicker identities.
- A dedicated send to a list that consented to "the newsletter".

## Gate result

| Condition | Evidence so far | Result |
|---|---|---|
| Measured engagement | "Solid click history, filter on" is a claim. I need six issues of per-link human clicks and the filter's name. | **Blocked.** Owner: you or the sender-platform admin. Cheapest fix: export the last six issues' per-link clicks. |
| Describable reader | No signup question or survey was mentioned. | **Blocked.** Owner: newsletter editor. Cheapest fix: add one signup question (role, company size). |
| Seller with hours | No named seller or invoicing entity. | **Blocked.** Owner: Driftly. Name a seller and the invoicing entity. |
| Readers told | Unknown whether the signup form or privacy notice mentions sponsor content. | **Blocked.** If missing, update the signup text and announce sponsor content in an issue before the first paid one. |

A failed "seller" or "readers told" condition blocks every sale until it is fixed. If only engagement or the reader description fails, the fallbacks are a pilot at the floor, classified or job lines, or no sales.

## Acceptance policy

This is written before judging any cheque.

```
We accept sponsors whose product serves [readers: role, stack, from signup question].
We do not accept: products that compete with Driftly or any product we sell,
  including a module or add-on inside a broader product; [add categories: crypto,
  gambling, ...].
Sponsors buy a labelled slot. They never buy editorial coverage, ranking or a review,
and they see only their own unit before send.
We may require edits or decline copy, with a reason, up to the copy deadline.
One link per unit, to the sponsor's own domain. No downloads, no unreadable shorteners.
```

Competitor-rule exception: accept integration partners whose product does not overlap with Driftly's, with the same "Ad" label. Any exception for a module inside a competitor's product must be written into the policy before a cheque exists. Don't carve one out for Ostrander.

**Ostrander against the policy:**
- Fit: observability serves the readers.
- Competitor rule: **fails**, because of the product analytics add-on.
- Link: their landing page would also likely cross-sell the add-on.

Verdict: refuse. Log it in the refusal log as date, Ostrander, competitor rule, and who decided.

**Reply to Ostrander** (draft):
> Thanks for the interest. Our policy doesn't accept products that compete with Driftly, which includes your product analytics add-on, so we can't run your ad. We'd be glad to revisit if that changes.

## Sales route

Recommendation: **one direct labelled primary slot per issue.** Ranking: direct primary slot, then network listing, classifieds, bundles, dedicated sends.

- Network listing: kept only if 18k clears the network's floor and its ads respect our competitor rule. Networks skip our per-ad policy, so check this before signing.
- Dedicated sends: deleted. I haven't confirmed the list consented to partner offers, and the EU and UK require consent that names them.
- Bundles: deferred until three consecutive issues sell out.
- Re-rank once questions 6 and 8 are answered. A revenue deadline inside a month would promote classifieds and the network.

## Inventory and caps

- Cap: the charter's cap, otherwise one primary slot plus classifieds. **Blocked:** I haven't seen the charter. If it forbids paid placements, stop here.
- Primary slot spec: position 2 after the lead item, a word limit, one link, no image. Keep it identical every issue.
- Category exclusivity: a priced add-on, limited to the booked issues.

## Rate card

Provisional until questions 2, 3 and 6 are answered. No final price.

| Method | Working | Result |
|---|---|---|
| Cost-recovery floor | (sender-platform cost + seller hours × hourly rate + any host share) ÷ sellable slots | **Blocked**: seller hours and rate unknown |
| Comparable band | Developer titles at 28–73 per 1k gross subscribers, from Q2 2024 cards (Golang Weekly 28, Postgres Weekly 73). Apply the ratio, not the dollar figure, to 18k. | About $500–1,300 for a primary slot (provisional) |
| Click value | Median filtered human clicks on past sponsor units × cost per click. With no sponsor history, use editorial clicks at that position × an ad discount, labelled self-set. | **Blocked**: needs the click export |

- Until the first sponsor report, cap click value at the band's top plus a third.
- Never price under the floor.
- A cost per click the sponsor states from search is buyer-supplied: mark it and discount it.
- Secondary units run at one third to one half of the primary. Classified and job lines run at a twentieth to a sixth.
- Every sponsor pays the same price for the same slot and date.

## Label

```
AD · Acme Queue: managed Postgres queues for background jobs
AD · ANZEIGE · Acme Queue: ...   (only if German readers are a real share)
```

- Put the label before the copy, in the HTML part, the plain-text part and the web archive.
- Mark sponsor links `rel="sponsored"` in the archive.
- Keep sponsor names out of the subject line.
- **Blocked:** reader regions (question 7) decide whether "Anzeige" is needed. If unsure, add it.

## Booking terms

- One named slot and issue, with the card price.
- Hold released after 7 days.
- Copy deadline two working days before send.
- Late copy runs as the sponsor's name, one neutral line and the link, or moves to a later issue.
- Edit and reject rights.
- Fixed house label, one link to the sponsor's own domain.
- Sponsor notice of one week; refunds for issues more than a week out.
- Pause clause: move the slot or refund.
- Make-good for a failed send, broken link or missing label, in the next comparable slot.
- Sponsor warrants its claims.
- Payment before the copy deadline, via a named invoicing entity.
- Aggregate report only.
- No exclusivity unless bought.
- Performance pay only on top of a flat fee above the floor, with the sponsor's tracking named.

## Report template

Send within a week of the issue.

```
Issue: #NNN, sent YYYY-MM-DD to N delivered addresses
Slot: primary, position 2, label "AD"
Link: https://sponsor.example/...
Unique human clicks: N (filter: [name the bot-click filter and its rules])
Total clicks recorded: N (before filtering)
Opens: directional only, inflated by mail-privacy features
Median unique human clicks, last six primary slots: N
What we need back: signups or trials you attributed to this link
```

No subscriber names, emails or companies.

## Pass thresholds

| Threshold | Result |
|---|---|
| Gate states all four conditions with evidence | Stated; 4 of 4 blocked on facts |
| Named sponsor judged against the written policy | Pass; Ostrander refused, with basis |
| Prices trace to the floor, a dated ratio or measured clicks | Band done; floor and click value blocked |
| "Ad" label in HTML, plain text and archive | Pass; "Anzeige" depends on question 7 |
| Terms name deadline, edit rights, cancellation, pause, make-good, payment | Pass |
| Report template names the filter and has no identities | Pass |

## What I need from you

1. The click export for the last six issues, with the filter named (per link, human clicks, and any past sponsor units).
2. How you know who reads it (signup question, survey or guess), and whether the signup text mentions sponsor content.
3. Who sells and invoices, their hours per month, and what an hour is worth.
4. The charter's sponsor rule and cap, plus reader regions.

I'd start with item 1. It unlocks the real price.