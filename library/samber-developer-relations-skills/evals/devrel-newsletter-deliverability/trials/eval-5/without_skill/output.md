# Pebbleworth Weekly: dedicated IP, Gmail bulk rules, and what to do instead

**Short answer: skip the dedicated IP. Your real deliverability problem is the `@gmail.com` From address, and that is free to fix.**

I haven't checked the platform's docs or Google's live guidelines. This is based on the rules as I know them (knowledge through mid-2026), so recheck Google's "Email sender guidelines" page before you act.

## 1. "Under 5,000/day, so the rules don't apply" is half right

- **The 5,000 threshold only decides whether you're a "bulk sender".** Google counts messages to personal Gmail addresses, aggregated across the whole primary domain, subdomains included. Once you cross it you're treated as a bulk sender permanently.
- **You probably are under it.** Your Gmail share of 4,200 newsletter subscribers plus 3,000 app emails is likely well below 5,000 a day. If both streams ever share `pebbleworth.app`, they add up toward the threshold.
- **The baseline rules apply to everyone who emails Gmail users:**
  - SPF or DKIM must pass.
  - Valid forward and reverse DNS must exist.
  - TLS must be used.
  - The spam rate in Postmaster Tools must stay under 0.3%.
- **Bulk-sender extras are DMARC, alignment, and one-click unsubscribe.** Gmail's filters reward these even below the threshold. Your newsletter needs working unsubscribe anyway, because of CAN-SPAM and GDPR.
- **Enforcement has been tightening.** Gmail started rejecting non-compliant mail rather than only junking it. Microsoft and Yahoo have similar rules.

## 2. The real problem: From `jonah.pebble@gmail.com`

The platform's servers send mail that claims to be from `gmail.com`. SPF and DKIM pass for the platform's domain, not Gmail's, so DMARC alignment fails. Google has said it will enforce DMARC on `gmail.com` From addresses. Even before hard rejection, this mail tends to land in spam or Promotions. You also build no domain reputation of your own, because you're borrowing Gmail's.

A dedicated IP doesn't fix this. A clean IP sending a failing-DMARC `@gmail.com` message is still a failing message.

**Fix:**
1. Send from a domain you own, such as `jonah@news.pebbleworth.app`.
2. Set up the platform's custom sending domain. It will give you DKIM and SPF records, and you add a DMARC record.
3. Set **Reply-To: jonah.pebble@gmail.com**. Replies still land in your inbox, which was your reason for using Gmail.

## 3. Dedicated IP: not worth it for you

- **Your volume is too low and too bursty.** About 4,200 sends once a week is a spike on a cold IP, with nothing in between. IP reputation builds from steady daily volume (tens of thousands a month is the usual rule of thumb) and decays when idle. A cold IP sending a weekly burst looks suspicious and gets throttled.
- **It needs warm-up.** You'd spend weeks ramping volume you don't have.
- **Shared pools from reputable platforms already have history.** The risk that "other senders hurt me" is real but modest on a decent platform. Ask them how they police abusers and whether they segment pools.
- **Domain reputation matters more than IP reputation.** Gmail weights it heavily, and you control it. It's yours whether the IP is shared or dedicated.
- **It probably wouldn't touch your app mail.** The 3,000 notifications a day likely go through a different provider, so this add-on wouldn't cover them.

**When I'd revisit:** steady volume above roughly 100k emails a month, a platform whose shared pool is demonstrably dirty (check Postmaster Tools and inbox-placement tests), or a need for IP-level isolation. Even your 3,000 a day of app mail is only borderline. Fix the domain setup first.

## 4. Do these instead

1. **Move the newsletter to its own subdomain** (`news.pebbleworth.app`) and keep app notifications on a different one (`mail.pebbleworth.app`). That isolates reputation, so a spam spike on one stream doesn't drag down the other. Hedged: Google aggregates the bulk-sender status at the primary domain, but reputation signals separate well in practice.
2. **Authenticate both streams:**
   - SPF, DKIM, and DMARC with alignment.
   - Start DMARC at `p=none` with reporting (`rua=`). Move to `quarantine` once the reports are clean.
3. **Add Gmail Postmaster Tools** for every sending domain. Keep the spam rate under 0.10% and never let it touch 0.30%.
4. **Check one-click unsubscribe** (the `List-Unsubscribe` and `List-Unsubscribe-Post` headers) on the newsletter. Keep it off the transactional notifications, which are exempt.
5. **Prune inactive subscribers.** Sunset anyone who hasn't opened in around 6 months. Engagement is a major Gmail signal.
6. **Run a placement test.** Send one newsletter to a few seed Gmail, Outlook, and Yahoo accounts and see where it lands. Then decide about the IP with data.

## 5. What to ask the platform

- Does a custom sending domain with DKIM come on every plan, and do you recommend a gmail.com From?
- How do you police abusive senders on shared IPs, and what is the pool's spam rate?
- Can you show your Postmaster reputation for the shared IPs?

Tell me which platform it is and I can tighten this to its actual setup steps.