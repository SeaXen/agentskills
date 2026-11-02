# Pre-send check: Quillwork v3.0 announcement (Mode: restart a silent list)

## Direct answer

⚠️ **Don't send to all 9,800 at 9am Tuesday.** Send Tuesday, but ramp by cohort over about four sending days. Warm cohorts get v3.0 on launch day and the rest follow within the week.

- The list cleaning service did not make the 9,800 safe. Verification can't see recycled spam traps or readers who no longer want the mail. After 8 or more months of silence, those traps are the main risk.
- The 1,600 removed addresses are not bounces. Treat them as unproven and don't mail them this week.
- Authentication and the one-click headers are unverified. You can check them this weekend with a seed send.

## Misreads in the plan

| Misread | Applies because | Do instead |
|---|---|---|
| Verify the old list with a cleaning service, then mail all of it | "Verified" 9,800 plus one 9am blast is exactly this plan | Restart by engagement cohort, most recent first. Never one big send |
| "Delivered" means inbox | You will likely read the platform's delivered figure on Tuesday | Read raw bounces, Postmaster Tools spam rate and reader reports, not delivered or open rate |

## Evidence table

I have no headers, bounce logs or dashboards yet, so every step is **unverified**, not passed.

| Step | Check | Result | Source needed |
|---|---|---|---|
| 1 Delivery state | Raw SMTP replies from the last (February) send, then from the first ramp send | Unverified | Platform bounce export with raw text |
| 2 Authentication | `dkim=pass` with `d=` on your domain, `dmarc=pass`, a DMARC record of at least `p=none` | Unverified | Raw headers of a seed copy at Gmail, Outlook.com and Yahoo |
| 2 One-click | `List-Unsubscribe` (HTTPS), `List-Unsubscribe-Post: List-Unsubscribe=One-Click`, both in DKIM `h=`; GET must not unsubscribe | Unverified | Same seed headers, plus the GET/POST test |
| 3 Listings | Sending, link and tracking domains on the Spamhaus domain list | Unverified | Spamhaus's own lookup page |
| 4 Complaints | Gmail spam rate per stream | Unverified, because Postmaster Tools status is unknown | Postmaster Tools |
| 5 Events | 8+ months silent, public-form signups, possible bot signups, a platform move since February? | Silence is confirmed. The rest is unknown | You |
| 6 Content | Not reached | Steps 1 to 5 are open | - |

## Risks ranked

1. **Recycled spam traps in the dormant list.** Addresses that died during the silence now act as traps. The first send after the gap lands on them, and a one-day blast hits them all at once.
2. **False comfort from the cleaning service.** The cleaning removed "risky" addresses by its own scoring, which says nothing about traps or consent. It also invites the single-blast plan.
3. **Unknown authentication and one-click state.** If anything changed since February (platform, DNS, template), this is the most likely cause of a failed send. It is also the cheapest to check.
4. **Signup quality.** Single opt-in on a public docs form lets in typo traps, pristine traps and bot signups. Whether the form used confirmed opt-in is unknown.
5. **Unknown complaint baseline.** Without Postmaster Tools there is nothing to hold the ramp against.

## Fix plan

Today is Friday 2026-10-30. v3.0 ships Tuesday 2026-11-03. The deadline promotes authentication, the one-click headers and the ramp. The subdomain move, DMARC enforcement and any platform change wait until after launch.

| # | Fix | Owner | Date | Done when |
|---|---|---|---|---|
| 1 | Import all unsubscribes, bounces and complaints from the old export as suppressions | DevRel | Fri 10-30 | Suppression list matches the export, and the 1,600 removed addresses are tagged "unproven, held out" |
| 2 | Verify the sending domain in Postmaster Tools | DevRel | Fri 10-30 | Spam rate visible, or "no data yet" recorded as the baseline |
| 3 | Confirm custom DKIM on your own domain, an aligned return path and a DMARC record of at least `p=none` with `rua` | DNS owner | Sat 10-31 to Mon 11-02 | A seed copy shows `dkim=pass` with `d=` on your domain and `dmarc=pass` at Gmail, Outlook.com and Yahoo |
| 4 | Check the one-click headers, then GET and POST the URI on a seed address | DevRel | Mon 11-02 | Seed still subscribed after GET, unsubscribed after POST, POST returns 2xx with no redirect, and both headers are in DKIM `h=` |
| 5 | Branded HTTPS tracking domain, or send without tracking | DevRel | Mon 11-02 | No shared tracking domain in the issue's links |
| 6 | Spamhaus domain lookup on the sending and link domains | DevRel | Mon 11-02 | Not listed, or the cause fixed before requesting removal yourself |
| 7 | Order the 9,800 by last human click (after bot-click filtering), or by signup date, newest first, if no click data exists | DevRel | Mon 11-02 | Four cohorts defined, sizes recorded |
| 8 | Run the ramp below, reading raw bounces and the spam rate before each step | DevRel | Tue 11-03 to Fri 11-06 | Every step cleared its hold check, or the hold is recorded |
| 9 | Put the re-confirmation ask in the v3.0 issue (see Open questions) | DevRel | With the Tuesday send | Non-responders are suppressed by the date the issue states |
| 10 | Move to a newsletter subdomain and publish DMARC enforcement (subdomain first) | DNS owner, DevRel | After launch, with a date set at the Nov 10 re-check | Aligned, warmed up over about six weeks, reported separately |

