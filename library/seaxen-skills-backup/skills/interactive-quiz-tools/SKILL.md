---
name: interactive-quiz-tools
description: "Build interactive study/quiz UIs (exam, flashcard, scenario, viva) on top of structured markdown content. Covers MD-content to JSON DB extraction, browser-side quiz/flashcard engine (timer, history, analytics, localStorage), static-site deployment via the docker-cp shortcut. Use when the user asks to build an exam page, make flashcards interactive, create a quiz from MCQs/SBAs, extract questions and build a tool, or make the MCQ/SBA sections clickable. Applies to any structured content with MCQs, SBA Questions, and Flashcards sections (MedSea topic.md files, Obsidian notes, Notion exports, etc.)."
version: 1.0.0
author: Hermes Agent
license: CC0-1.0
metadata:
  hermes:
    category: productivity
    tags: [study-tools, quiz, flashcards, mcq, sba, interactive, static-site, exam-prep]
---

# Interactive Quiz Tools

**Class-level skill for building interactive study/quiz UIs (exam trainers, flashcard systems, scenario tools) on top of structured markdown content.** This skill is the consumer side of `medical-fcps-mrcp-exam-notes` (which produces the source MDs) — it takes the `## MCQs` / `## SBA Questions` / `## Flashcards` sections in those notes and turns them into a working browser-based quiz/flashcard app with timer, history, analytics, and localStorage persistence.

## When to Use This Skill

**Always use when:**
- User asks to "build an exam page" / "make a quiz" / "interactive MCQ test" from existing notes
- User wants flashcards to be "clickable" / "flip" / "rated" rather than just rendered
- User wants timer + submit + score + history + analytics on top of MCQ/SBA/Flashcard sections
- User references "FCPS/MRCP exam mode" or "viva practice tool" in a UI context
- The source content already has `## MCQs`, `## SBA Questions`, `## Flashcards` sections (in MedSea topic.md or any markdown)

**Don't use when:**
- Creating the MCQ/SBA/Flashcard SECTIONS themselves (use `medical-fcps-mrcp-exam-notes` for the note format)
- Just rendering a static page with questions listed (this skill is for INTERACTIVE tools)
- Building Notion-side quizzes (this skill targets static HTML/JS for `medsea` docker container)
- Single-file micro-quizzes with no timer/history/analytics (overkill — use raw HTML)

## The Class Pattern (3 phases)

```
[MARKDOWN NOTES with ## MCQs / ## SBA Questions / ## Flashcards sections]
         |
         v  PHASE 1 — EXTRACT
  Python state-machine parser (NEVER regex backtracking)
         |
         v
  /assets/questions.json  (3-5 MB; indexed by chapter; mcq/sba/flashcard pools)
         |
         v  PHASE 2 — BUILD UI
  Shared engine.js  ---+
  /exam/index.html   ---+   (one HTML+JS per tool; shares engine + DB)
  /exam/app.js       ---+
  /flashcards/...    ---+
         |
         v  PHASE 3 — DEPLOY
  docker cp + chmod -R a+r  (fast-iteration shortcut; see "Deployment" below)
  git add + commit
```

**Why this works:** The same `questions.json` powers any number of interactive UIs (exam, flashcards, OSCE scenarios, viva, etc.). The shared engine provides DB loading, history, timer, format helpers — each new tool is just an HTML/JS file that calls `MedSea.Engine.startExam({...})` or `MedSea.Engine.startFlashcards({...})`.

## Phase 1 — MD Content Extraction (CRITICAL PITFALLS)

### Two-pass architecture (explicit + auto-generated questions)

**Default path:** use the two-pass design below when you want maximum coverage.

**Quality fallback:** if the user reports the live bank is full of junk prompts, malformed options, or contextless questions, switch to an **authored-only rebuild** instead of trying to salvage the generated JSON. See `references/authored-only-question-bank-rebuild.md`.

**Always start with this two-pass design BEFORE writing any parser** when the source content is clinical/educational markdown (textbooks, study notes):

