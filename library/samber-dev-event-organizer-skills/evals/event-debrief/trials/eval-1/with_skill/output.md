# PixelForge Summit debrief: is your co-organizer right?

**No.** Run the debrief, but make it the light version: one 60-minute session plus a 10-minute written pre-read from each of you.

## Why "only when something breaks" is wrong

- **Where the rule comes from.** Your co-organizer is borrowing it from outage post-mortems. SRE teams only write a post-mortem above a severity threshold, such as a SEV1 or an outage longer than 15 minutes.
- **Why it doesn't transfer.** A post-mortem contains an incident. A debrief improves something you will run again, and PixelForge returns every year. The skill says to run it every edition, unconditionally, and names "it went fine, let's skip it" as the failure the rule exists to prevent.
- **A quiet edition still has things worth saving.**
  - Practices that worked but nobody named get dropped quietly next year. Talks on time and budget on plan didn't happen by accident, and someone probably did something specific to make them happen.
  - "Zero incidents" is a claim you haven't tested yet. A debrief checks it against your risk register and run of show, and catches near-misses and things that only worked because someone improvised.
- **Your exhaustion is a finding.** Three people wiped out after an edition where nothing went wrong is a team-health signal. It is exactly what the debrief is meant to catch while it is still small. !!Con and JSConf EU both published this kind of burnout assessment only at shutdown, years too late to route it.
- **Timing.** You are 8 days out, which is fine. The skill warns that around six weeks out the timeline gets rebuilt from the loudest three memories and the quiet failures are gone. Your planning start in about five weeks is the deadline. Hold the session in the next 7 to 10 days, and book it today before the three of you disperse.

## The lightest version that still works

I haven't asked you the full interview, so these choices rest on three facts I could see:

- There are three of you.
- You are exhausted.
- Planning starts in five weeks.

Because of the exhaustion and the five-week deadline, I cut the multi-track and per-track options entirely. For a team of three they would be ceremony.

### 1. Calendar it now (2 minutes)

Pick a date inside the next 7 to 10 days. Do not wait until you feel rested.

### 2. Written pre-read (10 minutes each, done alone)

Each of you sends the others:

- 3 things that went well.
- 3 things that went poorly.

Since nothing went badly, use these prompts for the second list:

- Near-misses.
- Things that only worked because someone improvised.
- Work nobody owned.
- Anything you could not keep up with.

The pre-read stops the first speaker from anchoring the room. It also surfaces what the quietest person saw.

### 3. One 60-minute session

| Segment | Time | What happens |
| --- | --- | --- |
| Frame | 3 min | Read the blameless opening aloud (below). |
| Timeline | 10 min | Walk the edition chronologically, built from the run of show, chat history and ticketing timeline before memory. Mark disputed steps and gaps. No judgment yet. |
| What went well | 10 min | Do this first. Name what has to be deliberately preserved next year. |
| What went poorly | 10 min | Cover observations, not verdicts. |
| Reconcile | 10 min | Check against only the documents that exist: risk register, planned vs. actual budget, run of show, and the goals you set before the event. If a document doesn't exist, say so and skip it. If the goals were never written down, label that section "reconstructed", not "measured". |
| Team health | 7 min | Put it on the agenda explicitly. Phrase findings structurally, for example "one person held three roles with no backup", never "they took on too much". |
| Owners and dates | 10 min | Give every entry a name and a date, or an explicit "no action, because…". |

Decide the publication question inside the room, in the last couple of minutes, so it doesn't become homework.

### Blameless opening to read aloud

> We are reconstructing what happened, not deciding who is at fault. The question this session asks is what conditions allowed something, never who caused it. Everything that went wrong here went wrong inside a system we all built, mostly at the end of a long day. Nothing said in this room becomes a performance judgment, and nothing leaves it except the findings we agree to write down.

If any of you are unpaid volunteers, add this: nobody is here on work time, and saying "I could not keep up with this" is a finding about the workload, not about the person.

### 4. Write each finding in three parts, and no deeper

1. What happened, stated as a condition and never as a person.
2. What you did in the moment. "Nothing could be done" is a complete answer.
3. What changes next edition, with an owner and a due date.

Do not run 5-Whys on these. At most one or two findings per edition justify it.

### 5. Tracking: owner and date on every entry, plus plan carry-over

- Paste every open item into next edition's work-back plan as a real task. This costs about 30 minutes, and your five-week deadline favors it.
- Skip the standing tracker.
- Add one mid-cycle check-in only if an item has a shorter fuse than the planning cycle, such as a venue deposit or a sponsor conversation.

### 6. Publication: recap only, and let it slip

- A recap isn't on the planning critical path, so it can wait.
- A transparency report is only relevant if you received code-of-conduct reports. Please confirm the count.
- Findings you already wrote in step 4 make a short "what we're changing" section cheap to add later.
- If the event is private or NDA-bound, publish nothing.

## What you'll end up with

- One dated log of three-part entries, each with an owner and due date or an explicit no-action.
- Four handbacks. The risk-register, budget and run-of-show reconciliations go to the siblings that own them (`event-risk-management`, `event-budget`, `event-run-of-show`). The fourth is a goals check: did this edition hit the targets you set, passed on to `event-market-fit` as a signal only.
- Any team-health findings, routed to `event-team-structure`.
- A publication decision with its reason.
- A handover of the log to `event-continuous-improvement`. Trends across editions belong there, not in this debrief.

## How to tell it worked

- **One pass/fail test:** zero orphan entries. Every entry has a named owner and a date, or an explicit "no action, because".
- **Numbers to record, not hit:**
  - Days from doors closing to the session. This one will be about 8 plus however long you wait.
  - Role coverage. The target is 3 of 3 of you in the room or on the pre-read.

## What would change this plan

Tell me any of these and I'll re-rank:

- Were the goals written down before the event?
- Are all three of you unpaid volunteers, or is anyone's manager involved?
- Is leadership handing over after this edition?
- How many code-of-conduct reports came in?
- Is the event private?