# Saltmarsh Devs digest: deliverability report

## Direct answer

**Do not delete the 1,930 Outlook/Hotmail "hard bounces".** `550 5.7.515` means Microsoft refused your sending domain's authentication. The addresses are fine and the problem is on your side. Deleting them removes real readers and hides the fault.

**Delete only the 140 `5.1.1 user unknown` addresses.** Those mailboxes don't exist.

**You can't find or remove the Gmail people who reported you.** Gmail gives senders only an aggregate spam rate, with no list of who complained. Below, I explain how to localize the problem and bring the rate down. Your 0.4% is above Gmail's hard ceiling of 0.3%, so it is the most urgent item.

I haven't seen any headers, DNS records or bounce exports. The authentication cause below follows from the Outlook error text. It is not yet confirmed on a received copy.

## Claims checked against the misreads table

| Claim or plan | Verdict | Do instead |
|---|---|---|
| "Delete the 1,930 hard bounces" | Misread: "Suppress every 5xx as a bad address". A 5.7.x code is a policy block on the sender. | Keep them. Classify by code and text. |
| "Remove the Gmail people who reported us" | Misread: "Remove the Gmail complainers". There is no per-message complaint report. | Use the localization steps in Fix 1 below. |
| "Platform says hard bounce" | The platform's hard/soft label isn't evidence. | Read the raw SMTP text per provider. |

## Evidence table

| Step | Check | Result | Source |
|---|---|---|---|
| 1 Delivery state | Raw replies | **Fails.** About 1,930 `550 5.7.515` at outlook.com and hotmail.com: sender refused. 140 `550 5.1.1`: dead addresses. | Platform bounce report, as you gave it |
| 2 Authentication and alignment | `Authentication-Results` of a received issue | **Unverified, probable fail.** `5.7.515` means SPF, DKIM and DMARC don't reach Outlook's required level for `saltmarshdevs.io`. No headers seen yet. | Inferred from the error text |
| 2 One-click headers | `List-Unsubscribe` and `List-Unsubscribe-Post`, DKIM `h=`, GET test | **Unverified.** | - |
| 3 Listings | Spamhaus domain lookup on the sending, link and tracking domains | **Unverified.** | - |
| 4 Complaints | Gmail spam rate | **Fails.** 0.4% is above the 0.3% limit and four times the 0.1% target. | Postmaster Tools, as you gave it |
| 5 List and volume events | Import, old segment mailed, volume jump, bot signups | **Unverified.** | Open question |
| 6 Content | Not reached | Steps 1, 2 and 4 are failing or open, so wording is noise. | - |

Outlook.com's consumer rule applies to domains sending 5,000+ a day to Outlook, Hotmail and Live addresses. It requires SPF pass, DKIM pass and DMARC at least `p=none`, aligned. Rejections have run since May 2025.

## Causes, ranked

1. **Authentication or alignment gap at Outlook.** Probably no DMARC record, or DKIM signed by the platform's domain instead of `saltmarshdevs.io`. This accounts for about 93% of the bounces (1,930 of roughly 2,070).
2. **Gmail complaint rate at 0.4%.** The cause is unknown until you know which segment or issue drives it. Likely suspects are cold or old subscribers, a missing or broken one-click unsubscribe, or a recent import.
3. **Dead addresses (140 `5.1.1`).** About 6.8% of the bounces. If they cluster in one signup source or an old segment, that points to a list-source problem. Check this.
4. **Unchecked suspects:** a blocklist listing, and a shared or non-branded tracking domain.

## Fix plan

Order: stop the harm, repair authentication, repair one-click, suppress dead addresses, ramp back by cohort. Dates assume the next digest goes out Thursday 2026-11-05. Adjust them if your cadence differs.

