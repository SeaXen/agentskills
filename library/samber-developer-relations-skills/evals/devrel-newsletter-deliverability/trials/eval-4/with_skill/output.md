# Corvane DMARC plan review: `v=DMARC1; p=reject; pct=10` on corvane.com

## Direct answer

No, your worry is justified. Do not publish `p=reject; pct=10` next Monday. Publish `v=DMARC1; p=none; rua=mailto:<reports mailbox>` on Monday instead. Enforce only after the reports show every sender aligned. The security team's goal of reaching reject is right, but the route skips the monitoring and inventory steps.

Two things are wrong with the plan:

1. **It starts at `p=reject` with no data.** You have no DMARC record and no reports, so nobody knows which systems send as corvane.com or which pass alignment. Zendesk, the billing system and Greenhouse are the likeliest to fail. Once enforced, their mail bounces or is dropped: invoices, support replies and candidate emails.
2. **`pct` is not a safe ramp.** RFC 9989 (May 2026) removed `pct`, because receivers applied in-between values inconsistently. Receivers still on the old RFC 7489 may apply 10%. Receivers on the new RFC ignore it and may apply `reject` to 100% of failing mail from day one. You cannot predict which receiver does which, so "10% this week" is not a promise.

The newsletter is probably not the first thing to break. The risk is that the newsletter is the one sender you can verify cheaply, and the other four are unknown.

## Evidence table

I have not seen any headers, DNS or reports, so most steps are unverified. Unverified is not passed.

| Step | Check | Result | Source |
|---|---|---|---|
| 1 Delivery state | Raw SMTP replies | **Unverified.** No bounce log seen. | - |
| 2 Authentication | Newsletter issue shows `dkim=pass` with `d=` on corvane.com and `dmarc=pass` | **Unverified.** You don't know whether the platform signs as corvane.com or with its own domain. | - |
| 2 One-click | `List-Unsubscribe` and `List-Unsubscribe-Post` present and DKIM-signed | **Unverified.** | - |
| 3 Listings | Spamhaus domain lookup | **Unverified.** | - |
| 4 Complaints | Gmail spam rate in Postmaster Tools | **Unverified.** | - |
| 5 Events | Planned DMARC change on Monday | An upcoming event, not yet a problem. | You |
| 6 Content | Not reached | Steps 2 and 4 are open. | - |
| Plan | Misreads table | Two rows apply: `p=reject` on the root domain this week, and a `pct` ramp. | Plan text |

## Causes ranked: what the plan would break

1. **Unknown third-party senders fail alignment under `reject`.** This hits Zendesk, billing and Greenhouse.
   - Each tool has to sign with a DKIM key on corvane.com, or use a return path on corvane.com for SPF.
   - Many tools send from their own domain by default, so DMARC fails.
2. **Newsletter alignment is unknown.** If the platform signs with its own domain, every issue fails DMARC.
   - Gmail already requires bulk senders to publish DMARC at least at `p=none`, and rejects mail without it with `5.7.40`.
   - Staff mail also counts toward Gmail's volume for corvane.com, so the whole domain has to qualify, not just the newsletter.
3. **Google Workspace staff mail.** Check that DKIM signing is actually switched on for corvane.com.
4. **Forwarded mail.** Forwarding lists, aliases and gateways can break DKIM and SPF.
   - Under `p=reject`, those copies can be lost.
   - This is the accepted cost of enforcement, but you should know it going in.
5. **SPF lookup limit.** Adding includes for five senders can push the SPF record past 10 DNS lookups. That gives `permerror` and breaks every sender, including staff mail.

## Fix plan

Order: stop the harm, then repair authentication, then enforce.

