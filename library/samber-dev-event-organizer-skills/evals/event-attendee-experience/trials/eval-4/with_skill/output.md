# KernelCamp lunch plan: dietary distribution

**Verdict:** the data you collected is good. Two of the three planned mechanics would fail on the day, and a third creates a privacy problem. Fix those and the plan holds.

Source labels: **(skill)** means published practice from the event-attendee-experience skill and its references. **(self-set)** means my default, which you should adjust.

## 1. Your plan, item by item

| Your plan | Verdict | Why |
|---|---|---|
| One long buffet, small labels, self-serve | ❌ Change | A restricted meal sitting in the general line is taken by the wrong person, and the person it was ordered for goes without (skill, top failure mode). A 12-point "gluten-free" label does not stop that. For 2 nut allergies it also does not control cross-contact, because a shared serving spoon is not an allergen control (self-set). |
| One announcement, "lunch is served", to the whole room | ❌ Change | It floods one line with 435 people at once. Stagger by room or table, then make a final call once the flow thins (skill). |
| Spreadsheet filed with the registration export for next year | ❌ Change | Dietary answers are health data in several jurisdictions. Keep the printed list for meal service only, then destroy it. Do not file it with the registration export (skill). |
| Collected from ticket buyers only | ⚠️ Gap | The 25 volunteers and 10 mentors eat too. Ask everyone who receives a meal, not only ticket holders (skill). |
| Caterer "confirmed they can prepare all of it" | ⚠️ Verify | Confirm what that means per category, as described in section 2, step 5. |
| Pre-collecting restrictions | ✅ Keep | This is the published "collect in advance, serve from a separate table" model (skill). |

## 2. The fix: dietary distribution choreography

Do these in order.

1. **Close the staff gap first.**
   - Send the same dietary question to the 25 volunteers and 10 mentors now, with a firm deadline before the caterer's headcount date.
   - Ticket buyers declared 51 restrictions among 400, about 13%. On that rate, expect roughly 4 more from the 35 staff (self-set estimate). Replace it with real answers.
   - Give the caterer the final per-category count and a small buffer for late additions.

2. **Check the category list against what you were handed.** Your list is vegetarian, vegan, gluten-free, kosher and nut allergy. The skill's reference list also includes halal, lactose and other allergies. The categories you commit to come from your accessibility bar, so I'm not adding any. If halal or "other" never appeared on the form, ask whether the omission was deliberate.

3. **Set up a separate restricted-meal table.**
   - All declared restricted meals sit there, not in the general buffet.
   - One volunteer holds a printed list, alphabetical by last name then first name, and checks each person off as they collect (skill).
   - Print only name, meal type and lunch number. Nothing else from the registration row goes on that sheet.

4. **Make the general buffet multiple serving lines.**
   - Never use one table, even at small scale (skill). For 435 people, plan 4 lines or more, each serving from both sides if the layout allows. The count is self-set, so size it to the walk and the room.
   - Keep the small labels. They help everyone with preferences, but they are no longer the fulfilment mechanism.

5. **Verify three things with the caterer, per category.**
   - Kosher: are the 3 meals certified and individually sealed, or "prepared kosher-style"?
   - Nut allergies: is there a separate prep surface and utensils, and is the meal packed and named for the person?
   - Gluten-free: is it plated or sealed apart from the gluten items?
   - Get the answer in writing. "They can prepare it" does not tell you the answers (self-set).

6. **Check people off at the head of the line.**
   - A greeter with the list catches anyone rejoining the queue.
   - A person with a declared restriction is redirected to their own table here (skill).
   - Look people up by name. Do not add a dietary marker to the badge. That would turn health data into a visible label.

7. **Stagger the announcement.**
   - Call by room, table or zone, a few minutes apart. Three to four minutes is a self-set starting point.
   - Give a final call once the flow has thinned (skill).
   - Open the restricted table at the first call so those attendees are never behind the general queue.

8. **Write a fallback now, for anyone the caterer cannot serve.**
   - Order a one-off meal from the same vendor, or give the person a delivery gift card.
   - Tell them in advance that they are buying their own meal that day. Telling them in advance is what makes it a fallback and not a failure (skill).