If #3 or #4 fails on Monday, fix it before any send. A broken `dmarc=fail` at Gmail costs more than a one-day launch delay.

## Ramp

The sizes are an illustrative shape, a roughly doubling ramp over the 9,800. They are not measured data. Resize them once step 7 is done.

| Send | When | Who | About |
|---|---|---|---|
| 1 | Tue 11-03, 9:00 | Most recent human clickers, or newest signups | 800 |
| 2 | Wed 11-04 | Add the next cohort | 1,600 |
| 3 | Thu 11-05 | Add the next cohort | 3,200 |
| 4 | Fri 11-06 | Remaining active addresses, oldest and no-click tail last | about 4,200 |
| Later | After the ramp | The 1,600 held out | Re-confirmation only, in small batches, or drop |

Check these holds before each send:

- User-unknown bounces above about 2% of the previous cohort.
- A deferral spike at any provider.
- Gmail spam rate above 0.1%.

On a hold, re-send the same cohort size next time and check consent for the cohort that caused it. Pause any receiver that still blocks two sends after the fix is verified.

Classify bounces by code and text, not by the platform's hard/soft label:

- `5.1.1` or "user unknown": suppress now, permanently.
- `5.7.x`, `4.7.x` naming SPF, DKIM, DMARC or policy: keep the address and fix the sender.
- Other `4.x.x`: retry, and suppress after two consecutive bounces spanning two weeks or more.

Two more notes:

- Gmail counts every message to personal Gmail accounts from your domain and its subdomains, product and employee mail included. A ramp keeps day-one volume low. Meet the bulk rules (SPF, DKIM, DMARC, one-click, spam rate below 0.1%) anyway, because bulk status is permanent once reached.
- Readers behind corporate gateways may see Junk (Microsoft Defender moves BCL 7 and above by default). Scanners also click every link. Filter scanner clicks before using any click figure, and make the unsubscribe act on POST only. Offer the changelog as a feed for readers whose company junks bulk mail.

## Monitoring sheet

| Signal | Source | Alert level | Owner |
|---|---|---|---|
| Gmail spam rate | Postmaster Tools | 0.1% (never reach 0.3%) | DevRel |
| User-unknown share per cohort | Platform bounce export | About 2% (house rule) | DevRel |
| `4.7.x` and `5.7.x` counts per send | Raw bounce text | Any | DevRel |
| `dmarc` result | DMARC aggregate reports | Any fail from the platform source | DNS owner |
| Human clicks per delivered issue, after bot filtering | Platform plus filter | Trend only, never a placement proof | DevRel |
| Unsubscribe or complaint spike per cohort | Platform | Stop and read before the next send | DevRel |

## Pass-threshold status

| Threshold | Status | Missing fact, owner, re-check |
|---|---|---|
| Repeated claims checked against the misreads table | ✅ Passed | - |
| Each triage step has a verdict and evidence | ⏳ Blocked | Evidence for steps 1 to 5. DevRel, Mon 11-02 |
| Seed shows `dkim=pass` on your domain and `dmarc=pass` | ⏳ Blocked | Seed headers. DNS owner, Mon 11-02 |
| One-click headers present, DKIM-signed, GET doesn't unsubscribe | ⏳ Blocked | Seed test. DevRel, Mon 11-02 |
| Gmail spam rate read from Postmaster Tools, or its absence is an open task | ✅ Passed | Absence is logged as fix #2 |
| Every suppression rule separates dead addresses from policy blocks | ✅ Passed | See the bounce rules above |
| Every fix row has an owner, a date and a done-when | ✅ Passed | - |
| No open rate used as placement evidence or target | ✅ Passed | - |

## Open questions

1. Which sending platform do you use, and did anything change since February (platform, From domain, DNS, template, tracking domain)?
2. What is the From address, and what else sends from that domain (product mail, GitHub-style notifications, support tools)?
3. Was the signup form single or confirmed opt-in? Any bot-signup spikes?
4. Do you have last-click data per subscriber, or only signup dates?
5. What does the programme charter say for a list silent this long? This skill doesn't set the threshold. If you have no rule, ask the newsletter-program skill. Silent past the limit means the re-confirmation ask goes first, riding in the launch issue. A dormant tail inside an active list gets it last.
6. Is Postmaster Tools set up? Who can edit DNS, and how fast?
7. Which cleaning service was it, and which addresses did it flag? That matters for the held-out 1,600.

## Next action

Before Monday: send a seed copy to your own Gmail, Outlook.com and Yahoo addresses. Send me the three raw headers and I'll fill in steps 2 and 3 of the evidence table.