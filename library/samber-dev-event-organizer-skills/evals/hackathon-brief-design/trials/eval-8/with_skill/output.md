# Saltmarsh Hack brief: what to do in 4 days and 5 hours

I read the skill and its three references. Your constraints mean the brief can only be published if two things are settled first. They are minors and personal data. Everything else is cheap.

I have not run the full interview. Section 2 lists the answers I still need, and sections 4 and 5 are drafts that depend on them. The skill asks for approval section by section before anything is published, so nothing below is final.

## 1. Do this first (15 min, today)

**Send the data and minors review request now.** The skill treats two of your facts as gates, not menu choices:

- **Minors expected:** 16-year-olds from the technical school.
- **Personal data collected:** the form takes names, emails and school.

Both require a review before publication. That review is by counsel, or by whoever owns data protection for your organizing entity. Efficiency does not get a vote.

You have no lawyer, and the skill says that removes the route to full legal-grade text. It does not make a self-written substitute acceptable. Do not write consent or privacy wording yourself. Ask three places, in this order:

1. **Your organizing entity's data-protection contact.** For an association, that is whoever signs for it.
2. **The technical school.** Schools already run consent and safeguarding for outside events, so ask what they require for students to enter. This is a question for them, not a rule for you to write.
3. **Your national data-protection authority's free guidance for small organizers.**

Ask all three the same four questions:

1. What must the form tell a 16-year-old and their parents or guardian?
2. Is parental consent needed to enter, to be photographed, or to receive a cash prize?
3. Is the school field justified?
4. Can a minor's name sit next to a public repo?

The last question matters because the standard rule set makes code public and keeps it public to stay prize-eligible.

**Cut what you collect while you wait.** Minimizing is the one lever you control without a lawyer:

- Keep **name and email** only if the rules need nothing else.
- Keep **school** only if a rule uses it, for example verifying a student category. If no rule uses it, remove the field.
- Skip the optional "may we contact you later about your project" checkbox this year. It adds data, and the consent for it needs the same review. Add it in edition 2.

**Deadline for the reviewer.** Ask for an answer by **end of day 3**. If none comes, you have three honest options:

- Delay publication.
- Publish with even less data collected.
- Publish with the form closed until the review lands.

Do not publish an open form on day 4 with the review undone. The skill treats that as the point of no return.

## 2. Answers I still need (you can reply in one message)

These decide which rung each menu lands on:

1. **Hacking window:** start and end wall-clock times, and in person or digital.
2. **Demo and judging structure:** expo table, stage pitch, video only, or hybrid. This is a fixed input, and it decides the submission checklist.
3. **Problems:** do teams bring their own, or do you supply them? With sponsors funding prizes, the skill deletes the open theme, so you supply them. Confirm.
4. **Sponsors:** does either signed agreement promise a named challenge track? Does either sponsor ask for IP terms?
5. **Sponsor tech:** does either sponsor's API, data or hardware need keys? Has anyone on your team built something small against it? What happens if it goes down mid-event?
6. **Eligibility:** who may enter (age floor, school, geography) and who is barred (organizers, volunteers, judges, sponsors)? What team-size rule is already decided?
7. **Theme:** is it narrow, for example one vertical, or open to any domain? A narrow theme triggers the demand test in section 3.
8. **Prize payout:** who receives the cash, and how does a minor receive it? This belongs to the cash-prize skill, but the question comes up in the review.

## 3. Rung choices (re-ranked for your constraints)