9. **Plan for volunteers and mentors at the meal.** Volunteers run these tables and lines, so decide when they eat. That scheduling belongs to the volunteer-experience skill, but they use the same restricted table when they declared a restriction.

10. **Repeat the setup for lunch 2.** The same list and the same table apply. Re-check names against the day-two roster if the two lunches fall on different days.

## 3. Next year: what to keep

- **Destroy the named dietary list after the last lunch.** Do not keep it for next year.
  - Restrictions change, and so do the people.
  - Last year's list reads as a current health record for people who never agreed to its reuse.
- **Keep only aggregate counts per category.** For example: "~13% declared a restriction, kosher 3, nut allergy 2, no names." With groups this small, aggregates are the safest useful trace. Use them to brief next year's caterer (self-set).
- **Recollect at next year's registration**, from everyone who will eat, with a deadline tied to the caterer's headcount date.

## 4. The debate: pre-collected vs. live per-meal requests

**Neither is objectively better.** The skill deliberately refuses to rank them. They are not options with different value per unit of effort. They are two shapes of catering contract, and the contract picks one. Ranking them would be false precision.

| | **Model A: collect in advance, separate table** | **Model B: live per-meal request** |
|---|---|---|
| Published example | MLH | PyCon US 2026 |
| How it works | Pre-collected list, restricted meals at a separate table, names checked off | A named catering staff member takes special requests (such as kosher or allergen-free) at each meal |
| Depends on | Early collection, and a list you handle responsibly | The caterer carrying that capability under contract |
| What you skip | Nothing on the day | A pre-collected list to match |

Your situation already decided it. You collected in advance and the caterer confirmed, so you are running Model A. The remaining work is execution, and the failure modes above are execution failures, not a model failure.

A cheap hedge, which is a self-set suggestion and not a published hybrid: ask the caterer for one named contact on site for late questions. That covers the case where someone has a restriction they never declared.

## 5. Walkthrough audit rows for the meal

Fill these in on a physical walk before doors open. I have not seen your venue, so check each pain point against the building.

| Touchpoint | Action | Emotion | Pain point (verify on walk) | Opportunity |
|---|---|---|---|---|
| Meals: arrival at lunch | Leaves the session room toward food | Hungry, impatient | All 435 head to the same door the moment the session ends | Staggered call by zone, plus a second path to the lines |
| Meals: restricted table | Person with a nut allergy looks for their meal | Anxious about getting it wrong | The table is not visibly signed, or sits behind the general queue | Sign it plainly by name ("Pre-ordered meals"), at the front of the room, with no health detail on the sign |
| Meals: head-of-line check | Gives their name to the greeter | Slightly exposed | The queue backs up while the greeter searches a long list | Alphabetical list with the greeter standing clear of the lines |
| Help moment | Asks where their meal is | Worried | No one at the restricted table knows who owns the problem | A named organizer-on-duty for meal problems, as the escalation path |

## 6. Measurement

Pick two. Write down what each would change next edition, and record both before doors open.

1. **Dietary fulfilment** (gate, skill). Every attendee who declared a restriction received the meal that was ordered for them. The target is zero misses, with no threshold.
   - *Would change:* the table location, the check-off process and the caterer contract.
2. **Unclaimed or wrong-person restricted meals** (skill, per-edition record). Count both, with the lunch number and what happened.
   - *Would change:* the headcount buffer, and whether the staff-collection gap mattered.

Also worth recording per edition, as hand-added signs: any sign you add by hand at lunch marks a decision point the design missed.

## 7. What I could not ask

- **Event days:** are the two lunches on different days or the same day? This changes whether to repeat the dietary check-off.
- **Registration gate:** I assumed paid tickets (a registration gate exists). If there is any walk-in registration, those people also need the dietary question.
- **Sibling decisions I did not touch:** the buffet as the catering service style belongs to event-hospitality, and the accessibility bar sets the category list. I only changed how the food reaches people.