# Succession and burnout evidence

The evidence behind the succession menu and burnout guardrails, plus parallels from adjacent domains.

## Succession practices actually used by recurring events

- **FOSDEM's two-manager rule:** every devroom must list at least two managers "to make sure there is a backup in case of issues." An enforced operating rule - the skill's default succession rung generalizes it to every named role.
- **EuroPython Society's voting-rights pipeline:** permanent workgroup members keep voting rights year to year, letting "non-voting members… become voting members in the following year" - a standing contributor-to-decision-maker ladder, built in 2015 specifically against knowledge loss when the conference location changes.
- **DjangoCon US / DEFNA:** succession solved structurally - the 501(c)(3) persists as the legal entity, so the conference survives as volunteer chairs rotate beneath it.
- **KubeCon co-chairs:** paid, time-boxed co-chair roles rotate "for each conference" by design, with foundation staff as the continuity layer underneath. Rotation works here _because_ a standing body holds the institutional knowledge - the precondition the menu's caveat names.
- **DjangoCon Europe's support patches:** a working group of previous organizers, plus a foundation "Events Support" function from 2027, bolted onto a full-rotation model - a knowledge-transfer layer that only partially offsets the model's documented host-recruitment fragility.

## Practitioner guidance at meetup/hackathon scale (small samples)

- **The 6-12-month handover window** - Ethereum Meetup Organisers survey (April 2020): "Once someone starts a meetup, they should keep their eyes open for the volunteers that help… those will need to take over in 6-12 months. The leaders of meetup get burnout… and someone needs to take over."
- **"It's dangerous to organize alone"** - Ted Laderas's 2024 PositConf talk on data-science meetup burnout: co-organizers, shared values, and spread duties as the resilience design.
- **Workload benchmark** - Paul Balogh's meetup write-up: "Burnout is real. Small tasks add up. Build a team of committed co-organizers," with "at least 4 to 8 hours a month" as the per-organizer preparation estimate at meetup scale.
- **Onboarding new organizers** - MLH's organizer guide recommends running the mini-events being considered for attendees as team-building exercises when integrating new organizing-team members.

## Events that ended citing burnout, in their own words

Lead with the first two - first-hand and unambiguous. Cite the last two only with their caveats.

- **JSConf EU / CSSconf EU (2019)** - the canonical case, from the closing statement: "we reached the limit of what can be responsibly handled by our volunteer team. The small community gathering we set out for has evolved into a 3 day event weekend with over 1600 attendees in total, 60+ flights and 100+ hotel stays to book, 120 scholarships to cover and a dozen visas to organize. The cost of all this exceeds one million Euro." Not a vague "burnout" - an itemized list of what became too much, carried by 6 core organizers.
- **!!Con (2024)** - co-founder Lindsey Kuper: "after !!Con 2022, the team was burned out and needed to take a year off in 2023… it's not at all surprising that we decided that !!Con should come to an end." An earlier FAQ had already flagged: "There's only so much that our small team of volunteers can do."
- **XOXO Festival (2024)** - exhaustion plus finances, and tech-adjacent rather than a developer conference; the closing statement also cited "events like ours are more financially challenging than they used to be." Corroboration, not a clean burnout case.
- **Nine Worlds (2018-2019)** - burnout plus governance and money problems, reported secondhand (the committee cited "burnout and mismanagement of volunteers and staff, as well as issues with money"). Weight lowest: mixed causes, a secondhand account, and a geek-culture convention rather than a tech conference.

## Survey evidence, and its honest limits

- **WordPress Community Team, 2020 Meetup Organizer Survey** (n=65 organizers, 26 countries): ~35% were the _sole_ organizer of their group; ~34% said one organizer plans all events. The best available quantified "bus factor = 1" proxy - roughly a third of meetup groups. The 2018 organizer roundtables had already named burnout a top cross-cutting theme: "The struggle is real."
- **The limits, stated plainly:** the quantified burnout datasets in tech measure OSS _maintainers_, not event organizers. Cite the WordPress figures as the best real numbers available, say so, and never imply precision beyond them.

## Parallels from other domains (supporting framing only)

From OSS-maintainer material (GitHub's opensource.guide) - structurally similar (unpaid, self-selected labor sustaining a community asset others depend on, no HR safety net), but drawn from open source rather than from events:

- **"Personal ecology"** (via the Rockwood Leadership Institute): sustaining energy over the lifetime of the work. The useful transfer: burnout prevention is a structure-design question - pacing, backups, rotation - not individual willpower.
- **Five burnout causes** map onto organizing-team risk:
  - Lack of positive feedback (silent satisfied attendees vs. loud complainers).
  - Not saying no (one lead absorbing adjacent unclaimed roles).
  - Working alone (a role with no peer or backup is a burnout risk by construction).
  - Not enough time or resources (unpaid roles with real deadlines and real dependents - sponsors, speakers, attendees).
  - Conflicting demands (an employer-affiliated organizer whose employer wants visibility the team wouldn't otherwise grant).
- **Mitigation levers:**
  - Multiple points of contact per area so anyone can take a break.
  - Exploring funding as a bridge from all-volunteer toward paid roles.
  - Written boundaries on what a role will and won't do.
  - Rest and tooling for mundane work.
- **Governance-document practices:**
  - Write roles, join-paths, and decision rights down (the OSS convention is a `GOVERNANCE.md` - the event equivalent is a team charter).
  - Keep leadership activity visible so the team doesn't read as a private clique to the tech-savvy volunteer base whose respect legitimizes it.
  - Move accounts, domains, and socials off any single person's personal ownership with at least one backup admin.
- **Three leadership-selection lenses** (BDFL / meritocracy / liberal contribution) - a complementary way to talk about _who gets influence_ (founder authority vs. earned roles vs. current active work), distinct from the org-layer split the skill's main menu ranks. opensource.guide flags "meritocracy" as a contested term for some communities; carry that caveat. Use these lenses only when a team is debating influence philosophy, and always labeled as borrowed from open-source governance.
- **Full-time-vs-contractor shape test** (from startup staffing material): work that carries cross-edition institutional knowledge - sponsor relationships, financial continuity, credential custody - is the shape that degrades badly when left unpaid-and-precarious; short-term, specialized, one-edition work is the shape that stays volunteer or goes to a vendor. A framing device for _why_ the paid-hire gate exists; the concrete threshold comes from the first-hire evidence in the governance reference.
