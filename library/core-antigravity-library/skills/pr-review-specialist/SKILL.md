---
name: pr-review-specialist
description: High-impact Pull Request (PR) reviews, automated diff analysis, severity calibration, and security flagging. Use when reviewing PRs, analyzing diffs, providing structured code review feedback, or checking for introduced regressions.
allowed-tools: Read, Write, Edit, Glob, Grep
version: 1.0
category: security-audit
---

# Pull Request Review Specialist

> **Rigorous Code Review, Severity Calibration & Constructive Engineering Feedback**

---

## 🏗️ Core Principles

| Principle | Rule |
|-----------|------|
| **Severity Calibration** | Always prefix comments with severity: `[BLOCKER]`, `[SECURITY]`, `[PERF]`, `[NIT]`, or `[QUESTION]`. |
| **Explain the "Why"** | Never say "change this to X". Explain the consequence: "If `data` is empty, this throws a TypeError on line 42 because...". Suggest concrete alternatives. |
| **Praise Good Engineering** | Highlight clean abstractions, well-written tests, and clever optimizations (`[KUDOS]`). |
| **Review Diffs Holistically** | Check what was REMOVED as carefully as what was ADDED. Watch out for bypassed tests, removed validations, or suppressed lint rules. |

---

## 📋 PR Review Checklist

### 1. Correctness & Logic
- [ ] Does the code satisfy the acceptance criteria of the task?
- [ ] Are edge cases (null, undefined, empty array, network timeout) handled?
- [ ] Are state transitions clean without race conditions?

### 2. Security & Data Integrity
- [ ] Is user input sanitized and validated before use?
- [ ] Are permissions / authentication verified on new endpoints?
- [ ] Are secrets or PII accidentally logged or committed?

### 3. Performance & Resource Management
- [ ] Are database queries optimized (no N+1 loops, necessary indexes in place)?
- [ ] Are memory listeners, intervals, and subscriptions cleaned up?
- [ ] Are heavy computations memoized or offloaded?

---

## 📋 Standard Review Output Format

```markdown
## 📋 Pull Request Review Summary

### 🚦 Verdict: CHANGES REQUESTED / APPROVED WITH NITS

### 🔴 Critical Blockers
- **[BLOCKER]** [Line 45](file:///path/to/file.ts#L45): Potential unhandled promise rejection in error handler causes server crash on timeout.

### 🟡 Suggestions & Improvements
- **[PERF]** [Line 112](file:///path/to/file.ts#L112): `Array.find()` inside `.map()` creates an $O(N^2)$ loop. Consider converting to a `Map` lookup.

### 🟢 Commendations
- **[KUDOS]** Comprehensive property-based test coverage for edge case numbers.
```

---

## ❌ Anti-Patterns

- ❌ Vague feedback like "looks weird" or "refactor this".
- ❌ Bikeshedding over formatting when automated linters/formatters should handle it.
- ❌ Approving pull requests with commented-out code or `@ts-ignore` bypasses.
