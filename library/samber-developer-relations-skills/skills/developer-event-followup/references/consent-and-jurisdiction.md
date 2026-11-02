# Consent and jurisdiction

Contents: gate table → rules by jurisdiction → purpose-limitation cases → deliverability limits.

This page frames the questions for the user's privacy owner. It is not legal advice, and regulator guidance changes: confirm the current text before relying on any row.

## Gate table

Fill one row per record source. The last column decides which tracks in SKILL.md are open.

| Source                  | What the attendee heard or read                                                                                         | Jurisdiction        | Requested reply allowed?        | Marketing allowed?                                           |
| ----------------------- | ----------------------------------------------------------------------------------------------------------------------- | ------------------- | ------------------------------- | ------------------------------------------------------------ |
| graded conversation log | "I'll send the config, check in after you've tried it, and add you to our monthly release notes - unsubscribe any time" | UK, limited company | yes                             | yes, objection link in every message                         |
| scanner export          | scanner screen said "scan to receive our updates"                                                                       | Germany             | yes, if something was requested | no, without a consent you can show                           |
| raffle entries          | form said "entry only puts you in the draw"                                                                             | France              | no request was made             | no                                                           |
| organizer-supplied list | organizer's notice: "shared with sponsors for product updates"                                                          | US                  | nothing was requested           | yes, within that notice; CAN-SPAM opt-out and postal address |
| organizer-supplied list | organizer's notice: "shared with sponsors for product updates"                                                          | EU or UK            | nothing was requested           | no, unless the consent named your company                    |
| sign-up sheet           | header said "get the workshop materials"                                                                                | Canada              | yes                             | only if relevant to their role (see Canada)                  |

Rules for filling it:

- Copy the purpose line exactly. When nobody can say what staff said, treat the purpose as "none stated" and open no marketing track.
- One record can carry two sources (scanned and entered the draw). Judge each message against the source that covers it; a separately ticked opt-in counts on its own, and a draw entry without the tick widens nothing.
- A jurisdiction missing from the table below: treat it as prior-consent until the privacy owner names its rule.
- Note the date of capture: the record proves the basis later.

## Rules by jurisdiction

| Regime                         | Marketing email to a person met at the event                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       | Badge scan alone enough?                                                              |
| ------------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------- |
| EU, ePrivacy art. 13           | Unsolicited marketing email to individuals needs prior consent. The EDPB's legitimate-interest guidelines (1/2024, consultation version of October 2024, para 114) say this rules out GDPR legitimate interest as the basis for it. Soft opt-in (art. 13(2)) covers only contacts obtained from customers in the context of a sale, for your own similar products, with an opt-out at collection and in every message. Member states apply the email rule to company addresses differently.                                                                                                                                        | no                                                                                    |
| EU, soft opt-in after a signup | The CJEU (C-654/23, Inteligo Media, 13 November 2025) accepted that a free account can count as a sale of a service where it is tied to a paid offering, read the exception narrowly, and treated informational newsletters as direct marketing.                                                                                                                                                                                                                                                                                                                                                                                   | a free-tier signup at the booth may open it; a scan does not                          |
| UK, PECR and UK GDPR           | The PECR email rule does not apply to corporate subscribers (limited companies); sole traders and some partnerships need consent or soft opt-in. Soft opt-in needs selling or negotiating: a free-trial signup or a quote request counts, browsing does not. UK GDPR transparency still applies, and the right to object is absolute. Keep a business do-not-email list. When you cannot tell whether an address is corporate, treat it as an individual subscriber (consent or soft opt-in); a delegate who gave a personal address is one. The ICO marks this guidance as under review after the Data (Use and Access) Act 2025. | yes for corporate addresses, with a privacy notice                                    |
| France, CNIL                   | Business prospecting on legitimate interest, without prior consent, when the message relates to the person's profession, they were informed at collection, and objecting is simple. Generic addresses (contact@, info@) fall outside these rules.                                                                                                                                                                                                                                                                                                                                                                                  | only if informed at collection                                                        |
| Germany, UWG s.7               | Email advertising needs prior express consent, business recipients included. The existing-customer exception (s.7(3)) needs a sale. A scanned trade-fair badge is not consent. The accepted proof of consent is double opt-in: one confirmation email free of advertising, then a logged click.                                                                                                                                                                                                                                                                                                                                    | no                                                                                    |
| US, CAN-SPAM                   | Opt-out regime with no business exception: accurate headers, a working opt-out for at least 30 days after sending, opt-outs honoured within 10 business days, and a valid postal address in every commercial message.                                                                                                                                                                                                                                                                                                                                                                                                              | yes, if compliant                                                                     |
| Canada, CASL s.10(9)(c)        | Implied consent when the person disclosed the address to you, did not say they refuse messages, and the message is relevant to their business role. This route has no statutory expiry. The two-year (purchase, contract) and six-month (inquiry, application) windows in s.10(10) belong to existing business relationships, not to a handed-over card.                                                                                                                                                                                                                                                                           | a card or an attendee-initiated request: yes; an exhibitor-initiated scan is untested |

Myths to correct when the user repeats them:

- "Business cards are good for six months under CASL" - the six-month window is for inquiries; disclosure-based consent has no fixed expiry, though it lapses if the message stops being relevant to the role.
- "B2B is exempt from consent everywhere" - Germany says otherwise, and the EU rule depends on the member state.
- "The organizer's registration consent covers us" - it covers the organizer sharing data with you for what its notice said; your messages need your own basis.

## Purpose-limitation cases

Each purpose needs its own basis, identified at collection and told to the person (EDPB 1/2024, para 10). What staff said at the booth is the purpose.

```
// ✓ Good - stays inside "send the config and check in"
Subject: The Terraform config from the booth
Hi Ana, here is the module we sketched for your staging refresh, plus the event credit.
I'll check in next Thursday to see if it ran.

// ✗ Bad - same record, new purpose nobody heard at the booth
Subject: Welcome to the Acme newsletter!
You're now subscribed to monthly product news...
```

```
// ✗ Bad - raffle entry reused
"Thanks for entering our draw! Here's 20% off Acme Pro."
// The draw form said entry only puts you in the draw. The ICO: prize-draw consent "can't be carried over for anything else".
```

## Deliverability limits

- Google: keep the Postmaster spam rate below 0.10% and never reach 0.30%. Bulk-sender rules apply above 5,000 messages a day to Gmail addresses. Postmaster reports personal Gmail only, so complaints from developers on company domains stay invisible there; watch your sending platform's complaint feed too.
- Yahoo: keep the spam rate below 0.3%.
- One event batch sent to every scan can move a domain's complaint rate for every campaign after it.
