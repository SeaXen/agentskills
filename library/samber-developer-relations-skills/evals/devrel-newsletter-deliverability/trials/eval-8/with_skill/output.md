# Larchmont Data newsletter: should we switch platforms next month?

## Direct answer

**No. Don't commit to a platform switch yet.**

- **What the evidence shows.** Gmail readers get the mail, Postmaster Tools shows a 0.04% spam rate, and DMARC passes. Together those mean the sender's reputation at consumer mailbox providers is healthy. The failures are at big-enterprise gateways such as Microsoft Defender and similar filters, which score and quarantine bulk mail by their own rules.
- **Why a new platform won't fix it.** A different platform doesn't change how those gateways treat bulk mail. It also resets your tracking and IP signals and needs a full warm-up (about six weeks, per M3AAWG). If the cause is on your side, the new platform would likely show the same symptom.
- **What to do instead.** Get the headers of one Junk or quarantined issue from an affected reader. They show the cause, usually within a day. Run the checks below first. Move to a platform change only if the current platform can't sign with your own domain or won't expose raw bounce text.

## Claims checked against the misreads table

| Claim | Verdict |
|---|---|
| "Postmaster shows 0.04%, so we're healthy everywhere" | **Partly wrong.** It is a Gmail-consumer number only. Gmail's sender rules and Postmaster don't cover Google Workspace or Microsoft 365 tenants, which is where banks sit. It rules out a complaint problem at Gmail, not at corporate filters. |
| "DMARC passes, so authentication is fine" | **Incomplete.** DMARC passes on either aligned SPF or aligned DKIM. If it passes only on SPF, or DKIM is signed with the platform's domain, it can pass while gateways still score you worse. Check `d=`. |
| "Switch platform to fix it" | **Last on the fix order.** A platform change comes after stopping harm, repairing authentication and headers, hygiene, ramping, tracking domain, subdomain and DMARC enforcement. |
| Platform delivered rate (if cited) | **Not placement evidence.** Delivered means the server answered 250. Junk and quarantine both count as delivered. |

## Evidence table

| Step | Check | Result | Source |
|---|---|---|---|
| 1 Delivery state | Raw SMTP replies at enterprise domains | **Unverified.** "Junk or quarantine" implies accepted, but no one has read the bounce log. | Platform bounce log, not yet pulled |
| 2 Authentication | DMARC | Pass | User, via the platform or DMARC reports |
| 2 Authentication | DKIM `d=` on your own domain, aligned SPF | **Unverified** | Needs raw headers |
| 2 One-click | `List-Unsubscribe` (HTTPS), `List-Unsubscribe-Post`, both in the DKIM `h=` list | **Unverified** | Needs raw headers |
| 2 One-click | A GET on the unsubscribe URL does not unsubscribe | **Unverified.** This matters here: gateways fetch every URL. | Seed test (see the authentication reference) |
| 3 Listings | Spamhaus domain list for the sending, link and tracking domains | **Unverified** | Spamhaus's own lookup page |
| 4 Complaints | Gmail spam rate | **Pass:** 0.04%, under the 0.1% target. Covers personal Gmail only. | Postmaster Tools |
| 5 Events | Platform move, new domain, import, send to an old segment, volume jump, tracking-domain change | **Unverified.** No date has been lined up against when the complaints began. | Question to the team |
| 6 Content and links | Shared tracking domain, shorteners, link reputation | **Unverified.** Reached only after steps 1 to 5 pass, but the tracking domain is a cheap check. | Header and link audit |
| Corporate gateway | Bulk Complaint Level (BCL), category | **Unverified.** This is the most probable explanation. | `X-Forefront-Antispam-Report` in a Microsoft 365 reader's copy |

## Causes, ranked

1. **Bulk scoring at corporate gateways (most likely).** Microsoft Defender gives each bulk message a BCL from 0 to 9. The default threshold of 7 sends it to Junk. The Standard preset uses 6, and Strict quarantines from 5. Admins can lower the thresholds further. Mimecast, Proofpoint and Barracuda hold suspected bulk mail in quarantine digests. Microsoft's own guidance lists legitimate newsletters at BCL 7 to 9. This fits "banks and Fortune 500s, but Gmail is fine", and it is a recipient-side policy that a platform change doesn't alter.
2. **Weak signals on your own domain.** Candidates are DKIM signed by the platform's domain instead of yours, a shared tracking domain, an unaligned return path, and missing or unsigned one-click headers. These are cheap to check and fix.
3. **Link scanners distorting your data.** Gateways click every link, so scanner clicks can hide dead or unengaged addresses and inflate engagement. If your unsubscribe acts on GET, scanners may also be unsubscribing enterprise readers silently. That would make enterprise readers vanish as well as land in Junk.
4. **A list or volume event on your side.** This is unverified. It can't be ruled out until someone dates when the complaints began.
5. **Platform limitation (least likely).** Only if the platform can't sign with your domain or hides raw bounces.

## Fix plan

Order: stop the harm, then authentication, headers, hygiene, tracking domain, subdomain and DMARC enforcement, and platform change last. Dates are relative to the day you start. Each owner needs to confirm their date.

