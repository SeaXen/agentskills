**Start with Hacktoberfest. Hold off on the GSoC application for a year — not never, just not yet.**

**Why not GSoC right now**

- Time math doesn't work. Google's own guidance is ~5+ hrs/week per intern for a 12–22 week coding period, plus writing the org application, an idea list, and picking projects months beforehand. That alone exceeds your entire 4 hr/week budget, before your existing review load is even counted.
- Your two current problems — 3-week PR silence, broken Windows build — are bandwidth symptoms, not pipeline symptoms. GSoC adds more of the exact thing you're already short on (structured mentor hours), so it makes both worse, not better.
- Solo maintainer = single point of failure. GSoC org admins prefer ≥2 mentors per project as backup; going in alone is a common rejection reason, independent of project quality.
- The 80%-Outreachy-retention stat doesn't actually argue for applying now. It says mentorship pays off once you can afford the up-front hours — it says nothing about the hours themselves being cheap. Retention is the outcome of a well-run internship, not a discount on running one.

**Why Hacktoberfest fits now**

- Bounded to one month, contributor-initiated — you're not recruiting, they show up.
- You control exposure: label only a handful of curated issues instead of opening the whole backlog, so triage load stays sized to your 4 hours.
- It costs you triage time, not mentorship time — a smaller, different category of hour than GSoC needs.
- It gives you real data on your throughput under higher PR volume, which is the actual prerequisite for a credible GSoC application later, not a stat about someone else's program.

**Do these two things before opening it**

- Label the Windows build failure "help wanted." It's a good Hacktoberfest issue on its own, and it removes the first-contact failure that would otherwise hit Windows-using contributors (and later, students) immediately.
- Add a one-line response-time expectation to CONTRIBUTING.md or a pinned issue (e.g., "I aim to acknowledge within a week; full review may take longer"). An unacknowledged PR is worse than a slow one — this costs you nothing and directly fixes the thing that already burned a contributor.

**Reassess GSoC next year once**

- Response time is consistently under a week.
- Windows builds pass.
- You've run at least one Hacktoberfest cycle and know your real hours-per-contributor cost.
- You've lined up a co-mentor — apply as two, not one.