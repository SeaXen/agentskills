# Marrowgate Developer Newsletter: Template and Ownership

## Part 1: Template

### Rules (apply before filling the template)

- Send monthly, on a fixed day. Pick the first Tuesday.
- Include only items that shipped, changed, or were decided this month. Each item links to its changelog or docs page.
- Fill four sections, in this order: Shipped, Changing, Community, Next.
- Skip any section with no real item. Never pad it.
- Never write generic tips. A "Tip" is allowed only if it comes from a real support ticket or community thread, and you link the source.
- Apply the thin-month rule. If Shipped is empty, either send a short issue with only Changing and Community, or skip the month and say so in the archive.
- Never include billing or security notices. They go through the service-notice channel (Part 2, section 5).
- Write one primary call to action per issue.
- Publish the archive page before you send. The email links to it.

### Issue template

```markdown
---
issue: YYYY-MM
send_date: YYYY-MM-DD
owner: <name>
reviewer: <name>
status: draft | reviewed | sent | skipped
skip_reason: <required if status is skipped>
archive_url: https://<archive-host>/newsletter/YYYY-MM
---

**Subject** (max 60 chars, names the lead item): <Lead item, concrete>
**Preheader** (max 90 chars): <Second most important item>

# Marrowgate Developer Update: <Month YYYY>

<One-sentence intro: the single most important thing this month. No greeting filler.>

## Shipped
<!-- Max 5 items. Omit the section if empty. -->
- **<Feature or fix name>**: <what it does for a pipeline author, one sentence>. [Changelog](<url>) · [Docs](<url>)

## Changing
<!-- Deprecations, breaking changes, behavior changes. Every item has a date. Omit if empty. -->
- **<Change>** — effective <YYYY-MM-DD>. Affects: <who>. Action: <what to do>. [Migration guide](<url>)

## Community
<!-- Max 3 items. Real, linkable, sourced. Omit if empty. -->
- <Community post, plugin, talk, or answered question>. By <name or handle, with consent>. [Link](<url>)

## Next
<!-- Confirmed events and dates only. No roadmap promises. Omit if empty. -->
- <Event or release window>, <date>. [Details](<url>)

---
**Primary CTA:** <one link, one verb>
Read online: <archive_url> · Unsubscribe: {{unsubscribe_url}}
You get this because you subscribed to the Marrowgate developer newsletter.
Account, billing, and security notices are sent separately and are not affected by this subscription.
```

### Pre-send checklist

1. Every item has a link that resolves.
2. Every date in Changing is absolute (`2026-11-04`), never "next week".
3. No billing or security content appears anywhere.
4. The archive page is live and matches the email.
5. A test send passed SPF, DKIM, and DMARC alignment (check the headers).
6. The reviewer signed off in the issue file.

## Part 2: Ownership

### 1. Roles

| Role | Responsibility | Named person |
|---|---|---|
| **Newsletter owner** | Accountable for every issue. Sets the calendar, applies the thin-month rule, and decides to send or skip. | `<name>`, one person |
| **Backup owner** | Takes over during absence. Has full tool and domain access. | `<name>` |
| **Reviewer** | Checks accuracy, links, and dates before sending. Must differ from the author of the issue. | `<name>`, rotating |
| **Content contributors** | Product, docs, and community supply items by the intake deadline. | Each team nominates one contact |
| **Sending-infrastructure owner** | Owns the sending domain, DNS, and email service account (section 3). | `<name>`, an employee in IT/platform |

"The devrel team" is the owning function, not the owner. A named person is accountable.

### 2. Calendar

- **T-10 working days:** Owner opens the issue file and requests items.
- **T-5:** Intake closes. Owner applies the thin-month rule and records the decision.
- **T-3:** Draft complete.
- **T-2:** Reviewer signs off.
- **T-0:** Send, then publish or confirm the archive page.
- **T+5:** Owner records opens, clicks, and unsubscribes in the issue file and notes one thing to change.

### 3. Sending domain and infrastructure

