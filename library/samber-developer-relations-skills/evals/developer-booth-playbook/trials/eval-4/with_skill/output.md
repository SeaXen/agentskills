# Booth staffing plan: 20x20, 3-day Python conference, hall 9:00-18:00

**Next action:** don't plan 8 on the booth at all times. Treat 8 as your roster, put about 3 on the floor per block (4 at peaks), and put an engineer on every block.

Figures are labeled **[yours]**, **[convention]** or **[assumed]**. Confirm the assumed ones before the event.

## 1. Why 8 at all times fails

- **The 50 sq ft figure is a ceiling, not a target.** [convention] It is an exhibit trainer's rule of thumb repeated in organizer kits, with no study behind it. 400 sq ft ÷ 50 = 8 is the most the space can hold. Staff who outnumber visitors form a closed group that nobody walks into.
- **Headcount comes from conversations.** The method is:
  - Two per shift, at least one able to debug a stranger's code.
  - Plus one per demo station.
  - Plus one optional peak slot, filled only once the shift log shows visitors leaving a queue.
- **8 at all times is arithmetic you can't staff.** [yours: 8 people, 9-hour hall, 3 days] It means 8 × 9 h × 3 days = 216 floor-hours from 8 people. That is 9 hours a day on the floor each, with no breaks and no talks.
- **It also guarantees the failure you flagged.** Six of the eight would be non-engineers, so most hours nobody could answer "how does this behave at scale?" Conversations would end at the first follow-up question.

## 2. Headcount

- **Base:** 3 on the floor per block, which is 1 engineer, 1 qualifier and 1 demo driver. **[assumed]** This assumes one demo station. With two stations, add one driver per station.
- **Peak:** 4 on the floor, filling the optional slot only when the log shows a queue.
- **Floor-hours:** 27 per day base and 36 per day at full peak, so 81-108 over three days against 216 for the 8-at-all-times plan.
- **Roster:** the 8 people cover this with room for off-floor time.

## 3. Engineer coverage (2 engineers, 4 blocks a day)

With 4 blocks a day and each engineer capped at 2 blocks a day, the 2 engineers cover all 4 blocks exactly. Each works two non-consecutive blocks, so every block has one person who can debug.

| Block | Engineer | Qualifier | Demo driver | Optional peak slot |
|---|---|---|---|---|
| B1 9:00-11:15 | E1 | N1 (**captain**) | N2 | N3 |
| B2 11:15-13:30 | E2 | N3 | N4 | N5 |
| B3 13:30-15:45 | E1 | N5 | N6 | N2 |
| B4 15:45-18:00 | E2 | N1 (**captain**) | N4 | N6 |

- **Blocks:** 2h15 each, inside the 2-3 hour guidance [convention, agency advice, not fatigue research], with a 15-minute overlap to hand over open conversations by name. Doors open at 9:00, so B1 starts with setup beforehand.
- **Captain:** N1 is a marketing or CS lead. They work B1 and B4, which means they open and close the day, and are reachable the rest of the time. They own the brief, the rules table, the log and the end-of-day review.
- **Drivers:** the demo driver needs the demo path, not engineering depth, so CS staff fit this role well. A driver never qualifies while driving.
- **Everyone but the captain and one other is on the floor at most twice a day.** Nobody works a full day.
- **Rotation:** swap E1 and E2 between mornings and afternoons each day, and rotate N2-N6 one position per day.
- **Off-floor:** everyone off the floor does log clean-up, restocking, hallway conversations and sessions. Engineers off the floor stay **reachable within minutes**: on-site, on a shared chat channel, never on a call-heavy errand.

### The trade-off to accept

- **No block ever has two debug-capable people.** If two hard questions land at once, one visitor waits for the engineer.
- **Engineers pay for the coverage.** Each spends 4.5 floor-hours a day and is on call the rest, for three days. Count this as engineer-days off the roadmap.
- **Can any CS person debug the product for a stranger?** Each one who can adds coverage, so one engineer could drop to a single block on day 3, or you could double up at peaks. Tell me who and I'll redo the grid.

