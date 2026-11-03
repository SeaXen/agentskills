# Cardiology Live Vault Topic Production

Use this reference when working inside the user's Davidson Chapter 16 Cardiology system under `/mnt/tb/Medicine/Cardiology/`.

## Scope and boundary
- Chapter: **Davidson Chapter 16: Cardiology**
- Keep work inside the Cardiology chapter boundary.
- This chapter may use a mixed but still true-disease-level-oriented hierarchy: disease entities + high-yield syndromic states + interpretation/procedure nodes needed for FCPS/MRCP cardiology.
- Be explicit that this is usually **not a pure disease-only taxonomy**. Cardiology benefits from disease files plus files like ECG approach, troponin interpretation, reperfusion strategy, syncope risk stratification, and hemodynamic profiles.

## Source split for this user
- Anatomy: **Gray's Anatomy + Davidson correlation**
- Physiology: **Guyton & Hall + Ganong + Davidson**
- Clinical discussion: **Davidson + PasTest + personal notes when available**

## Proven Cardiology scaffold pattern
Validated chapter build used:
- chapter MOC
- chapter hierarchy map
- heading hubs
- topic-group hubs
- disease-level / small-topic scaffold files
- chapter pinned message
- chapter session-resume note
- master-index updates

Current validated Chapter 16 hierarchy counts from session:
- 10 heading hubs
- 20 topic-group hubs
- 103 disease-level/small-topic scaffold files in hierarchy
- 12 preserved root-level core notes
- 148 total Cardiology markdown files after scaffold build

## Current heading hubs
- Clinical Assessment, Hemodynamics, and Cardiac Investigations
- Ischaemic Heart Disease and Acute Coronary Syndromes
- Heart Failure and Acute Cardiac Decompensation
- Arrhythmias and Cardiac Conduction Disorders
- Hypertension and Cardiovascular Risk States
- Valvular Heart Disease and Murmur Syndromes
- Cardiomyopathies and Myocardial Disease
- Pericardial, Endocardial, and Inflammatory Cardiac Disease
- Adult Congenital Heart Disease and Cardiac Shunts
- Syncope, Shock, and Acute Hemodynamic Emergencies

## Preserved root-level core notes
- Heart Failure
- Acute Coronary Syndrome
- Hypertension
- Arrhythmias
- Valvular Heart Disease
- Ischemic Heart Disease
- Cardiomyopathy
- Pericardial Disease
- Infective Endocarditis
- Congenital Heart Disease in Adults
- Syncope
- Shock and Hemodynamic Profiles

## Validation workflow proven in session
When the user asks for a strict Davidson validation/refinement pass for Cardiology:
1. Read the current local chapter roadmap/MOC/rules first.
2. Search public Davidson-like snippets or chapter-result previews for cardiology themes.
3. Be honest: if full licensed chapter text is unavailable, label the result as a **public-snippet validation/refinement pass**, not a verbatim TOC match.
4. Use those snippets to refine heading names and topic coverage.
5. Record the honesty note in the hierarchy file itself.

Publicly surfaced validation themes that were useful in this session:
- clinical assessment / JVP
- heart failure
- hypertension
- arrhythmias
- valvular disease
- ischaemic heart disease / ACS
- cardiomyopathy
- pericardial disease
- infective endocarditis
- congenital heart disease
- syncope
- hemodynamic / shock assessment

## Continuation files
Key control notes created in session:
- `/mnt/tb/Medicine/Cardiology/Cardiology MOC.md`
- `/mnt/tb/Medicine/Cardiology/Davidson Chapter 16 - Cardiology Hierarchy.md`
- `/mnt/tb/Medicine/00_Index/Chapter Rules/Cardiology Channel Rules.md`
- `/mnt/tb/Medicine/00_Index/Chapter Rules/Cardiology Channel Pinned Message.md`
- `/mnt/tb/Medicine/00_Index/Cardiology Channel Session Resume 2026-05-06.md`

## Recovery when prior transcript is truncated or ambiguous
If session search says a prior cardiology run was cut off, or the transcript summary cannot confirm whether git/push finished:
1. Treat the live vault as authoritative, not the transcript summary.
2. Read the current `Cardiology MOC.md` and `00_Index/Cardiology Channel Session Resume 2026-05-06.md` first.
3. Check cardiology-scoped git status with:
   - `git -C /mnt/tb/Medicine status --short -- Cardiology '00_Index/Cardiology Channel Session Resume 2026-05-06.md'`
