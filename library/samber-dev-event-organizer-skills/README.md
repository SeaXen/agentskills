# Skills for tech event organizers

**Technical event operations**: conferences, meetups, hackathons, and the community programs around them.

Written for **event organizers, conference producers, hackathon leads, and community builders**, covering strategy through day-of production. Every skill is **tool-agnostic**: it teaches the decision, not one vendor's ticketing console.

<img width="1904" height="640" alt="image" src="https://github.com/user-attachments/assets/11c1a293-6267-4b81-8476-c7cbcb380cfb" />

## 📚 Related Collections

- [`developer-relations-skills`](https://github.com/samber/developer-relations-skills): DevRel strategy & execution: _for developer advocates, DevRel managers, community managers_
- [`developer-platform-skills`](https://github.com/samber/developer-platform-skills): Platform & SDK developer experience: _for platform engineers, DX engineers, SDK authors, API product managers, DevRel engineers_

_Part of the [samber skills ecosystem](https://github.com/samber?tab=repositories&q=skills)_

## 🚀 Install

Install every skill in this repo, not just one. Skills here are atomic by design and reference each other freely: picking a single skill leaves its sibling skills uninstalled, so cross-references and routed handoffs go nowhere.

<details>
<summary><b>skills.sh</b> — universal, works with any Agent Skills-compatible tool</summary>

```bash
npx skills add samber/dev-event-organizer-skills
```

</details>

<details>
<summary><b>Claude.ai</b></summary>

1. add as a plugin marketplace: open **Settings -> Capabilities -> Plugins**
2. click **Add -> Add marketplace -> Add from a repository**
3. enter `samber/dev-event-organizer-skills`
4. then **Sync**

</details>

<details>
<summary><b>Claude Code</b></summary>

```bash
/plugin marketplace add samber/dev-event-organizer-skills
/plugin install dev-event-organizer-skills@dev-event-organizer-skills
```

</details>

<details>
<summary><b>Codex (OpenAI)</b></summary>

```bash
codex plugin add github:samber/dev-event-organizer-skills
```

</details>

<details>
<summary><b>Cursor</b></summary>

```bash
git clone https://github.com/samber/dev-event-organizer-skills.git ~/.cursor/skills/dev-event-organizer-skills
```

Cursor auto-discovers skills from `.agents/skills/` and `.cursor/skills/`.

</details>

<details>
<summary><b>Gemini CLI</b></summary>

```bash
gemini extensions install https://github.com/samber/dev-event-organizer-skills
```

Update with `gemini extensions update dev-event-organizer-skills`.

</details>

### First run

```
/dev-event-kickoff I'm running a 200-person developer conference in March and the call for papers still isn't open.
```

## 📦 Skills

This collection covers the full event-organizing surface.

### Start here

[`dev-event-kickoff`](./skills/dev-event-kickoff): Routes any event-organizing task to exactly one skill in this collection, or names the gap when none fits.

### Meta

- [`event-team-structure`](./skills/event-team-structure): Designs the standing organizing team between editions: legal entity, decision rights, roles, succession, burnout guardrails, and the first paid hire.
- [`dev-event-career`](./skills/dev-event-career): Guides a practitioner into and up the event-organizing ladder: role fit, portfolio audit, interview prep, and offer evaluation.
- [`dev-event-hiring`](./skills/dev-event-hiring): Builds the hiring side of an event-organizing role: scorecard, posting, interview loop, sourcing channels, and ramp plan.

### Launch & strategy

- [`event-budget`](./skills/event-budget): Builds one edition's money model: fixed and per-head costs, break-even, and the sponsorship and ticket targets it hands downstream.
- [`event-cultural-identity`](./skills/event-cultural-identity): Defines and audits the event's lived culture: the register, its tone across every touchpoint, and the rituals worth protecting.
- [`event-date-selection`](./skills/event-date-selection): Picks the date the event runs on, checking audience calendars, observances, and competing events before anything is announced.
- [`event-first-edition`](./skills/event-first-edition): Launches a first edition from zero: minimum viable scope, the founding team, a reverse timeline, and written go/no-go dates.
- [`event-format-selection`](./skills/event-format-selection): Chooses the event's structure: shape, track count, session-format mix, delivery mode, and hackathon demo and judging structure.
- [`event-growth-strategy`](./skills/event-growth-strategy): Grows an established event edition over edition through one deliberate lever, and treats capping or shrinking as a valid strategy.
- [`event-market-fit`](./skills/event-market-fit): Reads whether the concept, audience, and price meet real demand, and returns a go, hold, pivot, or stop call.
- [`event-planning-timeline`](./skills/event-planning-timeline): Builds the months-long work-back plan: parallel tracks, dependency gates, latest-safe commitment dates, and checkpoints that cut scope instead of dates.
- [`event-portfolio-strategy`](./skills/event-portfolio-strategy): Shapes one team's several event properties into a set where each feeds the others, with a written kill criterion per property.
- [`corporate-event-strategy`](./skills/corporate-event-strategy): Decides what a company-run event is funded to accomplish: the goal mix, budget ownership, and the measurement commitment written upfront.
- [`event-positioning`](./skills/event-positioning): Defines what the event stands for, against which alternatives, and for which audience identity, ending in a positioning statement.
- [`event-risk-management`](./skills/event-risk-management): Runs the standing risk register: risk taxonomy, likelihood-impact scoring, treatment and insurance postures, and the go/no-go decision date.
- [`business-event-formats`](./skills/business-event-formats): Picks which company-run event shape to run, from an invite-only dinner to a multi-city roadshow or a floor-primary event.

### Program & speakers

- [`event-cfp-design`](./skills/event-cfp-design): Designs the published call for papers: timeline, form depth, anonymization posture, review criteria, speaker benefits, and first-time-speaker support.
- [`event-talk-selection`](./skills/event-talk-selection): Runs the review process on submitted proposals: committee shape, rubric, anonymization, conflict recusal, the cut rule, and decline messages.
- [`event-speaker-sourcing`](./skills/event-speaker-sourcing): Finds and qualifies the speakers a call for papers will not bring in, and returns a ranked shortlist with evidence.
- [`event-speaker-cold-outreach`](./skills/event-speaker-cold-outreach): Writes and sequences the invitation to a shortlisted speaker: what to disclose, which channel, how to personalize, when to follow up.
- [`event-speaker-experience`](./skills/event-speaker-experience): Takes care of a speaker who already accepted: point of contact, material deadlines, A/V, consent, on-site hosting, and post-event follow-up.
- [`event-speaker-coaching`](./skills/event-speaker-coaching): Runs the coaching program for accepted speakers: the offer, mentor pairing, dry runs, capped feedback, timing cuts, Q&A and slide accessibility.
- [`event-schedule-design`](./skills/event-schedule-design): Lays selected talks into the published grid: slot lengths, room matching, clash detection, buffers, and publication timing.
- [`workshop-program-design`](./skills/workshop-program-design): Runs the hands-on session itself: facilitator coverage, participant prerequisites, capacity ceilings, session length, materials, and the room's network posture.
- [`startup-pitch-contest`](./skills/startup-pitch-contest): Runs a pitch contest or demo day inside a larger event: applications, judge conflicts, prizes, and the scoring slate.

### Sponsors & partnerships

- [`event-sponsor-value-proposition`](./skills/event-sponsor-value-proposition): Articulates what each sponsor segment genuinely buys, one segment at a time, and what the event can honestly promise.
- [`event-sponsor-prospectus`](./skills/event-sponsor-prospectus): Assembles the prospectus itself: section anatomy, tier table, add-on cards, audience evidence, and the per-edition refresh routine.
- [`event-sponsor-outreach`](./skills/event-sponsor-outreach): Runs the net-new sponsor sales motion: scored target list, budget-cycle timing, first-touch channels, objection handling, and pipeline tracking.
- [`event-sponsor-pricing`](./skills/event-sponsor-pricing): Builds the sponsorship rate card: revenue target first, then tiers, add-ons, exclusivity premiums, in-kind valuation, and discount policy.
- [`event-sponsor-agreement`](./skills/event-sponsor-agreement): Turns a sold sponsorship into a term sheet for counsel: deliverables, payment, force majeure, cancellation, exclusivity, and renewal.
- [`event-sponsor-fulfillment`](./skills/event-sponsor-fulfillment): Delivers everything a signed sponsor was promised, from asset collection through the day-of experience to the post-event report.
- [`event-sponsor-renewal`](./skills/event-sponsor-renewal): Turns the post-event report into a renewal: ask timing, non-discount renewal offers, price-change messaging, at-risk rescue, and renewal rate.
- [`event-booth-experience`](./skills/event-booth-experience): Designs the expo floor as one system: layout, tier-to-spec catalog, setup and teardown schedule, power, network, and staffing.
- [`event-b2b-matchmaking`](./skills/event-b2b-matchmaking): Designs the mechanic behind scheduled 1:1 meetings between two populations, starting from whether the event should run one at all.
- [`cross-event-promotion`](./skills/cross-event-promotion): Brokers reciprocal visibility swaps with independent events: partner scoring, swap formats, a lightweight agreement, and a per-partner delivery ledger.
- [`event-side-event-coordination`](./skills/event-side-event-coordination): Decides four things about events others run inside your dates: approval, calendar deconfliction, use of your name, and liability.
- [`event-media-partnerships`](./skills/event-media-partnerships): Sets up barter media and community partnerships: exchange formats, partner scoring, a no-cash agreement, and a two-direction delivery ledger.

### Venue & logistics

- [`event-venue-sourcing`](./skills/event-venue-sourcing): Finds and negotiates the venue: one written space program, a sourcing ladder, site-visit depth, negotiation posture, and contract traps.
- [`event-vendor-sourcing`](./skills/event-vendor-sourcing): Sources, vets, and contracts the suppliers the venue does not include: caterers, AV, security, insurance, swag, and print.
- [`event-hospitality`](./skills/event-hospitality): Sets the food, drink, and social floor: catering service style, break content, alcohol posture, and the evening programme.
- [`event-official-social-program`](./skills/event-official-social-program): Decides how many official social occasions run, whether any overlap, and which one clears the published access set.
- [`event-run-of-show`](./skills/event-run-of-show): Builds the minute-by-minute playbook staff execute on the day: cue sheet, transitions, comms channels, on-duty rotation, and disruption handling.
- [`event-volunteers`](./skills/event-volunteers): Staffs one edition with volunteers: post list, roster arithmetic, shift design, recruitment channels, recognition, and the no-show protocol.
- [`event-volunteer-experience`](./skills/event-volunteer-experience): Covers the hours a volunteer is off post and the weeks after the event: rest space, closure, and the alumni loop.
- [`event-production`](./skills/event-production): Engineers technical execution: capture coverage, signal paths, recording redundancy, crew roles, the venue tech spec, and the media budget line.
- [`virtual-event-production`](./skills/virtual-event-production): Runs delivery for an event with no room: platform choice, moderation posture, remote-speaker readiness, and the failure drill.
- [`hybrid-event-design`](./skills/hybrid-event-design): Designs programme and staffing for in-room and remote audiences at once: session eligibility, parity depth, crew split, and cue track.
- [`event-learning-expedition-design`](./skills/event-learning-expedition-design): Takes your own audience into a host organization you do not control: host-dependency posture, access rules, and repeatability.
- [`event-sustainability-plan`](./skills/event-sustainability-plan): Estimates the event's footprint, ranks the levers that cut it (travel first), schedules the data to collect, and writes an offset-free sustainability page.

### Tickets & attendees

- [`event-ticket-pricing`](./skills/event-ticket-pricing): Prices attendee tickets: the free-to-commercial posture, the tier ladder, gating rules, scholarships, group discounts, and refund policy.
- [`event-marketing-plan`](./skills/event-marketing-plan): Builds the attendee-acquisition plan: segment-to-channel mapping, a campaign calendar spine, ranked channel mix, budget posture, and per-phase targets.
- [`event-social-media`](./skills/event-social-media): Runs the event's own social presence: platform set, hashtag split, post calendar, amplification asks, and staffed live coverage.
- [`event-press-relations`](./skills/event-press-relations): Pursues earned coverage: press posture, accreditation policy, media page, announcement beats, embargoes, and the on-site press operation.
- [`event-landing-page`](./skills/event-landing-page): Builds the event's public front door and the small site around it: page shape, the dominant call to action, and per-section reveal timing.
- [`event-attendee-email-sequences`](./skills/event-attendee-email-sequences): Designs and writes the attendee email arc: sequence depth, reminder cadence within caps, segmentation, and the know-before-you-go email.
- [`event-comms-channels`](./skills/event-comms-channels): Designs the attendee-facing channel architecture: which channels exist, who is on each, message routing, writer consistency, and wind-down.
- [`event-no-show-management`](./skills/event-no-show-management): Reduces and absorbs no-shows: the show-up expectation, an overbooking ceiling, waitlist design, and day-of gap absorption.
- [`event-registration-forecast`](./skills/event-registration-forecast): Forecasts final registrations from the sign-up pace curve as a low/mid/high band, with the commit figure at each lock date and attendance by ticket type.
- [`event-vip-social-program`](./skills/event-vip-social-program): Runs the private room once a named-guest programme exists: seat list, invitation and door access, and placement against the public programme.

### Experience & day-of operations

- [`event-code-of-conduct`](./skills/event-code-of-conduct): Writes the code of conduct and the enforcement pipeline behind it: scope, reporting channels, response team, sanctions ladder, transparency report.
- [`event-attendee-experience`](./skills/event-attendee-experience): Designs the general attendee's on-site day: check-in, badge posture, quiet room and facilities, help desk, and dietary mechanics.
- [`event-accessibility-inclusion`](./skills/event-accessibility-inclusion): Decides which access provisions the event commits to, then publishes and staffs them: provision depth, captioning, request channel, economic access.
- [`event-vip-management`](./skills/event-vip-management): Receives named guests whose presence creates escort, protocol, security, or discretion obligations, without building a status tier the room reads.

### Hackathon

- [`hackathon-brief-design`](./skills/hackathon-brief-design): Writes the challenge document teams read before building: problem statements, tracks, rules, eligibility, submission checklist, and evaluation category names.
- [`hackathon-judging`](./skills/hackathon-judging): Designs the rubric and scoring process: judge-allocation arithmetic, weighted criteria, score combination, conflict recusal, and tie-breaks.
- [`hackathon-cash-prize`](./skills/hackathon-cash-prize): Structures what a hackathon awards: prize medium, pool size, split shape, payout rigor, and the exposures routed to counsel.
- [`hackathon-team-formation`](./skills/hackathon-team-formation): Decides how participants end up building together: team-size rule, matchmaking mechanic, the unpicked-participant path, and the membership freeze.
- [`hackathon-mentoring`](./skills/hackathon-mentoring): Designs the mentor programme for one edition: coverage depth per track, recruitment source, request mechanic, and briefing depth.

### Post-event

- [`event-feedback`](./skills/event-feedback): Designs and runs participant feedback for one edition: per-format instrument, role modules, anonymity posture, collection channel, and closing the loop.
- [`event-debrief`](./skills/event-debrief): Runs the organizing team's retrospective on a finished edition: timeline, reconciliations against risk, budget and schedule, and owned action items.
- [`event-continuous-improvement`](./skills/event-continuous-improvement): Turns a run of debrief logs into cross-edition trends and one deliberate change, routed to the sibling that owns it.
- [`event-community-building`](./skills/event-community-building): Animates the event's audience in the months between editions: cadence posture, attendee conversion, and the community-asset handover.
- [`event-content-repurposing`](./skills/event-content-repurposing): Turns an edition's captured recordings into derivatives: publishing latency, derivative mix, speaker amplification asks, and rights posture.
- [`tech-podcast-youtube-channel`](./skills/tech-podcast-youtube-channel): Runs an organizer's standing podcast or video channel: whether it exists at all, guest sourcing, cadence, and wind-down.

## 👤 Contributors

![Contributors](https://contrib.rocks/image?repo=samber/dev-event-organizer-skills)

## 💫 Show your support

Give a ⭐️ if this project helped you!

[![GitHub Sponsors](https://img.shields.io/github/sponsors/samber?style=for-the-badge)](https://github.com/sponsors/samber)

## 📝 License

Copyright © 2026 [Samuel Berthe](https://github.com/samber).

This project is under [MIT](./LICENSE) license.
