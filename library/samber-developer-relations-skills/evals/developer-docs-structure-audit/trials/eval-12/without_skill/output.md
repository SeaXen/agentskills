# Diátaxis four-quadrant classification — `docs/`

Diátaxis quadrants: **Tutorial** (learning, hands-on) · **How-to** (task, hands-on) · **Reference** (lookup, informational) · **Explanation** (understanding, informational).

## Classification table

| Path | Quadrant | Notes |
|---|---|---|
| `intro.md` | **Explanation** | Orientation/landing page — "what is this, why use it." Not a quadrant itself, but closest to Explanation. Keep short, link out to the other three. |
| `getting-started/install.md` | **Tutorial** | Single guaranteed-path setup for a beginner. |
| `getting-started/first-pipeline.md` | **Tutorial** | Hands-on, one correct path, builds confidence. Textbook tutorial. |
| `getting-started/concepts.md` | **Explanation** ⚠️ | Misfiled. "Concepts" is background/mental-model content, not a step-by-step task — belongs with `architecture/`, not `getting-started/`. |
| `guides/` (31 files) | **Split — mostly How-to** ⚠️ | "Guide" is Diátaxis's most overloaded word. Needs a per-title pass; apply this test to each file: |
| `api/` (210 files, auto-gen) | **Reference** | Unambiguous — auto-generated API docs are the canonical Reference case. Leave as-is. |
| `architecture/overview.md` | **Explanation** | System design rationale. |
| `architecture/scheduler.md` | **Explanation** | Design/behavior discussion, not a task. |
| `architecture/storage.md` | **Explanation** | Same. |
| `faq.md` | **None — decompose** ⚠️ | FAQ isn't a Diátaxis quadrant; it's a junk drawer. Each Q&A belongs in one of the four buckets (see below). |

## Triage rule for `guides/` (31 files)

Diátaxis splits "guide" on one axis: **is the reader learning, or getting something done?**

- Title reads "Learn X" / "Understanding X" / "Why X" → **Explanation**, move toward `architecture/`.
- Title reads "How to X" / "Configure X" / "Deploy X to Y" / task-with-a-goal → **How-to guide**. This will be the bulk of the 31.
- Title reads "X options" / "X reference" / parameter tables → **Reference**, move toward `api/` or a new `reference/` section.
- Title is a second guaranteed-path onboarding lesson → **Tutorial**, move to `getting-started/`.

Expect roughly 25-28 of the 31 to land in How-to once titled; the rest scatter to the other three.

## `faq.md` decomposition rule

Walk each Q&A pair and reclassify:
- "How do I …?" → How-to guide.
- "Why does … work this way?" / "What is …?" → Explanation.
- "What does error X mean?" / parameter/limit lookup → Reference.
- Delete entries that are just a second copy of a Tutorial step.

Once emptied, retire `faq.md` (or leave a stub that links to the four real homes) rather than maintaining a fifth bucket.

## Resulting structure

```
Tutorial     → getting-started/install.md, getting-started/first-pipeline.md
             + any relocated guides/ "second lesson" files

How-to       → guides/ (bulk, post-triage)
             + relocated faq.md "how do I" entries

Reference    → api/ (all 210, untouched)
             + any guides/ files that are really parameter/option tables
             + relocated faq.md error/lookup entries

Explanation  → intro.md, getting-started/concepts.md (moved),
               architecture/overview.md, architecture/scheduler.md, architecture/storage.md
             + relocated faq.md "why/what is" entries
```

Net moves: pull `concepts.md` out of `getting-started/` into `architecture/` (or a new `explanation/`), retire `faq.md` into its target quadrants, and split `guides/` along the How-to/Explanation/Reference line above. `api/` needs no change.