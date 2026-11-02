# Fernhill CLI digest: deliverability report

## Direct answer

**Your unsubscribe endpoint is the main problem. The spam theory is unproven.**

`GET /unsubscribe?u=<base64 email>` unsubscribes on a plain GET, so corporate link scanners are unsubscribing your readers. Microsoft Safe Links, Proofpoint, Mimecast and Barracuda fetch every URL in a message when it arrives. With about 60% of your list at large companies, this fits both symptoms:

- **Silent unsubscribes:** a scanner "clicked" the unsubscribe link for readers who never did.
- **Click-through 4% to 11%:** the same scanners click every link in each copy. The jump is machine traffic, not readers liking the issue more.

I can't date the cause from what you gave me. I can say it matches "enterprise readers only" and "no content change". Ask ops what changed around August: a customer's gateway rollout, a listmonk upgrade, a new link or tracking setup.

A second flaw: the link is the base64 of the address. Anyone can unsubscribe anyone by encoding an email address. Fix that in the same change.

The 18% Gmail open rate does **not** show you're in spam. Mail-privacy features and image blocking move opens without moving placement. Gmail placement is **unverified** until you read Postmaster Tools.

## Misreads checked

| Your claim | Verdict |
|---|---|
| "Readers unsubscribe without clicking" | Correct, and this is the scanner pattern. |
| "Clicks 4% to 11%, nothing changed" | Not real engagement. Scanners click every link of a copy. Don't report it or use it for any inactivity rule until filtered. |
| "Gmail opens fell to 18%, so we're in spam" | Opens are not placement evidence. Read the Postmaster Tools spam rate, rejections and click trends. |
| Unsubscribe via GET with a base64 email | Fails twice: it acts on GET, and the URL is guessable. Use POST only, GET shows a confirm page, and the token is opaque and checked server-side. |

## Evidence table

| Step | Check | Result | Source |
|---|---|---|---|
| 1 Delivery state | Raw SMTP replies per provider | **Unverified.** Need the listmonk and SES bounce log with raw text. Look for `5.7.x` and `4.7.x` at Gmail and Microsoft. | Not supplied |
| 2 Authentication | `dkim=pass` with `d=fernhill.dev`, `dmarc=pass` | **Unverified.** Confirm SES Easy DKIM signs with your domain. Confirm a custom MAIL FROM, or at least aligned DKIM. | Not supplied |
| 2 One-click | `List-Unsubscribe` (HTTPS), `List-Unsubscribe-Post: List-Unsubscribe=One-Click`, both in DKIM `h=` | **Unverified.** Scanners also fetch header URIs, so a GET-acting endpoint is hit from the header too. | Not supplied |
| 2 GET test | GET the URI on a seed address | **Fails by design.** Ops confirms the link acts on a plain GET. Verify on a seed to be certain. | Ops statement |
| 3 Listings | Spamhaus domain lookup for `fernhill.dev`, link and tracking domains | **Unverified.** Use Spamhaus's own lookup page. | Not supplied |
| 4 Complaints | Gmail spam rate, per stream | **Unverified.** No Postmaster Tools data. Keep below 0.1%, never reach 0.3%. | Not supplied |
| 4 Stream mixing | Digest and password resets share `digest@fernhill.dev` | **Confirmed.** A newsletter complaint or block now hits password reset mail. | Your description |
| 5 Events | Start date of the unsubscribe reports | August. Matches the scanner pattern, but the trigger is unidentified. | Your description |
| 5 Events | Clicks 4% to 11% with no content change | **Machine-click signature.** | Your description |
| 6 Content | Not reached | Steps 1, 2 and 4 are open. | - |

Walk-through note: step 5 shows a confirmed failure (the GET endpoint). The other earlier steps are unverified, not passed. Collecting their evidence is in the fix plan.

## Causes ranked

1. **Unsubscribe acts on GET, so scanners unsubscribe readers.** Evidence: enterprise-only reports, no click, and the endpoint design. Impact: lost subscribers and a corrupted engagement signal.
2. **Scanner clicks inflate click-through.** Evidence: 4% to 11% with no content change. Impact: any inactivity rule or "top content" decision built on clicks is wrong.
3. **Guessable unsubscribe token.** Evidence: base64 of the email. Impact: anyone can unsubscribe anyone.
4. **Newsletter and password resets share one `From:` address.** Evidence: your description. Impact: shared reputation, and Gmail asks for subscription mail from a different address than other mail.
5. **Gmail placement: unknown.** The 18% open rate can't confirm or rule it out. Postmaster Tools can.
6. **Corporate Junk placement (possible, separate):** Microsoft Defender can move bulk mail to Junk at BCL 7 or higher. Check headers from an affected reader before blaming the list.

## Fix plan

Order: stop the harm, repair the headers, clean up, then the slower structural work.

