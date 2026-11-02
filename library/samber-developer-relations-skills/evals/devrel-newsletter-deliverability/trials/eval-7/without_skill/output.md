**Next action (2 min):** Do not pay the $299. Open the 4 MXToolbox results and write down which lists they are and which IP or domain each lists.

## 1. Blocklists: skip the $299

- UCEPROTECT levels 2 and 3 list whole netblocks or ASNs, not your sending behavior. Your ESP's neighbors can put you there.
- Major mailbox providers (Gmail, Outlook, Yahoo) mostly ignore UCEPROTECT and similar small lists. Spamhaus is the list that matters, and it shows nothing.
- Paid "delisting from all" is the business model for some of these lists and their resellers. UCEPROTECT sells expedited delisting itself. Treat the offer as a paid shakedown, not a fix.
- Do this instead (about 20 minutes):
  1. Note each list name and what it lists: your sending IP, your domain, or your provider's block.
  2. If it is your ESP's shared IP or range, tell the ESP. Delisting is not your job.
  3. If it is your own dedicated IP, check the list's lookup page for the reason. Most delist free after 7 to 14 days of clean sending.
  4. Check Google Postmaster Tools for domain and IP reputation. That is real Gmail data, which MXToolbox is not.

## 2. The 92% seed test

- It does not show you are fine. Seed tools usually count Promotions as "inbox". A newsletter in Promotions can score 92% while Primary placement is 0%.
- Seed accounts are not real recipients. They carry no engagement history, so they say little about reputation.
- Check the report's split: inbox tab vs spam vs missing. The 8% is the number to look at.

## 3. Getting into Primary

Honest take: a marketing-style newsletter lands in Promotions by design. Gmail's classifier is per-user and not controllable. Nothing below is guaranteed. Ranked by effect:

1. **Ask readers to move it.** Put one line in the email: "In Gmail, drag this to Primary." Gmail remembers that choice for that sender per user. This is the only reliable lever.
2. **Look like person-to-person mail.** Use a real sender name and address ("Sam at Tidewater", not "Tidewater Updates"). Write mostly plain text. Use no more than 2 or 3 links. Use no images, buttons or banners. Avoid heavy HTML templates and tracking-heavy link wrappers.
3. **Get replies.** End with a real question and send from a reachable address, not no-reply. Replies and contact-adds train Gmail more than anything else.
4. **Keep the unsubscribe headers.** Do not remove `List-Unsubscribe` and one-click unsubscribe to dodge the Promotions tab. Gmail and Yahoo require them for bulk senders, and removing them hurts deliverability.
5. **Split the streams.** Send breaking changes and deprecation notices as a separate plain, short, low-link "API notice" from its own sender. Gmail treats it differently from the marketing digest. Sunset deadlines should not sit in Promotions.

## 4. Basics to confirm

- SPF, DKIM and DMARC all pass and align.
- Spam-complaint rate in Postmaster Tools is below 0.1%. Gmail's limit is 0.3%.
- The list is opt-in and you prune non-openers.

## 5. Rethink the goal

A changelog is an expected, subscribed email. Promotions is not spam and it is not a delivery failure. If opens are healthy, the cost is small. Measure the open rate and replies before spending effort on tab placement.

**Next:** run step 1 of the blocklist list above (name the 4 lists and what each lists). Then paste them here if you want me to say which, if any, matter.