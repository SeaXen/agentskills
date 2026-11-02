# Penhale Conf workshop day post-mortem: where to start

Start with the network failure. It's the only one of your four problems that belongs to this skill. The other three go to other skills, so don't mix them into one debrief.

## Triage

| Problem | Owner | Why |
|---|---|---|
| ❌ Room network died ~25 min in, never recovered | `workshop-program-design` (this skill) | It's an attendee-side failure: a room of laptops that couldn't reach what the exercise needed. |
| ⚠️ Camera feed dropped twice, video unusable | `event-production` | It's a recording signal-path failure. This skill stops at the attendee's environment. |
| ⚠️ Two of four parallel sessions ended 15 min apart and jammed the corridor | `event-schedule-design` | It's a grid and buffer problem. |
| ⚠️ Half the team wants to stop charging separately | `event-format-selection` | Ticketing was decided there, so don't re-argue it in this debrief. |

- **Schedule inputs I can supply.** The corridor jam comes from end times. Those depend on the session lengths and capacities set here, so hand the schedule skill the real lengths and room fill from each session.
- **Pricing.** A bad day doesn't show that the pricing was wrong. Take any evidence about sell-through to `event-format-selection` as a separate review, not as a reaction to this post-mortem.

## First step: find out what broke

Don't write a fix yet. A dead network at minute 25 has several possible causes, and each one leads to a different remedy. My own guess is that the failure came from a cold-install or sign-in burst, but nothing you've told me confirms it.

Candidate causes:
- bandwidth or peak load
- a blocked protocol or port
- a blocked device class
- the access point's device limit
- participant VPNs or ad-blockers
- the venue never answering your questions

Answer these six questions. The first two are the most important.

1. **What was the exercise doing at minute ~25?** (Installs, downloads, vendor sign-ins, a hosted console or remote lab?) Failure at that point suggests a simultaneous-load or policy cause.
2. **Did the whole room drop, or only some people?** Whole-room points at the venue's access point or circuit. Partial points at policy, VPNs or device classes.
3. **What did the venue say in writing about this room's network before the day?** (Sustained bandwidth, device count, blocked protocols.) If the answer is "nothing" or "it's fine", that is itself a finding.
4. **Did the exercise need anything installed or signed into on participants' own machines?** And did the prerequisites list accounts as well as software?
5. **Was there any fallback?** (Offline copy, pre-downloads, a "use your own data" instruction, a demo-only mode.) And did anyone have a plan for the moment the network failed?
6. **Who was in the room besides the instructor, and could they help with the content?** The dropout window shows whether coverage was adequate.

## Provisional conclusions

These hold only if your answers match them.

- **The network posture for next edition.** The skill treats a prior-edition network failure (Q12) as the trigger to remove the live dependency. If the venue also didn't answer in writing, that is a second trigger for the same step. In practice:
  - **Run the session so it works offline.** The exercise either needs no live network service, or participants have pre-downloaded everything.
  - **Ask the venue in writing.** The questions: how many simultaneous devices does the room's access point hold, which protocols and ports are blocked and can they be opened for a day, and are unusual device classes blocked by default.
- **"Assume the network holds" is off the menu.** If participants had to download, install or sign in during the session, the whole room was a load case, not an assumption.
- **Whether hands-on runs at all.** If the exercise needs a live service and the venue hasn't answered in writing, strike full hands-on and run a demonstration plus published material. Only keep full hands-on for content that can't be learned by reading.
- **Live recovery plan.** This skill has no mid-session protocol for a network that fails anyway. That belongs to `event-run-of-show`, so agree it there before next time instead of improvising.

## Measurements to set before the next edition

Set the metric and the trigger that would change the plan before the session starts:
- **Ready at minute zero.** Ask at the door how many participants finished the prerequisites. A low share means moving up the prerequisite menu.
- **Started versus finished.** A wide gap in a full room points at coverage.
- **Help latency.** How long a raised hand waits.

## Next steps

1. **Today:** answer the six questions and collect any venue emails.
2. **Then:** I'll turn the answers into the per-session delivery sheet, one section at a time for your validation.
3. **In parallel:** send the camera drops to the `event-production` review, and the corridor timing to `event-schedule-design`. Bring the pricing question to `event-format-selection` separately.

This is a framework plus questions, not a finished diagnosis. I haven't seen the logs, the venue correspondence or the exercise, so I haven't named a cause.