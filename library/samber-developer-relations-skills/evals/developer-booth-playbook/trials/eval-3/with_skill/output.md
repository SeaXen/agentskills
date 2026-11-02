# re:Invent booth plan: 20x20, theater sessions and demo

**Four of your five ideas break re:Invent exhibitor rules.** I took the rules from the re:Invent sponsor help-centre editions the playbook cites. Check them against this year's sponsor portal before you commit, because rules can change between editions.

| Your plan | Verdict | Replacement |
|---|---|---|
| Two people with flyers in the aisles | ❌ Banned. Soliciting is prohibited, and materials found outside the booth are confiscated and can cost future participation. | Everything happens inside the booth. See "Filling the theater" below. |
| Hiring table in the corner | ❌ Banned. Employee recruiting is prohibited on the premises. | No table and no recruiting collateral. See "Hiring" below. |
| Branded lanyards as giveaways | ❌ Banned. Sponsors may not provide company-branded lanyards, as giveaways or for staff. | Stickers and an earned useful item. See "Swag". |
| Own HubSpot scanning app | ❌ Banned. Only the provided lead retrieval device is allowed, and outside devices, software and APIs are not. | Scan with the AWS device, then import the export into HubSpot. See "Capture". |
| DJ-level speakers | ⚠️ Limited. Island booths get demos only, speakers angled inward, and an 80 dB cap. An inline booth gets no amplification at all. | Small directional speakers. See "Sound". |

## 1. Rules table

Source: re:Invent sponsor help centre, Booth Staffing and Exhibiting Rules & Guidelines. This covers the editions the playbook cites. Re-verify every row against this year's portal.

| Rule | Answer | Status |
|---|---|---|
| Staffing during Expo hours | Mandatory | Published |
| Lanyards | Conference lanyard required. No company-branded lanyards for staff or as giveaways. | Published |
| Staff badges | Own name only. Badge swapping can expel the sponsor. Third-party reps need prior written approval. | Published |
| Lead retrieval | Provided device only. Outside devices, software and APIs not permitted. | Published |
| Soliciting, flyers, recruiting | Prohibited. No direct sales in the booth. | Published |
| Giveaways, signage, activities | Approval through the sponsor portal. No AWS or event logo lock-ups. | Published |
| Draws and raffles | Inside the booth only, aisles never blocked. Sweepstakes need Nevada Gaming Control Board approval. | Published |
| Sound | Inline: no amplification. Island: demos only, speakers inward, 80 dB cap. | Published |
| Wi-Fi | No private networks or hotspots, even for a demo. | Published |
| Leads released when | Not stated for this year. The 2021 edition held leads until fees were paid. | Ask |
| Teardown start, service-order deadlines, shipping deadlines | Not stated | Ask |
| Theater sessions: amplification, content approval, schedule listing | Not stated | Ask |
| Code of conduct signed by every staffer | Not stated | Ask |

⚠️ A 20x20 is normally an island booth. Confirm that in your package, because it decides the sound rule.

## 2. Conversation bar

- **Grade A** = has the problem now, builds with or influences the decision, and agreed a named next step. Staff log these exact words.
- **Minimum:** 20 A per hall day. I assumed this figure, so please confirm it. It is self-set and does not come from your sponsorship plan. If you have one, replace this with its wording and count.
- **Pass:** the A minimum is met, and every A has a next step and an owner. Report B beside it as warm interest.
- **Scans** are activity. Report them beside the A count and never as the goal.

## 3. Crew and shifts

**Crew model:** engineers with a DevRel captain, which is the playbook default for a developer booth.

**Assumptions to confirm:**
- Seven people: one captain, three engineers who can debug a stranger's code, one demo driver, and two qualifiers.
- One demo station.
- Three hall days of three blocks each.
- Your two flyer people become the qualifiers, and one of them is trained as a backup driver.

Headcount comes from conversations, not floor area:
- Two per shift, plus one demo driver, plus a peak slot you fill when the log shows a queue.
- Each block runs 2 to 3 hours with a 15-minute overlap.
- Nobody works more than two blocks a day.

Daily pattern, repeated each day. Replace the block times with the real hall hours.

| Block | Captain | Engineer(s) | Demo driver | Qualifier |
|---|---|---|---|---|
| 1 | Cap | E1 | D1 | Q1 |
| 2 | Cap | E2 | Q2 | Q1 |
| 3 | reachable | E3, plus E1 on the peak slot | D1 | Q2 |

- An engineer is on every block.
- The engineer who is off the floor presents the theater sessions.
- If you have fewer than three engineers, put them on peak blocks, cap them at two blocks a day, and staff the off-peak blocks with a trained non-engineer.
- Keep an engineer reachable within minutes, and state that trade-off in the plan.

**Role cards**
- **Captain** owns the brief, the rules table, the log and the end-of-day review. The captain escalates conduct questions to the organizer and never adjudicates them.
- **Engineer** answers the second question, debugs on the attendee's laptop, and writes the technical note in the record.
- **Demo driver** runs the demo the attendee drives. The driver never qualifies while driving.
- **Qualifier** greets, asks the opener, routes the person to the engineer or the demo, and captures the record.

