**Next action (2 min): message your treasurer, "Please send me the bank's IBAN certificate (RIB) for the new account, and confirm it receives SEPA transfers in EUR."**

Don't put the IBAN on an invoice until you have it. "Fairly sure" isn't enough. The skill says to verify the receiving account and currency work *before* the sponsor pays.

## Do these in order (about 45 min of your time, plus waiting on the treasurer)

1. **Verify the account.**
   - Ask the treasurer for the bank-issued IBAN/BIC document.
   - Check that the account holder name matches the legal entity that will invoice.
   - Ask whether it takes incoming SEPA transfers in EUR.
   - Optional: have someone send a EUR 1 test transfer from another account.
2. **Pin down what Halden actually bought.**
   - Write down the package, the activities, and the EUR 6,000 amount.
   - Include only activities the program really contains. Anything promised on the phone but missing on the day turns a yes into a lost renewal.
   - Also write down whether the EUR 6,000 includes VAT. This is not in the skill. I'm adding it because it changes what you invoice.
3. **Invoice immediately, once step 1 is clear.**
   - "Payment terms are whatever" doesn't work here. Put a due date on the invoice, even a generous one.
   - Send the invoice with a short written confirmation of amount and payment method. A phone yes is not yet a signed yes.
   - Use the skill's close mechanics on a yes: invoice, written confirmation, verified account.
4. **Hand off to `samber/dev-event-organizer-skills@event-sponsor-agreement`.** It handles terms and the signature. Payment terms belong there, so do not leave them open.
5. **Update the pipeline.**
   - Move Halden to "Committed", then to "Signed" once the agreement is back.
   - Name one liaison for Halden. That person owns contact, payment chasing, and discount codes through fulfillment.
   - Mark whether Halden is renewal or net-new, so the stage conversion rates stay separate.
6. **Check the deal-size gate.**
   - A small pledge needs a signature and nothing else.
   - If EUR 6,000 is in your largest pledge tier, run a quick values-alignment check inside the organizing team before you finalize.
7. **Log it.** If a conversation surfaced any objection or odd request, record it by sponsor segment so it can feed back to `event-sponsor-value-proposition`.

Then go back to the list.

## Two questions for you

- Is EUR 6,000 your top tier? That decides step 6.
- Is Halden a returning sponsor or net-new? That decides the pipeline tag in step 5.