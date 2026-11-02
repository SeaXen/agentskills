# Hospitality sanity-check: Loomhall Conf, next edition

Both fixes fail, for different reasons. I based this on the `event-hospitality` skill and its service-styles reference.

## Verdict

| Fix | Verdict | Why |
|---|---|---|
| Bigger laminated signs | ❌ Wrong diagnosis | Swapped cards are rarely a sign-size problem. The fault is usually upstream of the serving line. |
| Quiet voucher refund, tell the 3 at check-in | ❌ Fails the skill's own rule | The credit fallback is only acceptable when a one-off addition is genuinely unavailable, and only in advance. Learning on the day, at the serving table or at check-in, is "a failure" in the skill's words. |

## Fix 1: bigger signs

**What the incident tells us.** Two cards were swapped. Bigger print makes a wrong card easier to read. It does nothing about a card on the wrong dish.

The skill names this failure mode directly. A missing or wrong declaration starts where a delivery is received and nobody is assigned to capture the allergen detail and carry it through to plating. The fix is the handover step, "not just the sign".

**Replace "bigger signs" with these:**

1. **Name a receiver per delivery.** One named person receives each delivery and checks every dish against the caterer's written allergen declaration.
2. **Make the declaration come from the caterer.** Cards are printed from the caterer's dish-level manifest, not hand-written or re-typed on site.
3. **Add a second-person check before doors open.** Someone other than the receiver confirms each card sits on the dish it describes. Use the same check every time a dish is swapped or refilled.
4. **Keep the sign, but post the allergen detail early.** Post it before the line forms, for example the menu at check-in. A restricted attendee can then plan instead of interrogating a server.
5. **Stop relying on the line for declared restrictions.** At 500, a self-serve buffet fails one way: the wrong person takes a restricted dish. Cross-contact from shared utensils is a residual risk that no card removes. Serve declared restrictions as individually packaged labelled meals, matched by name, even if everyone else uses the buffet. The label travels with the food.
6. **Never run any dish unlabelled.** An unlabelled buffet is the one the skill deletes outright.

**Gates to track, both with a threshold of zero misses:**

- **Dietary fulfilment:** every declared restriction met at every meal.
- **Declaration completeness:** every allergen-carrying item has a readable declaration before it is taken.

**Two things I could not check:**

- I don't know how your cards were produced or placed last edition. A short root-cause note from the team would show which handover step broke.
- The sick attendee is outside this skill's scope. I would still make sure someone owns direct follow-up with them.

## Fix 2: quiet refund for the 3 kosher meals

**Why it fails:**

- **Timing.** The skill allows a credit only when a one-off addition to the standing order is genuinely unavailable, and only if the person is told in advance. Telling them at check-in leaves "every remaining option … a delivery credit nobody can spend".
- **"Quietly."** This is a religious accommodation the event was asked to carry. Concealing the change moves the work onto the people it was meant for. It also separates them from the room while everyone else eats together.
- **Who decides.** Which dietary needs the event commits to belongs to `event-accessibility-inclusion`. Hospitality chooses a style that can carry that list and does not drop items from it.

**Do this instead, in order:**

1. **Route to `event-vendor-sourcing` now.** Ask whether the caterer can add the three meals as a one-off addition, or whether a separate certified kosher supplier can supply sealed meals. The skill treats "can the supplier meet the dietary counts inside the standard order, or does it need a separate small order" as a selection criterion.
2. **Check the venue.** Ask whether outside food may enter (Q2/Q6), and whether a mandated caterer blocks a second supplier. Neither answer is in your brief yet.
3. **Hand the packaged meals out as named, labelled items** through `event-attendee-experience`. A sealed meal is the natural fit.
4. **Only if step 1 genuinely fails, tell the three now.** Do it directly and well before the event. Explain the situation, offer a delivery credit sized to a real kosher meal, and let them choose. The person must be able to arrange their own meal.
5. **Re-count.** "Three" is the number requested. The skill requires dietary counts from everyone fed: attendees, speakers, volunteers, organizers and sponsor staff. The real kosher count may be higher.

## Open inputs before I write the full brief

I need these from you and have not assumed them:

- The **expected-show-up figure** from `event-no-show-management`. "500 expected" is a registration-style number until that skill confirms it. Catering should be ordered against expected show-up, with the gap to registrations stated separately as buffer.
- The **dietary categories and depth** the accessibility bar commits to.
- **Venue and supplier answers:** mandated caterer, outside food, who may serve, and chafing or open-flame limits.
- Whether the **caterer's contract** still allows a change of supplier or an addition.

## Record for next edition

- Declared counts against counts served.
- Which restrictions the caterer could not cover, and the fallback used.
- The longest meal queue.
- Who handled each delivery handover.

Should I write the full hospitality brief next, covering style, counts, fallbacks, break content, alcohol posture and evening decision? I would present it section by section for your approval before anything is ordered.