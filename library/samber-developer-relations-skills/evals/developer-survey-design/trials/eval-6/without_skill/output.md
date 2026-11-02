Cut the draft to about 15 questions, a 10-tool random grid, and 1 optional free-text box. Then time it with 5 people.

My estimate of the current draft is 9 to 12 minutes. I used these assumptions, so check them in the pilot (step 5):
- Closed question: about 10 seconds.
- Grid row: about 6 seconds.
- Free-text box: about 40 seconds if answered.

| Part | Time |
|---|---|
| 23 closed questions | about 4 min |
| 30-row grid | about 3 min |
| 4 free-text boxes | up to 2.5 min |
| **Total** | **about 9.5 min** |

## Steps

1. **Triage the 28 questions (30 min).**
   - Write the decision each question changes next to it. If no decision changes, cut the question.
   - Cut anything you already know from CRM or signup data. Pass those values in as hidden fields.
   - Cut near-duplicates.
   - Target 15 or fewer. This step saves about 2 minutes.

2. **Randomize the grid.**
   - Show each respondent 10 of the 30 tools, chosen at random. Keep the 4-point scale.
   - Cost is about 1 minute, down from 3.
   - You still get about 500 responses per tool (1,500 × 10 ÷ 30), which is enough for a rate of roughly ±4 points.
   - Alternative: ask a single checklist, "Which do you use regularly?". It takes about 20 seconds but loses the "heard of" and "tried" levels. Pick it only if you don't need those levels.

3. **Keep 1 free-text box, at the end, optional.**
   - Make the prompt specific, for example "What is the one thing we should fix first?". "Any other feedback?" gets low-value answers.
   - Four boxes can produce thousands of comments, and you can't hand-code that in six hours.
   - One box at a 30 to 40% answer rate gives about 500 comments. Coding them by hand takes 2 to 3 hours.
   - Better: have an LLM draft the themes, then you check 100 comments by hand. Confirm Tidewrack's data policy allows sending comments to an LLM.

4. **Add branching.**
   - Use 2 or 3 screener questions, such as role or usage level. Show follow-ups only to people they apply to.
   - Each person then sees about 12 questions instead of 15.
   - Branching adds a little analysis work, because each follow-up has a smaller base. Keep it to 2 or 3 branches.

5. **Pilot with 5 to 8 people, timed.**
   - Use the median and the slowest quartile. Aim for a median of 3.5 minutes or less. Only then do most people finish under 5.
   - Ask the VP: does "under five minutes" mean the median or the maximum? The maximum is impossible to guarantee.
   - Write "about 4 minutes" on the invite only after the pilot.

6. **Format for speed.**
   - Use single-choice over multi-select.
   - Put each scale on one page and use mobile-friendly layouts.
   - Show a progress bar.
   - Make nothing mandatory except the screeners.

## Six-hour analysis budget

Write the analysis plan before fielding. Each kept question needs a planned chart. If a question has no chart, cut it.

| Task | Time |
|---|---|
| Clean data (drop speeders and straight-liners) | 0.5 h |
| Core crosstabs | 2 h |
| Grid (a tidy table of tool × level × share) | 1 h |
| Open text | 1.5 h |
| Write-up | 1 h |

The 28-question draft would not fit in this budget, mainly because of the four comment boxes.

## Next step

Paste your 28 questions. I'll mark each one keep, cut, or hidden field, and give you the revised time estimate. About 10 minutes.