# Batch Completion Workflow for Chapter Disease-Level Notes

Distilled from the Davidson Chapter 23 (Gastroenterology) completion session where 111 disease-level files were upgraded from partial/scaffold to full FCPS/MRCP template standard.

## When to Use
- A chapter folder contains N disease-level files (typically 50-150) with varying completeness
- The task is to bring ALL files to uniform full-template standard in a single session
- Files share a common 14-section template but differ in which sections are missing

## Workflow

### 1. Audit & Categorize (5-10 min)
Run a script to check each file for presence of core sections:
```python
core_sections = ['Learning Objectives', 'Mind Map', 'Flowchart', 'Must Know',
                 'Self-Test Scorecard', 'Revision Prompts', 'Answer Key']
```
Group files by what they're missing:
- **Group A**: Has LO, MM, FC → needs Must Know, Scorecard, Answer Key
- **Group B**: Missing LO, MM, FC → needs everything
- **Group C**: Core disease files → needs Must Know, Scorecard
- **Group D**: Symptom/investigation/management topics → vary

### 2. Process by Category (parallelizable)
For each category, write a single `execute_code` script that:
- Reads each file
- Finds insertion point (before `## Answer Key Pearls` or at end)
- Appends missing sections with topic-specific content
- Writes back

**Key technique**: Use generic template suffix with topic-specific `must_know` arrays defined in a dict at top of script. Process 10-25 files per script to stay under token limits.

### 3. Verify & Iterate
Run `chapter_verify.py` after each batch. Fix any remaining gaps.

## Time Estimates
- Audit: 5 min
- Per file (scripted batch): ~10-30 sec
- 111 files × 3 batches: ~1-2 hours total wall time
- Verification: 30 sec

## Pitfalls & Fixes

| Pitfall | Fix |
|---------|-----|
| Status tag mismatch (`full-fcps-mrcp-topic-note` vs `full-fcps-mrcp-note`) | Patch `chapter_verify.py` to accept both |
| `write_file` timeout on large files | Use `patch` to append sections; cap single write at ~25KB |
| Token limit on large batch scripts | Split into multiple `execute_code` calls (10-25 files each) |
| Template drift across batches | Define ONE canonical `topic_specific` dict per batch; don't re-type |
| Missing MCQ/SBA extraction | Use regex to pull from existing file before appending Answer Key |

## Template Components to Append (in order)
1. `## Mind Map` (mermaid)
2. `## Flowchart` (mermaid)
3. `## Must Know / Should Know / Nice to Know`
4. `## Self-Test Scorecard`
5. `## Revision Prompts`
6. `## Answer Key with Explanations` (extracted MCQ/SBA explanations)

## Reference File
Use the canonical complete file as structural reference:
`/mnt/tb/Medicine/Gastroenterology/Oesophageal Disorders/Gastro-oesophageal reflux disease.md`
(~23KB, all sections present, verified template)