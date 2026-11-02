## Scope call before I start

Your two requirements collide with each other, and it's worth naming that instead of quietly picking one. The skill's own scope check says: *"The reader is new to the problem space and needs concepts explained → getting-started guide, not a quickstart."* Data analysts who've never met embeddings or chunking are exactly that reader. A pure quickstart (zero explanation, domain-expert audience) would fail them at word one.

Resolution I'm shipping: one page, but structurally two artifacts glued together — a short, clearly-boxed concepts primer (the getting-started part) immediately followed by a real quickstart (three steps, no digressions, hard budget). This keeps it to one afternoon and one URL. The seam is deliberate: once this page proves out, split the primer into its own "Core concepts" explainer that other Vellum docs can link to, and let the procedural half become a true no-explanation quickstart for readers who already know the space (your own engineers, partners integrating Vellum). I'm flagging this as the thing to revisit, not deciding it silently.

Second call: I don't have a real Vellum product to cold-run against, so every command, output, and score below is invented-but-internally-consistent, the same way the skill's own worked example uses a fictional "Pigeon" API. **Nothing here is verified. Treat it as a draft someone must cold-run on real infrastructure before it ships** — see the Verification plan section, which names who runs it and against what.

Third call, and the one I'd push back hardest on if you were in the room: your audience is data analysts, some of whom have "never opened a terminal" energy. `pip install` and a `.py` file are a real risk to the time budget below, bigger than embeddings-as-a-concept. I did not promote the container to a notebook to fix this — that's a standing hosting/upkeep cost the skill says to only take on with a named owner, and "one afternoon" rules that out today. I flagged it instead as the first thing your cold run should test.

---

## 1. Success moment and time budget

**Success moment:** given a new claim description, Vellum returns the past claims that are actually about the same kind of incident — ranked by meaning, not by shared keywords.

**Time budget:** 3 min to read the primer + 7 min hands-on = **10 min total**, committed as two numbers, not one, because folding reading time silently into a "10-minute quickstart" claim is exactly the kind of thing a cold run should catch as a lie. Baseline for the product class (data platform: "query returns rows the reader inserted") is 10 min — the primer rides inside that budget, it doesn't extend it.

---

## 2. The page

```markdown
# Find your first matching claim in Vellum (10 minutes)

You'll load five sample claim notes into Vellum, then search with a new claim
description and watch Vellum surface the notes that describe the same kind of
incident — even though none of them share an exact phrase with your search.

Reading the two concepts below takes about 3 minutes. The hands-on part takes about 7.

---

## First, two ideas you'll use in the next 7 minutes

**Embedding.** Vellum turns each claim note into a list of numbers that captures
what the note is *about*. Notes about similar incidents end up with similar
numbers, even if the wording is completely different. "Rear-ended at a stoplight"
and "collision at an intersection" land close together; "kitchen fire" lands far away.

**Chunking.** A short claim note becomes one list of numbers. A long adjuster
report gets split into smaller pieces first, then each piece gets its own list of
numbers — otherwise one giant report would drown out five short ones in a search.
Vellum decides where to split; you'll see it happen in step 2.

That's the whole mental model: **text → numbers that capture meaning → search by
nearest numbers.** Everything below just does that three times.

## Before you start

- Python 3.9 or later: check with `python3 --version` ([install](https://www.python.org/downloads/))
- A Vellum test API key: [create one](#) — no card required, self-serve
- **Use synthetic claim data for this page, not real policyholder data.** Test
  keys write to a sandbox project, but there's no reason to put real PII through
  a tutorial.

> **On a managed insurer network, or need a signed DPA before any data leaves
> your environment?** Skip this page and ask your Vellum account team for a
> scoped sandbox tenant on your production infrastructure — the steps below are
> the same once you have a key, but provisioning is a separate, longer process.

## 1. Install the client and confirm your key works

    pip install vellum-vdb==1.4

Create `check.py`:

```python
from vellum_vdb import Client

