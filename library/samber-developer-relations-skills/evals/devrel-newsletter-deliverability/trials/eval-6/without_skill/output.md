# Saltmarsh Devs digest: bounce cleanup and Gmail spam rate

**Next action:** don't delete anything yet. About 1,790 of those 1,930 "hard bounces" are probably real subscribers.

## 1. The ~1,790 outlook.com / hotmail.com "bounces" (550 5.7.515)

This is not a bad-address bounce. Microsoft is rejecting your mail because `saltmarshdevs.io` fails its sender-authentication requirements. Since May 2025, Microsoft requires SPF, DKIM, and DMARC for high-volume senders. DMARC must be at least `p=none`, and SPF or DKIM must align with the From domain. Your platform sees a permanent 550 and labels it a hard bounce. The mailboxes are fine.

If you delete these people, you lose real subscribers. If the platform suppresses them, they also stop receiving future issues, even after you fix the problem.

**Fix, in order (about 30 min of work, plus DNS propagation):**

1. Check the DNS records:
   ```
   dig +short TXT _dmarc.saltmarshdevs.io
   dig +short TXT saltmarshdevs.io
   ```
   - You need a `v=DMARC1` record and an `v=spf1` record that includes your platform.
2. Check how the platform signs mail.
   - Send yourself a digest and open "Show original" in Gmail.
   - In the `DKIM-Signature` header, `d=` should be `saltmarshdevs.io`. If it is the platform's domain, DKIM is not aligned.
   - Look at the `Authentication-Results` line. You want `spf=pass`, `dkim=pass`, and `dmarc=pass`.
3. In the platform's sending-domain settings, turn on custom DKIM for `saltmarshdevs.io` and a custom return-path (bounce) domain. Publish the CNAME/TXT records it gives you.
4. Add `_dmarc.saltmarshdevs.io` as `v=DMARC1; p=none; rua=mailto:<an address you read>` if it is missing. Start at `p=none`, then tighten later.
5. Confirm with a test send to an outlook.com address you control. It must arrive, in Inbox or Junk, with `dmarc=pass`.

**Then clean up the list:**

1. Export the full bounce list with its reason column. Count by status code:
   ```
   grep -c '5.7.515' bounces.csv
   grep -c '5.1.1' bounces.csv
   ```
   - Check whether the 140 are inside the 1,930 or on top of it. Anything that matches neither code needs a manual look.
2. **Remove the 5.7.515 contacts from the bounce/suppression list** and set them back to subscribed. Do this only after step 5 above passes. If the platform can't un-bounce in bulk, ask its support to reclassify them as "blocked", not "hard bounce".
3. Decide whether to re-send. These people missed last Thursday's digest. Options are to send them that issue as a late copy, or to let them catch the next one. If you re-send, do it in batches (say 500 at a time) and watch the rejection rate.
4. Find out why Thursday was different. Did the digest list pass a size threshold, or did anyone change DNS, DKIM keys, or the platform's sending setup recently? I can't tell from here. If it was a platform change, tell their support the error text, because other customers will have hit it too.

## 2. The 140 "550 5.1.1 user unknown"

These are real hard bounces: the mailbox doesn't exist. **Suppress them**, so a future import can't re-add them. Suppressing is better than deleting, because the platform keeps the record.

Before you do, sort the 140 by domain. A cluster of typos such as `gmial.com` or `hotmial.com` means you can fix and re-add those people. Also check whether they come from one old import or signup form. If so, fix that source.

## 3. Gmail spam reports: you can't get the names

Gmail never tells senders who clicked "Report spam". Postmaster Tools shows an aggregate rate only. No feedback loop, report, or API gives Gmail complaint identities, so you can't remove those people directly. Don't trust any tool that claims to.

**What you can do about the 0.4%:**

- ⚠️ **The rate is too high.** Google's guidance is to stay under 0.1% and never reach 0.3%. At 0.4%, inbox placement is at risk. Check whether 0.4% is a single-day figure on a small Gmail volume, where a handful of reports swings the number.
- **Find which segment drives it.** Add a `Feedback-ID` header (format `campaign:segment:type:yourid`) if the platform allows custom headers. Postmaster Tools then breaks the spam rate down by ID once volume is enough. That points to a segment or campaign, not to a person.
- **Remove likely complainers by proxy.** Suppress or move to a re-permission flow every Gmail subscriber with no open or click in the last 90–180 days. Check the other direction too: segments that grew recently or came from a bulk import are the usual source.
- **Make unsubscribing easier than reporting spam.**
  - Check a sent copy's headers for `List-Unsubscribe` and `List-Unsubscribe-Post: List-Unsubscribe=One-Click`. Gmail requires these for bulk senders. Most platforms add them, but verify.
  - Put a visible unsubscribe link at the top or bottom of the digest.
- **Remind people why they get it.** Add a line like "You're getting this because you signed up at …" and keep the From name recognizable.
- **Check for per-address complaints from other providers.** Microsoft (JMRP) and Yahoo do offer per-address complaint feeds. The platform's complaints list will show those complainers, and you should suppress them. Gmail will not appear there.

## Order of work

1. Fix DNS and DKIM, then run the test send (about 30 min plus propagation).
2. Un-bounce the 5.7.515 contacts, and decide on a re-send.
3. Suppress the 140 true bounces.
4. Add the `Feedback-ID` header and suppress inactive Gmail subscribers before the next send.
5. Re-check Postmaster Tools for 3–5 days after the next send.

If you share the platform's name and a sample `Authentication-Results` header, I can say exactly which DNS records are missing.