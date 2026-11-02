# StreamSummit edition 1: launch plan

I assumed a few things you haven't told me. Each assumption is marked and has a number you can swap.

- **Size:** about 250 attendees.
- **Format:** one conference day plus an optional workshop day.
- **Date:** autumn 2027.
- **City:** undecided. The venue section gives selection criteria instead.
- **Currency:** EUR.
- **Budget figures:** planning assumptions from my own estimates, not quotes. Replace them with real quotes before you commit.

## 0. Three problems to fix before spending anything

### 0.1 "We know there's appetite" is an assumption, not a fact

Streaming being popular as a technology tells you nothing about whether 250 engineers will pay and travel to an independent event from a vendor they may not know. The cost of testing this is small and the cost of being wrong is a venue deposit.

Run a **6-week validation gate** (section 1) before signing anything. The gate has pass and fail thresholds written down now, so the result can't be argued afterwards.

### 0.2 "Independent" and "run by Parqet Labs" pull against each other

Speakers and attendees will check who is behind the event. Decide how you handle it before the announcement:

- **Disclose Parqet's role up front.** Hiding it is the one move that damages trust permanently.
- **Put a program committee in place.** It should have a majority of non-Parqet members, public selection criteria, and blind CFP review.
- **Cap Parqet at one talk slot.** Keep competing vendors on the sponsor list on equal terms.
- **Use a separate brand.** Give it its own domain, its own Code of Conduct, and its own social accounts.
- **Consider a legal entity.** A small non-profit, or a fiscal host, makes "independent" credible.
- **Name the real Parqet payoff** in the internal brief: category authority, a community you convene, and warm relationships. If the goal is pipeline, say so and measure it separately (section 7). Don't pretend to attendees that it isn't.

### 0.3 Your three success metrics don't fit a first edition

| Metric | Problem | Replacement |
|---|---|---|
| **Viral coefficient** | It needs a repeatable invite loop. One edition of ~250 people gives a very noisy estimate. | Track **referral rate**: the share of tickets bought through a referral link or "invited by" field, plus invites per attendee. |
| **CAC vs LTV** | A conference attendee has no defined lifetime value. Ticket revenue is one-off. | Define it in two parts. **Event-level:** cost per attendee against revenue per attendee (tickets plus sponsors). **Parqet-level:** cost per qualified conversation and per influenced opportunity. Compute LTV only if Parqet can attach a customer value to an attendee. |
| **Month-over-month cohort retention** | "Retention" is undefined for an attendee, and with ~250 people each cohort percentage swings widely. | Define "active" as one of: joined the community channel, posted or reacted, opened a post-event email, registered for edition 2 or a meetup. Measure at 30/60/90 days. Report counts next to percentages. |

Agree on these definitions now. If you define them after the event, you'll pick whichever version looks best.

## 1. Validation gate (Oct–Nov 2026, about 6 weeks)

**Goal:** show that independent demand exists beyond Parqet's own audience.

**Actions**
1. Publish a one-page site with the dates and city as "planned", a **waitlist**, and a **speaker interest form**. Don't announce a firm date.
2. Run 15–20 interviews with streaming engineers who are not Parqet customers. Ask what events they attend, what they paid, and what would make them travel for a new one.
3. Ask 10 people you'd want as program committee members or speakers whether they'd commit.
4. Ask 3–5 potential sponsors, including non-competitors and cloud and data vendors, for a letter of intent.
5. Do a small **paid pre-sale test**: 30 "founding" tickets at a deep discount, refundable. Waitlist signups are cheap. Money is the real signal.

**Thresholds (my suggested starting points, adjust to your risk appetite)**

| Signal | Go | Fail |
|---|---|---|
| Waitlist signups from outside Parqet's own list | 600+ | under 250 |
| Founding tickets sold | 40+ | under 15 |
| Program committee yes | 6+ | under 3 |
| Sponsor letters of intent | 2+ | 0 |

If the result is in between, shrink to a 120-person single-day event or run a meetup-scale edition 0.

## 2. Positioning and format

- **Audience:** engineers and architects building and operating streaming systems: Kafka, Flink, Spark Streaming, Pulsar, Redpanda, Materialize, and similar. Cover the stream-processing and streaming-database space broadly, not only Parqet's category.
- **Promise:** practitioner-led talks on running streaming in production, with no product pitches from stage.
- **Tone:** war stories and trade-offs, such as exactly-once in practice, state management, and operating costs.
- **Format:** one main track, single stage, 45 minutes of content with 15 minutes of buffer. Add a second room only for workshops.
- **Day 0 (optional workshop day):** four hands-on 3-hour workshops, capped at 30 people each, priced separately.
- **Day 1 (conference):** 9:00 to 18:30, then an evening social.

