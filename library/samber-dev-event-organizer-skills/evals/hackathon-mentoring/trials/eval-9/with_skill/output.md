# Laying the 19 mentors onto the volunteer grid

**Don't lay mentors on by headcount. Lay them on by tag × slot.** The grid you already have schedules people. It has no idea which expertise must be in the room at which hour, and that is the one thing this plan adds.

I couldn't ask the interview questions, so assumptions are marked ⚠️ and the open questions are at the end.

## What stays in the volunteer grid

Keep all of this unchanged for mentors:

- The 4-hour shifts and the 15-minute handover overlap.
- Confirmed sign-ups.
- The rule "do not leave your post until a replacement is confirmed".
- The backfill protocol.

Mentors are a separate role, not a volunteer subtype. Give them:

- Their own lane on the grid.
- Their own sign-up form.
- Their own chat channel.
- Their own role marker.

Don't send them through the general volunteer sign-up.

## Step 1: Build the demand grid (~20 min)

Rows are the coverage units, taken from the brief's own words. Columns are your existing slots.

| Coverage unit | S1 | S2 | S3 | S4 | S5 | S6 | S7 | S8 (tail) |
|---|---|---|---|---|---|---|---|---|
| Embedded hardware | | | | | | | | |
| Applied ML | | | | | | | | |
| Accessibility | | | | | | | | |
| General stack (git, deploy, dominant language) | | | | | | | | |
| Sponsor technology, by product name (if the brief names one) | | | | | | | | |

30 h ÷ 4 h gives 7 full shifts plus a 2 h tail. Use your grid's actual cut.

Fill each cell with one of three levels:

- **Unstaffed (published as such)**: nobody holds the tag for that slot, and participants are told so.
- **Available**: someone holding the tag is on the roster and reachable through the request mechanic.
- **Guaranteed**: someone holding the tag is physically present for the stated hours.

The guarantee level comes from the sponsor-integration depth in the brief:

- **Optional bonus challenge:** available is enough.
- **Required for one track, or the sole substrate:** that unit needs guaranteed in every hour it is worked. The brief's fallback sentence promises those teams a route. If the unit is unstaffed, that promise breaks quietly.
- **No sponsor technology named:** the three tracks default to available, plus the general stack.

## Step 2: Tag-check the 19 before you place anyone (~20 min)

Make a table with one row per tag:

| Tag | Built with it | Only read the docs | Slots it must be guaranteed | Slots holders can cover |
|---|---|---|---|---|

Rules for filling it in:

- **Use the brief's vocabulary.** The tag is "accessibility", not "frontend".
- **Name the sponsor technology as its own tag.** "Knows the SDK" and "knows its language" are different coverage.
- **Record two depths only: built with it, or read the docs.** Ask at sign-up. A roster of docs-readers looks covered and isn't.
- **A mentor with two tags counts toward both tags, but not in the same slot at 03:00.** One person covering two tracks overnight is thin coverage. Mark those cells.

Then run these checks:

1. **A tag with one holder is a single point of failure.** That person is the only valid replacement for themselves. The "don't leave until replaced" rule then pins them to the floor, so a guarantee can't outlast their shift. Recruit a second holder, or downgrade that unit to available and publish it.
2. **A guaranteed cell needs a built-with holder.** If it only has a docs-reader, say so to the team plainly.
3. **If a track's tag-holders can't cover its guaranteed slots, don't fill the gap with another track's mentor.** Downgrade the cell and publish it, or recruit.

⚠️ I'm not giving a mentors-per-shift or mentors-per-participant number. None is published, and any figure I gave would be invented. The check above is a supply count against your own cells. It is not a staffing formula.

## Step 3: Place mentors from their own sign-up

