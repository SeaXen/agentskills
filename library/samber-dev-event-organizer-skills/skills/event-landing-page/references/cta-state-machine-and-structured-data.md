# The date-gated CTA state machine, and structured data

Contents: the published gating rules · the transition table · the manual fallback · structured data · what this does not cover.

## The published gating rules

Three buttons, each rendered from the event's own front-matter dates:

| Button       | Renders when                                                                                                                                 |
| ------------ | -------------------------------------------------------------------------------------------------------------------------------------------- |
| **Propose**  | the current date falls between `cfp_date_start` and `cfp_date_end`                                                                           |
| **Register** | registration is explicitly flagged open, **or** the current date falls inside the registration window and registration is not flagged closed |
| **Contact**  | an organiser email exists - unconditional, at every phase                                                                                    |

Two properties of this design are worth stating, because they are what makes it more than a rendering trick:

- **The page consumes dates it does not own.** The CFP dates come from `samber/dev-event-organizer-skills@event-cfp-design`, and the registration window comes from `samber/dev-event-organizer-skills@event-ticket-pricing`. Both already exist before the page does, and the page never invents a phase.
- **The two gates are independent.** Neither suppresses the other, so both buttons can be on screen at once when the windows overlap. That overlap is exactly the case the dual-row rung in SKILL.md exists for.

## The transition table

Build this table before writing any markup, one row per transition, with a real date and a named owner in every row. The phases come from `samber/dev-event-organizer-skills@event-marketing-plan`; the per-row CTA and section states are this skill's own construction, laid over the gating rules above.

| From date          | Phase            | Primary CTA           | Secondary              | Sections live                                                                   |
| ------------------ | ---------------- | --------------------- | ---------------------- | ------------------------------------------------------------------------------- |
| -                  | Pre-announcement | Contact               | -                      | Nothing public                                                                  |
| announcement       | Announced        | Notify me, or Contact | -                      | Hero, dates, location, positioning, CoC                                         |
| `cfp_date_start`   | CFP open         | Propose               | Notify me              | + CFP link, speaker benefits                                                    |
| `cfp_date_end`     | CFP closed       | Notify me, or Contact | -                      | CFP section removed, not left saying "closed"                                   |
| registration opens | On sale          | Register              | Propose, if still open | + ticket ladder, refund policy                                                  |
| speaker reveal     | Program building | Register              | -                      | + Speakers                                                                      |
| agenda release     | Program live     | Register              | -                      | + Program, schedule banner                                                      |
| early-bird close   | Final push       | Register              | -                      | ladder rung updated by `samber/dev-event-organizer-skills@event-ticket-pricing` |
| doors              | Live             | Practical info        | -                      | + on-the-day details                                                            |
| after doors        | Archived         | Contact               | -                      | + recordings, photos; status line on the hero                                   |

Two rows are load-bearing and get skipped most often:

- **CFP closed**: remove the section rather than leaving a "submissions are closed" notice on the front door - the notice is a placeholder wearing different words.
- **Archived**: FOSDEM's page carries an explicit status line once the edition ends, which is the honest alternative to a site that looks live for another eleven months.

## The manual fallback

Many event sites cannot evaluate a date at render time: a hosted page builder, a static file somebody edits by hand, a volunteer with no developer. Where that holds, the manual path is the correct mechanism rather than a downgrade from the gated one. The state machine is unchanged; only its enforcement moves from the renderer to a person with a calendar.

The four steps below are this skill's own construction, and they suit a small event where one person carries every transition:

1. Take the transition table above and copy each row's date into the campaign calendar `samber/dev-event-organizer-skills@event-marketing-plan` already maintains, as a dated task rather than a note.
2. Name one person per transition. An unnamed transition is one that silently does not happen, and the stale Propose button is the most common casualty.
3. Write the target state of each transition as a checklist item - "remove the Propose button, remove the CFP section, add the notify-me capture" - so whoever executes it does not have to re-derive the intent.
4. Set the reminder one day before the date, not on it. A CFP that closes at midnight needs the button gone that morning.

It is more fragile than date-gated rendering, and it still beats a developer dependency on every campaign moment. Say which mechanism you chose and why.

## Structured data

The DevOpsDays theme auto-emits a `schema.org` `ExhibitionEvent` JSON-LD block on every event page. Fields:

- `name`
- `description`
- `startDate` and `endDate`
- `url`
- `image`
- `location` - an object carrying the venue name and its address

Emit the equivalent on the front door. It is a machine-readable copy of facts the page already states, so it costs nothing beyond keeping it in sync, and it is the one pre-launch gate item a script can verify outright. Two rules:

- Never let it carry a date the visible page contradicts.
- Update it when a date moves rather than treating it as write-once.

`ExhibitionEvent` is what this source emits. Other event subtypes exist; pick the one that matches the event and do not treat this specific value as the requirement. The requirement is a machine-readable name, description, dates, URL, image and location.

## What this does not cover

Search visibility strategy, keyword targeting and content-driven acquisition are outside this skill entirely. The structured-data block is a page-completeness requirement - a public event whose dates and location are not machine-readable is incomplete - not an SEO programme. Anyone asking for the latter needs a search skill, not this one.
