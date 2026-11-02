# Ostlund Labs newsletter: the 1,400 badge scans and the re-permission email

## Direct answer

**No. The "Do you want to keep receiving our newsletter? Click yes!" email is not a legal clean-up.** For individual subscribers in Germany, the rest of the EU and the UK, an email asking for marketing consent is itself marketing. Regulators have fined senders for exactly this. The email would add one more unlawful send. It would also not repair the 1,400 sends you have already made.

Fix it by suppressing the scanned segment, not by asking it to opt in. Then work out whether the segment is the cause of your churn. This is not legal advice, so your privacy owner makes the final call on each segment.

## 1. Refusals applied

| Move | Label | Why | Replacement or reversal |
|---|---|---|---|
| Importing the 1,400 badge scans (already done) | **Law** for EU, UK and German individuals. **Trust and house rule** for UK company addresses and Canadian scans | The scans were collected for the event, not for your newsletter. German law (UWG §7 with GDPR) needs prior express consent that names the sender. The burden of proof is on you, not on the attendee. | Reversal task: suppress the segment (steps below). |
| "Re-permission" email to those 1,400 | **Law** (EU and UK individuals) | The email asks for marketing consent, so it is marketing sent to people with no consent. | Don't send it. Use the lawful routes in section 4. |

**One exception to check before suppressing everyone.** Look at what the booth scanner or the sales form said. If a person ticked a separate, unticked box that named Ostlund Labs and covered email, that person has consent. Keep them, and keep the scan record as proof. If the scan only said "we may contact you" or "partners may contact you", it is not consent.

**Reversal steps, in order:**
1. **Stop sending to the segment now.** Every further send is another violation, and the segment is the likeliest cause of the complaints.
2. Tag the 1,400 as one segment, with source `badge-scan-may-<event>`. Check the tag is not mixed in with organic subscribers.
3. Split the segment by country.
   - **EU, UK and Germany, individuals:** suppress.
   - **US:** opt-out rules apply, so it may be lawful. Your privacy owner decides.
   - **Canada:** an implied-consent route may exist, but only with a role-relevant message and no stated refusal.
   - **UK limited-company addresses:** exempt from the consent rule, but they still need sender identity and an opt-out. Your privacy owner decides.
4. Move the suppressed addresses to a **suppression list**, not a delete, so nobody re-imports them later. Keep the scan record and the date of the import.
5. Tell your privacy owner what happened. They decide whether the import needs recording or reporting internally. Do not decide this alone.

## 2. Growth gate

| Condition | Status | Evidence |
|---|---|---|
| Programme holds (owner, backup, last three issues on cadence) | **Unproven** | You didn't say. Confirm the owner and backup, and that the last three issues went out full and on time. |
| Consent of each segment is known | **Fails** | The 1,400 have no recorded consent. The other 4,200 are unknown to me: how were they collected, and was it single or double opt-in? |
| Sources can be told apart | **Probably fails** | Check whether each subscriber record has a source field. If not, the badge scans are mixed into the list with no tag. That is also why you cannot yet prove the cause of the churn. |

Do these first, before you open or add any growth channel.

## 3. Churn reading: is the import really the cause?

Likely, but not yet proven. Here is why it is the lead suspect:

- The 1,400 are 25% of your 5,600 list.
- The jump from 0.2% to 0.7% per send is about 28 extra unsubscribes per send on 5,600 subscribers.
- If all of that came from the 1,400, their unsubscribe rate is roughly **2.2% per send**. That is about 10x your organic baseline, and a plausible rate for people who never asked for the newsletter.
- For context only: Mailchimp's average is 0.22% and Brevo's figure for the software sector is 0.44%. Your old 0.2% was normal, and 0.7% is well above the sector figure.

**Test it by splitting the last six sends, plus the two sends before May, by three dimensions:**

1. **Source.** Badge-scan segment against everyone else. If the other 4,200 are still near 0.2%, the cause is confirmed.
2. **Tenure.** Unsubscribes concentrated in the first three issues after the import point to people who never wanted the newsletter.
3. **Issue.** If one issue spiked and then the rate returned, the cause is that issue's content, not the import.

**Also check:**
- **Complaints and unsubscribes together.** Complaints rising while unsubscribes stay flat means people can't find the unsubscribe, or never knew they subscribed. "Never knew I subscribed" is the consent problem showing.
- **Your provider's one-click unsubscribe.** If Gmail or Yahoo launched one inside your window, it can shift complaints into unsubscribes. Rule that out before blaming the content.
- **Your actual complaint rate.** Google's guidance is to stay under 0.1% and never reach 0.3%, and it binds senders of 5,000+ messages a day to Gmail. At 5,600 subscribers you are below that scale, but your sending platform likely enforces its own limit, so check it. Rising complaints put inbox placement at risk for all 5,600 subscribers, not just the badge-scan ones. If placement is already slipping, route that to the deliverability skill.
- **The signup promise.** Does the welcome or form promise a cadence and content the issues don't deliver? Check this for the organic 4,200 too.

## 4. How to reach the 1,400 people lawfully

- **Talk end card or booth sign.** At the next event, show a signup link or QR code. People sign up themselves, and no consent review is needed.
- **Event registration form.** Add a separate, unticked newsletter box to the next registration form, for events you organise.
- **In-product invite.** For the scanned people who are also product users, show one invite inside the product with an unticked box.
- **Sales follow-up.** Whether sales may contact them one to one is a separate legal question from the newsletter. Ask your privacy owner, and keep it out of the newsletter list.

## 5. What to tell your manager

> "A consent-request email is itself marketing under German and EU rules, and regulators have fined senders for it. The fix is to suppress the scanned segment, not to email it. We keep the people who ticked a box naming us, and invite the rest at our next event or inside the product. This also protects deliverability for the other 5,600 subscribers' mail."

## 6. Signup contract going forward

Every form should carry:
- **Promise:** what arrives, how often, who sends it, a link to the latest issue, and the privacy notice. Write the cadence you really keep.
- **Choice:** a separate unticked box, never a condition of a ticket, download or account.
- **Confirmation:** double opt-in on public forms. With half your list in the EU and a large share in Germany, the confirmation click is the one per-subscriber proof of consent that holds up.
- **Record:** timestamp, source tag, form version, the consent text shown, and the confirmation click.
- **Suppression:** keep unsubscribed and removed addresses on the list so they can't be re-added.
- **Booth rule for sales:** if booth scans are ever used for the newsletter, the scanner form needs its own unticked, named checkbox for Ostlund Labs.

## 7. Metrics to track from now

Report per source, never as gross list size or open rate:

- Net confirmed growth.
- Unsubscribes and complaints per send.
- First-issue click rate (human clicks, bot clicks filtered).
- Early churn: share of a cohort gone within its first three issues.
- One outcome signal matching your charter, such as SDK signups from newsletter links.

Set baselines from your own numbers for the next two months, and label every target a house rule.

## 8. Open questions

1. What did the booth scanner or sales form say about email consent, and is the wording on file? *(owner: sales, plus your privacy owner; re-check this week)*
2. What countries are the 1,400 in? *(owner: you; one CRM export)*
3. Who are the owner and backup of the newsletter, and did the last three issues go out on time? *(owner: you)*
4. How were the other 4,200 subscribers collected, and does each record carry a source tag? *(owner: you)*
5. What are your actual complaint rate and sending-platform limit? *(owner: you; check the provider dashboard)*

**Pass-threshold result:** the plan passes on refusals, gate, signup contract and churn reading. The metric sheet and gate evidence are **blocked** on questions 3, 4 and 5. Re-check after the segment split in section 3.