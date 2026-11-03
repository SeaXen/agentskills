# Chapter Scaffold System (Validated Pattern)

This system was validated for Cardiology (111 topics, complete) and Rheumatology (78 topics scaffolded, 10 upgraded).

## Directory Structure

```
/mnt/tb/Medicine/<Specialty>/
├── <Specialty> MOC.md                    # Master index + completion tracking
├── Davidson Chapter XX - <Specialty> Hierarchy.md  # Full validated tree
├── Chapter XX <Specialty> Roadmap.md     # Study sequence, weights, phases
├── <Specialty> Channel Session Resume YYYY-MM-DD.md  # Continuation prompt
├── Templates/
│   └── <Specialty> Topic Template.md     # (optional, now in skill references)
└── <Heading Hub Name>/                   # One per major section
    ├── <Heading Hub>.md                  # scaffold-hub
    ├── <Topic Group 1>/
    │   ├── <Topic Group Hub>.md          # scaffold-hub
    │   ├── <Disease 1>.md                # scaffold → full-fcps-mrcp-note
    │   └── <Disease 2>.md
    └── <Topic Group 2>/
        ├── <Topic Group Hub>.md
        └── ...
```

## File Status Values

| Status | Meaning | Used For |
|--------|---------|----------|
| `scaffold-hub` | Heading/topic-group hub, not yet expanded | Hub files |
| `scaffold` | Disease-level placeholder with expansion targets | Initial disease files |
| `full-fcps-mrcp-note` | Fully upgraded exam-ready note | Completed topics |
| `true-disease-level-scaffold-system-validated` | MOC-level flag | MOC frontmatter |

## Frontmatter for Hub Files (scaffold-hub)

```yaml
---
tags: [medicine, <specialty>, davidson, scaffold-hub]
chapter: <Chapter Name>
davidson_part: Part 3: Clinical Medicine
davidson_chapter: Chapter XX: <Chapter Title>
heading: <Heading Hub Name>
topic_group: <Topic Group Name>  # or same as heading for top-level
topic: <Hub Display Name>
status: scaffold-hub
updated: YYYY-MM-DD
---
```

## Frontmatter for Disease Scaffolds

```yaml
---
tags: [medicine, <specialty>, davidson, scaffold]
chapter: <Chapter Name>
davidson_part: Part 3: Clinical Medicine
davidson_chapter: Chapter XX: <Chapter Title>
heading: <Heading Hub Name>
topic_group: <Topic Group Name>
topic: <Disease Name>
status: scaffold
updated: YYYY-MM-DD
---
```

## MOC Tracking Section

In `<Specialty> MOC.md`, maintain:

```markdown
## Completed scaffold-to-full-note topics (verified full FCPS/MRCP notes: N)
  - ✅ [[Section/Disease|Disease Name]] — full FCPS/MRCP note completed
  ...
```

Update count and ✅ links after each batch commit.

## Git Workflow

1. Create scaffolds in batches (heading hubs → topic groups → diseases)
2. Commit after each logical layer (hubs, then disease scaffolds)
3. Upgrade scaffolds → full notes in priority order (must know → should know → nice to know)
4. Commit after each upgrade batch (user preference: **10 topics per batch**; min 3-5)
5. Update MOC ✅ tracking in same commit
6. Push to remote

## Session Continuity

- Create `<Specialty> Channel Session Resume YYYY-MM-DD.md` after each session
- Contains: current progress, next priority topics, active state, open questions
- Enables seamless handoff across context windows
- Reference in MOC for quick access

## Priority Order for Upgrades

**Must Know (Core)** — Highest exam weight, guaranteed viva/SBA:
- Prototype diseases (RA, SLE, OA, Gout, etc.)
- Emergencies (Septic arthritis, GCA)
- Core investigations/drugs

**Should Know (High Yield)** — Frequent but not universal:
- Variants (PsA, SpA subsets)
- Organ-specific (Lupus nephritis, RA-ILD)
- Secondary causes

**Nice to Know (Advanced)** — Rare, niche, or advanced:
- Rare vasculitides
- Overlap syndromes
- Complex pain syndromes