## 3. Program

**Sessions (about 14 slots)**

| Slot | Content |
|---|---|
| Opening keynote | State of streaming in production, an independent speaker |
| 8 practitioner talks (35 min) | Real systems: migrations, incidents, cost, schema evolution, late data, backfills |
| 2 deep dives (45 min) | Internals and correctness (state, checkpoints, exactly-once) |
| 1 panel | "What we'd do differently" with 4 practitioners |
| Lightning talks (5 min × 8) | Open call, selected the week before |
| Closing | Community round-up and edition 2 announcement |

- **Speaker mix:** at least 70% non-Parqet. Allow a maximum of one Parqet talk, with no product pitch. Aim for 30–40% from underrepresented groups, and say so in the CFP.
- **CFP:** open for 6 weeks. Make the submission template short (abstract, outline, what the audience will learn). Review blind, with three reviewers per talk.
- **Speaker support:** pay travel and one hotel night for external speakers, offer a free ticket plus a guest, run a rehearsal call, and publish a speaker guide.
- **Hallway track:** give each talk a dedicated chat thread. Run structured "ask me anything" tables over lunch.
- **Recordings:** record every talk, with speaker consent, and release them over the following 8 weeks. This is your longest-lived asset.

## 4. Venue

Choose from these criteria before choosing a city:

1. **Capacity:** a main hall for 300 (about 20% headroom), plus 2 breakout rooms for 30–60 each.
2. **Access:** near a major airport and train station, with step-free access throughout.
3. **AV and network:** in-house AV with a recording-capable setup, and wired internet that has been tested with the venue's technician at full load.
4. **Catering:** flexible, with vegan, halal, gluten-free, and allergy labelling built in.
5. **Cost:** a day rate that includes setup and teardown. Ask for a **cancellation clause** with a staged deposit (10–20% at signing).
6. **Neutrality:** avoid a venue owned by a competitor or sponsor.

**City:** score 3–4 candidates on where your waitlist concentrates, travel cost, and hotel availability. Check clashes with the big streaming conferences and with local holidays before fixing a date.

**Process:** collect 3 quotes, tour the top 2, and sign only after the validation gate passes. Add a **force-majeure** clause and a reduced-capacity clause.

## 5. Budget (planning assumptions, EUR)

**Costs**

| Item | Estimate |
|---|---|
| Venue and AV, including recording | 25,000 |
| Catering (about €55 per head × 250) | 14,000 |
| Speaker travel and hotel (about 12 external speakers) | 12,000 |
| Marketing, design, website, ticketing fees | 10,000 |
| Production staff, security, volunteer care, signage | 6,000 |
| Insurance, legal, accessibility, Code of Conduct training | 4,000 |
| Contingency (about 15%) | 10,000 |
| **Total** | **≈ 81,000** |

**Revenue (one scenario)**

| Source | Assumption | Amount |
|---|---|---|
| Paid tickets | 150 × ~€200 average | 30,000 |
| Free and discounted tickets | 100 (speakers, volunteers, scholarships, community) | 0 |
| Sponsors | ~8 × ~€5,000 average | 40,000 |
| **Total** | | **≈ 70,000** |

**Gap:** about €11k, which Parqet would cover. A conservative case (100 paid tickets, 5 sponsors) widens it to about €36k. Decide now the maximum subsidy Parqet will carry, and treat it as a cap, not a target.

**Workshops:** priced at about €250 each and aimed at roughly cost recovery. Do not count them in the base case.

**Sponsorship rules**
- Sponsorship buys visibility and a table, **not** stage time and not program influence.
- Publish the tiers, prices, and conduct limits openly.
- Every sponsor, including Parqet, signs the same terms.
- Set a single-sponsor revenue cap (for example, no sponsor above 25% of sponsor revenue) so no one holds leverage.

**Ticket tiers:** founding (refundable pre-sale), early, standard, and a scholarship pool of about 10% of seats, funded by sponsors and Parqet.

## 6. Marketing

**Principle:** most of the work happens before and after the event. Treat the 24–48 hours after the event as the moment pipeline is won or lost.

**Phases**

| Phase | Timing | Activities |
|---|---|---|
| Validate | Oct–Nov 2026 | Waitlist, interviews, founding tickets |
| Announce | Jan 2027 | Open CFP, announce committee, publish brand and Code of Conduct |
| Build | Feb–May | Speaker reveals in waves, early-bird tickets, partner communities, sponsor outreach |
| Push | Jun–Aug | Full program, workshop launch, speaker content, local meetup co-promotions |
| Close | Final 6 weeks | Standard tickets, logistics, reminder sequences, attendee-to-attendee intros |
| Retain | Event + 90 days | Recordings, community channel, edition 2 waitlist |

