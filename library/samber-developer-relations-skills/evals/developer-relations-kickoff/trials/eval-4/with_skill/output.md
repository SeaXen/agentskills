# Tessellate Data — DevRel kickoff (developer-relations-kickoff)

No `devrel-context.md` exists for this project → **cold start**. I'm running the full kickoff in one pass rather than a multi-turn interview, since you asked for the complete deliverable now. That means I've substituted my own best-effort answers for the capped interview instead of asking you turn-by-turn — flagged below so you can correct anything before it drives real spend.

## Given vs. assumed

| # | Question | Status |
|---|---|---|
| Q1 surface | Events and speaking (d) | **Given** — both asks are events |
| Q2 goal / decided vs open | Decided: run own 600-person Lisbon conference (June 2027); decided: sponsor 3 external conferences this autumn (~$85k). Open: venue, ticketing tiers, CFP mechanics, prospectus for #1; which 3 events, tiers, activations, proof method for #2 | **Given**, from your message |
| Q3 who adopts/pays | Assumed: organization-buys or both (developer evaluates, someone else signs) | **Assumed** — typical for a data platform, not stated |
| Q4 funded driver | Assumed: developer adoption + ecosystem/partnerships | **Assumed, unconfirmed** — matters, see below |
| Q5 stage | Assumed: dedicated person or small team | **Assumed** — a $85k sponsorship spend plus a 600-person event implies more than a side-of-desk job |
| Q6 constraints/date | Autumn 2026 for sponsorships (i.e. now — this is tight), June 2027 for the conference, $85k ceiling, CFO wants post-hoc proof | **Given** |
| Q7 one-off vs. compounding | Assumed: standing — an annual user conference and a repeatable sponsorship motion are both compounding bets, not one-offs | **Assumed** |

⚠️ Q4 matters most: if nobody at Tessellate can actually name the funded driver behind this spend, `devrel-strategy` jumps to rung 1 by this skill's own promotion rule (an undefined driver means every later metrics/budget conversation stays generic). Confirm the driver before locking the short-list below.

## Route

Two asks, two different owners:

🎯 **The $85k / 3-conference sponsorship program** → `samber/developer-relations-skills@developer-event-sponsorship`. Its declared scope is a verbatim match: "which events, which tier, which activation, what ROI proof."

🎯 **The 600-person Lisbon conference (venue, ticketing tiers, self-run CFP, sponsor prospectus)** → this is organizer-side work. `samber/developer-relations-skills` has no skill for it — it's a named coverage gap (running your own conference, selling sponsorship as the organizer, running your own CFP). This is organizer-side work — `samber/dev-event-organizer-skills` covers it; this collection stops at the sponsor and speaker side.

## Short-list (this collection only, ordered by value ÷ effort)

Fixed autumn dates promote the sponsorship work to rung 1 outright — "this autumn" is now, and sponsor deals typically lock weeks ahead, so this isn't a diagnosis-first situation, it's already urgent.

1. **`developer-segmentation`** — names which developer/buyer segments Tessellate actually needs in the room, which is the real filter for "which 3 conferences." Costs one session over existing customer/lead data.
2. **`developer-event-sponsorship`** — turns the segments + $85k into a picked shortlist, tier, activation, and proof method per event. Costs one focused session; promoted to rung 1 by the autumn deadline.
3. **`devrel-analytics`** — instruments the tracking (UTMs, badge-scan capture, lead-source tagging) that makes the CFO's "proof it did something" real instead of a guess after the fact. Costs one instrumentation pass, cheapest if you already have a CRM/link tool.
4. **`devrel-metrics`** — turns the raw captured numbers into a framework leadership trusts: which numbers get a target, the attribution rule, what gets cut as vanity. Needs Q4 (funded driver) answered or it stays generic.
5. **`devrel-budget-allocation`** — splits the $85k across the 3 events into line items with a return threshold and a cut list, so the CFO sees discipline rather than an even three-way split. Optional but cheap once #2 is done.

## Chain

`developer-segmentation` → `developer-event-sponsorship` → `devrel-analytics` → `devrel-metrics`