1. **Pass 1 — index all files**: walk `diseases/*/topic.md` (subdirectories) AND `diseases/*.md` (flat files). Flat files exist in older chapters — see "Flat-file indexing pitfall" below.
2. **Pass 1.5 — collect chapter fact pools**: for each chapter, parse "High-Yield / Definitions / Key Facts / One-Page" tables into a per-chapter `global_facts` list. These are needed as MCQ distractors in Pass 2.
3. **Pass 2 — extract + auto-generate**:
   - If topic.md has `## MCQs` / `## SBA Questions` / `## Flashcards` sections → parse them explicitly (state machine, see below)
   - **ALSO** auto-generate from clinical content sections:
     - `## 9. Viva Questions` tables (Q | Expected Answer) → flashcards 1:1
     - `## 8. FCPS/MRCP High-Yield Summary` / `## Definitions / Key Concepts` / `## Key Facts` tables (Topic | Fact) → MCQs with chapter-fact distractors
     - `## 12. One-Page Revision Card` tables → flashcards
   - If topic.md has NO explicit sections → still auto-generate from the clinical content sections (this is how all 32 chapters got covered)

**Validated result (MedSea 2026-06-21):** With explicit-only extraction, only 17/32 chapters had questions (most topic.md files don't have `## MCQs` sections — they have clinical content instead). After adding auto-generation, **all 32 chapters** have questions: 19,489 MCQs + 2,283 SBAs + 20,813 flashcards = 42,585 total. See `references/auto-generation-from-clinical-content.md` for the full algorithm.

### Flat-file indexing pitfall (validated 2026-06-21)

Older MedSea chapters (Ch 1-9, 17, 20) keep their topic files as **flat `.md` files in `diseases/`** rather than in subdirectories. A naive `for tdir in diseases.iterdir(): if tdir.is_dir(): ...` walker misses all of them.

```python
# WRONG — only catches subdir topics
for tdir in d.iterdir():
    if not tdir.is_dir(): continue
    md = tdir / 'topic.md'

# RIGHT — index both layouts
for tdir in d.iterdir():
    if tdir.is_dir():
        md = tdir / 'topic.md'
        if md.exists(): file_index.append(...)
for md in d.glob('*.md'):
    stem = md.stem.lower()
    if 'moc' in stem or 'hierarchy' in stem: continue  # skip overview files
    file_index.append(...)
```

### Per-topic density caps (validated 2026-06-21)

Without caps, auto-generation can produce 5-30 MCQs per topic (one per table row), exploding the DB to 18,000+ MCQs for ~3,000 topics. Cap at the generator level, not after extraction:

```python
if len(mcqs) > 8: mcqs = mcqs[:8]      # keep first 8 facts as MCQs
if len(flashes) > 10: flashes = flashes[:10]  # keep first 10 flashcards
```

Prefer earlier rows (definitions, top of section) over later ones — they're typically more fundamental.

### Why NOT regex backtracking

`re.findall(r'(?ms)^(\d+)\.\s+\*\*(.+?)\*\*\s*\n((?:^[ ]*[A-D]\.\s+.+\n?){2,4})\s*\*Answer:\s*([A-D])\*\s*\n', section)` works for ONE format. As soon as the source has multiple formats, regex with greedy/non-greedy backtracking will:
- Take 5-15 minutes for 1,400 files (CPU pinned at 95%, no progress)
- Miss sections where the answer line is `**Answer: A**` instead of `*Answer: A*`
- Misparse numbered list items in tables as questions
- Drop 60-90% of questions

**Validated pitfall (MedSea, 2026-06-21):** First regex-based extractor got 361 MCQs out of expected 1,373. The state-machine rewrite got 1,776 MCQs in 12 seconds.

### The state-machine pattern (working code)

```python
def parse_topic(text, chapter_num, chapter_name, chapter_slug, topic_slug):
    section = None           # None | 'mcq' | 'sba' | 'flash'
    cur_q = None             # dict being built for current MCQ/SBA
    expecting_options = False
    cur_flash = None

    def push_q(kind):
        if cur_q and cur_q.get('stem') and cur_q.get('answer') and cur_q.get('options'):
            if cur_q['answer'] in cur_q['options']:
                # ... append to mcqs[] or sbas[]
        cur_q = None; expecting_options = False

    # Form A: "1. **Hyponatraemia is defined as..."  (opens ** but no close)
    # Form B: "1. **Q:** Which of the following..."  (**Q:** then text)
    # Form C: "1. **Question:** stem" (rare)
    NUM_RE = re.compile(r'^\s*(\d+)\.\s+(.+?)\s*$')
    OPT_RE = re.compile(r'^\s*([A-E])\.\s+(.+?)\s*$')
    # Answers: "*Answer: X*" or "**Answer: X**" or "Answer: X"
    ANS_RE = re.compile(r'^\s*\**\s*Answer\s*:?\s*\**\s*([A-E])\s*\**\s*$', re.IGNORECASE)

    def extract_stem(line):
        s = line.strip()
        m = re.match(r'^\d+\.\s+(.*)$', s)
        if not m: return None
        rest = m.group(1).strip()
        if rest.startswith('**'):
            inner = rest[2:]
            if inner.startswith('**'):
                return inner.rstrip(':').rstrip('*').strip()
            qm = re.match(r'^(Q|Question)\s*:\s*\**\s*(.*?)\**\s*$', inner, re.IGNORECASE)
            if qm: return qm.group(2).strip()
            return inner.rstrip(':').rstrip('*').strip()
        return rest

    for line in text.splitlines():
        if line.startswith('## ') and not line.startswith('### '):
            # flush previous section
            if section in ('mcq', 'sba'): push_q(section)
            elif section == 'flash': flush_flash()
            h = line[3:].strip().lower()
            if h.startswith('mcq'): section = 'mcq'
            elif 'sba' in h: section = 'sba'
            elif 'flashcard' in h: section = 'flash'
            else: section = None
            continue

        if section in ('mcq', 'sba'):
            stripped = line.rstrip()
            # Try new numbered question first (only when not currently parsing options)
            if not expecting_options and re.match(r'^\s*\d+\.\s+', stripped):
                stem = extract_stem(stripped)
                if stem and len(stem) > 5:
                    push_q(section)
                    cur_q = {'stem': stem, 'options': {}, 'answer': None}
                    expecting_options = True
                    continue
            if expecting_options and cur_q:
                m = OPT_RE.match(stripped)
                if m: cur_q['options'][m.group(1)] = m.group(2); continue
                m = ANS_RE.match(stripped)
                if m: cur_q['answer'] = m.group(1).upper(); expecting_options = False; continue
                if stripped == '': expecting_options = False; continue
                # Non-blank non-option non-answer: end current Q, treat as content
                expecting_options = False

        elif section == 'flash':
            stripped = line.rstrip()
            # Format A: "- Q: ...\n  A: ..."
            m = re.match(r'^\s*-\s+Q:\s*(.+)$', stripped)
            if m: flush_flash(); cur_flash = {'front': m.group(1).strip(), 'back': None}; continue
            m = re.match(r'^\s*A:\s*(.+)$', stripped)
            if m and cur_flash: cur_flash['back'] = m.group(1).strip(); continue
            # Format B: "**Q:** ...\n**A:** ..."
            m = re.match(r'^\s*\*\*Q:\*\*\s*(.+)$', stripped)
            if m: flush_flash(); cur_flash = {'front': m.group(1).strip(), 'back': None}; continue
            m = re.match(r'^\s*\*\*A:\*\*\s*(.+)$', stripped)
            if m and cur_flash: cur_flash['back'] = m.group(1).strip(); continue
            # Format C: "- **Q:** ..." (dash + bold Q)
            m = re.match(r'^\s*-\s+\*\*Q:\*\*\s*(.+)$', stripped)
            if m: flush_flash(); cur_flash = {'front': m.group(1).strip(), 'back': None}; continue

    # flush at EOF
    if section in ('mcq', 'sba'): push_q(section)
    if section == 'flash': flush_flash()
    return mcqs, sbas, flashes
```

**Key design choices:**
1. **Accept A-E options** (not just A-D). MedSea has 5-option MCQs in some files; the strict A-D regex silently drops 5-option questions.
2. **Self-declaring question detection**: a numbered line `N. ...` is only a question if it's followed by option lines within the same block. If the next non-blank line is not `A.`/`B.`/etc., treat the line as content (table row, list item) and don't enter `expecting_options` mode. This avoids misfiring on numbered list items in other sections.
3. **Bail out on unexpected non-blank lines** while `expecting_options`: set `expecting_options = False` and fall through. Next numbered line gets a fresh attempt.
4. **Split parser into a separate module** (`parser_lib.py`) so test scripts can `import` it without triggering the main loop. Loading a script that has main code under `if __name__ != '__main__':` does NOT prevent import side effects in some setups. Explicit split is safer.

### The MedSea topic.md format variations (validated 2026-06-21)

| Format | Stem line | Answer line | Flashcard line |
|---|---|---|---|
| **A** (Ch 19 Biochem — hyponatraemia) | `1. **Hyponatraemia is defined as...:**` (no close) | `*Answer: B*` | `- Q: ...\n  A: ...` |
| **B** (Ch 26 Derm — ichthyosiform) | `1. **Q:** Which of the following...` (`**Q:**` then text) | `**Answer: A**` (5 options A-E) | `- **Q:** ...\n  **A:** ...` |
| **C** (Ch 11 Poisoning) | varies | varies | varies |

All three must be supported. The state machine above handles A, B, and C.

### Output schema (`/assets/questions.json`)

### Quality gates before deploying a rebuilt bank

When the issue is **question quality**, not just parser coverage, run explicit structural gates before copying JSON into the live site:
- MCQ one-option count must be 0
- MCQ `<4 options` count must be 0
- MCQ missing-answer count must be 0
- MCQ leading `Q:` count should be 0 after normalization
- banned generic/contextless stems should be 0 (`What is the first-line treatment?`, `What is the diagnosis?`, etc.)
- SBA malformed count must be 0
- flashcard fronts should be normalized into prompt/question form when possible

If those checks fail, **do not deploy**. Rebuild with stricter keep-rules. The worked MedSea fallback is documented in `references/authored-only-question-bank-rebuild.md`.

```json
{
  "generated_at": "2026-06-21T13:50:00Z",
  "version": 2,
  "totals": {"mcq": 1776, "sba": 2058, "flashcard": 6808, "chapters": 17},
  "chapters": [
    {"num": 19, "slug": "19-clinical-biochemistry-and-metabolic-medi", "name": "...",
     "mcq_count": 280, "sba_count": 140, "flashcard_count": 140, "topic_count": 28},
    ...
  ],
  "mcq": [
    {"id": "a4baca7bebb9", "chapter_num": 19, "chapter_name": "...",
     "chapter_slug": "...", "topic_slug": "19.2.3-hyponatraemia",
     "question": "Hyponatraemia is defined as serum sodium:",
     "options": {"A": "<130 mmol/L", "B": "<135 mmol/L", "C": "<140 mmol/L", "D": "<125 mmol/L"},
     "answer": "B"},
    ...
  ],
  "sba": [...], "flashcard": [...]
}
```

**File size budget:** 1,776 MCQs + 2,058 SBAs + 6,808 flashcards + 17 chapter metadata = ~3.2 MB minified JSON. gzipped ~600 KB. Loaded once on page open; cached by browser after first visit.

## Phase 2 — Interactive UI Architecture

### The shared engine pattern (one `engine.js`, many tools)

```javascript
// /assets/exam-engine.js — exposes window.MedSea = {DB, Engine, History, Format}
(function () {
  'use strict';

  // DB loader with fetch + cache
  var DB = {
    load: function() { /* fetch('/assets/questions.json') + cache */ }
  };

  // localStorage-backed history
  var History = {
    add: function(rec) { /* push to localStorage['medsea_exam_history_v1'] */ },
    exams: function() { return this.all().filter(r => r.type === 'exam'); },
    flashes: function() { return this.all().filter(r => r.type === 'flashcard'); },
    byChapter: function(type) { /* aggregate accuracy per chapter */ },
    stats: function() { /* total attempts, accuracy, retention, streak */ }
  };

  // Exam runner
  function startExam(cfg) {
    // cfg: {questions, duration_sec, title, chapters, mode, question_types}
    // returns state object with: idx, answers, submit(), goto(), next(), prev()
    // auto-submits on timer expiry; pushes to History on submit
  }

  // Flashcard runner
  function startFlashcards(cfg) {
    // cfg: {cards, duration_sec, title, chapters}
    // returns state with: idx, ratings, flip(), rate(qid, 'known'|'hard'|'unknown'|'skip')
  }

  // Pool filter helpers
  var Pool = { filter: function(pool, filters) { /* by chapter */ },
               shuffle: function(arr) { /* Fisher-Yates */ },
               pick: function(arr, n) { /* shuffle + slice */ } };

  // Format helpers
  var Format = { fmtTime: function(sec) { /* mm:ss */ },
                 fmtDate: function(iso) { /* toLocaleString */ },
                 pct: function(n, d) { /* round(100*n/d) */ } };

  window.MedSea = { DB, Engine: {startExam, startFlashcards}, History, Format, Pool };
})();
```

**Why this design:** Each new tool (exam, flashcard, OSCE, viva) is just a thin HTML/JS file. Adding a viva tool = copy the flashcard HTML, change `MedSea.Engine.startFlashcards` to a new `startViva` that returns audio prompts + rating. No re-implementation of timer/history/analytics.

### Each tool page (single-file pattern)

```html
<!DOCTYPE html>
<!-- /exam/index.html — copy this skeleton, change tool-specific fields -->
<header><!-- nav, chapter stats --></header>
<main>
  <div class="tabs"><!-- Setup | Runner | Result | History | Analytics --></div>

  <section class="panel" id="panel-setup">
    <!-- chapter chips, mode toggles, count + time inputs, start button -->
  </section>

  <section class="panel" id="panel-runner">
    <!-- sticky bar: progress + timer + quit/submit -->
    <!-- question card with clickable options -->
    <!-- prev/next + question palette -->
  </section>

  <section class="panel" id="panel-result">
    <!-- hero score + grade label -->
    <!-- stat cards: correct/incorrect/skipped/time/per-Q -->
    <!-- review list: each question with your answer + correct answer + color border -->
  </section>

  <section class="panel" id="panel-history"><!-- past attempts --></section>
  <section class="panel" id="panel-analytics"><!-- overview + chapter bars + streak --></section>
</main>

<script src="/assets/exam-engine.js"></script>
<script src="/exam/app.js"></script>
```

### Feature checklist for "beast mode" tools (user preference)

User said "make it beast and as much as option possible" and "give me you best 10/10". When building interactive tools, include ALL of these — they're expected, not optional:

| Feature | Exam | Flashcard | Why |
|---|---|---|---|
| **Chapter multi-select** (chips, not dropdown) | yes | yes | Want to study specific chapters, not "all" |
| **Quick presets** (All / Clinical / System / Clear) | yes | yes | One-click for common selections |
| **Live question count** (e.g. "2058 matching") | yes | yes | Avoid setting impossible count |
| **Question type toggle** (SBA / MCQ / Both) | yes | N/A | Different exam styles |
| **Card count** | yes | yes | 1-500 |
| **Time limit** (optional, with auto-submit) | yes | yes | Real exam simulation |
| **Shuffle** (yes/no) | yes | yes | Avoid memorization by position |
| **Show-answer mode** (each Q / end only) | yes | N/A | Study vs test mode |
| **Order** (random/sequential) | N/A | yes | Flashcard study patterns |
| **Card flip mode** (flip+rate / quick read) | N/A | yes | Different learning styles |
| **Auto-flip timer** (off/5s/10s) | N/A | yes | Practice auto-recall |
| **Keyboard shortcuts** (Space/1/2/3/left/right) | N/A | yes | Speed of use |
| **Sticky progress bar** with timer warn/danger states | yes | yes | At-a-glance status |
| **Question palette** with per-question state colors | yes | yes | Jump to any question |
| **Hero result** with grade label (Outstanding/Strong/Pass/Below/Fail) | yes | yes | Instant feedback |
| **Per-question review** with your-answer vs correct-answer | yes | N/A | Learn from mistakes |
| **Weak cards list** in flashcard result | N/A | yes | Re-study what you missed |
| **History tab** with all past attempts | yes | yes | Track improvement |
| **Replay exam** button (re-do same questions) | yes | N/A | See if you improved |
| **Analytics tab** with overview cards | yes | yes | Cross-tool stats |
| **Chapter-wise accuracy bars** (color-coded) | yes | yes | Identify weak chapters |
| **Daily streak counter** | yes | yes | Habit building |
| **localStorage persistence** (no server needed) | yes | yes | Privacy + works offline |
| **Responsive** (works on mobile + tablet) | yes | yes | Study anywhere |
| **Dark mode** (matches MedSea design system) | yes | yes | Consistent UX |
| **Toast notifications** (toast(msg)) | yes | yes | Non-blocking feedback |
| **Confirm dialogs** for destructive actions (quit/clear) | yes | yes | Prevent data loss |

## Phase 3 — Deployment (Docker-Cp Fast Iteration)

**The MedSea container is built with `COPY site/` in the Dockerfile — NOT a bind mount.** New files added to the host `site/` directory do NOT appear in the running container. Two deployment options:

### Option A — `docker cp` fast iteration (USE THIS DURING DEVELOPMENT)

```bash
# Copy new files into the running container
docker cp /mnt/tb/Sea-knowledge/#MedSea/site/exam medsea:/usr/share/nginx/html/exam
docker cp /mnt/tb/Sea-knowledge/#MedSea/site/flashcards medsea:/usr/share/nginx/html/flashcards
docker cp /mnt/tb/Sea-knowledge/#MedSea/site/assets/questions.json medsea:/usr/share/nginx/html/assets/questions.json
docker cp /mnt/tb/Sea-knowledge/#MedSea/site/assets/exam-engine.js medsea:/usr/share/nginx/html/assets/exam-engine.js

# CRITICAL — fix permissions (docker cp preserves restrictive host perms; nginx can't read 600 files)
docker exec medsea chmod -R a+r /usr/share/nginx/html/exam /usr/share/nginx/html/flashcards /usr/share/nginx/html/assets

# Verify all endpoints return 200
curl -s -o /dev/null -w "%{http_code} %{size_download}b\n" http://localhost:8855/exam/
curl -s -o /dev/null -w "%{http_code} %{size_download}b\n" http://localhost:8855/assets/questions.json
```

**Time:** ~3 seconds vs 5+ minutes for a full `docker build --no-cache`. Use during development.

### Option B — full Docker rebuild (USE THIS BEFORE FINAL DEPLOY / container restart)

```bash
cd /mnt/tb/Sea-knowledge/#MedSea
docker build --no-cache -t medsea-site:latest .  # ~5 min for 1.2GB site
docker stop medsea && docker rm medsea
docker run -d --name medsea --restart unless-stopped -p 8855:80 medsea-site:latest
curl -s -o /dev/null -w "HTTP %{http_code}\n" http://localhost:8855/
```

**CRITICAL — `-p 8855:80` not `-p 8855:8855`:** nginx inside the container listens on port 80 (see `docker/nginx.conf`). Mapping host 8855 to container 8855 leaves the port unmapped → curl returns HTTP 000 even though container is "Up". Validated 2026-06-21.

### The `chmod -R a+r` pitfall (validated 2026-06-21)

`docker cp` from the host preserves restrictive file permissions (often 600 from how the host wrote them). nginx in the container runs as `nginx` user (uid 101) and CANNOT read 600 files. Result: `GET /exam/` returns 403 Forbidden even though the file exists.

**Fix:** `docker exec medsea chmod -R a+r <new-dirs>` after every `docker cp`. Alternatively, copy with explicit perms:

```bash
docker cp --follow-link=false /path/to/file medsea:/dest/  # doesn't help
# OR rebuild the image (COPY preserves source perms which you can set first)
chmod -R a+r /path/to/site/{exam,flashcards,assets} && docker build ...
```

### Pretty-URL routing

The MedSea nginx config has `try_files $uri $uri/ $uri/index.html /index.html;` — so `/exam/` automatically serves `/exam/index.html` (no special rewrite needed). Just drop `index.html` in the directory and the URL works.

## Browser Verification Pattern

### Snapshot/DOM mismatch pitfall (validated during MedSea UI QA)

Sometimes browser automation shows a rich accessibility snapshot but `browser_console` DOM evaluation returns an empty or stale document. Treat that as a **browser-automation inconsistency**, not immediate proof the site is blank.

When that happens:
1. verify server output with `curl` first (HTML size, markers, content-type)
2. add cache-busting query params when reloading (`?v=...`)
3. use `browser_vision` on the actual rendered page for the final truth on what a user sees
4. for JSON-backed apps, verify the live chunk endpoints directly with `curl` and then confirm the UI counters/state from the browser

Do not conclude "page is blank" from DOM-eval alone if the snapshot or vision view disagrees.

For interactive tools that use `localStorage` and `confirm()` dialogs, the browser_console testing pattern needs two adjustments:

```javascript
// 1. Bypass confirm() for automated tests
window.confirm = () => true;

// 2. Trigger the action that depends on confirm
document.getElementById('btn-submit').click();

// 3. Check result panel rendered
document.querySelector('.result-score').textContent
// -> "X / Y" (note: the textContent concatenates spans, so "0/20" + "0%" appears as "0/200%")
//   This is a textContent artifact, not a bug. The visual rendering is correct.

// 4. Check history panel
document.querySelectorAll('.hist-item').length  // >=1 after a submit

// 5. Check analytics panel
document.querySelectorAll('.analytics-card').length  // >=3
document.querySelectorAll('#ch-bars .bm-row').length  // >=1 if history exists
```

## Reference Files

| File | Purpose |
|---|---|
| `references/medsea-topic-md-formats.md` | Full catalogue of MCQ/SBA/Flashcard format variations found in MedSea topic.md files. Use this BEFORE writing a parser — confirm whether the new source chapter matches an existing format or introduces a new one |
| `references/docker-cp-shortcut.md` | Detailed docker-cp vs docker-build tradeoffs, the `chmod -R a+r` pitfall, and the `-p 8855:80` port mapping rule |
| `references/localstorage-history-schema.md` | Schema for the `medsea_exam_history_v1` localStorage key — version field, record types, fields used by Analytics tab |
| `references/interactive-ui-feature-checklist.md` | Full "beast mode" feature checklist with HTML/JS snippets for each (keyboards, toasts, color states, etc.) |
| `references/authored-only-question-bank-rebuild.md` | Quality-first fallback for exam/flashcard banks: rebuild from authored `topic.md` sections only, parse answer keys, enforce structural gates, and deploy only after live sample verification |

## Templates

| File | Purpose |
|---|---|
| `templates/exam-index.html` | Complete skeleton for an exam tool page (Setup/Runner/Result/History/Analytics tabs, sticky bar, question palette). Copy and adapt per tool |
| `templates/exam-app.js` | JS logic skeleton (tab switching, setup form, exam engine integration, result rendering, history/analytics). Copy and adapt |
| `templates/flashcard-index.html` | Complete skeleton for a flashcard tool (3D flip animation, rate buttons, palette) |
| `templates/flashcard-app.js` | JS logic for flashcard engine integration, keyboard shortcuts, weak cards list |
| `templates/exam-engine.js` | Shared engine (DB loader, History, Exam runner, Flashcard runner, Pool, Format). Drop in once, reuse across all tools |

## Scripts

| File | Purpose |
|---|---|
| `scripts/extract_questions.py` | MD to JSON DB extractor (state-machine parser). Usage: `python3 extract_questions.py`. Output: `/site/assets/questions.json`. Skips modules' main code via import guard so it can be imported for testing |
| `scripts/parser_lib.py` | Pure-function parser library (importable). The `extract_questions.py` orchestrator imports this. Splitting prevents import side-effects when running tests |
| `scripts/deploy_to_medsea.sh` | One-command deployment via `docker cp` + `chmod -R a+r` + verify. Usage: `bash deploy_to_medsea.sh`. Rebuild-and-redeploy script also included |

## Integration with Other Skills

| Skill | When to Use Together |
|---|---|
| `medical-fcps-mrcp-exam-notes` | The source content (MedSea topic.md files) is produced by this skill. The `## MCQs` / `## SBA Questions` / `## Flashcards` sections it requires ARE what this skill consumes |
| `medsea-publishing-pipeline` | The deploy / Docker / site rebuild patterns are documented there. This skill's `docker cp` shortcut is the fast-iteration version; use the publishing-pipeline skill for production rebuilds |
| `medsea-multi-platform-sync` | When adding new chapters, sync them across Notion + GitHub first, THEN re-run `extract_questions.py` to include the new content in `questions.json` |
| `medsea-question-bank-audit` | Rebuild pipeline (`rebuild_question_bank_v5.py`), quality gates, deploy verification, mechanical audit script, rebuilder pitfalls (PasTest `text` shadowing, topic_slug, answer E UI) |
| `medsea-chapter-audit` → `references/medsea-product-sector-ratings.md` | Full MedSea product audit (/10 per sector, missing features backlog) when user asks for final rating or scan all apps |
| `static-spa-library-site` → `references/header-design-polish-2026-06.md` | Unify home/exam/flashcards header, mobile shell, search pills; browse before CSS; don't break runners |
| `static-site-mermaid-migration` | If migrating topic rendering to client-side mermaid, the topic.md files in this skill's source set may need re-extraction to preserve the MCQ sections (Mermaid blocks can contain regex-bait) |

## Forbidden Actions

| Action | Why |
|---|---|
| **Using regex with backtracking** for MCQ/SBA extraction | Takes 10+ minutes for 1,400 files and drops 60-90% of questions due to format variations. Use the state-machine parser pattern |
| **Forgetting `chmod -R a+r` after `docker cp`** | `GET /exam/` returns 403 even though file exists. Always chmod after copy |
| **Mapping `-p 8855:8855` on the medsea container** | nginx listens on port 80 INSIDE the container. Must be `-p 8855:80`. Returns HTTP 000 silently otherwise |
| **Reading `localStorage` without a versioned key** | Migration will break all existing user history. Use `medsea_exam_history_v1` (the v1 suffix is the schema version) |
| **Auto-submitting without warning the user** | Quietly ending a user's 20-question exam because they hit the timer without seeing the warning breaks trust. Use a 60-second visual warning (`timer.danger` class with pulse animation) before auto-submit fires |
| **Hiding the answer review after submit** | Users want to learn from mistakes. Always show a per-question review with their answer + correct answer + a color-coded border (green=correct, red=wrong) |
| **Claiming "100% complete" without verifying in browser** | Build success does not equal working UI. Always `browser_navigate` the deployed page and exercise the full flow (start exam, answer, submit, check result + history) |
| **Using `git add -A` after extraction without reviewing diffs** | `extract_questions.py` regenerates the entire `questions.json`. Verify the diff is just timestamp + counts, not accidental schema drift |
| **Mixing module-level code with parser functions** | Loading a script that has top-level orchestration code as a module runs that code on import. Split parser (pure) from orchestrator (with `if __name__ == '__main__':` guard OR a separate file) |
| **Hardcoding exam option letters A–D only** | MedSea bank includes A–E MCQs/SBAs; correct answer may be **E**. Hardcoded `['A','B','C','D'].forEach` hides E and makes those items unanswerable. Use `Object.keys(q.options).filter(...).sort()` in `exam/app.js`. |
| **Assuming monolithic `questions.json` only** | MedSea v5 serves `questions-index.json` + lazy chunks (`questions-mcq.json`, `questions-sba.json`, `questions-flashcard.json`) via `site-db.js`. Exam page loads index first, then chunks on Start. |
| **Loading full MCQ/flashcard monolith when user picked 1–3 chapters** | Wastes RAM/parse time. Use `questions-by-chapter/{n}-{kind}.json` when chapter selection ≤6; wire `SETUP.chapters` into `MedSea.DB._loadChunks(mode, chapterNums)`. Rebuild must emit shards (`rebuild_question_bank_v5.py` `write_chapter_shards`). |
| **Auditing bank with wrong schema assumptions** | Live JSON stores `options` as a **dict** `{"A": "text"}`, not a list. Flashcards use `front`/`back`, not `question`. An audit script that assumes arrays will report 100% false positives. Always check `isinstance(opts, dict)` and use `front`/`back` for flashcards. |
| **Leaving short abbreviation distractors ("PE", "MI", "DKA")** | Looks unprofessional in exam UI. Add `expand_abbrev_options()` in rebuilder — exact-match expansion only. See `medsea-question-bank-audit` skill. |
| **Deploying shards with directory perms 644** | `tar` deploy + `find -type f -exec chmod 644` accidentally sets 644 on the **directory** too. nginx can't traverse → serves `index.html` fallback (200 HTML instead of JSON). **Fix:** always `find -type d -exec chmod 755 {}` after file perm fix. |
| **Deploying JS/CSS but forgetting updated HTML** | Container serves old HTML without new `<script>` tags → `window.MedSea` false → exam/flashcards dead. Tar deploy must include ALL changed files: HTML, JS, CSS, JSON. Add `?v=N` cache-bust on JS includes. |

## Update Protocol

When this skill needs updating (new question format, new tool type, new UI feature):
1. Run the extractor on a sample chapter; confirm all format variations handled
2. Update `references/medsea-topic-md-formats.md` if a new format was found
3. Update `scripts/parser_lib.py` state machine to handle the new format
4. Add a new tool (OSCE, viva, etc.) by copying the flashcard template + adding a new runner in `exam-engine.js`
5. Update `references/interactive-ui-feature-checklist.md` with any new feature
6. Commit with descriptive message
