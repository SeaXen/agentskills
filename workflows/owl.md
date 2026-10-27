---
description: Activates the OWL (Optimized Workforce Learning) decoupled multi-agent pipeline (DeepInvestigator + DeepCoder).
---

# /owl - Decoupled Multi-Agent Engineering Pipeline

$ARGUMENTS

---

## Purpose

Activates Antigravity's decoupled multi-agent engineering architecture. Splits the task into two specialized decoupled pipelines: **DeepInvestigator** for root cause analysis and edge-case attacks, and **DeepCoder** for layer-0 code synthesis and compiler/test verification.

---

## Workflow Steps

1. **Step 1: Investigation (`DeepInvestigator`)**
   - Spawns `DeepInvestigator` subagent in `Workspace='inherit'`.
   - Maps full call chains, audits invariant constraints, tests boundary edge cases, and attacks hypotheses.

2. **Step 2: Implementation (`DeepCoder`)**
   - Passes verified invariants and edge cases into `DeepCoder`.
   - Enforces compiler gates, checks downstream consumers, and runs test suites.

3. **Step 3: Synthesis & Verification**
   - Verifies downstream callers across the entire call-tree.
   - Verifies zero collateral breakage before presenting results.
