---
name: medical-chapter-study-pack
description: "Use when preparing structured exam-oriented chapter notes for a medical subject such as nephrology, respiratory medicine, neurology, cardiology, or gastroenterology. Produces elaborate editable Markdown notes with anatomy, physiology, clinical discussion, MCQs, SBAs, and flashcards, and supports chapter-specific rule overrides."
version: 1.3.1
author: Hermes Agent
license: MIT
metadata:
  hermes:
    tags: [medical-education, exam-prep, markdown, fcps, mrcp, study-notes]
    related_skills: [hermes-agent]
---

## Reference Files

- `references/fcps-mrcp-note-template.md` — Validated full note template structure (Cardiology 111, Rheumatology 10)
- `references/chapter-scaffold-system.md` — Chapter scaffold system: MOC, hierarchy, hubs, scaffolds, git workflow
- `references/davidson-chapter-mapping.md` — Davidson chapter mapping process and validation checklist
- `references/chapter-15-completion-workflow.md` — Chapter 15 (Nephrology and Urology) completion workflow and validation process
- `references/file-size-guidelines.md` — File size guidelines and content structure standards for FCPS/MRCP topic files
- `references/deep-vault-progress-tracking.md` — Progress counting methodology across multiple vaults/progress sources
- `references/davidson-chapter5-population-epidemiology-pattern.md` — Complete Davidson 24e Chapter 5 (Population Health & Epidemiology) scaffold pattern: 27 topic files, MOC, hierarchy, template, file naming, frontmatter standards, FCPS/MRCP content structure, priority distribution

# Medical Chapter Study Pack

## Overview

This skill is for building **exam-oriented medical chapter notes** for subjects such as **nephrology, respiratory medicine, neurology**, and similar areas. The output should be **elaborate, structured from A to Z, and editable as Markdown (`.md`)** whenever possible.

The writing style should be useful for **FCPS and MRCP** preparation unless the user specifies another exam style. Prioritize the user's preferred references when they are provided. If chapter-specific rules are given, follow them for that chapter and treat them as overrides of the generic structure.

## When to Use

Use this skill when the user asks for:
- full chapter notes on a medical topic
- topic summaries in Markdown
- exam-oriented notes for FCPS / MRCP
- anatomy + physiology + pathology + management in one package
- practice questions after a topic
- flashcards for revision
- a reusable structure that can be adapted to a specific system (renal, respiratory, neuro, etc.)

Do not use this skill for:
- non-medical topics
- management decisions for a real emergency patient without clear clinical framing
- one-line fact lookup when the user does not want a chapter-style note

## Default Output Standard

Unless the user requests otherwise, prepare the topic in **Markdown** using this structure.

Default assumptions when file output is requested:
- Notes may be saved as real `.md` files, not just shown in chat
- The user may choose a **custom root directory** such as `/mnt/tb/Medicine`
- Create **chapter/system folders automatically** when useful
- Prefer **Obsidian-friendly Markdown** when the user wants vault-style notes
- Support optional **Git/GitHub workflows** for versioning and backup

When file output is requested, prefer a structure like:

```text
<root>/
├── 00_Index/
│   └── Medicine MOC.md
├── Nephrology/
│   ├── Nephrology MOC.md
│   ├── AKI.md
│   └── CKD.md
├── Respiratory/
│   ├── Respiratory MOC.md
│   ├── Asthma.md
│   └── COPD.md
└── Neurology/
    ├── Neurology MOC.md
    ├── Stroke.md
    └── Epilepsy.md
```

Unless the user requests otherwise, prepare the topic in **Markdown** using this structure:

```md
# Topic Name

## Learning Objectives
## Definition
## Core Anatomy
## Core Physiology
## Normal Values / Important Cut-offs
## Classification
## Etiology / Causes
## Risk Factors
## Pathophysiology
## Clinical Features
## Approach / Algorithm
## Investigations
## Interpretation Frameworks
## Diagnosis
## Differential Diagnosis
## Tables / Comparison Charts
## Management
## Drug Interactions / Contraindications / Comorbidity Cautions
## Procedures / Indications / Contraindications
## Procedure Mini-Sections
## Complications
## Red Flags / Emergencies
## Prognosis
## Topic Correlation
## Special Situations
## FCPS/MRCP High-Yield Points
## Common Viva Questions
## Common Confusions / Exam Traps
## Mnemonics
## Mind Map
## Flowchart
## Suggested Visuals / Image Notes
## Suggested Video References
## One-Page Revision Summary
## 24-Hour Recall Prompts
## 7-Day / 15-Day / 30-Day Revision Tracker
## Must Know / Should Know / Nice to Know
## My Weak Points
## Self-Test Scorecard
## Exam Answer Modes
## Summary

## MCQs (10)
## SBA Questions (10)
## Flashcards
## Answer Key with Explanations
```

## Obsidian-Friendly Notes Mode

When the user wants Obsidian-friendly notes, prefer:

- clean Markdown headings
- note-per-topic organization
- chapter-level MOC/index notes
- `[[Wikilinks]]` to related topics
- tags such as `#medicine #nephrology #AKI`
- callouts such as:
  ```md
  > [!important]
  > Key exam or clinical point.
  ```
- Mermaid blocks for flowcharts, mind maps, and simple concept diagrams when useful
- related-topic sections like:
  ```md
  Related: [[CKD]], [[Hyperkalemia]], [[Acid-Base Disorders]]
  ```

When appropriate, make notes graph-view friendly by linking related disease, physiology, investigation, and management topics.

## File and Folder Rules

When the user requests actual files:

1. Ask for or infer the **root save location** only if it materially affects file creation.
2. Support custom locations such as `/mnt/tb/Medicine`.
3. Create **chapter folders** automatically, e.g. `Nephrology`, `Respiratory`, `Neurology`.

---