| Menu | Choice | Why |
|---|---|---|
| Rules rigor | **Adopted standard set, plus an age carve-out if the review sets one** | **Minimal is deleted** because the prizes carry cash value. **Full legal-grade is unreachable** because you have no counsel. The adopted set costs under an hour and is built to be forked. |
| Recurring edition | Adopted set with edition fields isolated at the top | Written once and reused, so next year is an edit of dates and prizes. |
| Challenge tracks | **General track plus one optional bonus challenge per sponsor** | **One unified challenge is deleted** because sponsors fund prizes. Each sponsor needs a published criterion to attach its prize to. |
| Not chosen | A youth or beginners track | It needs fraction wording and per-track eligibility text, and with a handful of entrants it risks an empty track. |
| Problem statements | **Structured statement** (context, question, constraints, resources, minimum viable submission) | **Open theme is deleted** because sponsors fund prizes. A fully specified challenge is the longest lead time here, so it is out for a 4-day deadline. |
| Sponsor depth | **Optional bonus challenge** | **Required for one track** needs a signed track promise and someone on your team who has built against the API. If either is missing, stay optional. |
| Sponsor fallback | A published fallback sentence per sponsor prompt | If their platform fails, teams are judged on design and integration plan, not on a working call. |

If the theme is narrow, run the demand test: pick a checkpoint date, set your own pre-registration count, and write the wider theme down now. It costs about 15 minutes. Skip it if the theme is open.

## 4. The edition block and the rules text

**Edition block.** This is the only part that changes yearly.

> **Saltmarsh Hack [YEAR]**
> - Hacking window: [start, day, time, time zone] to [end, day, time, time zone]
> - Submission deadline: [wall-clock time, named time zone]
> - Judging mode: [as chosen by the format decision]
> - Prizes: each challenge track awards a prize. *(No figure appears here. The amount belongs to the cash-prize decision.)*
> - Code of conduct: [link]. Report to: [a person or address you control]

**Rules, adapted from the published MLH set.** It is explicitly offered for forking. I adapted the wording. Edit the bracketed fields.

1. Teams have [1–4] people. [Solo entry allowed / not allowed.]
2. Organizers, volunteers, judges, sponsors and anyone in a privileged position at the event may not compete.
3. Every team member takes an active part.
4. One project per team. A team **may** enter that one project in several challenge tracks. Entering a sponsor track never forfeits the general prize.
5. Crossposting to other hackathons is [allowed / not allowed].
6. No work on the project before the window opens, and development stops at the deadline. Ideas may be old, but code may not be reused from earlier projects.
7. Libraries, frameworks and open-source code are allowed if listed in the readme. Open-sourcing old code only to use it here is not allowed.
8. After the deadline, debugging and small fixes are [allowed up to a few lines / not allowed]. New features are never allowed.
9. AI tools may be used. Teams list them in the submission and answer questions about them. A project may not be a reskin of an existing AI tool. Undisclosed use is grounds for disqualification.
10. Code is publicly available and stays public afterwards to remain prize-eligible. Remove API keys before sharing. **Hold this line until the review answers the public-repo question for minors.**
11. Organizers may disqualify a team for breaking these rules, breaking the code of conduct, or unsporting behavior.

**Eligibility text.** The source says its copy-paste set contains no age limit, and its "students only" line must be replaced. Define every word a team could argue about:

> Open to [age floor]+ [and/or students of ... ]. "Student" means [definition with a numeric boundary, for example graduated within N months]. Participants under [age of majority] must [requirement supplied by the reviewer].

I deliberately left the minors requirement blank. Whether it is parental consent, school sign-off, or both is a legal question for the review, not a sentence for me to write.

**Intellectual property: write no clause at all.** The MLH set has none, and the skill states ownership is a jurisdictional question. Do not write "participants keep their work" as if it were a fact. If a sponsor asks for IP terms, stop and route it to counsel through the sponsor-agreement decision. You have no counsel, so tell that sponsor you cannot offer IP terms by day 4.

## 5. Tracks, problem statements, checklist, categories

**Tracks.**

- **General track.** One structured statement under the Saltmarsh theme.
- **Sponsor track A.** An optional bonus challenge.
- **Sponsor track B.** An optional bonus challenge.

Each sponsor track needs five things:

