Neither deliverable belongs to `event-booth-experience`, so I stopped without building the spreadsheet or drafting the reply. I read the SKILL.md and `references/setup-teardown-and-staffing.md` in full. I did not read `decision-menus.md` or `floor-plan-and-booth-specs.md`, because the routing question didn't need them.

**Why I stopped**
- **The spreadsheet.** The skill says "Never build a per-sponsor tracking matrix here." It lists that as a failure mode (rebuilding `event-sponsor-fulfillment`'s job). A row per sponsor for payment, staging, power drop and questions is a per-sponsor matrix, and that skill covers the payment gate and staging for each signed sponsor.
- **The Vantiq reply.** Answering one sponsor's FAQ from the floor brief is also `event-sponsor-fulfillment`'s job. This skill only produces the generic brief for every sponsor.
- **The shipping answer.** The skill says to "route every venue-specific figure to the venue rather than stating it." I don't have the venue's shipping window, delivery address or receiving fees. Anything I wrote would be invented, and a crate sent to a venue that won't accept it is expensive.

**What this skill gives you**
- The Vantiq reply needs the shipping answers first. The skill's venue questions are:
  1. How soon can sponsors start shipping, to what address, and what fees apply to received shipments?
  2. What hours does your team have access to the space?
  3. Is there secure overnight storage, explicitly including sponsors' equipment?
- The published FAQ pattern routes shipping to the organizers instead of publishing self-service instructions.
- The spreadsheet should include the power request deadline as a published date. The skill names a missing deadline as a failure mode: the drop lands on the morning at a venue that needed two weeks.
- That deadline, the shipping window and the move-in time are rows of the master schedule, written as offsets from the moment registration opens on day one. You don't have that schedule yet.

**Next step**
`event-sponsor-fulfillment` exists in the sibling skills folder. I haven't read it. It should handle both the 14-row tracker and the Vantiq reply.

To go ahead, send me:
1. The venue's shipping window, delivery address and receiving fee, or tell me you don't have them yet.
2. The power request deadline.
3. The registration-open time on day one.

If you want the full floor brief first (schedule, tier specs, power allocation), say so. That is the right order if the venue answers aren't settled yet.

Which do you want: fulfillment skill now with those three facts, or floor brief first?