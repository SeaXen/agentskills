# FenConf email plan: 1,200-address list, April 2 to June 18

**Recommendation:** build a calendar-driven campaign of 9 sends, not a lifecycle nurture tree. Branch on registration status and clicks, never on opens. Replace the re-engagement branch with one "stay or go" email and then a sunset.

I checked the calendar assuming the event is in 2027. If it's a different year, recheck the weekdays and holidays below.

## 1. Why I didn't build the branching nurture

1. **The list is small and the window is fixed.** The window is 11 weeks. If 3-5% of 1,200 click a given email, that's 36-60 people. Splitting them into engaged and quiet branches leaves cells of a few dozen. You can't test or learn from cells that small, and every branch costs you copy.
2. **Open data is unreliable.** Apple Mail Privacy Protection and corporate security scanners inflate opens, and scanners also trigger clicks. In a developer audience, "opened" mostly means "has an Apple device or a spam filter". Use real clicks and, better still, pricing-page and checkout visits.
3. **Event nurture follows the calendar, not the contact.** Everyone is counting down to the same three dates. What matters is who has already bought, because buyers must never get a "buy now" email. Most of the effort goes into the suppression sync, not the branching.
4. **Quiet people don't need different content.** They need a new reason to care. The agenda drop is that reason, and everyone gets it.

⚠️ **Hard dependency:** the ticketing platform must feed buyers back into your email tool before every send. Daily sync is the minimum, and run it again right before emails 8 and 9. If a buyer gets "last call", you've lost credibility with a list that small.

## 2. Calendar traps

- **Thu May 6 is Ascension, a public holiday in France, and Fri May 7 is a bridge day.** Publish the agenda on the site and social on May 6 as planned, but send the email **Mon May 10**. A holiday send will underperform badly.
- Mon May 17 is Pentecost Monday, so there are no sends that day.
- **Fri Apr 2 is a weak B2B send day, but the announcement date is fixed.** Send at 9:30 Paris time, then follow up on Thursday Apr 8 so the first week isn't one email.
- Doors on Fri Jun 18 means the last-call email goes out Tue Jun 15. Set registration to close Wed Jun 16 for badge printing.

## 3. Segments and rules

| Segment | Rule |
|---|---|
| **Buyers** | Leave the nurture track on purchase and move to the registered track (section 5). Suppress them from all sales sends. |
| **Not registered** | Get the 9-send track in section 4. |
| **Cold** | Zero clicks across sends 1-5 and not registered. Evaluated Thu May 20. They skip sends 6-9 and get the stay-or-go email instead. |
| **Unsubscribed or bounced** | Suppressed everywhere. |

- **Frequency cap:** no more than 1 marketing email per 3 days per person. Your product lifecycle emails count. Check whether current customers are on this list, because they'll hit the cap fastest.
- **Send window:** Tue-Thu, 9:30-10:30 Paris time, except the dates noted above.
- **Consent:** confirm the consent basis per segment before Apr 2. Stale prospects are where GDPR and deliverability problems come from. The sunset in section 6 helps both.
- **List hygiene:** if the list is more than 12 months stale, send a plain-text pre-warm to the engaged part first. A sudden 1,200-address blast on a quiet domain risks the spam folder.

## 4. Main track (not registered): 9 sends

Each send has one job and one CTA. Items marked `[ ]` need your input.

| # | Date | Job | Subject | Single CTA | Audience and variants |
|---|---|---|---|---|---|
| 0 (optional) | Thu Mar 25 | Warm the list | "Save June 18-19 for something new in Lyon" | Join the notify list | Date and city only. Tells people the announcement is coming. |
| 1 | **Fri Apr 2** | Announce | "FenConf: our first developer conference, Lyon, June 18-19" | Get your ticket | Everyone. Cover what, who, where, when and price. State the format honestly: first edition, 2 days, [N] attendees. |
| 2 | Thu Apr 8 | Who it's for | "Who FenConf is for (and who it isn't)" | See what you'll leave with | Everyone not registered. Name 3 concrete takeaways and 1-2 customer or speaker quotes. |
| 3 | Tue Apr 20 | Speaker reveal | "First speakers at FenConf Lyon" | Read the speaker lineup | Everyone not registered. Show 3-4 speakers with talk topics. |
| 4 | Tue Apr 27 | Remove the budget blocker | "Need budget approval for FenConf? Send this email" | Copy the manager email | Everyone not registered. Include a ready-made justification, an itemized cost and a group-discount line `[if any]`. This matters because paid developer events are usually approved by someone else. |
| 5 | **Mon May 10** | Agenda | "The FenConf agenda is live: [N] talks, 2 days" | Build your schedule | Everyone not registered. Lead with the 3 strongest sessions. Tag clicks by track if you have 2 or more. |
| 6 | Thu May 20 | Deadline | "Early pricing ends tomorrow night" | Buy at early price | Skip cold. Pricing-page clickers get a line referencing the sessions they clicked. |
| 7 | Tue Jun 1 | Make it real | "Getting to FenConf: Lyon, the venue, and day one" | Pick your ticket | Skip cold. Cover the venue, trains and hotels, evening social, and a short "what the first conference attendees will see". |
| 8 | Tue Jun 8 | Last price move | "10 days to FenConf: final pricing and seats left" | Reserve your seat | Skip cold. Use "seats left" only if it's true. |
| 9 | **Tue Jun 15** | Last call | "Last call: FenConf registration closes tomorrow" | Register now | Skip cold. The sync must run immediately before this send. |

