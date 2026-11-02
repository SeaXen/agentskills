Here's the trimmed README, plus where the cut material goes. GitHub auto-detects `CONTRIBUTING.md`, `CODE_OF_CONDUCT.md`, `SECURITY.md`, and `LICENSE` at repo root and surfaces them in its own UI (community tab, new-issue template picker, "Report a vulnerability" button) — so moving content into them isn't a loss of visibility, it's the idiomatic location Java/GitHub tooling already expects.

## New `README.md` (~90 lines, from 1,400)

```markdown
<div align="center">
  <img src="docs/logo.svg" alt="Parsely" width="160">
  <h1>Parsely</h1>
  <p><strong>A fast, streaming CSV library for Java — parse and write gigabyte-scale files with constant memory.</strong></p>

  [![CI](https://github.com/quillmark/parsely/workflows/CI/badge.svg)](https://github.com/quillmark/parsely/actions)
  [![Maven Central](https://img.shields.io/maven-central/v/dev.quillmark/parsely.svg)](https://central.sonatype.com/artifact/dev.quillmark/parsely)
  [![Javadoc](https://javadoc.io/badge2/dev.quillmark/parsely/javadoc.svg)](https://javadoc.io/doc/dev.quillmark/parsely)
  [![License](https://img.shields.io/github/license/quillmark/parsely.svg)](LICENSE)

  [Documentation](https://parsely.quillmark.dev) • [Javadoc](https://javadoc.io/doc/dev.quillmark/parsely) • [Changelog](CHANGELOG.md)
</div>

---

## Why Parsely?

- **Streaming, not in-memory** — read and write rows one at a time; a 10 GB file uses the same heap as a 10 KB one.
- **Zero-copy parsing** — avoids intermediate `String` allocation on the hot path.
- **RFC 4180 compliant**, with configurable delimiter, quoting, and escaping for real-world dialects.
- **No reflection, no annotations required** — plain `Iterator<CsvRecord>` API.

## Installation

**Maven**
```xml
<dependency>
  <groupId>dev.quillmark</groupId>
  <artifactId>parsely</artifactId>
  <version>3.4.0</version>
</dependency>
```

**Gradle**
```groovy
implementation 'dev.quillmark:parsely:3.4.0'
```

## Quick Start

```java
try (CsvReader reader = CsvReader.open(Path.of("data.csv"))) {
    for (CsvRecord record : reader) {
        String name = record.get("name");
        int age = record.getInt("age");
        System.out.printf("%s is %d%n", name, age);
    }
}
```

Writing follows the same streaming shape:

```java
try (CsvWriter writer = CsvWriter.open(Path.of("out.csv"))) {
    writer.writeHeader("name", "age");
    writer.writeRow("Ada Lovelace", 36);
}
```

More examples: [`/examples`](examples) · full walkthrough: [Getting Started](https://parsely.quillmark.dev/getting-started).

## Documentation

This README covers installation and a first read/write loop only. Everything else lives on the docs site, versioned per release:

- [API Reference](https://parsely.quillmark.dev/api) (Javadoc: [javadoc.io](https://javadoc.io/doc/dev.quillmark/parsely))
- [Configuration Reference](https://parsely.quillmark.dev/configuration) — every `CsvReaderOptions` / `CsvWriterOptions` field
- [Guides](https://parsely.quillmark.dev/guides) — dialects, encodings, backpressure, Reactive Streams adapter

## Contributing

Bug reports and PRs welcome. See [CONTRIBUTING.md](CONTRIBUTING.md) for dev-environment setup, build commands, and the PR checklist.

## Community

Governed by our [Code of Conduct](CODE_OF_CONDUCT.md) (Contributor Covenant).

## Security

Found a vulnerability? See [SECURITY.md](SECURITY.md) to report it privately — please don't open a public issue.

## Changelog

See [CHANGELOG.md](CHANGELOG.md) for release history since 2021.

## Credits

Built and maintained by the [Quillmark](https://github.com/quillmark) team and [contributors](https://github.com/quillmark/parsely/graphs/contributors).

## License

[Apache 2.0](LICENSE)
```

## Where the rest goes

| Old section | New home | Why |
|---|---|---|
| Table of Contents (22 hand-written entries) | Deleted | GitHub renders an auto-outline (⋮≡ button, top-left of any rendered `.md`) from headings — a hand-maintained TOC is redundant and drifts. |
| Full API Reference (61 methods) | Javadoc (`javadoc.io`) + `docs/api.md` on the docs site | Java already has a canonical, generated, always-in-sync place for this — a README can't keep 61 signatures current across releases. |
| Configuration table (40 rows) | `docs/configuration.md` | Same reasoning — one table cell edit shouldn't require touching the landing page. |
| Contributing (80 lines) | `CONTRIBUTING.md` at repo root | GitHub auto-links it into the PR template and "Contribute" panel; no need to inline it. |
| Code of Conduct (full Covenant text) | `CODE_OF_CONDUCT.md` at repo root | GitHub surfaces this in the repo's Community tab automatically once the file exists at that path. |
| Security policy | `SECURITY.md` at repo root | Enables GitHub's native "Report a vulnerability" button. |
| Changelog (all releases since 2021) | `CHANGELOG.md`, or defer entirely to GitHub Releases | Releases page already timestamps and links each version; no need to duplicate it in prose. |
| Credits | One line linking `graphs/contributors` | Auto-updates itself; a manual list goes stale the day after someone new merges a PR. |

Net effect: the file a visitor lands on shrinks from 1,400 lines to ~90, covers only "what is this, how do I install it, how do I use it in 30 seconds, where do I go for more" — and nothing that needs updating on every release or PR lives in it anymore.