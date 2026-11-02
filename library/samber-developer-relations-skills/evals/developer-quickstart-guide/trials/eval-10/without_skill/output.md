# 1. Quickstart — `docs/quickstart.md`

```markdown
---
title: Quickstart
description: Store your first documents in Vellum and run a semantic search — no ML background required.
---

# Vellum Quickstart

**Time:** ~25 minutes
**You'll need:** A Vellum account (free tier is fine) and one PDF, DOCX, or text file to test with — a claims note, policy wording, or underwriting guideline works well.
**No prior experience with embeddings, vector databases, or machine learning is assumed.**

By the end of this page you will have:

- Uploaded a real document into Vellum
- Watched Vellum split it into chunks and turn each chunk into a vector
- Asked a plain-English question and gotten back the exact passage that answers it — even when your question doesn't share a single word with the source text

---

## Before you touch anything: what problem is this solving?

Skip this section if you already know what embeddings and chunking are. Everyone else, read it once — it's the difference between "I copied some code" and "I know why this works."

### The problem with keyword search

Say you have ten years of commercial property claims notes, and you want to find every claim similar to a new one: *"pipe burst in the ceiling of a vacant unit during a cold snap."*

A keyword search for "pipe burst" misses the adjuster who wrote *"water intrusion from a ruptured supply line."* Same event, no shared words. Insurers lose real time to this — the answer is in the file, but it's filed under different language than the search box expects.

### What an embedding actually is

An embedding is a list of numbers that represents the *meaning* of a piece of text, not its exact wording. Vellum generates this list automatically for every piece of text you give it, using a machine learning model — you never write or tune this model yourself.

The property that matters to you: **text with similar meaning gets a similar list of numbers.** "Pipe burst in the ceiling" and "ruptured supply line caused water intrusion" end up close together in that numeric space, even though they don't share a single word. "Pipe burst" and "hail damage to roof" end up far apart.

Vellum stores each embedding in a **vector store** (this product) and can then answer "which stored texts are numerically closest to this new text?" in milliseconds, across millions of documents. That's what people mean by *semantic search* or *similarity search* — search by meaning, not by string match.

### What chunking is, and why you can't skip it

A 40-page underwriting manual can't become one embedding. One vector can only represent one idea well — cram a whole manual into it and the vector becomes a blurry average of everything in the document, matching everything a little and nothing precisely.

**Chunking** is splitting a document into smaller pieces — a paragraph, a clause, a section — before embedding each piece separately. Chunk well, and a search for "flood exclusion in coastal zones" returns the three-sentence clause that actually answers it, not the entire manual with a shrug attached.

Vellum chunks documents for you automatically on upload, using sensible defaults for common formats (PDF, DOCX, plain text, HTML). You don't need to configure this to get a working result today — see [Chunking strategies](/guides/chunking-strategies) later if your results need tuning for very long or very short documents.

### The full pipeline, in one picture

```
Your document
     │
     ▼
  Chunking          ← splits the document into meaningful pieces
     │
     ▼
  Embedding         ← each chunk becomes a list of numbers (a vector)
     │
     ▼
  Vector index      ← Vellum stores the vectors so they can be searched
     │
     ▼
Your question  ──►  embedded the same way  ──►  compared against every
                                                  stored vector  ──►  the
                                                  closest matches come back
