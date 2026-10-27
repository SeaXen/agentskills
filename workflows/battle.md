---
description: Activates Antigravity's Colosseum Battle Mode (forks rival subagents in isolated branches, pits them against each other, and merges the winner).
---

# /battle - Colosseum Battle Mode

$ARGUMENTS

---

## Purpose

Activates an adversarial arena between two competing implementations instead of relying on a single agent's code choices.

---

## Workflow Steps

1. **Step 1: Forking Competing Arms**
   - Fork two rival subagents concurrently in isolated git worktrees (`Workspace='branch'`):
     - **Competitor Arm Alpha:** Safe, clean, and robust abstraction.
     - **Competitor Arm Beta:** Minimal complexity, directness, and high throughput.

2. **Step 2: Colosseum Referee Audit**
   - Pits both implementations against an adversarial critic (`Role: critic@colosseum`).
   - Runs stress tests, boundary attacks, and benchmarks against both branches.

3. **Step 3: Crown Victor & Merge**
   - Merges the winning branch back into the working tree.
