# AceRoute Skills layout polish

Session-derived layout lessons from the next Skills-page visual cleanup pass.

## Trigger
Use this when the Skills page has the right data but the layout feels visually wrong:
- cards look overlapped even though DOM order is correct
- a card appears blank because content is compressed into one cramped row
- analytics cards are in the wrong row order
- every panel inherits the same giant fixed height and the page feels heavy

## User corrections that mattered
The user corrected two things explicitly:
1. `Category Usage` should sit beside `Skill Activity`, not lower on the page.
2. `Possible Overlaps` must look like a readable list, not a blank/dark card with a tiny badge or cramped pills.

Treat those as layout requirements, not cosmetic suggestions.

## Layout pattern that worked
Use row-specific grids instead of one shared rule for every Skills row.

### Recommended order
1. `Skill Activity` + `Category Usage`
2. `Top Tags` + `Maintenance Queue`
3. `Skills` + `Top Categories`
4. `Top Used Skills` + `Stale + Unused Skills`
5. `Possible Overlaps`
6. `Skill Details`

### Why
- the two charts belong together as the primary analytics row
- the maintenance and tag lists are both medium-height operational lists
- the big inventory panels should stay together
- overlap detection is secondary and should not compete with the main analytics row
- detail cards should stay last because they are naturally tall

## CSS/layout rules that fixed the problem
Do not force the same fixed height onto every Skills card.

Instead, use row-specific classes, for example:
- `skills-chart-grid`
- `skills-tertiary-grid`
- `skills-primary-grid`
- `skills-secondary-grid`
- `skills-overlap-card`

Pattern that worked:
- charts row: compact (`~320px` cards)
- tags / maintenance row: medium (`~560px` cards)
- skills / categories row: tall (`~764px` cards)
- top-used / stale row: medium-tall (`~640px` cards)
- overlap card: auto height, not fixed giant height

Important:
- `align-items:start` on the relevant grids
- make only the intended inner lists scroll (`flex:1; min-height:0; overflow:auto`)
- do not let overlap/detail cards inherit the same height rule as the inventory panels

## Overlap card rendering rule
Do NOT render overlap candidates as one dense pill-row.
That is what made the card look blank / broken in the screenshot.

Render each candidate as a proper row with:
- skill name
- category + use count meta
- explicit `Open` button

Suggested DOM shape:
- group header (`stub`, count)
- repeated `.overlap-skill-row`

This makes the card readable even when there is only one overlap group.

## Verification checks
Use browser DOM checks after the rebuild:
- card titles and top positions should show the intended order
- `Skill Activity` and `Category Usage` should have the same top and compact height
- `Possible Overlaps` should have a small natural height, not a giant inherited one
- overlap text should contain readable member rows, not just one compressed string

Concrete checks that worked:
- inspect `#page-skills .card h2` positions/heights
- inspect `#skillSimilarList .stack-item` height and text
- verify charts with `!!Chart.getChart(canvas)`

## Practical takeaway
When a user says a dashboard card `looks overlapped`, do not assume z-index first.
For AceRoute Skills, the real cause was layout inheritance:
- wrong row grouping
- fixed heights applied too broadly
- compressed overlap rendering

Fix the structure first, then the styling.
