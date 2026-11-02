# Four-Quadrant Classification — docs/ (Docusaurus)

**Evidence available:** file tree only — no page content, no front matter, no nav config, no analytics, no product-surface list (interview Q1–8 unanswered). Classifications below are titles/paths only; confidence is capped accordingly, per the skill's evidence-labeling rule. `guides/` and `api/` have no individual filenames, so those two get a section-level call, not a per-page one.

## Per-page / per-section table

| Page | Mode | Confidence | Why |
|---|---|---|---|
| `intro.md` | **Landing (not a mode)** | Low | Root-level "intro" ahead of a separate `getting-started/` folder reads as an overview/index, not a tutorial step. Judge it on whether it routes to all four quadrants — can't confirm without content. |
| `getting-started/install.md` | **Tutorial** | Medium | Onboarding-sequence position implies one linear setup path for a beginner, not a branching how-to. Verify it doesn't branch on OS/package-manager — that would make it a how-to instead. |
| `getting-started/first-pipeline.md` | **Tutorial** | High | "First X" is Diátaxis's own canonical tutorial title pattern — a contrived, guaranteed-success walkthrough to a working artefact. |
| `getting-started/concepts.md` | **Explanation** | High | Topic-titled ("Concepts," not a goal), cognition + acquisition by name. Check it doesn't end in a setup procedure — that's the "concepts page ending in a how-to" mixing symptom. |
| `guides/` (31 files) | **How-to guide** (section default) | Medium | "Guides" is the conventional how-to-section name. Can't verify per-file without titles — some of the 31 likely lean tutorial (a second "getting started" in disguise) or leak reference tables (numbered steps + option table is the most common mixing symptom at this file count). |
| `api/` (210 files, auto-generated) | **Reference** | High | Hard case, explicit: auto-generated API docs are reference by construction. Audit completeness/entry points, not prose — out of scope for mode judgment. |
| `architecture/overview.md` | **Explanation** | High | "Architecture overview" is the compass sheet's own worked example of an explanation title. |
| `architecture/scheduler.md` | **Explanation** | Medium | Topic-titled under an explanation-typed section. Flag for a content check: if it's actually a config/flag-by-flag rundown of the scheduler, it's reference, not explanation — title alone can't rule that out. |
| `architecture/storage.md` | **Explanation** | Medium | Same reasoning and same caveat as `scheduler.md`. |
| `faq.md` | **Mixed — not a mode** | High (on the classification itself) | Hard case: FAQ is a symptom, not a mode. Each Q&A belongs to whichever real mode its answer serves — likely a scatter of how-to and explanation entries filed under one URL. |

## Quadrant summary

- **Tutorial:** `install.md`, `first-pipeline.md` (2 confirmed) — thin, but that's normal; a getting-started sequence needs only one or two.
- **How-to:** `guides/*` (31, unverified individually) — the only how-to surface in the tree.
- **Reference:** `api/*` (210, auto-gen, out of prose-scope) — no other reference surface visible (no CLI reference, no config-file reference, no error-code table outside the API). Whether that's a real gap depends on the product's actual surfaces (unanswered Q5) — flagging as a question, not a finding.
- **Explanation:** `concepts.md`, `architecture/overview.md`, `architecture/scheduler.md`, `architecture/storage.md` (4).
- **Not a mode (index/symptom pages):** `intro.md`, `faq.md`.

## Findings worth a look (not confirmed — content unseen)

1. **`faq.md` mixing, high-confidence hard case.** Standard fix: keep it as a thin index, file each answer under its real mode, link out.
2. **`guides/` at 31 files is past this skill's flat-list heuristic (~30)** — worth a subfolder split or a check for a sub-topic cluster once file names are available.
3. **`concepts.md` inside `getting-started/`** — not a placement error by default (bridging concepts pages commonly sit in onboarding), but confirm it doesn't end in a procedure; if it does, that procedure belongs in `guides/`.
4. **No standalone reference surface besides auto-generated API** — flag as a coverage question for the team (CLI flags? config file schema?), not as a confirmed gap, since the product's surfaces weren't given.

To turn any of this from "proposed" into "confirmed," I'd need either repo/site access (front matter, actual `guides/`+`api/` filenames) or the product's surface list — happy to go a layer deeper on either.