```

Everything below is you clicking through this pipeline once, end to end.

---

## Step 1: Create an index

An **index** is where a related set of documents lives — think of it as one searchable collection. Most teams start with one index per use case (e.g., `claims-notes`, `underwriting-guidelines`) rather than one per document.

1. Log in to [app.vellum.example](https://app.vellum.example) and click **New Index**.
2. Name it `quickstart-demo`.
3. Leave **Embedding model** on the default (`vellum-embed-general-v2`) — it's tuned for mixed business documents and is the right choice unless a later guide tells you otherwise.
4. Click **Create**.

**Checkpoint:** you should land on the index's empty dashboard, showing `0 documents`, `0 chunks`.

---

## Step 2: Upload a document

1. In `quickstart-demo`, click **Upload documents**.
2. Drag in one PDF, DOCX, or `.txt` file. A claims note, a policy wording page, or a short underwriting guideline all work well for this test.
3. Click **Upload**.

Vellum chunks and embeds the file automatically. For a single document this takes a few seconds.

**Checkpoint:** the dashboard now shows `1 document`, and a chunk count greater than zero (a two-page document typically produces 5–15 chunks). Click **View chunks** to see exactly how your document was split — this is worth doing once so chunking stops being an abstract idea.

---

## Step 3: Ask a question

This is the moment the concepts above become real.

1. Click the **Search** tab.
2. Type a question in your own words — one that does *not* quote the source text verbatim. If you uploaded a water-damage claim, try something like *"cold weather pipe failure in an unoccupied building."*
3. Click **Search**.

**Checkpoint:** the top result is the chunk describing the actual incident, with a similarity score (closer to 1.0 is a stronger match). Note that this worked even though your query and the source text likely share almost no exact words — that's the embedding doing its job.

If the top result looks wrong, see [Troubleshooting](#troubleshooting) below before assuming something is broken — a handful of near-misses is normal on a single-document test index.

---

## Step 4 (optional): Do it from code

The dashboard is the fastest way to see the concept work. Once you're ready to automate ingestion or search from your own systems, the same three steps map directly to API calls.

### Install the SDK

```bash
pip install vellum-client
```

### Get your API key

**Settings → API Keys → Create key** in the dashboard. Treat this like a password — it has full read/write access to your indexes.

```bash
export VELLUM_API_KEY="your-key-here"
```

### Upload and query

```python
from vellum import Client

client = Client(api_key="your-key-here")  # or reads VELLUM_API_KEY automatically

# Step 1 & 2: upload a document to an existing index — Vellum chunks
# and embeds it server-side, same as the dashboard upload.
with open("claim-notes-2026-04.pdf", "rb") as f:
    result = client.documents.upload(
        index="quickstart-demo",
        file=f,
        metadata={"line_of_business": "commercial_property", "state": "OH"},
    )

print(f"Uploaded {result.document_id}, split into {result.chunk_count} chunks")

# Step 3: ask a question in plain language
matches = client.search(
    index="quickstart-demo",
    query="cold weather pipe failure in an unoccupied building",
    top_k=5,
)

for m in matches:
    print(f"{m.score:.3f}  {m.text[:100]}...")
```

Expected output:

```
Uploaded doc_8f2a1c, split into 9 chunks
0.891  Adjuster note 2026-04-11: insured reports water damage originating from ceiling of unit 4B...
0.734  Property was vacant pending sale at time of loss, heat had been shut off approximately...
0.298  Policyholder disputes deductible amount cited in initial estimate...
```

Notice the `metadata` field on upload — `line_of_business` and `state` here. That's how you'll later narrow a search to, say, only Ohio commercial property claims. See [Metadata filtering](/guides/metadata-filtering).

---

## What you built

- An index (a searchable collection of vectors)
- One document, automatically chunked into smaller, meaningfully-sized pieces
- An embedding for every chunk, generated for you
- A working semantic search over it, queryable by meaning rather than exact wording

That's the entire mental model behind every larger Vellum use case — claims triage, underwriting guideline lookup, policy Q&A — just with more documents and, usually, metadata filters layered on top.

---

## Troubleshooting

**Search returns nothing, or only very low scores (below ~0.3).**
Your query is likely about a topic that isn't in your test document. Try a question you know the uploaded file actually addresses, or upload a second, more varied document.

**The top result is the right document but the wrong section.**
This is a chunking issue, not a search issue — the relevant sentence probably got merged into a chunk with unrelated content. See [Chunking strategies](/guides/chunking-strategies) to adjust chunk size for long-form documents like underwriting manuals.

**Upload fails with `unsupported_file_type`.**
Quickstart supports PDF, DOCX, TXT, and HTML. Scanned image-only PDFs (no text layer) aren't supported yet — see [Supported file types](/reference/file-types) for OCR workarounds.

**API calls return `401 Unauthorized`.**
Your key is missing or wrong in the `VELLUM_API_KEY` environment variable — regenerate it from **Settings → API Keys** and re-export it in the same terminal session you're running from.

**`403 index_not_found` on upload or search.**
The `index` string in your code must match the index name exactly, including case — check it against the dashboard.

---

## Next steps

- [Core concepts: indexes & search](/getting-started/core-concepts-indexes) — namespaces, distance metrics, and when to split into multiple indexes
- [Chunking strategies](/guides/chunking-strategies) — tune chunk size once documents get longer than a few pages
- [Metadata filtering](/guides/metadata-filtering) — restrict search by line of business, state, date, or any field you define
- [Vellum for insurance](/getting-started/vellum-for-insurance) — worked examples for claims triage and underwriting lookup
- [Security & compliance](/security/data-residency) — data residency, encryption, and retention, relevant before loading real policyholder data
```