See `references/session-learnings-2025-06.md` for detailed session learnings (Infectious Disease/STI/HIV completion, June 2025).
4. Create **MOC/index notes** when useful for navigation.
5. Create a **Templates/** folder when the user wants reusable note skeletons.
6. Use readable filenames such as `AKI.md`, `CKD.md`, `Nephrotic Syndrome.md` unless the user wants a numbering convention.
7. If editing an existing vault or repo, preserve the existing naming and folder conventions.
8. In chapter channels marked for **actual topic production**, do **not** stop at chat output alone: create or update the real topic `.md` note in the chapter folder.
9. When creating a first or major topic note for a chapter, check the chapter **MOC/index** and update it if needed (for example: add the note link, mark it created, or update simple task/progress checkboxes already present).
10. Keep chapter-topic notes **Obsidian-friendly** by default when the vault is described that way: clean headings, wikilinks, simple frontmatter if the vault uses it, and readable filenames.
11. If the user says to do Git work for that task, run the full requested repo workflow after file changes (typically `git add`, `git commit`, and `git push`). If Git work is not explicitly requested, treat it as optional side-effect work rather than automatic unless that chapter has an established chapter-specific override saying to push after every completed change or batch.

### Actual Topic Production in a Live Vault

When the user says a chapter/topic channel should produce the **real note file**, do not stop at chat output. Treat the file update as part of the core deliverable.

Preferred workflow:
1. Inspect the target chapter folder and existing note names first.
2. Reuse the established clean topic filename if a starter note already exists; otherwise create a clean topic filename in the chapter folder.
3. Write or replace the topic note as a real `.md` file using **Obsidian-friendly structure** and wikilinks.
4. Update the chapter **MOC/index** when needed so the new or expanded topic is visible from navigation notes.
5. If the vault is also a Git repo and the user asks for it, run the Git workflow too: `git add`, `git commit`, and `git push`.

### True Disease-Level Chapter Scaffold Mode

When the user asks for **all topics in a chapter**, or explicitly asks for a hierarchy like:
- `chapter > heading > topic > small topic`
- `chapter > subheading > disease`
- `true disease-level files`

then do **not** stop at a flat chapter MOC or a single list note.

Preferred hierarchy workflow:
1. Validate the chapter boundary first (especially for Davidson-based study plans).
2. Build or update a chapter hierarchy note that maps:
   - chapter
   - heading
   - topic group
   - disease-level / small-topic files
3. Create a **heading hub note** for each major heading.
4. Create a **topic-group hub note** under each heading when the heading contains multiple diseases/subtopics.
5. Create **separate disease-level `.md` files** for the small topics under that heading/topic group.
6. Update the chapter **MOC** so it navigates the hierarchy clearly, rather than showing only a flat list.
7. If the user wants this behavior generalized, update the governing skill/rules so future chapters follow the same scaffold logic.

Recommended folder shape:

```text
<Chapter>/
├── <Chapter> MOC.md
├── <Chapter Hierarchy>.md
├── <Heading A>.md                     # heading hub
├── <Heading A>/
│   ├── <Topic Group 1>.md            # topic-group hub
│   ├── <Disease 1>.md
│   ├── <Disease 2>.md
│   └── <Disease 3>.md
├── <Heading B>.md
├── <Heading B>/
│   ├── <Topic Group 2>.md
│   ├── <Disease 4>.md
│   └── <Disease 5>.md
```

Important rules for this mode:
- Keep filenames readable and topic-specific.
- Preserve strict chapter boundaries when the user asks for Davidson alignment.
- Treat each disease-level file as the unit to upgrade later into a full FCPS/MRCP note.
- Update the MOC and hierarchy note after bulk scaffold generation so navigation stays usable.
- When the user later asks for a **must-know full-note batch** (for example, "first 10 must-know Neurology disease files"), first map the requested exam topics onto the **existing scaffold filenames already present in the vault** rather than inventing new parallel note names. If the exact requested label does not exist, choose the nearest existing disease-level scaffold that best represents the requested exam topic inside the validated chapter boundary, then make that mapping explicit in the MOC or task summary.
- During batch conversion, prefer upgrading the existing scaffold files in place and then update the chapter MOC so the completed batch is clearly visible with completion markers (for example `✅ full FCPS/MRCP note completed`).

Important details:
- When the user points to a chapter-specific **session resume** note (for example `00_Index/<Chapter> Channel Session Resume <date>.md`) and says to use it as the current setup, treat that resume as the workflow authority for the session **but reconcile it with the current live chapter MOC before choosing the next topics**. Resume notes may lag behind newer completions already recorded in the MOC.
- In that situation, preferred continuation workflow is: (1) read the resume note, (2) read the current chapter MOC, (3) compare the resume queue against already-completed `✅` full-note entries, (4) select the next remaining scaffold files still pending, and (5) update the MOC status marker/count language to match the new completion milestone (for example `first-15-must-know-full-notes-completed`) after the batch is written.
- In a nephrology vault rooted at `/mnt/tb/Medicine`, actual topic production should normally land in `/mnt/tb/Medicine/Nephrology/`.
- In this user's nephrology vault flow, repeated chapter-topic production should upgrade the existing starter note in place, annotate `Nephrology MOC.md` with `✅ full FCPS/MRCP topic note` once expanded, and update the relevant nephrology topic-group hub and chapter hierarchy note when those navigation layers expose the same topic.
- When the user points nephrology work to `00_Index/Nephrology Channel Session Resume <date>.md` as the active setup, use it together with the live `Nephrology MOC.md` to select the next scaffold topic, then after the batch update the resume note itself to reflect completion state and refresh the recommended safe next command so the next Discord restart can continue cleanly.
- For nephrology continuation prompts like `next 1`, `next 2`, or similar, treat the requested number as an exact batch size: inspect the live `Nephrology MOC.md` plus the active nephrology session-resume note, select the next uncompleted disease-level scaffold files already present in the hierarchy, and upgrade exactly that many files in place rather than widening the batch.
- If the user also imposes a **minimal-read nephrology workflow** such as `read only Nephrology MOC + target note + maximum 1 directly relevant hub`, treat it as a hard task-level constraint for writing work. When the user says `next N` without naming the target files, use the live `Nephrology MOC.md` together with the active nephrology session-resume note only to identify the next exact target(s), then read exactly those target note files plus at most one directly relevant hub for navigation/update. Do not broaden into extra nephrology files once the targets are known.
- Under that same nephrology minimal-read rule, after writing, update only the target note files, `Nephrology MOC.md`, and that same one relevant hub if needed; if confident topic selection or completion would require reading beyond this working set, stop and ask instead of silently widening scope.
- If an exact nephrology `next N` request cannot be satisfied from the current visible one-hub sequence, say so plainly and give the exact visible remainder rather than guessing. Offer the smaller same-hub batch or ask for explicit wider-scope permission.
- Once the user explicitly widens nephrology scope for that continuation run, use the nephrology session-resume note plus the live hierarchy/MOC to pull the exact next batch in sequence, but keep the work orderly: prefer a coherent same-heading mini-run around the recommended next scaffold when one is obvious, and after writing update only the MOC plus the directly touched hubs/navigation files needed for that widened batch.
- If nephrology channel rules say to run git after **every** completed nephrology change or batch, treat that as an ongoing chapter override rather than waiting for a per-turn reminder. In that mode, path-stage all nephrology files changed in the batch, plus the nephrology session-resume note if it was updated for continuity, then commit and push without re-asking while still excluding unrelated repo changes.
- After an automatic nephrology push, verify both outcomes before closing the batch: (1) the push succeeded to the expected branch/remote, and (2) `git status --short -- Nephrology 00_Index/'Nephrology Channel Session Resume <date>.md'` is clean so no nephrology continuity edits were left behind unintentionally.
- When reporting nephrology progress, do **not** count only files with `status: complete-topic-note`; this vault may also contain older completed root-level topic notes still marked `status: full-note`. Prefer the live `Nephrology MOC.md` completion markers as the primary source of truth, then cross-check against file statuses (`complete-topic-note` plus legacy `full-note`) before reporting completed vs remaining counts.
- In this nephrology vault, the completed count should include **both**: (1) preserved root-level core notes already marked complete in the `## Preserved Root-Level Core Notes` section of `Nephrology MOC.md`, and (2) upgraded disease-level queue/topic entries marked `✅ full FCPS/MRCP topic note`. Do not undercount by looking only at the numbered conversion queue.
- If nephrology progress counts differ between the hierarchy reference total and the unique real topic-file total, explain the difference explicitly instead of collapsing them into one number. In this user's vault, the hierarchy may reference topics more broadly than the set of unique currently upgradable topic files; for practical completion reporting, present the **unique actual topic-file total** as the working denominator and label the hierarchy-reference count separately.
- In this user's respiratory vault flow, actual topic production normally lands in `/mnt/tb/Medicine/Respiratory/` and upgrades the existing starter note in place when present.
- When the user points respiratory work to `00_Index/Respiratory Channel Session Resume <date>.md` as the active setup, use it together with the live `Respiratory MOC.md` to select the next scaffold topic, then after the batch update the resume note itself to reflect completion state (for example mark the finished queue item and refresh the recommended safe next command) so the next Discord restart can continue cleanly.
- For respiratory continuation prompts like `next 1`, `next 2`, or similar, treat the requested number as an exact batch size: inspect the live `Respiratory MOC.md` plus the active respiratory session-resume note, select the next uncompleted disease-level scaffold files already present in the hierarchy, and upgrade exactly that many files in place rather than widening the batch.
- In respiratory batch conversion work, update navigation at both levels after promoting a scaffold note: (1) mark the completed item in `Respiratory MOC.md`, and (2) mark the corresponding link in the relevant topic-group hub and, when useful, the chapter hierarchy file so completion is visible from navigation rather than only from the topic file.
- If respiratory channel rules say to run git after every completed respiratory batch, treat that as an ongoing chapter override rather than waiting for a per-turn reminder. In that mode, stage the respiratory files changed in the batch plus the respiratory session-resume note if it was updated, commit and push without re-asking, then verify both outcomes before closing the batch: (1) the push succeeded to the expected branch/remote, and (2) `git status --short -- Respiratory 00_Index/'Respiratory Channel Session Resume <date>.md'` is clean so no respiratory continuity edits were left behind unintentionally.
- When reporting respiratory progress, use the live `Respiratory MOC.md` as the source of truth for the total disease-level topic count, and cross-check completed full topics against note status markers such as `status: full-note` so the completed-versus-left count reflects full upgraded notes rather than scaffold files.
- For short user prompts like `how many complete and left topic in respiratory`, prefer a concise progress reply that gives exactly: **total topics**, **completed full topics**, and **left topics**. Recompute `left = total - completed` from the live counts at reply time rather than relying on older session summaries.
- After a respiratory push, explicitly mention any unrelated non-respiratory modified files that remain untouched so repo scope is clear.
- In this user's cardiology vault flow, actual topic production normally lands in `/mnt/tb/Medicine/Cardiology/` and must stay strictly within **Davidson Chapter 16: Cardiology**.
- In cardiology topic production, use the source split: **Gray's + Davidson** for anatomy, **Guyton & Hall + Ganong + Davidson** for physiology, and **Davidson + PasTest + personal notes** for clinical cardiology.
- Cardiology full-note output should emphasize **ECG interpretation, ACS / ischemia logic, heart-failure and hemodynamic profiling, murmur/valve clues, syncope/shock differentiation, red flags, one-page summary, 10 MCQs, 10 SBAs, flashcards, and answer explanations**.
- In this user's gastroenterology vault flow, actual topic production normally lands in `/mnt/tb/Medicine/Gastroenterology/` and must stay strictly within **Davidson Chapter 23: Gastroenterology**, with **Hepatology kept separate as Davidson Chapter 24**.
- For Gastroenterology chapter scaffolding in this vault, keep luminal GI disease, GI bleeding, endoscopy/investigation, small-bowel malabsorption, IBD/functional bowel disease, lower GI/colorectal disease, and pancreatic disease in Gastroenterology; move hepatitis, cirrhosis, portal hypertension, jaundice/LFT interpretation, ascites, hepatic encephalopathy, and liver failure to Hepatology.
- When the user asks for the **best** or **true disease-level** Gastroenterology scaffold rather than a minimal shell, prefer a validated hierarchy centered on these heading domains: symptom-pattern approach, endoscopy/investigations, oesophageal disorders, stomach/duodenum, upper GI bleeding, small-bowel malabsorption/coeliac disease, inflammatory/functional bowel disorders, lower GI/colorectal disease, and pancreatic disorders.
- During a strict Davidson Gastroenterology validation/refinement pass, use the live vault roadmap/MOC first, then public searchable snippets only as a **public-snippet validation/refinement pass** rather than claiming a verbatim licensed-table-of-contents extraction.
- When building Gastroenterology for Discord continuation, also create or refresh the chapter pinned-message note and a chapter session-resume note so continuation is operational instead of leaving only the scaffold files.
- Under a strict Gastroenterology **minimal-read** rule (`Gastroenterology MOC.md` + exact target note + max 1 directly relevant hub), treat that as a hard task constraint for writing work. Do not inspect extra Gastroenterology files, hierarchy notes, or unrelated chapter notes unless the user explicitly widens scope.
- For Gastroenterology continuation prompts like `next 1`, `next 3`, `next 5`, or `next 10`, treat the requested number as an **exact batch size**. Use the live `Gastroenterology MOC.md` to identify the next visible pending topic sequence, then read exactly those target note files plus only the directly relevant hub(s) needed for navigation updates.
- If the next visible Gastroenterology `N` topics cross more than one hub and the current turn still carries the **max 1 hub** minimal-read restriction, stop and ask before widening scope. Do not silently cross into multiple hubs just to satisfy `next N`.
- If the user then clarifies with a scope-widening reply (for example confirming they want the `5 topic` batch rather than only the next single-hub subset), treat that as permission for that turn to complete the exact requested batch across the necessary hubs.
- After that explicit gastro scope-widening approval (for example `do next 4`), proceed immediately without another clarification loop: read the exact target notes plus only the directly touched hubs needed for that widened batch, then complete exactly that batch size.
- If the user later gives a larger bare continuation prompt again (for example `do next 10`) after already granting cross-hub continuation in the same active gastro sequence, continue in visible order across the directly touched hubs needed to satisfy the new exact batch size instead of reopening the same clarification loop.
- In that resumed cross-hub mode, exhaust the current visible topic-group/heading sequence first, then continue into the next visible heading in order from the MOC/hub chain. Do not jump arbitrarily across Gastroenterology headings.
- In this user's nephrology continuation flow, if the user gives a bare prompt like `next 5` after a prior nephrology batch and the active resume note already names the next scaffold, use the live `Nephrology MOC.md` + nephrology session-resume note + hierarchy to pull the next exact batch in sequence, but prefer a **coherent same-heading mini-run** around that recommended next scaffold when the nearby pending topics are clearly grouped (for example a glomerular diseases cluster). Do not satisfy `next 5` by scattering across unrelated headings if an obvious local run exists.
- After a nephrology batch selected this way, refresh the nephrology session-resume note with the new explicit completed count, the batch date, the exact completed filenames, and the next recommended single-file scaffold so the next Discord restart can resume without re-deriving the queue.
- When patching nephrology hierarchy/navigation files after a glomerular or mixed nephrology batch, use **unique anchored context blocks** rather than short repeated link lines, because the hierarchy may contain the same topic names in more than one section and broad replacements can fail or hit the wrong block.
- If the live Gastroenterology MOC no longer shows enough visible pending items to satisfy the user's exact `next N` request, do not stop at `list only` or ask again if the user has already widened scope. Continue by reading the current active heading hub and, if needed, the next directly relevant heading hub(s) to extend the queue in-order before moving elsewhere.
- In that gastro continuation case, prefer finishing the current heading's visible sequence first (for example continuing the active pancreatic run after `Acute pancreatitis`) so the exact `next N` stays orderly and chapter-local rather than jumping arbitrarily across headings.
- In Gastroenterology batch conversion work, after upgrading the target scaffold files in place, update `Gastroenterology MOC.md` and mark the same topics `✅` in each directly touched relevant hub so completion is visible from navigation.
- After a gastro batch that spans more than one heading hub, verify all touched hubs explicitly with a quick re-read or status-count check before git work so the exact requested batch size, hub checkmarks, and MOC entries stay aligned.
- When patching `Gastroenterology MOC.md` after a mixed-hub batch, use hub-specific unique anchor context for insertions into the completed lists rather than a broad nearby completed-topic block. Reusing an anchor that already contains duplicated hub items can accidentally insert the new lines twice.
- If a Gastroenterology MOC patch produces unexpected duplicate completed entries, immediately re-read the affected MOC region, remove only the duplicate lines, and then re-verify chapter totals from real file-status searches rather than assuming the navigation list is authoritative.
- See `references/gastroenterology-moc-patching-pitfalls.md` for the duplicate-insertion failure mode and recovery pattern.

- For this user's Gastroenterology chapter flow, use the source split: **Gray's + Davidson** for anatomy, **Guyton & Hall + Ganong + Davidson** for physiology, and **Davidson + PasTest + personal notes** for clinical discussion.
- Gastroenterology full-note output should emphasize **dysphagia and alarm features, dyspepsia / *H. pylori* / peptic-ulcer logic, upper-GI bleeding severity and resuscitation logic, chronic diarrhoea / malabsorption / coeliac differentiation, IBD vs IBS vs infective bowel disease differentiation, colorectal cancer clues and lower-GI bleeding logic, pancreatitis severity / complications / red flags, and common exam/viva traps** when relevant to the topic.
- If the Gastroenterology channel rules say to push after every completed batch or change, treat that as an ongoing chapter override rather than waiting for a per-turn reminder. In that mode, path-stage only the changed `Gastroenterology/` files (plus any intentionally updated gastro continuity/rule files), commit with a gastro-specific message, push, and verify `git status --short -- Gastroenterology` is clean before closing the batch.
- When reporting Gastroenterology chapter progress, do **not** count raw `✅` links in `Gastroenterology MOC.md` as unique completed topics. The same topic may appear in more than one MOC section (for example both a conversion queue and a completed list), so link counts can overstate progress. Prefer counting real topic files by frontmatter status across the chapter tree (for example `status: full-fcps-mrcp-topic-note` versus `status: scaffold`) and present the MOC `✅` count, if mentioned at all, only as a non-unique navigation marker count.
- Before changing Gastroenterology chapter-level status text to a completion state (for example `first-pass-full-note-complete`) or claiming `N / N` done, verify that whole-tree scaffold searches under the chapter return zero remaining disease-level scaffold files. If scaffold files remain, keep the MOC summary in a partial-completion state and report the true completed-versus-left counts from file statuses.
- See `references/gastroenterology-progress-counting.md` for the proven pitfall and counting workflow.
- When the user points to `00_Index/Cardiology Channel Session Resume <date>.md` as the active setup, use the resume together with the live `Cardiology MOC.md` before selecting the next topic, then refresh the resume note after the batch so the queue, restart prompt, and recommended safe next command stay current.

- In cardiology batch conversion work, update both navigation layers after upgrading scaffold notes in place: (1) append the completed notes in `Cardiology MOC.md`, and (2) mark the corresponding links with `✅` in the relevant topic-group hubs and chapter hierarchy so completion is visible from navigation.
- If cardiology channel rules say to run git after **every** completed cardiology change or update, treat that as an ongoing chapter override rather than waiting for a per-turn reminder. In that mode, path-stage all cardiology files changed in the batch, plus the cardiology session-resume note if it was updated for continuity, then commit and push without re-asking while still excluding unrelated repo changes.
- After an automatic cardiology push, verify both outcomes before closing the batch: (1) the push succeeded to the expected branch/remote, and (2) `git status --short -- Cardiology 00_Index/'Cardiology Channel Session Resume <date>.md'` is clean so no cardiology continuity edits were left behind unintentionally.
- In this user's neurology vault flow, actual topic production normally lands in `/mnt/tb/Medicine/Neurology/` and must stay strictly within **Davidson Chapter 28: Neurology**. Treat **Stroke** as excluded and belonging to the separate Stroke Medicine chapter/folder.
- In the neurology vault, when the user points to `00_Index/Neurology Channel Session Resume <date>.md` as the setup baseline, use it for sequencing but reconcile it against the current live `Neurology MOC.md` before selecting the next topics because completed counts may have advanced beyond the resume.
- Treat the neurology session-resume note as a **strong continuity layer**, not a throwaway note. For this user, the best continuity stack is: **live MOC = source of truth**, **heading hubs = navigation truth**, **session-resume note = restart checkpoint**, **memory = durable preferences only**.
- If the user says to "retrieve/see previous setup" or references a broken/hung prior Discord session, recover continuity actively instead of asking the user to restate everything: read the cited chapter session-resume note, use session search to recover prior chapter-specific decisions/queues when available, then cross-check the live chapter MOC and heading hubs before acting.
- When the user asks for stronger restart reliability or asks whether a new session will remember the setup, prefer updating the neurology session-resume note itself with: current counts, latest meaningful milestone, latest pushed commit when known, exact next queue, exact next-1 recommendation, and short restart prompts such as `Use current Neurology MOC + session resume and do next 3.`
- After a meaningful neurology batch or milestone change, refresh the session-resume note if its queue, counts, or restart prompt has become stale. This note should be maintained as an operational checkpoint, not left frozen at the original first-session state.
- When refreshing the neurology session-resume note, also update the commit reference block so it does not advertise a stale pre-batch commit after a newer neurology push has succeeded.
- If the resume note itself is edited **after** the main batch push and that edit requires its own follow-up commit, avoid ambiguity: record the **primary batch content commit/message** for the topic-content batch in the session-resume note, rather than silently replacing it with a later metadata-only resume-refresh commit. If useful, mention the current repo HEAD separately in chat.
- Practical neurology push pattern: if the resume note needs the real pushed commit hash/message but those values are only known after the main content push succeeds, it is acceptable to (1) push the main neurology content batch first, (2) patch the resume note to replace any temporary `pending current batch push` placeholders with the actual primary content commit/message, then (3) make a small resume-only follow-up commit/push and re-verify clean neurology status.
- For neurology `next 2` / `next 3` continuation prompts, prefer staying in the same heading or topic-group when possible, but still satisfy the **exact batch size** even if the current mini-sequence has only one obvious file left. In that case, finish the last file in the current sequence, then continue immediately to the next pending scaffold in the same heading before stopping.
- If the user gives a chapter-channel governance message for neurology (sources, scope, output structure, file location, git behavior, or chapter exclusions), treat it as an operational chapter override, not just chat content: fold it into the working rules for the batch, keep Stroke excluded, and ensure the live vault workflow reflects those constraints.
- If the user names an exact neurology target file and says to upgrade **only the first file** or otherwise narrows scope to one file, treat that file as the whole batch. Do not widen the task to the rest of the queue. Update only the directly related navigation notes that need the completion reflected, typically `Neurology MOC.md` and the relevant heading hub if its completion markers are used.
- In neurology batch conversion work, update both navigation layers after upgrading scaffold notes in place: (1) append the completed notes and milestone marker in `Neurology MOC.md`, and (2) mark the corresponding links with `✅` in the relevant heading hub notes (for example `Epilepsy.md`, `Meningitis.md`, `Neuroimaging.md`) so completion is visible from chapter navigation.
- When reporting neurology progress after a batch, use the live `Neurology MOC.md` as the source of truth. Prefer counting completed topics from the explicit completed-entry list — in this user's vault the reliable pattern is completed lines beginning with `- ✅ [[` — rather than inferring counts from file status fields or older regex assumptions.
- For neurology continuation prompts like `next 3`, `next 5`, or similar, treat the requested number as an exact batch size: inspect the current MOC plus relevant heading hubs, select the next uncompleted disease-level scaffold files already present in the hierarchy, upgrade exactly that many notes in place, then update navigation and counts before reporting back.
- If the user explicitly imposes a **minimal-read neurology workflow** such as `Read only Neurology MOC + the target note + at most 1 directly relevant hub`, treat it as a hard task-level operating constraint. Do not inspect extra neurology files, hierarchy notes, or resume notes for that turn.
- Under that minimal-read neurology rule, allowed working set for a targeted upgrade is: `Neurology MOC.md`, the target disease-level note, and at most one directly relevant heading/topic-group hub; after writing, update only `Neurology MOC.md` and that same hub if needed, then do neurology-only path-scoped git add/commit/push if the standing chapter rule requires git.
- Under that same minimal-read rule, if the user asks to `complete next N` without naming the files, use the live `Neurology MOC.md` plus at most one directly relevant heading hub to identify the next visible consecutive pending topics, keep the batch within that single hub sequence, and stop to ask for more context rather than widening the read scope if confident selection or writing would require additional files.
- When the user explicitly says `Do not git push` for the current neurology continuation, treat that as a task-level override even if a broader chapter git habit exists. Finish the note/MOC work and stop short of push.
- If the user upgrades the neurology git workflow from "push only when explicitly asked" to an ongoing rule like "always git push after complete or change of neurology," treat that as a chapter-specific override for future neurology batches. After each completed neurology batch, stage the Neurology path changes, commit with a batch-specific message, and push to the current branch/remote without re-asking.

### Acute Medicine (Davidson Chapter 9) — Chapter-Specific Rules
When working in `/mnt/tb/Medicine/Acute Medicine and Critical Illness/`:

- **Topic character**: Focus on syndromes and time-critical approaches (ABCDE, shock types, sepsis bundles, acute respiratory failure, altered consciousness, ICU triggers) rather than single diseases.
- **Source split** (when expanding):
  - Clinical discussion → Davidson + PasTest + local critical care notes
  - Algorithms & red flags → Prioritize clear escalation criteria and early warning scores
- **First-pass priority topics**: ABCDE approach, Shock (all types), Sepsis & Septic Shock, Acute Respiratory Failure / NIV, Coma & Altered Consciousness.
- **MOC & hierarchy**: Keep the MOC lean. Use a short "Starter Topic Queue" + "Key Linked Topics" section rather than a full multi-heading hierarchy (unlike organ-based chapters).
- **Progress reporting**: Count completed full FCPS/MRCP notes from explicit `✅` markers in the MOC. Do not over-count because most topics are approach-based rather than disease files.
- **Git rule**: Follow the same "git after every completed batch" pattern as other chapters unless the user overrides for this channel.
- **Template**: Always use `Templates/Acute Medicine and Critical Illness Topic Template.md` as the base.
- When such a neurology auto-push override exists, stage the full currently pending `Neurology/` path for that batch before commit, rather than only the newly written topic files, because the MOC and heading-hub updates are part of the deliverable and earlier same-session neurology edits may still be pending.
- After an automatic neurology push, verify both outcomes before closing the batch: (1) the push succeeded to the expected branch/remote, and (2) `git status --short -- Neurology` is clean so no chapter changes were left behind unintentionally.

- When you add one of these rapid-revision companions, update `Respiratory MOC.md` with a small `## Rapid Revision Sheets` section or add the new link under that section if it already exists.
- When the user asks for the **best** or **true disease-level** Respiratory scaffold system rather than a safe first-pass scaffold, do not stop at a minimal chapter shell. Prefer a fuller hierarchy that preserves existing root-level core notes but expands additional heading/topic-group coverage such as: upper airway and sleep-related breathing disorders, symptom-approach files, physiology/investigation mini-topics, pleural subtypes, pulmonary vascular subtopics, ILD/environmental subtypes, ventilatory support escalation, and thoracic malignancy subtypes.
- For this fuller Respiratory scaffold pass, verify the result explicitly by recounting heading hubs, topic-group hubs, disease-level topics, and total markdown files, then update all navigation/control notes that depend on those counts: `Respiratory MOC.md`, the chapter hierarchy file, the chapter session-resume note, `00_Index/Davidson Chapter Progress Tracker.md`, and the Respiratory summary block in `00_Index/Medicine MOC.md`.
- If both `AKI.md` and a longer natural-language filename are plausible, preserve the repo's existing convention rather than inventing a new duplicate note.
- When a starter template note already exists, upgrade that file in place instead of creating a parallel duplicate.
- When updating the MOC, mark clearly when a topic has been expanded into a full FCPS/MRCP note if that helps navigation.
- If the user explicitly requests chat output **and** file creation, deliver both.

Recommended reusable templates include:
- `Templates/Generic Topic Template.md`
- `Templates/Nephrology Topic Template.md`
- `Templates/Respiratory Topic Template.md`
- `Templates/Neurology Topic Template.md`
- Davidson-aligned chapter templates for the broader medicine roadmap when the user is organizing study chapter-by-chapter.

Recommended control/index notes include:
- `00_Index/Medicine MOC.md`
- `00_Index/Davidson Chapter Roadmap.md`
- `00_Index/Davidson Chapter Progress Tracker.md`
- `00_Index/Weekly Study Dashboard.md`
- `00_Index/All System Rules.md`
- `00_Index/Medicine Chapter Channel Plan.md`
- `00_Index/Chapter Rules Index.md`
- `00_Index/Chapter-Specific Rule Template.md`
- `00_Index/Chapter Rules/<Chapter> Channel Rules.md` for filled chapter-specific rule packs

When the user is organizing study work across Discord channels, treat the system/index channel separately from chapter channels:
- use the index/system channel for skill edits, rule updates, exports, and vault maintenance
- use chapter channels for topic-specific study, chapter-specific source rules, MCQ/SBA expansion, and note development
- when a chapter channel's preferences stabilize, preserve them as chapter-specific override rules
- when the user creates a new chapter channel and asks how to start it, provide a **channel kickoff message** that acts like a pinned mini-constitution for that chapter
- the kickoff message should usually include: channel purpose, exam target, source hierarchy, required output structure, question requirements (e.g. 10 MCQs + 10 SBAs), formatting rules, separation from `#index`, a `First topic:` line, and a file workflow clause when the user expects vault output
- prefer giving both: (a) a full pinned-message version and (b) a short ready-to-post version
- when the user expects actual topic production beyond chat, explicitly add a **File and Git Workflow** rule to the kickoff message: create/update the real `.md` file in the correct chapter folder under the user's vault root, keep filenames clean, update the chapter MOC/index if needed, and only run git add/commit/push when the user explicitly requests repo update side effects
- when the user says work should **continue in a Discord chapter channel**, make the pinned/kickoff message operational rather than descriptive: tell the channel to continue the remaining disease/topic queue from the chapter MOC/hierarchy, upgrade files **in place**, update the chapter MOC after each completed topic or batch, and if the user asked for repo syncing, add an explicit instruction to **git commit + push the chapter-related files after each completed batch/session**
- when the user says work should **continue in a Discord chapter channel**, make the pinned/kickoff message operational rather than descriptive: tell the channel to continue the remaining disease/topic queue from the chapter MOC/hierarchy, upgrade files **in place**, update the chapter MOC after each completed topic or batch, and if the user asked for repo syncing, add an explicit instruction to **git commit + push the chapter-related files after each completed batch/session**
- when the user then gives short operational prompts like **"next 2"**, **"start next 2"**, or **"next 3"** in a live chapter channel, interpret them as: inspect the current chapter MOC plus relevant heading hubs, choose the next logical uncompleted disease-level topics already present in the scaffold, upgrade exactly that many files in place, mark them `✅ full-note` in the heading hubs and MOC, then perform the chapter-scoped git workflow if that channel's rules require it
- **Batch-size verification rule:** in these `next N` chapter-channel turns, verify both before and after writing that the number of upgraded disease-level files is **exactly N**. Do not overrun the requested batch size just because adjacent topics are available in the same topic group. When reporting completion, recount the exact files changed in the batch so the chat summary, MOC updates, and git commit all reflect the same N-topic scope.
- If a chapter-channel run is **interrupted mid-turn** before writing or pushing, explicitly distinguish **inspection-only progress** from actual file changes before resuming or reporting. Check the relevant chapter path with `git status --short -- <Chapter>` and say clearly whether notes were merely read/selected or whether files were actually modified/committed.
- In this interruption-recovery case, do not imply the batch was completed just because the next topics were already identified; confirm whether the chapter files are still clean or whether partial edits exist, then either resume the batch or report that nothing substantive was changed.
- in this batch-conversion mode, prefer staying within the same heading/topic-group when there is an obvious unfinished sequence (for example several remaining reperfusion files in a row), but use the current MOC/hubs as the source of truth rather than inventing a new queue in chat
- if you patch the MOC after using a partial/paginated file read, re-read the full MOC before final verification so the updated completion list and queue are grounded in the current file contents
- if the chapter is nephrology, explicitly include the nephrology source split: Gray's + Davidson for anatomy; Ganong + Guyton & Hall + Davidson for physiology; Davidson + PasTest + Notes and Notes + personal notes for clinical nephrology

- if the chapter is respiratory and the user is following the same source hierarchy, explicitly include: Gray's + Davidson for anatomy; Ganong + Guyton & Hall + Davidson for physiology; Davidson + PasTest + personal notes for clinical discussion, with emphasis on spirometry, ABG interpretation, oxygen therapy cautions, imaging clues, and overlap/differential thinking
- if the chapter is cardiology in this user's vault rooted at `/mnt/tb/Medicine`, actual topic production normally lands in `/mnt/tb/Medicine/Cardiology/`.
- For this user's cardiology chapter flow, use **Gray's + Davidson** for anatomy, **Guyton & Hall + Ganong + Davidson** for physiology, and **Davidson + PasTest + personal notes** for clinical discussion.
- In cardiology hierarchy work, it is acceptable and often preferable to build a **true disease-level-oriented** scaffold rather than a rigid disease-only taxonomy: preserve disease entities, but also keep high-yield interpretation, syndromic, and pathway files when they are central to FCPS/MRCP cardiology (for example ECG approach, troponin interpretation, hemodynamic profiles, reperfusion strategy, syncope risk stratification).
- When the user asks for strict Davidson validation/refinement in cardiology, read the live chapter roadmap/MOC first, then validate against public searchable Davidson-like snippets if full licensed text is unavailable, and explicitly label the result as a **public-snippet validation/refinement pass** rather than a verbatim chapter TOC match.
- When cardiology chapter scaffolding is built for Discord continuation, also create/update the chapter pinned-message note, session-resume note, `Medicine MOC.md`, `Davidson Chapter Progress Tracker.md`, and `Chapter Rules Index.md` so continuation is operational rather than only structural.
- In this user's current cardiology chapter flow, treat `git add` / `git commit` / `git push` after **each completed cardiology change or update** as an operational chapter override, not an optional side effect.
- **Explicit full-repo push override**: When the user issues a direct command such as "full push", "push medicine folder", or similar scope-widening instruction, immediately suspend the cardiology-only staging rule for that turn, stage the requested broader set, commit with a message that notes the user override, push, then resume the scoped rule for future turns.
- For cardiology continuation prompts that point to `00_Index/Cardiology Channel Session Resume <date>.md`, use the resume together with the live `Cardiology MOC.md` before selecting the next topic, then refresh the resume note after the batch so the queue, restart prompt, and recommended safe next command stay current.
- For cardiology continuation prompts like `next 1`, `next 2`, `next 10`, `complete 2 topic`, or `do next N and complete those`, treat the requested number as an **exact batch size**. 
  - **Always** re-read the live `Cardiology MOC.md` (completed section) + the `Davidson Chapter 16 - Cardiology Hierarchy.md` (or relevant heading hub) **before** proposing or acting on the next N.
  - Never guess the next topics from memory of previous batches — the MOC/hierarchy is the only source of truth.
  - Report progress counts only from explicit ✅ lines in the MOC completed section (not estimates). When the user asks "how many complete and how many left", give the tracked total (103 disease-level + 12 preserved core = 115) plus the verified ✅ count vs remaining.
  - If the proposed next topics turn out to already be marked ✅, immediately acknowledge the correction and re-read before suggesting replacements.
- In cardiology batch conversion work, update navigation at all directly exposed layers after upgrading a scaffold note in place: `Cardiology MOC.md`, the relevant topic-group hub, and the chapter hierarchy note when it lists the same topic.
- When reporting cardiology progress, do not rely only on `status: full-fcps-mrcp-note` files, because preserved root-level core notes may already be full but not yet converted to the newer status marker. Use the live `Cardiology MOC.md` as the primary source of truth, count explicit completed entries there, and cross-check any preserved root-level notes that are already marked as full in the MOC before reporting completed vs left.
- For this validated Cardiology Chapter 16 setup, the usual working total is **115 tracked topic units** = **103 hierarchy disease-level topics** + **12 preserved root-level core notes**. If only the MOC markers are verified, report the result as **explicitly verified completed/left** instead of overstating a full audit of every legacy note.
- When the user asks for cardiology progress counts like `how many topic done and left`, do **not** count only the explicit scaffold-completion lines (for example regex hits on `- ✅ [[`). That can undercount because `## Preserved core topic notes` may already include root-level full notes marked `✅`. Count completed scaffold entries **plus** preserved core notes already marked full/`✅`, then compute `left = total - completed`. See `references/cardiology-progress-counting.md`.
- During cardiology auto-push, path-stage the changed `Cardiology/` files plus the cardiology session-resume note if it was updated for continuity, while still excluding unrelated repo changes.
- For cardiology `next 2`, `next 3`, or another multi-topic cardiology batch while the standing rule remains **git after each completed cardiology change or update**, prefer a **topic-by-topic git cycle** inside the batch: finish topic 1 plus its MOC/hub/hierarchy/resume updates, commit/push/verify clean, then continue to topic 2. Do not collapse several completed cardiology topics into one commit when the chapter rule is explicitly per change/update.

**Critical honesty rule (user-enforced):** Never output phrases such as "batch complete", "MOC updated", "git done", "upgraded in place", or "notes written" unless the actual `write_file`/`patch` calls for the topic files + MOC/hub updates + `terminal` git commands have succeeded in the current turn. Descriptive language ("I will write...", "batch started") is allowed, but any claim of completion without real file-system and git output is forbidden. If the user asks "complete N" or "do next N", default behavior is to execute the writes, not describe the plan. Violation of this rule has previously caused user frustration; treat it as a hard constraint.
- Under a **strict minimal-read cardiology workflow** (`Cardiology MOC + target note(s) + max 1 directly relevant hub`), if the user says `complete next N incomplete topics` without naming files, use the live `Cardiology MOC.md` to choose the most obvious current sequence, then read exactly **one** directly relevant topic-group/heading hub and select the next visible consecutive unfinished topics from that same hub. Do not widen to the session-resume note or chapter hierarchy unless the user permits a broader read.
- In that strict minimal-read cardiology mode, the allowed working set is only: `Cardiology MOC.md`, the target topic note(s), and **one** directly relevant hub. After writing, update only the upgraded target note(s), `Cardiology MOC.md`, and that **same one touched hub** if needed. Do not inspect or edit extra cardiology files unless the user explicitly widens scope.
- If more context is genuinely needed to identify the exact next targets or to complete the requested batch confidently, stop and ask instead of silently widening the read scope.
- In that strict minimal-read cardiology mode, prefer staying in the same visible topic-group sequence when the hub makes the next unfinished files obvious (for example, after completed `Aortic stenosis` and `Aortic regurgitation`, continue with `Mitral stenosis` and `Mitral regurgitation` from `Left-sided valvular disease.md`).
- If the current strict cardiology hub exposes **fewer remaining topics than the requested exact batch size**, do not silently overrun the read scope. Tell the user the exact visible remainder and ask whether to: (a) continue with the smaller same-hub batch, or (b) allow **one extra directly relevant hub** for that turn so the exact `next N` can be satisfied.
- In this cardiology mode, always reuse the existing scaffold/note if present. Do not create duplicate parallel cardiology notes for the same topic.
- If the user grants that **one extra relevant hub** for cardiology, treat it as a task-level scope widening for that turn: finish the last visible topic(s) in the current hub first, then read the next directly relevant hub in the same heading sequence and complete exactly the remaining count needed. Keep the widened batch orderly rather than jumping arbitrarily across headings.
- If the user later gives a larger bare cardiology continuation prompt in the **same active sequence** (for example `next 5`) after already allowing this one-extra-hub widening, continue in visible order across the directly relevant hubs needed to satisfy the exact batch size instead of reopening the same clarification loop. Exhaust the current hub first, then continue into the next directly relevant hub in the same heading, and only then move to the next heading when needed.
- When a cardiology multi-topic batch is completed under the standing rule `git after each completed cardiology change or update`, preserve a **topic-by-topic git cycle** even for larger batches: complete topic 1 + touched navigation files, commit/push/verify clean; then topic 2; and so on through the requested exact count. Do not collapse a `next 5` batch into one broad cardiology commit.
- After an automatic cardiology push, verify both outcomes before closing the batch: (1) push succeeded to the expected branch/remote, and (2) `git status --short -- Cardiology 00_Index/'Cardiology Channel Session Resume <date>.md'` is clean so no cardiology continuity edits were left behind unintentionally.
- If a cardiology `git push` reports a ref-lock / `cannot lock ref 'refs/heads/main' ... expected ...` style race or mismatch, do **not** assume the batch failed. Immediately `git fetch origin main` and compare local `HEAD` with `origin/main`. If the fetched remote now points to the same commit as local `HEAD`, treat the push as already succeeded and avoid creating duplicate recovery commits. Only retry push after this verification step.
- If the user questions whether the chapter workflow skill is actually being used in a live cardiology channel, make the skill usage visible: explicitly state the loaded relevant skills at the start of the batch reply (for example `Loaded: medical-chapter-study-pack` and `Loaded: obsidian`) before proceeding with the topic work.
See `references/cardiology-live-vault-topic-production.md` for the proven Chapter 16 heading set, continuation prompt, current git override, and honesty/pitfall notes from session.
See `references/cardiology-strict-operating-prompt.md` for the proven Chapter 16 minimal-read operating rule: work only inside `/mnt/tb/Medicine/Cardiology/`, read only `Cardiology MOC.md` + target note(s) + max 1 directly relevant hub, update only the same touched hub plus MOC after writing, stop and ask if more context is genuinely needed, and keep git add/commit/push strictly cardiology-scoped with post-push clean-scope verification.
See `references/cardiology-display-name-to-filename-mapping.md` for the complete display-name to actual filename mapping used when patching navigation files.

## Proven Cardiology Batch Completion Workflow (from June 2026 sessions)

When completing a batch of cardiology topics from scaffold to full FCPS/MRCP notes, the following sequence has proven effective:

1. **Identify targets**: Use live `Cardiology MOC.md` completed section + `Davidson Chapter 16 - Cardiology Hierarchy.md` to find next uncompleted scaffold topics still present in the hierarchy. The MOC completed section (lines starting with `- ✅ [[`) is the source of truth for what's done.

2. **Strict minimal-read**: Read only `Cardiology MOC.md` + target note(s) + **one** directly relevant hub. Do not widen to session-resume or full hierarchy unless needed.

3. **Write/upgrade in place**: Use the existing scaffold file if present. Upgrade to full FCPS/MRCP note following the template structure (all sections: Learning Objectives through Answer Key). Reuse the exact same file path — no parallel duplicates.

4. **Dual navigation update**: After each topic, update **both**:
   - `Cardiology MOC.md` — append to completed list with `✅ [[path|display]] — full FCPS/MRCP note completed`
   - `Davidson Chapter 16 - Cardiology Hierarchy.md` — add `✅` before the same link
   Both must be patched in the same turn to stay aligned.

5. **Progress counting**: Count from explicit `✅` lines in MOC completed section. **Do not** rely on file-size or `status:` frontmatter alone — preserved root-level core notes may have different status markers. Report as "verified completed/left" from MOC counts.

6. **Honesty rule (hard constraint)**: Never claim "batch complete", "upgraded in place", "MOC updated", or "git done" unless the actual `write_file`/`patch` calls for topic files + MOC/hub updates + `terminal` git commands have succeeded in the current turn. Descriptive language ("I will write...", "batch started") is allowed; completion claims require real file-system and git output.

7. **Hierarchy display-name ↔ file-name mapping**: Display names in hierarchy/MOC (e.g., "Atrioventricular block") often differ from actual file names (e.g., "AV block and conduction disorders.md"). Build a mapping before cross-referencing or patching.

8. **Git per-change cycle**: Under the standing rule "git after each completed cardiology change or update", preserve a **topic-by-topic git cycle** even for multi-topic batches: finish topic 1 + touched navigation files, commit/push/verify clean; then topic 2; etc. Do not collapse a `next N` batch into one broad commit.

9. **Post-push verification**: After each push, verify (1) push succeeded to expected branch/remote, and (2) `git status --short -- Cardiology 00_Index/'Cardiology Channel Session Resume <date>.md'` is clean.

10. **Duplicate directory audit**: Before verification, check for parallel scaffold directories (e.g., `Pericardial | Endocardial |+Inflammatory Cardiac Disease/` vs `Pericardial, Endocardial, and Inflammatory Cardiac Disease/`). Remove duplicates to avoid false completion claims.

11. **Missing Viva section batch-add**: Many scaffold-to-full conversions lack "Common Viva Questions". Add missing sections systematically during upgrade rather than one-by-one later.

12. **The 11 topics completed in June 2026 batch** (pattern for future batches):
    - Sinus tachycardia
    - Multifocal atrial tachycardia
    - Premature ventricular complexes
    - Complete heart block
    - Monomorphic ventricular tachycardia
    - Polymorphic ventricular tachycardia and torsades de pointes
    - Ventricular fibrillation and cardiac arrest rhythms
    - Sinus node dysfunction
    - Atrioventricular block
    - Pacemaker indications
    - Acute pulmonary edema
    - Cardiac syncope
    - Vasovagal syncope
    - Exercise testing and ischemia provocation
    - Ambulatory ECG monitoring
    All followed the full template with all required sections (Learning Objectives through Answer Key with 10 MCQs, 10 SBAs, flashcards, full answer explanations).

13. **Display-name ↔ file-name mapping for cross-referencing**: Before patching MOC/hierarchy, build a mapping from hierarchy display names to actual file paths. Example mappings discovered:
    - "Atrioventricular block" → "AV block and conduction disorders.md"
    - "Complete heart block" → "Complete heart block.md"
    - "Ventricular tachycardia and VF" → "Ventricular tachycardia and VF.md"
    - "Ventricular fibrillation and cardiac arrest rhythms" → "Ventricular fibrillation and cardiac arrest rhythms.md"
    - "Sinus tachycardia" → "Sinus tachycardia.md"
    - "Multifocal atrial tachycardia" → "Multifocal atrial tachycardia.md"
    - "Premature ventricular complexes" → "Premature ventricular complexes.md"
    - "Sinus node dysfunction" → "Sinus node dysfunction.md"
    - "Pacemaker indications" → "Pacemaker indications.md"
    - "Acute pulmonary edema" → "Acute pulmonary edema.md"
    - "Cardiac syncope" → "Cardiac syncope.md"
    - "Vasovagal syncope" → "Vasovagal syncope.md"
    - "Exercise testing and ischemia provocation" → "Exercise testing and ischemia provocation.md"
    - "Ambulatory ECG monitoring" → "Ambulatory ECG monitoring.md"

14. **Template completeness checklist**: Every full FCPS/MRCP note must contain ALL sections through "Answer Key with Explanations" including: Learning Objectives, Definition, Pathophysiology, Clinical Features, ECG/Investigation tables, Management algorithms (Mermaid), Differential Diagnosis, Complications, Prognosis, FCPS/MRCP High-Yields, Common Viva Questions, Common Traps, Mind Map, Revision Summary, 24h Recall, Tracker, Must/Should/Nice to Know, Self-Test Scorecard, Exam Answer Modes, 10 MCQs, 10 SBAs, Flashcards, Full Answer Key.
- if a reusable kickoff format would help, use `templates/chapter-channel-kickoff-message.md`

When exporting the skill system into the user's repo or vault, prefer both:
- a user-facing export in `00_Index/` such as:
  - `medical-chapter-study-pack.skill.md`
  - `Davidson Study Organization Reference.md`
  - `Obsidian Vault Bootstrap Reference.md`
  - `How to Use This System.md`
- a raw internal-reference export folder at `00_Index/References/` containing copies of linked skill references such as:
  - `davidson-study-organization.md`
  - `obsidian-vault-bootstrap.md`
  - `README.md` explaining the folder purpose

After creating these exports, add or update cross-links from `00_Index/Medicine MOC.md` and related guide notes so the vault remains navigable inside Obsidian.

If the user wants a finalized system package, also export or maintain:
- `00_Index/All System Rules.md` as the stable rule summary
- `00_Index/Medicine Chapter Channel Plan.md` as the Discord chapter-channel architecture note
- `00_Index/Chapter Rules Index.md` as the tracker for completed and pending chapter-rule packs
- `00_Index/Chapter-Specific Rule Template.md` as the reusable starter for any new chapter channel
- `00_Index/Chapter Rules/` as the folder containing filled chapter-specific rule notes such as cardiology, respiratory, neurology, nephrology, gastroenterology, endocrinology, hematology, rheumatology, and infectious disease

See `references/obsidian-vault-bootstrap.md` for a proven full-Obsidian vault layout, template set, and Git/GitHub bootstrap workflow.

See `references/davidson-study-organization.md` for Davidson chapter mapping, tracker conventions, and the chapter-template coverage pattern proven in session.

See `references/davidson-chapter-boundary-validation.md` for the proven workflow to validate strict Davidson chapter boundaries and prevent adjacent-chapter bleed-through (for example: Neurology vs Stroke medicine).

See `references/channel-workflow-and-system-rules.md` for the proven split between index/system channels and chapter-topic channels, plus the recommended final exported governance notes.

See `references/chapter-channel-rule-packs.md` for the proven per-chapter governance layout, ready-now chapter rule packs, and the recommended contents of each chapter rule file.

See `references/nephrology-live-vault-topic-production.md` for the proven workflow when a nephrology topic must be delivered both in chat and as a real note file under `/mnt/tb/Medicine/Nephrology/`, including MOC updates and optional Git sync.

See `references/nephrology-strict-operating-prompt.md` when the user provides a strict nephrology channel constitution: Davidson Chapter 18 only, exact minimal-read working set, in-place topic upgrades only, limited hub updates, and nephrology-scoped git hygiene.

See `references/respiratory-live-vault-topic-production.md` for the proven workflow when a respiratory topic must be expanded in place under `/mnt/tb/Medicine/Respiratory/`, the Respiratory MOC should be annotated to show the topic is now a full FCPS/MRCP note, and git sync must stage only the respiratory files touched for that task.

See `references/gastroenterology-live-vault-topic-production.md` for the proven Chapter 23 workflow: strict separation from Hepatology Chapter 24, minimal-read selection from the live `Gastroenterology MOC.md`, exact-topic in-place scaffold upgrades, hub-limited navigation updates, and gastro-only git add/commit/push with clean-scope verification.

See `references/neurology-live-vault-topic-production.md` for the proven Neurology Chapter 28 workflow: strict exclusion of Stroke into the separate Stroke Medicine chapter, using the session-resume note together with the live `Neurology MOC.md`, upgrading existing disease-level scaffold notes in place under `/mnt/tb/Medicine/Neurology/`, marking completed topic links with `✅` in the relevant heading hubs, and updating Neurology milestone counts from the MOC after each batch.

See `references/stroke-medicine-hierarchy-pattern.md` for the proven Davidson Chapter 29 hierarchy pattern, representative heading/topic-group/disease-level file layout, and the exact index notes that also need updating when Stroke Medicine is separated from Neurology into its own live chapter system.

See `references/stroke-live-vault-topic-production.md` for the proven Chapter 29 continuation workflow: re-read the live Stroke Medicine MOC plus heading hubs before each `next N`, upgrade exactly N scaffold notes in place, mark them `✅ full-note`, and use stroke-path-scoped git add/commit/push with post-push verification.

See `references/cardiology-audit-and-completion-workflow.md` for the proven Cardiology Chapter 16 audit workflow: verify true completeness by content sections (not file size), build hierarchy↔file display-name mapping, cross-validate MOC and Hierarchy tracking files, batch-add missing Viva sections, remove duplicate scaffold directories, and update both tracking files from verified reality.
See `references/cardiology-workflow-lessons.md` for the refined FCPS/MRCP note template, mermaid diagram patterns, batch git workflow, MOC/hierarchy update rules, session resume rules, and pitfalls from the June 2026 cardiology production sessions (17 new full notes + 13 legacy upgrades).

For this user's Stroke Medicine continuation workflow, use the live `Stroke Medicine MOC.md` as the source of truth for progress reporting, with the current working denominator **86 disease-level scaffold files** unless the live hierarchy is rebuilt. After each stroke batch, report the exact number completed in that batch, then update the cumulative completed/left count from the explicit MOC completed list rather than from file-status guessing or stale session summaries.
- When selecting or auditing the remaining Stroke Medicine queue, `search_files` for markdown content matching `^status:\s*scaffold$` under `/mnt/tb/Medicine/Stroke Medicine` is a reliable cross-check for exactly which disease-level notes are still unfinished. Use it to verify the last pending topics instead of relying only on visual scanning of the MOC.
- When a Stroke Medicine batch finishes the chapter-level first pass and there are **zero** remaining `status: scaffold` disease-level notes, perform a finalization pass in `Stroke Medicine MOC.md`: update frontmatter status from scaffold-built wording to a completion state such as `first-pass-full-note-complete`, add a build-summary line showing `86 / 86` first-pass completion, and report `0 left` explicitly after re-counting from the live MOC.
- In the Stroke Medicine channel, a bare continuation prompt like `Next` should default to **`next 1`** rather than triggering a clarification loop. Re-read the live MOC plus the relevant current heading/topic-group hub, pick exactly one next pending scaffold in sequence, upgrade it in place, update navigation, and then run the stroke-scoped git workflow.
- If the user asks only for the **next single topic name/path** (for example `give me next 1 topic`), do **not** widen into note-writing work. Identify the next pending stroke topic using the live `Stroke Medicine MOC.md` plus **at most one relevant hub**, then reply with just the next topic and path unless more was requested.
- If the user asks for **selection only** with prompts like `next 2` or `next 3` and the surrounding context indicates they want the next topic names/paths rather than immediate file upgrades, keep the turn in **queue-selection mode**: read the live `Stroke Medicine MOC.md` plus the relevant current hub, identify exactly **N** next pending topics in visible order, and reply with only those topic names/paths. Do not silently widen into note-writing, MOC edits, or git work unless the user explicitly requests the batch to be completed.
- If the user explicitly imposes a **minimal-read stroke workflow** such as `Read only Stroke Medicine MOC + target note + max 1 relevant hub`, treat that as a task-level operational constraint: do not inspect additional files, and if more context would actually be needed, stop and ask rather than silently broadening the read scope.
- For a single targeted stroke upgrade under that minimal-read rule, the allowed working set is: `Stroke Medicine MOC.md`, the target disease-level note, and at most one relevant heading/topic-group hub; after writing, update only the MOC and that one hub if needed, then do stroke-only git add/commit/push.
- For Stroke Medicine `next 2`, `next 3`, or similar continuation prompts, prefer staying within the same currently active topic-group subgroup when the next pending items are clearly consecutive there (for example continuing a rehabilitation subgroup) before moving to the next subgroup, while still honoring the exact requested batch size.
- When selecting a Stroke Medicine batch, inspect both the chapter-level section hub and the nested topic-group hub before writing so the chosen files match the visible live subgroup order rather than only the flat MOC list.
- If the current stroke heading/topic-group exposes fewer remaining items than the user's requested exact batch size, do **not** silently stop short or overrun. Either (a) read the next relevant heading hub and continue into it to satisfy the exact `next N`, or (b) if you want explicit confirmation before crossing the heading boundary, tell the user the exact remaining count in the current heading and offer the cross-heading continuation choice plainly (for example: `continue 9` vs `continue 10 with 1 from the next heading`).
- If the user chooses the smaller in-heading option after that clarification (for example `continue 9`), treat that as the new exact batch size for the turn and do **not** silently add a cross-heading topic just because a larger earlier request existed.
- If no dedicated Stroke Medicine session-resume note exists, do not block on that absence. Continue directly from the live `Stroke Medicine MOC.md` and the relevant heading/topic-group hubs, and report the exact next pending topic chosen.
- When patching `Stroke Medicine MOC.md`, watch for duplicate link text appearing in both the completed section and the lower running list. Use extra heading context (for example anchoring near `## Tasks` or the surrounding subsection) so MOC patches stay unique instead of failing on ambiguous matches.

## Git / GitHub Mode

If the user wants version control or syncing:

- notes can be stored inside a Git repository
- the repository can be newly created or existing
- topic files can be committed after creation or update
- pushing to GitHub is possible if authentication and repo details are available

Typical workflow:
1. Create or use an existing root folder
2. Create chapter folders and notes
3. Initialize or open a Git repo
4. Inspect `git status` before staging anything
5. Stage only the files changed for the current topic/task unless the user explicitly asks for a broader repo sync
6. Commit changes with meaningful messages
7. Push to GitHub if the user requests and auth is available

Do not assume GitHub push by default; treat it as optional side-effect work.

**Live-repo safety rule:** when the vault already has unrelated modified/untracked files, do **not** sweep them into the topic commit by default. In chapter-topic production, prefer path-specific `git add` for the note and any directly related MOC/index files you updated, then commit only those files unless the user explicitly wants all pending repo changes included.

**Respiratory repo follow-up rule proven in session:** if the user later asks to "commit/push respiratory" or to "update git push of respiratory" after multiple respiratory files were created across recent turns, stage **all currently pending respiratory-only changes** that belong together (for example the new `*-last night.md` files plus `Respiratory MOC.md`) while still excluding unrelated changes elsewhere in the repo.

## What to Clarify Only When Needed

Do not over-ask. But if file output is requested and the information is not otherwise available, clarify only the minimum needed:
- target root folder
- whether Obsidian mode is desired
- whether Git/GitHub sync is desired
- chapter naming convention if the user cares about numbering or custom taxonomy

### 1. Use user-specified references first
If the user gives preferred books, treat them as the main framework.

### 2. Match references to section type
Use the most suitable source set for the section being written:
- **Anatomy** → anatomy-focused references named by the user
- **Physiology** → physiology-focused references named by the user
- **Clinical medicine / disease discussion** → major medicine texts, exam banks, and user notes

### 3. If references are incomplete
Use additional standard sources only as needed, while keeping the user's preferred references primary.

## Davidson Chapter Coverage Mode

When the user is studying from **Davidson's Principles and Practice of Medicine**, the skill can align outputs with Davidson's major chapter structure. Use this to organize notes, MOCs, trackers, or templates by Davidson part/chapter when helpful.

### Strict Davidson Chapter Boundary Rule

If the user asks to keep a chapter channel or MOC **strictly within a specific Davidson chapter**, do not infer topic ownership loosely from generic neurology/medicine knowledge. Instead:

1. verify the chapter boundary against the vault's Davidson roadmap/index notes first
2. if needed, verify the chapter's internal contents using a reliable preview/source snippet available through tools
3. tighten the topic queue, pinned message, and MOC so they match the chapter's own headings/subdomains
4. explicitly exclude adjacent Davidson chapters when confusion is likely

Example proven in session:
- **Chapter 28: Neurology** should cover neurology chapter headings such as clinical examination/localization, headache syndromes, functional neurological disorder, epilepsy, vestibular disorders, sleep disorders, neuro-inflammatory disease, paraneoplastic neurological disorders, neurodegenerative disease, movement disorders, meningitis, and parenchymal CNS infections
- **Stroke** should be excluded from the Neurology chapter workflow when the Davidson roadmap places it in the separate **Chapter 29: Stroke medicine**
- **Chapter 29: Stroke medicine** can then be scaffolded as its own hierarchy with heading hubs, topic-group hubs, and disease-level files for stroke recognition/assessment, TIA, acute ischaemic stroke, intracerebral haemorrhage, neuroimaging and acute evaluation, reperfusion therapy, stroke-unit care/complications, secondary prevention, special stroke scenarios, and recovery/rehabilitation

When this kind of correction happens, update all three if they exist:
- chapter rule note
- pinned/kickoff message
- chapter MOC/topic queue

When splitting adjacent Davidson chapters into separate live vault systems, also update the destination chapter so the separation is operational rather than only conceptual:
- build or expand the destination chapter MOC
- create/update the chapter hierarchy map
- create heading hubs, topic-group hubs, and disease-level scaffold files under the destination chapter folder
- add the chapter pinned-message note and link it from `Chapter Rules Index` if the user is channel-driven
- update roadmap / master MOC / progress tracker so both chapters remain discoverable

Current high-level map supplied by the user:

### Part 1: Fundamentals of Medicine
- Clinical decision-making
- Clinical therapeutics and good prescribing
- Clinical genetics
- Clinical immunology
- Population health and epidemiology
- Principles of infectious disease
- Oncology
- Pain and palliative care

### Part 2: Emergency and Critical Care Medicine
- Acute medicine and critical illness
- Poisoning
- Envenomation
- Medicine in austere environments

### Part 3: Clinical Medicine
- Infectious disease
- HIV infection and AIDS
- Sexually transmitted infections
- Cardiology
- Respiratory medicine
- Nephrology and urology
- Clinical biochemistry and metabolic medicine
- Endocrinology
- Diabetes mellitus
- Nutritional factors in disease
- Gastroenterology
- Hepatology
- Haematology and transfusion medicine
- Rheumatology and bone disease
- Dermatology
- Neurology
- Stroke medicine
- Medical ophthalmology
- Medical psychiatry
- Maternal medicine
- Adolescent and transition medicine
- Ageing and disease
- Laboratory reference ranges

If the user wants a Davidson-based study roadmap, preserve this part/chapter structure in index notes, trackers, or file metadata where practical.

When organizing a Davidson-based vault, prefer a pair of index notes:
- `00_Index/Davidson Chapter Roadmap.md`
- `00_Index/Davidson Chapter Progress Tracker.md`
- `00_Index/Weekly Study Dashboard.md`

and keep chapter-specific templates aligned with the Davidson chapter names when this improves planning and retrieval.

## Dashboard and Tracker Conventions

For a mature Obsidian study vault, prefer these index/control notes when the user wants structured long-term preparation:

- `00_Index/Medicine MOC.md` → master navigation
- `00_Index/Davidson Chapter Roadmap.md` → chapter map
- `00_Index/Davidson Chapter Progress Tracker.md` → chapter-by-chapter progress
- `00_Index/Weekly Study Dashboard.md` → short-term execution board

When useful, the dashboard/tracker may include:
- manual summary counts for chapters started / completed
- checkbox progress blocks for first pass, MCQs, SBAs, and revision cycles
- exam countdown fields
- optional Dataview blocks for automatic counts if the user's Obsidian setup supports Dataview

Prefer manual fallback fields even when adding Dataview snippets, so the notes remain useful without plugins.

## Chapter-Specific Override Pattern

When the user gives rules for a particular chapter, restate and follow them. Example pattern:

- **Nephrology anatomy** → Gray's Anatomy + Davidson
- **Nephrology physiology** → Ganong + Guyton & Hall + Davidson
- **Nephrology clinical discussion** → Davidson + PasTest + notes

The same logic should be adapted for other chapters like respiratory or neurology if the user specifies different sources.

## Interpretation Blocks and Procedure Mini-Sections

For chapters where interpretation skill is central, add a dedicated **Interpretation Frameworks** section when relevant. Examples include:

- **Nephrology** → urinalysis, urine electrolytes, acid-base analysis, dialysis indications
- **Respiratory** → ABG interpretation, spirometry patterns, oxygen therapy cautions
- **Cardiology** → ECG approach, heart failure profiles, murmur clues, ACS interpretation
- **Gastroenterology / Hepatology** → LFT interpretation, jaundice pattern approach, GI bleed severity clues
- **Neurology** → lesion localization, neuroimaging clues, CSF interpretation when relevant
- **Endocrinology / Metabolic medicine** → dynamic endocrine patterns, electrolyte interpretation, diabetic emergency comparisons
- **Haematology** → CBC/peripheral smear patterns, coagulation profiles, transfusion reactions

When procedures matter, add a short **Procedure Mini-Sections** block under procedures or management, covering:
- indication
- contraindication
- preparation
- key steps or principle
- complications
- viva pearls

Examples:
- dialysis / catheter-related issues
- ABG sampling
- pleural tap
- lumbar puncture
- ascitic tap
- transfusion-related procedures

## Writing Rules

1. Be **elaborate and exam-oriented**.
2. Explain from **basic concepts to advanced clinical application**.
3. Prefer **clear headings, bullets, tables, comparison charts, flowcharts, and structured algorithms** where useful.
4. Highlight **high-yield FCPS/MRCP points**.
5. Include **common viva traps, MCQ traps, differentiating features, and practice pearls** when relevant.
6. Keep the note **editable** and cleanly structured for later revision.
7. If requested, revise the existing `.md` note rather than rewriting from scratch.
8. Add **topic correlation / integration with related topics** when useful, e.g. AKI vs CKD, nephrotic vs nephritic, asthma vs COPD.
9. Add **treatment/management cautions**, including major drug interactions, contraindications, disease-specific precautions, drug-dose cautions in organ dysfunction, and when a treatment should be avoided if comorbid conditions coexist.
10. Include **practical exam/viva/clinical warnings** such as important complications, red flags, and commonly missed management errors.
11. Include **normal values, important cut-offs, staging criteria, diagnostic thresholds, and emergency thresholds** when relevant.
12. Add a **stepwise approach/algorithm** for diagnosis or management whenever it would improve understanding.
13. Add **special situations** such as pregnancy, elderly patients, diabetes, hypertension, liver disease, heart failure, sepsis, pediatric differences, or immunocompromised states when relevant.
14. Include **one-page rapid revision content** for last-minute exam review when feasible.
15. Mark content as **Must Know / Should Know / Nice to Know** when prioritization would help the learner.
16. Add **24-hour recall prompts**, a **7-day / 15-day / 30-day revision tracker**, and a **self-test scorecard** when the user wants maximum exam performance.
17. Include a **My Weak Points** section when the note is intended for repeated revision or self-correction.
18. Prefer **active-recall-friendly writing**, including short prompts, compare-and-contrast triggers, and blank-page recall cues when useful.
19. Add **Interpretation Frameworks** for chapters where pattern recognition and result interpretation are core exam skills.
20. Add **Procedure Mini-Sections** when bedside procedures, sampling techniques, or intervention indications are important.
21. Support **exam-answer modes** when helpful, such as long-answer, short-note, viva, ward-case discussion, rapid revision sheet, or last-night-before-exam sheet.

## Study Execution and Retention System

When the user wants the **best exam-performance version**, do not stop at content delivery alone. Structure the topic so it supports:

1. **Understanding** — full explanatory note from basics to advanced clinical use
2. **Recall** — flashcards, one-page summary, mnemonics, and quick prompts
3. **Performance** — MCQs, SBAs, viva questions, compare-and-contrast traps, and management cautions

For high-yield study mode, prefer a **3-layer topic output**:

### Layer 1: Full Note
- complete topic explanation
- integrated anatomy/physiology/pathology/clinical medicine
- investigations, diagnosis, management, complications, and special situations

### Layer 2: Rapid Revision
- one-page summary
- must-know cut-offs and criteria
- algorithm snapshot
- common confusions and emergencies

### Layer 3: Active Recall and Testing
- flashcards
- 24-hour recall prompts
- 10 MCQs + 10 SBAs
- viva-style short questions
- self-test scorecard

When useful, explicitly encourage the learner to revise each topic at:
- **24 hours**
- **7 days**
- **15 days**
- **30 days**

Prefer adding a simple scorecard such as:
- Understanding /10
- Recall /10
- MCQ performance /10
- SBA performance /10
- Viva confidence /10

Interpretation example:
- **<35/50** = weak topic, needs re-study
- **35–44/50** = acceptable but not secure
- **45+/50** = strong exam-ready topic

When appropriate, add prompts that force active recall, such as:
- Explain the topic in 2 minutes without notes
- Compare this topic with a common differential
- State first-line management and major contraindications
- List emergency red flags from memory
- Write the diagnostic approach from a blank page


## Enrichment Elements

Add these when they materially improve understanding:

- **Tables** for classifications, comparisons, causes, investigations, and drug summaries
- **Interpretation Frameworks** for ABGs, ECGs, urinalysis, CSF, LFTs, CBCs, endocrine patterns, and similar high-yield result interpretation tasks
- **Mind maps** in Markdown bullet-tree format for rapid revision
- **Flowcharts** for diagnostic and management pathways
- **Approach / algorithm sections** for symptom-based and diagnosis-based reasoning
- **Normal values / important cut-offs** for quick revision and viva recall
- **Correlation with related topics** so the learner can connect one chapter to another
- **YouTube/video reference suggestions** for visual learning when appropriate
- **Image/diagram suggestions** (or image prompts/requests) for anatomy, physiology, pathways, and disease patterns when visual explanation would help
- **Red flags / emergency points** for urgent recognition and escalation
- **Special situations / comorbidity cautions** for real-world management nuance
- **Procedure mini-sections** for indications, contraindications, complications, and viva pearls
- **One-page revision summaries** for pre-exam rapid review
- **Must Know / Should Know / Nice to Know** prioritization when topic breadth is high
- **24-hour recall prompts** for next-day reinforcement
- **7-day / 15-day / 30-day revision trackers** for spaced repetition
- **Self-test scorecards** to identify weak topics and measure readiness
- **My Weak Points** sections for personalized correction of recurrent mistakes

If direct web/video lookup is available and requested, provide concrete references. Otherwise, provide the exact type of video or diagram the learner should look for.

## Suggested Expanded Structure

When suitable, enrich the standard topic structure with these sections:

```md
## Learning Objectives
## Normal Values / Important Cut-offs
## Approach / Algorithm
## Investigations
## Interpretation Frameworks
## Tables / Comparison Charts
## Drug Interactions / Contraindications / Comorbidity Cautions
## Procedures / Indications / Contraindications
## Procedure Mini-Sections
## Red Flags / Emergencies
## Topic Correlation
## Special Situations
## Common Confusions / Exam Traps
## Mnemonics
## Mind Map
## Flowchart
## Suggested Visuals / Image Notes
## Suggested Video References
## One-Page Revision Summary
## 24-Hour Recall Prompts
## 7-Day / 15-Day / 30-Day Revision Tracker
## Must Know / Should Know / Nice to Know
## My Weak Points
## Self-Test Scorecard
## Exam Answer Modes
## Answer Key with Explanations
```

## Exam Answer Modes

When requested, the same topic can be rewritten into one or more exam-performance formats:

- **Full note**
- **Long-answer exam format**
- **Short note**
- **Viva answer**
- **Ward-case discussion**
- **Rapid revision sheet**
- **Last-night-before-exam sheet**
- **MCQ pack only**
- **SBA pack only**

Adapt depth, structure, and wording to the requested mode while preserving clinical accuracy.

## Question Bank Rules

After each topic, include both:

### A. MCQs (10)
- Single best correct answer
- Cover definitions, mechanisms, investigations, complications, and management
- Keep them exam style
- Provide answer key with brief explanations when feasible

### B. SBA Questions (10)
- Single best answer clinical-style stems
- Include common ward/exam scenarios when possible
- Provide answer key with brief explanations

### C. Answer Key with Explanations
- Prefer a dedicated answer key section after the questions
- Keep explanations concise but educational
- Clarify why the best answer is correct and, when useful, why common distractors are wrong

## Flashcard Rules

When possible, add flashcards after the questions.

Preferred simple format:

```md
- Q: ...
  A: ...
```

If the user asks for Anki style, use:

```md
Question::Answer
```

Flashcards should focus on:
- definitions
- classic associations
- thresholds / criteria
- causes
- complications
- first-line investigations
- first-line management
- differentiating features

## Editing Existing Notes

If the user asks to edit a chapter file, support edits such as:
- add more detail
- shorten for revision
- expand anatomy or physiology
- add normal values / cut-offs
- add algorithms / flowcharts / mind maps
- add interpretation frameworks
- add tables / mnemonics / flowcharts
- add red flags / emergencies
- add special situations or comorbidity cautions
- add procedure mini-sections or viva pearls
- add drug interactions, contraindications, and dose cautions
- add more MCQs or SBAs
- switch the same topic into long-answer, short-note, viva, ward-case, or last-night-before-exam mode
- add or refine must-know / should-know / nice-to-know prioritization
- add 24-hour recall prompts or spaced-revision trackers
- add a my-weak-points section or self-test scorecard
- update references or chapter-specific rules
- convert to viva format
- create a one-page revision sheet

## Reusable Prompt Pattern

When applying this skill, infer or confirm these fields from the user request:
- **chapter/system**: nephrology / respiratory / neurology / etc.
- **topic**: e.g. AKI, asthma, stroke
- **exam target**: FCPS / MRCP / both / other
- **reference rules**: chapter-specific source preferences
- **Davidson map**: optional part/chapter alignment when the user is following Davidson
- **output mode**: full note / short note / revision note / viva / MCQ pack
- **answer mode**: long-answer / short-note / viva / ward-case / rapid revision / last-night-before-exam
- **file format**: Markdown by default
- **save mode**: chat only / write to file
- **root path**: e.g. `/mnt/tb/Medicine`
- **vault mode**: standard Markdown / Obsidian-friendly
- **versioning**: no git / local git / GitHub sync
- **structure mode**: flat topic notes / chapter > heading > topic group > disease-level files

## Common Pitfalls
## Common Pitfalls

1. Mixing anatomy, physiology, and clinical references without respecting the user's preference hierarchy.
2. Assuming a topic belongs to a chapter based on broad specialty knowledge instead of the user's Davidson chapter boundaries.
3. Leaving adjacent-chapter bleed-through in the MOC, pinned message, or starter topic queue after the user requests strict chapter scoping.
4. Giving superficial summaries when the user asked for A-to-Z detail.
5. Forgetting to include the **10 MCQs + 10 SBAs** after the topic.
6. Omitting flashcards when they are feasible.
7. Producing plain text when Markdown structure is clearly preferred.
8. Ignoring chapter-specific rule updates from the user.
9. Treating a chapter-channel request as chat-only content when the user actually expects real vault output (`.md` file creation, chapter-folder placement, MOC updates, and optional git workflow) and failing to make that workflow explicit in the kickoff message or topic prompt.
10. Discussing treatment without noting important contraindications, drug interactions, comorbidity conflicts, dose issues, or exam-relevant cautions.
11. Missing helpful tables, algorithms, topic correlations, mind maps, visuals, video references, or flowcharts when they would substantially improve understanding.
12. Failing to include interpretation frameworks for chapters where pattern recognition and report interpretation are central.
13. Failing to include normal values, cut-offs, staging, red flags, or emergency thresholds for topics where they are central.
14. Omitting special situations such as pregnancy, elderly patients, organ dysfunction, or multiple comorbid diseases when they materially change management.
15. Giving rich notes but no active recall system, revision tracker, or self-test method when the user wants high exam performance.
16. Failing to prioritize content into must-know vs should-know vs nice-to-know when the chapter is broad and time-limited.
17. Ignoring when the user wants the same topic transformed into a specific exam-answer mode such as short note, viva, or long answer.

### Template Completeness Verification (Critical)

**Pitfall observed**: Initial batch of notes had full template; subsequent batches (10 notes) missed ~50% of required sections:
- Must Know / Should Know / Nice to Know
- Common Confusions / Exam Traps
- Mnemonics
- Mind Map / Flowchart / Suggested Visuals
- 24-Hour Recall / Revision Tracker / My Weak Points / Self-Test Scorecard
- Exam Answer Modes (Long Answer, Short Note, Viva, Ward Case, Last-Night Sheet)
- **10 MCQs + 10 SBAs + Flashcards + Answer Key with Explanations** (placeholder text only)

**Fix**: After writing ANY note, verify against the full template checklist (see `references/template-completeness-checklist.md`). Do not mark `status: full-fcps-mrcp-topic-note` until ALL sections are present.

### WikiLink Consistency

**Pitfall observed**: 3 mismatches between hierarchy links and actual filenames:
- `[[Septic Shock]]` vs `Sepsis and Septic Shock.md` (separate note created)
- `[[Malignant Hyperthermia / Neuroleptic Malignant Syndrome]]` vs `Malignant Hyperthermia Neuroleptic Malignant Syndrome.md` (slash in link, no slash in filename)
- `[[Early Warning Scores (NEWS2 / MEWS)]]` vs `Early Warning Scores (NEWS2 MEWS).md` (slash in link)

**Fix**: 
1. Use exact filename (no slashes, special chars) for WikiLinks
2. When hierarchy lists a topic, create the file with matching name, or update hierarchy link to match
3. Verify all links resolve after batch creation

### Hierarchy-Driven Topic Selection

Always read the chapter hierarchy file FIRST to determine the exact topic list, rather than relying on MOC starter queue alone. The hierarchy is the authoritative source for chapter coverage.
19. **Relying on file size as a completeness proxy.** File size ≥5KB does NOT guarantee all required sections exist. Must verify all 6 required sections: Learning Objectives, Management, MCQs, SBAs, Revision/One-page, Viva. In the Cardiology audit, 40 files were ≥5KB but only 25 had all sections.
20. **Assuming hierarchy display names match file names.** Display names in chapter hierarchy/MOC (e.g., "Atrioventricular block") often differ from actual file names (e.g., "AV block and conduction disorders.md"). Always build a mapping before cross-referencing.
21. **Failing to synchronize MOC and Hierarchy tracking files.** Both must be cross-validated against actual file content. In Cardiology, MOC claimed 40 complete; Hierarchy had 16; reality was 25. Update both together after verification.
22. **Missing duplicate skeleton directories.** Parallel scaffold directories (e.g., `Pericardial | Endocardial |+Inflammatory Cardiac Disease/` vs `Pericardial, Endocardial, and Inflammatory Cardiac Disease/`) cause confusion and false completion claims. Audit and remove duplicates before verification.
23. **Not checking for missing Viva sections.** Many files had LO, Management, MCQs, SBAs, Revision but lacked "Common Viva Questions". Batch-add missing sections systematically rather than one-by-one.

## Verification Checklist

- [ ] Topic is structured in Markdown
- [ ] Learning objectives are included when useful
- [ ] Anatomy and physiology are covered when relevant
- [ ] Normal values / important cut-offs are included where relevant
- [ ] Clinical discussion is exam-oriented
- [ ] High-yield FCPS/MRCP points are included
- [ ] Useful tables/comparison charts are included where appropriate
- [ ] Topic correlations are included where helpful
- [ ] A stepwise diagnostic or management approach is included where relevant
- [ ] Interpretation frameworks are included where relevant
- [ ] Treatment cautions, contraindications, major drug interactions, dose issues, and comorbidity issues are addressed where relevant
- [ ] Procedures / indications / contraindications are included where relevant
- [ ] Procedure mini-sections are included where relevant
- [ ] Red flags / emergencies are included where relevant
- [ ] Special situations are included where relevant
- [ ] Exactly 10 MCQs are included unless the user requests a different count
- [ ] Exactly 10 SBA questions are included unless the user requests a different count
- [ ] Flashcards are added when possible
- [ ] Mind map is added when possible
- [ ] Flowchart is added when possible
- [ ] Suggested visuals and/or video references are included when helpful
- [ ] One-page revision summary is included when feasible
- [ ] 24-hour recall prompts and/or spaced-revision tracker are included when useful
- [ ] Must-know prioritization is included where helpful
- [ ] Self-test scorecard is included when the user wants challenge-based revision
- [ ] Exam answer mode is matched to the user's request when specified
- [ ] Answer key with explanations is included
- [ ] User-specified chapter rules and references are followed
- [ ] When hierarchy mode was requested, the chapter MOC, hierarchy map, heading hubs, topic-group hubs, and disease-level files are all created or updated consistently
- [ ] Output is easy to edit later
- [ ] **DEEP VERIFICATION PASSED** (see `references/deep-verification-checklist.md`):
    - [ ] All hierarchy wiki-links match actual .md filenames
    - [ ] Every `status: full-fcps-mrcp-topic-note` file has all 5 required sections (MCQs, SBA, Flashcards, Answer Key, Must Know)
    - [ ] MOC ✅ count equals verified complete file count
    - [ ] Hierarchy status line reflects accurate completion numbers
