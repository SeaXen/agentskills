**Verdict: don't switch platforms yet. Switching probably won't fix this, and it costs a month.**

**Next action (about 30 minutes):** Get one bounced or quarantined message from a bank reader. Ask their IT team for the full headers, or the quarantine reason code. Everything below depends on that evidence.

**Why the data points away from the platform**

- **0.04% spam rate in Postmaster Tools.** This is Google's view only. It says nothing about Microsoft 365, Proofpoint, Mimecast or Barracuda. Those filters protect banks and Fortune 500s.
- **DMARC passes.** That proves authentication, not reputation or content. Enterprise gateways add checks Gmail doesn't make.
- **Gmail is fine and enterprise is not.** The split follows the receiving filter, not your sending platform. A new platform sends through the same kind of shared IPs, to the same filters.

**Likely causes, most likely first**

1. **Link tracking and redirect domains.** Gateways rewrite or detonate links. A shared tracking domain from the platform often has poor reputation. Fix: set up a custom branded tracking domain.
2. **Content signals.** Many links, image-heavy layout, URL shorteners, and attachments all raise filter scores. Newsletters also trigger "bulk" classification by design.
3. **Missing or inconsistent `List-Unsubscribe` and `List-Unsubscribe-Post` headers.** These matter for bulk mail.
4. **Shared IP reputation.** This is the one real platform issue. Check whether your IP is shared, and check your sending history on Microsoft's side.
5. **Sending-domain age or volume spikes.** Low or uneven volume to Microsoft domains gives them little reputation to judge you on.
6. **Admin policy at the reader's company.** Some banks quarantine all external bulk mail by default. No platform change fixes that. Only allowlisting does.

**Checks to run (all free)**

1. Read the headers of a Microsoft 365 test delivery. Look for `X-Forefront-Antispam-Report`, the `SCL` value, and `X-MS-Exchange-Organization-SCL`.
2. Sign up for Microsoft SNDS and JMRP. These show reputation for Outlook.com and Microsoft 365 senders.
3. Check your sending IP and domain on MXToolbox, Talos Intelligence, and Spamhaus.
4. Send a test to mail-tester.com and a Microsoft 365 test inbox. Compare the scores.
5. Confirm SPF, DKIM, and DMARC all align with your visible From domain. Check the platform doesn't sign with its own domain only.

**Fixes to try before migrating**

- Custom tracking and link domain on your own subdomain.
- Dedicated IP, only if your volume supports it. Low volume on a dedicated IP hurts.
- Plain-text-friendly layout, fewer links, no shorteners.
- Ask engaged enterprise readers to allowlist your sending domain and IP. Give them a one-paragraph note to forward to IT.
- Offer a plain-text or web-archive version for readers behind strict gateways.
- Ask the platform's support for deliverability data on Microsoft domains. A good vendor can show it.

**When migrating is justified**

- Your headers show the platform's shared IP or tracking domain is blocklisted.
- The vendor can't or won't give you a custom domain, a dedicated IP, or Microsoft-side data.
- You've fixed the items above and enterprise delivery stays bad for 4 to 6 weeks.

**What to tell the CEO**

"Gmail reputation is healthy, so the platform isn't the proven cause. Enterprise filters judge differently. I'll have evidence from real headers in a week. If the platform is the cause, we migrate with a reason. If not, a migration costs a month and leaves the problem in place."

**Time estimate:** About 1 hour to gather headers and run the checks. 1 to 2 days to set up the custom tracking domain. 1 to 2 weeks to see if enterprise delivery improves.

Next: ask one bank reader for the quarantine reason or full headers today.