---

# 2. README — `README.md`

```markdown
<div align="center">
  <h1>Vellum</h1>
  <p><strong>A managed vector store for teams who don't want to run one.</strong></p>

  <a href="https://github.com/vellumdb/vellum/actions"><img src="https://img.shields.io/github/actions/workflow/status/vellumdb/vellum/ci.yml?branch=main" alt="CI status"></a>
  <a href="https://pypi.org/project/vellum-client/"><img src="https://img.shields.io/pypi/v/vellum-client.svg" alt="PyPI version"></a>
  <a href="https://github.com/vellumdb/vellum/blob/main/LICENSE"><img src="https://img.shields.io/badge/license-Apache--2.0-blue.svg" alt="License"></a>
  <a href="https://status.vellum.example"><img src="https://img.shields.io/badge/status-operational-brightgreen.svg" alt="Status"></a>

  <br><br>

  <a href="https://docs.vellum.example">Documentation</a> •
  <a href="https://docs.vellum.example/quickstart">Quickstart</a> •
  <a href="https://vellum.example">Website</a> •
  <a href="https://vellum.example/discord">Discord</a>
</div>

---

Vellum stores documents as searchable vectors and handles chunking, embedding, indexing, and scaling for you. Point it at your documents, query in plain language, get back the passage that actually answers the question — not just the ones that share keywords.

This repo hosts the official SDKs and CLI. The vector store itself runs as a hosted service; self-hosting is covered in [Self-hosting](#self-hosting) below.

## Why Vellum

- **Zero infrastructure** — no index sharding, no embedding model hosting, no GPU capacity planning
- **Automatic chunking and embedding** — upload a PDF or plain text, Vellum handles the rest
- **Metadata filtering built in** — narrow any search by your own fields (line of business, state, date, customer ID, anything)
- **SOC 2 Type II, encryption at rest and in transit** — see [Security & compliance](https://docs.vellum.example/security)

## Quick start

```bash
pip install vellum-client
```

```python
from vellum import Client

client = Client(api_key="your-key-here")

client.documents.upload(index="claims-notes", file=open("claim.pdf", "rb"))

