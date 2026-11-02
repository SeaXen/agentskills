# Kaggle plan for Gatekeep (Q4, 4 hrs/week)

## Next action (15 min)

Send your CMO the three lines below, then book a 30-min call. Don't start building anything yet.

> 1. "20M users" counts registered accounts. They are mostly data scientists and students, not people who buy CI/CD security tools.
> 2. I propose a capped 8-week test: one dataset, two notebooks, about 2 hrs/week. It has a kill rule at week 6.
> 3. A hackathon is out this quarter. It costs more than my whole budget. I'll reconsider next quarter if the test passes.

## Why not the full plan

- **Audience mismatch.** Gatekeep's buyers are platform, DevOps and AppSec engineers. Kaggle's audience is ML practitioners. The overlap is small, and the 20M figure says nothing about it.
- **Your budget.** You have 52 hours for the whole quarter. A hackathon (rules, prizes, judging, moderation, promotion, follow-up) would take 30–50 hours by itself. That would leave your core channels with nothing.
- **Attribution.** Kaggle doesn't hand you buyer identities. You'd be judging the test on weak signals, so you need a kill rule set in advance.

## The one angle that fits

Pitch **security of ML and data pipelines**, not generic CI/CD security. These overlap with Gatekeep's product:

- ML repos run GitHub Actions and GitLab CI with cloud and model-registry secrets.
- Notebooks and pipelines leak API keys.
- Model files (pickle) and third-party Actions are supply-chain risks.

The Kaggle-native format is **a dataset plus a notebook that analyzes it**. It fits the platform and shows your expertise.

**Asset 1: Dataset.** Aggregated, anonymized CI misconfiguration patterns from public workflow files. Examples are unpinned Actions, over-broad `GITHUB_TOKEN` permissions, and secrets in logs. Use public repos only, and name no repos or people.

**Asset 2: Notebook A.** "What N public ML repos get wrong in their CI". It's a data story with charts, and the last cell shows how to scan your own repo (free scanner or docs link, with a UTM).

**Asset 3 (only if A works): Notebook B.** A hands-on "secure your training pipeline in 20 minutes" tutorial.

## 13-week schedule (52 hrs)

| Weeks | Kaggle | Core channels | Notes |
|---|---|---|---|
| 1 | 3 hrs | 1 hr | Check CRM and customers for ML-team contacts. Read Kaggle's current terms on promotion. Get legal sign-off on the dataset. |
| 2–3 | 2.5 hrs each | 1.5 hrs each | Build the dataset: collect, aggregate, anonymize, document. |
| 4 | 2.5 hrs | 1.5 hrs | Write and publish Notebook A. Add UTM links. |
| 5–6 | 1 hr each | 3 hrs each | Share A in a few ML-security and MLOps communities. Answer comments. **Week 6: kill-or-continue check.** |
| 7–8 | 2 hrs each (if continuing) | 2 hrs each | Notebook B and a dataset update. |
| 9–13 | 0–1 hr | 3–4 hrs | Maintain the notebooks if the test passed. Otherwise, back to core channels. |

Total on Kaggle if the test passes: about 22 hrs. If it's killed at week 6: about 14 hrs.

## Week-6 gate

Set the thresholds from your own baselines, not from mine. Pull your typical docs and blog click-through numbers first. As a starting guess, to adjust:

- **Continue** if Notebook A gets at least about 1,000 views, at least about 30 tracked clicks to your docs or scanner, and at least one reply from someone with a plausible buyer title (platform, DevOps, AppSec).
- **Kill** if there are fewer than about 10 tracked clicks and no buyer-title replies. Report it as a result, not a failure.

Track `utm_source=kaggle` clicks, new scanner installs or signups with that source, and a self-reported "where did you hear about us" field.

## Hackathon

- **This quarter:** no.
- **Next quarter, only if the gate passes and you get budget or help:** a Kaggle community competition on "find the CI misconfiguration" is the cheapest format. Estimate 30–50 hrs of setup and moderation, plus prizes. Budget for those before you commit.
- **Cheaper option:** offer a judge or mentor slot at an existing ML-security event instead.

## Rules and risks

- **No gaming.** Kaggle's vote and medal mechanics are an engagement signal. I recall that forks were recently changed to count as votes, but I haven't verified it, so check Kaggle's current progression docs. Don't ask colleagues to upvote or fork, and don't create test forks from team accounts.
- **Disclose affiliation.** Say you're from Gatekeep, and keep the sales pitch to the last cell.
- **Data hygiene.** No secrets, internal paths or customer names in the dataset or outputs. Check everything before publishing, since notebook outputs are public.
- **Check the terms.** Review Kaggle's current policies on commercial content before you publish.

## What to tell the CMO if they push back

You are testing the channel cheaply and will have an answer at week 6. Spending the full budget on an unproven audience would be the riskier move. You can show results with real numbers instead of the user count.

## Questions for our call

1. Do any customers or leads have ML or data-platform teams?
2. Can Gatekeep share aggregated scan data, or do you need to collect public data fresh?
3. Is there a prize or event budget for next quarter?