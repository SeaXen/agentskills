No — two parts of that plan actively work against you, and the playbook this is built on calls out both by name. Here's the prep plan.

# Interview plan: presentation round at Grendal Systems (Thu), from Mon night

## Where you are

Monday night, 45 minutes in front of the panel Thursday — roughly three days of runway. Current plan: write an entirely new talk on their platform and run the full 45 minutes as one continuous live demo against their staging API, which you've seen go down about once a day.

## Assessment

| Item | Risk | Reasoning | Call |
|---|---|---|---|
| New talk written from scratch | High | Format guidance is explicit: "Reuse and adapt an existing talk rather than writing a new one." A from-scratch build also eats the days you need for rehearsal. | Change |
| Whole round run as one live demo | High | Format guidance: "Prepare for the demo to fail: checkpoints, a recorded fallback, a reset path." No fallback on infra with a known ~daily outage rate means one bad roll of the dice can blank your entire round, not just a segment of it. | Change |
| Assuming it's a single presentation format | Unverified | Loops vary company to company even for the same title — confirm with the recruiter rather than assume. | Confirm |
| Two full timed rehearsals before Thursday | At risk | The standard rehearsal plan wants two complete timed run-throughs before day-of. A talk still being written Wednesday doesn't leave room for that. | Fix via steps below |

## What to do next

1. **Tonight (Mon):** Message your Grendal contact — confirm the round is presentation-only (not presentation + something else), and ask their side about the staging environment's actual reliability rather than relying on your own read of "roughly once a day."
2. **Tonight (Mon):** Pick a talk or demo you've already given or built, and adapt it to their platform instead of starting blank. If nothing reusable exists, scope the content down hard so it's *finished*, not just started, by Tuesday.
3. **Tue:** Break the demo into segments. Record a screen-capture fallback for each one, plus a local/sandboxed mock you can fall back to if staging drops. Keep the truly live portion small and deliberate — 5–10 minutes where interactivity earns its keep — not the whole 45.
4. **Tue night or Wed:** Full timed run-through, out loud, recorded. Watch it once at 1.5x, fix only the two worst moments.
5. **Wed:** Second full timed run-through. Deliberately rehearse the recovery path — staging goes down mid-demo — so if it happens for real, it plays as handled, not as a scramble.
6. **Thu, day of:** Bring the recorded fallback, the links, and one question you actually want answered.

## Review point

Wednesday evening: if you don't have one complete timed run-through recorded, with the fallback tested end-to-end, cut the live portion further rather than trying to buy more rehearsal time you don't have left.

## Open questions

- Is there a reusable talk or demo already in your back pocket, or is this genuinely greenfield? Determines how much of steps 2–3 is adaptation versus real build work.
- Which sub-role is this panel scoring you against (outreach advocate, product-focused advocate, DX engineer)? Changes what "good" looks like in the talk.
- Has the staging outage pattern been confirmed with Grendal directly, or is "roughly once a day" your own outside observation? Affects how much fallback infrastructure is worth building.
- Are there other rounds in this loop, and where do they land relative to Thursday?