---
description: Triggers on-demand context compaction (persists active state into durable artifacts and flushes transient token history).
---

# /compaction - On-Demand Context Compaction

$ARGUMENTS

---

## Purpose

Explicitly compacts the active conversation context, preventing context exhaustion during long-running sessions.

---

## Workflow Steps

1. **State Preservation:**
   - Identifies active file paths, key symbols under investigation, and ongoing test statuses.
   - Writes or updates this state into a persistent summary artifact in `<artifactDir>/session_state.md`.

2. **Context Compaction:**
   - Summarizes completed work and flushes obsolete step details.
   - Outputs a compact checkpoint with: Accomplished So Far, Current State, and Immediate Next Actions.
