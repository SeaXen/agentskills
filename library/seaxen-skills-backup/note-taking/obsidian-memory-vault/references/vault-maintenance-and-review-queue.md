# Vault maintenance pass (no folder sprawl)

When the user asks to improve, update, or "do best" for the Obsidian vault — **maintain and refresh**, do not add top-level folders or bulk notes.

## High-value edits (in order)

1. **`System/Assistant/context.md`** — current ports, services, open items, date in header.
2. **`GET /api/memory-candidates`** — process review queue (see below).
3. **`Work/<Project>.md`** — one lean note per *active* project; link from `Work/Work Index.md`.
4. **`Memory/decisions.md`** — append structured entries for durable decisions (do not rely on auto-promote from queue).
5. **`AGENT.md` Daily Note Index** — any new `Daily/YYYY-MM-DD.md` gets `[[YYYY-MM-DD]]` same turn.

Skip: duplicating skill content into vault; new architecture notes every week; raw chat imports.

## Memory review queue — false positives

The dashboard scanner (`/api/memory-candidates`) flags lines containing keywords like "decision", "fix", "preference" in **any** markdown — including:

- Tag lists (`#decision #project`)
- Table rows in bridge/architecture docs
- `[[decisions]]:` bullets in daily notes (already routed)
- "Read preferences.md" session-protocol lines

**Workflow:**

1. Manually write durable content to `decisions.md` / `issues-fixes-log.md` when appropriate.
2. `POST /api/memory-review` with `status: "rejected"` for each pending candidate that is noise (include `candidate_id` + full candidate object fields from GET).
3. Re-check `GET /api/memory-health` — `review_queue.pending` must be **0** for `review_flow` score 100.

**Symptom:** After a vault edit session, **new** pending items appear (often 3–9). Health drops ~98.8 until cleared. This is expected — not a regression in recall.

## Live verify (ad-hoc)

After maintenance:

```bash
curl -sS 'http://127.0.0.1:6065/api/memory-health'
curl -sS 'http://127.0.0.1:6065/api/recall-eval'
curl -sS 'http://127.0.0.1:6065/api/recall?query=MedSea&limit=1'
```

Or run `scripts/flush_memory_review_noise.py` then confirm pending=0.

## Dr. Sagar preference

Lean vault: user dislikes extra skills/folders without reuse value. Prefer patching `obsidian-memory-vault` + `obsidian-vault-learn-bridge` over new per-session skills.