# Davidson Ch 17 Respiratory — Audit Case Study (2026-06-16)

## Scenario
User asked: "is Respiratory if fully complete with information or just scaffolded check /mnt/tb/Medicine/, check all files 1 by 1"

Previous session had ended with claim: "26/115 disease-level topics complete (23%)" — counting only the 9 root-level starter notes converted in that session.

## What the file-by-file audit revealed
- **Actual: 52/162 .md files (32%) were TRULY complete**, with the per-disease-level topic completion at **52/115 (45%)**
- The agent's 23% figure was based on **delta from this session**, not the actual on-disk state
- **38 disease-level notes in subdirectories** had been completed in a prior session and had full `## MCQs`, `## SBA`, `## Answer Key`, ≥10KB, 27+ sections — but the agent never re-counted them

## Status taxonomy discovered
| Status tag | Count | Notes |
|------------|-------|-------|
| `status: full-fcps-mrcp-note` | Many | Canonical, used by most subagents |
| `status: full-fcps-mrcp-topic-note` | Many | Variant — also means complete; same author, different label |
| `status: full-fcps-mrcp-hub` | 2 | MOC + Hierarchy only |
| `status: hierarchy-hub` | 36 | Topic-group hub files (navigation only) |
| `status: scaffold` | 43 | Pure stubs (1-5KB, headers only) |
| (no status) | 0 after audit | All files had a status after this session |

**The audit script MUST accept both `full-fcps-mrcp-note` and `full-fcps-mrcp-topic-note` as "complete" — they are equivalent in the chapter's history.**

## "Header says 10, body has 5" failure mode (24 files)
A specific pattern: 24 files had `## MCQs (10)` and `## SBA Questions (10)` headers but the bodies contained only 5 questions each. The headers were correct, the section structure was correct, but the question banks were truncated.

**Root cause:** Prior session built these files but ran out of time/context partway through, leaving the question banks half-complete. Status was set to "complete" prematurely.

**Detection:** Section header regex matches → but `^\d+\.\s+\S` count inside the body < 8. File is incomplete even though status is FULL.

## What worked in the audit
1. `execute_code` with `glob.glob('**/*.md', recursive=True)` + per-file read_file to get full content
2. Per-file `re.findall(r"^## ", content, re.MULTILINE)` to count sections
3. Per-file `re.search(r"## MCQs? \(?10?\)?[^\n]*\n(.*?)(?=\n## [^#]|\Z)", content, re.DOTALL)` to extract MCQ body
4. Per-file `len(re.findall(r"^\d+\.\s+\S", mcq_body, re.MULTILINE))` to count questions
5. Categorization: status tag + size + section count + real_q_count

## What to fix in this chapter (next session priority)
1. **24 files need MCQ/SBA completion** — most are scaffold+body with Q1-Q5 done, just need Q6-Q10 + answer key entries
2. **43 pure scaffolds need full content expansion** — these are 1.5KB stub files with 5 section headers and 0 content
3. **MOC "Suggested first full-note conversion queue"** needs every actually-complete file marked with ✅ (currently only 11 hub files shown)

## Lessons captured in SKILL.md
- Pitfall #19: Agent session-end completion claim can be 2× too low by ignoring pre-existing complete files
- Pitfall #20: Header-claim vs body-content mismatch in MCQ/SBA sections
- Trigger phrasing: "check all files 1 by 1" demands full re-audit, not delta summary

## Pattern for "honest progress report" session-end
After any batch note-creation session, BEFORE writing the session summary:
1. Run the audit script over the whole chapter
2. Count `truly_complete = [f for f in files if is_complete(f)]`
3. Report `len(truly_complete) / total` as the progress percentage
4. Cross-check against MOC's own claim and flag any divergence
5. List BOTH the "newly added in this session" delta AND the total

Never report a completion percentage based on the delta alone — always re-audit.
