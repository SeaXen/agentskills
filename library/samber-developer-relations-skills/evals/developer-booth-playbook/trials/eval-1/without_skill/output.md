# KubeCon EU booth plan: Kubernetes cost-monitoring tool

Three things in the current plan need to change before the rest makes sense:

1. **The goal.** 500 scans with a shirt for each one measures how many people walked slowly past the booth. It doesn't measure pipeline.
2. **The staffing.** Four people in a 10x20 booth for every hall hour wears the team out. It also leaves the SDRs as the people answering technical questions.
3. **The shirts.** 600 shirts handed out for a scan will fill your CRM with people who don't remember you. The shirts are already bought, so this plan changes what earns one.

## 1. Goal

**Primary objective: pipeline.** The product is self-serve below 50 nodes and sales-assisted above it. Booth success is therefore qualified conversations with people running 50+ nodes, and trial starts from everyone else.

| Tier | Metric | Role |
|---|---|---|
| Vanity | Badge scans (cap at about 500), foot traffic, shirts given | Tracked, never reported as success |
| Real | Qualified conversations, pre-booked meetings held, trial starts from the booth | The scoreboard |
| Decisive | Cost per qualified conversation, opportunities created, pipeline influenced at 90 and 180 days | Decides whether you return |

**Qualified conversation** means all three of these:
- The person runs Kubernetes in production, or owns its cost: platform, SRE, FinOps or an engineering lead.
- They have a cost-visibility problem they can describe.
- They agreed to a named next step: a trial, a call, or a booked slot.

Cost per qualified conversation can only be compared once the fully loaded cost is known. That cost covers the sponsorship fee, booth build, shipping, shirts, travel for 4+ people, and staff time. Staff time is the line most teams leave out, and it often doubles the total.

**Proposed targets.** These are my assumptions, not benchmarks. Calibrate them against your fully loaded cost and your blended acquisition cost before you sign anything.

| Target | Value |
|---|---|
| Qualified conversations | 80–120 |
| Of those, at 50+ nodes (sales-assisted) | 25–40 |
| Meetings booked before the show and held on site | 15–20 |
| Trial starts from the booth, active at 30 days | 40+ |

Decide the go/no-go threshold before signing. For example, set a ceiling for cost per qualified conversation derived from your current blended acquisition cost. If you can't set one, you can't judge the event afterward.

To tell the VP of marketing: 500 scans is reachable, and about 21 scans an hour for 24 hours is easy if shirts are the incentive. It just doesn't predict revenue. Keep it as a visible secondary number so the goal isn't taken away, and put the qualified count next to it.

## 2. Before the show (weeks −8 to 0)

This is where most of the pipeline is made.

1. **Target list (week −8).** Build 40–60 named accounts running 50+ nodes. Use the speaker list, the sponsor list, past attendees, trial users who went quiet, and open opportunities. Assign each account to one SDR.
2. **Meeting outreach (weeks −6 to −2).** Ask for 15 minutes at a specific place and time, for example "Tuesday 14:00 at the demo station, I'll show your own cluster's cost breakdown". Aim for 15–20 booked meetings.
3. **Open-pipeline invites.** Invite current trial users and open deals to a booth slot. An in-person demo shortens deals already in motion.
4. **Announce your presence with a reason (week −3).** Email and social posts say what they get, not "come to booth X". For example: "Bring a cluster, leave knowing your top three cost drivers in 5 minutes."
5. **Check the contract and compliance (now).** Confirm the badge-scan consent terms for EU attendees and what data you receive. Confirm the exact hall hours and add-on deadlines. Large events close contracts about a quarter ahead.
6. **Set up tracking.** Create an event-specific signup URL and promo code, and tag the CRM source "KubeCon EU". Add a "heard us at" self-report field.
7. **Brief the staff (week −1).** Cover the qualification bar, the 50-node routing rule, the competitor answers, and the do-not-say list.

## 3. The booth

### Layout
- **10x20 with one demo station.** The station is the bottleneck: a 5-minute demo handles about 12 people an hour at best, and in practice fewer.
- **Add self-serve capacity.** Put up a second screen or kiosk where attendees can run a guided cost scan themselves. Use a sandbox cluster with realistic fake data, so no real credentials are involved. This keeps the engineer free for deep conversations.
- **Offline fallback.** Recorded or local-only demo mode, because conference Wi-Fi fails. Test it before day one.
- **Signage.** One line about the problem, not the product. For example: "Find the $ your clusters waste. Bring a cluster. 5 minutes."

### The offer (a help desk, not a pitch)
1. Attendee brings a real cluster, or uses the sandbox.
2. In 5 minutes they connect a read-only agent, or see a sample cost breakdown.
3. They leave with one concrete finding and one next step.

Developers reward booths that help and punish booths that pitch first.

### Staffing: not 4 people × every hour

Four people on the floor at all times is 96 staff-hours of standing, which causes fatigue by day two. A 10x20 with one station comfortably holds 3. The SDRs also shouldn't be the first technical contact, because the best conversations here are Kubernetes cost questions that need an engineer.

**Proposed rotation (2-hour blocks, 3 on the floor, 1 off):**

