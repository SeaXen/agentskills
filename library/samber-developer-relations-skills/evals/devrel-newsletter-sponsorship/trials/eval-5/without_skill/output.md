# Setting up the Nimbit sponsored send for Corvane Builders

## Bottom line

- Marketing's "partner, not advertiser" argument doesn't hold. Regulators and the law look at who benefits, whether Corvane is paid, and what the recipients agreed to. Nimbit paying to reach your list makes it a paid promotion either way.
- **Send the email: yes, with conditions.** Corvane sends it from its own domain, it is about the Corvane x Nimbit integration, and it is clearly labeled as a partnership.
- **Hand over the CSV of clicking companies: not as asked.** This is the real risk. Use an opt-in landing page instead (option B below).
- This is not legal advice. Have your DPO or counsel review the final design before anything is sent. The review should be short because the design below is conservative.

## Why the CSV is the problem

- A click is personal data, and a company name next to a click usually identifies a person. At a 3-person company, or with a `@gmail.com` address, it identifies exactly one individual.
- Giving it to Nimbit's SDRs means Corvane discloses personal data to a new controller. Nimbit's outreach is then Nimbit's own marketing.
- Your list was collected for Corvane's newsletter and docs updates. Passing click data to a third party for sales follow-up is a different purpose. It would need its own legal basis and disclosure in your privacy notice.
- Germany is strictest. Advertising email generally needs consent, including B2B, and tracking pixels or links need care.
- The UK treats sole traders and partnerships as individuals who need consent.
- France allows more B2B latitude, but only for messages relevant to the recipient's job and with a clear opt-out at collection.
- The US (CAN-SPAM) needs no consent, but requires honest sender identity, an unsubscribe, and a postal address. Paid placements should also be disclosed.

## What Nimbit can get

| Option | What Nimbit receives | Verdict |
|---|---|---|
| A. Aggregate report | Sends, unique clicks, click-through rate by region, no names | Safe. Offer it as the default. |
| **B. Opt-in handoff** (recommended) | Only people who click, land on a Corvane-hosted page, and tick an unticked box naming Nimbit | Best fit for SDR follow-up. These are real leads. |
| C. Company-level list | Domains with at least 5 distinct clickers, free-mail domains excluded, no individuals | Gray zone. Needs a documented legitimate-interest assessment and a privacy-notice update. Exclude Germany and UK sole traders. Use it only if Nimbit rejects B. |
| D. Full click-level CSV | Names, emails, companies | Don't do this without separate consent from each person. |

**How option B works:**

1. The email's CTA goes to a Corvane page such as "Get the Nimbit integration guide / talk to the Nimbit team".
2. The page has a form, plus an unticked checkbox: "Share my name, work email and company with Nimbit so they can contact me about this integration. Privacy notice: [Nimbit link]."
3. Only people who submit with the box ticked go to Nimbit, with the timestamp and the consent text they saw.
4. Everyone else stays anonymous and appears only in aggregate numbers.
5. Nimbit's first email to each lead links to its own privacy notice and offers an opt-out.

## Setup steps

1. **Audit consent (before agreeing to anything).**
   - Pull the exact signup and docs-subscription wording for each source.
   - Pull the consent logs by country.
   - Find out whether anyone is on the list only through the product signup, with no explicit marketing opt-in.
2. **Segment the 26,000 by country and basis.**
   - **Germany:** send only to people with documented double opt-in for marketing email.
   - **UK:** send to individuals with consent. Corporate addresses are lower risk, but sole traders count as individuals.
   - **France and US:** send with the standard unsubscribe and sender requirements.
   - Expect the sendable audience to be smaller than 26,000. Tell Nimbit the delivered count up front, and price per delivered email or per qualified lead, not per list size.
3. **Write the email as Corvane content.**
   - It is from Corvane, about the integration as a Corvane feature, and shows Corvane's postal address.
   - Put a visible label in the header, for example "Sponsored by Nimbit" or "In partnership with Nimbit". Don't disguise it as editorial content.
   - The subject line must not mislead.
   - Corvane keeps editorial control, and Nimbit approves factual claims only.
4. **Add the technical requirements.**
   - One-click unsubscribe (RFC 8058) and a working List-Unsubscribe header. Gmail and Yahoo require both for bulk senders.
   - Suppress everyone who unsubscribed from Corvane Builders.
   - Judge success on clicks and form submissions. Open rates are unreliable because of Apple Mail Privacy Protection.
   - Use UTM-tagged links, so Nimbit can track conversions on its own site without personal data from you.
5. **Update your privacy notice before the send.**
   - Name the purposes: partner announcements and click measurement.
   - Name the recipient category: integration partners, when the person opts in.
6. **Decide on warming and frequency.**
   - This is an extra send beyond the monthly. A cold dedicated send to 26,000 people risks spam complaints and domain reputation.
   - Send it to engaged subscribers first, and stagger the rest over a few days.
   - Consider a "partner announcements" option in your preference center.
7. **Sign a sponsorship agreement with Nimbit.** It should cover:
   - Corvane keeps the list. There is no list rental, and Nimbit never receives addresses except through option B.
   - The deliverables are one send, the agreed segment, and the reporting you offer (option A numbers plus option B leads).
   - Nimbit may use B-leads only for the integration topic. It must honor opt-outs and name its own lawful basis.
   - It includes a controller-to-controller data-sharing clause and mutual indemnities for the content claims each side supplies.
   - It sets payment terms and a cancel-if-not-compliant right.
8. **Do a test send and check:**
   - the sponsor label renders correctly in the major clients
   - the unsubscribe works
   - the consent box is unticked
   - the form posts to your system, not directly to Nimbit's CRM

## What to tell marketing

- "Partner" is not a legal category for email. What counts is who is promoted, who is paid, and what recipients consented to.
- The send is fine as a labeled, Corvane-sent announcement to the right segments.
- The click-level CSV is what exposes Corvane to fines, complaints and loss of subscriber trust. The opt-in page gets Nimbit better leads anyway, since the people on it asked to be contacted.

## Open questions to settle first

- What consent wording did signups and docs subscribers see? This decides the Germany and UK segments.
- How many of the 26,000 are in each country, and how many have explicit marketing opt-in?
- Does Nimbit accept option B, or does it insist on company lists? If it insists, option C needs a documented legitimate-interest assessment and counsel's sign-off.
- Is the fee flat, or tied to leads? A per-lead fee creates pressure to loosen the consent rules, so a flat fee plus a per-qualified-lead bonus is safer.

**Next action:** pull the signup consent text and the per-country list counts. Everything else depends on those two numbers.