**Answer:** Both of the growth PM's asks are refused as specified, and each has a replacement that fits the same goal.
- **Single opt-in on the docs-footer form:** keep double opt-in. The form is public and 35% of subscribers are in Germany.
- **Pre-checked box on the product signup page:** replace it with an unticked box. A pre-checked box is invalid consent in the EU, UK and Canada, and "they can unsubscribe" is not a defense.

The copy and flow below are ready to ship. They assume the monthly cadence in the placeholder, so confirm it against the charter first (see Open questions).

## Refusals applied

| Ask | Type | Why | Replacement |
|---|---|---|---|
| Pre-checked "Send me the developer newsletter" box | **Law** | Pre-ticked consent is invalid in the EU, UK and Canada, and in Germany too. The sender must be able to prove consent, and a pre-ticked box proves nothing. Unsubscribing later does not cure invalid consent. | A separate, unticked box, below |
| Single opt-in on the docs-footer form | **Law-adjacent proof problem** | No regime names double opt-in, but you cannot exclude German readers, bots or someone typing another person's address. German courts accept the confirmation click as proof of one subscriber's consent. A general claim that you run double opt-in does not prove it. | Keep double opt-in. Cut the friction around it instead (below). |

Pre-checking would also pollute the per-source metrics with people who never chose the newsletter. It would show up as early churn and complaints, the same pattern as an unconsented import.

## On the PM's concern: signups lost to double opt-in

- **What you lose:** people who never confirm. That group includes bots, typos and addresses entered by someone else, none of which you can lawfully mail anyway.
- **The only figure I have:** Mailchimp reported 39% of its double opt-in starters finished. It is not specific to developers and it is context only, not a target. Your own docs-footer confirmation rate is the number that matters, and I don't have it.
- **What to track:** report confirmed signups per source, never form submissions. A drop in submissions-to-confirmed is not a drop in subscribers you could have kept.
- **Levers that raise confirmation without weakening proof:**
  1. Show an on-page "check your inbox" state, with a resend link and a spam-folder hint.
  2. Send the confirmation email within seconds, from a recognisable sender name.
  3. Keep the confirmation email to one sentence and one button, with no promotion.
  4. Link the latest issue on the form, so readers know what they are confirming.

## Growth gate

- **Programme holds:** unproven. I have no charter, owner, backup or cadence evidence. Proving it is the first task.
- **Consent known:** unproven. I don't know how the existing list was collected beyond the docs footer. Classify each segment before counting the list.
- **Sources distinguishable:** unproven. Add the hidden `source` field to both forms below before any traffic goes to them.

## Signup contract

Both forms share this contract.
- **Promise:** what arrives, how often, who sends it, the latest issue, and the privacy notice.
- **Choice:** separate and unticked.
- **Confirmation:** double opt-in on both forms (reason below).
- **Guard:** honeypot plus per-IP rate limit.
- **Record:** timestamp, source tag, form version, exact consent text shown, and the confirmation click.
- **Welcome:** latest issue plus how to unsubscribe.
- **Suppression list:** unsubscribed addresses stay on it so no later import re-adds them.

## Form 1: docs footer (public)

Source tag: `docs-footer`. Form version: `v1`.

```
Vellumgate developer newsletter
Once a month, from the Vellumgate API team: releases, deprecations with
dates, one deep dive. Read the latest issue first.

[ email address                    ]   [ Subscribe ]

Vellumgate [legal entity name] sends this newsletter. Unsubscribe from any
issue. Privacy notice.
```

- Submitting the form is the consent act, and the text beside the button is the consent text. Store that exact text with the record.
- Keep the form separate from any other form on the page.
- Do not put a subscriber count in the copy unless it is the confirmed, current count.

**After submit (on-page state):**

```
Check your inbox. We sent a confirmation link to {email}.
You are subscribed once you click it. Nothing is sent before that.
Nothing there? Check spam, or resend.
```

**Confirmation email.** One sentence and one button, with no promotion, sponsor or product pitch.

```
Subject: Confirm your Vellumgate developer newsletter subscription

Someone entered this address for the Vellumgate developer newsletter
(one email a month); confirm to subscribe, or ignore this email and
nothing will be sent.

[ Confirm subscription ]
```

