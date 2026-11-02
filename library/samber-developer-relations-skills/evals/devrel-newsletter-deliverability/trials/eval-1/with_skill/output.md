# Deliverability report: Petrel Labs monthly SDK digest

## Direct answer

I'm not giving you new subject lines. The header you pasted shows the fault, and it isn't the wording.

```
dkim=pass header.i=@mailer-cloud.net
spf=pass   smtp.mailfrom=bounces.mailer-cloud.net
dmarc=fail header.from=petrel.dev
```

DKIM and SPF both pass, but for the platform's domain (`mailer-cloud.net`), not yours (`petrel.dev`). DMARC needs one of them to match the `From:` domain, and neither does. The new tool is signing mail for itself. That is the usual result of a platform move without custom DKIM and return-path records, and it fits "June, right after we switched". Fix that first. Rewriting subject lines changes nothing while DMARC fails.

Two other points:

- **Rewriting every subject line and dropping "free":** wrong order. Filters weigh authentication and reputation first, and word lists are folklore at Gmail and Outlook. Content is the last step of the triage. Keep your subject lines and the "free-tier" section. If you want to test wording later, treat it as a tiebreaker, once authentication passes.
- **Opens falling from 41% to 22%:** by itself this doesn't prove spam placement, because mail-privacy features and image blocking move opens independently. Here the failed DMARC is the stronger evidence. Don't use opens as a target or a placement measure.

## Evidence table

| Step | Check | Result | Source |
|---|---|---|---|
| 1 Delivery state | Raw SMTP replies per provider | **Unverified.** No bounce log with raw text yet. Look for `4.7.32`, `5.7.26` and `5.7.1` at Gmail. | Not supplied |
| 2 Authentication | `Authentication-Results` | **Fails.** `dkim=pass` on `mailer-cloud.net`, `spf=pass` on `bounces.mailer-cloud.net`, `dmarc=fail header.from=petrel.dev`. No alignment on either mechanism. | June issue header at Gmail |
| 2 One-click | `List-Unsubscribe` (HTTPS URI), `List-Unsubscribe-Post`, both in DKIM `h=` | **Unverified.** Only the authentication line was supplied. | Not supplied |
| 3 Listings | Spamhaus domain lookup for `petrel.dev` and the tracking domain; shared IP | **Unverified.** | Not run |
| 4 Complaints | Gmail spam rate in Postmaster Tools | **Unverified.** Access not confirmed. | Not supplied |
| 5 Events | Platform move, followed by the drop in June | Matches the start date. The list itself did not change, as far as you've said. | You |
| 6 Content | Subject lines, "free" | **Not reached.** Step 2 fails. | n/a |

## Causes, ranked

1. **DMARC alignment lost in the platform move.** `dmarc=fail` with the new tool's domain in both `d=` and the envelope. At about 14,000 recipients, with a large Gmail share likely, you fall under Gmail's bulk-sender rules (the permanent threshold is near 5,000 a day to personal Gmail accounts, counted across your domain and its subdomains). Gmail has enforced those rules with rejections and spam-foldering since November 2025.
2. **Reputation reset from the move (new sending path, new tracking and IP signals).** Probable but unproven. Every issue since June has also been unauthenticated, which can drag down the domain's reputation.
3. **Unknown complaint rate.** It can't be ruled out until Postmaster Tools shows data.
4. **Corporate gateways for work readers** (Microsoft Defender bulk scoring). Check headers from an affected company only after causes 1 to 3 are fixed.
5. **Content.** Not supported by any evidence you've given.

## Password resets on petrel.dev

You send resets from the same domain, so this needs a decision. The newsletter's problems can bleed into reset mail through shared domain reputation, and Gmail counts all your streams together. Three consequences:

- **Check whether the reset tool is aligned.** Run the same header check on a real reset email. I can't tell from what you've sent whether it passes DMARC.
- **Do not publish `p=quarantine` or `p=reject` on `petrel.dev` yet.** With the newsletter failing DMARC, enforcement would send it to junk or bounce it, and an unaligned reset sender would break too. Stay at `p=none` with reports until every sender is aligned.
- **Move the newsletter to its own subdomain (`news.petrel.dev`).** That gives the digest its own reputation signal, so a bad week for the newsletter stops touching resets. A subdomain doesn't fully shield the root domain, because Gmail rolls subdomain volume up to the primary domain. That is why it sits later in the plan.

## Fix plan

Order: stop the harm, repair authentication, repair headers, clean up suppressions, ramp back by cohort, tracking domain, subdomain, DMARC enforcement, platform change last.