vellum = Client(api_key="<YOUR_TEST_API_KEY>")
print(vellum.ping())
```

Run it:

    python3 check.py

You should see:

    {'status': 'ok', 'project': 'sandbox-7f3a'}

`AuthenticationError: invalid key format`? Test keys start with `vlm_test_` —
re-copy the key, a trailing space from the dashboard is the usual cause.

## 2. Load five claim notes

Create `load.py`:

```python
from vellum_vdb import Client

vellum = Client(api_key="<YOUR_TEST_API_KEY>")

claim_notes = {
    "auto1": "Rear-end collision on I-90 near exit 4. Minor bumper damage. "
             "Other driver cited for following too closely.",
    "fire1": "Kitchen fire caused by unattended stove. Smoke damage throughout "
             "first floor. Fire department responded within 8 minutes.",
    "water1": "Burst pipe in the upstairs bathroom during the January freeze "
              "caused water damage to the bathroom, hallway, and the kitchen "
              "ceiling directly below. Contractor found the pipe had frozen and "
              "split overnight; the leak wasn't discovered until the ceiling "
              "began to sag the next morning. Homeowner shut off the main water "
              "valve and called emergency services. Estimated repair cost "
              "pending inspection, but initial assessment suggests full ceiling "
              "replacement and repainting of the hallway.",
    "auto2": "Two-vehicle collision at the intersection of 5th and Main. Other "
             "driver ran a red light. Front-end damage to bumper and hood.",
    "hail1": "Hail storm damage to roof shingles and gutters. Claim filed after "
             "the spring storm passed through the county.",
}

result = vellum.documents.add(collection="claims_notes", documents=claim_notes)
print(result)
```

Run it:

    python3 load.py

You should see:

    {'documents_added': 5, 'chunks_created': 6, 'collection': 'claims_notes'}

Six chunks from five notes — the long water-damage note above was split into
two, exactly what the chunking idea above described.

`chunks_created: 0`? A note is empty or all whitespace — check `claim_notes`
before calling `.add()`.

## 3. Search with a new claim

Create `search.py`:

```python
from vellum_vdb import Client

vellum = Client(api_key="<YOUR_TEST_API_KEY>")

matches = vellum.search(
    collection="claims_notes",
    query="Vehicle rear-ended at a stoplight, bumper and trunk damage, other driver at fault.",
    top_k=3,
)
for m in matches:
    print(m.chunk_id, m.score, m.text[:60])
```

Run it:

    python3 search.py

You should see:

    auto1   0.91   Rear-end collision on I-90 near exit 4. Minor bumper...
    auto2   0.84   Two-vehicle collision at the intersection of 5th and...
    water1#2 0.47  ...ceiling began to sag the next morning. Homeowner...

Scores near 0, or fewer than 3 results? Vellum indexes asynchronously — search
can lag `.add()` by a few seconds on a fresh collection. Wait 5 seconds and
rerun `search.py`.

## What just happened

The two auto-collision notes ranked first and second, with a real gap down to
the water-damage chunk in third — none of them share a phrase with your query,
so this couldn't be keyword search. That's chunk → embed → store → nearest-match,
the pipeline the primer described, done for you in three function calls.

## Next steps

- [Choosing a chunk size for longer documents](#) — adjuster reports and policy PDFs need this
- [API reference](#)
- [Community Slack](#)
```

---

## 3. Cut list

Removed from the page, and where it lives instead:

- **How nearest-neighbor search actually works internally** (ANN indexes, distance metrics) → explanation doc, linked from "what just happened" once it exists.
- **Chunk-size tuning, overlap, splitting strategies** → dedicated how-to, linked from Next steps. The quickstart shows chunking happen once, on autopilot; it doesn't teach the reader to configure it.
- **Enterprise auth (SSO/SAML), tenant provisioning, DPAs** → enterprise onboarding doc, linked from the callout box, not inlined as a second path.
- **Billing, plan limits, quotas** → pricing page.
- **Data residency / SOC2 / HIPAA posture** → security page (see nav section below) — material to an insurer evaluator, but it's a purchasing-decision document, not a hands-on-keyboard one.
- **Filtering by metadata, hybrid search, re-ranking** → separate how-to guides; each is its own quickstart-sized success moment.

