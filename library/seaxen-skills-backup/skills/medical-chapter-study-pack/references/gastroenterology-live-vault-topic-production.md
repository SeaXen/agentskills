# Gastroenterology live vault topic production

Proven workflow for this user's Davidson Chapter 23 Gastroenterology channel.

## Scope and chapter boundary
- Root: `/mnt/tb/Medicine/Gastroenterology/`
- Chapter boundary: **Davidson Chapter 23 only**
- Keep **Hepatology** fully separate as **Davidson Chapter 24**
- Do not mix hepatitis, jaundice/LFT interpretation, cirrhosis, portal hypertension, ascites, hepatic encephalopathy, or liver failure into Gastroenterology work
- Keep luminal GI disease, GI bleeding, endoscopy/investigation, malabsorption, IBD/functional bowel disease, colorectal/anal disease, and pancreatic disease inside Gastroenterology

## Source split
- Anatomy: **Gray's + Davidson**
- Physiology: **Guyton & Hall + Ganong + Davidson**
- Clinical discussion: **Davidson + PasTest + personal notes**

## Output standard
Use FCPS/MRCP-oriented, Obsidian-friendly Markdown. When relevant, include:
- definition
- anatomy
- physiology
- classification
- etiology / risk factors
- pathophysiology
- clinical features
- investigations
- interpretation frameworks
- diagnosis
- differential diagnosis
- management
- complications
- red flags / emergencies
- one-page summary
- revision prompts
- 10 MCQs
- 10 SBAs
- flashcards

High-yield emphasis areas:
- dysphagia logic and alarm features
- dyspepsia / *H. pylori* / peptic-ulcer logic
- upper-GI bleed severity and resuscitation logic
- chronic diarrhoea / malabsorption / coeliac differentiation
- IBD vs IBS vs infective bowel disease differentiation
- colorectal cancer clues and lower-GI bleeding logic
- pancreatitis severity, complications, and red flags
- common exam traps and viva traps

## Minimal-read operating rule
Normal working set per task:
1. `Gastroenterology MOC.md`
2. the exact target note
3. maximum **1 directly relevant hub**

Rules:
- Do **not** read the full chapter tree by default
- Do **not** inspect extra hubs, hierarchy notes, or unrelated chapter notes unless the user widens scope
- Reuse the existing scaffold note if it already exists; do not create duplicate parallel notes
- Upgrade only the exact requested topic in place
- Update only `Gastroenterology MOC.md` and the same directly relevant hub when needed

## `next N` behavior
- Treat `next 1`, `next 3`, `next 5`, etc. as **exact batch sizes**
- Use the live `Gastroenterology MOC.md` to identify the next visible pending topics
- If the next visible `N` topics cross more than one hub while the turn still has a **max 1 hub** restriction, stop and ask before widening scope
- If the user repeats or clarifies that they want the full cross-hub batch (for example `5 topic` or `next 5` after being warned), treat that as permission for that turn to read the exact target notes plus the necessary touched hubs and complete the batch

## Navigation update rule
After completing a topic or approved batch:
- update `Gastroenterology MOC.md` if needed
- update only the directly touched relevant hub(s) if needed
- mark completed entries with `✅` where that convention is already in use
- avoid broad cleanup outside the working set

## Git rule
When the chapter rule says to push after completion:
- stage only Gastroenterology-path changes for the batch: `git add -- 'Gastroenterology'`
- commit with a gastro-specific message
- push to the active branch/remote
- verify clean scope with: `git status --short -- Gastroenterology`

## Progress-counting notes
Useful cross-checks from session:
- completed full notes: search for `^status:\s*full-fcps-mrcp-topic-note$`
- remaining scaffolds: search for `^status:\s*scaffold$`
- when reporting counts, prefer the live `Gastroenterology MOC.md` as the source of truth and use status searches as a cross-check

## Pitfalls
- Silently widening beyond the exact requested topic or batch
- Crossing into Hepatology because of nearby liver-related GI topics
- Reading extra hubs or chapter files despite the minimal-read rule
- Creating duplicate notes instead of upgrading the existing scaffold in place
- Forgetting to update the MOC/hub markers after writing
- Running a broad repo commit instead of a gastro-only path-scoped commit
- Assuming a cross-hub `next 5` is allowed without user confirmation under a strict one-hub rule