| Role | Floor duty | Off-floor duty |
|---|---|---|
| Solutions engineer | Demo station, 3 of 4 blocks per day | Short breaks; one of the 4 blocks on pre-booked deep dives |
| SDR 1, 2, 3 | Greet, qualify, book | One block per day each on pre-booked meetings, same-day note cleanup and next-day follow-up |
| **Second technical person (recommended add)** | Covers the SE's breaks; takes engineering-depth questions | N/A |

A second engineer or a product person is the most important addition. If the SE is out sick or on a break, the booth is mostly SDRs saying "let me find someone". If you can't add anyone, schedule the SE's breaks deliberately and use the self-serve kiosk to cover them.

Other staffing rules:
- Hourly 10-minute breaks, water, and shoes.
- No phones on the floor, and no one sits at the back.
- Engage with questions, not "can I scan you?".
- Peak traffic is typically just after the keynote and at lunch. Put all hands on the floor then and schedule off-floor work in the quiet hours.

### Shirts: what earns one

The 600 shirts are a sunk cost, so use them to produce signal rather than scans.

- **Gold tier (about 150–200 shirts):** completing the 5-minute cost scan, or a qualified conversation with a next step. Tag these in the scanner.
- **Silver tier (the rest, about 400):** one shirt per person who completes a short demo or answers two qualifying questions. No "scan and run".
- **Cap daily distribution** at about 200 so you don't run out on day three.
- **Keep about 30 in reserve** for pre-booked meeting attendees, customers and follow-up gifts.

### Scanning
Use the scanner as a qualification tool, not a turnstile. After each real conversation, record:
- A rating: hot, warm, or scan only.
- Node count, or a rough size.
- Their stated problem, in a few words.
- The agreed next step.

The follow-up writes itself from these notes. Without them it will be generic.

## 4. Follow-up (24–48 hours, then 14 days)

| Tier | Who | Action | Owner |
|---|---|---|---|
| Hot | 50+ nodes, a named problem, an agreed next step | Personal email in 24h that references the conversation, with a calendar link | SDR who spoke with them, then the AE |
| Warm | Real conversation, under 50 nodes, or no stated next step | One relevant asset tied to their problem, plus trial link | Product-led nurture sequence |
| Scan only | No conversation | One light touch, or nothing | Marketing; don't burn the domain on people who won't remember you |

Run the first email wave on the Friday of the show, and the rest by the following Wednesday. Don't wait two weeks and send a generic sequence. Confirm now who answers replies during the two weeks after the show.

Also route non-sales conversations to the right place, instead of dumping them all on sales:
- Feature requests and beta candidates → Product.
- Bugs → Engineering.
- Partner interest → Partnerships.
- Case-study material → Marketing.
- Candidates → Recruiting.

## 5. Daily rhythm

| When | What |
|---|---|
| 08:30 | Team stand-up: yesterday's count against target, today's pre-booked meetings, who is off-floor when |
| 10:00–18:00 | Booth rotation as above; pre-booked meetings at set slots |
| 18:00–18:30 | Log cleanup: every conversation tagged and a next step written |
| Evening | Optional: a small dinner for 8–12 target accounts. It usually produces more meetings per dollar than the booth itself |

Check the numbers against pace at midday each day. If you're at 20 qualified conversations after day one against a 100 target, change the greeting, the location, or the offer on day two.

## 6. Content

You are already paying for the studio, so capture:
- Short clips of the demo and of attendees' reactions, with permission.
- One recap post per day.
- Two or three customer or user quotes.
- Any talk or panel recording you're allowed to publish, with the transcript.

## 7. Post-event review (within 2 weeks)

1. Compute the fully loaded cost and divide it by the number of qualified conversations.
2. Compare against the threshold you set before signing.
3. Record the verdict: **renew**, **renegotiate** (right audience, wrong package), or **drop**.
4. Check pipeline at 30, 90 and 180 days, and tag deals "influenced", not "sourced".
5. Judge a first edition against awareness-stage expectations. Don't write off events as a channel because of one result.

## 8. Risks

| Risk | Mitigation |
|---|---|
| Demo or Wi-Fi fails | Offline mode, recorded fallback, tested on site on day zero |
| Shirt-seekers swamp the booth | Tiered shirt rules; a separate, visible shirt hand-out point |
| SE overloaded | Second technical person, kiosk, scheduled breaks |
| Follow-up stalls | Named owner per account, first wave on Friday |
| EU consent issue on scanned data | Confirm the consent terms in the contract; store only what you may use |
| Pressure to report 500 scans as success | Pre-agree with the VP that the scoreboard is qualified conversations; report scans as context |

## 9. Questions that would sharpen this plan

1. What is the all-in budget, including the fee, travel and staff time, and the fully loaded cost per qualified conversation you can accept?
2. What is your blended customer acquisition cost today? It sets the threshold in section 1.
3. Can you add a second technical person?
4. Do you have a CRM and scanner that can capture the qualification fields?
5. What are the exact hall hours and the booth location, and how close is it to the keynote room?
6. Are there other events this year, or is this the single big bet? That changes how much to invest in this one.