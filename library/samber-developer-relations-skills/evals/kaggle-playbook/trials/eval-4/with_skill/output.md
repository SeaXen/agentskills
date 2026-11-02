# Synthora on Kaggle: verdict on the dataset, email gate, medals and Kaggle Models plan

**Verdict: do the dataset, change three things.**

1. Publish it under an Synthora organization, not your personal account.
2. Drop the email gate.
3. Measure forks, downloads and tagged-link signups instead of medals.

Kaggle Models comes later, and I'd only do it with a small model, not your production generator.

I read the Kaggle playbook and its two reference files. I did not check any live Kaggle page. Kaggle renders client-side, so every number below comes from the playbook, and I flag the ones to confirm in a browser.

## Fit verdict: invest

A stranger can fork a notebook, load your data and run it with the internet off, and you sell data, so the dataset row ranks highest for you.

## What I assumed

I assumed answers where you gave none. Tell me which are wrong, because each one moves the plan.

| Question | Assumption | What changes if wrong |
|---|---|---|
| Who posts? | You, as a named account with little Kaggle history | If you already have Expert-tier standing, skip the week 1–4 earn-first phase. |
| Goal and date | Adoption by practitioners, no hard launch date | If a competition or launch date exists, the competition starter-notebook row moves up. |
| Hours | About 6 per week, solo | At 2 hours per week, drop to one notebook per month and skip the forum phase. |
| "Same model" | A Synthora generator model uploaded to Kaggle Models | If you mean something else, my Models advice needs redoing. |

## Your three ideas

| Idea | Verdict | Why |
|---|---|---|
| Personal account owns the dataset | ❌ Change | The playbook says content comes from named people but the organization profile is the brand surface. Datasets can sit under an organization. If the dataset lives on your personal account and you leave, Synthora loses it. Request the organization now, since Kaggle must approve it. |
| Form link in the description to get the "full" version | ❌ Drop | A public Kaggle dataset has no email gate, and every download is anonymous to you. A crippled free version also scores worse on usability and draws "bait" comments. I found no explicit Kaggle rule against it, so that second risk is [practitioner] and unconfirmed. Put lead capture behind the product (see below). |
| Success = medals | ❌ Replace | A dataset medal needs 5, 20 or 50 counted votes for bronze, silver or gold. Novice votes, self-votes and votes on posts older than about 90 days don't count. Forks count as votes. Medals reward votes, not adoption, and they push you toward the vote-collusion Kaggle bans for. |
| Kaggle Models, "same model" | ⏳ Later | See Kaggle Models below. |

### Dataset design (40 GB)

- **Size limits.** 40 GB fits the 200 GB per-dataset cap [platform]. The cap on top-level files is 50, so use folders or partitioned parquet.
- **Forkability.** The fork test is whether a stranger can fork the notebook and run all cells. I could not confirm Kaggle's notebook RAM and disk limits live, so check them in a browser before you commit to 40 GB. A saved output is capped at about 20 GB [platform]. If the notebook can't load the full set, ship a slice of a few GB (my suggestion) that the starter notebook runs end to end, plus the full partitioned files.
- **Make it complete, not a teaser.** Public means the useful version. The next section covers how this earns leads.
- **Licence.** Pick CC BY 4.0 or CC0 and say it in the description. Models and datasets with custom licences gate downloads, which suppresses adoption.
- **Competing datasets.** Several credit-card fraud datasets already exist. I didn't check the current ones. Search Kaggle first and open your description with what yours has that they lack: scale, a documented fraud-pattern taxonomy, known label noise, or a temporal split.
- **Synthetic claims.** Don't claim privacy guarantees you haven't tested. If you generated it from real cardholder data, do a privacy review before publishing, because publishing is hard to reverse.
- **Usability score.** Fill every field: subtitle, tags, cover image, source, licence, file and column descriptions, and a public notebook. The 0–10 score feeds dataset search.

### Where leads come from instead of the form

- **Notebook cell.** The last cell of the starter notebook says: "Need your own schema or more rows? {Synthora link with tracking tag}". It is one "About" cell at the end, not a banner on top.
- **Product link.** Link to a free-tier generator, a hosted demo or a docs page. Don't promise a bigger copy of the same data.
- **Dataset page.** Link the starter notebook, not the form.
- **No vote asks.** Announce in the Accomplishments forum only. Never ask anyone, on or off Kaggle, for votes.