4. If status is clean, continue from the live queue in the resume/MOC.
5. If status is dirty, distinguish partial file edits from a completed-but-unpushed batch before continuing.
6. Recompute the next exact queue from the live completed-topic markers in the MOC rather than trusting stale chat summaries.

## Continuation prompt
```text
Use /mnt/tb/Medicine/00_Index/Cardiology Channel Session Resume 2026-05-06.md as the current setup. Continue Cardiology from there. Work only inside Davidson Chapter 16: Cardiology. Create/update real files under /mnt/tb/Medicine/Cardiology/, update Cardiology MOC and hierarchy notes when needed, and do git add/commit/push after each change or update.
```

## Proven continuation workflow for topic-upgrade turns
1. Read the active cardiology session-resume note.
2. Read the live `Cardiology MOC.md` before choosing the next target, because the resume queue can lag behind newer completions.
3. If the user says `next N`, treat `N` as an exact batch size and upgrade exactly that many scaffold files already present in the hierarchy.
4. Upgrade the existing scaffold note in place under `/mnt/tb/Medicine/Cardiology/`.
5. Update navigation at the directly exposed layers that mention the topic:
   - `Cardiology MOC.md`
   - relevant topic-group hub
   - `Davidson Chapter 16 - Cardiology Hierarchy.md` when it lists the topic
6. Refresh the session-resume note so the queue, compact continuation prompt, and recommended safe next command remain accurate after the batch.
7. Run path-scoped `git add` / `git commit` / `git push` for the cardiology batch without waiting for another reminder.

## Progress-count reporting workflow
- Do not report cardiology completion counts from `status: full-fcps-mrcp-note` files alone.
- This chapter can contain preserved root-level core notes that are already full but may not yet use the newer status marker.
- Use the live `Cardiology MOC.md` as the primary source of truth for `completed` vs `left` reporting.
- The working denominator for this validated Chapter 16 setup is usually:
  - **103** disease-level/small-topic scaffold files in the hierarchy, plus
  - **12** preserved root-level core notes,
  - giving **115 tracked cardiology topic units**.
- Count:
  1. explicit completed scaffold-to-full-note entries in the MOC, and
  2. preserved root-level core notes already marked as full in the MOC.
- When only those markers are verified, label the result as **explicitly verified completed/left** rather than implying every older legacy note has already been audited.
- Then cross-check against file statuses only as a secondary validation layer.

## Git workflow nuance
- Current cardiology workflow override: run `git add` / `git commit` / `git push` after **each completed cardiology change or update**.
- During a cardiology auto-push, stage the changed `Cardiology/` files plus the cardiology session-resume note if it was updated for continuity, while still excluding unrelated repo changes.
- Commit only the current cardiology batch; do not sweep unrelated repo modifications into the commit.
- Verify after push that cardiology-scoped status is clean with:
  - `git status --short -- Cardiology '00_Index/Cardiology Channel Session Resume 2026-05-06.md'`

## Honest Completion Rule (Critical)

**Never claim "batch complete", "MOC updated with ✅", "git done", or "full FCPS/MRCP note completed" until ALL of the following are true:**

1. The actual .md file has been written with write_file (or equivalent real write).
2. The file has been verified to exist on disk (read_file or ls succeeds).
3. The MOC/hierarchy has been updated with the real ✅ only after the file write is confirmed.
4. Git has been run and verified clean for the cardiology path.

**Pitfall — False Completion Claims**
- Repeatedly claiming completion without actual file writes destroys user trust.
- Users will explicitly correct this behavior ("unmark all that you mark as complete without write anything", "you just messed up every thing").
- When this happens, immediately stop all claims, clean the MOC of fake ✅ entries, and only resume real writes.
- Never treat "described the batch" as equivalent to "executed the batch".

**Stronger Rule — Never Stop Mid-Batch (Added 2026-06-05)**
- When the user says "fix all", "complete next N", "do all", or shows clear frustration with stopping midway ("why after 1 fix you stop", "you already stop"), the agent **must continue until the entire requested scope is finished**.
- Do not stop after 1–2 items and claim progress.
- If the batch is large, the agent may report incremental progress, but must not claim the batch is done until every item in the requested scope has been completed with real file writes.
- This pattern has been explicitly corrected multiple times in the same session. It is now a hard rule for cardiology topic production work.

---

## Comprehensive FCPS/MRCP Note Template (Validated 2026-06-10)

Each full note **must include all sections below** in order. No placeholders. Target ~15–25 KB per note.

