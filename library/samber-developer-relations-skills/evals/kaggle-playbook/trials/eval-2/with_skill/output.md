# Tracewell on Kaggle: the notebook and forum post as asked won't work

I read `kaggle-playbook` and its `limits.md` and `templates.md`. Both items as you described them would fail or get removed, so below is what to publish instead.

## Fit verdict: skip the competition surfaces

Your product is hosted-only, needs an API key, and the trial expires after 14 days. The skill's test is whether a stranger can fork the notebook and run your product with internet off.

| Your plan | Problem |
|---|---|
| Starter notebook in the competition's Code tab | **Code competitions run submissions with internet off [platform, per rules].** Tracewell logging can't run in a submission, so the notebook only works as an internet-on exploration notebook. The skill says "no competition starter notebooks for code competitions" for hosted APIs. |
| `os.environ['TRACEWELL_API_KEY'] = 'tw-xxxx'  # replace with yours` | A placeholder key breaks every fork. Secrets don't follow forks [platform], and a broken fork costs you the comments section. |
| Forum post saying Tracewell gives you an edge | **Linking or promoting your own work in a competition forum is spam and gets deleted [platform].** The post would also claim an edge you haven't measured. |
| Logging every prompt to a paid SaaS | **Tools must be free and equally accessible, or pass the Reasonableness Standard [platform, competition rules].** A trial that expires mid-competition invites a ruling against it, and the host decides, not you. |
| Logging competition prompts to a third-party service | Competition data often can't leave Kaggle. **I haven't read this competition's rules.** Check its data-use section before anything leaves the notebook [unconfirmed]. |

Two more checks:

- **Public code is OSI-licensed.** Code shared publicly during a competition is deemed licensed under an OSI license that allows commercial use [platform, competition rules].
- **Votes and forks.** Colleague forks and votes count as manipulation. Use one colleague for the fork test, never the team.

## What I'd ship instead

The default rung from the skill is forum answers from week 1 and one standalone notebook from week 3, run in parallel.

1. **Forum answers.** Substantive answers in this competition's forum, with no links and no claim about Tracewell.
2. **Standalone notebook.** A notebook on a public LLM-ranking dataset (not attached to the competition), internet on, key from Kaggle Secrets. Do this only if Tracewell can give notebook users a key that doesn't expire in 14 days. If it can't, skip even this.
3. **Competition starter notebook.** Only if a future competition has internet on, or a Tracewell local mode exists that runs offline.

## Notebook outline: standalone, internet on

Title (names the task, not the product): **"Tracing and comparing LLM answer rankers on {public dataset}"**. Tags and subtitle name Tracewell.

1. **Cell 1 (markdown):** the standard first cell.
   ```markdown
   # Comparing LLM answer rankers on {dataset}: {method}

   **Needs internet on and one secret.** Runs on {CPU | GPU T4 x2}, about {N} minutes.
   Add-ons > Secrets > add `TRACEWELL_API_KEY` with a free key from {signup page},
   then tick it for this notebook. Forks do not inherit secrets,
   and secrets need internet on, so this notebook cannot run in code competitions.

   I work on Tracewell. The last section compares it with {plain baseline: logging to a local JSONL file}
   and says where the baseline wins.
   ```
2. **Cell 2: pinned install and key check.** Pin `tracewell=={version}`. Fail clearly if the secret is missing.
   ```python
   from kaggle_secrets import UserSecretsClient
   key = UserSecretsClient().get_secret("TRACEWELL_API_KEY")  # raises if label not added
   ```
3. **Cell 3: load the public dataset** and show 5 rows.
4. **Cells 4-6: ranking baseline.** A prompt template, a pairwise or listwise ranker, and a CV score computed with no Tracewell code.
5. **Cells 7-8: add tracing.** Wrap the ranker calls with `{Tracewell call}` and log prompt, response and latency. Show one screenshot or table of what you can then see (for example, the slowest 10 prompts, or disagreements between rankers).
6. **Cell 9: what the tracing found**, with real numbers from your own run. Don't write "edge" unless a score moved.
7. **Cell 10: baseline comparison.** Local JSONL logging against Tracewell, including where the baseline wins (no key, offline, free).
8. **Last cell: what to try next.**
   ```markdown
   ## What to try next

   - Swap `{parameter}` to see {effect}.
   - Tracewell docs for {feature}: {link with tracking tag}
   ```

Notes on the outline:

- Put exactly one "About Tracewell" cell at the end, never a banner on top.
- Fit the runtime under the session cap and state the accelerator in cell 1.
- Fork test: one colleague forks it from their own account and runs all cells. That fork counts as a vote, so one person only.
- A named staff member posts it, with the dataset under your organization profile.
- Each poster reaches Contributor in week 1: complete profile, verified phone, one notebook run, one competition submission, one comment, one vote.
- Announce the notebook only in the Accomplishments forum, never in the competition forum.

## Forum post: earn-first, no product pitch

The post answers a real question in this competition in full. There's no link and no vote request. If the answer uses Tracewell, add "(I work on Tracewell)" after naming it, which is the skill's disclosure rule. Fill the `{fields}` from your own runs, and have the poster run the code first. The text below is a shape, not a claim.

```text
Title: {Specific question the thread asks, answered}

{Direct answer in the first sentence.}

What I saw: {CV vs LB gap, length-bias in the judge prompts, position bias in
pairwise ranking, ...}. What fixed it for me: {change}. CV {a} -> LB {b}
on {n} seeds.

Code:
{minimal runnable snippet, competition-legal, no external services}

Caveat: {where it didn't help}.
```

Tracewell belongs in a post only where it was the tool that exposed the problem, as one phrase such as "found it by logging every prompt (I work on Tracewell)". Even then, the fix has to stand alone without the product.

Do not post this:

```text
// ✗ Bad - teaser plus own-work link and a vote request
Tracewell gives you an edge in this competition, link here, an upvote would help!
```

## Cadence, with owners to fill

| Weeks | Action | Hours/week |
|---|---|---|
| 1-4 | Each poster answers 2-3 forum questions a week, in full, no links. Request the organization profile. | 2-3 |
| 3 | Standalone notebook published after the fork test. | 6-8 once |
| 4-8 | One notebook or dataset every two weeks. Answer every comment within two days. | 2-3 |
| Monthly | Read forks, copies and comments per notebook. Drop topics that drew none. | 1 |

Hours are my estimates. The skill defines the cadence but not the hours.

## Measure

- Forks and copy-and-edit counts from accounts outside Tracewell, which also count as votes.
- Signups from a tagged link in the closing cell, and notebooks that import the package.
- Hygiene, pass threshold zero: removed posts, staff warnings, plagiarism reports, medal retractions.

## Open questions

1. Can a notebook user get a Tracewell key that doesn't expire after 14 days? This decides whether the standalone notebook is worth building.
2. Does this competition's data-use rule allow sending prompts to an external service?
3. Who posts: named staff, and any with Kaggle history at Contributor or above?
4. How many hours per week, and who can answer forum questions within a day?
5. Does Tracewell have a local or offline mode? That would reopen the competition starter notebook.

My answers to 1 and 5 would move the notebook rows up or down the ranking. Kaggle limits and rules change, and its pages render client-side, so confirm any number above in a real browser before quoting it.