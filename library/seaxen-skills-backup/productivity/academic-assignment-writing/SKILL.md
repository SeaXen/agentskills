---
name: academic-assignment-writing
description: Write and package submission-ready academic assignments, especially Bangla university-style essays with optional department framing, references, and PDF export.
version: 1.0.0
author: Hermes Agent
license: CC0-1.0
metadata:
  hermes:
    category: productivity
    tags: [academic-writing, assignments, essay, bangla, markdown, pdf, formatting]
---

# Academic assignment writing

Use this skill when the user asks for an assignment, essay, term paper, short academic note, or submission-ready `.md` / PDF deliverable for school, college, or university.

This skill is especially useful for:
- Bangla assignments that should sound natural and handwritten rather than robotic
- University submission style formatting with title, submission block, headings, conclusion, and references
- Department-specific reframing, such as Islamic Studies, where the same topic needs discipline-relevant references or vocabulary
- Deliverables that must be provided both as Markdown and PDF

## Core approach

1. **Detect the academic context first.**
   - Identify level: school, college, university.
   - Identify department/course if mentioned.
   - Identify required tone: simple, formal academic, exam-style, handwritten-sounding, or highly referenced.
   - Identify delivery format: plain text, `.md`, PDF, or both.

2. **Shape the structure before drafting.**
   - For university submission style, include:
     - assignment title
     - submission information block
     - introduction
     - concept/definition section
     - analysis/body sections
     - context-specific section(s)
     - conclusion
     - references
   - Keep headings explicit and readable.

3. **Write in a human, student-like voice.**
   - Avoid chatbot phrases.
   - Avoid over-polished corporate vocabulary.
   - Keep paragraph rhythm varied.
   - If the user asked for a humanized tone, make it readable aloud and plausible as student writing.

4. **Adapt to the department, not just the topic.**
   - Reframe examples and references based on discipline.
   - Example: for Islamic Studies, discuss the topic through justice, coexistence, moral reasoning, and relevant Qur'anic / historical references where appropriate.
   - Add references only when they actually fit the framing; do not stuff citations in mechanically.

5. **Package the deliverable cleanly.**
   - Save the output as `.md` when requested.
   - If the user asks for a file only, write the file directly instead of pasting the full essay again.
   - If the user gives a target word range, verify the final saved file and adjust the content until it falls inside the requested range.
   - If the user also wants PDF, generate it if the environment permits and verify the file exists.

## Recommended structure by level

### School / college
- simpler vocabulary
- shorter paragraphs
- direct explanation
- minimal references unless requested

### University submission style
- formal heading
- submission metadata block
- academically toned introduction
- conceptual framing, historical/contextual discussion, critical analysis
- conclusion written as synthesis, not just repetition
- references section, even if brief

## Department-specific adaptation

### Islamic Studies framing
When the user asks for an assignment under Islamic Studies:
- Keep the tone academic, not preachy.
- Distinguish between a modern political concept and Islamic ethical/legal thought.
- If relevant, add Qur'anic references on:
  - no compulsion in religion
  - justice toward others
  - human diversity and mutual recognition
  - peaceful coexistence / distinct belief communities
- Useful references from this session:
  - Surah Al-Baqarah 2:256
  - Surah Al-Ma'idah 5:8
  - Surah Al-Hujurat 49:13
  - Surah Al-Kafirun 109:6
  - Charter of Madinah / Madinah Constitution as a coexistence example
- Present the relationship carefully: do not claim Islam and secularism are identical; explain overlaps and differences with nuance.

## PDF export workflow

### Preferred order
1. Use existing document converters if available: `pandoc`, `wkhtmltopdf`, `libreoffice`, `soffice`.
2. If none are available and the document is Bangla, use the fallback described in `references/bengali-pdf-export.md`.
3. Verify the output file exists and has non-zero size before delivering it.

## Pitfalls

- Do not treat "university submission style" as just a nicer essay. It usually needs a submission info block and reference section.
- Do not assume "humanized" means casual. Often it means natural, readable, and not obviously AI-generated.
- Do not add religious references mechanically. Under Islamic Studies, they should support analysis, not replace it.
- When the user asks to "add more topic" to an existing assignment, expand the same document section-by-section with relevant subheadings instead of replacing the whole piece with a new draft.
- For biography or comparative-religion assignments, useful expansion topics include: knowledge contribution, personality and character, social/political role, educational lessons, and historical impact.
- Do not promise PDF unless you have actually generated and verified it.
- For Bangla PDF export, do not assume default system fonts can render Bengali.

## Verification checklist

Before finalizing:
- Does the output match the requested academic level?
- Does the department framing appear in the body, not only the title?
- Are references relevant and non-random?
- If PDF was requested, does the file exist and openable-size look reasonable?
- If both `.md` and PDF were requested, are both saved?

## Support files

- `references/bengali-pdf-export.md` — fallback method for generating Bengali PDFs when common converters are missing.

## Output pattern

When returning files, provide a brief summary of what changed and attach the requested deliverables directly.
