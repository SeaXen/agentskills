# Antigravity Subagent Orchestration

## 1. Native Subagent Concept

In Antigravity, subagents are independent execution threads spawned with isolated context windows, specialized system prompts, and task-specific toolsets.

### Key Benefits:
- **Zero Context Pollution**: Complex sub-tasks (e.g., analyzing 50 legacy files, running penetration scans) run in subagents without bloating the primary agent's token history.
- **Role Specialization**: Subagents run with persona configurations matching the domain agent files in `.agent/agents/`.

---

## 2. Invocation Patterns

### Parallel Task Spawning
When several independent investigations are needed:
1. Orchestrator defines clear, bounded prompts for each subagent.
2. Each subagent runs independently and produces a concise summary report.
3. The parent orchestrator synthesizes the results without needing the full raw log in primary context.

### Reactive Wakeup
Antigravity automatically notifies the primary agent when a background subagent finishes execution. There is no need for active polling or tight loop sleeps.

---

## 3. Orchestration Guardrails

- **One Task, One Goal**: Never pass ambiguous or multi-phase instructions to a single subagent.
- **Structured Output**: Require subagents to return structured markdown (tables, checklists, file diff paths).
- **Early Stop**: Define explicit return criteria and max duration to prevent runaway executions.
