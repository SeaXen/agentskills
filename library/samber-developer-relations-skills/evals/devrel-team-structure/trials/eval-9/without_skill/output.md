## Vantor Mesh DevRel restructure

### The reorg doesn't fix the actual problem yet

Five people run twelve programs (API docs, 2 blogs, Discord, webinar, 3 SDKs, sample apps, champions, conference track, YouTube, changelog, Stack Overflow). That's already thin coverage per person. Moving to Marketing and splitting into two pods with two leads takes 2 of those 5 people partly out of production work and into people-management — you're not adding capacity, you're adding a coordination layer on top of the same capacity that already missed two quarters of goals.

Before locking the structure, get the VP to answer: were the misses caused by (a) Product setting DevRel goals DevRel doesn't fully control (feature-adoption metrics, roadmap dependencies), or (b) genuine overload — 12 programs, 5 people, nothing done well? If it's (a), moving to Marketing and renegotiating OKRs solves it and the pod split is optional. If it's (b), splitting into two pods without adding headcount makes it worse, not better. Recommend the answer below regardless, but flag this diagnosis as the thing that determines whether you also need to ask for headcount alongside the reorg.

### Recommended structure

```
VP Marketing
 └─ DevRel Lead (overall, player-coach — see headcount note below)
     ├─ Content Pod Lead
     │    └─ 1-2 ICs
     └─ Community Pod Lead
          └─ 1 IC
```

Don't give this five-person team two full people-managers with no working overall lead — that's 2 managers over 3 ICs. Either make the two pod leads player-coaches who still own programs directly, or keep one overall DevRel lead and make "content" / "community" informal swimlanes owned by senior ICs, not a full second management layer, until the team grows past ~8.

### Program ownership

| Program | Pod | Why |
|---|---|---|
| API docs | Content | Accuracy needs proximity to code/API changes, not audience-building skill |
| Changelog | Content | Same — technical accuracy, not narrative |
| SDKs (×3) | Content | Engineering work; needs whoever on the team can actually code |
| Sample apps repo | Content | Same — code artifact, not editorial |
| Engineering blog | Content | Editorial, but technical-audience |
| Product blog | Content | Editorial |
| YouTube channel | Content | Produced artifact, one-to-many |
| Discord | Community | Relationship-driven, real-time, people-facing |
| Champions program | Community | Relationship management |
| Conference track | Community | Speaking pipeline, event presence, relationship-driven |
| Stack Overflow presence | Community | Reactive, one-to-one-at-scale, relationship-adjacent |
| Monthly webinar | Split, single owner | Content pod builds the deck/narrative; Community pod runs registration, live delivery, follow-up. Pick ONE owner (recommend Community) so it doesn't become a two-owner orphan. |

Content pod ends up heavier (7 workstreams, including all engineering-adjacent work) than Community (5). Staff it 3 people (lead + 2 ICs) against Community's 2 (lead + 1 IC) — don't split 5 people evenly just because there are two pods.

Flag internally that "content vs. community" isn't really the fault line inside this list — "engineering-adjacent accuracy work" (docs, SDKs, samples, changelog) and "audience/relationship work" (everything else) is the real split, and it happens to map onto Content vs. Community here only because of how you've bucketed it. Make sure whoever leads Content actually has (or manages someone with) the engineering chops to keep 3 SDKs and API docs from rotting — that's a different skill than running a blog calendar.

### Protect technical accuracy through the reporting-line change

Moving to Marketing risks optimizing the team for top-of-funnel metrics (blog traffic, webinar attendance, YouTube views) at the expense of docs/SDK accuracy, which has no natural champion once Product isn't the reporting line. Give the Content Pod Lead a dotted line to Product/Engineering specifically for API docs, SDKs, and changelog, with a review SLA (e.g., docs updated within N days of an API change) — otherwise accuracy drifts silently and you'll be back here in a year with a different complaint.

### Before you lock this in, cut scope

Two pods covering 12 programs with 5 people only works if something gets deprioritized. Candidates to cut or pause, in order:
- **Product blog** — if it duplicates ground Marketing's existing content team already covers once DevRel sits under Marketing, fold it into their calendar instead of running it twice.
- **Conference track** — if the speaking pipeline is thin, treat as opportunistic (submit CFPs, don't run a dedicated program) rather than a standing workstream.
- **Stack Overflow presence** — if volume is low, downgrade from "owned program" to "someone checks it weekly," freeing real capacity for Discord/champions.

Don't cut API docs, SDKs, changelog, or Discord — those are the ones with the highest cost if neglected (broken trust with existing developers) versus the highest ones with the highest cost if skipped (missed reach with new ones).

### Metrics per pod (replace whatever caused the last two misses)

- **Content pod:** docs freshness (days from API change to doc update), SDK release cadence + issue response time, blog/YouTube reach and engagement, sample-app usage.
- **Community pod:** Discord active members + response time, active champions + content produced, webinar attendance + follow-up engagement, conference talks accepted.

Set these fresh as part of the move — don't let the new pods inherit the old Product-set goals that already failed twice.

### Sequencing

1. Get the VP to confirm the root-cause diagnosis above (capacity vs. goal-setting) — changes whether you also ask for headcount.
2. Move reporting line to Marketing, set the dotted-line SLA back to Product/Eng for docs/SDKs.
3. Name the two pod leads as player-coaches, not pure managers; assign the 3/2 IC split.
4. Cut or downgrade the 2-3 lowest-ROI programs above to make the split viable at current headcount.
5. Set the new metrics per pod before the next quarter starts, so this isn't goal #3 that gets missed under a new label.