| # | Fix | Owner | Date | Done when |
|---|---|---|---|---|
| 1 | **Make unsubscribe POST-only.** GET shows a confirm page with a button. No JavaScript auto-submit. Use an opaque random token looked up server-side, not the email. | Engineering (whoever owns the endpoint) | Before the next issue; target 2026-11-02 | A GET on a seed address leaves it subscribed. A POST unsubscribes it with a 2xx and no redirect. A guessed base64 URL does nothing. |
| 2 | **Add RFC 8058 headers.** HTTPS `List-Unsubscribe`, `List-Unsubscribe-Post: List-Unsubscribe=One-Click`, both listed in the DKIM `h=` tag. Point both at the new POST endpoint. | Engineering, DNS/SES owner | 2026-11-02 | Raw headers of a received seed issue show all three. |
| 3 | **Identify scanner-removed readers.** Use web logs and listmonk events. Flag unsubscribes with no prior click, within seconds of delivery, from cloud IP ranges, on enterprise domains. | DevRel with Engineering | 2026-11-06 | A list of suspected scanner removals exists. |
| 4 | **Handle those readers carefully.** Don't re-add them silently. Send a short note on how to resubscribe, and restore anyone who asks. Genuine unsubscribes stay suppressed. | DevRel | 2026-11-13 | Note sent. Restore requests honoured. |
| 5 | **Filter bot clicks.** Drop clicks within seconds of delivery, from cloud IPs, or on every link of one copy. Re-baseline click-through. | DevRel/analytics | 2026-11-13 | A filtered human-click rate is published next to the raw one. Use it for any inactivity rule. |
| 6 | **Set up Gmail Postmaster Tools** for `fernhill.dev`. | DevRel with DNS owner | 2026-11-02 | The spam rate is visible per day. |
| 7 | **Pull the raw bounce log** from listmonk and SES. Classify by code and text. Suppress only dead addresses (`5.1.1`). Keep sender-side `5.7.x` blocks. | DevRel | 2026-11-06 | Rules distinguish dead addresses from policy blocks. |
| 8 | **Verify authentication** on a received issue at Gmail, Outlook.com and Yahoo. Check `dkim=pass` with `d=fernhill.dev` and `dmarc=pass`. Publish `_dmarc` with `p=none` and `rua` if missing. | DNS/SES owner | 2026-11-06 | Headers show alignment on all three. |
| 9 | **Spamhaus domain lookup** for the sending, link and tracking domains. | DevRel | 2026-11-06 | Result recorded. |
| 10 | **Branded HTTPS tracking domain** on your own domain (or send without tracking). | Engineering | 2026-11-20 | Links no longer use a shared domain. |
| 11 | **Move the digest to a subdomain**, for example `digest@news.fernhill.dev`, with its own DKIM, aligned return path and warm-up (about six weeks). Password resets stay on the root domain. | DNS/SES owner, DevRel | Next quarter | Subdomain aligned, warmed and reported separately in Postmaster Tools. |
| 12 | **DMARC enforcement**: newsletter subdomain first, organizational domain last, after inventorying every sender. | DNS owner | After item 11 | Reports show only known, aligned sources. |
| 13 | **Publish a short allow-listing note** for readers' IT teams: sending domain and DKIM `d=`. Offer an archive or feed link for readers whose company junks bulk mail. | DevRel | 2026-11-20 | Note live and linked from the footer. |

Skip item 11's "dedicated IP" idea if it comes up. A weekly burst on a dedicated IP is the inconsistent volume pattern that hurts reputation.

## Monitoring sheet

| Signal | Source | Alert level | Owner |
|---|---|---|---|
| Gmail spam rate | Postmaster Tools | 0.1% | DevRel |
| `4.7.x` and `5.7.x` counts per send | SES and listmonk bounce log | Any | DevRel |
| User-unknown share per send | Bounce log | About 2% (house rule) | DevRel |
| Unsubscribes with no prior click | listmonk events and web logs | Any after fix 1; should fall to near zero | Engineering |
| Human click rate after bot filtering | Analytics | Trend only | DevRel |
| DMARC aggregate reports | `rua` mailbox | Any unknown source | DNS owner |

## Pass-threshold status

| Threshold | Status |
|---|---|
| User's repeated claims checked against the misreads table | Passed |
| Each triage step has a verdict or is marked unverified | Passed |
| `dkim=pass` on your own domain and `dmarc=pass` on a received issue | **Blocked.** Missing: raw headers of a received issue. Owner: DNS/SES owner. Re-check 2026-11-06. |
| One-click headers present and DKIM-signed, and GET does not unsubscribe | **Failed** on GET (fix 1). Headers blocked on the same raw-headers fact. Re-check after 2026-11-02. |
| Gmail spam rate read from Postmaster Tools | **Blocked.** Open task, fix 6. Re-check 2026-11-06. |
| Suppression rules separate dead addresses from policy blocks | **Blocked.** Needs the raw bounce log. Re-check 2026-11-06. |
| Every fix row has an owner, date and done-when | Passed |
| No open rate used as placement evidence or a target | Passed |

## Open questions

1. What changed in August: a customer gateway rollout, a listmonk upgrade, a template, link or tracking change?
2. Is the `/unsubscribe` endpoint listmonk's own or a custom service? Does it also back the `List-Unsubscribe` header?
3. What share of the list is on Gmail, Outlook and work domains?
4. What does the raw header of a received issue show for authentication and unsubscribe headers?
5. Do password resets sign with `d=fernhill.dev` and share the same SES configuration set?
6. What does the programme's inactivity rule say? Run it on filtered human clicks, not raw clicks.

I did not run any commands against your systems. Every verdict above comes from your description and the skill's rules.