**Etiquette:** stand at the front edge facing the aisle. No more than two staff talk to each other at once. Eat and take calls off the floor. Help first, and mention the product only when it answers the problem.

**Account executive:** if you add one, keep them off pricing talks in the booth because no direct sales are allowed. Use them for follow-up after the show.

## 4. Filling the theater

Without flyers, use these:
1. Invite existing users and open evaluations to book a theater slot before the show. Pre-booked conversations are the surest A grades.
2. Post the session schedule where your community already gathers, and list it in the sponsor portal or event app if you can (ask).
3. Put session times on approved booth signage.
4. End every session with one named next step, such as "Priya is at the demo station now, bring your stack". A qualifier then takes the hand-off.

## 5. Capture

Use the **AWS scanner with grade and note**.
- Scan A and B conversations only, after the conversation, and never everyone walking past.
- Grade and note in the same minute. A scan with no note is a name with no memory.
- Say the purpose aloud: "Can I scan your badge? I'll send the config we sketched and our solutions engineer will follow up about the trial. Privacy details are on this card."
- Hand over a privacy-notice card. Ask your privacy owner what legal basis covers your follow-up.
- When the leads are released, import the export into HubSpot with the grade and notes. Do not use HubSpot to scan.
- A next-step QR code (book a call, claim a credit) is optional and needs portal approval first. It must not collect lead data.

**Record fields:** grade, problem in the attendee's words, stack, role, next step (dated), owner, route, consent basis, captured by and shift.

**Route field:** drop "recruiting" at this event. Use self-serve invite, sales, product, engineering, partnerships or community.

**Floor scripts**
- **Opener:** "What are you building at the moment?"
- **Three questions:**
  1. "How do you handle that today?"
  2. "Who else on your team deals with it?"
  3. "Would it help to [next step] next week?"
- **Hand-off:** "Priya built the part you're asking about. Priya, they're running [stack] and hitting [problem]."
- **Exit:** "I don't want to keep you from the sessions. Here's a sticker, and the docs page is on the card."

## 6. Swag

- **Ambient:** stickers on the table, ungated, with a design where the logo isn't the whole thing.
- **Earned:** a useful item handed over after an A or B conversation. Never give one for a scan. A C takes a sticker.
  - Size the stock to your expected A plus B count plus a named buffer, not to attendance.
  - For shirts, stock XS to 4XL in straight and fitted cuts.
- **Banned:** branded lanyards, anything gated behind a scan or form, and AWS or event logos.
- **Draw:** skip it unless you want the Nevada Gaming Control Board approval, official rules, and a jurisdiction check with counsel.
- **Approvals:** every item and sign goes through the portal first.
- **Leftovers:** ship home for the next event.
- Lock the swag order and shipping dates back from the portal's advance-warehouse deadline. I don't know your deadline, so please send it.

## 7. Sound

- Use two small directional speakers angled inward, for demo audio only. Background music is not a demo, so skip it.
- Measure at the booth edge with a dB meter and stay under 80 dB. Aim lower at the front edge so staff can still hold a conversation. That second target is my judgment, not a published rule.
- Ask the organizer whether theater sessions get their own amplification allowance. If not, use headphones for theater audio.
- No hotspot for the demo. Order booth internet through the exhibitor service order, and keep a recorded fallback.
- For the demo design itself, use `developer-live-demo-design`.

## 8. Hiring (15 engineers)

Do not recruit from the booth. That includes a table, job flyers and a "we're hiring" sign.
- Ask the organizer whether a spoken pointer to your website is acceptable, and keep it to that.
- Take the recruiting plan to `tech-employer-branding`. For off-site options, use `devrel-field-events`, and check that they sit outside the premises and the rules.
- Your engineers on the floor will be seen anyway. A good booth is the best employer-brand signal you have.

## 9. Show loop and debrief

**Every shift:** the outgoing shift logs 5 minutes before handover. It completes every record, counts A, B and C, notes the questions it couldn't answer, and names the open conversations it hands over.

**End of day one:** the captain compares the counts to the daily share of the minimum and adjusts day two:
- A count well under the daily share → put engineers on peak blocks and rewrite the opener toward the problem.
- A queue → fill the peak slot.
- C counts dominate → move the stickers off the front edge.
- The same question unanswered three times → write the answer on a card and send it to docs.

**Same-day debrief** (30 minutes, the day the hall closes, everyone who worked a shift):
- A count against the minimum, pass or miss, with B beside it.
- Scan count as activity.
- The top three unanswered questions go to product and docs.
- What to change next edition.
- The graded log goes to follow-up, each A with its owner and date.

## Answers I need from you

1. **Crew (blocks the plan):** how many people can you send, and how many of them can debug a stranger's code?
2. **Hall hours (blocks the plan):** what are the daily Expo hours and keynote times?
3. Is the 20x20 an island, and what are the theater session rules?
4. Do you have an A-conversation bar or minimum in a sponsorship plan, or should we keep my 20 per day?
5. What is your swag order lock date, and do you already have swag stock?
6. Is this a one-off, or will you run the booth again next year?
7. How many engineer-days can you pull off the roadmap, and who owns the log after the event?

I couldn't check this year's exhibitor manual, so every row marked Published comes from the cited editions and needs a portal check.