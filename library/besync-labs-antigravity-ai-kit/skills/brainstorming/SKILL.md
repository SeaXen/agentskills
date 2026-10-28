---
name: brainstorming
description: Socratic questioning and discovery protocol. Ensures requirements clarity before implementation.
version: 1.0.0
allowed-tools: Read, Glob, Grep
category: frontend-ui-components
---

# Brainstorming & Communication Protocol

> Understand before building. Ask before assuming.

---

## 🛑 SOCRATIC GATE (MANDATORY)

### When to Trigger

| Pattern                                     | Action                             |
| ------------------------------------------- | ---------------------------------- |
| "Build/Create/Make [thing]" without details | 🛑 ASK 3 questions                 |
| Complex feature or architecture             | 🛑 Clarify before implementing     |
| Update/change request                       | 🛑 Confirm scope                   |
| Vague requirements                          | 🛑 Ask purpose, users, constraints |

### 3 Questions Before Implementation

1. **STOP** — Do NOT start coding
2. **ASK** — Minimum 3 questions:
   - 🎯 **Purpose**: What problem are you solving?
   - 👥 **Users**: Who will use this?
   - 📦 **Scope**: Must-have vs nice-to-have?
3. **WAIT** — Get response before proceeding

---

## 🧠 Dynamic Question Generation

> **⛔ NEVER use static templates.** Generate questions based on context.

### Core Principles

| Principle           | Application                  |
| ------------------- | ---------------------------- |
| **Context-aware**   | Questions match the domain   |
| **Prioritized**     | Ask most important first     |
| **Open-ended**      | Encourage detailed responses |
| **Assumption-free** | Don't lead the answer        |

### Question Generation Process

```
1. Identify domain (frontend, backend, mobile, etc.)
2. Detect ambiguities in request
3. Generate 3-5 clarifying questions
4. Order by impact on implementation
5. Present clearly with formatting
```

### Question Format

```markdown
Before I proceed, I have a few questions:

1. **[Topic]**: [Specific question]?
2. **[Topic]**: [Specific question]?
3. **[Topic]**: [Specific question]?

Feel free to answer all at once, and I'll start implementing.
```

---

## 📊 Progress Reporting

### Status Icons

| Icon | Meaning                  |
| ---- | ------------------------ |
| ✅   | Complete                 |
| 🔄   | In progress              |
| ⏳   | Pending                  |
| ❌   | Failed/Blocked           |
| ⚠️   | Warning/Attention needed |

### Status Board Format

```markdown
## Status Update

| Task            | Status | Notes    |
| --------------- | ------ | -------- |
| Database schema | ✅     | Migrated |
| API endpoints   | 🔄     | 3/5 done |
| Frontend pages  | ⏳     | Next up  |
```

---

## ⚠️ Error Handling

### Error Response Pattern

```markdown
🔍 **Symptom**: [What happened]
🎯 **Root cause**: [Why it happened]
✅ **Fix**: [The solution]
🛡️ **Prevention**: [How to avoid in future]
```

---

## ✅ Completion Message

### Structure

```markdown
## ✅ Complete: [Task Name]

### What was done

- [Deliverable 1]
- [Deliverable 2]

### How to verify

[Specific steps to test]

### Next steps (suggested)

1. [Optional follow-up]
2. [Optional follow-up]
```

---

## Communication Principles

| Principle        | Implementation                     |
| ---------------- | ---------------------------------- |
| **Concise**      | No unnecessary details             |
| **Visual**       | Use emojis for quick scanning      |
| **Specific**     | "~2 minutes" not "wait a bit"      |
| **Alternatives** | Offer paths when stuck             |
| **Proactive**    | Suggest next step after completion |

---

## Anti-Patterns (AVOID)

| ❌ Don't            | ✅ Do            |
| ------------------- | ---------------- |
| Jump to solutions   | Understand first |
| Assume requirements | Ask questions    |
| Over-engineer v1    | MVP first        |
| Ignore constraints  | Factor them in   |
| "I think" phrases   | Ask for clarity  |