## 4. Non-engineer rules (the 6)

Brief everyone for 30-45 minutes before the show, and run each driver through the demo path once. **[assumed]** Cover these points:

1. **Opener is about their work, not the product.** Use "What are you building at the moment?" and "What's the most annoying part of [problem space] right now?"
2. **Three qualifying questions:**
   - "How do you handle that today?"
   - "Who else on your team deals with it?"
   - "Would it help to [concrete next step] next week?"
3. **Never guess a technical answer.** Use the hand-off line: "Priya built the part you're asking about. Priya, they're running [stack] and hitting [problem]." If the engineer is off-floor, promise a dated answer, which becomes the named next step, and log the question.
4. **Log unanswered questions.** If the same question comes up three times, write the answer on a card and send it to docs.
5. **Etiquette:** stand at the front edge facing the aisle, no laptops or phones out except to help someone, at most two staffers talking to each other at once, and eat and take calls off the floor.

## 5. Conversation bar

- Use the qualified-conversation definition and minimum count from your sponsorship plan. If none exists, set one yourself and label it self-set.
- **Grade A** means the attendee has the problem now, builds with or influences the decision, and agreed a named next step.
- **Grade B** means they have the problem but no next step. **Grade C** means they are curious or here for swag.
- Only A counts toward the minimum, and B is reported beside it as warm interest. Scans are activity, reported separately.
- **Placeholder, not a target:** I need your minimum A count (Q3). Divide it by 3 to get the daily share, which is what the end-of-day-one review checks against.
- Every record carries grade, problem in the attendee's words, stack, role, next step, owner, route, consent basis, and who captured it and on which shift. Grade at capture, never at the hotel.

## 6. Show loop

1. **End of every shift (5 minutes):**
   - Complete open records.
   - Count A, B and C.
   - List unanswered questions.
   - Pass open conversations to the incoming shift by name.
2. **End of day one:** the captain reads A against the daily share and adjusts day two.
   - A well under share: put engineers on peak blocks and rewrite the opener toward the problem.
   - Queues at the booth: fill the optional peak slot.
   - Mostly C: move the sticker off the front edge so the opener comes first.
3. **Day three:** traffic often drops on the last day [assumed, check last edition's notes]. If it does, drop the optional slot.
4. **Same-day debrief (30 minutes) when the hall closes:** A vs the minimum, B beside it, scan count as activity, top three unanswered questions, and what to change next edition. The graded log, each A with its owner and date, then goes to follow-up.

## 7. Exhibitor rules to check first

Fill these from **this event's** exhibitor manual, never from another event. Rules flip between events.

- **Is the booth required to be staffed during all hall hours, and is there a fee or penalty?** Some shows make an empty booth a breach. This is why every block above has someone on it.
- **How many staff passes does the package include?** A roster of 8 needs 8 passes. If you have fewer, the roster shrinks, and I'll rebuild the grid.
- Who counts as staff and what badge rules apply.
- Teardown time, lead retrieval, giveaways, draws, soliciting outside the booth, recruiting, lanyards, and any code of conduct staff must sign.

## 8. What I need from you

These change the plan. Q3 and Q5 are the ones that matter most:

1. **Q2:** staff passes and lead retrieval in the package: how many passes, and does it include lead retrieval? No lead retrieval means a hand-written conversation log instead of scanning.
2. **Q3:** your minimum A count and the exact A wording.
3. **Q5:** can any of the 6 non-engineers debug the product for a stranger?
4. **Q6:** keynote and break times, so I can replace my peak-block guesses.
5. **Demo stations:** how many?
6. **Q10:** how many engineer-days can you pull off the roadmap, and who owns the log afterwards? If the answer is "very few", I'd cap the crew at two per shift and use the crew-of-two rules.