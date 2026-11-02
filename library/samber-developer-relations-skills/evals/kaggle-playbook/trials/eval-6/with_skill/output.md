# Kaggle plan for Quillsort: 6 h/week, 8 weeks, starting from Novice

I followed `kaggle-playbook` and its two reference files. I did not check Kaggle live, so every cap, quota and medal figure below is unconfirmed until you check it in a browser. Labels: **[platform]** is Kaggle docs, rules or staff, **[practitioner]** is community lore.

## Do this first (week 1, about 2 h)

1. Take your own account from Novice to Contributor. Complete the profile, verify your phone, run one notebook, make one competition submission, leave one comment and cast one vote **[platform]**. Votes from Novices don't count toward medals **[platform]**, so this comes before anything you publish.
2. Request a Kaggle organization named Quillsort. Kaggle approves it **[platform]**. It will own datasets and models. Notebooks and forum posts still come from named people.
3. Don't create a shared "Quillsort" user account. Kaggle allows one account per person **[platform]**.
4. Don't ask colleagues to vote or fork anything, and don't ask off-platform either. That breaks the same guideline **[platform]**. Forks now count as votes **[platform staff]**.

## 1. Fit verdict: invest

A stranger can fork a notebook and run Quillsort with internet off. It's a pip-installable, CPU-only library with no key or API. That passes the skill's test. The only open condition is that someone answers forum questions every week, which you're covering.

My own judgement, not from the skill: competitive data scientists mostly tune GPU-accelerated gradient boosting. A CPU-only library needs a concrete, honestly shown edge, such as speed on a CPU session, small-data accuracy, determinism, or diversity in an ensemble. Every notebook should state where the baseline wins. If you have no benchmark evidence yet, producing it in weeks 2–3 comes before any promotion.

## 2. Answers that re-ranked the surfaces

| Answer | Effect |
|---|---|
| Runs offline as a library | Starter notebook for a competition moves up to second, behind forum answers. Forum answers build the standing it needs. |
| Goal is adoption, no launch date | No dated launch. Compounding surfaces (notebooks, datasets) beat one-shot ones. |
| 6 h/week, small team | Hosting is ruled out. It needs daily forum staffing for the whole run and carries prize, tax and licence work. |
| Novice account, no presence | Standing is built before anything is promoted. Forum answers start in week 1, and the Contributor steps come first. |

I'm assuming you're the only poster and nobody else can reliably answer forum questions within a day. If that's wrong, tell me; it changes weeks 4–8.

## 3. Ranked surfaces for you

| Rank | Surface | Why now |
|---|---|---|
| 1 | Full answers in competition forums, no links | Compounding, cheapest, and builds standing. Start in week 1. |
| 2 | Standalone notebook on a public dataset | Compounding. Gets forked for months. |
| 3 (tie) | Dataset you own with a starter notebook | Best fit is a Quillsort wheels dataset, for code competitions with internet off. |
| 4 | Starter notebook attached to an active competition | Week 5 at the earliest. Its audience ends with the competition. |
| 5 | Organization profile | Cheap. Request it in week 1. |
| 6 | One Accomplishments post | The only place you may link your own work **[platform]**. |
| Skip | Kaggle Models | You ship a library, not weights. |
| Skip | Hosting a Community Competition or Hackathon | You can't staff the forum daily at 6 h/week. |
| Skip | Featured Competition, staff competing under the company name | Needs months of staff time per competition. |

Default rung: forum answers from week 1 and one standalone notebook from week 3, in parallel. Move to a dataset or competition starter once that notebook passes the fork test.

## 4. Fork-test status

No notebook exists yet, so nothing has been tested. Each notebook passes only when this is done:

1. One colleague forks it once from their own account and runs all cells. Never spread this across the team, because forks count as votes.
2. For a standalone notebook, a pinned `pip install quillsort==X.Y.Z` with internet on is fine. For a code competition, install offline from an attached wheels dataset. A pure CPU wheel avoids CUDA headaches.
3. No API key is needed, so no Secrets step.
4. It runs on CPU well under the session cap. State "CPU" in the first cell.
5. Pin the package version.

## 5. Eight-week cadence

All rows are owned by you. The colleague only does the fork test.

