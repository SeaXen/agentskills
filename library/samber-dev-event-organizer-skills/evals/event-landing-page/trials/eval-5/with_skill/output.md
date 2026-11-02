# PortsideJS go/no-go: ❌ NO-GO for Thursday as it stands

Six of the seven items are fixable well before Thursday. The seventh, the checkout accessibility, can fail the launch on its own. I haven't seen the live site, so this is based on your description. Gate items 1 and 2 are unverified.

⚠️ **Date check:** my system date is 2026-10-14, after October 8-9. If this is the 2026 edition, the event has already happened and none of this applies. If it's a different year, ignore this.

## Why four of these are one problem

The headline, the price, the early-bird date and the JSON-LD are all facts that arrived already decided. The team changed three of them for taste ("punched up", "looked odd", "seemed arbitrary"), and the fourth is stale from a draft. Each change creates a second source of truth that attendees will screenshot. The fix is to present what arrived and send any real change back to the owning sibling skill.

## Fixes, in order

| # | Issue | Verdict | Fix | Owner and time |
|---|---|---|---|---|
| 1 | Hero says "Where the JavaScript elite ship the future" | ❌ | Restore the agreed line verbatim, including "There are many rockstar-speaker events. This is not one of them." The new line is the "rockstar" pitch the agreed line rejects, and it names no audience. To change positioning, go back to `event-positioning`. | Page owner, 5 min |
| 2 | Ticket shows €300, sheet says €289 | ❌ | Show €289. Rounding a price is an override. Also check what the checkout actually charges: if it charges €289, the page now advertises a price nobody pays. | Page owner, 10 min. Pricing questions go to `event-ticket-pricing`. |
| 3 | Early-bird deadline shown as Sept 1, sheet says Aug 22 | ❌ | Show Aug 22, or whatever the sheet says. An invented cutoff is a scarcity line the ladder doesn't support. Also check that the early-bird rung isn't already expired on launch day; if it is, it shouldn't display as live. | Page owner, 10 min. If the date really is wrong, `event-ticket-pricing` changes it. |
| 4 | "Submit a Talk" still live, CFP closed 2 weeks ago | ❌ | Remove the button and the CFP section. Don't replace it with a "submissions closed" notice, which is a placeholder in different words. Show Register as the single primary CTA, with Contact unconditional. | Page owner, 10 min |
| 5 | JSON-LD says Oct 1-2 | ❌ | Set `startDate` to Oct 8 and `endDate` to Oct 9, then check that `name`, `url`, `image` and `location` match the visible page. Run a structured-data validator. | Page owner, 15 min. This is the one check a script can confirm. |
| 6 | Checkout date-of-birth calendar is mouse-only | ❌ **Blocks launch** | See below. | Ticketing provider, plus `event-accessibility-inclusion` owner |
| 7 | 9% conversion target | ⚠️ Drop it | See below. | Marketing |

## Item 6: do not defer this one

Registration must be completable with the keyboard alone, including any date picker and the payment step. Someone who can't get through checkout doesn't attend, and no on-site provision fixes that. Retrofits after launch rarely get scheduled. Because the checkout is the provider's, it's the most likely item to run past Thursday.

1. **Today:** ask the provider to replace the widget with a plain typed field, or to make it keyboard-operable. Also ask whether the date-of-birth field is required at all.
2. **If they can't fix it by Thursday:** publish a named person with an email or phone route to register, and tell the owner of `event-accessibility-inclusion`. An unusable registration path is a provision-level fact their accessibility page has to state.
3. **The alternate route doesn't turn this into a pass.** Strictly, the gate still fails until the keyboard pass succeeds. Launching on the alternate route is a risk decision for the accessibility owner, not the page team.
4. Run the full keyboard pass on the real checkout, not a mock, and don't rely on an automated score.

## Item 7: no number to defend

- This skill quotes no conversion rate for event pages. Published figures come from SaaS and paid-traffic funnels, so 9% is false precision.
- A 400-person event page won't reach the roughly 1,000 sessions needed to test anything. A single edition has no second run to iterate on.
- Replace the target with the pre-launch gate below. Any ticket-sales target per phase belongs to `event-marketing-plan`.
- Do track which per-channel link brought each visitor, and whether any section promises content past its date.

## The four-check gate

All four must pass, or the page doesn't go live. These checks are this skill's own construction, not a published standard.

1. **Every CTA transition has a date, an owner, and has fired:** ⚠️ Unverified. The Propose button still being live shows it didn't fire. Build the transition table with a named person per row, and set reminders one day before each date.
2. **What, who, when, where and cost are answerable in one phone screen:** ⚠️ Unverified until fixes 1-3 are in. Hand it to someone who has never seen the event.
3. **Structured data validates with the real dates, location and URL:** ❌ Fails now (Oct 1-2). Fix 5 resolves it.
4. **Registration completes by keyboard alone:** ❌ Fails now. Item 6.

## Verdict

- **Changes to ship today:** fixes 1-5, about an hour in total, then re-run gate checks 2 and 3.
- **Becomes GO when:** checks 1-3 pass, and check 4 passes or the accessibility owner explicitly signs off on a staffed alternate route.
- **If the provider can't commit to a fix by Wednesday,** slip the launch rather than ship a broken checkout. The campaign date is the cheapest thing here to move.