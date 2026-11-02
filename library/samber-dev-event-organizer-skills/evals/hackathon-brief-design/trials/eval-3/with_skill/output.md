# Kestrel Labs Devfest: 8 challenge tracks?

**Verdict: no. Run 3 challenge tracks: one general track plus one per sponsor.** Your reasoning for 8 doesn't hold, and the numbers you gave point to 3. This answers the track-count question from `hackathon-brief-design`. I haven't drafted the brief yet, because the interview answers it needs (listed at the end) are still missing.

## Why 8 doesn't work

1. **The Friday session tracks have no bearing on this decision.**
   - Session tracks are parallel streams on Friday. That's an event-format decision, owned by `event-format-selection`.
   - A challenge track is a thematic category that a team enters its project into. It's a content and prize construct.
   - Neither count should be derived from the other. A brief that borrows the session-track count invents categories nobody sponsored.

2. **"About 50 people per track" isn't a real number.**
   - A team submits one project, and that project can enter several challenge tracks. The standard rules say both "You may not submit multiple projects" and "You may submit to multiple challenges".
   - Adding a track therefore doesn't split the field, so no per-track headcount exists.
   - No published ratio scales track count to participant headcount.
   - 400 is also registrations, not attendees or teams. With teams of up to 4, you're judging roughly 100 to 200 teams, not 400 people.

3. **Judging capacity is the real ceiling.**
   - The only sourced limit comes from MLH's guide. It says to aim for 3 tracks when there are no sponsor tracks and no overall 1st/2nd/3rd placement, never 20 or more, and to raise the count only as far as the judges can absorb without deliberations turning chaotic.
   - You have 6 judges. At 2 judges per track, that's 3 tracks, and 8 would leave 0.75 judges per track. The 2-per-track figure is my arithmetic, not a published rule. The exact judging mechanics are for `hackathon-judging`.

4. **Two sponsors fund prizes, and that fixes the structure.**
   - The "one unified challenge" option is off the table. A sponsor prize needs a published track or criterion to attach to, or it gets improvised at the ceremony.
   - Two sponsors plus an open track is 3 tracks.
   - Eight tracks is the "fully partitioned" structure. It needs enough sponsors that each funds its own prize and a demographic carve-out already required. You have two sponsors and no carve-out mentioned.
   - The other 5 tracks would have no sponsor, no prize owner and no judge capacity. They'd get empty tracks and prizes nobody competed for.

## Recommended structure

| Challenge track | Owner | Prize |
|---|---|---|
| General | Kestrel Labs | One prize line |
| Sponsor A | Sponsor A | One prize line |
| Sponsor B | Sponsor B | One prize line |

- **Cross-track rule, published once:** "One project per team. A project may enter several challenge tracks. Entering a sponsor track does not forfeit the general prize." Teams assume the opposite, and that assumption suppresses sponsor-track entries.
- **Prize amounts and cash handling** go to `hackathon-cash-prize`. The brief says "each challenge track awards a prize" and prints no figure.
- **Add a beginners track only if** you need that carve-out. If you do, the required fraction of the team ("at least half first-timers", for example) must be published before teams form. Otherwise the fully partitioned structure stays off.
- **Sponsor prompts:**
  - Write each sponsor prompt as a problem with a capability constraint ("persist data across sessions using the provided store"), not as "must use Sponsor X".
  - Publish the access path: where keys come from, the rate limit, and who to ask when it fails.
  - Publish a fallback sentence. A team whose sponsor integration fails through no fault of its own is judged on design and integration plan, not on a working call.
  - Make the sponsor integration an optional bonus path by default, so an outage costs one prize rather than the event.
  - Promote it to "required for one track" only if a signed agreement names that track and someone on your team has built something small against the API end to end.

## What the structure needs next

If the 8 were really 8 themes you care about, don't turn them into tracks. Fold them into the general track's problem statements, or into the sponsor prompts. If you still want more than 3 tracks, the lever is more judges or more sponsors, not a bigger list.

**To unblock the brief, I need these answers (one at a time is fine):**

1. Has either sponsor's signed agreement already promised a named challenge track?
2. Does either sponsor's API, dataset or hardware need keys or accounts? Has anyone on your team built something small against it end to end, and what happens to those teams if it goes down?
3. What is the hacking window in hours, and is the event in person or digital?
4. Which demo/judging structure is already chosen: expo table, stage pitch, video-only, or hybrid?
5. What team-size rule has `hackathon-team-formation` set? Is solo entry allowed?
6. Do you need a beginners, student-only or similar carve-out?
7. Are there cash prizes, minors attending, or personal data collected at submission? Any of these routes the rules to counsel before publication.
8. When must the brief be published? Is this a one-off or a recurring edition?
9. Do participants bring their own problems, or do you supply the problem statements?

Once I have those, the brief gets built in order: rules and eligibility first, then tracks and problem statements, sponsor framing and fallbacks, evaluation category names, and the submission checklist. Each section comes to you for approval before anything is published.