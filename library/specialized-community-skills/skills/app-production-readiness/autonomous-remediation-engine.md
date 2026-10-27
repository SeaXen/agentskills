# Autonomous Remediation Engine — Implementation Plan

> **STATUS: COMPLETE (10/10) ✅**
> All 5 phases implemented, tested, verified on real applications, and pushed to GitHub.
> Commit: `b3ef9f5` & `57216d9` on `main`.

---

## 1. Architecture & Design Principles

```
┌─────────────────────────────────────────────────────────────┐
│                       qa/report.md                          │
│               (Exact file:line BLOCKERS)                    │
└──────────────────────────────┬──────────────────────────────┘
                               │
                               ▼
┌─────────────────────────────────────────────────────────────┐
│                 scripts/remediate.py                        │
│            (Finding Parser & Handler Router)                │
└──────┬───────────────────────┬───────────────────────┬──────┘
       │                       │                       │
       ▼                       ▼                       ▼
┌──────────────┐       ┌──────────────┐       ┌────────────────┐
│ Deterministic│       │   Atomic     │       │  Agent Recipe  │
│   Codemods   │       │ Rollback &   │       │   Generator    │
│  (AST/Regex) │       │ Verification │       │ (Complex Logic)│
└──────────────┘       └──────────────┘       └────────────────┘
```

### Core Tenets:
1. **Never Break the Build (Atomic Rollback):** Every file modification is backed up to `qa/fix-backup/` prior to editing. If a modification introduces syntax errors, typecheck failures, or test crashes, it is immediately reverted.
2. **Hybrid Execution:**
   - **Deterministic Codemods:** Handle mechanical, unambiguous AST/HTML/CSS fixes (touch targets, missing focus-visible, unescaped innerHTML, empty catch blocks, missing aria-labels, security headers).
   - **Structured Recipe Output:** For complex creative design refactoring or high-risk domain logic, generate a structured prompt/recipe file (`qa/recipes/<issue-id>.md`) for direct execution by an AI coding agent.
3. **Continuous Re-Verification:** Once a fix is applied and syntax-checked, the target gate is re-measured using the skill's own verifiers to guarantee the finding is closed.

---

## 2. Measurable Success Criteria

1. **Deterministic Remediation Library:**
   - [x] `sec_xss_innerhtml`: Convert unvalidated `innerHTML` to `textContent` where applicable.
   - [x] `sec_cors_wildcard`: Restrict wildcard CORS on authed endpoints.
   - [x] `ui_touch_targets`: Inject minimum 44x44px CSS sizing for touch interaction targets.
   - [x] `ui_focus_visible`: Add accessible `:focus-visible` styling for interactive elements.
   - [x] `ui_reduced_motion`: Inject `prefers-reduced-motion` override rules.
   - [x] `code_empty_catch`: Inject structured error logging into empty `catch` blocks.
   - [x] `a11y_aria_labels`: Inject descriptive `aria-label` on unlabelled icon buttons.
   - [x] `seo_meta_tags`: Scaffold Open Graph and Twitter metadata tags in HTML `<head>`.
2. **Atomic Rollback Engine:**
   - [x] 100% of failed fixes revert cleanly with zero orphaned files or syntax regressions (`test_rollback_session` passes).
3. **Agent Recipe Generation:**
   - [x] Structured markdown recipes generated for logic-heavy findings (e.g. oversized functions, complex API contracts) complete with file excerpts and suggested refactoring steps.
4. **Self-Testing:**
   - [x] `scripts/test_remediation.py` with 8 unit and integration tests passing.
   - [x] 100% compliance with `skill_check.py` and `test_docs.py` (9/9 passed).

---

## 3. Work Breakdown Structure (Phases & Tasks)

### Phase 1: Core Framework & Finding Parser (`scripts/remediate.py`) — [DONE]
- [x] **Task 1.1: Report & Findings Ingestion**
  - Parse `qa/report.md` and `qa/summary.json` to extract structured issue objects.
- [x] **Task 1.2: CLI Interface & Flags**
  - Implemented `--root`, `--auto`, `--recipe-only`, `--dry-run`, and `--rollback`.

### Phase 2: Deterministic Codemod Engine (`scripts/remediation_handlers.py`) — [DONE]
- [x] **Task 2.1: Security Handlers**
  - `remediate_xss_innerhtml` and `remediate_cors_wildcard`.
- [x] **Task 2.2: UI / UX Handlers**
  - `remediate_touch_targets`, `remediate_focus_visible`, and `remediate_reduced_motion`.
- [x] **Task 2.3: Accessibility & Code Quality Handlers**
  - `remediate_empty_catch` and `remediate_aria_label`.

### Phase 3: Rollback Guard & Verification Runner — [DONE]
- [x] **Task 3.1: Pre-Commit Snapshot & Syntax Validation**
  - Created atomic backup in `qa/fix-backup/<session_id>/`.
  - Added syntax validation guard before overwriting targets.
- [x] **Task 3.2: Rollback CLI**
  - Supported instant rollback via `python scripts/remediate.py --rollback`.

### Phase 4: Agent Recipe Generator — [DONE]
- [x] **Task 4.1: Markdown Recipe Formatter**
  - Generates context-rich recipes in `qa/recipes/<gate>_<target>_<rule>.md` with code snippets, line numbers, and agent instructions.

### Phase 5: Verification, Documentation & Integration — [DONE]
- [x] **Task 5.1: Unit & Integration Tests (`scripts/test_remediation.py`)**
  - All 8 unit tests passing in 0.30s.
- [x] **Task 5.2: Documentation & Skill Packaging**
  - Documented in `SKILL.md` and `README.md`.
  - Tested with `skill_check.py` (`[OK] skill package is healthy`) and `test_docs.py` (9/9 passed).
- [x] **Task 5.3: Live Benchmark Test on `Lumen`**
  - Successfully fixed CSS touch targets, focus visible, reduced motion, and generated 4 refactoring recipes.

---

## 4. Checkpoint Verification Plan — All Complete ✅

- [x] All 8 deterministic codemods pass unit tests.
- [x] Rollback on syntax failure verified by test.
- [x] `skill_check.py` returns `[OK] skill package is healthy`.
- [x] `test_docs.py` passes 100%.
- [x] Live execution against `Lumen` resolves real blockers without regressions.
