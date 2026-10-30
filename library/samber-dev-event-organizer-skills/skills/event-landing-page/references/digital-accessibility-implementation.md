# Implementing the accessibility target on this page

**Scope warning, and it is the whole point of this file.** Everything here applies to the event's _digital_ surface only - this page, the site around it, and the forms it links to.

None of it says anything about physical, sensory, dietary or economic provision on site. Web accessibility and event accessibility are separate disciplines, and a conformant website is not an accessible conference.

Never present a passing page audit as accessibility coverage, and never let it stand in for the provision set.

**Never choose the target.** `samber/dev-event-organizer-skills@event-accessibility-inclusion` decides the standard, the level and which surfaces are in scope, and it owns the content of the accessibility page itself.

It also owns the full audit checklist across the whole digital layer, including the schedule, the livestream player and published program documents. This file covers only what the page build has to get right at build time, in build order.

The target that sibling sets is WCAG 2.2 at level AA, structured as the four POUR categories. Take the target from it; do not re-derive it here, and do not negotiate it downward because a deadline is close.

## Build order

The sequence below is this skill's own ordering, not part of the standard. Accessibility costs a fraction as much built in as retrofitted, and the retrofit never gets scheduled. Work in this order, because each item is cheapest at the moment listed.

1. **Structure, before styling.** Real headings in a real order, landmark regions, one `h1`. This is nearly free while the markup is being written and expensive once the visual design is done, and it is what lets someone navigate the page without seeing it.
2. **Contrast, at palette time.** 4.5:1 for normal text, 3:1 for large text and for interface components at AA. Fixing this while choosing colours costs one decision; fixing it after launch means renegotiating a brand.
3. **The CTA, when it is wired.** The primary button must be a real button or link - reachable by keyboard, with a visible focus state, and with text that says what it does. "Register for DevConf 2026" survives being read alone by a screen reader; "Click here" does not.
4. **Every form, as it is built.** Labels in text and programmatically associated, help text associated too, errors described in words rather than by colour, and a field order that is navigable by keyboard including any date picker. A field labelled only by its placeholder loses its label the moment someone starts typing.
5. **Images and the hero, at asset time.** Text alternatives for anything carrying information, and an empty alternative for anything purely decorative. If the hero puts text over a photograph, check the contrast against the busiest part of the image, not the average.
6. **Zoom and narrow viewports, before launch.** The page must remain usable at 200% zoom and on a narrow screen. Event pages break here more than anywhere else, because a date range and a venue address are both long strings in a layout designed around short ones.

## The one flow that matters most

The registration flow is the highest-stakes path on the whole site: someone who cannot complete it does not attend, and no on-site provision rescues that. Exercise it end to end **with the keyboard alone**, including any date picker, any custom dropdown and the payment step. Do it on the real ticketing platform rather than a mock: that platform is usually a third party whose accessibility you inherit without controlling.

The same applies to the CFP form, one step upstream of every lineup-diversity effort `samber/dev-event-organizer-skills@event-cfp-design` runs, and to any accommodation-request field, which `samber/dev-event-organizer-skills@event-accessibility-inclusion` owns the handling of.

This keyboard pass is item 4 of the pre-launch gate in SKILL.md, and it is binary. It passes or the page does not go live.

## Why the automated score is not the check

Automated tools catch a minority of failures, and none of the ones that matter most in a registration flow: a form technically labelled but incomprehensible, a modal that traps focus, an error that only appears as a colour change. Run a tool if your environment has one, use it to localise failures to specific elements, then do the keyboard pass - that is the step that finds the failures that stop someone attending. A perfect automated score is not conformance, and reporting one as though it were is how a page ships broken.

## When the ticketing or CFP platform is the problem

Both are normally external tools the page links out to. When the inherited flow fails the keyboard pass and you cannot change it, three honest responses exist, in order:

1. Raise it with the platform.
2. Publish an alternative route to the same outcome - a stated email or phone path to register, staffed by a named person.
3. Tell `samber/dev-event-organizer-skills@event-accessibility-inclusion`, since an unusable registration path is a provision-level fact its accessibility page has to state rather than a page-level defect this skill can quietly absorb.
