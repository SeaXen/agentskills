# Audience calendars

Contents:

1. The two audience rules, and what each one actually claims
2. Calendar categories to check
3. How to verify a category without inventing dates
4. Reading a mixed audience

## 1. The two audience rules, and what each one actually claims

Each rule below comes from exactly one organizer guide. Neither guide claims to generalize beyond its own audience, and the pair only becomes a rule because they disagree for a reason.

| Audience                                             | Day type                          | Source                        | The reason given                                                                                             |
| ---------------------------------------------------- | --------------------------------- | ----------------------------- | ------------------------------------------------------------------------------------------------------------ |
| Working professionals attending as part of their job | Weekday                           | DevOpsDays organizing guide   | Work topics belong to work life; weekends are "used for refreshing energy with family"                       |
| Students, hobbyists, personal-project builders       | Weekend, Friday evening to Sunday | MLH hackathon organizer guide | Weekdays collide with class, exams, and part-time work; a Sunday-afternoon finish gives "a sense of closure" |

Two limits worth stating to the user:

- The MLH rule is a _membership requirement_ for its member events, not merely a recommendation - strong evidence of what the audience needs, though part of its force is organizational rather than behavioural.
- Both guides are community-run; neither speaks for company-run or vendor-run events, whose attendees may be sent on employer time regardless of the day.

What neither guide gives: the size of the penalty for getting the day type wrong. They say which day, not how much a mistake costs. Do not attach a percentage to it.

## 2. Calendar categories to check

This is the method that replaces the date list this skill refuses to invent. Work outward: the categories at the top constrain nearly every event, the ones at the bottom only matter for audiences that actually reach that far.

1. **The audience's own institutional calendar.** For students, the MLH guide names exams, university and school breaks, and major events at the university or organizing body. For working professionals, the equivalents are employer quarter-end and fiscal-year-end freezes, and - because they are the family time the DevOpsDays rule protects - the school holidays of the region their children attend school in.
2. **National public holidays**, in every country a meaningful share of attendees travels from, plus the host country. Bridge days and regionally variable holidays matter as much as the fixed ones; several countries observe holidays that apply in some regions only.
3. **Religious and cultural observance calendars** for the communities present in the audience. Many are lunar or lunisolar and fall on different Gregorian dates every year, so a date that was clear last year says nothing about this year. Observance also varies within a community - some periods restrict travel or eating rather than work.
4. **Ecosystem anchor dates**: the flagship event, organizer conference, or release cycle the rest of your sub-field already schedules around. The MLH guide treats its own organizer conference this way, and it works as a template for finding the equivalent in any ecosystem.
5. **Local civic and cultural events** in the host city - marathons, festivals, trade fairs, elections. They compete for venues, hotel inventory, transit capacity, and local press regardless of topic.
6. **Employer budget and travel-approval cycles**, for events where attendance is expensed. This category is a judgment call rather than a documented rule; treat it as a hypothesis to test with two or three prospective attendees rather than a constraint to assume.

What the guides actually say about holidays is a warning against the obvious heuristic, not a heuristic of its own: the MLH guide records that holidays are "a great way to attract more crowd" in some cultural contexts, and that a short university break can _raise_ turnout for a single weekend event even though breaks generally reduce participation. So a holiday hit is a flag to investigate, never an automatic rejection.

## 3. How to verify a category without inventing dates

The failure this section exists to prevent is a confident wrong list. A reader who is told the dates are clear stops looking; a reader who is told a category is outstanding goes and checks.

- Name the specific year and the specific country or institution before looking anything up. "European holidays" is not a checkable object.
- Prefer the authority that publishes the calendar: a government's official public-holiday page, a university's published academic calendar, a religious community's own published observance dates for that year.
- If you can browse the web, verify each category against such a source and cite where each date came from. If you cannot, ask the user for the calendars that apply to their audience - they usually know their own community's better than any general source.
- Record the result per category as **checked** (with the source) or **outstanding**. There is no third state; "probably fine" is outstanding.
- Never carry a date forward from a previous year for any lunar or lunisolar observance, and never infer one country's holidays from a neighbour's.
- Report outstanding categories to the user alongside the candidate windows, so the date is chosen with the gap visible rather than after it has been papered over.

## 4. Reading a mixed audience

A genuine mix - say, a conference that wants both employed engineers and students - has no day type that satisfies both rules, and the compromise slot takes the worst half of each. Three honest ways out, in the order they are usually worth trying:

- **Pick the pole the event is actually built for** and accept lower attendance from the other. Cheapest, and it keeps the event legible to the audience it is positioned for.
- **Split the day types across the programme**: the main weekday programme for the employer-time audience, with a weekend-adjacent satellite (workshop day, hack day, community day) for the personal-time one. Costs a second day of logistics and a second volunteer roster.
- **Use the boundary days.** Friday and Monday sit on the seam between employer and personal time, which is why they attract compromise proposals. Treat this as the weakest option, not the obvious one: a boundary day is the day _both_ audiences can most easily be pulled away from, and neither guide endorses it.

Whichever route is chosen, say which pole was picked and why in the deliverable - a mixed-audience date that does not name its pole reads as an oversight to everyone it disappoints.
