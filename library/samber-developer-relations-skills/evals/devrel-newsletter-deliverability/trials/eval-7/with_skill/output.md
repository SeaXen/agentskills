# Deliverability report: Tidewater API changelog newsletter

## Direct answer

Don't pay the $299, and don't chase Primary. You are probably not fine yet, because nothing you've sent shows that authentication and complaint rate are healthy.

- **Promotions** is an inbox category, not a spam verdict. Tricks to force Primary raise complaints and put the sender at risk. The only supported move is to ask readers to move one issue to Primary or reply to it, then leave it alone.
- **The $299 delisting service** is a misread. Spamhaus removal is free, and Spamhaus shows you clean. Delisting before the cause is fixed gets you relisted.
- **The 92% seed test** is a directional snapshot, not proof. Seed inboxes have no engagement history, so the number says little about real readers. I don't know whether it counted Promotions as "inbox", and I don't know where the other 8% went.

I haven't seen headers, Postmaster Tools data or bounce logs, so most triage steps below are **unverified**, not passed.

## Misreads checked

| Your claim or plan | Verdict | Do instead |
|---|---|---|
| "Which tricks get us into Primary?" | Misread. Promotions is a category, and tricks raise complaints. | Ask readers to move or reply to one issue, then leave it. |
| "A company will delist us from all of them for $299." | Misread. Removal is free, and a paid delisting before the fix means relisting. | Fix the cause, then request removal yourself from each list. |
| "92% seed test, so we're fine." | Misread. Seed inboxes have no engagement history. | Use Postmaster Tools spam rate, raw headers and reader reports. |
| "4 blocklists, but Spamhaus is clean." | Partly right. Spamhaus is the list that matters most, and it is clean. | Find out what each of the 4 lists. A list on a shared platform IP is not your domain's problem. |

## Evidence table

| Step | Check | Result | Source |
|---|---|---|---|
| 1 Delivery state | Raw SMTP replies per provider | **Unverified**: no bounce log supplied | None |
| 2 Authentication | `dkim=pass` with `d=` on your domain, `dmarc=pass` | **Unverified**: no headers supplied | None |
| 2 One-click | `List-Unsubscribe`, `List-Unsubscribe-Post`, both in the DKIM `h=` list, GET does not unsubscribe | **Unverified** | None |
| 3 Listings | Spamhaus domain and IP lists | Clean, as reported. I didn't re-run it, so confirm on Spamhaus's own lookup page. | You, via MXToolbox |
| 3 Listings | 4 other lists, including UCEPROTECT | **Unverified**: I don't know which of your domain, link domain or sending IP they list | MXToolbox |
| 4 Complaints | Gmail spam rate, target below 0.1% | **Unverified**: no Postmaster Tools data | None |
| 5 Events | Platform move, new domain, import, old segment, volume jump | **Unverified**: not told | None |
| 6 Content | Promotions placement | Not reached. This step only counts after steps 1 to 5 pass. | None |

## Causes ranked

1. **Unknown: authentication or alignment.** This is the first thing to check, because it gates everything else. It is unverified, not cleared.
2. **Unknown: complaint rate.** It is invisible until Postmaster Tools is set up. A platform's own complaint figure under-counts Gmail.
3. **Blocklist listings of unknown scope.**
   - By general knowledge, not from the skill: UCEPROTECT's wider levels list whole IP ranges, so you can be listed because of other senders on a shared pool.
   - The skill says to ignore checkers that report dozens of minor lists.
   - If it is a shared platform IP, raise a ticket with your platform. If it is your own domain or link domain, find the cause.
4. **Promotions placement.** This is a normal category for bulk, tracked, HTML mail. It is not a fault to fix with tricks.

## Fix plan

Order: stop harm, then authentication, then headers, then evidence, then cohort ramp, then the longer-term moves.

