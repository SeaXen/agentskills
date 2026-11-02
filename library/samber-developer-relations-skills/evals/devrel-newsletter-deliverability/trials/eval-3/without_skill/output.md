# Diagnosis: security scanners are clicking your links, and the Gmail "spam" assumption is unproven

I haven't seen your logs, so the main cause below is a strong inference from the symptoms, not a confirmed fact. The checks to confirm it are in section 3.

## 1. Most likely cause: enterprise mail scanners "click" every link

- **The mechanism.** Gateways like Microsoft Defender Safe Links, Proofpoint, Mimecast and Barracuda fetch every URL in an inbound email to check it for malware. They do this before or when the message lands, and no human is involved.
- **The unsubscribes.** `GET /unsubscribe?u=<base64 email>` changes state on a GET. The scanner fetches it and the reader is unsubscribed. That matches "unsubscribed without clicking anything", and it only affects enterprise readers, who sit behind these gateways.
- **The click-through jump.** The scanner also fetches your tracked links, and listmonk records each fetch as a click. Your 4% to 11% jump with unchanged content is the same cause. The extra clicks are machines.
- **Why August.** I can't tell from here. Either an enterprise customer or Microsoft changed its scanning policy, or something changed on your side in August. Check your config and deploy history for when the GET endpoint or the `List-Unsubscribe` header changed.

Two related problems:
- **Forgeable link.** The link is an unsigned base64 of the address, so anyone can unsubscribe any address. It also puts the email address in URLs that get logged. Treat this as a security bug independent of the scanner issue.
- **Header endpoint.** If your `List-Unsubscribe` header points at the same GET endpoint, some scanners and mailbox providers will trigger it too.

## 2. Gmail and spam: not established

- An open rate of 18% doesn't show spam placement. You haven't said what it was before, and opens are a noisy signal. Apple Mail Privacy Protection and scanner prefetches inflate opens elsewhere. Gmail's Promotions tab also lowers opens without being spam.
- If the Gmail drop is real, the likely drivers are a falling Gmail reputation or missing one-click unsubscribe, which Gmail has required from bulk senders since 2024.
- **Bigger risk:** `digest@fernhill.dev` also sends your password resets. If the digest's reputation drops, resets go to spam too. That is the part to fix whatever the cause.

## 3. Confirm before changing anything

1. **Unsubscribe logs** (reverse proxy or app). For each unsubscribe, check:
   - User-agent and source IP. Microsoft, Proofpoint and Mimecast ranges are the suspects.
   - Seconds since the campaign was delivered to that address. Scanner hits land within seconds.
   - Whether the same address hit other links in the same second.
2. **Click data.** Compare click-through for `gmail.com` addresses (the control group) against enterprise domains.
   - In listmonk, `link_clicks` joined to `subscribers` and `campaigns` gives time-to-click. I wrote the table names from memory, so check them against your schema.
   - Individual tracking must be on, or clicks aren't tied to subscribers.
   - Look for many links clicked in the same second, in HTML order, including the footer.
3. **Honeypot.** Add a hidden link that no human would see. Any clicks on it are bots.
4. **Gmail health:**
   - Check Google Postmaster Tools for domain reputation and spam rate. Aim for under 0.1% and stay well below 0.3%.
   - Check the SES reputation dashboard for bounce and complaint rates, and confirm bounces and complaints flow back to listmonk.
   - Confirm SPF, DKIM and DMARC align on `fernhill.dev`.
   - Send a seed message to a Gmail account and see which tab it lands in.

## 4. Fix, in order

1. **Make unsubscribe safe on GET.**
   - GET shows a page with a confirm button, and the unsubscribe happens on POST. Scanners don't submit forms.
   - The simplest route is to drop the custom endpoint and use listmonk's native `{{ UnsubscribeURL }}`. It uses a per-subscriber UUID and a confirmation page. Verify the behavior in your version.
2. **Replace the unsigned token** with a per-subscriber random ID or an HMAC-signed value. Never put the email in the URL.
3. **Add RFC 8058 one-click.** Send `List-Unsubscribe` plus `List-Unsubscribe-Post: List-Unsubscribe=One-Click`, handled on POST, and DKIM-sign both headers. Check listmonk's privacy settings for the unsubscribe header.
4. **Separate the mail streams.**
   - Put the digest on its own subdomain, for example `news.fernhill.dev`, with its own SES identity and configuration set.
   - Keep password resets on a different subdomain.
   - Consider a dedicated SES IP pool for transactional mail.
5. **Repair the data.** Restore the unsubscribes that match the bot signature: seconds after delivery, a scanner IP or user-agent, and no later human activity. Keep the genuine ones. Reply to the readers who wrote in. Whether to re-add people without their action is a consent call, so decide it with whoever owns GDPR for you.
6. **Re-baseline click-through.** Exclude clicks within a few seconds of delivery, and clicks that hit several links at once. Only compare against the 4% after that filtering.

## 5. What I need from you

- What was the Gmail open rate before, and when did it start dropping?
- Does the `List-Unsubscribe` header exist today, and what URL does it use?
- Did anything change in August: deploys, SES settings, or the unsubscribe endpoint?
- Are individual click and open tracking enabled in listmonk?

With those answers and a sample of the unsubscribe logs, I can confirm or rule out the scanner theory.