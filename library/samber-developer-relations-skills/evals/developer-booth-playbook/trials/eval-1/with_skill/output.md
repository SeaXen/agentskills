# KubeCon EU Booth Plan: Kubernetes Cost-Monitoring Tool

**Next action:** get the VP to agree to the unit change in section 1 before anything else. The rest of the plan depends on it.

Labels on figures: **[yours]** = from your brief, **[event]** = published by the event, **[conv]** = convention or rule of thumb, **[assumed]** = confirm before the event.

## 0. Changes to the current plan

| Current plan | Problem | Change |
|---|---|---|
| Goal: 500 badge scans | A scan counts activity, not a conversation. Chasing it fills the booth with people who want a shirt. | Goal becomes **qualified conversations (grade A)**. Scans are reported beside it as activity. |
| 600 shirts for anyone who lets us scan | Gating swag behind a scan pulls shirt collectors and grades every record C. | Keep the shirts and hand them out as an **earned item** after an A or B conversation. Nothing is gated behind a scan. |
| 4 people in the booth every hour | Staff outnumber visitors and become a closed group. The single SE is on the floor 8 hours a day, which is too long. | 2-3 people per block on a rotation, SE on peak blocks (section 4). |

## 1. Conversation bar

Wording for the VP and for every staffer:

- **Grade A** = the person runs Kubernetes and has a cost-visibility problem now, builds with or influences the decision, and **agreed a named next step**.
  - Under 50 nodes, the next step is starting the self-serve trial.
  - Over 50 nodes, the next step is a booked call with the SE.
- **Grade B** = has the problem, no next step yet.
- **Grade C** = curious, learning, or here for swag.
- **Minimum: 45 A over 3 days (15 a day)** [assumed, self-set]. Confirm it with the VP. It is the pass/fail line.
- **Sanity check:** 2 conversation-capable staff × 24 hall hours × the low end of the trainer's 3-per-hour target gives about 144 conversations [conv]. 45 A is about 31% of that. It is reachable but not slack. If the VP wants more A, add staff rather than raise the percentage.
- **Reporting to leadership:** "A count vs 45, B count as warm interest, scans as activity." A big scan count with a missed A count is a miss.

## 2. Rules table

The skill requires this table to come from this edition's exhibitor manual. I could not read it, so every cell below is unconfirmed.

| Rule | Answer | Source |
|---|---|---|
| Booth staffed during all hall hours? Penalty? | **Not stated** | Manual |
| Teardown allowed from | **Not stated** | Manual |
| Lead retrieval: provided? Own app allowed? Scan only in booth? | **Not stated.** Assumed included with the package [assumed]. The KubeCon NA report carries name, title, company and email, with no phone [event]. | Sponsor guide |
| Leads released when | **Not stated** | Manual |
| Giveaways inside booth only? Approval? | **Not stated.** The CNCF guidelines say no materials outside the booth space [event, NA edition]. | Manual |
| Draws and games | **Not stated** | Manual |
| Event, CNCF or LF logo on swag | The CNCF guidelines ban it [event, NA edition]. **Check our shirt artwork now.** | Branding guidelines |
| Branded lanyards | Staff may wear their own. Not as giveaways [event, NA edition]. | Branding guidelines |
| Soliciting or flyers outside booth | The CNCF guidelines ban it [event, NA edition]. | Branding guidelines |
| Recruiting at booth | **Not stated** | Manual |
| Sound and amplification limit | **Not stated** | Manual |
| Staff badges (own name, transfers) | **Not stated** | Manual |
| Code of conduct signed by each staffer | **Not stated** | Manual |
| Booth graphics approval by | The CNCF guidelines require CNCF approval [event, NA edition]. Deadline **not stated**. | Branding guidelines |
| Service orders due (power, internet, lead devices) | **Not stated** | Manual |
| Shipping: warehouse deadline, return | **Not stated.** EU customs time applies to the 600 shirts if they come from outside the EU. | Manual |

Naming rule: never write "KubeCon" alone as the event name. Use the full name.

## 3. Crew

The skill's default is an engineer crew with a DevRel captain. You have 3 SDRs and 1 SE, which is the sales-led model with an engineer on call. That model ranks last for developer audiences.