results = client.search(index="claims-notes", query="frozen pipe burst in vacant unit")
print(results[0].text)
```

Full walkthrough, including what an embedding and a chunk actually are: [docs.vellum.example/quickstart](https://docs.vellum.example/quickstart).

## Installation

| Language | Install |
|---|---|
| Python | `pip install vellum-client` |
| Node.js | `npm install @vellum/client` |
| Go | `go get github.com/vellumdb/vellum-go` |
| CLI | `curl -sSL https://cli.vellum.example/install.sh \| sh` |
| Any other language | [REST API reference](https://docs.vellum.example/api/rest) |

## Usage

<details>
<summary>Upload and search (Python)</summary>

```python
from vellum import Client

client = Client(api_key="your-key-here")

client.documents.upload(
    index="underwriting-guidelines",
    file=open("guideline.pdf", "rb"),
    metadata={"state": "OH", "line_of_business": "commercial_property"},
)

results = client.search(
    index="underwriting-guidelines",
    query="flood exclusion for coastal zones",
    filters={"state": "OH"},
    top_k=5,
)
```
</details>

<details>
<summary>Same thing, REST</summary>

```bash
curl -X POST https://api.vellum.example/v1/indexes/underwriting-guidelines/search \
  -H "Authorization: Bearer $VELLUM_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"query": "flood exclusion for coastal zones", "top_k": 5}'
```
</details>

## Self-hosting

Vellum's ingestion and query engine can run in your own VPC for teams with data residency requirements the managed service doesn't cover yet. See [Self-hosted deployment](https://docs.vellum.example/self-hosted) — this covers the engine only; embedding generation still calls the managed API unless you also configure a local model (see that page).

## Documentation

- [Quickstart](https://docs.vellum.example/quickstart)
- [Guides](https://docs.vellum.example/guides) — chunking, metadata filtering, RAG pipelines, batch imports
- [API reference](https://docs.vellum.example/api)
- [Security & compliance](https://docs.vellum.example/security)

## Contributing

SDK and CLI contributions are welcome — see [CONTRIBUTING.md](CONTRIBUTING.md). The hosted vector store itself is closed-source; this repo covers only the client libraries.

## Support

- Bug in an SDK or the CLI: [open an issue](https://github.com/vellumdb/vellum/issues)
- Product/account questions: [support@vellum.example](mailto:support@vellum.example)
- Real-time status: [status.vellum.example](https://status.vellum.example)

## License

Apache 2.0 © Vellum
```

**What changed from a typical "grown organically" README, and why:** one badge row instead of scattered ones lower down; a single Quick Start block above the fold instead of installation buried under history/roadmap/screenshots; SDK install table instead of four separate prose paragraphs; usage examples collapsed behind `<details>` so the page doesn't force-scroll past code most readers won't run today; self-hosting and contributing pushed below docs links, since most visitors are evaluating the product, not shipping a PR.

---

# 3. Docs nav reorganization

The 40-ish items had no grouping, so everything competed for attention at the same visual weight. Below is a structure ordered by *user journey* — learn the concept → do the common task → go deeper → integrate → operate → get reference/support — rather than alphabetically or by when the page happened to get written.

### Structure

```
Getting Started                              (expanded by default)
├── Overview
├── Quickstart
├── Core concepts: embeddings & chunking
├── Core concepts: indexes & search
├── Vellum for insurance
└── Migrating to Vellum

Guides                                        (collapsed by default)
├── Chunking strategies
├── Choosing an embedding model
├── Uploading documents (PDF, DOCX, CSV, HTML)
├── Metadata filtering
├── Hybrid search (keyword + semantic)
├── Re-ranking results
├── Building a RAG pipeline
├── Batch importing large datasets
├── Updating and deleting vectors
└── Multi-tenant namespaces

SDKs & API
├── REST API reference
├── Python SDK
├── Node.js SDK
├── Go SDK
├── CLI reference
└── Rate limits & pagination

Integrations
├── LangChain
├── LlamaIndex
├── OpenAI / Anthropic models
├── Snowflake sync
└── Slack

Security & Compliance
├── Data residency & regions
├── Encryption at rest & in transit
├── SOC 2 report
├── Compliance for insurers (state data rules, GLBA)
├── SSO & SCIM
└── Audit logs

Administration
├── Organizations & teams
├── Roles & permissions
├── Billing & usage
└── Monitoring & alerts

Reference
├── Supported file types & embedding models
├── Distance metrics (cosine, dot product, Euclidean)
└── Glossary

Troubleshooting & Support
├── Common errors
├── Status & incident history
├── Support channels
└── Changelog
```

### Rules applied

- **Header nav stays flat: 4 items max** — *Docs*, *API Reference*, *Pricing*, *Status* — the 8 groups above live inside the docs sidebar, not the top nav. A sidebar with 40 items in one flat list is a wall; 8 named groups with 4–10 items each is scannable.
- **"Getting Started" is the only group expanded by default.** Everything else collapses until clicked — matches how a first-time reader actually moves through the site versus a returning reader who jumps straight to *SDKs & API*.
- **Concepts precede tasks, tasks precede reference.** *Core concepts* sits above *Chunking strategies* even though the latter gets more search traffic — a reader who lands mid-guide without the concept page will bounce, not scroll up.
- **"Vellum for insurance" lives in Getting Started, not buried in Guides.** For your actual traffic mix (mid-size insurers), this is a top-3 page; alphabetical or chronological ordering was hiding it.
- **Security & Compliance is its own top-level group, not nested under Administration.** Insurance buyers evaluate compliance before they evaluate features — it needs to be findable without opening an unrelated parent first.
- **No page is an orphan.** Every item above should be linked from at least one other page's body text (e.g., the Quickstart already links to *Chunking strategies*, *Metadata filtering*, and *Vellum for insurance* — extend that pattern to the remaining guides as you migrate them into this structure).

### Implementation note

If your docs tool uses a JSON/YAML sidebar config (Docusaurus, Mintlify, etc.), each group above maps directly to one category object with `collapsed: true` except *Getting Started*. Migrate one group at a time rather than cutting over all 40 items at once — verify old URLs still resolve (redirect, don't rename-and-break) before moving to the next group, since anything already indexed by search engines or bookmarked by a customer will 404 otherwise.