# Refundable deposit flow for the monthly Rust breakfast (Austin)

## 0. Design choices

- **Charge the card at registration and refund it at scan-in.** A card authorization hold would be simpler. But card holds expire after about 7 days (check Stripe's current limit), and a monthly event opens registration earlier than that. A hold that lapses means you have no commitment and no money.
- **Refund every attendee who physically scans in, however late.** The catering is already paid, and a late person still eats. Lateness isn't what costs you money. Absence is.
- **Forfeit the deposit only for no-shows.** Keep this rule simple. A rule with many exceptions leads to arguments at the door.
- **Expect fewer RSVPs and a higher show rate.** Your current 50% show rate (45 of 90) is your own number. It's higher than CNCF's ~30% no-show planning figure, so use yours. A deposit will probably cut RSVPs and raise the show rate. That is my estimate, not a measured result. Measure it over the first three editions before you trust any new catering formula.
- **Fees are a real cost.** Stripe generally doesn't return its processing fee on refunds, so each refunded deposit costs roughly $1.50. Check Stripe's current fee. Across 45 attendees that's about $65 a month. Either budget for it or say "fees apply" on the page. I recommend you absorb it, because an attendee who loses $1.50 will be annoyed.

## 1. Registration page copy

> **Rust at Breakfast, [date], 8:00 am, [venue], Austin**
> Free event. Refundable $40 seat deposit.
>
> We pay for breakfast for everyone who RSVPs. When people don't show, the food goes to waste. So we hold **$40 on your card to reserve your seat, and refund all of it when you scan in at the door.** Come at 8:00 or come at 9:15, you get the full $40 back.
>
> **How it works**
> 1. Register and pay the $40 deposit.
> 2. You get a QR ticket by email.
> 3. Scan it at the door. Your $40 refund starts right away. It appears on your card in 5–10 business days.
>
> **Can't make it?** Cancel yourself from your ticket link until **[date, 48 hours before]** and you get the full $40 back. We lock the catering count 48 hours out. After that, a no-show forfeits the deposit.
>
> **Emergency?** Reply to your ticket email within 7 days of the event and we'll review it.
>
> Forfeited deposits go to [covering catering / a Rust community charity: pick one and say so].
>
> [ ] I understand the $40 deposit is refunded when I scan in, and forfeited if I don't attend and haven't cancelled by the deadline. *(required checkbox)*
>
> [Reserve my seat, $40 refundable]

The checkbox and the plain wording about forfeiture are your defense against chargebacks. Put the refund, the deadline and the forfeit rule on the checkout page itself. Also put them in the confirmation email.

## 2. When the card is charged

| Moment | Action |
|---|---|
| Registration | Stripe Checkout charges $40 immediately. Metadata: `event_id`, `attendee_id`. |
| Immediately | Confirmation email with QR ticket, cancel link, and the refund and forfeit rules repeated. |
| T-72h and T-48h | Reminder email: "Can't come? Cancel here before [deadline] for your $40." |
| T-48h | Cancellation window closes. Send the final headcount to the caterer. |

Waitlist: when someone cancels, offer the seat to the next person. Charge that person's card when they accept, not before.

## 3. How the refund fires

1. Staff open a check-in page on a phone or tablet. Attendees scan the QR from their email or wallet. A name search is the fallback.
2. The scan marks the attendee `checked_in` and calls the Stripe Refund API for the full $40. Use an idempotency key (`refund-{attendee_id}-{event_id}`) so a double scan cannot refund twice.
3. The attendee gets an email: "Refund of $40 issued, allow 5–10 business days."
4. If the venue Wi-Fi is down, the check-in page queues scans locally and fires the refunds when it reconnects. Staff keep a paper list of names as the final backup.
5. If a refund fails (expired or closed card), email the person for another way to pay them back, or offer to donate it.
6. Reconcile after the event. Every refund must match a `checked_in` record, and no `checked_in` record may lack one.

Walk-ins without a registration get in free if there is food left. They pay no deposit and get no refund.

## 4. Late arrivals

- **Anyone who scans in before the event ends gets the full refund.** There is no penalty window.
- Put "Come at 8:00 or come at 9:15, you get the full $40 back" on the page. It removes the temptation to skip when running late.
- If you want people on time, handle that with the food and the talk, not the deposit. Serve breakfast from 8:00 to 8:45 and start the talk at 8:45.
- If someone arrives after the event has ended, treat it as a no-show. The 7-day emergency review still applies.

## 5. No-shows

1. The day after the event, send an email: "We missed you. Your $40 deposit was forfeited under the rule you accepted. If you had an emergency, reply within 7 days."
2. Review replies. Refund genuine emergencies and note them. Don't argue the rest.
3. After day 7, close the books. Put forfeited money where the page said it goes.

## 6. Measure and adjust

Log per event: RSVPs, door count, show rate, cancellations before the deadline, forfeits, and refund fees paid. After three events:

- Set catering to your own measured door count plus a small buffer.
- If RSVPs fall by more than the no-shows you were losing, the deposit costs you real attendance. Lower it to $20 or move to charging only no-shows later.

## 7. Legal and accounting checks

- Ask your accountant how forfeited deposits are treated for Northbeam. That's a tax question I can't answer.
- Chargebacks are the main risk. The checkbox, the refund and forfeit terms in the confirmation email, and your check-in log are the evidence. Keep the log for at least a year.

## 8. Alternative if the deposit hurts RSVPs

Collect the card at registration without charging it (Stripe SetupIntent). Charge $40 only to no-shows after the event. This avoids refund fees and shows no money leaving anyone's account up front. The downsides are failed charges, more disputes, and a weaker commitment signal. I'd start with the charge-and-refund design above and switch only if the data says to.