| # | Fix | Owner | Date | Done when |
|---|---|---|---|---|
| 1 | **Stop the harm.** Hold the next send to Gmail addresses until the cause is localized. Don't re-send last week's issue to bounced Outlook addresses. | Newsletter owner | Today | Next send is scheduled only to cohorts that pass the gates in Fix 6. |
| 1a | **Localize Gmail complaints.** In Postmaster Tools, read the daily spam rate per sending domain. If your platform lets you set a `Feedback-ID` header and signs with your own verified DKIM domain, use Gmail's feedback-loop view. It flags segments with unusual spam rates, but small lists often show no data. Otherwise send cohorts (recent clickers, mid-age, oldest) on separate days and compare each day's rate. | Newsletter owner | 2026-11-05 to 11-07 | The segment driving complaints is named, or you have a documented "no data" result. |
| 1b | **Pause the worst cohort.** Stop mailing the segment that shows the highest rate. | Newsletter owner | Same day it is identified | That segment gets no mail until the re-confirmation step in Fix 6. |
| 2 | **Repair authentication.** Send a seed copy to an outlook.com address and read its raw headers. Publish custom DKIM and the return-path records for `saltmarshdevs.io`, so DKIM `d=` is your domain. Publish `_dmarc.saltmarshdevs.io` as `v=DMARC1; p=none; rua=mailto:<your address>`. Check with `dig +short TXT _dmarc.saltmarshdevs.io`. | DNS owner | This week | The seed issue shows `dkim=pass` with `d=saltmarshdevs.io`, `spf=pass` and `dmarc=pass`. |
| 3 | **Repair one-click unsubscribe.** Check the headers for an HTTPS `List-Unsubscribe` and `List-Unsubscribe-Post: List-Unsubscribe=One-Click`. Both must appear in the DKIM `h=` list. GET the URL on a seed address and confirm it is still subscribed. POST it, expect a 2xx with no redirect, and confirm it is now unsubscribed. | Newsletter owner | This week | Both tests pass. |
| 4 | **Suppress the 140 `5.1.1` addresses** permanently. For the 1,930 `5.7.515` addresses, export the list, then make the platform un-suppress them or exclude them from auto-deletion. Ask the platform for raw bounce text if you only see hard/soft buckets. | Newsletter owner | This week | 140 suppressed. 1,930 retained and flagged "sender-side block". Export saved. |
| 5 | **Check blocklists.** Use Spamhaus's own lookup page for the sending, link and tracking domains. If listed, fix the cause first, then request removal yourself (it's free). | DNS owner | This week | Lookup result recorded. |
| 6 | **Ramp back by cohort.** Send to recent clickers first, then double the cohort each step over consecutive days. Hold the ramp if user-unknown bounces pass about 2% of a cohort, deferrals spike, or the Gmail rate passes 0.1%. Mail the 1,930 Outlook addresses only after Fix 2 passes, starting with the most recent clickers. If Outlook still rejects two sends after the fix is verified, pause that domain and escalate through Microsoft's sender support. | Newsletter owner | Next issue and the following ones | The Outlook `5.7.515` count is zero. Gmail spam rate has stayed below 0.1% for 7 consecutive days. |
| 7 | **Prevent repeats.** Apply the inactivity rule on human clicks after bot-click filtering. Confirm consent for any imported or old segment with the list-growth skill. | Newsletter owner | Next month | The rule is written in the programme charter. |
| 8 | **Later, not this week.** Move to a newsletter subdomain, add a branded tracking domain, and move DMARC to enforcement (subdomain first). | DNS owner | After the above | Not blocking this recovery. |

At 0.4%, Gmail offers no mitigation help until your rate has been under 0.3% for 7 consecutive days. Fix 1 is the priority for that reason.

## Monitoring sheet

| Signal | Source | Alert level | Owner |
|---|---|---|---|
| Gmail spam rate, per stream | Postmaster Tools, daily | Alert at 0.1%, urgent at 0.3% | Newsletter owner |
| `5.7.x` and `4.7.x` counts per send, by provider | Platform raw bounce log | Any non-zero count | Newsletter owner |
| `5.1.1` share per cohort | Platform raw bounce log | About 2% (house rule) | Newsletter owner |
| DMARC pass rate by source | Aggregate reports (`rua`) | Any source failing | DNS owner |
| Spamhaus listing | Spamhaus lookup, before each send | Any listing | DNS owner |
| Human clicks per delivered issue | Platform, after bot-click filtering | Trend only. Don't use opens as placement evidence. | Newsletter owner |

## Pass-threshold status

| Threshold | Status | Missing fact, owner, re-check |
|---|---|---|
| Repeated claims checked against the misreads table | Passed | - |
| Each triage step has a verdict and evidence, or is marked unverified | Passed | - |
| A received issue shows `dkim=pass` on your domain and `dmarc=pass` | **Blocked** | Raw headers of a received issue. Owner: newsletter owner. Re-check 2026-11-02. |
| One-click headers present, DKIM-signed, and GET doesn't unsubscribe | **Blocked** | Header and GET/POST test. Owner: newsletter owner. Re-check 2026-11-02. |
| Gmail spam rate read from Postmaster Tools | Passed | You supplied 0.4%. |
| Suppression rules separate dead addresses from policy blocks | Passed | - |
| Every fix row has an owner, a date and a done-when check | Passed | - |
| No open rate used as placement evidence | Passed | - |

## Open questions

1. Which platform do you use, and is it on a shared pool? How many recipients per send, and what share is Gmail, Outlook and work addresses?
2. What is the `From:` address, and what else sends as `saltmarshdevs.io` (product, billing, employee mail)? Who edits DNS, and how fast?
3. Does a DMARC record exist today? Do the headers of a delivered issue show DKIM `d=` as your domain or the platform's?
4. What changed before last Thursday: a platform move, an import, a send to an old segment, a volume jump?
5. How was the list collected, and when did each segment last receive mail?
6. Is the 0.4% Gmail rate from the same send or a longer window? Is Postmaster Tools verified on `saltmarshdevs.io` itself?
7. Does a hard date apply to the next issue?

The 1,930 Outlook bounces probably have a single cause (authentication) that is fixable in DNS within days. The Gmail complaints are the harder problem and need the cohort test and the segment pause.