- **Take the slot from the mentor at sign-up.** They pick it from the grid, you don't assign it. The slot is the commitment, and presence beyond it is a courtesy you can't schedule against.
- **Place guaranteed cells first, scarcest tag first.** Fill the rest afterwards.
- **Stagger the specialties by when each track needs help.** Don't roster everyone from open to close. Put early-stage mentors where a track is still defining its problem, and technical mentors where teams have a direction and are building.
- ⚠️ I haven't read the brief's sequencing, so I can't say which track peaks when. One hypothesis to test: hardware teams need a build mentor once parts are in hand, and accessibility teams need one early, before a design is locked. Check it against the brief.
- **Handover overlap carries two things.** The first is the shared blocked-team view, so the incoming mentor doesn't re-visit a team that is fine. The second is the visit log, if any mentor is also judging (see Step 7).
- **The replacement must hold the same tag.** Add tags to your backfill list. A backfill with the wrong tag doesn't fill a guaranteed cell.

## Step 4: Decide the overnight hours (~10 min)

Friday night is the highest-stakes stretch, because that is when the most teams are blocked. Pick one of these and publish it:

- **Staffed.**
- **Thinly staffed.** The general stack plus any unit you promised as guaranteed, with the other tracks published as unstaffed and a time they return.
- **Published as unstaffed.**

My default is thin. Don't leave it unannounced.

## Step 5: Request mechanic and what you publish

- **Publish the mentor grid itself.** Names, tags and hours go where teams read the brief, before the window opens. That is the "what each present mentor actually knows" list, and it lets a team reach the right person by name.
- **Give mentors a visible marker and a named role.** This is the cheapest fix for the failure where mentors are present and nobody can tell who they are.
- **Add a staffed mentor area if the space is more than one room, or the mentor crew is bigger than the organizing team.** Use a request channel with routing if the event is hybrid or digital.
- **Don't make scheduled office hours the only route.** This window runs overnight, and a 03:00 blocker can't wait for a 10:00 slot.
- **Don't route every request through one organizer's DMs.** That person sleeps. Any routing role needs at least two people, or a fallback participants already know.

## Step 6: Escalation when no mentor holds the skill

Publish this route before the window opens:

1. Try the roster's docs-readers, who must say plainly that they haven't built with it.
2. Ask the sponsor's channel, if it's their technology.
3. Ask the room. This is a request, never an assignment.
4. Tell the team early that no help exists. A team told at hour 4 can pivot. A team told at hour 30 can't.

Log every case as a coverage gap against a track.

## Step 7: Briefing, sponsor staff, judging

- **Mentor briefing (not the jury briefing):**
  - Logistics.
  - The request mechanic in participants' wording.
  - The code-of-conduct escalation pointer.
  - The help-versus-build boundary: mentors explain, diagnose and unblock, and don't write code that ships. If a mentor already committed to a repo, the team declares it.
  - Ask before touching anything, don't evaluate the idea, and say aloud what you don't know.
- **Sponsor staff:**
  - They are a sponsorship deliverable, not volunteers. A missing one is a fulfilment failure you take to the sponsor, not a no-show you backfill.
  - Add the engagement rule: no pitching and no recruiting while wearing the marker.
- **Judging:** if any of the 19 is also on the judge list, keep a log of which mentor spent meaningful time with which team. The recusal rule lives in the judging plan, and this log is its input.
- **Visit cadence:** set a minimum check-in number per assigned team. It's your own number, compared only with your own past editions. Stop scheduled visits before the final stretch.
- **Interruption limits:** cap each visit with a visible timer, and let teams show a do-not-disturb signal.

## Done check (all five written before the window opens, zero blanks)

1. Tags mapped to tracks.
2. The coverage commitment per track and slot.
3. The request mechanic in participants' wording.
4. The mentor briefing with the boundary sentence.
5. The escalation route for an uncovered skill.

## Open questions (they change the plan)

1. **What time does the window open?** This fixes which slots count as "overnight".
2. **Does the brief name a sponsor technology, and at what depth?** This decides whether any cell must be guaranteed. It is the biggest unknown.
3. **Is the event in person, and how many rooms?** This picks the request mechanic.
4. **Is any sponsor staff among the 19, under a signed agreement?**
5. **Is any mentor also on the judge list, and do prizes carry cash value?** Cash value forces the boundary into the mentor briefing.
6. **When does the roster close?** A close date favours community mentors, whose tagging is quick, over a sponsor negotiation.
7. **What is the tag breakdown of the 19?** Send me the per-track count and depth, and I can fill in the Step 2 table.