⚠️ **Open risk: the sending domain is registered on an ex-contractor's registrar account.** The company cannot prove ownership, change DNS, renew the domain, or recover it if that person is unreachable. Anyone who controls that account can send as Marrowgate or break delivery.

Treat this as a blocker for formalising the newsletter. Do these steps in order:

1. Identify the registrar and the account holder. Ask the ex-contractor for an authorisation code and an account-push, or for the registrar's transfer process.
2. Transfer the domain into a company-owned registrar account. Use a shared role address and two named admins, not a personal email. Enable MFA and registrar lock.
3. Turn on auto-renew. Put the renewal date in the shared calendar with a 60-day reminder.
4. Rotate all credentials the contractor could hold: registrar, DNS host, and email service provider (ESP). Remove their access.
5. Verify SPF, DKIM, and DMARC after the transfer, and publish DMARC at `p=quarantine` or stricter once reports are clean.
6. Record the registrar, DNS host, ESP account, admins, and renewal date in the internal runbook.

If the contractor is unreachable, escalate to the registrar's dispute process and send the newsletter from a new, company-owned subdomain in the meantime.

Ongoing rules:

- Put the newsletter on its own subdomain, such as `news.<company-domain>`. This isolates its reputation from the product's other mail.
- Keep the sending-infrastructure owner and the backup as the only admins.
- Review access every quarter and on every departure of anyone with access.

### 4. Archive

- Publish every issue at a permanent URL (`/newsletter/YYYY-MM`) before sending. Include skipped months with a one-line reason.
- Keep issues public and indexable, with no tracking parameters in archived links.
- Never edit a sent issue silently. Mark corrections with a dated note at the top.
- The owner stores the source file (the issue template, filled in) in the docs repo.
- Redirect, never delete, any URL that has been sent.

### 5. Billing and security notices

Do not send these through the newsletter. They have a different audience, a different legal basis, and different failure costs.

- **Audience:** Newsletter subscribers are not the same people as account billing and security contacts.
- **Unsubscribes:** A subscriber who unsubscribes from the newsletter must not lose a security notice. Billing and security notices also must not depend on newsletter opt-in.
- **Trust:** A security notice inside a marketing email trains readers to ignore both. It also looks like phishing.

| Notice type | Channel | Owner | Sender |
|---|---|---|---|
| Billing (invoices, price changes, failed payments) | Transactional | Finance, with support | Billing address on the transactional subdomain |
| Security (advisories, incidents, key rotation) | Transactional plus the status page | Security lead | Security address on the transactional subdomain |
| Product breaking changes | Newsletter **Changing** section, plus in-product and docs notice | Newsletter owner | Newsletter sender |

If a deprecation also affects billing or security, the newsletter may link to the official notice. It must not replace it.

### 6. Decisions and escalation

- **Send or skip:** The owner decides at T-5 and records the reason in the issue file.
- **Disputed content:** The owner decides. Anything about security or pricing needs sign-off from its owner (security lead, finance) before inclusion.
- **Errors after sending:** Publish a dated correction in the archive. Send a follow-up only if the error could cause harm, such as a wrong deprecation date.
- **Owner leaves or changes role:** The backup takes over the same day. Handover covers the issue files, ESP access, and domain admin status. Revoke the departing owner's access in the same week.

### 7. Review

- Review the newsletter every quarter. Check three things: whether the owner's slot is staffed, whether the domain and renewal dates are in order, and whether any month was skipped or padded.
- Cut a section if it was empty in 3 of the last 6 issues.

## Notes and assumptions

- I did not inspect your DNS, registrar, or ESP, so the domain steps assume the ex-contractor still holds the account. Confirm who the registrant is with a WHOIS lookup and your registrar.
- Names, hostnames, and the first-Tuesday send day are placeholders to replace.
- I cut the nine sections to four. I had no data on which sections your readers use. Check per-section clicks from the past year before you finalise the cut.
- I did not read anything under `skill-wip/`, as you asked.