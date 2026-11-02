# Northbound rating sheet and selection plan

I read the skill and its references. I haven't seen your published call, so the assumptions are listed at the end.

## Changes to your plan

| Your plan | Change | Why |
|---|---|---|
| All six rate | 1–2 people anonymize and don't score. The other 4–5 grade. | The call promised no names. A tool hiding the author field does not hide what authors wrote in the abstract, and a small team recognises regulars. Anonymizers must not vote. |
| 1–5 on overall quality | A/B/C/D/X advocacy grade, plus a mandatory comment | You will meet, so the scale should measure what the call spends: advocacy. A single "overall quality" number hides why a reviewer is lukewarm (topic or speaker?). |
| Average the six scores | Best-worst pair per proposal (e.g. "AC"). Never an average. | A mean erases disagreement. It also lets ten 3s beat one A plus one D, which is the proposal worth debating. |
| Top 22 by score | Rule-based cut before the call, then discussion of the shortlist only, then a program-fit pass | 190 proposals can't be discussed in 2 hours. A pure rank list skips topic and employer spread and the new-speaker balance. |

Solo curation is off the table. A blind-review promise rules it out.

## Roles

- **Anonymizers (2, non-voting):** see raw submissions. They rewrite identifying details into placeholders like `[Large Tech Firm]` and `[they]`. They keep identity only where it is the talk's subject. They assign random IDs so submission order can't identify anyone. They never score.
- **Graders (4):** see only anonymized proposals.
- **Arbiter:** name one person now. They decide if a reviewer won't recuse, and decide the fallback for a proposal that loses too many reviewers.

If you can't spare two anonymizers, use one anonymizer and five graders. If the team is too small to recognise regulars, platform hiding plus a published limit is the cheaper rung.

## Rating sheet

One row per proposal, one tab per grader.

| Column | Content |
|---|---|
| `id` | Random ID from the anonymizers, not submission order |
| `title`, `abstract`, `outline` | Anonymized text |
| `format`, `length` | As submitted |
| **`grade`** | A, B, C, D or X (see below) |
| **`comment`** | Mandatory, 1–3 sentences. A grade without a reason is incomplete. |
| `flag_product` | Y/N. If the audience forgot the product name tomorrow, would they keep the lesson? |
| `flag_fresh` | Y/N. Is the "latest" or "state of the art" claim still true on the event date? |
| `flag_depth` | Y/N. Does it open where most of the room follows and end deep? |
| `flag_conflict` | Free text: employer, friend or competitor tie. Fill it only if you kept reviewing despite a minor conflict. |

### Grade legend (printed at the top of the sheet)

| Grade | Meaning |
|---|---|
| A | I will actively advocate for this talk |
| B | I like it and won't advocate |
| C | Neutral |
| D | I will argue against it |
| X | Abstain: I think I know the speaker, or I have a close tie |

Write the comment so it can become decline feedback later. For example: "Concrete debugging arc, reaches a resolution; narrower than our median but the failure mode generalises."

### Aggregate columns (the anonymizers fill these, not the graders)

| Column | Content |
|---|---|
| `pair` | Best and worst grade, e.g. "AC" |
| `a_count` | Number of A grades |
| `d_count` | Number of D grades |
| `x_count` | Number of X grades |
| `status` | Out, discuss or provisional-in. Derived from the cut rule below. |

## Cut rule (write it down before anyone scores)

1. Zero A grades: out, unless a grader asks on the call to rescue it.
2. Two or more A grades and no D: provisional-in.
3. One A, or any D alongside an A: discuss on the call.
4. If rules 2 and 3 together exceed about 45 proposals, tighten *before* looking at who is in the set. Raise the bar to "two or more A" for discussion.
5. A proposal with fewer than three non-X grades is escalated to the arbiter. Don't compare its pair to the others.

The 45 is my estimate for a 2-hour call, not a sourced figure. It leaves about 15 minutes for the opening, about 15 for the fit pass and about 90 for discussion, which is roughly 2 minutes per proposal.

## Conflict of interest

Put these in the reviewer brief before scoring opens:

- Abstain with X on a colleague, an employer, a competitor, or anyone you think you've identified. This is an honour-system rule. No registry or audit exists, so any escalation beyond the arbiter is your own design.
- If you are an organiser who also submitted, disclose it to the committee before scoring. Don't score your own talk or your employer's. Set a written cap on organiser-given talks per edition.
- Sponsor-employed speakers go through the same review. Set a self-imposed ceiling on how many sponsor-affiliated slots exist.

## Where identity enters

State this to the committee and keep it written down:

- Graders never see names, through the cut and the call.
- For the program-fit pass, the anonymizers add categorical tags to the shortlist only. The tags are `employer A/B/C`, `local/out-of-town`, `first-time Y/N` and `sponsor-affiliated Y/N`.
- Names are revealed only for accepted and waitlisted speakers, so someone can coordinate them. Declined submitters are notified without graders learning who they were.

Say plainly, to the team and in any public statement: blind review is a process commitment. No evidence shows it changes acceptance outcomes by demographic.

## Program-fit pass (shortlist only, 15 minutes)

Check topic spread, employer spread, local versus out-of-town, first-time speakers and sponsor-affiliated count. Also hold back a small number of slots to fill late by invitation, close to the news cycle. A fast-moving infrastructure topic goes stale in months. Decide how many slots to hold open before the call.

Record every trade, e.g. "swapped #A in for #B to avoid a third talk from employer C". Without that record, next year's committee re-litigates it blind.

## Waitlist and notification

- Fill 22 slots, then build an ordered backup list of about 5 talks. Five is one documented single-track size, not a rule.
- Send acceptances first, with a confirmation deadline.
- Send declines only once acceptances are confirmed. Include a recap of the published criteria and your acceptance ratio (22 of 190, about 11.6%). That is a cheap, honest reframe.
- Tell waitlisted speakers the date they will know. Don't give odds.
- If you can afford it, send edited per-proposal feedback. Mandatory comments make that nearly free to produce.

## Timeline across the three weeks

| When | Step |
|---|---|
| Days 1–3 | Anonymizers process the 190 proposals. Committee signs off the rubric, cut rule and COI brief. No grading before this. |
| Days 4–15 | Graders score. Aim for every grader reading all 190 (about 4 minutes each, about 13 hours). If that's too heavy, assign each proposal to at least three graders, which is the one sourced coverage threshold. |
| Day 16–17 | Anonymizers compute pairs and statuses. They circulate the discussion list and tags. |
| Day 18–21 | Call, then fit pass, then notifications. |

## Metrics to record for next edition

- Acceptance ratio (22 of 190).
- Balance outcome: first-time speakers, employer spread, local share.
- Proposals per grader, and how many lost graders to X or recusal.
- Declined-submitter return rate.

Write down now what result would make you change the rubric. Treat any balance target as a goal or a gate, and decide which before review opens.

## Assumptions to confirm

1. The call promised only "without seeing names". If it also published criteria or a notification date, the sheet must carry those criteria and the dates must hold.
2. This is a community-owned event with no bought slots, and there are no invited talks in the 22. If there are invited talks, keep them out of the blind pool and reduce the open slots.
3. Two people can anonymize about 190 proposals at roughly 5 minutes each in the first three days.
4. The submission form carries no financial-assistance request. If it does, anonymizing is also what enforces "asking for money doesn't hurt your chances".

If any of these is wrong, the cut rule or roles change. Tell me which, and I'll rework that part.