- Segmentation hands sponsorship the ranked list of who you need visibility with.
- Sponsorship hands analytics the picked events/tiers/activations and what "proof" is supposed to mean for each.
- Analytics hands metrics the actually-captured numbers (leads, scans, pipeline-touched) instead of guesses.
- Metrics hands the CFO the one number set with an attribution rule attached.

## Not now

- **`devrel-strategy`** — not now, unless Q4 comes back genuinely undefined (see ⚠️ above). Unblocking condition: confirm the funded driver.
- **`devrel-content-calendar`** — not now. Unblocking condition: both the conference date and the 3 sponsored events are locked, so recap/teaser content has real anchors to plan against.

## Gap

Collection v1 has no skill for organizing your own conference or hackathon, conference booth operations, or post-event follow-up — which is most of your first ask (venue, ticketing tiers, CFP-as-organizer, sponsor prospectus). Route that whole thread to `samber/dev-event-organizer-skills`. Don't stretch `developer-event-sponsorship` or `conference-cfp-submission` onto it — both assume you're the guest, not the host.

## Context artifact (save as `devrel-context.md` at Tessellate's project root)

I haven't written this to disk — this session has no real Tessellate Data repository to commit it into. Copy it into your own repo so the next session starts warm instead of cold.

```markdown
# DevRel context

_Last updated: 2026-09-19_

## Product and audience

- Product: Tessellate Data — [confirm: what the product is and what a developer does with it]
- Adoption motion: assumed organization-buys or both — unconfirmed, confirm before it drives the sponsorship short-list

## Program

- Funded driver: unconfirmed — assumed developer adoption + ecosystem/partnerships. Confirm; this reorders the short-list.
- Pillar mix: not yet set
- Stage and team: assumed dedicated person or small team — unconfirmed

## Surfaces owned

- Events: committed — own 600-person user conference, Lisbon, June 2027; sponsoring 3 external conferences, autumn 2026, ~$85k total budget

## Measurement

- Metrics currently reported: none known
- Known blind spot: no confirmed post-sponsorship ROI method yet — CFO has asked for proof after the fact, which is the gap `devrel-analytics` + `devrel-metrics` close

## State

- In flight: sponsorship target-event selection (autumn 2026, urgent); own-conference planning (venue, ticketing, CFP, prospectus — routed to `samber/dev-event-organizer-skills`)
- Decided: run own conference in Lisbon, June 2027; sponsor 3 external conferences this autumn, ~$85k ceiling
- Open: which 3 events, tier per event, activation per event, proof method; venue, ticketing tiers, CFP structure, sponsor prospectus for own event
- Constraints: autumn timing is tight — sponsor deals typically lock weeks ahead of the event, and this is being decided in September for an autumn season already underway

## Stakeholders

- CFO — requires post-hoc proof of sponsorship spend; decision rights on the $85k budget

## Session log

- 2026-09-19 - "where do we start on the conference + sponsorship spend" → routed sponsorship to `developer-event-sponsorship`, routed own-conference to `samber/dev-event-organizer-skills` (gap) → wrote this artifact
```

## Routines (dry-run — nothing created yet)

```
Routine: kickoff re-invocation
Trigger: monthly, given two live high-stakes workstreams over the next 9 months
Runs: developer-relations-kickoff
Output channel: updated devrel-context.md + refreshed short-list, posted wherever the team tracks DevRel work
Cost: near-zero per firing
First fire: 2026-10-01
```

```
Routine: sponsorship deadline & proof-capture sweep
Trigger: ahead of each of the 3 target events' sponsor deadline, and again right after each event
Runs: developer-event-sponsorship (pre-event) then a devrel-analytics data pull (post-event)
Output channel: a note to the CFO/finance channel with captured numbers per event
Cost: two short passes per event, up to 6 touches this autumn
First fire: as soon as the 3 target events are picked — date depends on step 2 of the short-list above
```

```
Routine: measurement read
Trigger: after the first sponsored event concludes
Runs: devrel-metrics
Output channel: CFO-facing ROI summary
Cost: one session
First fire: date TBD, depends on which 3 events are chosen
```

## Memory

Nothing written to persistent memory for this session — Tessellate Data is a hypothetical scenario in this conversation, not a real project with its own repository, and the skill's memory step exists to keep a real project's artifact in sync across sessions. If this becomes a real engagement, the context artifact above is what should seed memory, never the reverse.