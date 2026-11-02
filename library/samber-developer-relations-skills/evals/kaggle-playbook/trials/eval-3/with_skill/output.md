# Labelforge medical image segmentation competition on Kaggle: setup plan

I read the `kaggle-playbook` skill and both of its references. Figures are labelled **[platform]** (Kaggle docs, rules, staff) or **[practitioner]** (community reports). Kaggle changes prize caps and medal rules without notice. I could not check live pages, so confirm every figure marked "confirm" in a real browser before you commit.

## 1. Your three goals conflict

| Goal | Community Competition ($15k fits) | Featured Competition (with Kaggle) |
|---|---|---|
| Grandmasters show up | Weak. Without medals, a $15k pool is the only draw. | Strong. |
| Medals on the line | Typically none [platform]. | Usually yes [platform]. |
| Winning models stay proprietary | Possible only with a "write-up only" winner licence. | Negotiated; confirm with Kaggle. |
| Fits $15k | Yes, self-serve and free to host. | No. It is negotiated and priced well above a Community prize pool. Seen prize pools run $25k to $1M+ [practitioner]. |

- **Community Competitions** typically award no points or medals [platform]. The skill's expectation is students and newcomers, not Grandmasters.
- **Featured Competitions** need a partnership with Kaggle. Your whole budget is smaller than the lowest Featured pool seen.
- **Hackathon** is not an option. Community Hackathon pools cap at about $10k, and the format is judged write-ups, not segmentation scoring.

You can get two of the three goals at this budget. Pick which two before anything else.

## 2. Recommendation

Run a **Community Competition** with a **write-up-only winner licence**. Tell your leadership the medals goal is out unless Kaggle says otherwise.

1. Before committing, ask Kaggle in the Competition Hosting forum or through the partnership route. Ask whether a $15k medical-segmentation competition qualifies for medals, and what a Featured deal would cost. Don't promise medals externally until Kaggle confirms in writing. I can't verify that a Community Competition can award them.
2. If medals matter more than the $15k cap, the real choice is a larger budget for a Featured Competition. That is a finance decision, not something to squeeze into this budget.
3. If medals and Grandmasters are non-negotiable and no extra budget exists, don't host this quarter.

## 3. What "proprietary" can mean

You can't keep the winning models fully proprietary and also run a public competition.

- **Winner licence is a rules choice.** Options are OSI (Apache 2.0 or MIT), CC-BY 4.0, or write-up only. Never plan to keep winning code proprietary without saying so in the rules.
- **Write-up only** is the closest option. Winners don't have to license their code, but you receive a public method description, not the model or weights.
- **Public competition code is OSI-licensed by rule.** Anything shared in the competition's forum or notebooks is deemed licensed under an OSI licence that allows commercial use. Strong ideas will be public and free for anyone, including competitors, before the competition ends.
- **Your real proprietary edge** is your data pipeline, the labeled data's quality, and what your ML team builds from the public write-ups.
- **A separate commercial deal with winners** (buying weights or code) is outside the rules block above. Whether Kaggle allows that arrangement, and how to word it, is a question for the Competition Hosting forum. Don't assume it.

Write the winner licence into the rules and Overview before launch. Never change it mid-run.

## 4. Your ML engineers

- **They can't win prizes.** Exclude employees, contractors, judges and organizers from prizes in the rules. They may compete only where your policy allows.
- **My recommendation (judgment call): keep them off the leaderboard.** They know the data's labeling quirks, which is an unfair edge, and a staff win looks bad for a host trying to attract outsiders.
- **Better use of their time:** a baseline starter notebook posted in week 1 of the competition. It must carry the full method and no vote request.
- **Forum duty:** the same engineers answer data questions in the forum. Staff the forum daily for the whole run, because an unanswered data question in week one sets the tone.
- **No colleague votes or forks.** Forks count as votes. Staff votes and forks on the baseline notebook are collusion, and a vote cluster from one company is what manipulation bans target [platform, practitioner]. Use one colleague for the single fork test.