| Week | Hours | Work |
|---|---|---|
| 1 | 6 | Contributor steps and organization request (2 h). Pick 2–3 active tabular competitions and read their rules (1 h). Post 2 full forum answers, no links (3 h). |
| 2 | 6 | 3 forum answers (2.5 h). Choose the public dataset and task, and run Quillsort against the strongest baseline you'd really use (3.5 h). |
| 3 | 6 | Publish notebook #1 (3.5 h). Colleague fork test, one fork (0.5 h of their time). 2–3 forum answers (2 h). |
| 4 | 6 | Answer notebook comments within 2 days. Build the wheels dataset under the organization, with every usability field filled (3 h). 2 forum answers (2 h). First monthly metrics read (1 h). |
| 5 | 6 | If an active competition fits and notebook #1 passed its fork test: starter notebook in the competition's Code tab, full method, no vote request (4 h). Forum answers (2 h). |
| 6 | 6 | Notebook #2 on a different task (4 h). Comments and forum answers (2 h). |
| 7 | 6 | One Accomplishments post: what readers asked for, what changed, no medals, no vote request (1.5 h). Dataset or notebook update with a changelog cell (2.5 h). Forum answers (2 h). |
| 8 | 6 | Metrics read, then drop topics that drew nothing (2 h). Forum answers (2 h). Plan the next 2 months (2 h). |

Rules that apply all through:
- Each forum answer is complete without a link. If it uses Quillsort, say "(I work on Quillsort)" after naming it.
- Never post your own link outside Accomplishments **[platform]**.
- Never rerun a notebook for position **[platform]**.
- Never fork a notebook and add one cell **[platform]**.
- Check every AI-drafted answer by running its code first **[platform]**.

## 6. Competition plan

You won't host or sponsor. The only competition action is the week-5 starter notebook. Before posting it:
- Read the rules and check the data format.
- Confirm Quillsort is free and equally accessible. MIT and free passes the Reasonableness Standard **[platform, rules]**.
- If it's a code competition, install from the wheels dataset.
- Any code you share publicly in a competition is deemed OSI-licensed **[platform, rules]**.

Playground-style monthly tabular competitions are likely a good place for early answers and a starter. They typically award no medals **[platform]**, so expect newcomers rather than Grandmasters. I haven't confirmed which competitions are open, so check that live.

## 7. Templates, filled

**Notebook first cell**

```markdown
# {Task in plain words}: Quillsort on {dataset}

**Runs with internet off** on CPU, about {N} minutes.
Quillsort {version} installs from the attached `quillsort-wheels` dataset.

I work on Quillsort. The last section compares it with {strongest baseline}
and says where the baseline wins.
```

**Notebook last cell**

```markdown
## What to try next

- Swap `{parameter}` to see {effect}.
- Quillsort docs for {feature}: {link with tracking tag}
```

**Forum answer shape**: answer the question in full, with code and the numbers you measured. No link, no teaser, no vote request.

**Accomplishments post**

```text
Title: {notebook or dataset name} - what we learned from your comments

Three things readers asked for, what changed in v{N}, and what we
plan next. Link: {url}
```

**Dataset description** (wheels dataset)

```markdown
## About
Prebuilt CPU wheels of Quillsort {version} for offline notebooks.

## Files and columns
- `quillsort-{version}-*.whl` - {platform tag}.

## Licence
MIT.

## Starter notebook
{link to the notebook that installs from it}
```

## 8. Metrics

Targets are self-set, because Kaggle publishes no vendor benchmark.

- **Forks and copy-and-edit counts from outside accounts, dataset downloads.** Votes are only a secondary signal.
- **Signups from the tagged link in the closing cell.** Also competition notebooks that import `quillsort`, and `kagglehub` downloads if your docs pull the dataset.
- **Hygiene, pass threshold zero.** Removed posts, staff warnings, plagiarism reports, medal retractions.
- Review monthly, at the end of weeks 4 and 8.

## Questions that would change this plan

1. Who besides you can answer forum questions within a day?
2. Is there a benchmark showing where Quillsort beats or loses to CPU-run baselines? If not, week 2 builds one.
3. Does anyone on the team already hold an Expert-or-above Kaggle account?