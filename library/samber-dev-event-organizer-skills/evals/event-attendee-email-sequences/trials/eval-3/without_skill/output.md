# Short answer

⚠️ **Don't send the merged blast as planned.** An unsubscribe link doesn't give you permission to send. It only keeps a send you're already allowed to make from becoming a second violation. The two lists have different legal footing, so treat them separately.

This assumes you're UK-based, since the conference is in Edinburgh. UK GDPR and PECR then apply, and so do EU rules for any recipients in the EU. I'm not a lawyer, so have whoever handles data protection at your company confirm the final call.

## List 1: 1,900 ticket buyers

🟠 **Buying a ticket is not marketing consent.** The likeliest route is the PECR "soft opt-in", which needs all of these:

1. You collected the email during the ticket sale.
2. You're marketing your own similar thing, and a sequel conference qualifies.
3. The buyer got a clear chance to refuse marketing at checkout, and gets one in every email.

What to check before sending:

- **Checkout wording.** Look at the actual checkout page from last year. If there was no opt-out or privacy notice mentioning future event marketing, the soft opt-in is weak.
- **Who owns the data.** Check the ticketing platform's terms. It may be an independent controller, and its export may not be yours to use for your own marketing.
- **Buyer or attendee.** Soft opt-in covers the person who bought. Someone else on a company-bought ticket was never your customer in that sense.
- **Opt-outs.** Remove anyone who unsubscribed, complained or asked for erasure after last year's event. Also remove refunded and charged-back buyers and anyone who opted out at checkout.
- **Recipients outside the UK.** EU member states differ, and some are stricter, so check the country split.
- **Privacy notice.** You received this data indirectly from the platform. You need to tell people how you use it, and the email footer should link to that notice.

## List 2: 450 newsletter signups

🟢 **This is the stronger list, but verify one thing.** You said the form has an opt-in checkbox for event news. That doesn't mean all 450 ticked it.

- **Send only to the ticked ones.** If the checkbox was optional, send only to those who ticked it.
- **Checkbox default.** It must not have been pre-ticked.
- **Checkbox wording.** It must plausibly cover this email: event announcements from your organisation.
- **Consent records.** You should have a timestamp, the wording shown and the source for each record, in case of a complaint.

## Merging the lists

- **Dedupe first.** The count will drop below 2,350.
- **Tag every record.** Keep a field for source and basis (`soft-opt-in` or `consent`), and don't flatten them into one anonymous list.
- **Apply one suppression list across everything.** Someone who unsubscribed from your newsletter must not get the announcement just because they also appear in the ticketing export.

## What every email needs

- Sender identity, your company name and a postal address.
- A working one-click unsubscribe that you honour promptly, ideally with a `List-Unsubscribe` header.
- A link to your privacy notice.
- A subject and body that are honest about being a promotion.

## Deliverability

⚠️ The 1,900 addresses are a year old and may have bounces and dead mailboxes. Sending to all of them at once from a domain that hasn't sent that volume risks complaints and spam-folder placement for the whole domain.

- Check SPF, DKIM and DMARC on the sending domain.
- Send the consented 450 first, then the ticket buyers in batches.
- Remove hard bounces as you go.

## Recommended plan

1. Filter list 2 to the contacts who ticked the event-news checkbox.
2. Audit last year's checkout flow, then decide whether list 1 qualifies for the soft opt-in.
3. Dedupe, tag and suppress across both lists.
4. Send to the consent segment first, then the soft opt-in segment in batches.
5. If list 1 fails the audit, send a one-off "stay in the loop" opt-in request instead. Consider whether even that is allowed, because it can itself count as marketing. Otherwise rely on organic channels for those people.

I can draft the segmentation checklist or the email footer and unsubscribe copy. I can also write the two-segment send schedule if you want it.