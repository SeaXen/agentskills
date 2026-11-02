# Corvane Builders: Nimbit sponsorship plan

## Direct answer

Don't set it up as asked. Marketing is wrong on the label, and two of Nimbit's asks fail on consent.

1. **"Partner, not advertiser" doesn't change anything.** Once Nimbit pays for the placement, it is advertising. A partner announcement is only editorial when the partner paid or traded nothing. Payment triggers the label in the US, UK, EU and Germany.
2. **Decline the dedicated send to all 26,000.** Your readers signed up for "the newsletter" or for docs updates. In the EU and UK that consent doesn't cover a paid send for a third party, and the UK soft opt-in never does. In the US, CAN-SPAM applies instead of a ban. Your readers in the UK, France and Germany put you in the strict regimes.
3. **Decline the CSV of clicking companies.** Handing a third party named companies and their clickers has no lawful basis or notice in the EU or UK. Corporate mail gateways also click every link, so the list would be partly machine noise.

**Offer instead:**
- **A labelled primary slot** in a normal issue of Corvane Builders.
- **Aggregate reporting** to Nimbit.
- **Opt-in lead capture** that Nimbit can actually use (see Route below).

Nimbit gets its announcement and a real lead path. Marketing gets a revenue line that won't land in a complaint or a regulator's inbox.

## Refused asks

| Ask | Basis | Replacement |
|---|---|---|
| Dedicated send to the whole list | Law (EU/UK consent). US: CAN-SPAM duties. | Labelled slot in a normal issue, or a separate partner-offers opt-in list |
| CSV of companies whose people clicked | Law (EU/UK) and trust | Aggregate counts only. Company-size bands only if the privacy notice already covers it. Never company names. |
| "Partner, so no label" | Law: paid placement must be identifiable as advertising | `AD` label, plus `ANZEIGE` for German readers |

## Gate result

All four conditions must hold. I have no evidence yet for any of them, so none is confirmed.

| Condition | What's needed | Status |
|---|---|---|
| Measured engagement | Six issues of per-link human clicks, with the bot-click filter named (a historical export counts) | **Blocked.** Owner: whoever runs the sending platform. |
| Describable reader | A signup question or survey. A mixed list is described by its largest segment (product signups), and the media kit says so. | **Blocked.** Owner: DevRel. |
| Seller with hours | A named person who answers, approves copy and reports, within an hours ceiling, plus an invoicing entity | **Blocked.** Owner: you. |
| Readers told | Signup form or privacy notice says issues carry labelled sponsor content | **Blocked.** Owner: DevRel and legal. |

"Readers told" and "seller" block every sale until fixed. If the signup text is silent, update it. Then announce sponsor content in an issue before the first paid one, with the unsubscribe link prominent.

If only engagement or the reader description fails, run a **pilot booking**. That is one issue at the cost-recovery floor, with the missing evidence disclosed to Nimbit in writing. Its report becomes your first data point.

## Acceptance policy (write it before judging Nimbit's cheque)

