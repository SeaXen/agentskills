# Kaggle plan for "Semantic search with Vectorpine"

**I haven't written the General-forum post, the competition-thread comments, or the "would love an upvote" text.** Each of the four pieces of this week's plan is on the Kaggle playbook's list of things that get content removed or accounts banned. Replacements for all four are below.

## What to cancel, and why

| Planned | Rule broken | What happens |
|---|---|---|
| Post the link in General | Linking your own work outside the Accomplishments forum is spam **[platform]** | Deleted, and it marks Vectorpine as a promoter |
| Link plus "upvote if this helps!" in 3 competition threads | Vote requests in competition forums are reportable **[platform staff]**. Own-work links are spam too. | Deleted, and likely reported in three active communities at once |
| 9 engineers upvote to reach gold | Coordinated voting is progression manipulation **[platform]**. Kaggle can retract medals, make content ineligible, or suspend accounts. | A vote cluster from one company is what the ban waves target **[practitioner, unconfirmed by staff]**. Forks now count as votes **[platform staff]**, so forking also counts. |
| Rerun every morning | Re-running to climb Hotness is "Abuse of Hotness Algorithm" **[platform]** | Reportable |

The upvote plan also wouldn't reach gold even if it were allowed:

- Gold needs 50 counted votes. Votes from Novices, self-votes, and repeat votes from the same people don't count toward medals.
- Most of your engineers made their accounts this week, so they are Novices.
- Asking for votes on Slack, X or email breaks the same guideline.

## Fit verdict: invest

The embedded in-process mode is what makes this work. A stranger can fork a notebook and run Vectorpine with internet off. Without an embedded mode, you'd be limited to notebooks and datasets only.

## Interview answers

I couldn't ask these, so I assumed the answers. Tell me if any is wrong.

1. **Product:** runs inside a Python notebook, in embedded mode. This keeps the competition starter notebook ranked second, behind forum answers.
2. **Who posts:** named engineers on their own accounts, mostly Novices. This moves forum answers to the front, because they build the standing a starter notebook needs.
3. **Goal:** adoption by practitioners, no hard launch date. This favours compounding surfaces (forum answers, standalone notebooks) over one-shot ones.
4. **Hours:** assumed about 6 hours a week across the team, with two engineers answering forum questions within a day.

## Ranked surfaces for Vectorpine

1. **Full answers in active competition forums, no links.** Compounding, and the best value per hour.
2. **Your standalone notebook.** It's already published, which is the right surface.
3. **A dataset you own, plus a notebook.** Do this once the notebook passes the fork test.
4. **Starter notebook attached to a competition.** Week 5 at the earliest, and only if a competition really fits.
5. **Organization profile.** Request it now.
6. **Accomplishments post.** The one place you may link your own work.

## Fork-test result: not yet run

The test: a stranger forks the notebook and runs all cells.

1. **One colleague forks it once**, from their own account, and runs every cell. One fork only; it counts as a vote, so don't spread the test across the team.
2. **Pin the Vectorpine version** with `pip install`. If the notebook is meant for code competitions, install offline from an attached dataset of wheels instead.
3. **Check it needs no API key.** Embedded mode shouldn't.
4. **State the accelerator in the first cell.**
5. **Pin or freeze the Kaggle environment.**

## Rewritten week-one plan

**Day 1: cancel and clean up (one person, about 1 hour)**
- If any link or vote request has already gone out, delete it yourself. Never repost it reworded.
- Stop the daily reruns.
- Tell the 9 engineers not to vote on or fork the notebook. Their organic interest is fine, but coordinated staff votes and forks count as collusion.

**Day 1-2: fix the notebook (one engineer, about 3 hours)**
- Replace the first cell with the template below.
- Put the title on the task, not the product, for example "Hybrid search over {dataset}".
- Move the Vectorpine pitch to one "About Vectorpine" cell at the end.
- Fill in the tags and subtitle. Name the product there.
- Run the fork test.

**Week 1-4: earn first (each poster 2-3 answers a week)**
- Each engineer completes their profile, verifies their phone, runs one notebook, makes one submission, writes one comment and casts one vote. That makes them a Contributor and makes their votes count.
- Each engineer answers real questions in competitions where vector search or embeddings help, in full and with no links.
- Request the organization profile now.

**Week 3 onward:** one new notebook or dataset every two weeks. Answer every comment on your notebooks within two days.

**Week 5 at the earliest:** a competition starter notebook, only if one fits and the notebook passes the fork test.

## Filled templates

### Notebook first cell

```markdown
# Semantic search: hybrid retrieval on {dataset}

**Runs with internet off** on CPU, about {N} minutes.
Vectorpine {version} installs from the attached `{wheel-dataset-slug}`.

I work on Vectorpine. The last section compares it with a plain
NumPy cosine-similarity baseline and says where the baseline wins.
```

### Notebook last cell

```markdown
## What to try next

- Swap `{parameter}` to see {effect on recall or latency}.
- Vectorpine docs for embedded mode: {link with tracking tag}
```

### Competition forum answer (earn-first)

This is the shape of an answer. It needs a real question, so I can't write the content until you pick the competitions.

```text
{Direct answer to the poster's actual question, with the reasoning.}

Code:
{runnable snippet}

Result on my split: {metric before} -> {metric after}.
(I work on Vectorpine; the snippet uses its embedded mode, but the
same approach works with any ANN index.)
```

Rules for these answers:
- No links to your own work and no vote requests.
- Run the code before posting it.
- If an AI drafted it, a human checks it first.
- Disclose the affiliation only where the answer uses the product.

### Accomplishments post

This is the only place to link the notebook. I'd hold it until week 4 or later, when you have forks and comments to report. Four upvotes is too thin, and low-content posts get downvoted.

```text
Title: Semantic search with Vectorpine - what we learned

Three things readers asked for in the comments, what we changed in v2,
and the next dataset we plan. Link: {url}
```

There is no vote request in it.

## Metrics

Kaggle publishes no vendor benchmark, so set your own targets.

- **Primary:** forks and copy-and-edits from accounts outside the company, and dataset downloads.
- **Secondary:** votes.
- **Conversion:** signups from the tagged link in the closing cell, and competition notebooks that import Vectorpine.
- **Hygiene, pass threshold zero:** removed posts, staff warnings, plagiarism reports, medal retractions.

The playbook says the rankings reward recent votes from readers past Novice tier. You get those from forum answers and a notebook that runs when forked, not from organised voting.

I can draft real forum answers once you tell me which three competitions you'd target.