### Kaggle Models

- **Ranking.** It is below the dataset, notebook and organization profile in value per hour, and it is not low effort.
- **Variations.** A Kaggle model variation is framework + weights + licence. Uploading your production generator gives the product away.
- **Safer version.** Train a small generator on your public dataset and use an Apache 2.0 or MIT licence, so it is allowed in competitions. A custom licence gates downloads.
- **Gate.** Do it only after the dataset's starter notebook passes the fork test and draws outside forks. Then the model gets its own notebook and the same tagged link.
- **Weights size.** The cap is 200 GB public [platform], which is not a constraint here.

## Ranked surfaces for Synthora

Offline-capable and data-first, so the dataset row moves up.

1. Dataset with a starter notebook (+++ value, ++ effort).
2. Full forum answers in active competitions (no links), which builds standing.
3. A standalone notebook on a public dataset.
4. Organization profile (request it now).
5. Kaggle Models.
6. Accomplishments post.

The playbook's default rung is forum answers from week 1 and one standalone notebook from week 3, in parallel. Your dataset is the standalone notebook's dataset, so move it to week 3–4.

## Fork-test plan

I haven't run it, so no result yet. Before publishing:

1. Ask one colleague to fork once from their own account and run all cells. Never spread the test across the team, because each fork is a vote.
2. Pin package versions in the first cell.
3. State the accelerator in the first cell (CPU is fine for tabular fraud).
4. Make sure the runtime fits the session cap, and say the expected run time.
5. Keep any API key out of the notebook. Kaggle Secrets don't follow forks and don't work with internet off.

## Eight-week cadence (about 6 hours per week, you)

| Week | Do | Hours |
|---|---|---|
| 1 | Request the organization. Reach Contributor tier: profile, phone, one notebook run, one submission, one comment, one vote. Start answering 2–3 competition forum questions a week, in full, with no links. | 6 |
| 2 | Same forum answers. Draft the dataset description and column documentation. | 6 |
| 3 | Build the starter notebook. Fork test with one colleague. | 6 |
| 4 | Publish the dataset under the organization, with the notebook. Post once in Accomplishments. | 6 |
| 5–6 | Answer comments within two days. Ship version 2 with a changelog cell. | 5 |
| 7 | Second notebook on the dataset (a different task, such as a drift study). | 6 |
| 8 | Read forks, copies and comments. Decide whether the Models step is worth it. | 3 |

## Metrics

Targets are self-set, because Kaggle publishes no vendor benchmark.

- **Primary.** Dataset downloads, and forks or copies from accounts outside Synthora.
- **Business.** Signups from the tagged link in the closing cell. Also `kagglehub` downloads if your own docs pull the dataset.
- **Secondary.** Votes, as a signal only.
- **Hygiene, threshold zero.** Removed posts, staff warnings, plagiarism reports and medal retractions.
- **Medals.** Count them if they arrive, but don't plan to them.

## Drafts, filled in

**Dataset description**

```markdown
## About

Each row is one synthetic credit-card transaction with a fraud label.
Generated by Synthora {generator version} on {date}. Not derived from real cardholder records. {Confirm before publishing.}

## Files and columns

- `transactions/*.parquet` - {rows} rows, partitioned by month. `{column}`: {meaning, unit, nulls}.
- `sample.parquet` - {rows} rows, the slice used by the starter notebook.

## Licence

CC BY 4.0. Attribution: Synthora.

## Starter notebook

{link to the notebook that loads it}
```

**Notebook first cell**

```markdown
# Fraud detection on synthetic card transactions: gradient boosting on the Synthora set

**Runs with internet off** on CPU, about {N} minutes.
Packages are pinned in the next cell.

I work on Synthora. The last section compares a model trained on this data with
one trained on {plain baseline} and says where the baseline wins.
```

**Notebook last cell**

```markdown
## What to try next

- Change the time split to see how the fraud-pattern drift affects recall.
- Need your own schema or more rows? Synthora generator docs: {link with tracking tag}
```

## Open questions

1. Is the dataset generated from real cardholder data, and has anyone reviewed the privacy side?
2. Which existing Kaggle fraud dataset is your closest competitor, and what does yours do that it doesn't?
3. Is there a hard date, such as a launch or conference, that should drive the schedule?

**Next action:** request the Synthora organization on Kaggle today. Kaggle approves it, so it blocks week 4.