Using the oss-launch skill's Step 3 (positioning) and the credibility codes in `references/announcement-examples.md`, checked against the HN norms in `references/channel-playbook.md`. All three pieces read as marketing copy an HN audience will discredit on sight — here's the weak/strong diff on each, then a direct answer on the benchmark.

## One-liner

**Weak:** "Basalt: the revolutionary, blazing-fast data platform that reimagines how modern teams move data."
Three superlatives (revolutionary, blazing-fast, reimagines), no category, no audience, no concrete capability. HN moderators rewrite titles like this; readers file it as an ad before evaluating it.

**Strong shape:** `Basalt is an open-source ETL runtime for data engineering teams that <capability Airflow lacks>.`

I won't fill that last clause with an invented technical claim — pick whichever is literally true of Basalt, don't approximate:

- "...run pipelines as plain code, without standing up a scheduler + webserver + worker + metadata-DB cluster." (only if deployment really is simpler)
- "...get sub-second pipeline start with no DAG-parsing warm-up." (only if that's measured, not felt)

Whichever you use, it must be something Airflow specifically can't claim — that's the whole job of the sentence.

## Comparison table

**Weak (yours):** every row is yes/Basalt, no/Airflow. Per the skill: "every row favors you, so a reader stops believing the whole page." This is the textbook example of the pattern that gets a launch discredited in the first reply.

**Strong shape** — real dimensions, real numbers, and at least one row you lose:

| | Basalt | Airflow |
|---|---|---|
| Deployment model | [single binary / describe honestly] | Scheduler + webserver + worker + metadata DB |
| Time to first pipeline | [measured minutes, real number] | [real number, not a guess] |
| [Your actual measured perf axis] | [number, link to method] | [number] |
| Ecosystem / integrations | [real count] | 90+ provider packages, 10 years of operators |
| Best when | [your real sweet spot] | Teams already invested in Airflow's operator ecosystem |

Concede ecosystem/maturity to Airflow explicitly — you will lose that row no matter what you write, and losing it openly is what buys credibility for the rows you actually win.

## HN first comment

**Weak (yours):** "incredibly excited... game-changer... 10x faster... love your feedback and support!" — this is close to a word-for-word match of the skill's own documented Weak example. No named author, no technical hook, no disclosed limitation, unsourced "10x faster" stacked on top of the table's inflated claims.

**Strong shape**, following the four things the reference calls out (who's speaking, a technical hook, disclosed limits, a specific invitation), plus the commercial disclosure this launch needs since a company sells a managed version:

> I'm [name], and I built Basalt after [the real problem you hit — what specifically broke or was painful about running pipelines on Airflow]. [One concrete technical decision and its tradeoff — e.g. "it trades X for Y; the method's in `bench/README.md` so it can be argued with"].
>
> It doesn't do [real missing feature] yet, and [real rough edge — untested platform, breaking API, whatever is actually true].
>
> Basalt is built and maintained by [Company]. The core is [license] and stays that way; we sell a hosted version. Nothing in this repo is time-limited or crippled — if it stops being useful without the paid product, that's a bug, tell us.
>
> Happy to go deep on [specific technical area].

Drop "10x faster" entirely unless you can point at a public method — see below.

## The 6x benchmark: don't lead with it

No, for three reasons, all directly from Step 3's rule ("give benchmarks a method and a reproduction command, or drop the numbers"):

1. **"Internal workload" isn't a method.** The first HN reply to any performance claim is "what workload, what's the repro?" With no answer, that reply becomes the top comment and the launch is now defending a number instead of showing the project.
2. **It stacks on an already-inflated page.** A one-liner with three superlatives, a table with zero losing rows, and an unsourced "10x faster" already primes readers to distrust the next number. A second unverifiable claim (6x) compounds that instead of adding credibility.
3. **Single-competitor, single-workload numbers read as cherry-picked** even when they're honest — there's no way for a stranger to tell the difference without the method.

What to do instead: publish the benchmark method and a reproduction command in the repo (a `bench/` directory, per the skill's own worked example), then reference it as supporting evidence inside the README or the first comment — never in the one-liner or as the launch's headline claim. If the method can't be made public and reproducible before launch day, drop the number for this launch entirely and let the concrete capability claim carry the one-liner instead. A number nobody can rerun is a liability, not an asset, on this specific audience.