**Channels**
- **Communities where streaming engineers already are:** Slack and Discord communities, subreddits, Hacker News (only for substantive posts), dev.to, LinkedIn, and X. Participate first and promote second.
- **Speaker amplification:** give every speaker a shareable card and a short blurb. Their audiences are your best acquisition channel.
- **Co-promotion with meetups and open-source communities** in the streaming space, on equal terms.
- **Content before the event:** a "state of streaming" survey (published with raw data), a practitioner interview series, and a short CFP-advice post.
- **Email:** welcome sequence for the waitlist, three reminder emails per ticket tier, and a "bring a colleague" push.
- **Referral mechanics:** each ticket includes a link that gives the referee a discount and gives the referrer credit toward a workshop. This also feeds the referral-rate metric.
- **SEO and AI discoverability:** one clear site with a program page per talk, schema markup, and transcripts after the event.

**Parqet's own channels** (customer list, newsletter, social) are legitimate, but label the source in tracking so you can tell Parqet-origin demand from independent demand.

**Do not**
- Buy attendee lists.
- Imply endorsements you don't have.
- Gate the program or speaker list behind a form.

## 7. Measurement

Tag every registration with its source (Parqet-origin, referral, community, speaker, paid, other) and ask "How did you hear about us?" at checkout.

**Event health**
- Registrations to attendance (show-up rate; a typical range is wide, so track yours as your own baseline)
- Referral rate and invites per attendee
- Net promoter score or a single "would you come back?" question
- Share of non-Parqet attendees (this is the "independent" test)

**Economics**
- Cost per attendee and revenue per attendee
- Cost per qualified conversation and per influenced Parqet opportunity (a separate lens; attribute honestly, since events are multi-touch)
- Subsidy against the cap

**Community retention (30/60/90 days)**
- Percent and count of attendees "active" under your agreed definition
- Registrations for edition 2 or follow-up meetups

**Decision rule for edition 2:** write the thresholds before edition 1. For example: at least 60% non-Parqet attendance, subsidy under the cap, a "would come back" score you consider acceptable, and at least X% active at 90 days. Judge on the trend across two or three editions, since the first run usually underperforms.

## 8. Operations and risk

- **Code of Conduct:** published, with a named contact and a response process. Train staff and volunteers.
- **Accessibility:** step-free, quiet room, live captions if budget allows, and dietary and access questions at registration.
- **Privacy:** minimal data, clear consent for photos and recordings, and no sharing of attendee lists with sponsors without opt-in. Check local data-protection rules for your venue's country.
- **Staffing:** assign a lead per area (program, sponsors, venue, marketing, attendee experience). Two organizers can't also run the day, so recruit 10–15 volunteers and a professional event producer for the day.
- **Insurance:** event cancellation and liability.
- **Contingency plans:** speaker dropout (keep 2 reserve lightning speakers), AV failure, and low sales (a staged scale-down option set in the venue contract).
- **Reputational risk:** any hint that the program favors Parqet will cost you. The committee and the disclosure are the protection.

## 9. Timeline

| When | Milestone |
|---|---|
| **Oct–Nov 2026** | Validation gate (section 1) |
| **Early Dec 2026** | Go/no-go against the pre-agreed thresholds |
| **Dec–Jan** | Committee, brand, entity, venue quotes, sponsor prospectus |
| **Jan 2027** | Venue signed, CFP and public announcement |
| **Mar** | CFP closes, review, speaker confirmation |
| **Apr–May** | First speaker wave, early-bird tickets |
| **Jun–Aug** | Full program, workshops, marketing push |
| **Sep** | Final logistics, run-of-show, rehearsals |
| **Event (autumn 2027)** | Day 0 workshops, Day 1 conference |
| **+48 hours** | Personal follow-ups, thank-you emails, survey |
| **+8 weeks** | All recordings published |
| **+90 days** | Retention read-out, edition 2 decision |

## 10. Decisions I need from you and Tomas

1. **Budget:** what's the maximum Parqet subsidy?
2. **City or region:** where do your waitlist and community concentrate?
3. **Primary outcome:** community, category authority, or pipeline? Pick one, because the plan above optimizes differently for each.
4. **Independence:** will you set up a separate entity or fiscal host?
5. **Gate thresholds:** do the go/fail numbers in section 1 match your risk appetite?
6. **Team:** who beyond you and Tomas can commit time? Is there budget for a producer?

I can turn any section into a working document next: the sponsor prospectus, the CFP text, the validation-gate survey, or the measurement spreadsheet.