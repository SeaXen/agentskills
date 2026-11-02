# Docs quality score for Pinerock's board

## Why the straight 4s don't survive contact

A first-pass audit that returns 4s across the board almost always means the rubric was applied too generously, not that the docs are exemplary. There's a published data point to check yourself against: the CNCF's 2024 analysis of TUF — a serious, widely-used CNCF project — scored **Information architecture 2, New user content 1, Content maintainability 3, Content creation processes 1, Inclusive language 3**. That's the realistic band for a project with no dedicated writer: mostly 1s and 2s on the criteria that touch a new user or a repeatable process, 3s only where a maintainer culture has already formed a habit (consistent PR review, a house style nobody wrote down). Pinerock — two maintainers, no writer — sits closer to TUF's profile than to a 4/5 profile by construction, independent of how good the prose is. "The writing is decent" is a real signal, but it's not one of the five criteria below, and it's the one thing that made the 4s feel earned.

Don't hand the board one blended number either. A single figure averages away exactly the information a board needs ("is this a writing problem or a process problem") and can't be checked by anyone outside the docs team. Score in two separate layers instead, and keep them visibly separate in whatever you hand up.

## Layer 1 — CNCF TechDocs rubric (the number that travels outside the docs team)

This is the most concrete public instrument for scoring a documentation set, it's free to reuse, and a board member or a future auditor can go verify it against the source (`github.com/cncf/techdocs`). Score each top-level docs section against it, not the docs as a whole — a single number still hides which section is dragging.

Scale (use the named anchors, not just odd numbers — it forces a real decision at 2 and 4):

| Score | Meaning |
|---|---|
| 1 | Not present |
| 2 | Needs improvement |
| 3 | Meets standards |
| 4 | Meets or exceeds standards |
| 5 | Exemplary |

Criteria — Project documentation category (this is the one a structure audit owns in full):

- **Information architecture** — can a reader find the right page without search?
- **New user content** — is there a supported first path for someone with zero context?
- **Content maintainability** — is content structured so it doesn't rot on the next release?
- **Content creation processes** — is there a repeatable way contributors add/update docs, or does it depend on one person remembering?
- **Inclusive language** — plain, bias-free language throughout.

Fill this per section, not as a single row:

| Section | Information architecture | New user content | Content maintainability | Content creation processes | Inclusive language |
|---|---|---|---|---|---|
| Getting started | | | | | |
| Guides / how-tos | | | | | |
| Concepts / architecture | | | | | |
| API / reference | | | | | |
| Operations / deployment | | | | | |

Score contributor documentation (communication channels, beginner-friendly issues, new-contributor onboarding, governance docs) as a **separate table**, and only if the board actually asked about contributor health — don't fold it into the headline docs-quality number, it's a different question.

Deliverable shape CNCF itself uses, worth mirroring because it gives three different readers three different documents: an **analysis** (the ratings above, with a one-line comment per score), an **implementation plan** (recommendations broken into blocks a maintainer can do in an evening), and an **issues list** contributors can pick off directly.

## Layer 2 — structural scorecard (the number that drives the actual work)

This is not published anywhere — it's a working baseline, and you should say that explicitly when you present it, and agree the target column with your co-maintainer before you score against it. A 120-page project and a 900-page platform don't pass on the same numbers.

| Measure | How to compute | Target | Source |
|---|---|---|---|
| Mode purity | single-mode pages ÷ total pages | ≥ 90% | self-set |
| Surface coverage | product surfaces carrying the modes they need ÷ total surfaces | 100% of top surfaces | self-set |
| Entry points | one tutorial/quickstart per primary audience | present | Diátaxis |
| Orphans | pages absent from navigation | 0 | self-set |
| Dead nav entries | nav entries pointing at nothing | 0 | self-set |
| Broken internal links | link checker over the built site | 0 | self-set |
| Nav depth | deepest navigation level | ≤ 3 | self-set |
| Thin sections | nav sections holding a single page | 0 | self-set |
| Demand coverage | top 20 recurring questions (issues, Discord/Slack, search) with a findable answer | ≥ 90% | self-set |
| Staleness | pages untouched since the last major release | ≤ 10% | self-set |
| ROT rate | pages flagged Redundant/Outdated/Trivial ÷ total | report — no target | standard content-audit heuristic |

ROT gets reported, not graded — there's no defensible pass mark for it, and pretending there is invites the board to argue the wrong number.

You get most of these mechanically. From the docs repo:

```bash
python3 scripts/docs-inventory.py ./docs --nav mkdocs.yml > inventory.tsv
```
(swap `--nav` for whatever Pinerock's generator uses — MkDocs, Docusaurus, etc. — the script flags the reference for each.)

That gives mode purity, orphans, dead nav entries, nav depth, and thin sections straight from the file tree and nav config. Broken links come from a link checker over the built site. Staleness and ROT need `git log` dates plus a judgment pass on each page. Demand coverage needs whatever signal you can actually reach — GitHub issues labeled `question`/`docs`, Discord/Slack search, or docs-site search if you have analytics; for a 120-page project with two maintainers, issues are probably your best and cheapest signal.

## Rules for the board number specifically

- **The audit is unfinished while any must-fix measure fails.** Don't present a final grade off a first pass — re-run the inventory script and re-score after each remediation batch, and report the delta (that delta, not the absolute score, is what proves the two maintainers' time is working).
- **Label the two layers by where they came from** when you present them — the CNCF scale is a published external instrument the board can cross-check; the structural scorecard's targets are yours, and saying so up front is what makes the number defensible rather than "trust me."
- Don't let a clean CNCF score on, say, Content maintainability paper over a scorecard that shows 40% mode purity — they're measuring different things and a board slide averaging them together will hide the one that actually predicts whether a new contributor can find anything.