# Labelforge Kaggle competition: setup plan

## Bottom line

Three of your goals conflict, and you have to resolve that before anything else.

| Goal | What it needs | Conflict |
|---|---|---|
| Medals on the line | Kaggle-run Featured or Research competition. As I understand Kaggle's progression rules, Community competitions award no medals. | Kaggle approves these and sets the rules, including the winner license. |
| Grandmasters show up | Medals, a clean problem, a trustworthy leaderboard. Prize money matters less than you'd expect, and $15k is modest. | None, if the first two are met. |
| Proprietary winning models | Exclusive IP assignment from winners. | Kaggle-run medal competitions typically require winners to grant an open-source or non-exclusive license. Exclusive assignment drives Grandmasters away. |

**Recommendation:** drop "proprietary" and replace it with "productizable". Run a medal-awarding competition and accept a non-exclusive license. Open-source licenses such as MIT and Apache allow commercial use, so your ML team can still ship what wins. Competitors can too. Your moat becomes the labeled data, your labeling workflow, and your integration, not model exclusivity.

If exclusivity is non-negotiable, run a Community competition with custom rules. You'd get no medals and few Grandmasters. I wouldn't do that.

⚠️ I can't verify Kaggle's current hosting fees, license options, or medal thresholds from here. Confirm all of them in step 1.

## Steps

1. **Contact Kaggle's host team this week.** Ask for each of the following in writing:
   - Whether they'll host a Featured or Research competition at a $15k prize pool.
   - Any hosting or management fees on top of the prize. Your budget has no room for these, so a fee may end the Featured route.
   - Which winner licenses they allow.
   - The minimum-team and medal rules.
   - Their timeline from approval to launch.
   - Fallback: if Featured doesn't fit, ask about Research.
2. **Clear the data legally before anything else.** Every participant gets the images.
   - Confirm Labelforge owns the images and labels, or holds written rights from the data owners to publish them.
   - De-identify the data, including DICOM headers, burned-in text, and dates.
   - Check HIPAA and GDPR exposure, and any ethics approval or consent requirements.
   - Pick a data license that allows competition use. Kaggle will probably want some post-competition access too.
   - Expect this to be the longest-lead item.
3. **Build a trustworthy evaluation.** Grandmasters leave quickly if the leaderboard is noisy or leaky.
   - **Metric:** Dice, plus a boundary metric such as Hausdorff or surface distance. Specify per-class handling and empty-mask handling.
   - **Splits:** split by patient, never by slice. Hold out whole sites or scanners in the private test set to reward generalization.
   - **Test data:** keep it hidden permanently. Make the public/private split big enough that the private score doesn't shake up wildly.
   - **Quality checks:** audit label noise on the test set. Have a second annotator review it, because disputed labels sink credibility.
   - **Format:** prefer a code competition (notebook submissions) so test images never leave your control. Add a runtime limit.
4. **Set rules that make winners usable.**
   - Cap inference time and hardware. Otherwise you get 30-model ensembles that you can't deploy.
   - Require winners to submit reproducible code and a write-up.
   - Set team size, daily submission limits, and entry and merger deadlines.
5. **Set the timeline.** "Next quarter" is tight if Kaggle approval takes weeks. A realistic plan:
   - Weeks 1–4: Kaggle approval, legal clearance, and data prep in parallel.
   - Weeks 4–6: baseline, metric, and a dry run.
   - About 8–10 weeks live.
   - Then winner verification and prize payment.

   If clearance slips, launch next quarter and start approval now.
6. **Allocate the $15k.** The whole budget is the prize pool, and anything else comes out of it or out of internal time.
   - Reserve roughly $1–1.5k for costs you can't absorb: legal review, validation compute, payment and tax handling. If Kaggle charges a fee, this plan changes.
   - Split the remaining ~$13.5k top-heavy. For example: 1st $6.5k, 2nd $4k, 3rd $2k, 4th $1k.
   - Prizes to international winners come with tax and withholding paperwork. Plan staff time for it.
   - If you don't need the reserve, add it to the prizes.

## Your ML engineers

They almost certainly can't compete. Host employees are normally ineligible, and they know the data and the test set. A fair, credible leaderboard matters more than their participation. Give them these jobs instead:

- Build the baseline and starter notebook.
- Own the metric and validation, and audit the test labels.
- Answer questions in the competition forum, because visible, knowledgeable host engagement is a Grandmaster draw.
- Prepare the post-competition path: review winning solutions, distill or simplify them, and integrate them.

If they want to compete, run a separate internal exercise on a different split. Keep it off the public leaderboard.

## Realistic expectations

- $15k is low for a medal competition. Pull Grandmasters with problem quality, data cleanliness, and metric trust, not just prize money.
- Medals depend on Kaggle's team-count thresholds, so participation decides how many medals are on offer. Promote it. Host a launch post, tag relevant communities, and write a clear problem statement.
- Open-licensed winners mean you get working code and write-ups, but not exclusivity. Budget engineering time to turn them into something deployable.

## Decisions I need from you

1. Do you own, or have publishing rights to, the images and labels?
2. Is non-exclusive licensing acceptable, or is exclusivity a hard requirement?
3. Do you have a hard launch date, or can the start slip a few weeks?