- **Fit:** the product serves your readers, builders integrating APIs, and its claims are checkable.
- **Vetoes:** [fill in: for example crypto, gambling, claims you can't verify].
- **Competitor rule:** refuse any product that competes with Corvane, including a module inside a broader product. Accept integration partners with no overlap, with the same label as any ad. **Nimbit passes only if it doesn't overlap with your gateway.** Confirm that.
- **Editorial firewall:** the slot buys a position and a label, never coverage or a review. Nimbit sees only its own unit before send.
- **Edit rights:** you can require edits or reject copy, with a reason, up to the copy deadline.
- **Links:** one link to Nimbit's own domain, no downloads, no opaque shorteners.
- **Refusal log:** date, sponsor, rule applied, decider. Log today's two declined asks.

Publish a short version on your advertise page.

## Sales route

Ranked by efficiency: direct primary slot, then network listing, classifieds, bundles, dedicated sends.

**Recommendation: one direct, labelled primary slot in the next normal issue.**
- **Dedicated send:** deleted, because of the consent problem above. Promote it only if you build a separate opt-in list for partner offers and agree a complaint threshold with whoever owns deliverability.
- **Network listing:** unlikely to fit at your size, and a network's ads would bypass your policy.
- **Lead path for Nimbit's SDRs (my suggestion, not from the skill):** the slot links to a Nimbit-hosted page about the joint integration. That page carries Nimbit's own signup form with an explicit, unticked "contact me about Nimbit" consent. People who opt in become Nimbit's leads lawfully, and no list leaves Corvane. Have counsel check the wording. The skill doesn't prescribe this.

Please confirm the route before I go further.

## Inventory and caps

- **Slot:** one primary, position 2 (after the lead item), roughly 60 to 80 words, one link, optional image. Fix the spec and keep it identical every issue.
- **Cap:** one paid unit per issue unless your charter says otherwise. No secondary slots yet.
- **Exclusivity:** none by default. If sold, it is a priced add-on limited to the booked issue.
- **Frequency:** you send monthly, so a slot is rare inventory. Book only issues you've committed to send.

## Rate card (provisional)

I won't quote a final price. I need your delivered count, the click data, and the seller's hours and rate.

| Method | Working | Result |
|---|---|---|
| Cost-recovery floor | (platform cost + seller hours × hourly rate + any entity share) ÷ sellable slots | **Blocked:** needs question 6 answers |
| Comparable band | Published developer titles at 36k to 61k subscribers run about 22 to 30 per 1,000 on a primary slot. A 16k niche title runs about 73. At 26,000 subscribers that gives roughly **650 to 1,900 USD**. | **Provisional.** Cards date from Q2 2024: re-check before quoting. Broad lists sit at the low end, narrow ones at the high end. |
| Click value | Median filtered human clicks on past sponsor units, or editorial clicks at position 2 × a discount derived from any labelled unit you've sent. Multiply by cost per click. | **Blocked:** needs click export |

- **Price from clicks, not from 26,000 or from open rates.** Opens are inflated by mail-privacy features.
- **Nimbit's own cost per click** is a buyer-supplied anchor. Mark it and discount it.
- **Before the first report exists,** click value is capped at the band's top plus a third, and never goes below the floor.
- **Same price for any sponsor** taking the same slot and date.
- **No raw-click guarantee.** After six sponsor reports you can offer an optional floor on filtered human clicks, with a make-good.
- **Performance pay:** only on top of a flat fee that clears the floor, with a written tracking-dispute rule.
- **Any figure you didn't measure** is labelled self-set.

## Label

Put it on the unit before the copy, in the HTML part, the plain-text part and the web archive:

```
AD · ANZEIGE · Nimbit: <one-line description of the joint integration>
```

- **Wording:** "Ad" is recognised in the US and UK. "Anzeige" is needed for your German readers.
- **France:** it falls under the EU regime and "Ad" covers it. Adding "Publicité" is my suggestion, not from the skill. Ask counsel.
- **Don't use** "Presented by", "Sponsored by", "Together with Nimbit" or a logo alone. Those read as funding, not advertising. A friendly line may sit beside the label, never replace it.
- **Subject line:** keep Nimbit out of it. A promotional subject can turn the whole issue into commercial email.
- **Archive links:** mark Nimbit's link `rel="sponsored"`.
- **Real legal exposure** (cross-border consent, the lead-capture form) goes to counsel. This plan isn't legal advice.

If Nimbit pays nothing and trades nothing, the announcement is editorial. You can run it as a normal item under your curation rule, with no label. The data refusals still apply.

## Booking terms

Confirm in writing before the invoice:
- **Slot and date:** one named slot, one named issue.
- **Price and currency:** the card price for that slot.
- **Hold:** released if not confirmed within 7 days.
- **Copy deadline:** 2 full working days before send. Late copy runs as Nimbit's name, one neutral line and the link, or moves to a later issue. You never write promotional copy for Nimbit.
- **Edit rights:** you may require edits or reject copy, with a reason.
- **Label:** fixed house label, not negotiable.
- **Links:** one link to Nimbit's domain. Their tracking parameters are allowed.
- **Cancellation:** at least one week's notice. Prepaid fees are refunded for issues more than a week out.
- **Pause clause:** if you skip or pause an issue, the slot moves or is refunded in full.
- **Make-good:** a failed send, broken link or missing label reruns in the next comparable slot at no charge.
- **Warranty:** Nimbit warrants its claims and that the link stays live and safe. You may pull a unit whose claims or destination change.
- **Payment:** before the copy deadline, from a named invoicing entity. Check VAT treatment for a cross-border sponsor.
- **Data:** aggregate report only. No list, no clicker identities.

## Sponsor report template

```
Issue: Corvane Builders #<n>, sent <date> to <delivered> delivered addresses
Slot: primary, position 2, label "AD · ANZEIGE"
Link: <Nimbit URL with its utm parameters>
Unique human clicks: <n>   (filter: <platform bot-click filter, on>; <exact rules, e.g. clicks within 10 s of delivery and all-links-clicked sends removed>)
Total clicks recorded: <n> (before filtering)
Opens: directional only, inflated by mail-privacy features; not reported as reach
Median unique human clicks, last six issues' primary slots: <n>
What we need back: signups or trials you attributed to this link
```

Send it within a week. Add no names, emails or companies. If your privacy notice allows it, add counts per company-size band only.

## Pass-threshold result

| Threshold | Result |
|---|---|
| Gate states all four conditions with evidence | **Blocked.** Evidence missing. |
| Nimbit judged against the written policy | **Pending.** Competitor-overlap check needed. |
| Every price traces to the floor, a dated ratio or measured clicks | **Blocked.** Provisional band only. |
| Label before the copy in HTML, text and archive, plus Anzeige | Passes as drafted |
| Terms name deadline, edit rights, cancellation, pause, make-good, payment | Passes as drafted |
| Report names the filter and holds no identities | Passes as drafted |

## What I need from you

Send these in this order:
1. Does Nimbit's product overlap with Corvane's gateway in any way?
2. Delivered count per issue, plus per-link human clicks for the last six issues and which bot filter was on.
3. Who sells and services sponsors, their hours per month and hourly value, and which entity invoices.
4. What the signup form and privacy notice say about sponsor content.
5. What you know about the readers (signup question or survey), and the rough split across the US, UK, France and Germany.
6. Does the charter allow paid placements, and with what cap?
7. Is there a date the revenue must land by, and is this a one-off or a standing line?

## Reply you can send Nimbit

"We can run your integration announcement as a labelled ad in the next Corvane Builders issue, at [price after the data above]. We can't send a dedicated email to the full list or share names of companies who clicked, because our readers' consent doesn't cover it. You'll get an aggregate click report within a week. For leads, we'll link to a Nimbit page with an opt-in form, so the people who want to hear from you come to you directly."