The wording is neutral about who entered the address. A German regional court has held that even a neutral confirmation email can be unlawful when a third party typed the address. The honeypot and rate limit are the mitigation, so don't skip them.

**Welcome email** (after the confirmation click):

```
Subject: You're in: the latest Vellumgate developer newsletter

Welcome. Here is the latest issue: [link]. The archive is here: [link].
One email a month. Unsubscribe from the footer of any issue.
```

## Form 2: product signup page

Source tag: `signup-page-box`. Form version: `v1`.

This is not a verified login. The email is not yet verified at the moment of signup, so it follows the public-form rule: double opt-in.

```
[ ] Send me the Vellumgate developer newsletter: one email a month on
    releases and deprecations. Unsubscribe from any issue. Privacy notice.
```

- The box is unticked by default and is not a condition of creating the account.
- Put it below the account fields, not inside the sentence that links the Terms of Service. Terms and consent stay in separate sentences.
- Do not bundle it with the account-verification email.

## Signup flow (product page)

1. The user submits the form. The account is created whether or not the box is ticked.
2. If the box is ticked, store a pending record: timestamp, `signup-page-box`, form version, the exact checkbox text, and (if your privacy notice covers it) the IP address. This is a request, not a subscription yet.
3. Send the account-verification email. It says only "verify your account". It never mentions the newsletter, and verifying never subscribes anyone.
4. Send a separate newsletter confirmation email, the same one-sentence email as Form 1. Mark the record confirmed only on the click, and store the click timestamp.
5. If the user doesn't click, they receive nothing, and the pending record expires after a fixed window. Pick one with the privacy owner, for example 7 days.
6. On confirmation, send the welcome email.
7. Add the unsubscribed address to the suppression list on any unsubscribe. Unsubscribe is one click: an optional reason field comes after it completes, never a required field or a login.

**Optional second path:** an in-product invite for logged-in users who didn't tick the box. Use an unticked checkbox in dashboard settings, tagged `in-product-invite`. This form sits behind a verified login, so single opt-in is acceptable there as long as you keep the full record. It reaches existing users without any import.

## Do not do

- Do not import existing product accounts or trial users into the newsletter. Account signup is not newsletter consent (house rule).
- Do not email existing users asking them to subscribe. That email is itself marketing without consent in the UK and EU.

## German readers

An optional German version of the consent text, if you want to show it to German-locale visitors. Have a native speaker and the privacy owner review it before use.

```
[ ] Ja, schickt mir den Vellumgate-Developer-Newsletter: einmal im Monat
    Releases und Deprecations. Jederzeit abbestellbar. Datenschutzhinweis.
```

## Metric sheet

Every metric is per source tag and counts confirmed subscribers. All targets are house rules, set from your own baseline after two months of tagged data.

| Metric | Sources |
|---|---|
| Net confirmed growth | `docs-footer`, `signup-page-box`, `in-product-invite` |
| Confirmation rate (confirmed ÷ submissions) | per form |
| First-issue click (human clicks only) | per source |
| Activation (human click in first four issues) | per source |
| Early churn (gone within three issues) | per source |
| Unsubscribes and complaints per send | per source |
| Outcome: product signups from newsletter links | the charter's funding answer |

Do not rank a source on fewer than about 30 confirmed signups. Do not report gross list size, form submissions or open rate as growth.

## Open questions

- **Charter and cadence (owner: DevRel lead):** does a charter exist with an owner, a backup and a monthly cadence? Did the last three issues go out on time? The copy says "once a month" as a placeholder. Change it to the real cadence before launch, because a broken promise is the commonest cause of early unsubscribes.
- **Existing list consent (owner: privacy owner):** how was the current list collected, and which segments have no recorded source? Classify them, and suppress any with no basis, before counting the list.
- **Sender entity name:** the legal entity that sends the newsletter. Consent must name the sender, so fill the placeholder in Form 1.
- **Legal review:** this is not legal advice. Send the final call on the German-locale copy and the pending-record expiry window to whoever owns privacy.
- **Docs-footer baseline:** current docs-footer submissions and confirmations. Without them, the PM's "loses too many signups" claim can't be checked.

**Pass-threshold result:** all six thresholds pass except two that are blocked. The growth-gate evidence is unproven for programme and consent, and I haven't invented it. Re-check once the charter and list-collection answers arrive.