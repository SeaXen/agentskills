# Verdict: NO-GO as the page stands. Likely GO by Thursday once the fixes below are done.

Five of the seven items are quick copy or data fixes. Two need a decision from you.

## ❌ Blockers (fix before Thursday)

| # | Issue | Fix | Effort |
|---|---|---|---|
| 1 | Hero says "Where the JavaScript elite ship the future" | Restore the agreed line: "A JavaScript conference for maintainers, not influencers. There are many rockstar-speaker events. This is not one of them." The current line contradicts the positioning. "Elite" is the rockstar framing the agreed copy rejects. | 5 min |
| 2 | Ticket price shows €300, but the sheet says €289 | Show €289. "Looked odd" is not a reason to change a price. A page price that differs from checkout is a consumer-protection problem. Ask the sheet's owner whether €289 is intended. | 5 min plus one question |
| 3 | Early-bird deadline shows Sept 1, but the sheet says Aug 22 | Use the sheet's date, or have the owner confirm a new one. Moving the deadline silently commits you to selling at the early-bird price for 10 more days. The ticketing provider's cutoff must match the page. | 10 min plus one question |
| 4 | "Submit a Talk" button is live and the CFP closed two weeks ago | Remove it, or replace it with "CFP closed, speakers announced". A live dead-end button on launch day looks sloppy. | 5 min |
| 5 | JSON-LD says Oct 1-2, but the event is Oct 8-9 | Fix `startDate` and `endDate`. Google event results and AI answers will otherwise show wrong dates. While you're there, check `offers.price`, `validThrough`, the venue, and the CFP or other draft leftovers. | 15 min |

## ⚠️ Needs your decision: checkout accessibility

The date-of-birth calendar widget works only with a mouse. That fails keyboard access (WCAG 2.1.1) at the exact step where buyers pay. "Fix after launch" is risky here, for two reasons:
- Keyboard and screen-reader users cannot buy a ticket. You would be paying for traffic that cannot convert.
- The European Accessibility Act has applied to e-commerce in the EU since June 2025. A microenterprise exemption may cover you, but I can't confirm that from here. Check it.

Before Thursday, do these in order:
1. Ask the provider whether the DOB field can become a plain typed input. Many providers offer this as a setting.
2. Ask whether you need DOB at all. Dropping it is also better data minimization.
3. If neither works, publish a fallback, such as "email us to buy a ticket", and get a written fix date from the provider.

I would call this a go with the fallback in place. I would not call it a go with nothing in place.

## ⚠️ Fix the target, not the page: 9% conversion

9% is far above what a paid-ticket landing page normally reaches. Benchmarks for free sign-ups or general landing pages run in the low single digits. A €289 ticket should convert lower. If you launch against 9%, a healthy campaign will read as a failure by Friday.

Rebuild the target from the goal:
- Define the denominator: unique visitors to purchases.
- Work back from how many tickets you need to sell.
- Set the target as a range, such as a floor, an expected rate, and a stretch rate.

## ℹ️ Check the dates

The environment date I see is 2026-10-14. If that is right, October 8-9 and both deadlines have already passed. I assume the event is in a future year, but confirm that the page, JSON-LD, and checkout all carry the same year.

## Root cause worth fixing

Three of these items come from someone "correcting" a value that looked odd: price, deadline, headline. Name one source of truth for the brief and the pricing sheet. Before launch, a second person should diff the live page, JSON-LD, and checkout against it.

## Next action

Send the two questions today: the €289 and Aug 22 confirmation to the sheet's owner, and the DOB-field options to the ticketing provider. Do the copy fixes (items 1, 4, and 5) while you wait for the answers.

I can draft the JSON-LD block or a pre-launch checklist if that helps.