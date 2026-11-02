# Take-home brief: Developer Advocate candidate assignment

## Scenario to hand candidates

Give all three the same concrete scenario — not "write about our API" (too open, rewards prior blogging experience) but a specific developer problem:

- Provide sandbox API key + docs link (same for all three).
- Scenario: "A developer wants to add usage-based billing to their SaaS app using Quilt Metrics. Write a tutorial that gets them from zero to seeing their first usage event tracked and a billing threshold alert firing."
- Define the reader explicitly: "a backend engineer, mid-level, who has never used a metering API before."
- Say what "done" looks like: 1,200-word tutorial (markdown or Google Doc), working code snippets they actually ran, 5-min Loom walking through the same flow live.

## Logistics (fixes fairness problems before they show up in scoring)

- **Give 7 days, not 48 hours.** A tight deadline structurally favors whoever has no day job or existing content pipeline to fit around — irrelevant to the actual skill you're testing.
- **Assign a real contact for technical questions during the take-home.** This is literally the job (unblocking developers) — test it, don't just test solo output.
- **Put in writing**: ownership of the submission, whether/how it might ever be published, and that it's evaluated only if they don't move forward — no surprise repurposing of unpaid work.
- **State explicitly in the brief**: "We're evaluating this submission on its own, not your existing portfolio. Two candidates in this process already have public blogs/talks — that history does not factor into scoring here." Say this to all three candidates. It normalizes the field and gives you cover to actually enforce it in step below.

## Rubric — score the submission blind to who wrote it

Strip names, assign submission IDs, have 2+ raters score independently before comparing notes. This matters here specifically: two candidates' work will "read like" polished existing content and pattern-match to competence; the career-changer's won't have that halo, positive or negative. A structured rubric is what stops "familiar voice = better" from substituting for actual measurement.

| Dimension | Weight | What you're actually checking |
|---|---|---|
| Technical accuracy | 25% | Code runs as written, steps match sandbox reality, no hand-waved errors. Hard gate: if the tutorial's core flow doesn't work, cap the total score regardless of prose quality. |
| Teaching clarity | 25% | Progressive disclosure, no unexplained jargon, anticipates the reader's likely confusion points. This is the core DevAd skill — test it directly, don't infer it from byline count. |
| Developer empathy | 15% | Did they pick realistic details (error handling, rate limits, what happens when the key is wrong), or just happy-path the demo? |
| Verbal delivery (Loom) | 15% | Score separately from the writing — pacing, whether they can explain live under time pressure, whether they got flustered by real errors on screen. This is the "conference talk" skill in miniature; test it fresh rather than trusting a CV line. |
| Structure/craft | 10% | Hook, clear steps, working snippets, recap, one clear next action for the reader. |
| Initiative | 10% | Did they add anything unprompted — a diagram, a troubleshooting section, a suggestion for the docs themselves. |

Scale each 1–4 with written anchors (e.g., for teaching clarity: 1 = reader would get stuck, 4 = reader could follow with zero prior context) so raters aren't scoring on vibes.

## One thing worth flagging, not deciding for you

Unpaid 6–8 hour take-homes are industry-standard, but for a Series B company hiring a DevRel specifically — someone whose entire job is "produce content that represents us publicly" — some candidates and communities read unpaid content-creation take-homes less favorably than unpaid coding take-homes, because the output looks uncomfortably close to free marketing labor. A small honorarium ($150–300) or an explicit "we'll credit/link this as your byline regardless of outcome" costs little and removes that read entirely. Your call — just flagging it as a live norm in DevRel hiring specifically, not general engineering hiring.