1. The prompt is written as a problem, never from the sponsor's marketing copy.
2. The sponsor confirms the rewrite.
3. The access path is published: where keys come from, the rate limit, and who to ask.
4. The constraint is stated as a capability, not "must use Sponsor X".
5. The fallback sentence is written.

**Problem statement skeleton, one per track:**

> **Context** (2–3 sentences, who has this problem). **The challenge** (one sentence ending in a question mark). **Constraints** (only what a judge can check). **Resources provided** (and what is *not*). **Minimum viable submission** (the smallest real entry; "a single working flow counts, a design with no running code does not").

The minimum viable submission matters most. Teams typically reach about a quarter of their own plan, so make that quarter demoable. For beginners and 16-year-olds, keep resources ready to use rather than ready to find.

**Submission checklist.** This is derived from your demo structure, which I don't have yet. The default parts are:

- A public code link.
- A readme listing frameworks and AI tools.
- A one-paragraph description in the team's words.
- Keys removed.

The rest depends on the format:

- Expo table: no video unless it is optional and says so.
- Video only: a video of two minutes or less, made during the event, naming the hackathon at the start.
- Stage pitch: a named presenter and a slide deadline.

State the deadline as **a wall-clock time in a named time zone**, before the first judging slot. State the late policy before anyone is late, and say what "submitted" means: the link exists and is reachable.

**Evaluation categories.** Name them. **Do not print any weight, scale or total.** Weights belong to the judging decision. Starting from the published set: **Technology, Design, Completion, Learning.** Adapt the descriptions to a school-heavy audience. Learning suits them well.

**What is not judged.** Print the exclusion list with a reason for each. The published shape excludes code quality, pitch quality, idea quality and real-world problem fit. Decide the content for your event, and make sure it does not contradict any sponsor prize. Print the elimination criteria (binary knockouts) next to the categories.

## 6. Your 5 hours

| Slot | Time | Task |
|---|---|---|
| Day 1 | 0:15 | Send the review request (section 1) |
| Day 1 | 0:30 | Answer the open questions (section 2) |
| Day 1 | 0:45 | Rules and eligibility: edit the 8 fields, leaving the minors line blank |
| Day 2 | 1:15 | Three structured statements, 25 min each |
| Day 2 | 0:30 | Sponsor confirmation and fallback sentences. Send each sponsor its prompt for sign-off. |
| Day 3 | 0:30 | Submission checklist, categories, exclusion list, deadline |
| Day 3 | 0:30 | Ambiguity pass, then add the reviewer's wording |
| Day 4 | 0:30 | Pass-threshold check, your approval, publish |

That is 4:45, leaving a 15-minute buffer. Use the buffer for the reviewer's edits, because they are the likeliest slip.

**Ambiguity pass.** For every rule, write the reading a team arguing the opposite would use. A rule with a second plausible reading is not yet written.

**Pass threshold: all seven exist in writing with zero blanks before publishing.**

1. The hacking window, with start and end times.
2. The eligibility statement.
3. The team-size rule.
4. Each track's problem statement, with its minimum viable submission.
5. The submission checklist matching the chosen demo format.
6. The named evaluation categories.
7. The submission deadline with its late policy.

Then freeze the brief. A rule added after teams start building applies to a competition nobody entered. Two other things are not yours to resolve in this brief: the prize figure and payout to minors, and any weighting.

## 7. Record for edition 2

- Every clarification question asked during the event. Each one names a sentence the next brief needs.
- Submissions rejected as invalid, and why.
- Tracks that drew no entries.
- The reviewer's wording, kept as a reusable block.
- Which fields you edited in the rule set.
- Whether anyone asked for the school or contact data, so you can decide whether the form needs them.

## One decision for you

Section 1 sets a hard dependency. Do you have a named person for the data-protection review at your organizing entity, or does it have to be the school or the national authority? Answer that first, because everything else fits inside 5 hours and that step is the one that can push the date.