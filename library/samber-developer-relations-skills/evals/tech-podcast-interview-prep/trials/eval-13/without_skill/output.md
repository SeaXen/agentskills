Your angle: **don't pitch the outage — pitch the failure mode.** The show has covered "how to get OTel data flowing" (2x) and "how to keep it affordable" (1x). Nobody's covered what happens *after* that work is done and the observability stack itself becomes the thing that falls over. That's a real gap, and it's the one story you're positioned to tell that they haven't heard.

**Angle: "The observability paradox — what happens when your eyes go dark at your worst possible moment."**

This works because it reframes the constraint (NDA on the incident review) as a non-issue rather than a workaround. The NDA covers the *vendor's formal post-mortem* — their findings, their root-cause admissions, anything that identifies them. It does not cover your own team's experience, your own architecture, or the changes you made afterward. Those are yours to tell. Split the material along that line and there's nothing to dance around on air.

**What's fair game (yours, not the vendor's):**
- The shape of the failure in general terms: your tracing backend became a bottleneck under a traffic spike it wasn't sized for — a widely-recognized failure class, not a vendor-specific defect.
- What "flying blind" actually looked like operationally during Black Friday: what decisions got made without full trace visibility, what you fell back on (logs, metrics, gut instinct, dashboards you'd normally ignore), how the incident commander adapted in real time.
- Everything you changed since April on your side of the fence: sampling strategy, backpressure/load-shedding on the telemetry pipeline, decoupling collection from the hot request path, treating the observability stack as a production system with its own capacity plan and SLOs instead of assumed-infinite infrastructure.
- The organizational lesson: observability tooling is usually procured/architected assuming normal load, then trusted blindly at peak load — the exact moment you need it most is the moment it's least tested.

**What stays out, and how to set that boundary with the host in advance (not live):** tell them upfront, before recording, that the vendor's formal incident review is under NDA until January, so you won't name the vendor or cite the official findings — but the architecture, the decisions, and what you rebuilt are open. Hosts want to know this ahead of time, not discover it mid-question. It reads as professional, not evasive.

**Bonus move:** offer the second half as a future booking. "Ask me back in January and I'll walk through the vendor's actual findings once the NDA lifts" gives the host a concrete reason to have you on twice, and creates its own anticipation hook in the meantime — you're trading one episode for a near-guaranteed second one.

**One-line pitch you can send the host:**

"You've done two episodes on getting OTel data flowing and one on keeping it cheap — I want to talk about the episode nobody's done yet: what happens when the observability stack itself is the thing that goes down, at your highest-stakes traffic moment of the year. I've got a real one from this April, and I can walk through the architecture failure and everything we rebuilt since — the vendor post-mortem specifics are NDA'd until January, but the failure mode and the fix are fair game now, and I'd happily come back in January to close the loop once they're not."

**Suggested working title:** "Who Watches the Watchers: Designing Observability That Survives Its Own Worst Day"