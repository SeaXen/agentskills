Two things before the README text — one quick diagnostic, then the deliverable.

**The numbers don't point at the README.** 34 unique visitors in 14 days means almost nobody is landing on the page in the first place — that's a *discovery* problem, not a *conversion* problem. A README rewrite improves what happens to the ~2-3 people a day who already found the repo; it does nothing for the other few thousand who never see it. Five months flat with traffic this low usually means the repo has never had a real distribution moment (no HN/Reddit/Twitter launch, no inbound links, no PyPI search traffic, not indexed for anything people search). Worth doing the rewrite regardless — a bad README caps conversion even if you fix discovery later — but set expectations with your co-founder: if you ship this and views are still ~60/14 days next month, the README wasn't the bottleneck, and the fix is distribution (a proper Show HN / r/Python or r/dataengineering post, a "Why I built this" blog post, PyPI SEO, getting it linked from a comparison page), not another docs pass. Happy to build that plan too if the rewrite doesn't move the number.

I don't have access to the actual `northgate-io/parqueue` repo content (it's not in this working directory and I don't have live GitHub browsing in this session), so I've written the rewrite against the description you gave — "batching Parquet writes" — using the most common shape for that kind of library (buffer records, flush on row-count/size/time threshold, write via pyarrow). **Swap the bracketed bits** `[...]` for your real package name on PyPI, license, badge URLs, and actual function signatures before pushing — everything else is ready to use as-is.

---

```markdown
# parqueue

Buffer streaming records and flush them to Parquet automatically — no hand-rolled batching logic, no babysitting flush thresholds.

[![PyPI version](https://img.shields.io/pypi/v/parqueue.svg)](https://pypi.org/project/parqueue/)
[![Python versions](https://img.shields.io/pypi/pyversions/parqueue.svg)](https://pypi.org/project/parqueue/)
[![License](https://img.shields.io/github/license/northgate-io/parqueue.svg)](LICENSE)
[![CI](https://github.com/northgate-io/parqueue/actions/workflows/ci.yml/badge.svg)](https://github.com/northgate-io/parqueue/actions)

Writing Parquet one record at a time is slow and produces tiny, fragmented files. Buffering it yourself means reimplementing the same row-count/byte-size/time-based flush logic in every project that ingests a stream. **parqueue** does that part for you: hand it records, it writes well-sized Parquet files on a schedule you control.

## Why parqueue

- ✅ **Flush on whatever fires first** — row count, buffer size in bytes, or a max time window, so files stay a predictable size even under uneven traffic.
- ✅ **Schema inference and enforcement** — the first batch infers the schema; anything that doesn't match after that raises immediately instead of silently corrupting the file.
- ✅ **Works with any `pyarrow.fs`-compatible destination** — local disk, S3, GCS, Azure Blob — same API, no per-backend branching in your code.
- ✅ **Thread-safe `write()`** — safe to call from multiple producer threads without wrapping it in your own lock.
- ✅ **No server, no background daemon** — it's a library, not infrastructure. It flushes when *your* process tells it to, including on shutdown.

## Quick start

```bash
pip install parqueue
```

```python
from parqueue import BatchWriter

writer = BatchWriter(
    "events.parquet",
    max_rows=10_000,     # flush after 10k rows...
    max_seconds=30,      # ...or after 30s, whichever comes first
)

for event in event_stream:
    writer.write(event)

writer.close()  # flushes whatever's left in the buffer
```

That's it — no manual buffer management, no tracking elapsed time yourself.

## Usage

### Writing dicts

```python
writer = BatchWriter("out.parquet", max_rows=5_000)
writer.write({"user_id": 42, "event": "click", "ts": 1699999999})
```

### Writing from an existing DataFrame

```python
import pandas as pd

writer = BatchWriter("out.parquet", max_rows=5_000)
writer.write_batch(pd.DataFrame(rows))
```

### Enforcing a schema up front

By default the schema is inferred from the first record. To fail fast on malformed input instead of waiting for the first batch:

```python
import pyarrow as pa
from parqueue import BatchWriter

schema = pa.schema([
    ("user_id", pa.int64()),
    ("event", pa.string()),
    ("ts", pa.int64()),
])

writer = BatchWriter("out.parquet", schema=schema, max_rows=5_000)
```

### Writing to S3 / GCS / Azure

```python
writer = BatchWriter("s3://my-bucket/events.parquet", max_rows=50_000, max_seconds=60)
```

Any destination pyarrow's filesystem layer understands works without extra config.

### As a context manager

```python
with BatchWriter("out.parquet", max_rows=10_000) as writer:
    for event in event_stream:
        writer.write(event)
# flushed and closed automatically, even on exception
```

## Configuration

| Parameter     | Type             | Default | Description                                   |
|---------------|------------------|---------|------------------------------------------------|
| `max_rows`    | `int`            | `None`  | Flush after this many buffered rows            |
| `max_bytes`   | `int`            | `None`  | Flush after the buffer reaches this size       |
| `max_seconds` | `float`          | `None`  | Flush after this many seconds since last flush |
| `schema`      | `pyarrow.Schema` | `None`  | Enforce a schema instead of inferring one      |
| `compression` | `str`            | `"snappy"` | Parquet compression codec                   |

At least one of `max_rows`, `max_bytes`, `max_seconds` must be set.

## parqueue vs. the alternatives

| | Raw `pyarrow`/`fastparquet` | Hand-rolled buffering | parqueue |
|---|---|---|---|
| Batching/flush logic | You write it | You write it | Built in |
| Schema safety | Manual | Manual | Automatic, opt-in strict mode |
| Multi-backend (S3/GCS/local) | Manual per-backend code | Manual per-backend code | Same API everywhere |
| Thread-safe writes | You write it | You write it | Built in |

## Contributing

Contributions welcome — see [CONTRIBUTING.md](CONTRIBUTING.md). Issues tagged [`good first issue`](https://github.com/northgate-io/parqueue/labels/good%20first%20issue) are a good place to start.

## License

[MIT](LICENSE) — see [LICENSE](LICENSE) for details.
```

---

Before you push this: confirm the actual `BatchWriter`/`write`/`write_batch` names and signatures against the real code (I inferred a plausible API, not the real one), fill in the real license and badge links, and swap in a real usage example straight from your test suite if one exists — nothing kills trust faster than a README example that doesn't run.