### Frontmatter (required)
```yaml
---
tags: [medicine, cardiology, davidson, <topic-slug>, fcps, mrcp]
chapter: Cardiology
davidson_part: Part 3: Clinical Medicine
davidson_chapter: Chapter 16: Cardiology
heading: <Parent Heading>
topic_group: <Topic Group>
topic: <Topic Name>
status: full-fcps-mrcp-note
updated: YYYY-MM-DD
---
```

### Body sections (in order)
1. **Title + Related links** — Obsidian `[[wikilinks]]` to MOC, Hierarchy, Parent Heading, Topic Group, related core topics
2. **`> [!important]` callout** — One-sentence high-yield summary: why this topic matters for FCPS/MRCP, key exam traps, red flags
3. **Learning Objectives** — 4–5 measurable, exam-oriented bullets
4. **Definition** — Concise, exam-ready; include diagnostic criteria if applicable
5. **Anatomy / Embryology** (if applicable) — Key facts with exam relevance
6. **Physiology / Pathophysiology** — Mechanism in 4–5 numbered steps or structured explanation
7. **Classification / Etiology / Risk Factors** — Tables preferred
8. **Clinical Features** — Symptoms + Signs (with bedside pearls)
9. **Investigations** — Essential + Etiology-directed/Advanced
10. **Interpretation Frameworks** — Clinical recognition + ECG/Imaging/Hemodynamic patterns + Differential framework
11. **Diagnosis** — Criteria, gold standard, clinical judgment
12. **Differential Diagnosis** — Comparison table
13. **Management** — Immediate/Acute + Long-term/Chronic (with doses, targets, trial evidence) + Device/Procedural/Surgical indications + Special populations
14. **Drug Interactions / Contraindications / Comorbidity Cautions** — **Critical for FCPS/MRCP** — specific drug-disease and drug-drug interactions
15. **Procedures / Indications / Contraindications** — For key procedures (e.g., pericardiocentesis, thrombolysis, EPS, tilt table)
16. **Complications of Mismanagement** — What happens if you get it wrong
17. **Red Flags / Emergencies** — Immediate actions
18. **Prognosis** — Natural history, mortality, modifying factors
19. **Topic Correlation** — Links to related notes in vault
20. **Special Situations** — Pregnancy, elderly, CKD, post-COVID, etc.
21. **FCPS/MRCP High-Yield Points** — 8–12 bullet pearls
22. **Common Viva Questions** — 8–10 questions
23. **Common Confusions / Exam Traps** — 6–8 items
24. **Mnemonics** — 3–5 memorable aids
25. **Mind Map** — Text-based structure
26. **Suggested Visuals / Image Notes** — What diagrams would help
27. **Suggested Video References** — Search queries for review
28. **One-Page Revision Summary** — 8–12 high-yield bullets
29. **24-Hour Recall Prompts** — 5 active recall questions
30. **7-Day / 15-Day / 30-Day Revision Tracker** — Spaced repetition plan
31. **Must Know / Should Know / Nice to Know** — Tiered mastery
32. **My Weak Points** — Checklist for self-assessment
33. **Self-Test Scorecard** — 5 metrics /10 with interpretation bands
34. **Exam Answer Modes** — Footer marker

> **Note**: The basic `fcps-mrcp-template.md` in medical-folder-audit is a minimal scaffold. Use the **comprehensive template above** for actual topic upgrades.

---

## Batch Size Guidance (Validated 2026-06-10)

- **Optimal batch: 7–10 notes** per turn.
- Completing 7 notes (this session) took ~15 tool calls and stayed within token limits.
- Batches >10 risk stream timeouts on large write_file calls.
- If user says "next N", treat N as exact batch size.

---

## Hierarchy Update Pitfall & Fix (Added 2026-06-10)

**Problem**: The hierarchy file lists the same topic under multiple parents (e.g., Microvascular angina appears under "Chronic coronary syndromes and angina" AND under "Acute coronary syndromes and myocardial infarction"). Patch-based updates create duplicates.

**Fix**: **Rewrite the entire hierarchy file** with `write_file` after each batch, rather than patching. The hierarchy is small enough (<20 KB) to rewrite atomically. This guarantees no duplicates and consistent ✅ markers throughout.

---

## Three-File Update Protocol (Per Batch)

After writing all notes in a batch, update **all three** tracking files in one pass:
1. `Cardiology MOC.md` — Add ✅ entries in "Completed scaffold-to-full-note topics" section
2. `Davidson Chapter 16 - Cardiology Hierarchy.md` — Rewrite entire file with ✅ markers at every occurrence
3. `Cardiology Channel Session Resume 2026-05-06.md` — Update queue (mark completed, add new suggestions)

Then run **single git add/commit/push** for the whole batch.