| # | Fix | Owner | Date | Done when |
|---|---|---|---|---|
| 1 | Hold the next digest until fix 2 passes. | DevRel | now | No issue goes out with `dmarc=fail`. |
| 2 | Publish the new tool's custom DKIM and return-path records for `petrel.dev`, keeping the current `From:`. Keep the old tool's records live for a week if both are still wired. | Whoever owns DNS (**name them, and how fast they can edit**) | 2026-11-04 | A seed issue received at Gmail, Outlook.com and Yahoo shows `dkim=pass` with `d=petrel.dev` and `dmarc=pass`. |
| 3 | Check the one-click headers on that seed. `List-Unsubscribe` carries an HTTPS URI, `List-Unsubscribe-Post: List-Unsubscribe=One-Click` is present, and both are in the DKIM `h=` list. A GET on the URL must not unsubscribe the seed, and a POST must. | DevRel plus platform support | 2026-11-04 | Both tests pass on a seed address you own. |
| 4 | Verify `petrel.dev` in Gmail Postmaster Tools. | DevRel | 2026-11-04 | Spam rate and authentication views visible. |
| 5 | Pull the platform's bounce log with raw SMTP text. Suppress `5.1.1` and "user unknown" addresses. Keep every `4.7.x` or `5.7.x` address (those are sender blocks, not bad readers). | DevRel | 2026-11-06 | Suppression list updated by code and text, not by the platform's hard/soft label. |
| 6 | Look up `petrel.dev`, the link and tracking domains and the sending IP on Spamhaus's own lookup page. | DevRel | 2026-11-06 | Listed or not, recorded. |
| 7 | Check the password-reset mail headers for `dmarc=pass`. | Platform or infra lead | 2026-11-06 | Reset mail passes, or the unaligned sender is on a fix list. |
| 8 | Send the held issue by click cohort over consecutive days, most recent human clickers first and roughly doubling each step. Hold the ramp if user-unknown bounces pass about 2% of a cohort, deferrals spike, or the Gmail spam rate crosses 0.1%. Colder cohorts roll into later issues. | DevRel | next issue window | Warm cohorts reached on the date, the rest within the following issues, spam rate under 0.1%, no `4.7.x` or `5.7.x` at Gmail. |
| 9 | Set up a branded HTTPS tracking domain (for example `links.petrel.dev`). | DevRel plus DNS owner | 2026-11-20 | Links no longer use the platform's shared tracking domain. |
| 10 | Publish `_dmarc.petrel.dev` at `p=none` with `rua`. Read the reports weekly and list every sender: product, billing, support, HR, the reset tool, the newsletter. | Infra lead | 2026-11-20 | Every source listed with an owner and an aligned or retire decision. |
| 11 | Move the digest to `news.petrel.dev` with its own DKIM and return path, and warm it by the same cohort ramp. It reports separately from resets. | Infra lead, DevRel | Q1 2027 | Subdomain aligned, warmed and reported on its own. |
| 12 | Enforce DMARC on the newsletter subdomain first, using `p=quarantine; pct=0; t=y`, then `p=reject; pct=0; t=y`, then `p=reject`. Do not use a `pct=25` ramp: RFC 9989 removed `pct`. Enforce `petrel.dev` last, after step 10 shows everything aligned. | Infra lead | after 10 and 11 | Reports show only aligned sources. |
| 13 | Change platform. Not recommended unless the tool can't sign with your domain or won't expose raw bounces. | n/a | not planned | n/a |

If the DNS owner can do both steps 2 and 11 in one pass, it may be cheaper to launch straight on `news.petrel.dev` and skip a second warm-up. That is your call. The plan above fixes the live problem on the current `From:` first.

## Monitoring sheet

| Signal | Source | Alert level | Owner |
|---|---|---|---|
| Gmail spam rate | Postmaster Tools | 0.1% (never reach 0.3%) | DevRel |
| `4.7.x` / `5.7.x` counts per send | Platform bounce log (raw text) | Any | DevRel |
| User-unknown share per cohort | Platform bounce log | About 2% (house rule) | DevRel |
| `dkim` and `dmarc` result on a seed copy | Raw headers, Gmail | Any `fail` | DevRel |
| DMARC aggregate pass rate per source | `rua` reports | Any unaligned source | Infra lead |
| Human clicks per delivered issue, after bot filtering | Platform | Trend only | DevRel |

## Pass-threshold status

| Threshold | Status |
|---|---|
| Every claim you repeated checked against the misreads table | Passed (subject-line rewrite and "open rate means spam" both applied). |
| Each triage step has a verdict and evidence, or is marked unverified | Passed. |
| A received issue shows `dkim=pass` on your own domain and `dmarc=pass` | **Failed.** Your June header shows `dmarc=fail` and the platform's domain. Fix 2 closes it. |
| One-click headers present, DKIM-signed, GET doesn't unsubscribe | **Blocked.** Missing fact: full raw headers of a recent issue. Owner: DevRel. Re-check 2026-11-04. |
| Gmail spam rate read from Postmaster Tools, or its absence is an open task | Passed as an open task (fix 4). |
| Suppression rules separate dead addresses from policy blocks | Passed (fix 5). |
| Every fix row has an owner, a date and a done-when check | Passed. Dates are proposals, and the owners need confirming. |
| No open rate used as placement evidence or target | Passed. |

## Open questions

1. **Raw headers of a recent issue:** are the one-click headers present, and are they DKIM-signed?
2. **Bounce log:** does the platform expose raw SMTP text, and do you see `4.7.32`, `5.7.26` or `5.7.1` at Gmail?
3. **Postmaster Tools:** is `petrel.dev` verified?
4. **Password resets:** which tool sends them, and does a reset email show `dmarc=pass`?
5. **What else sends as petrel.dev,** such as product, billing, support and employee mail?
6. **Who owns DNS, and how fast can they edit?**
7. **Gmail, Outlook and work-address mix** across the 14,000.
8. **Click history:** can you export last-human-click dates for the old tool's list?
9. **What did you do about the old tool's suppressions** (unsubscribes, bounces, complaints) in the move? Confirm they were imported before the first send.
10. **Is there a fixed date** for the next issue, such as a launch?