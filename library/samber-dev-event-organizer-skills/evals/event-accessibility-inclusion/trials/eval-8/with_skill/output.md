# StratosDev Days: quiet room sizing, and whether to explain it

I followed the `event-accessibility-inclusion` skill. I skipped its one-question-at-a-time interview and flagged what I still need at the end.

## Premise check

Employer-paid tickets don't reduce the need. The skill's rule is that an attendee's access need is identical whether the employer or the attendee bought the ticket, and no provision changes shape because of who paid. Well-paid professionals still include people who are neurodivergent, deaf, nursing, or overloaded by 900 people.

What does change with funding is the budget. At €1,400 × 900 attendees, you can fund the provision line without competing with catering. That moves you toward deeper provisions, not shallower ones. It is also the one place your "enterprise" framing is a real input. It doesn't touch the data-handling duty once someone discloses a need.

## (1) Is there a standard ratio for sizing a quiet room?

**No.** The skill's sources found no seat-per-100-attendees ratio and no square-footage rule in any accessible-conference guide, ACM page, or sensory-certification program. If a venue or vendor quotes a ratio, treat it as their own estimate, not an industry standard.

The one sourced figure is an operational observation, not a rule. An unconference series (AdaCamp Toolkit, now defunct) found "a maximum of around 5% of our attendees might be in the quiet room at any one time." It is that organizer's own experience, with a different audience and format, expressed as a share of attendees.

**What to put in the venue spec:**

| Item | Value | Label |
|---|---|---|
| Planning ceiling | 5% of 900 = **45 people at peak** | Sourced observation, applied by me. It is a ceiling, not a target. |
| Actual capacity | Pick from the rooms the venue offers. Roughly 15–25 seats would be a defensible choice if the 45 ceiling is unaffordable. | **Self-set.** Say so in the spec and on the page. |
| Size | Moderate | Sourced siting rule |
| Location | Away from the main hub | Sourced siting rule |
| Lighting | Dim | Sourced siting rule |
| Access | Wheelchair-accessible entrance and interior | Sourced siting rule |
| Nursing room | Separate room | Sourced siting rule |

Before you spec it, decide which rationale the room serves. It changes what you ask the venue for:

- **Interaction load:** a room where conversation is not allowed, for anyone who can't interact right now.
- **Sensory load:** a room for noise and light.

A silent room and a low-stimulation room are not the same space. Pick one, or define both rules explicitly.

Two more points:
- Write these criteria **before the venue is signed**. After signing, the venue's rooms decide for you.
- Name an owner for the day. A locked or unstaffed quiet room is the skill's first failure mode.

## (2) "Quiet rooms are standard everywhere, so no need to explain ours"

**The board member is wrong on both counts.**

**Not universal.** The skill's sourced counter-example is FOSDEM 2026. It provides no quiet space and says so on its own page, naming a public park five minutes away as the alternative. Published practice is also uneven. It ranges from one venue-checklist line (a hackathon guide) to a full templated page (the Linux Foundation template, which includes a named quiet space). Don't present any single event as the baseline.

**Even if it were universal, you'd still explain it.** "Quiet room" doesn't say what the room is for or what the rules are, and the skill's guidance is to state scope and rules on the page.

Publish three lines on the accessibility page, under "Spaces":

> **Quiet room: Room [X], [floor], open [hours].** For anyone who needs a break from noise, light or conversation. [Rule: no talking / low voices.] Seats [N]. No sign-up needed. Staffed by [named person].

Mention it in the 60-second opening and brief the registration desk. Anything that needs asking a human filters out the people least willing to ask, so signpost the room physically.

## Still open (the skill's interview)

- Is the venue already signed? If so, half the physical options are already fixed.
- Who owns accessibility by name until the debrief?
- Which jurisdiction applies? Public-event duties and disability-data rules are a question for counsel, and I can't answer them.
- When must the provision set be published, relative to attendees' travel booking?

I can draft the venue criteria sheet and the full accessibility page next, once you confirm those.