⚠️ **Pricing needs your decision, not mine.** I recommend one real early-bird deadline that falls after the agenda email, so the agenda drives the conversion. I haven't invented a discount. If you have no tiered pricing, drop send 6 and turn 8 into the single deadline.

## 5. Automations and the registered track

**One behavioral automation worth building: the checkout nudge.**

- **Trigger:** clicked a ticket or pricing link, no purchase after 48 hours.
- **Content:** one plain-text email: "Questions before you buy? Reply to this."
- **Limits:** once per person per 14 days, and never within 3 days of a campaign send.
- **Why:** this is the only place a one-to-one behavior signal beats the calendar.

**Registered track (nurture exit on purchase):** these are logistics emails, not nurture.

| # | Timing | Content |
|---|---|---|
| R1 | Instant | Confirmation, invoice, calendar file |
| R2 | 7 days after purchase | "Bring a teammate" (only if purchased before May 1) |
| R3 | Mon May 10 | Agenda live; build your schedule |
| R4 | Tue Jun 1 | Travel, venue, accessibility, dietary needs |
| R5 | Mon Jun 14 | Badge pickup, Wi-Fi, community channel, speaker Q&A |
| R6 | Thu Jun 17, 18:00 | "Doors tomorrow": QR code, times, address |
| Post | Mon Jun 21 | Thank you and a 3-question survey |

## 6. Re-engagement branch: one email, then a sunset

1. **Thu May 20:** evaluate. Cold means no clicks across sends 1-5 and not registered.
2. **Tue May 25, cold only:** send "Should we keep emailing you about FenConf?" with three one-click choices:
   - Keep me updated.
   - Only tell me about the recordings and next year.
   - Unsubscribe.
3. **Responses:**
   - Keep me updated: back into sends 7-9.
   - Recordings and next year: moved to a post-event list.
   - Unsubscribe: suppressed.
4. **No response by Jun 1:** suppress from all FenConf sends. Don't send a 4-touch win-back.

A cold contact who ignored five sends is unlikely to buy now, and mailing them again costs you deliverability. The preference choice also leaves you a clean list for next year.

## 7. Measurement and expectations

- Tag every link: `utm_source=email&utm_campaign=fenconf&utm_content=send-N`. Add a "how did you hear about FenConf?" field to checkout. This is your only protection against last-click over-credit.
- Track per send: clicks to the pricing page, checkouts started, tickets bought, unsubscribes, and the spam-complaint rate from the ESP. Ignore opens except as a rough deliverability check.
- **Rough expectation, which is my assumption and not a benchmark:** an owned list of 1,200 usually converts to tens of tickets, not hundreds. Replace this with your own numbers from past webinars or launches. If your ticket target is above ~60-80, email alone won't get you there.
- Other levers to plan for: speaker and sponsor promotion kits, community partners, and employee referrals.
- **Review points:** after send 3 (Apr 21), after send 5 (May 12) and after send 6 (May 21). Move budget or channels if tickets are under 25% of target by May 21.

## 8. Effort and work to do now

- **Copy:** 9 main emails, 6 registered emails, 1 nudge and 1 stay-or-go. That's about 17 emails, with few variants.
- **Variants:** only send 6's pricing-clicker line and the tagged-track links in send 5 differ by segment.
- **By Mar 12:** ticketing-to-ESP sync tested end to end, including suppression of a test buyer.
- **By Mar 19:** emails 1-4 drafted and approved. Speaker commitments for send 3 confirmed.

## Decisions I need from you

1. Which ticketing platform and which email tool? Does the ticketing platform sync buyers to the email tool, and how often?
2. What's the ticket target and the venue capacity?
3. Are there tiered prices, and is there a group or team rate?
4. Are customers on the 1,200 list, and how old is the list on average?
5. Do you have 3-4 speakers confirmed before Apr 20?