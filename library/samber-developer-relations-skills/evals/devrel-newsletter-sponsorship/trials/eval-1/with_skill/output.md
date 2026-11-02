# Pulse Weekly: Quillstack sponsor block

**Answer:** I can write the block, but not as they asked. "Presented by Quillstack" and "Thanks to our friends at Quillstack" can't be the label, and "Quillstack x Pulse Weekly" can't go in the subject line. The block below keeps their logo and their thank-you line. It adds a plain "AD · ANZEIGE" label above both. I applied the skill's label rules. Its references say this is not legal advice. Send anything you are unsure about to counsel.

## Refused asks

| Ask | Basis | What they get instead |
|---|---|---|
| "Presented by Quillstack" + logo as the header | Regulator guidance (US, UK) and German case law: it reads as funding, not advertising. About 40% of your readers are in Germany, where "Anzeige" is the expected word. | `AD · ANZEIGE` as the header. The logo sits under it. |
| "Thanks to our friends at…" as the only identifier | Same. The line is fine beside the label, never in place of it. | Kept verbatim, below the label. |
| "Quillstack x Pulse Weekly" in the subject line | Trust and law. A sponsor name in a normal issue's subject can turn the whole issue into commercial email (US). German rules also forbid hiding commercial character in the subject or header. | Normal editorial subject. They get their name and logo in the labelled unit, plus the click report. |

A dedicated send that names the sponsor in the subject would need a separate opt-in list for partner offers. Your readers signed up for "the newsletter", so that route is closed.

## The final block

Label first, in all three formats. The wording is identical everywhere, so the copy is the only variable.

### 1. Email (HTML part)

```html
<table role="presentation" width="100%" style="border:1px solid #d0d0d0; padding:16px;">
  <tr><td style="font-size:14px; font-weight:bold; letter-spacing:1px;">
    AD · ANZEIGE
  </td></tr>
  <tr><td style="padding-top:8px;">
    <a href="https://QUILLSTACK-DOMAIN/?utm_source=pulse-weekly&utm_medium=newsletter">
      <img src="QUILLSTACK-LOGO-URL" alt="Quillstack (Ad)" height="40">
    </a>
  </td></tr>
  <tr><td style="padding-top:8px; font-size:14px;">
    Thanks to our friends at Quillstack for supporting the community.
  </td></tr>
  <tr><td style="padding-top:8px; font-size:16px;">
    [QUILLSTACK-APPROVED COPY, within the slot word limit]
    <a href="https://QUILLSTACK-DOMAIN/?utm_source=pulse-weekly&utm_medium=newsletter">[link text]</a>
  </td></tr>
</table>
```

Notes:
- The label is readable body-size type, not grey fine print.
- There is one link, to Quillstack's own domain. The logo and the copy link point to the same URL.
- The logo's alt text carries "Ad", so image-blocking clients still show the label.

### 2. Plain-text part

```
AD · ANZEIGE
Quillstack
Thanks to our friends at Quillstack for supporting the community.

[QUILLSTACK-APPROVED COPY]
https://QUILLSTACK-DOMAIN/?utm_source=pulse-weekly&utm_medium=newsletter
```

The logo can't render here, so the name line stands in for it. The label still comes before any copy.

### 3. Web archive

Same HTML as the email, with one change: the link carries `rel="sponsored"`.

```html
<a href="https://QUILLSTACK-DOMAIN/?utm_source=pulse-weekly&utm_medium=newsletter" rel="sponsored">
```

Apply it to the logo link and the copy link. Search engines then don't read them as editorial links. Keep the label in the archive page itself, not only in an image.

## Subject line and preheader

- Subject: a normal editorial subject, for example `Pulse Weekly #NN: <lead story>`. No Quillstack name.
- Preheader: also no Quillstack, for the same reason.

## Before this goes out

These are the gaps I can't close from what you told me:

1. **Readers told (blocking).** Does your signup form or privacy notice say issues carry labelled sponsor content? Your first sponsor means the list has never seen this.
   - If not, update the signup text.
   - Announce sponsor content in an issue before the Quillstack issue, with the unsubscribe link prominent.
   - This blocks the sale until done.
2. **Measured engagement (unverified).** The gate needs six issues of per-link human clicks with a named bot-click filter. Without them, treat this as a pilot booking at the cost-recovery floor and tell Quillstack in writing what evidence is missing.
3. **Seller and invoicing entity (unverified).** You need a named person for copy approval and reports, and an entity that invoices.
4. **Copy and link.** I did not write Quillstack's promotional copy. They supply it. You may require edits or reject it, with a reason, up to the copy deadline. It needs one link, to their own domain.
5. **Editorial pieces.** The sponsor sees only their own unit before send. No review, mention or news-section coverage comes with the slot.

## Suggested reply to Quillstack

> Thanks for the block. Here is how we run every sponsor unit: a plain "AD · ANZEIGE" label sits above the logo, because roughly 40% of our readers are in Germany. Your logo and your thank-you line stay exactly as you wrote them, directly under it. We can't use "Presented by" as the label, and we keep sponsor names out of subject lines for all issues. Your unit, link and logo are visible in the email, the plain-text version and the web archive. After the issue you'll get a report: delivered count and unique human clicks, with the bot-click filter named.

## Report to send Quillstack within a week

```
Issue: #NN, sent [date] to [delivered count] delivered addresses
Slot: primary, position [n], label "AD · ANZEIGE"
Link: https://QUILLSTACK-DOMAIN/?utm_source=pulse-weekly&utm_medium=newsletter
Unique human clicks: [n]  (filter: [name the platform's bot-click filter and settings])
Total clicks recorded: [n] (before filtering)
Opens: directional only, inflated by mail-privacy features; not reported as reach
What we need back: signups or trials you attributed to this link
```

No subscriber names, emails or company names go in the report.

## Pass-threshold result

| Threshold | Result |
|---|---|
| Label before copy, in HTML, plain text and archive, with "Anzeige" for German readers | pass |
| Refused asks name their basis | pass |
| Report names the filter, no subscriber identities | pass |
| Gate with evidence for all four conditions | **blocked**: you must supply the click data, the signup wording and the seller (owner: you) |
| Price traced to floor, band and measured clicks | **blocked**: you didn't give a price, and I can't set one without your click data |
| Terms: copy deadline, edit rights, cancellation, pause clause, make-good, payment | **blocked**: none were discussed. Confirm them in writing before the invoice (checklist in `references/terms-and-reporting.md`) |