| # | Fix | Owner | Date | Done when |
|---|---|---|---|---|
| 1 | Replace Monday's record with `v=DMARC1; p=none; rua=mailto:<mailbox or report processor>`. Do not publish `pct`. | Security team, DNS owner | Mon 2 Nov 2026 | `dig +short TXT _dmarc.corvane.com` returns the record. |
| 2 | Check a newsletter issue's raw headers at a Gmail, an Outlook.com and a Yahoo address. Look at `Authentication-Results`. | You (DevRel) | Tue 3 Nov | You have a screenshot or text of `dkim=`, `spf=` and `dmarc=` for each. |
| 3 | If `d=` is the platform's domain, publish the platform's custom DKIM and return-path records for the sending domain. Keep the `From:` unchanged. | DNS owner, you | Fri 6 Nov | A seed issue shows `dkim=pass` with `d=` on corvane.com and `dmarc=pass`. |
| 4 | Verify the sending domain in Gmail Postmaster Tools. | You | Tue 3 Nov | Spam rate is visible, target under 0.1%. |
| 5 | Check the one-click headers. A GET on the unsubscribe URL must not unsubscribe a seed address. A POST must. | You | Fri 6 Nov | Both headers are present and DKIM-signed. The GET test leaves the seed subscribed. A 2xx response to POST unsubscribes it. |
| 6 | Read the aggregate reports for 2 to 4 weeks. Build an inventory of every source: Workspace, newsletter, Zendesk, billing, Greenhouse, plus anything the reports reveal. | Security team, you | Mon 30 Nov | Every source is listed with an owner and a pass/fail status. |
| 7 | Align each failing source with custom DKIM or a delegated subdomain, or retire it. | Each tool's owner | Mon 14 Dec | Reports show only aligned sources. |
| 8 | Move the newsletter to a subdomain, for example `news.corvane.com`, with its own warm-up of about six weeks. | DNS owner, you | Q1 2027 | The subdomain is aligned and reported separately. |
| 9 | Enforce the newsletter subdomain first with `_dmarc.news.corvane.com`: `p=quarantine; pct=0; t=y`, then `p=reject; pct=0; t=y`, then `p=reject`. | Security team | After step 8 | Reports show only the platform sending. |
| 10 | Enforce corvane.com the same way, last. | Security team | After step 7, earliest January 2027 | Zero legitimate failures for a full reporting cycle. |

Notes on the ramp:

- **`t=y` replaces the `pct` ramp.** `t=y` is an on/off test flag, not a percentage. Both `t=y` and `pct=0` mean "apply one level lower", so old and new receivers behave the same. That makes each rehearsal predictable.
- **Skipping the subdomain.** If you can't move the newsletter to a subdomain, skip steps 8 and 9. Run the same ladder directly on corvane.com. It's safe only after step 7.
- **Dates.** Treat dates after step 5 as proposals. The reports decide when you move on.

## Monitoring sheet

| Signal | Source | Alert level | Owner |
|---|---|---|---|
| DMARC pass rate per source | Aggregate reports (`rua`) | Any legitimate source below 100% blocks the next step | Security team |
| New unknown sender in reports | Aggregate reports | Any new source triggers an owner check | Security team |
| Gmail spam rate | Postmaster Tools | 0.1% investigate, 0.3% stop | You |
| `4.7.x` and `5.7.x` counts per send | Platform bounce log | Any, especially `5.7.26`, `5.7.40` or `4.7.32` | You |
| SPF lookup count | DNS check after each change | Above 10 lookups | DNS owner |
| User-unknown share per send | Platform bounce log | About 2% (house rule) | You |

## Pass-threshold status

| Threshold | Status |
|---|---|
| Claims checked against the misreads table | **Passed.** Two rows apply. |
| Each triage step has a verdict or is marked unverified | **Passed.** |
| Received issue shows `dkim=pass` on your domain and `dmarc=pass` | **Blocked.** Missing: raw headers of a received issue. Owner: you. Re-check Tue 3 Nov. |
| One-click headers present, signed, GET doesn't unsubscribe | **Blocked.** Missing: a seed test. Owner: you. Re-check Fri 6 Nov. |
| Gmail spam rate read from Postmaster Tools | **Blocked.** Missing: domain verification. Owner: you. Re-check Tue 3 Nov. |
| Suppression rules distinguish dead addresses from policy blocks | **Not applicable yet.** No suppression change proposed. |
| Every fix row has an owner, a date and a done-when | **Passed.** |
| No open rate used as placement evidence | **Passed.** |

## Open questions

1. What `From:` address does the newsletter use? Is it on corvane.com or a subdomain?
2. Does the newsletter platform sign with `d=corvane.com`, or with its own domain?
3. Is DKIM signing turned on for Google Workspace on corvane.com?
4. Do Zendesk, the billing system and Greenhouse already have custom DKIM or return-path records on corvane.com?
5. Does anything else send as corvane.com, such as the product, a CRM, calendar tools or HR systems?
6. Who owns DNS, and how fast can they change it?
7. How many newsletter recipients are on Gmail? Is there a known Gmail share across all streams combined?
8. Is there a hard date, such as a launch issue, that the newsletter must hit?

## What to tell the security team

- Put the reports in first. Start with `p=none` and aggregate reports on Monday.
- `pct` won't give a gradual ramp. Use `t=y` rehearsals.
- Move to reject once the reports show every legitimate source passing, not on a calendar date.
- Enforce the newsletter subdomain first and corvane.com last.