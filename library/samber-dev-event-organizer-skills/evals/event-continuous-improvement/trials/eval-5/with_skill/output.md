# Meridian Summit handover: contents and log restructure

**Method:** I read `event-continuous-improvement` and its three references, then ran its workflow on your three findings. I didn't run its one-question-at-a-time interview, so I assume a full rotation with 4 editions of written records and list the answers I still need at the end. The log format, the 2-versus-3 rule and the menus are that skill's own construction, not published organizer practice. The only external backing is that a persisted, shared document survives organizer turnover (DevOpsDays) and that MLH covers a first handover.

## Bottom line

- ⚠️ **Your biggest risk is the invoicing finding.** It is the only real pattern (3 of 4 editions), and the knowledge leaves with your crew. The log can't fix that. Write the procedure down before you hand over.
- The interpreter and teardown findings are **candidates** (2 of 4 each). Hand them over as candidates, with cheap fixes attached.
- Restructure the log by cleaning and classifying the live entries. Don't rewrite history, and don't retrofit all 4 editions into a new schema.
- Your handover is more than the log. It has five parts, listed in section 4.

## 1. The three findings, filed

All three pass the signal gate: current, reproducible in the event's own conditions, and generalizing. Per the de-personalisation rule, none of them names a person.

| Theme (keep this name stable) | Condition, de-personalised | Count | Label | Routes to |
|---|---|---|---|---|
| **Accessibility-service booking** | Interpreter booking has no written owner, backup owner or trigger date on the work-back plan | **2 of 4** (ed. 2, 4) | **Candidate** | `event-planning-timeline` (task) |
| **Teardown contact coverage** | Volunteer rota has one point of contact and no documented fallback during Saturday teardown | **2 of 4** (ed. 3, 4) | **Candidate** | `event-planning-timeline` (task); `event-team-structure` (evidence, flagged as 2 of 4) |
| **Sponsor invoicing: single knowledge holder** | Invoicing procedure exists only in one role-holder's head, with no written steps and no second trained person | **3 of 4** (to confirm, see below) | **Pattern** | `event-team-structure` (with the count); `event-planning-timeline` (task) |

**Interpreter**
- Two different people made the same miss. That points at a missing process, not at individuals. This cause is my inference. Check it against the original entries.
- Edition 3 is the gap. If the interpreter was booked on time that year, find out why. It may be the most useful fact in the log, and it may have lived in someone's memory only.
- Two occurrences don't justify claiming a trend. The fix is cheap and reversible, so act on it anyway.
- If you consider accessibility a legal or commitment exposure, the skill lets you lower the bar for severe-cost cases. Write the reason into the entry. That is your call.

**Teardown contact**
- The two occurrences are consecutive and recent, so it is clearly live.
- State the denominator every time: "2 of 4", never "recurring".

**Invoicing**
- "Three editions' debriefs" must mean three distinct editions, not three entries in one. Count editions only.
- Do not add this to the teardown finding's count. If you group both under a parent theme such as "single point of failure with no written fallback", recount by the union of editions. Adding the two counts together manufactures a pattern.
- Do not fold the interpreter finding into that parent theme. Its fix is a scheduling trigger, which is a different change.
- Sponsor renewal and sponsor demand belong to `event-market-fit`. Hand those over separately and say the split out loud: this log is operational only.

## 2. Restructuring the log

### Persistence
- **Rung:** the structured entry record. Four editions of records, full rotation and a compounding event all promote it over the appended document.
- **Fields:** theme, first-seen edition, occurrences as "N of M", status, condition, disposition, routed to, owner, audit verdict.
- **Don't retrofit all 4 editions.** Convert only the entries that pass the gate. Keep the raw debriefs as a linked archive.
- **If your hours are tight,** fall back to the appended document with the same fields written as one line each. That works at a lower ceiling.
- **Never delete a resolved entry.** Close it with the reason.
- **Entries naming a person** (such as "Priya forgot") get rewritten as conditions before they enter the log.

### The city change
Tag every entry **portable** or **site-bound**. Rotating cities makes this the key step.
- **Portable:** process and structure. All three findings above probably are.
- **Site-bound:** venue, local vendor, local rules. The gate says an entry caused by a venue the event has left is history, not a candidate. Close it as "host city changed" and don't delete it.
- **Check the invoicing finding.** If the procedure depends on your legal entity, bank or accounting setup, the new crew may not run it the same way. Then what transfers is the principle, "write the procedure down and train a second person", and not your steps.
- **Interpreter lead time** is local to each provider pool, so the new crew must find their own.

