## Before the rewrite: check the co-founder's theory

Your numbers don't clearly support "the README is the problem." 34 unique visitors over 14 days on a repo that's been live 5 months is thin traffic — averaging ~2.4 visitors/day. The clone-to-visitor ratio (3/34 ≈ 8.8%) sits in the ambiguous middle this skill's heuristic can't rule on by itself.

⚠️ Two different diagnoses produce the same "flat" symptom:
- **Conversion problem** (README's fault): decent traffic arrives, reads, leaves unconvinced.
- **Distribution problem** (not README's fault): almost nobody is arriving in the first place, so there's nothing for the README to convert.

At ~2-3 visitors/day, this looks closer to the second case. Before you spend the week: open Insights → Traffic → **referring sites**. If traffic is near-zero and undifferentiated (mostly `github.com` itself, no PyPI, no external referrers), that's a distribution problem — a README rewrite won't move it, and the week is better spent on PyPI presence, a Show HN/relevant-subreddit post, or getting `parqueue` linked from something people already search for.

That said: the fixes below are worth doing regardless of which diagnosis is right — a weak README caps conversion even once distribution improves, and most of this is under an hour of work. I'd frame it to your co-founder as "doing both, in this order" rather than "the README explains it."

## Access limitation — this affects what I can hand you

I don't have access to the actual `northgate-io/parqueue` source in this session (no local clone, no network reach to GitHub from here). That blocks two mandatory checks this skill treats as non-negotiable:

- **A2 (install runs)** — I can't run `pip install parqueue` and the first usage example from clean and confirm they work.
- **A3 (every claim verifiable)** — I can't check any flag, default, or method name against your actual argument parser / class definitions.

So below is a complete rewrite with the structure, positioning, and prose finished — but the install command, the exact API in the usage example, the license, and the status line are marked `[CONFIRM]` rather than invented. Writing a plausible-looking `Batcher(...)` API I made up would fail this skill's core rule (a claim in a README the source doesn't back is a hallucination, not a typo) and would be actively worse than what you have now if it's wrong. Fill those four spots, run the install/usage block from a clean venv once, and this is ready to ship.

Assumptions I made without the full interview (correct me if wrong): audience = Python developers doing data/ETL work, evaluating this as a dependency, deciding mostly alone (no enterprise trust-signal section added); project type = library.

## Positioning — pick one

1. **Mechanical**: "parqueue batches in-memory records and flushes them to Parquet files in Python."
2. **Problem removed** (recommended): "parqueue is the buffering-and-flush logic you'd otherwise hand-roll around `pyarrow.parquet.ParquetWriter` — accumulate records, flush on a threshold, avoid either a thousand tiny files or one giant in-memory table."
3. **What it replaces**: "Stop writing your own row-buffer wrapper every time a pipeline needs to stream into Parquet — parqueue is that wrapper, written once."

I'd go with #2: it names a real, recognizable API (`ParquetWriter`) so a reader instantly knows the alternative you're positioned against, and it states a concrete failure mode (tiny-files vs. giant-in-memory-table) instead of an adjective. Swap it if your actual differentiation is something else — e.g. if the real pitch is async/streaming support, or schema-drift handling, use that instead; I don't know your internals well enough to guess past this.

## The rewrite

```markdown
# parqueue

parqueue is the buffering-and-flush logic you'd otherwise hand-roll around
`pyarrow.parquet.ParquetWriter`: accumulate records in memory and flush them
to Parquet on your own threshold — row count, byte size, or time — instead of
producing one file per row or holding an unbounded table in memory.

[CONFIRM status line — pick the true one]
Early since shipping five months ago. Core write path is stable; [name what
isn't]. We run it ourselves in [where], and we'd rather you find the rough
edges than we find them for you.

## Install

Requires Python [CONFIRM minimum version].

\```bash
pip install parqueue
\```

Verify:

\```bash
python -c "import parqueue; print(parqueue.__version__)"
# [CONFIRM real output]
\```

## Usage

[CONFIRM — replace with a real, run-from-clean example. Shape to fill in:
construct the writer/batcher with a schema and a flush threshold, call the
per-record write method in a loop, show what happens on close/flush, and show
real output (e.g. resulting file(s) and row counts). Keep this to one
scenario — a log-ingestion loop or similar — not a signature list.]

\```python
# real minimal example goes here, tested against a clean install
\```

This example lives at [`examples/basic.py`](./examples/basic.py) and runs
with `python examples/basic.py`. [CONFIRM the file exists, or drop the line.]

## Why parqueue instead of the alternative

- vs. calling `pandas.DataFrame.to_parquet()` per batch: [CONFIRM concrete
  difference — e.g. no need to materialize the whole batch as a DataFrame
  first, no repeated schema inference per call]
- vs. raw `pyarrow.parquet.ParquetWriter`: [CONFIRM — e.g. threshold-based
  flush and row-group sizing handled for you, safe close on exit/exception]
- vs. `fastparquet`: [CONFIRM a real axis, or delete this row entirely if
  it's not a comparison your users actually make]

## What it doesn't do

[CONFIRM — name the real gap: no compaction of existing files, no schema
evolution across flushes, no distributed/multi-writer coordination, whatever
is actually true. This line costs one sentence and is the highest-trust
sentence on the page — don't skip it to look more complete.]

## Links

- [Full documentation](CONFIRM URL, or delete this row)
- [Changelog](./CHANGELOG.md)

## License

[CONFIRM — name it, link to the LICENSE file. Do not leave this section out;
license was the single highest-rated factor in GitHub's own 2017 Open Source
Survey for whether developers choose to use a project.]
```

## Badges

Cap at 4, all assessment signals (backed by a check, not a claim):
- PyPI version
- License
- Supported Python versions
- Last commit / maintenance status (or CI status if you run one)

Drop anything like "PRs welcome" — it signals nothing a reader can verify, and the evidence (Trockman et al., ICSE 2018) shows badge rows don't move adoption and can correlate with less of it once you're past a handful.

## What's left for you to close

1. Fill the four `[CONFIRM]` blocks from the real source — install command, one runnable usage example (test it from a clean venv), differentiation specifics, license, status.
2. Check referring-sites data in Insights before concluding this was ever a README problem.
3. Re-measure clones/visitors over the next full 14-day window after both the README ships and whatever distribution fix you pick — a single before/after on the README alone won't isolate which one moved the number.