- **Ask now:** can 1-2 more engineers or a DevRel person come? That puts an engineer on every block (upgrade grid below).
- **If not, run the grid in section 4**, with the trade-off stated openly: the SE is on the floor for peak blocks only. Off-peak, a trained SDR works the floor and the SE is reachable within minutes.
- **Train all 3 SDRs** on one thing before travel: how to run the demo path. A demo driver needs the demo path, not engineering depth.
- **Captain:** one SDR per day, rotating. The captain owns the brief, the rules table and the log. The captain works two blocks and stays reachable for the third.
- **Risk:** one SE is a single point of failure. If they are ill, there is no engineer. Name a backup from the product team now.

## 4. Shift grid (3 days, hall 10:00-18:00 [assumed])

Check the real hall hours in the manual. Day 3 is often shorter.

Blocks: **B1 10:00-12:30, B2 12:30-15:00, B3 15:00-18:00**, each with a 15-minute handover overlap. B2 and B3 are the peaks (post-lunch, afternoon break) [assumed].

| Block | On the floor | Role split | SE |
|---|---|---|---|
| B1 | SDR-1 (captain), SDR-2 | Qualifier + demo driver | Reachable within minutes, doing log cleanup, prep and hallway conversations |
| B2 | SDR-1, SDR-3, SE | Qualifier + demo driver + engineer | On the floor |
| B3 | SDR-2, SDR-3, SE | Qualifier + demo driver + engineer | On the floor |

- Each SDR works exactly 2 blocks a day. The SE works 2 (the cap).
- Nobody works a full day on the floor or more than 2 blocks in a row.
- Rotate the names each day so the captain and the B1 pair change.
- The optional 4th slot in a peak block is filled only once the shift log shows visitors leaving a queue.
- **With a second engineer:** put them on B1 so every block has one.

Etiquette, briefed once:

- Stand at the front edge, facing the aisle.
- No laptops or phones out except to help someone.
- Never more than two staff talking to each other.
- Eat and take calls off the floor.
- Help first. Mention the product only when it answers the problem in front of you.

## 5. Role cards

- **Captain:** owns the brief, rules table, log and end-of-day review. Escalates code-of-conduct questions to the organizer.
- **Engineer (SE):** answers the second question, debugs on the attendee's laptop, writes the technical note in the record. Takes the call booking for clusters over 50 nodes.
- **Demo driver:** runs the demo the attendee drives. Never qualifies while driving. Demo design: `developer-live-demo-design`.
- **Qualifier:** greets, opens, routes to the engineer or the demo, captures the record.

## 6. Floor scripts

**Opener** (about their work, not the product):
- "What are you running on Kubernetes at the moment?"
- "When the cloud bill lands, can your team tell which namespace or team drove it?"

**Three qualifying questions:**
1. "How do you track cluster cost today?" → current stack and pain.
2. "Who else on your team cares about it, and who signs off on tooling?" → role (builds, champions, decides).
3. "Roughly how many nodes?" Then:
   - Under 50: "Want me to send the trial link with the setup for your stack?"
   - Over 50: "Can our SE walk through your setup on a call? Does Tuesday work?"
   - If neither fits: a clear no, which makes it a B or C.

**Hand-off** (SDR to SE): "[SE name] built the part you're asking about. They run [stack] and see [problem]."

**Polite exit** (C, or once the next step is agreed): "I won't keep you from the sessions. The docs page for what we sketched is on this card." Hand over a sticker with the card.

**Purpose line, said before taking any contact detail:**
- Scanner: "Can I scan your badge? I'll send the setup we sketched, and our team will follow up about the trial. Privacy details are on this card."
- Never promise "nothing else" and then route the lead to a sales sequence. The purpose you say aloud is the purpose you may use.
- Hand every person whose details you take a card with the privacy-notice link. EU event: your privacy owner must confirm the legal basis for follow-up **before** the show, and it goes in the record.

## 7. Capture

- **Method:** scanner with grade and note. Scan **A and B conversations only, after the conversation**. Then grade and note in the app or a paired sheet.
- **Never scan** people who walk past.
- **Fallback:** if there is no lead retrieval in the package, use the hand-written conversation log. Check the sponsor package and Q2.
- **Next-step QR code:** one code per next step ("start trial", "book a call"), tagged with the event.
- **Record per conversation:**