| # | Fix | Owner | Date | Done when |
|---|---|---|---|---|
| 1 | Pull the raw headers of one issue received at Gmail, Outlook.com and Yahoo, and read `Authentication-Results`. | Newsletter owner | 2026-11-02 | `dkim=pass` with `d=` on your domain and `dmarc=pass` are confirmed, or the failure is recorded. |
| 2 | Run the one-click test on a seed address you own: GET must not unsubscribe, POST must return a 2xx with no redirect. | Newsletter owner | 2026-11-02 | The header and POST behaviour are confirmed, or fixed. |
| 3 | Verify the sending domain in Gmail Postmaster Tools. | DNS owner | 2026-11-03 | Spam rate is visible, below 0.1%. |
| 4 | Record which entity each of the 4 lists names, and re-check Spamhaus on its own lookup page. | Newsletter owner | 2026-11-02 | Each listing is classified as domain, link domain or shared IP. |
| 5 | If a list names your domain or link domain, find what changed and fix it before requesting removal. If it names a shared IP, raise a ticket with your platform. | Newsletter owner or platform support | 2026-11-06 | Cause named, fix done, removal requested directly. |
| 6 | Export the platform's raw bounce text. Suppress `5.1.1`-type dead addresses. Keep any `5.7.x` address and treat it as a sender block. | Newsletter owner | 2026-11-06 | Suppressions separate dead addresses from policy blocks. |
| 7 | Put one line in the next issue asking readers to drag it to Primary or reply once. | Newsletter owner | Next issue | Sent once, not repeated. |
| 8 | Check for a recent event (platform move, import, old segment mailed, volume jump). If one lines up with the problem, ramp back by engagement cohort. | Newsletter owner | 2026-11-06 | The event is identified, and the ramp runs if needed. |
| 9 | Longer term: a newsletter subdomain, a branded tracking domain, then DMARC ladder steps from `p=none` with reports. | DNS owner | Next quarter | Subdomain aligned and reported separately. |

## Monitoring sheet

| Signal | Source | Alert level | Owner |
|---|---|---|---|
| Gmail spam rate | Postmaster Tools | 0.1% | Newsletter owner |
| `4.7.x` and `5.7.x` counts per send | Bounce export | Any | Newsletter owner |
| Dead-address share per send | Bounce export | About 2% (house rule) | Newsletter owner |
| Blocklist status (Spamhaus, plus the 4 found) | Each list's own lookup | Any new listing | Newsletter owner |
| Human clicks per delivered issue, after bot-click filtering | Platform | Trend only | Newsletter owner |

Don't use open rate as placement evidence or as a target.

## Pass-threshold status

| Threshold | Status |
|---|---|
| Every user claim checked against the misreads table | **Passed** |
| Each triage step has a verdict and evidence, or is marked unverified | **Passed** |
| Received issue shows `dkim=pass` on your domain and `dmarc=pass` | **Blocked**. Missing: raw headers. Owner: newsletter owner. Re-check 2026-11-02. |
| One-click headers present and DKIM-signed, and GET does not unsubscribe | **Blocked**. Missing: headers and a seed test. Owner: newsletter owner. Re-check 2026-11-02. |
| Gmail spam rate read from Postmaster Tools, or its absence is an open task | **Passed**. It is an open task (fix 3). |
| Suppression rules separate dead addresses from policy blocks | **Passed** (fix 6) |
| Every fix row has an owner, a date and a done-when check | **Passed** |
| No open rate used as placement evidence | **Passed** |

## Open questions

1. Which 4 lists name you, and is each entry your domain, your link or tracking domain, or the platform's shared IP?
2. Which platform sends the newsletter, which `From:` domain does it use, and does it sign with your own DKIM domain?
3. What changed recently: platform move, import, a send to an old segment, or a volume jump?
4. Does the 92% seed result count Promotions as inbox, and where did the other 8% land?
5. Do you have any headers, bounce text, or Postmaster data you can paste?

## Out of scope

Primary-tab placement depends on HTML weight, the plain-text part and copy. That belongs to `devrel-newsletter-issue`, and no tweak there guarantees a tab. For readers behind corporate gateways who still get the issue junked, offer a feed or archive link, for example a changelog feed (`changelog-writing`).