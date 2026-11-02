Nothing is created yet. The skill requires a dry-run and your approval first, and I need three facts from you to fix the dates.

**Do this next (about 2 minutes):** reply with (1) the exact doors-open date, (2) the project root folder, and (3) where each alert should go, for example a Slack channel or an email.

## What I did and did not check

- ℹ️ This session is in the `example-repo` repo, not the PolarByte project. My search for `event-context.md` was blocked, so I did not confirm the file is missing. I'm treating this as a cold start.
- ℹ️ `CronList` returns no jobs in this session. Last year's reminders are therefore **not** in this session's scheduler, and I have not found them.
- ❌ I have not retired or touched any old job.
- ℹ️ The ticketing platform is not connected here. I cannot read ticket sales.

## Why 3 routines, not "as many as it takes"

You asked for as many routines as it takes. The skill caps routines at 4 and defaults to 3. A routine's cost is attention per firing times how often it fires. Routines that fire with nothing to decide get silenced, and then the go/no-go alert gets buried with them.

I add monitoring through more dated firings inside the routines, not through more routines. One slot is reserved for the ticket-pace check.

## Re-ranking, and which answer moved what

- **Edition 3 (Q1e, Q3c):** opens the recurring gate. The trend read returns, but it cannot fire until a debrief lands.
- **Fixed doors date (Q6a):** installs the work-back checkpoint early.
- **Signed venue contract:** moves the go/no-go review to rung 1, because the cancellation fees are now real.
- **No ticketing source detected:** deletes the ticket-pace check for now. I will reinstate it the day a sales export or connector is readable.
- **Unanswered:** funding model (Q4) and effort ceiling (Q7). If sponsors carry the budget and someone has weekly hours, the sponsor sweep becomes affordable.

## Dry-runs (approve, edit or drop each)

I assume doors open about 2027-07-12, nine months from today. That is a placeholder. Replace D with your real date. All dates below are approximate.

**Routine 1: go/no-go review**
- Runs: `samber/dev-event-organizer-skills@event-risk-management`
- Trigger: two firings before each cancellation-fee rung, placed ahead of the rung and never on it.
  - Prep, 21 days ahead: D-141 (about 2027-02-21), D-111 (about 2027-03-23), D-66 (about 2027-05-07). The lead time is long because venue, insurer or counsel signatures are slow.
  - Final call, 7 days ahead, only if the decision is still open: D-127, D-97, D-52.
- Output: a dated section in `event-context.md` plus a message in your channel with three options (hold, change scope, cancel) and the fee at each. Cancelling or postponing is contractual, so a human decides.
- Cost: six firings in total, each needing a real decision.
- Stops: after the D-45 decision, or once a no-go is taken.
- First fire: about 2027-02-21. The CFP closes about 2027-02-12, so the two are close together.

**Routine 2: work-back checkpoint**
- Runs: `samber/dev-event-organizer-skills@event-planning-timeline`
- Trigger: the plan's own replanning checkpoints. They don't exist yet.
- Proposed placeholders: CFP close +7 days, then D-180, D-90 and D-30.
- Output: a dated section in `event-context.md` listing scope cuts. Cutting scope is cheaper than moving the date.
- Cost: one team session per firing.
- Stops: on doors open.
- First fire: after the timeline session sets real checkpoints.

**Routine 3: kickoff re-invocation**
- Runs: this skill, `dev-event-kickoff`.
- Trigger: the day before each go/no-go prep firing and each work-back checkpoint, plus the day after CFP close.
- Output: a refreshed 5-line state summary and a session-log line in `event-context.md`.
- Cost: near zero. It stops the other two firing at work that no longer exists.
- Stops: on doors open.

**Held: ticket-pace check**
- Runs: `event-market-fit`.
- Trigger: each ticket-tier boundary, plus the 1st of the month while tickets are on sale.
- Needs: a readable ticketing export or connector, and a published pace checkpoint.
- First fire: the day sales become readable.
- Stops: on doors open.
- Reason it matters: only this routine can trigger a hold or pivot while ticket money is still refundable.

**Scheduler caveat:** `CronCreate` recurring jobs auto-expire after 7 days, so they cannot cover nine months. The fix is one-shot durable jobs pinned to each date, which need your project root. If you prefer, one recurring calendar reminder, "Event check-in – re-run the event organizer kickoff", is the skill's fallback.

## Last year's reminder jobs

Check these places and send me the list. Then we retire them one by one, each with your approval:
1. `.claude/scheduled_tasks.json` in the old event project.
2. Cloud routines. I can list them with the `schedule` skill.
3. Calendar reminders.
4. CI schedules.
5. The ticketing platform's automated emails.

Any job not re-anchored to edition 3's dates fires at nothing, so retire it. Retire old jobs before installing new ones.

## Route

`samber/dev-event-organizer-skills@event-risk-management`. It produces the go/no-go dates that Routine 1 needs. This skill handles the routine setup itself.

## Short-list, best value per effort first

1. `event-risk-management`: turns the 120/90/45 fee curve into dated decisions. It costs one session reading the contract.
2. `event-planning-timeline`: gives Routine 2 its checkpoints. It costs one session.
3. `event-cfp-design`: the CFP closes in about 4 months and the window cannot be compressed. A Q6b deadline ranks above the room-filling work. It costs a check of reviewer recruitment and timing.
4. `event-ticket-pricing`: tickets on sale make the refund and transfer policy binding. Check it against the venue fee curve. It costs one review session.
5. `event-marketing-plan`: registrations feed everything else. It costs a campaign through to doors.
6. `event-budget`: sets break-even against the cancellation fees. It is near-free if a budget file exists.

## Chain (talks lane)

`event-cfp-design` → `event-talk-selection` → `event-speaker-experience` → `event-schedule-design` → `event-run-of-show`

## Not now

- `event-talk-selection`: after the CFP closes and submissions are in.
- `event-schedule-design`: after `event-talk-selection` returns an accepted list.
- Sponsor sale (`event-sponsor-outreach` and the other sponsor skills): once you give funding (Q4) and a sponsor budget window.
- Sponsor sweep routine: same condition.
- Trend read routine: after this edition's debrief lands.
- `event-run-of-show` and `event-production`: when doors are within weeks.

## Gap

Ticketing platform operation (checkout, refunds, tax) has no skill. `event-ticket-pricing` only sets the price and writes the refund policy.

## Draft `event-context.md` (not written, because the project root is unknown)

```markdown
# Event context
_Last updated: 2026-10-12_

## Identity
- Event: PolarByte Days, edition 3. Funding model: not answered.

## Format
- Shape: two-day conference. Delivery: in-person. Track count: not answered.

## Dates
- Doors open: fixed date, announced, about 9 months out (exact date to fill).
- CFP close: about 2027-02-12. On-sale: since about 2026-10-05.
- Venue contract signed 2026-09. Cancellation fees step up at D-120, D-90, D-45.
- Go/no-go reviews: D-141, D-111, D-66.

## State
- Decided: venue signed.
- Open: routine approval, old-job inventory, funding, effort ceiling.

## Session log
- 2026-10-12 – set up check-ins → event-risk-management → dry-runs proposed.
```

When I write memory later, I will leave out attendee and speaker personal data, accommodation requests, conduct reports and negotiated rates.

**Next:** send the doors date, project root and alert channel.