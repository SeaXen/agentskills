**Start here:** spend 1 hour this week getting your account to Contributor. Then run Quillsort on a live tabular competition and measure it honestly. Publish nothing about Quillsort until you have a number that holds up.

## Why this order

- Competitive data scientists already use XGBoost, LightGBM, and CatBoost.
- They switch for a reason they can verify: a speed or score gain on a competition they know.
- Marketing posts without that evidence get ignored or downvoted.
- With about 48 hours total, the evidence has to come first.

## Plan: 8 weeks at 6 hours a week

**Week 1: foundation (6h)**
1. (1h) Reach Contributor tier. Verify your phone, fill in your profile, run one notebook, make one submission, and post one forum comment.
2. (1h) Write your single claim in one sentence. It must be something Quillsort can win on, such as CPU training time at equal score, memory use, or a specific data shape. Don't write "another GBDT".
3. (4h) Pick one live **Playground Series** competition.
   - These are monthly tabular competitions with fast feedback and heavy traffic.
   - Run Quillsort in a Kaggle notebook with internet on (`pip install quillsort`) and submit.
   - Run XGBoost, LightGBM, and CatBoost on identical folds and seeds.
   - Record score and wall-clock time.

**Week 2: decide go or no-go (6h)**
1. (3h) Repeat on 2 more tabular datasets of different sizes.
2. (2h) Write down where Quillsort wins, ties, and loses.
3. (1h) Gate: if it wins nowhere, stop the Kaggle push and fix the library first. Don't spend weeks 3 to 8 on this plan.

**Weeks 3-4: first public asset (12h)**
1. Publish one notebook: a reproducible benchmark showing the wins and the losses.
   - Include the same folds and seeds, run times, and a "when not to use Quillsort" section.
   - Honest losses build trust with this audience.
2. Publish one short "drop-in" notebook: a Quillsort model inside a standard CV and ensembling pipeline.
3. Make sure both run top to bottom on Kaggle CPU with no edits. Fix the install and the first-run experience if they don't.

**Weeks 5-6: show up where competitors read (12h)**
1. Post a competition-specific notebook or discussion thread with a real leaderboard result using Quillsort. Example: "Quillsort blended with LightGBM, +0.0003 CV".
2. Answer other people's questions in that competition's discussion for about 2h a week. Mention Quillsort only when it is actually relevant.
3. Don't self-promote in threads where it doesn't fit. Don't use second or colleague accounts to vote or fork. That breaks Kaggle's rules and gets flagged.

**Weeks 7-8: measure and decide (12h)**
1. Count signals:
   - Notebook views, votes, and forks.
   - Public notebooks by others that `import quillsort`. Search Kaggle for it.
   - PyPI download change and GitHub stars.
   - Issues opened by Kagglers.
2. Fix the top 1 or 2 friction points people report.
3. Decide whether to continue, and with which competition format.

## What to skip for now

- A Kaggle "organization" or branded account. Kaggle is people-driven, and a named person posting results is more credible.
- Paid sponsorship or hosting your own competition. That is a later step, after organic proof.
- Medals as a goal. Your own tier matters little, but Contributor is needed to publish and comment.

## Risks

- ⚠️ Your claim may not survive step 2 of week 1. That is a finding about the library, and finding it early is the point of this order.
- ⚠️ Kaggle CPU notebooks have limited cores and time. Report results on that hardware, because that is what readers can reproduce.
- ℹ️ If a competition's rules limit external tools, check them before you submit.

## Next action

Open Kaggle, go to Account, and complete the Contributor checklist (about 20 minutes). Then tell me the one-sentence claim from week 1 step 2, and I'll tighten the benchmark design around it.