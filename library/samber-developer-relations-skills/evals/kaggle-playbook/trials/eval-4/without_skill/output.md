# Verdict: ⚠️ right channel, wrong mechanics

Kaggle is a good place for a synthetic-data company to be seen. Three parts of this plan will probably work against you: the gated "full" version, medals as the metric, and the personal account. I haven't verified Kaggle's current rules, so check the items marked 🔎 before you build anything.

## 1. The 40GB size likely kills adoption

- Kaggle notebooks have roughly 20GB of working disk and about 30GB of RAM. 🔎 Check the current limits.
- A 40GB dataset is probably unusable in a notebook, so nobody will fork it or write about it.
- No notebooks means no votes, and no votes means no medals.
- Medals are the metric you chose, so the plan undermines itself.
- Ship a 1–2GB sample that loads fast, plus one benchmark notebook. Host the 40GB version elsewhere.

## 2. The email gate on the "full" version is risky

- 🔎 A description whose main job is sending people to a lead form may break Kaggle's rules on promotional content. It would risk removal of the dataset, or a flag on your account.
- A "free sample, pay with your email for the real one" setup also reads as a teaser. Kaggle users dislike teasers, and downvotes follow.
- Synthetic data has no privacy reason to be withheld, so a gate looks arbitrary to the reader.
- The better pattern is to make the dataset truly open and give people a reason to contact you. Examples:
  - a fidelity report
  - a "bring your own schema" generator trial
  - a larger or custom volume on request
- Put that link at the end of the description and in the notebook, not as the gate. Say plainly what the person gets.
- You are collecting emails, so the form needs GDPR-compliant consent and a stated purpose.

## 3. Medals measure the wrong thing

- Medals measure approval from Kaggle's community. Most of that community are learners.
- Your buyers are data and ML teams at banks and fintechs who need privacy-safe data. Most of them don't vote on datasets.
- Gaming votes is a trap. Kaggle has started counting forks as votes, so test forks from colleague accounts would create fake votes. 🔎 Check the current progression rules.
- Track measures tied to pipeline instead:

| Stage | Metric |
|---|---|
| Reach | Unique downloads, notebooks that use the data |
| Interest | Form submissions with consent |
| Qualification | Submissions from a company domain, with a stated use case |
| Outcome | Calls booked, pilots started |

- Write the attribution rule before launch. Example: "a lead counts if the form came from the Kaggle UTM link."
- Medals are fine as a side effect, not as the goal.

## 4. The personal account is a problem for you

- The asset, its followers, and its reputation belong to you, not Synthora.
- If you leave, or if legal asks who owns the content, that becomes a dispute.
- 🔎 Check whether Kaggle supports an organization or company-branded owner for datasets. If it does, use it.
- If it doesn't, create a dedicated Synthora account that your company controls, with credentials stored in the company password manager.
- Check with your employer that you are cleared to publish under Synthora's name. A synthetic fraud dataset also gets scrutiny from finance buyers, so the legal footing should be clean.

## 5. Credibility is the real risk

- Fraud is a crowded category. The classic ULB dataset is hugely popular, and PaySim and many synthetic ones exist.
- Synthetic fraud data gets dismissed unless you prove it works.
- Include in the dataset page:
  - a train-on-synthetic, test-on-real utility benchmark
  - a fidelity and privacy report
  - a note on what the data does not capture
- One honest limitations paragraph will earn more trust than 40GB.

## 6. Kaggle Models: clarify before building

"The same model" could mean two things:

- **A fraud detector trained on your synthetic data.** This is a good idea. It is a proof of utility and a natural companion to the dataset.
- **Your synthesizer's weights.** This gives away your product, so don't do it.

Ship the dataset first and the detector second. Doing both at once splits your attention, and you are the only devrel.

## Suggested plan (about 2 weeks of your time)

1. **Days 1–2:** Decide the owner account and get legal sign-off. Write the attribution rule.
2. **Days 3–6:** Build the 1–2GB sample, the benchmark notebook, and the fidelity report.
3. **Day 7:** Publish. Put the open, honest CTA at the end of the description.
4. **Days 8–14:** Share the notebook, not just the dataset. Answer every comment.
5. **Day 14:** Read the funnel table above. Decide whether to build the Models companion.

## Questions

1. Does Kaggle offer an organization-owned option for your dataset? I couldn't confirm it.
2. By "same model", do you mean a fraud detector or the synthesizer?
3. How many qualified leads would make this worth repeating? Pick the number before launch.
4. Is your employer comfortable with the Synthora branding on a personal account today?