| # | Fix | Owner | Date | Done when |
|---|---|---|---|---|
| 1 | Ask 3 to 5 affected readers (bank, F500) to forward the Junk or quarantined issue **as an attachment**, or send full headers. Collect the platform's raw bounce text for those domains. | DevRel | Within 3 days | You have headers from at least 2 different companies. `BCL`, `CAT` and any gateway verdict are recorded. |
| 2 | Read the received issue: `dkim=pass` with `d=` on your own domain, SPF aligned, `dmarc=pass` | DevRel, DNS owner | Within 3 days | The `Authentication-Results` line is pasted into the report. |
| 3 | Test one-click: both headers present, both in the DKIM `h=` list, a GET does not unsubscribe a seed address, a POST does and returns 2xx | DevRel | Within 1 week | Seed test passes. If the endpoint acts on GET, switch it to POST-only with a confirm page and an opaque token. |
| 4 | Filter scanner clicks (clicks within seconds of delivery, from cloud IP ranges, or on every link of one copy). Re-check suppressions: restore readers a scanner unsubscribed, and tell them how to resubscribe. | DevRel | Within 1 week | Enterprise-domain unsubscribes are audited. Human-click reports exclude scanner clicks. |
| 5 | Move to a branded HTTPS tracking domain on your own domain, or send without tracking | DNS owner | Within 2 weeks | Links resolve to your own site. |
| 6 | Publish a short allow-listing note for readers' IT teams: sending domain and DKIM `d=`, plus the Microsoft 365 options to allow the domain or adjust the bulk threshold | DevRel | Within 2 weeks | The note is on a public page you can share with readers. |
| 7 | Offer an archive or feed link for readers whose company junks bulk mail regardless | DevRel | Next issue | The link is in the issue footer. |
| 8 | Check Spamhaus's domain list for the sending, link and tracking domains | DNS owner | Within 1 week | Listed or not, recorded with the lookup date. |
| 9 | Move to a newsletter subdomain with its own custom DKIM and a warm-up of about six weeks, if the check in fix 2 shows shared-domain signals | DNS owner, DevRel | Next quarter | Subdomain aligned, warmed and reported separately. |
| 10 | DMARC enforcement: newsletter subdomain first, organizational domain last | DNS owner | Next quarter | Reports show only known sources. |
| 11 | Decide on a platform change, using the evidence from fixes 1 to 8 | CEO, DevRel | After fixes 1 to 8 | Platform change is approved only if the platform can't sign with your domain or won't expose raw bounce text. |

## Reply to the CEO

> We don't yet know that the platform is the cause. Gmail readers get the newsletter, and Postmaster Tools shows a spam rate of 0.04%. Enterprise mail gateways score bulk mail by their own rules, so a platform change would not alter that. A switch also resets our sending reputation and needs about six weeks to warm up. Within a week we can read headers from two or three affected readers, test our authentication and unsubscribe headers, and fix any gaps. If those checks show the platform is the limit, we switch with evidence. If not, we have fixed the actual problem for much less.

## Monitoring sheet

| Signal | Source | Alert level | Owner |
|---|---|---|---|
| Gmail spam rate | Postmaster Tools | 0.1% (never 0.3%) | DevRel |
| `4.7.x` / `5.7.x` counts per send | Platform bounce log | Any | DevRel |
| User-unknown share per send | Platform bounce log | About 2% (house rule) | DevRel |
| Enterprise-domain Junk or quarantine reports | Reader reports, headers | Trend per issue | DevRel |
| BCL on Microsoft 365 copies | `X-Forefront-Antispam-Report` | 6 or above | DevRel |
| Human clicks per delivered issue, after scanner filtering | Platform | Trend only | DevRel |
| DMARC aggregate reports | Report address | Any unknown source | DNS owner |

Do not use open rate as placement evidence or as a target.

## Pass-threshold status

| Threshold | Status |
|---|---|
| Every user claim checked against the misreads table | **Passed** |
| Each triage step has a verdict and its evidence, or is marked unverified | **Passed** |
| A received issue shows `dkim=pass` on your own domain and `dmarc=pass` | **Blocked.** The missing fact is the raw headers of a received issue. The owner is DevRel, due in 3 days. |
| One-click headers present, DKIM-signed, GET does not unsubscribe | **Blocked.** The missing fact is the seed test result. The owner is DevRel, due in 1 week. |
| Gmail spam rate read from Postmaster Tools | **Passed** at 0.04%, for personal Gmail only |
| Suppression rules distinguish dead addresses from policy blocks | **Blocked** until the bounce log is read. Due in 3 days. |
| Every fix row has an owner, a date and a done-when | **Passed** |
| No open rate used as placement evidence or target | **Passed** |

## Open questions

1. Which platform are you on now, and does it sign with your own domain (`d=`)?
2. What is the `From:` address, and what else sends from that domain (product, billing, support)?
3. What changed before the complaints began: a platform move, a new domain, an import, a send to an old segment, a tracking-domain change?
4. Can an affected reader share the full headers of a Junk or quarantined issue?
5. Does the platform show raw SMTP replies per recipient, or only hard and soft buckets?
6. Is there a hard date the fix must land by, such as a launch issue?