# Pebbleworth Weekly: deliverability report

## Direct answer

**Don't buy the dedicated IP.** It fixes a problem you don't have and leaves the one you do have untouched.

The real problem is the `From:` address. A gmail.com address can't be authenticated through a newsletter platform, so DMARC alignment fails. Move the newsletter to a domain you own, keep replies landing in your inbox with `Reply-To`, and keep the shared pool.

Your "under 5,000 a day" assumption is also unsafe. Details are below.

## Misreads checked

| Your claim | Verdict | Why | Do instead |
|---|---|---|---|
| "I send from `jonah.pebble@gmail.com` through a platform" | **Fails** | The platform can't sign DKIM for gmail.com, so `dmarc=fail` on `header.from=gmail.com`. gmail.com publishes `p=none; sp=quarantine`, and Google warns it will tighten that policy for Gmail `From:` impersonation. Yahoo and others may already treat these messages harshly. | Send from a domain you own. Set `Reply-To: jonah.pebble@gmail.com`. |
| "Under 5,000 a day, so Gmail's bulk rules don't apply" | **Unsafe** | Gmail counts messages to personal Gmail accounts, across the primary domain and its subdomains. Product and notification mail counts. Bulk status is permanent once reached. | Count the Gmail-consumer share across all streams (see below). Meet the bulk rules now. |
| "Dedicated IP so other senders can't hurt me" | **Wrong fit** | You send one burst of 4,200, then six quiet days. That is the inconsistent volume pattern reputation punishes. Vendor gates for dedicated IPs sit in the hundreds of thousands a month. A dedicated IP also needs a warm-up and a re-warm after every quiet spell. | Stay on the shared pool and sign with your own domain. Your reputation then follows your DKIM domain, not the pool. |

### The 5,000 count

- **Send day:** 3,000 notification emails plus 4,200 newsletter copies is about 7,200 messages. Only the Gmail-consumer share counts toward Gmail's threshold.
  - At 50% Gmail, that's about 3,600.
  - At 70% Gmail, it's about 5,000.
- **Today:** the newsletter sends from gmail.com, so it does not add to the `pebbleworth.app` count. That is the only reason you're below the line.
- **After the fix:** moving the newsletter to `news.pebbleworth.app` rolls its volume up to the primary domain. The combined count then becomes real.
- **Cost of crossing:** you'd be bulk permanently, with one-click unsubscribe, DMARC and a spam rate under 0.3% all mandatory.

Meeting the rules now costs an hour of DNS. Meeting them after Gmail starts throttling costs a lot more.

## Evidence table

I have no headers, bounce logs or Postmaster data from you. Missing evidence is marked unverified, not passed.

| Step | Check | Result | Source |
|---|---|---|---|
| 1 Delivery state | Raw SMTP replies at Gmail, Yahoo, Outlook | **Unverified**: no bounce export supplied | Platform bounce log |
| 2 Authentication | `Authentication-Results` of a received issue | **Expected to fail**: `From: @gmail.com` cannot align through a platform. Confirm in raw headers. | Your Gmail copy, "Show original" |
| 2 One-click | `List-Unsubscribe` (HTTPS) and `List-Unsubscribe-Post`, both in the DKIM `h=` list | **Unverified** | Same raw headers |
| 3 Listings | Spamhaus domain lookup for `pebbleworth.app` and the tracking domain | **Unverified** | Spamhaus lookup page |
| 4 Complaints | Gmail spam rate per stream | **Unverified**: Postmaster Tools not mentioned | Postmaster Tools |
| 5 Events | Volume and list events | No known event. The 3,000 a day of product mail is a standing volume risk. | You |
| 6 Content | Not reached | Steps 2 and 4 open | - |

## Causes ranked

1. **Freemail `From:` through a platform.** The DMARC alignment failure is the most likely cause of any spam-folder or rejection trouble. It also blocks DMARC reporting and your own Postmaster data.
2. **Unmeasured Gmail volume across two streams.** The bulk threshold is closer than "under 5,000" suggests.
3. **Unknown complaint rate.** It can't be ruled out until Postmaster Tools shows data.
4. **Dedicated IP pitch.** This is not a cause. It's a distraction costing money and a warm-up.

## Fix plan

Order: stop the harm, repair authentication, repair headers, then structure. The first three rows can land this week.

