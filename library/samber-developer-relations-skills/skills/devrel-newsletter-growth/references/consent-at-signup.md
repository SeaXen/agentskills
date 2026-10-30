# Consent when adding subscribers

Read this before changing a form, importing any list, or adding a co-registration or paid network. This is not legal advice: send the final call on any segment to whoever owns privacy.

## Contents

1. Rules per regime
2. Imports, events and partners
3. The consent record and the confirmation email
4. Good and bad form copy

## 1. Rules per regime

| Regime | Consent needed for newsletter email? | Who proves it, and how | Pre-ticked box | Bundled with terms, account or ticket | Lists from third parties |
|---|---|---|---|---|---|
| EU GDPR with ePrivacy | Yes for individuals, unless a soft opt-in applies. Business addresses vary by member state: consent in Germany, opt-out allowed for job-relevant B2B mail in France | The sender (GDPR Art. 7(1)) | Invalid | Presumed not freely given; separate purposes need separate consents | Every organisation relying on the consent must be named |
| UK PECR with UK GDPR | Yes for individual subscribers, including sole traders and partnerships outside Scotland. Corporate subscribers (limited companies, LLPs, government bodies) are exempt from the consent rule but still get sender identity and an opt-out | The sender; record who, when and how | Invalid, as are silence and inactivity | Consent as a condition of buying is unlikely to be valid | Consent must name your organisation, not "trusted partners"; no third-party list satisfies the soft opt-in |
| US CAN-SPAM | No: opt-out regime | n/a | n/a | Not prohibited | Opted-out addresses cannot be sold or transferred; honour opt-outs within 10 business days; postal address and honest headers |
| Canada CASL | Yes, express or implied. Implied routes: a published business address, or an address the person disclosed to you (a booth scan can qualify), each with a role-relevant message and no stated refusal; or an existing business relationship (two years after a purchase, six months after an inquiry) | The sender; keep records of consent, method and unsubscribes | Not accepted as express consent | The request must be separately identifiable | Treat as no consent unless it names you |
| Germany (UWG s.7 with GDPR) | Yes, prior express consent, in practice also for business addresses. The existing-customer exception needs a sale, similar own products, and notice at collection and in every message: free and trial signups rarely qualify | The sender. Courts accept a confirmed (double) opt-in as proof; testimony that the sender uses double opt-in in general does not prove one subscriber's consent | Invalid | As GDPR | Consent must name the sender |

A regional German court held that even a neutral confirmation email can be unlawful when someone else entered the address. Keep the confirmation minimal and block bot and third-party submissions with the guard in the signup contract.

## 2. Imports, events and partners

| Source | Can it join the newsletter? | Do instead |
|---|---|---|
| Product accounts, trial users, customers | House rule: not by import. A UK or EU soft opt-in offered at signup (tied to a sale or its negotiation; whether a free account counts is contested), or US addresses under opt-out rules, may be lawful: the privacy owner decides that segment, and it joins after one notice with an opt-out | One in-product invite with an unticked box |
| Event registrants where you organised the event | Only those who ticked a separate, unticked newsletter box at registration | Add the box to the next registration form |
| Sponsor badge scans, attendee lists from an organiser | No in the EU, UK, Germany or Canada unless the attendee consented to your named organisation for email | Booth sign or talk end card with the signup link |
| A segment with no consent record | No. A "would you like to subscribe?" email to it is itself marketing in the UK and EU | Suppress it; reach users in the product |
| Co-registration ("also subscribe me to partner newsletters") | Only with an unticked, per-newsletter, named choice | Check that your platform's recommendation widget works this way |
| Referral or recommendation network signups | Yes, when the network collected a named, unticked choice for your newsletter | Read the network's consent text before paying |
| Bought or rented lists, scraped commit or profile emails | No | Nothing |

## 3. The consent record and the confirmation email

Store per subscriber:

- timestamp of the form submission and of the confirmation click
- source tag and form version
- the exact consent text shown
- the IP address, if your privacy notice covers it

Confirmation email: one sentence on what they asked for, the confirm button, and nothing else. No promotion, no sponsor, no product pitch.

## 4. Good and bad form copy

```
✓ Good - separate choice, states what arrives and who sends it, unticked
[ ] Send me the Acme developer newsletter: one email a month on releases and
    deprecations. Unsubscribe from any issue. Privacy notice.

✗ Bad - bundled into terms, pre-ticked
[x] I agree to the Terms of Service and to receive product updates.

✗ Bad - verification doubles as subscription
"Click to verify your account. Verifying also subscribes you to our newsletter."
```