## 4. Verification plan

Nobody has cold-run this because the product used to write it doesn't exist yet in this conversation. Before it ships:

1. Clean machine, no Python pre-installed, fresh sandbox key, no cached credentials.
2. **First run: a reader who has genuinely never opened a terminal.** This is the highest-risk step on the page, higher than the concepts themselves — if `pip install` alone blocks them, no amount of primer-writing fixes that, and the container choice (plain page vs. something with zero local setup) needs to be reopened.
3. Second run: a data analyst comfortable in Excel/SQL, new to Python — the actual target profile.
4. Third run: someone who already knows embeddings (sanity-check that the primer doesn't insult or bore this reader into leaving).
5. Log every defect against the table format in the skill's verification protocol (step, elapsed, command ran verbatim, output matched, defect). Stop the timer at the `search.py` output matching what's documented above.
6. Real product output replaces every invented number in step 2/3 above before publish — the 0.91/0.84/0.47 scores are placeholders for "a real gap," not a claim about what your model will actually return.

Ship gate: all five cold-run criteria from SKILL.md § Pass threshold, on all three profiles above, elapsed time ≤ 10 min for profiles 2 and 3.

## 5. Instrumentation

In priority order (value per hour of wiring, not report order):

- **Step-level drop-off**: event at page load and after each of the 3 steps' copy actions. This alone tells you if step 1 (install) is where non-engineers bail — the thing I'd bet on.
- **Support tickets quoting a step number.**
- **Median page-load-to-success-event time** — the honest version of the "10 minutes" claim.
- **Completion rate.**
- **Day-7 return of completers** — promote this above the rest once completion looks healthy; it's the only signal that says the claims-search use case, not just the tutorial, landed.

Measure four weeks against this page's own baseline before committing to a target number; don't import one from a vendor blog.

---

## README rewrite

Your current README is a mess; here's a replacement built off the same success moment as the quickstart, so a visitor who reads only the README already understands what "working" looks like.

```markdown
<div align="center">
  <h1>Vellum</h1>
  <p><strong>A managed vector store: hand it text, search it by meaning.</strong></p>

  <a href="https://github.com/your-org/vellum-vdb/actions"><img src="https://github.com/your-org/vellum-vdb/workflows/CI/badge.svg" alt="CI"></a>
  <a href="https://pypi.org/project/vellum-vdb/"><img src="https://img.shields.io/pypi/v/vellum-vdb.svg" alt="PyPI version"></a>
  <a href="LICENSE"><img src="https://img.shields.io/badge/license-MIT-blue.svg" alt="License"></a>

  <br><br>

  <a href="https://docs.vellum.example/quickstart">Quickstart</a> •
  <a href="https://docs.vellum.example">Documentation</a> •
  <a href="https://vellum.example/security">Security</a>
</div>

---

## What this is

Vellum chunks your documents, embeds them, and indexes them for nearest-meaning
search — as one hosted service. You send text; you get ranked matches back.
No embedding model to host, no ANN index to tune.

This repo is the **Python client**. The vector store itself is a managed
service — see [Security](https://vellum.example/security) for data residency
and compliance details if that's the first thing you need to know.

## Quick start

    pip install vellum-vdb

```python
from vellum_vdb import Client

vellum = Client(api_key="<YOUR_TEST_API_KEY>")
vellum.documents.add(collection="notes", documents={"n1": "your first document"})

for match in vellum.search(collection="notes", query="something similar"):
    print(match.score, match.text)
```

For the full walkthrough with real output at every step, see the
[10-minute quickstart](https://docs.vellum.example/quickstart) — it builds a
small claims-search example end to end.

## Why Vellum

- **No infra to run** — no self-hosted index, no embedding model to serve.
- **Chunking and embedding happen in one call** — you don't hand-tune a splitter before you've seen a result.
- **Search by meaning, not keyword** — see the quickstart for a concrete before/after.

## Installation

    pip install vellum-vdb

Pin a version in production:

    pip install vellum-vdb==1.4

## Documentation

Full docs at [docs.vellum.example](https://docs.vellum.example):

- [Quickstart](https://docs.vellum.example/get-started/quickstart)
- [Core concepts](https://docs.vellum.example/get-started/concepts)
- [API reference](https://docs.vellum.example/reference)

## Contributing

This client library is open source; the hosted service is not. See
[CONTRIBUTING.md](CONTRIBUTING.md).

## License

MIT © Your Org
```

Cut from the old README (assume the usual culprits until you send me the actual file): architecture diagrams, a changelog pasted inline instead of linked, and any config-flag table — those belong in the reference docs, not the front door.

---

## Docs nav reorganization

I don't have your actual 40 titles, so this is the bucket structure to sort them into, not a rename of specific pages. Run the current list through it: for each of the 40, ask "which bucket does the reader's *goal* belong to," not "which product area does this describe" — that's usually where organic 40-item navs go wrong, they grow by feature area instead of by reader task.

**Header nav — 6 items, CTA rightmost:**

```
Get Started | Guides | Reference | Integrations | Security | Pricing        [Start free →]
```

Support/Community moves to the footer — it doesn't need permanent header real estate, and keeping the header at 6 leaves room before you hit the 7-item ceiling.

**Bucket structure (sidebar within each header item):**

```
docs/
├── get-started/            (docs.vellum.example/get-started/...)
│   ├── quickstart                  — the page above
│   ├── core-concepts               — embeddings & chunking, split out of the quickstart later
│   ├── install-sdks                — Python, Node, CLI install pages
│   └── migrating-from-x            — Pinecone/Weaviate/pgvector migration guides
│
├── guides/                  (how-to, task-oriented — this is where most of your 40 land)
│   ├── choosing-a-chunk-size
│   ├── choosing-an-embedding-model
│   ├── filtering-with-metadata
│   ├── hybrid-search
│   ├── re-ranking-results
│   ├── batch-importing-documents
│   ├── updating-and-deleting-records
│   ├── redacting-pii-before-indexing        — insurer-relevant, put it here not buried in reference
│   └── ...
│
├── reference/                (SDK & API reference — alphabetical is fine here, it's lookup not learning)
│   ├── python-sdk
│   ├── node-sdk
│   ├── rest-api
│   ├── cli
│   ├── error-codes
│   └── rate-limits
│
├── integrations/
│   ├── langchain
│   ├── llamaindex
│   ├── snowflake
│   ├── s3
│   ├── postgres-cdc
│   └── zapier
│
├── security/                  (evaluator-facing, not task-facing — enterprise insurers read this before anyone touches an SDK)
│   ├── data-residency
│   ├── soc2-and-compliance
│   ├── sso-and-sso-saml
│   ├── audit-logs
│   └── backups-and-uptime-sla
│
└── platform/
    ├── pricing-and-plans
    ├── usage-limits-and-quotas
    ├── changelog
    └── status-page
```

Footer: **Support** (FAQ, troubleshooting, Slack, contact) and **Company** (about, careers) — neither belongs in the primary nav; nobody arrives at your docs site looking for "About."

URL pattern: `/docs/{bucket}/{page}`, lowercase, hyphens, no dates. If any of your current 40 URLs don't match this, they need 301s when you move them — don't silently break inbound links from blog posts or support tickets that already point at the old paths.

One placement call worth flagging explicitly: **security content sits at the same header level as guides, not nested under "Reference."** For a mid-size insurer, "can we even use this" gets decided before "how do we use this," and burying compliance docs three clicks deep under Reference is a common reason enterprise docs sites lose evaluators before they ever reach a quickstart.

---

## The afternoon

- Draft quickstart + primer: ~1.5 hr (mostly done above — swap in real output)
- Cold run #1 (non-technical profile) + fix what it finds: ~1 hr
- README rewrite: ~30 min
- Bucket the 40 nav items into the structure above: ~45 min
- Buffer / write the 301 redirect list for any moved URLs: ~15 min

That's the full afternoon. The concepts-vs-quickstart split above and the nav bucket structure are the two decisions I'd want you to sign off on before the hour goes in — everything else is mechanical once those are set.