## 5. Budget

- **Prize pool: $15k** as stated. The host pays and ships prizes, including tax compliance, so bank fees, tax forms and any legal review come out of your budget too. Confirm the pool is the whole $15k and none of those costs is hidden.
- **Reserve (my judgment, not a Kaggle rule):** ask finance now. If tax and legal costs exceed zero, cut the stated prize pool rather than missing the payout. A short pool announced once beats a delayed payment.
- **Suggested split:** 1st $7,000, 2nd $4,000, 3rd $2,500, 4th $1,500 (total $15,000). Adjust if tax costs come out of the $15k.
- **Payment timing:** about 30 days after signed prize-acceptance documents and tax forms arrive [platform].
- **Staff time** is the hidden cost: daily forum answers plus data-question handling for the whole run.

## 6. Rules block (host), filled in

```text
PRIZES: 1st $7,000, 2nd $4,000, 3rd $2,500, 4th $1,500. Paid by Labelforge within
about 30 days of signed prize-acceptance documents and tax forms.
WINNER LICENSE TYPE: write-up only. Winners publish a solution write-up;
no code or weights licence is granted to Labelforge by these rules.
ELIGIBILITY: employees, contractors, judges and organizers of Labelforge may
participate where Labelforge policy allows but cannot receive prizes.
EXTERNAL TOOLS: free and equally accessible tools and data are allowed;
paid tiers are not required to win.
```

Add these obligations from the limits reference:
- Prize count, amounts and criteria stated in both Rules and Overview.
- A remediation window (about one week) for licence conflicts in winning code.
- An exemption statement for inputs under incompatible licences.
- Public code sharing only in the competition's forum or notebooks. Private sharing between teams disqualifies.
- Whether it's a code competition (internet off at submission) or a prediction competition. This is your call, and it sets the rules above.

## 7. Items outside the playbook

The skill doesn't cover these. Resolve them before launch.

- **Patient data:** de-identification, consent and a data licence that allows competitors to use the images. Get legal sign-off first.
- **Metrics and splits:** a segmentation metric (Dice or IoU), a hidden test set, and a leakage check across patients.
- **Data licence after the competition:** does the dataset stay public, or close? Decide and state it.

## 8. Timeline

| When | Action | Owner |
|---|---|---|
| Weeks 1-2 | Ask Kaggle about medals and the Featured cost. Get legal sign-off on the data. Finance confirms the budget split. | DevRel lead, legal, finance |
| Weeks 3-5 | Build the dataset and hidden test set. Write the rules block. ML engineers write the baseline notebook. Run one fork test from one colleague. | ML team |
| Week 6 | Submit the competition. Check the Overview matches the Rules. | DevRel lead |
| Run (8-12 weeks, your choice) | Daily forum answers. Baseline notebook posted in week 1. Answer every comment within two days. | Named ML engineers |
| After close | Collect prize documents and tax forms. Pay in about 30 days. Read the write-ups. | Finance, ML team |

Hours: expect roughly 5-8 hours per week of forum and data-question duty during the run. That's my estimate, not a Kaggle figure.

## 9. Metrics

Targets are self-set. Kaggle publishes no vendor benchmark.

- **Participation:** teams that submit, plus how many outside the company. Don't treat entrants as the goal; the segmentation scores matter more.
- **Quality:** top leaderboard score against your internal baseline. This tells you whether the competition produced something your ML team can use.
- **Forks and copies** of the baseline notebook from accounts outside the company.
- **Hygiene (pass threshold zero):** removed posts, staff warnings, plagiarism reports, and any rule disputes.

## 10. Questions for you

1. Will leadership accept "no medals" if Kaggle confirms none, or should I help you cost a Featured Competition?
2. Can finance confirm the $15k is the prize pool alone, or does it also cover tax and legal costs?
3. Is the data cleared for public release, and who owns that decision?
4. Which ML engineers are named for forum duty, and how many hours per week can they spend?

Your answers to 1 and 2 will change this plan most.