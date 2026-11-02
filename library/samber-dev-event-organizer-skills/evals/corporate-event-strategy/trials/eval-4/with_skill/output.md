# Solvi Sessions: goal-setup review and reporting plan

I followed `corporate-event-strategy`, including both reference files. I haven't run the full interview yet, so some answers below are assumptions. Section 6 lists the ones that would change the recommendation.

## Verdict

The goal setup is not right as written. Two points hold up and two don't.

- ❌ **"Developer goodwill" can't stay as a goal.** Product is putting in half the money. A funder won't accept a goal with no number attached, and goodwill has none. Once a function co-funds, goodwill-only is deleted from the menu, not ranked last. If it stays, it becomes the fallback the team retreats to when instrumentation runs late. Keep it as a rule for how the event behaves, not something you report.
- ❌ **"700 attendees" can't be a goal.** Heads through the door is a capacity fact, not an outcome. It is also the number marketing will report if the real number arrives late. The skill deletes it from the goal menu for that reason.
- ❌ **The deck doesn't mention the reason product is funding.** Product wants feedback on inference caching. That is an adoption goal, and the deck doesn't state it.
- ✅ **The funding split is probably right.** Marketing and product co-funding fits all three conditions: product has pushed for the event all year, the program is annual, and the goal should be adoption-first.

## 1. Audience: wanted versus assembled

- **Wanted:** the wider ML-engineering community. That is the 700-person ambition.
- **Assembled (assumed):** Solvi's own users and customers, plus whatever reach marketing buys.
- ⚠️ **The gap:** the adoption metric can only be measured on attendees you can match to product accounts. Community members who don't use Solvi can't be measured. If most of the 700 are outside the product, then either the goal depends on an acquisition campaign nobody has budgeted, or the adoption number comes from a minority of the room.
- **Action:** decide how many seats go to existing users. The matched-account count sets the sample for the adoption metric, so it is a planning input and not just a registration figure.

## 2. Buyer and user

- **Open (Q3):** does the engineer who attends also sign for Solvi? A model-serving runtime often has a separated buyer: a platform lead or a manager.
- **Effect on this event:** none for an adoption goal, because adoption reads on usage and not on purchase.
- **Rule for later:** if anyone proposes a pipeline number, state it as influence unless the buyer is the attendee.

## 3. Goal mix

**Recommendation: adoption-first**, with goodwill as a behavior constraint.

- **Goal:** attending accounts activate inference caching at a higher rate than comparable accounts that didn't attend.
- **Why it fits:** it maps to product's feedback request. Feedback is an input to product, but an input is not an outcome. The outcome that shows the feature landed is activation.
- **Constraint, not a goal:** the event stays practitioner-led, with no sales pitch in the sessions. That protects the goodwill the community expects without adding a second number to report.

**Rejected rungs:**

| Rung | Why rejected |
| --- | --- |
| Goodwill only | A co-funder is present, so it is deleted. |
| Attendance count | Capacity fact, not an outcome. |
| Pipeline-first | It needs a hard reporting date, a room that is mostly non-buyers, and an existing join to the sales systems. None is established. It would also bring in a sales veto that has no metric in this goal. |
| Blend | It needs both joins and a named reconciliation owner. Revisit in year 2 or 3 if the annual program compounds (see section 6). |

The rejected list stops the goal from quietly widening later, for example when sales asks for leads.

## 4. Budget ownership

**Marketing and product co-funded, 50/50.**

| Funder | What they buy | What they get | What they don't get |
| --- | --- | --- | --- |
| Product | Access to users at depth and structured feedback on inference caching. Their metric is the activation result. | A say over audience composition (how many seats go to existing users) and over a defined share of program slots. | Control of the whole program, or the event as a launch vehicle. |
| Marketing | Developer standing, which here is a constraint on how the event behaves. Marketing can use the event's reach and content afterwards. | Ownership of format, date, and everything outside product's two claims. | It carries no number of its own. See the risk below. |

- ⚠️ **Marketing's number:** marketing co-funds an event whose only reported number lives in the product organisation. Marketing has to be able to say what it bought. Fix: marketing co-owns the adoption goal and its report, and it reports on the same metric as product. Agree this now, not in the post-event review.
- **Positioning risk:** product co-funding often turns into using the event as a launch vehicle. If that starts, send the conflict to `event-positioning` instead of absorbing it as a program argument.
- **Single point of failure:** the line is now two functions. It survives one leaving, not two. Write the handover document when the agreement is made, not when someone departs.
- **Open (Q4):** who owns the budget line today? If nobody does, or the three answers disagree, name an owner before anything else.

