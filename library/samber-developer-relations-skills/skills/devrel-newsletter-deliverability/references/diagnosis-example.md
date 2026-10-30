# Worked diagnosis and a negative example

## Input

> "Our monthly SDK digest for Lanternfish (about 14,000 subscribers) has been landing in spam since we moved from one newsletter platform to another in May. Opens dropped from 41% to 22%. Marketing wants to rewrite the subject lines and remove the word 'free' from the free-tier section. We also send password resets from example.io. Can you fix it?"

Evidence the user then supplied: raw headers of a June issue received at Gmail, the new platform's bounce export, Postmaster Tools not set up.

## Output (abridged)

**Direct answer.** Authentication broke in the move: the new platform signs with its own domain, so DMARC fails for `example.io`. Fix the DNS before touching the copy. The open-rate drop is not placement evidence on its own.

**Evidence table**

| Step | Check | Result | Source |
|---|---|---|---|
| 1 Delivery state | Raw replies | 212 `4.7.32` deferrals at Gmail, 31 `5.1.1` | Bounce export |
| 2 Authentication | `Authentication-Results` | `dkim=pass header.i=@platform-mail.net`, `dmarc=fail header.from=example.io` | June issue headers |
| 2 One-click | `List-Unsubscribe-Post` | Present and covered by the platform's DKIM signature; passes RFC 8058 | June issue headers |
| 3 Listings | Spamhaus domain lookup | Not listed | Lookup on the day |
| 4 Complaints | Gmail spam rate | **Unverified**: Postmaster Tools not set up | - |
| 5 Events | Platform move in May; same list | Matches the start date | User |
| 6 Content | Not reached | Steps 2 and 4 open | - |

**Causes ranked**

1. DMARC alignment lost at the platform move (`4.7.32`, `dmarc=fail`).
2. Unknown complaint rate: cannot be ruled out until Postmaster Tools shows data.

**Fix plan**

| Fix | Owner | Date | Done when |
|---|---|---|---|
| Publish the new platform's custom DKIM and return-path records for `example.io`, keeping the current `From:` | Infra lead | this week | A seed issue shows `dkim=pass` with `d=example.io` and `dmarc=pass` |
| Verify `example.io` in Postmaster Tools | DevRel | this week | Spam rate visible |
| Suppress the 31 `5.1.1` addresses; keep the 212 deferred ones | DevRel | this week | Suppression list updated |
| Send the next issue by click cohort over consecutive sending days, most recent first | DevRel | next issue | Warm cohorts reached this issue, the rest within the following issues; no `4.7.32`, spam rate below 0.1% |
| Publish `_dmarc.example.io` `p=none` with reports, inventory senders | Infra lead | this month | Every source listed with an owner |
| Move the newsletter to `digest@news.example.io` so password resets stop sharing its signals, with its own warm-up | Infra lead, DevRel | next quarter | Subdomain aligned, warmed, reported separately |

**Monitoring sheet**: Gmail spam rate (Postmaster Tools, alert at 0.1%), `4.7.x`/`5.7.x` counts per send (bounce export, alert on any), user-unknown share per send (alert at about 2%, house rule), human clicks per delivered issue after bot filtering (trend only).

**Open questions**: the complaint rate; whether the password-reset tool already signs for `example.io`.

## Negative example

> "Spam filters flag words like 'free', so rename 'free tier' to 'no-cost tier', shorten the subject, cut images to raise the text ratio, and buy a dedicated IP so other senders can't affect you. Remove inactive subscribers who haven't opened in 90 days."

What is wrong:

- Starts at content, step 6, while step 2 fails in the user's own headers.
- Neither Gmail nor Microsoft publishes evidence that word swaps or image ratios move placement.
- A dedicated IP for a monthly send of 14,000 is the inconsistent-volume pattern reputation punishes, and it adds a warm-up.
- Opens-based inactivity removes readers whose mail clients block or fake opens, and keeps nobody safer.
- Treats the `4.7.32` deferrals as bad addresses by omission: no code was read at all.