| Field | Content |
|---|---|
| grade | A / B / C |
| problem | in the attendee's words |
| stack | cloud, K8s distribution, current tool, node count |
| role | builds, champions, decides |
| next step | concrete and dated |
| owner | the staffer who promised it |
| route | self-serve invite / sales / product / community |
| consent basis | what was said aloud + legal basis set by your privacy owner |
| captured by, at | name, block |

Example A: `grade A | "no idea which team burns 40% of the GPU nodes" | EKS, Kubecost-less, 120 nodes | champions, platform lead signs | SE call Tue 10:00 | Marc | sales | purpose said aloud: setup + trial follow-up`

A scan with only "great chat" cannot be graded or followed up.

## 8. Swag policy

- **Ambient item (default):** stickers on the table, ungated, with a design where the logo is not the whole design.
  - Size to hall traffic past the booth. Ask the organizer for an estimate.
  - **Check the lock date** (production plus EU shipping) before ordering more. If it is too late, skip the stickers.
- **Earned item: the shirts.** Handed after an **A or B conversation only**, never for a scan. A C takes a sticker.
  - Stock: expected A (45) + B (assume 2-3× A, so about 100-135) gives roughly 150-180 shirts needed at the booth.
  - **Check the size run today.** The need is XS to 4XL in straight and fitted cuts. Vendor orders run thin at both ends. Ask the VP what the 600 consists of.
  - Ship the rest home or keep it for the next event. Do not carry 600 shirts to the floor.
  - Confirm the artwork has no KubeCon, CNCF or LF logo.
- **No draw by default.** Prize draws carry the highest compliance cost. Add one only if the rules table allows it and counsel clears it. The entry must never double as marketing consent.
- **Banned:** gating any item behind a scan or form, event logos, branded lanyards as giveaways.
- **Leftovers:** ship home or donate where the event offers it.

## 9. Before the show

1. **Now:** get the exhibitor manual and fill section 2. Lock the swag and travel dates (work back from the lock date, Q8).
2. **Now:** agree the A bar and the 45 minimum with the VP in writing.
3. **Weeks before:** invite existing trial users, open evaluations and customers to book a slot at the booth. Post in the Kubernetes and FinOps communities you already use. Pre-booked conversations are the surest A grades on a busy floor.
4. **Before travel:** brief everyone on the grade definitions, scripts and purpose line. Rehearse the SDR-to-SE hand-off. Train the SDRs on the demo path.
5. **Before travel:** get the privacy owner's legal basis and the card with the privacy-notice link.

## 10. Show loop and debrief

**End of every block** (5 minutes before handover, outgoing shift):
1. Complete every record started.
2. Count A, B, C.
3. Note questions the booth could not answer.
4. Pass open conversations to the incoming shift by name.

If a block skips its log, reconstruct its A and B records the same evening.

**End of day 1, the captain reads the counts against 15 A and adjusts day 2:**
- Well under 15 A → put the SE on more peak time and rewrite the opener toward the cost problem.
- Visitors leaving a queue → fill the optional 4th slot.
- C dominates → move stickers off the front edge so the opener comes before the sticker, and keep shirts behind the counter.
- Same unanswered question three times → write the answer on a card and send it to docs.

**Same-day debrief** (30 minutes, the day the hall closes, everyone who worked a shift):
- A count vs 45, pass or miss. B count beside it.
- Scan count, reported as activity.
- Top three unanswered questions → product and docs.
- What to change next edition: crew, grid, scripts, swag.
- Handover: the graded log, each A with its owner and date, goes to follow-up (`developer-event-followup`). Follow-up stays within the purpose said at capture.

## 11. Open questions (blocking first)

1. **Blocking:** Does the VP accept A conversations as the goal, with scans reported as activity? What is the real minimum: 45 [assumed], or another number?
2. **Blocking:** Does the package include lead retrieval? Is the booth staffed during all hall hours by contract?
3. Can 1-2 more engineers or a DevRel person come?
4. What is the size and cut mix of the 600 shirts, and is there any event logo on them?
5. What is the swag and travel lock date?
6. Who owns the log after the event?

## 12. Not saved yet

Nothing is written to `devrel-context.md`. Say so if you want this plan saved there.