## quillsync label set — redesign

**Shape:** 4 small, mostly-exclusive facets instead of a flat pile of 47. Every facet answers one triage question a maintainer asks in the first 10 seconds of looking at an issue: *what kind, what state, can someone else pick it up, does it jump the queue.* Nothing beyond that, because your real constraint isn't taxonomy quality — it's that 35 issues land against ~4 person-hours/week of total maintainer time. Any label that doesn't directly speed up a triage or search decision is pure overhead you can't afford.

### Type — exactly one per issue

| Label | Color | Meaning |
|---|---|---|
| `type: bug` | `#d73a4a` | Confirmed or suspected defect in existing behavior. |
| `type: feature` | `#a2eeef` | New capability or enhancement request. |
| `type: question` | `#d876e3` | Usage question / support request — not a defect or feature ask. |
| `type: docs` | `#0075ca` | Docs missing, wrong, or unclear. |
| `type: chore` | `#cfd3d7` | Maintenance: CI, deps, refactor, release — usually maintainer-filed. |

### Status — zero or one; **no status label = untriaged**, so you don't need a separate "needs-triage" label

| Label | Color | Meaning |
|---|---|---|
| `status: needs-info` | `#fbca04` | Waiting on reporter for repro/logs/answer. Stale-bot target (see below). |
| `status: confirmed` | `#0e8a16` | Reproduced/accepted, ready to work. |
| `status: blocked` | `#e99695` | Stuck on an external dep, upstream fix, or a decision. |
| `status: wontfix` | `#eeeeee` | Closed, won't implement — reasoning stays in the thread. |
| `status: duplicate` | `#cccccc` | Closed, tracked elsewhere — link the canonical issue. |

### Community offload — your actual capacity lever

| Label | Color | Meaning |
|---|---|---|
| `help wanted` | `#008672` | Scoped enough to hand to a contributor. |
| `good first issue` | `#7057ff` | Small, well-scoped, onboarding-friendly. |

### Priority — one tier only

| Label | Color | Meaning |
|---|---|---|
| `priority: critical` | `#b60205` | Data loss, crash, sync corruption. Jumps the queue. Everything else sits in normal FIFO order — a 3-tier P0–P2 scheme isn't worth maintaining at 2h/week each. |

### Area — populate with your real top integrations, cap it

| Label | Color | Meaning |
|---|---|---|
| `area: <app-1>` | `#c5def5` | Fill with your highest-volume integration. |
| `area: <app-2>` | `#c5def5` | … |
| `area: <app-3>` | `#c5def5` | … |
| `area: <app-4>` | `#c5def5` | … |
| `area: <app-5>` | `#c5def5` | … |
| `area: other-integration` | `#c5def5` | Catch-all — don't create a label for a single-issue integration ask. |

I'm not guessing your integration names (Obsidian/Notion/Evernote/whatever) — pull your top 5 by actual issue volume with a quick label or title search, name those, and route the long tail into the catch-all. If a 6th integration consistently generates volume, promote it later; that's a one-click add, not a redesign.

**Total: 13 fixed labels + up to 6 area labels ≈ 19**, down from 47.

---

## Tonight's rollout order

1. **Rename in place wherever there's a clean 1:1 target** (e.g. old `enhancement` → `type: feature`). GitHub preserves every issue association on rename — zero per-issue work.
2. **Bug consolidation needs one extra step** because `type: bug` already exists, so you can't rename `bug` onto it directly:
   - Search `is:issue is:open label:bug`, select all, bulk-add `type: bug` (GitHub's issue-list bulk actions, or `gh issue list --label bug --json number -q '.[].number' | xargs -I{} gh issue edit {} --add-label "type: bug"`).
   - Repeat for `Bug`.
   - Once every formerly-`bug`/`Bug` issue carries `type: bug`, **delete** `bug` and `Bug` — deleting a label only strips it, the issue and its history stay intact.
3. **Delete the 19 singleton labels outright.** One issue each isn't worth preserving as a filterable category; the context lives in the issue body regardless, and recreating a label later costs one click if the need actually recurs.
4. **Area labels last** — this is the part safe to push past tonight if you run out of time; it doesn't block basic type/status triage.
5. **Add a stale-bot** (e.g. `actions/stale`) scoped to `status: needs-info` with no activity for ~21 days → auto-close with a polite comment. This is the piece that actually protects you from the math (35 in/week vs. 4 hours/week available) — the label alone just marks the issue, it doesn't reclaim your time.