### Trend depth
- **Default:** group by theme, with recurrence counted in editions.
- **Promoted:** the written trend review. The new crew didn't witness any of this evidence, so push it at them. Section 4 uses it as the handover cover document.

### Audit
- **Do one full pass now, in one sitting, before you leave.** Classify every entry Keep, Update, Consolidate, Replace or Delete. The only pass threshold is zero unclassified entries.
- **Skip a standing audit owner.** It needs someone who stays, and none of you do.
- **Hand the new crew two passes:** a kickoff pass before their planning, and a closure pass after their edition, with a "did it improve, yes or no, and why" column on each change record.
- **Rough effort** for the audit is 2 to 3 hours for 4 editions. That is my guess, and it depends on log size.

## 3. Change records

These are the first change records for the incoming crew to adopt. Checks must be observable at the edition, not surveyed afterwards. Every number is a placeholder for the crew to replace.

**CR-1: Sponsor invoicing procedure (do this one first)**
- **Change:** write the step-by-step procedure now, and have a second person run it once under supervision.
- **Because:** it is the only pattern at 3 of 4, and the holder leaves with the rotation.
- **Check:** the second person produces a sponsor invoice end to end, unaided.
- **Owner:** your crew writes the procedure now. The new crew runs the shadow session.

**CR-2: Interpreter booking**
- **Change:** add a dated task on the work-back plan with an owner, a backup owner, and a trigger date derived from the local provider's real lead time.
- **Because:** two different owners made the same miss, so the process failed.
- **Check:** written confirmation of the booking by a date set from that lead time, read off the plan. As a placeholder, at least double the 2-week point.

**CR-3: Teardown fallback contact**
- **Change:** put a named fallback with a working phone number on the run-of-show.
- **Because:** one point of contact failed in two consecutive editions.
- **Check:** the fallback is called at the start of teardown and answers within a set time. The placeholder is 5 minutes.

Bundling warning: the skill advises one deliberate change per edition so outcomes can be attributed. CR-1 is something you do before you leave, so it isn't a next-edition change. CR-2 and CR-3 sit in different workstreams with independent checks, so attribution holds. If the new crew is stretched, order them CR-1, then CR-2 (attendee harm), then CR-3.

## 4. What the handover contains

1. **Cover note, which is the first written trend review.** It states the bounds: 4 editions held, "candidate" means 2 and "pattern" means 3, the log is operational only and demand signals are handed over separately, and the blameless rule.
2. **Theme list** with the denominator on every count. Keep it to one page.
3. **Every live entry** in the structured format, with portable or site-bound tags.
4. **Change records** (CR-1 to CR-3) with their check lines. Outcomes are blank until the closure pass.
5. **What you tried that didn't work.** Nobody writes this list and every incoming crew needs it. Failed fixes are invisible in a log that only records findings.
6. **Sibling hand-offs, evidence only:** the demand signals to `event-market-fit`, any size ceilings to `event-growth-strategy`, and per-vendor rebook verdicts on each vendor's own record. Those are the other categories the skill routes out of the general log.
7. **Custody:** one named person on the incoming crew who opens the log before planning starts, and the date they do it. "The team" is the answer that produces a log nobody re-reads.

## 5. Order of work

1. Get the answers below.
2. Write the invoicing procedure (CR-1) while its holder is still reachable.
3. Convert and classify the entries: de-personalise, tag portable or site-bound, close the venue-bound ones.
4. Draft the cover note and change records.
5. Do the custody hand-off, then the three-way review with the incoming lead.

## What I still need from you

1. Which editions did the invoicing issue appear in, and are they three distinct editions?
2. How did edition 3 handle the interpreter booking?
3. Is the invoicing process tied to your legal entity or bank, and will the new crew use the same one?
4. Does any body survive the rotation, such as a steering group or a past-organizers group, to hold the log? If not, who receives it? DjangoCon Europe added a past-organizers support group for this case, which the skill cites as precedent.
5. How many hours do you have before handover, and what is the date?
6. Do you keep a list of fixes you tried that didn't work?