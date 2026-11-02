# TraceForge landing page: keep the single CTA, or extend the CFP?

I read the skill and its three references. I haven't seen your live page, so everything below rests on what you told me.

## Answer

1. **Don't keep the single Register button.** Your single-CTA rule is right for a ticketed event, but your situation meets both conditions where the skill says to promote Propose to a second button.
   - Your CFP and ticket windows overlap for six weeks, and the skill's threshold is "more than a couple of weeks".
   - Your call is running short, and then speaker acquisition is the binding constraint, not ticket sales.
2. **Don't extend the CFP yet.** Fix the door first, then decide the extension at a checkpoint with real data. Details are below.

## 1. Why the footer link fails

The skill names this case directly: "a CFP demoted to a text link for a month is a CFP nobody sees."

- Your link sits in the footer, which is worse than a text link in the hero.
- The PyCon US 2026 page you're likely thinking of has one button because it has one open action. Yours has two.
- One primary action on screen at a time is still the rule. The skill's default rung is a single date-gated primary. Two things move you off that default: the six-week overlap and the shortfall of submissions.

**What to ship (the "dual gated row"):**

- Register and Propose in the hero as two independent buttons, each shown only inside its own date window.
- Register gets the primary style. Propose gets a clearly secondary style, such as an outline button. It is a button, not a footer link.
- Next to Propose, a line like "Call for talks closes April 30". The date comes from the CFP timeline, not from me.
- Contact stays on screen at every phase.
- The Propose button links out to the CFP page. The form and timeline belong to `event-cfp-design`, so don't design them here.

This still looks clean. It is two buttons, not the four-button row the skill's negative example warns against.

## 2. CTA transition table

Dates are yours. Owners are blank because I don't know your team.

| From | Phase | On screen | Owner |
|---|---|---|---|
| Mar 1 | CFP open, no sales yet | Propose (primary), Notify me or Contact | ? |
| Mar 15 | On sale, CFP still open | Register (primary) plus Propose (secondary) | ? |
| Apr 30 close | CFP closed | Register only. Remove the CFP section instead of leaving a "closed" notice. | ? |
| Speaker reveal | Program building | Register, plus a Speakers section | ? |
| Agenda release | Program live | Register, plus Program | ? |
| Early-bird close | Final push | Register, with the ladder rung updated by `event-ticket-pricing` | ? |
| Oct 14 | Doors | Practical info | ? |
| After Oct 15 | Archived | Contact, plus recordings and photos, and a status line on the hero | ? |

- Speaker reveal, agenda release and early-bird close have no dates yet. They come from the marketing plan and the ticket ladder.
- The Apr 30 row is the one most likely to be missed. A Propose button still live on May 1 sends speakers to a closed form.
- Check whether Apr 30 is inclusive.
- If nobody can change the page on a date without a developer, use the manual route.
  - Put every row in the campaign calendar as a dated task with one named person.
  - Set the reminder one day before.
  - Write each transition as a checklist item, for example "remove Propose, remove the CFP section".

## 3. Extending the CFP to June

The call to extend belongs to `event-cfp-design` and `event-marketing-plan`. The page follows whatever they decide, so I'm giving a judgment here, not a ruling.

**Why wait:**

- **The arithmetic needs a clean read.** 18 submissions for 40 slots means you can't fill the program even by accepting everything. But you are three weeks into an eight-week call, with five weeks left.
- **You haven't tried the free fix.** The Propose button hasn't been visible yet, so today's count reflects a hidden call. An extension buys time for the same hidden call.
- **Extending moves other dates.** Speaker reveal and agenda release slide later. Berlin attendees and international speakers have visa and travel deadlines, and your 500 seats are already on sale against an unpublished program.

**What I'd do (my judgment, not from the skill):**

1. Ship the dual row now.
2. Have the program chair work the direct-invite and relay channels in parallel. That is outside this skill, so route it to `event-cfp-design`.
3. Set a checkpoint about two weeks before close, around April 16, and compare submissions against the 40-slot need.
4. If the call is still short at the checkpoint, extend once, with one new announced date. Don't extend in rolling steps. The page then moves the Apr 30 row to the new date and shifts the reveal dates.

## 4. Use last year's edition

This is the second edition, so an archive probably exists. The skill's top-value rung is to substitute the archive for content that doesn't exist yet.

- Put last year's talk recordings and photos next to the Propose button. That answers a speaker's real question, "what is this event like for a speaker?"
- **Check consent before publishing (Q11).** Recordings need what the speaker agreements actually granted. Photos need the badge opt-out that attendees were offered. A republished recording can't be un-published.
- Add the "other editions" list to the hero. It is a recurring-event field.
- Keep Program and Speakers off the page until they are real. Show "Program announced [date]" only if that date comes off the schedule and you'll hit it.

## 5. Things the skill says not to do

- **No A/B test.** An event page never reaches the roughly 1,000 sessions or 30 conversions the skill treats as the floor.
- **No conversion-rate target.** Published rates describe SaaS and paid-traffic funnels, not event pages, so I won't give one.
- **Don't move dates, prices or the positioning sentence on the page.** Carry the anti-positioning sentence verbatim: "There are many [archetype] events. This is not one of them."

## 6. Pre-launch gate

All four checks must pass before the new hero goes live. I haven't run any of them, because I haven't seen the site.

1. Every transition in the table has a date, a named owner, and fires on time.
2. What, who, when, where and what it costs are answerable on a phone, without scrolling, by someone who has never seen the event.
3. The event JSON-LD block validates and carries the real dates, location and URL. `ExhibitionEvent` is one option, so pick the subtype that fits.
4. Registration completes with the keyboard alone, including the payment step. Your accessibility sibling sets the WCAG target, and I haven't seen its scope.

## Questions that would change this

1. Who edits the page on a date, and can they do it without a developer? That decides between date-gated rendering and the manual route.
2. What are your positioning sentence and contrast sentence, word for word?
3. Does the past-edition archive exist, and what do the speaker agreements and badge opt-out permit?
4. What accessibility scope did `event-accessibility-inclusion` set?

## Hand-offs

- **To `event-cfp-design`:** the call is short. Ask for a decision rule on the extension, and for the direct-invite channels.
- **To `event-marketing-plan`:** tracked per-channel links for the Propose button, and the transition dates in the campaign calendar.
- **To `event-attendee-email-sequences`:** what happens after someone clicks Register. I haven't written those emails.