## 5. Measurement commitment

Write this before registration opens. A goal missing any of the four fields is an intention, not a goal. All thresholds are self-set, because industry figures don't transfer between companies.

| Field | Adoption goal |
| --- | --- |
| **Metric** | Share of attending accounts that activate inference caching in the window between the event and the close of the next quarter, compared with the same share for a matched set of non-attending accounts. |
| **Owner** | `[name]`, in the product org, someone who already reports capability activation. |
| **Source system** | Product telemetry that identifies accounts. This must exist; if it is a spreadsheet someone assembles, the join doesn't exist yet. |
| **Read date** | `[date]`: before the planning cycle that decides year 2 funding, which is the decision the number informs. |

- **Fix the matching rule in advance.** Match on prior usage, account size, and similar traits. Attendees self-select, so an unmatched comparison overstates the effect.
- **Feature maturity (Q9):** if inference caching isn't yet generally available, or shipping is dated after the event, the metric may be impossible as written. This needs confirming before registration.
- **Feedback:** collect it in a structured form tied to the same accounts, so it supports interpreting the activation result. It is not the goal metric.
- **Observables to pick (two or three):**
  - Goal-to-number latency: the gap between the event and the date the number is readable.
  - Funder attrition: does each funder still fund the line next cycle.
  - Goal drift: does the debrief score the goal set here.
  - Counterfactual honesty: see section 7.

## 6. Open items

The first question below decides the shape of the answer.

1. **Q5:** does a join already exist between the registration list and product telemetry, or does it have to be built? If it can't be built before the event, adoption isn't measurable yet, and year 1 is an honest goodwill-with-expiry edition. That would be a stated posture with an end date, not a goal.
2. **Q2:** roughly what share of the 700 will be existing users?
3. **Q6:** when must the goal and funding be agreed, and when does the line get renewed?
4. **Q8:** who holds the measurement job through the quarter after the event?
5. **Q1:** are positioning, format, and demand read settled elsewhere?

**Re-run this strategy when:**

- The goal changes.
- A funder joins or leaves.
- The product changes the buyer-and-user answer.
- The invite list stops matching the goal.

## Three reviews before registration opens

These are not optional, and two of them can't be fixed afterwards.

- ⚠️ **Legal review of terms, code of conduct, and insurance.** Staff are bound as well as guests. An incident at this edition can't be revised.
- ⚠️ **Privacy review of the attendee-to-telemetry join.** The skill names the sales-systems case. The same logic applies when attendee data joins product telemetry, so I'm flagging it as an extension. The notice and lawful basis must be right at registration, because data collected under the wrong notice can't be un-collected. Route the rule to the company's own counsel.
- ⚠️ **Hosting rules for customers and prospects.** This is a free half-day. It matters if any customer travel, meals, or gifts are offered, because the guest's employer rules apply too.

## 7. What to report to the two teams afterwards

Use one report with identical numbers, sent to both teams. Different versions for different funders is how a committee finds out it agreed to incompatible things.

**Report contents (same for both):**

1. **The result.** Activation rate for attendees against the matched comparison set, on the read date. Give the rates and the sample sizes.
2. **Counterfactual status, stated plainly.** Say which of these applies:
   - A matched comparison set was used.
   - No comparison set was available, so the figure is a before-and-after read, and the event is one of several plausible causes.
3. **What the room could and couldn't measure.** The count of attendees matched to product accounts, set against total attendance.
4. **Feedback.** The inference-caching findings, by theme. This is for product to use, and it is not a success claim.
5. **Funder status.** Whether each function would still fund year 2, and the re-run triggers.

**Framed per team:**

- **Product:** the activation result and the structured feedback on inference caching.
- **Marketing:** the same activation result, plus the constraint check: the event stayed practitioner-led, with no sales pitch in sessions. Marketing's own reach metrics (registrations, social, content reuse) go in as context. The 700 appears as capacity and reach, never as an outcome.

**Do not report:**

- A "goodwill score" or sentiment figure presented as an outcome. Report survey data, if any, as survey data.
- Attendance as success.
- A pipeline or revenue number. The join to the sales systems doesn't exist and the goal wasn't set.

**Send both teams before registration opens:**

- The four-field commitment.
- The rejected-rungs list.
- The statement of what each funder does and doesn't get.

Get both teams to confirm the deck wording change: replace "developer goodwill and 700 attendees" with the adoption goal, with goodwill as a constraint and 700 as a capacity target.