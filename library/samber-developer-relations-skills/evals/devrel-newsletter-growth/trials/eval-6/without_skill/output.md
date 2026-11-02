# Vellumgate newsletter: form copy and signup flow

## Decision summary

| Ask | Answer |
|---|---|
| Single opt-in on the docs footer | ❌ Keep double opt-in (DOI). |
| Pre-checked newsletter box on product signup | ❌ Ship it unchecked. |
| Goal: more confirmed subscribers | ✅ Reduce DOI drop-off instead (see the end). |

**Why not single opt-in**
- In Germany, §7 UWG requires prior express consent for marketing email. If a subscriber disputes consent, you must prove it.
- A public form accepts any address. Single opt-in lets anyone subscribe someone else, and you can't prove the address owner agreed. German courts and data protection authorities treat DOI as the accepted proof.
- 35% of your list is German, and a mixed flow adds complexity. Use DOI for everyone.
- The fines and warning-letter (Abmahnung) risk are not worth the lift. The cost is only the unconfirmed signups, who weren't confirmed subscribers anyway.

**Why not a pre-checked box**
- GDPR Art. 4(11) and Recital 32 require a clear affirmative act, and "silence, pre-ticked boxes or inactivity" don't count. The CJEU confirmed this in *Planet49* (C-673/17).
- "People can always unsubscribe" describes withdrawal of consent, which only matters after valid consent exists. It doesn't replace consent.
- A pre-checked box also bundles marketing into account creation. That makes the consent not freely given.

This is product guidance, not legal advice. Have counsel review the final wording and the privacy notice.

## 1. Docs footer form

**Idle state**

> **Developer newsletter**
> Feature-flag tips, API changes, and release notes. About twice a month.
> `[ you@company.com ]` `[ Subscribe ]`
> We'll email you a confirmation link first. Unsubscribe anytime. Details in our [Privacy Policy](/privacy).

**Submitted state (replaces the form, no page reload)**

> **Check your inbox.**
> We sent a confirmation link to **{email}**. You're not subscribed until you click it. The link works for 48 hours.
> Wrong address? [Use a different email]. No email after a few minutes? Check spam, or [resend it].

**Errors**

- Invalid address: "That email address doesn't look right. Check it and try again."
- Already confirmed: "You're already subscribed. Nothing more to do." This confirms the address is on the list, so some teams prefer the generic "Check your inbox" message here to avoid leaking list membership. Pick one deliberately.
- Rate limited: "Too many attempts. Try again in a few minutes."

## 2. Confirmation email

**Subject:** Confirm your Vellumgate newsletter subscription

> Hi,
>
> Someone, hopefully you, asked to receive the Vellumgate developer newsletter at this address.
>
> **[Yes, subscribe me]** ({confirm_url})
>
> This link expires in 48 hours. If you didn't ask for this, ignore this email. You won't be subscribed and we won't email you again.
>
> What you'll get: feature-flag tips, API changes, and release notes, about twice a month. You can unsubscribe in one click from any issue.
>
> Vellumgate · {company legal name and postal address}
> [Privacy Policy](/privacy)

## 3. Confirmed page

> **You're subscribed. ✅**
> First issue lands within two weeks. Meanwhile: [Quickstart] · [API changelog].

The welcome email (optional) states the cadence and links to one-click unsubscribe.

## 4. Product signup page: unchecked, separate checkbox

Keep this away from the terms-of-service checkbox. Don't bundle them.

> ☐ **Send me the developer newsletter** (feature-flag tips and release notes, about twice a month). You can unsubscribe anytime.

- Default state: **unchecked**. Never required to create the account.
- If ticked, send the same confirmation email (section 2) after signup.
- Optional shortcut: if the account verification email already proves address ownership, you may treat a ticked box plus a verified address as consent. Log the timestamp and the exact wording shown. This is the less conservative option, so ask counsel before using it for German users. DOI is the safe default.

## 5. Signup flow

1. Visitor submits the email, from either the footer or the signup page.
2. Validate format server-side. Rate-limit by IP and by address.
3. Create or update the record with status `pending`. Store:
   - timestamp
   - source (`docs_footer` or `product_signup`)
   - form version and consent text shown
   - IP (per your privacy policy)
4. Send the confirmation email with a single-use token. Expiry is 48 hours.
5. On click:
   - Verify the token.
   - Set status to `confirmed`.
   - Store the confirmation timestamp, IP and user agent. This is your proof of consent.
   - Show the confirmed page.
6. Handle edge cases:
   - **Expired link:** show "This link expired. [Send a new one]."
   - **Resubmit while pending:** resend at most once per hour, up to 3 times total. Then stop.
   - **Never confirmed:** delete the record after 7 days (or anonymise it, per your retention policy). Never email the person again.
   - **Already confirmed:** do nothing, and show the message you chose in section 1.
7. Every newsletter issue includes:
   - one-click unsubscribe, with `List-Unsubscribe` and `List-Unsubscribe-Post` headers (RFC 8058)
   - a visible unsubscribe link
   - your legal entity name and postal address
8. On unsubscribe, set status to `unsubscribed` immediately. Keep a suppression record so the address isn't re-added by import.
9. Handle erasure requests: delete the personal data, but keep a minimal suppression entry (hashed address) so you don't re-mail.

## What to give the PM: lower DOI drop-off

DOI loses people mostly at the inbox step, not at the form. Fixes that work without weakening consent:

1. **Send the email instantly.** Check the delay from submit to inbox. Anything over 30 seconds costs confirmations.
2. **Make the subject and button obvious.** "Confirm your Vellumgate newsletter subscription" with one large button.
3. **Show the "Check your inbox" state with the address,** plus resend and change-address links (section 1). This prevents typo losses.
4. **Send from a recognisable address** (e.g. `newsletter@vellumgate.com`) with SPF, DKIM and DMARC set, so it doesn't land in spam.
5. **Offer a link to your webmail provider** from the "Check your inbox" state, if you can detect it from the domain.
6. **Send one reminder** about 24 hours later for pending signups: "Your confirmation link is still waiting." This is a reasonable follow-up to a request the person made, but get counsel's view for German addresses.
7. **Put value on the form.** Show a sample issue or the topics. People who see what they get confirm more.
8. **Measure the right number.** Report confirmed subscribers per 100 form submissions, not raw signups. A single opt-in list inflates the count and includes typos, bots and people who never asked.

## Metrics to track

- Submit → email delivered → clicked → confirmed (a funnel by source: footer vs product signup)
- Spam complaint rate and bounce rate (single opt-in would raise both, and hurt deliverability for the whole domain)
- Unsubscribe rate per issue