| # | Fix | Owner | Date | Done when |
|---|---|---|---|---|
| 1 | Decline the dedicated IP add-on. | Jonah | 2026-10-30 | No add-on on the invoice. |
| 2 | Verify `pebbleworth.app` in Postmaster Tools. Read the spam rate per stream. | Jonah | 2026-11-02 | Spam rate visible. Alert at 0.1%, never reach 0.3%. |
| 3 | Pull the raw SMTP replies from the platform's bounce log. Classify them: `5.1.1` means a dead address, `5.7.x` means a sender block. | Jonah | 2026-11-02 | `5.1.1` addresses suppressed. `5.7.x` addresses kept. |
| 4 | Authenticate a newsletter subdomain `news.pebbleworth.app`: custom DKIM, aligned return path, branded HTTPS tracking domain (`links.pebbleworth.app`). Use the records your platform publishes. | Jonah (DNS) | 2026-11-04 | A seed issue shows `dkim=pass` with `d=news.pebbleworth.app`, `spf=pass` on your return path, and `dmarc=pass`. |
| 5 | Send from `jonah@news.pebbleworth.app` with `Reply-To: jonah.pebble@gmail.com`. | Jonah | first issue after row 4 | Replies still arrive in your Gmail inbox. |
| 6 | Check one-click headers. Both `List-Unsubscribe` (HTTPS) and `List-Unsubscribe-Post: List-Unsubscribe=One-Click` must be in the DKIM `h=` list. Then run the GET/POST test on a seed address. | Jonah | with row 4 | GET leaves the seed subscribed, POST unsubscribes it with a 2xx. |
| 7 | Warm the new sending identity. Send in click-cohort order, most recent clickers first, over the consecutive days of one issue's send window. | Jonah | next 2 to 3 issues | No `4.7.x` deferrals. Hold the ramp if user-unknown bounces pass about 2% or the spam rate passes 0.1%. |
| 8 | Publish `_dmarc.pebbleworth.app` as `v=DMARC1; p=none; rua=mailto:...`. Inventory every sender on the domain: the app, support, billing, calendar. | Jonah | 2026-11-13 | Each source listed and aligned or retired. |
| 9 | Check the product notification stream: SPF or DKIM aligned, DMARC pass, valid PTR and TLS. If any of it is subscribed or marketing-style, give it one-click too. | Jonah | 2026-11-13 | Gmail copy shows `dmarc=pass`. |
| 10 | Count the Gmail-consumer share from your app database and the platform export. Re-check monthly. | Jonah | 2026-11-13 | A number exists. Alert if the send-day Gmail count passes about 4,000. |
| 11 | DMARC enforcement. Do the newsletter subdomain first: `p=quarantine; pct=0; t=y`, then `p=reject; pct=0; t=y`, then `p=reject`. Do the root domain last. | Jonah | after 2 to 4 weeks of clean reports | Reports show only aligned sources. |

Notes on the plan:

- **No `pct=25` ramp.** RFC 9989 (May 2026) removed `pct`. Rehearse each level with `t=y` plus `pct=0`.
- **No root `p=reject` this week.** Unknown senders on the domain would start bouncing.
- **Replies:** a `Reply-To` does the job of the gmail `From:`, so you lose nothing.
- **Platform change:** not needed unless it can't sign with your domain or won't show raw bounces. Check that before you pay for anything.

## Monitoring sheet

| Signal | Source | Alert level | Owner |
|---|---|---|---|
| Gmail spam rate per stream | Postmaster Tools | 0.1% | Jonah |
| `4.7.x` and `5.7.x` counts per send | Platform bounce log (raw text) | Any | Jonah |
| User-unknown (`5.1.1`) share per send | Platform bounce log | About 2% (house rule) | Jonah |
| Gmail-consumer messages per day, all streams | App database plus platform export | About 4,000 a day | Jonah |
| DMARC pass rate by source | Aggregate reports | Any unaligned source | Jonah |
| Human clicks per issue | Platform, after scanner-click filtering | Trend only, never a placement signal | Jonah |

## Pass-threshold status

| Threshold | Status | Missing fact and owner | Re-check |
|---|---|---|---|
| Repeated claims checked against the misreads table | **Passed** | - | - |
| Each triage step has a verdict or is marked unverified | **Passed** | - | - |
| `dkim=pass` on your own domain and `dmarc=pass` in a received issue | **Blocked** | The raw headers of a received issue, from Jonah | 2026-11-04 |
| One-click headers present, DKIM-signed, GET does not unsubscribe | **Blocked** | Header and GET/POST test results, from Jonah | 2026-11-04 |
| Gmail spam rate read from Postmaster Tools, or absence is an open task | **Passed** (open task, row 2) | Postmaster access, from Jonah | 2026-11-02 |
| Suppression rules separate dead addresses from policy blocks | **Passed** (row 3) | - | - |
| Each fix row has an owner, a date and a done-when check | **Passed** | - | - |
| No open rate used as placement evidence | **Passed** | - | - |

## Open questions

1. What share of the 4,200 newsletter subscribers and of the 3,000 daily notifications go to Gmail, Outlook and Yahoo addresses?
2. Is `pebbleworth.app` verified in Postmaster Tools, and what spam rate does it show?
3. Does your platform let you sign DKIM and set a return path on your own domain? If not, that moves platform change up the plan.
4. What does the raw bounce log say, by provider?
5. Does the app's notification mailer sign with `d=pebbleworth.app`, and does it send any marketing-style mail?
6. Has the newsletter ever been mailed to a dormant segment, or imported from another source?

Re-check dates: 2026-11-02 (Postmaster and bounces) and 2026-11-04 (headers).