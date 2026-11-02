# Pre-send checks for the Quillwork v3.0 announcement

**Main recommendation:** don't send all 9,800 at once at 9am. Do a staged send, with a go/no-go check between waves. The reasons are below.

## 1. Send in waves, not one blast

You haven't mailed this list since February. Your sending domain and IP have no recent reputation, and some addresses have gone dormant or been recycled into spam traps. A cold 9,800-message burst to Gmail and Yahoo is the pattern that sends a whole announcement to spam.

Suggested schedule (adjust sizes to your ESP):

| Wave | When | Size | Who |
|---|---|---|---|
| 1 | Tue 9:00 | ~1,000 | Most recent signups, plus anyone who clicked in the last send |
| 2 | Tue ~11:00 | ~3,000 | Next newest |
| 3 | Tue ~14:00 or Wed 9:00 | Rest | Oldest signups |

Check these before each wave:
- **Hard bounce rate:** under 2%. Pause above that.
- **Spam complaint rate:** under 0.1%. Pause at 0.2% or more. Gmail and Yahoo treat 0.3% as a hard line.
- **Clicks, not opens:** Apple Mail Privacy Protection inflates opens.

Name one person who owns the pause button on Tuesday morning.

## 2. Confirm v3.0 is live before the first send

Your send date and your ship date are the same day. If the release slips or the docs deploy late, the email goes out pointing at nothing.

- Make the send a manual go after the tag is cut, the release is published, and the docs are live.
- Click every link from a real inbox: download, changelog, migration guide, docs.
- If v3.0 has breaking changes, link the migration guide prominently.
- Decide which timezone "9am" means. A global OSS audience gets this email at very different hours.

## 3. Authentication and Gmail/Yahoo bulk rules

At 5,000+ messages a day you fall under the Gmail and Yahoo bulk-sender requirements. Verify all of these before Tuesday:

- [ ] SPF, DKIM and DMARC pass, aligned on the From domain. Check the headers of a test email.
- [ ] One-click unsubscribe is present: `List-Unsubscribe` and `List-Unsubscribe-Post` headers, plus a visible footer link.
- [ ] The From and Reply-To addresses are real and monitored. v3 launch replies will arrive.
- [ ] The unsubscribe link works and takes effect immediately.
- [ ] Your ESP account is active and in good standing. After eight months idle, check for plan limits, a paused account, or a stale billing method.

## 4. Test sends

- Send to seed addresses at Gmail, Outlook, Yahoo and iCloud. Check inbox versus spam, and Gmail's Promotions tab.
- Run it through a spam checker such as mail-tester.
- Check the plain-text version, dark mode, and mobile rendering.
- Confirm the preheader text, the subject line, and that merge fields don't render blank.

## 5. Don't treat "verified" as "consented" or "engaged"

The cleaning service answered one question: does this mailbox exist and accept mail? It did not tell you whether the person remembers signing up.

- **Reconnect in the first line.** Add something like: "You're getting this because you signed up for Quillwork news on our docs site. It's been a while, so here's what changed."
- **Check the signup form.** Did the wording promise a newsletter, or only release announcements? A v3 announcement fits either way, but the first line should match what you promised.
- **Check for double opt-in.** If the form was single opt-in, expect more typos and bot signups. Those are the likely source of the spam traps and the reason to send oldest signups last.
- **Look at signup dates.** If a large share signed up more than 2 years ago, they are the likeliest to complain. Send them in the last wave and watch that wave closely.

## 6. Handle the 1,600 "risky" addresses carefully

"Risky" is not "invalid". Cleaning services use it for accept-all or catch-all domains, role addresses (`info@`, `team@`), and unknowns. Many company mail servers get flagged this way. These are real subscribers who opted in.

- **Ask the vendor for the breakdown by reason.** Don't cut 14% of your list blind.
- **Don't delete them.** Move them to a suppressed segment.
- **Exclude** anything flagged invalid, disposable, or a known spam trap.
- **Mail the rest later.** Once the main send shows healthy numbers, send the accept-all and role-address group in a small batch, for example 200 first. Alternatively, reach them through the GitHub release and the docs site banner.

## 7. Privacy and legal

- **Third-party processor:** you sent subscriber emails to a list-cleaning service. If you have EU subscribers, check that you have a data processing agreement with them and that your privacy policy covers email-verification vendors. Nantes-based senders are in scope for GDPR.
- **Footer requirements:** include the sender identity, a postal address (CAN-SPAM), and a working unsubscribe link.
- **Unsubscribes and complaints:** make sure they sync to a suppression list. Don't re-add anyone who unsubscribed, even if they are in the original 11,400.

## 8. Plan for after the send

- Monitor replies and bounces for 24-48 hours.
- Export hard bounces and complaints, and add them to suppression.
- Expect more unsubscribes than usual. After 8 months of silence, 0.5-2% is normal and healthy.
- Record the results (delivery, click rate, complaints per wave). That gives you a baseline for the next send.
- Set a regular cadence afterward, even if it's quarterly. Long gaps are what caused this problem.

## Final go/no-go checklist for Tuesday

1. v3.0 is released and docs are live (**do not send before this**).
2. SPF, DKIM, DMARC and one-click unsubscribe pass on a test email.
3. Seed tests landed in the inbox at Gmail and Outlook.
4. The wave plan and pause thresholds are written down, and one person owns the pause.
5. The 1,600 risky addresses are suppressed, not deleted.
6. Wave 1 numbers are clean: bounces under 2%, complaints under 0.1%. Only then send wave 2.

I couldn't see your ESP, DNS, or the cleaning vendor's report, so none of these items are verified. If you share the vendor's breakdown of the 1,600 and your signup-date distribution, I can help size the waves.