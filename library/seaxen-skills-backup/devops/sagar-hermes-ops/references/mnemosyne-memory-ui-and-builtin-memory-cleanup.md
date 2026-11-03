# Mnemosyne memory UI integration + built-in memory cleanup

## When this matters
Use when Dr. Sagar asks to:
- clean Hermes built-in memory while Mnemosyne is active
- verify whether built-in `MEMORY.md` still matters alongside an external memory provider
- add Mnemosyne visibility to a Hermes dashboard plugin

## Durable findings

### 1) Built-in memory still affects future sessions when Mnemosyne is active
Hermes keeps built-in memory active alongside the external provider.
Practical result:
- noisy `MEMORY.md` still pollutes future prompt context
- `USER.md` should usually be preserved unless the user explicitly wants profile cleanup
- for low-noise cleanup, prefer rewriting `MEMORY.md` to a short list of durable environment/agent facts rather than line-by-line trimming junk fragments

### 2) Safe cleanup shape for Dr. Sagar
Default pattern:
1. Back up `MEMORY.md` first.
2. Do **not** touch `USER.md` unless explicitly asked.
3. Replace `MEMORY.md` with only durable operational facts.
4. Verify both file contents and the live dashboard memory page after the edit.

Good reduced `MEMORY.md` shape:
- active external memory provider state
- one or two durable routing or operator facts
- no TODOs, no session fragments, no one-off debugging residue

### 3) Mnemosyne dashboard support can be added cleanly via read-only SQLite inspection
For `hermes-memory-ui`, useful minimal support was:
- add `mnemosyne` status block to plugin status/snapshot payloads
- add a dedicated `/mnemosyne` API route
- read the SQLite DB in read-only mode
- show:
  - working memory total
  - episodic total
  - extracted fact total
  - triples total
  - recent / matching working memories
  - recent / matching extracted facts

### 4) Verify the live dashboard, not just the patched files
A disk patch is not enough.
Verification sequence that worked:
1. syntax-check backend/frontend files
2. import backend module and call the new payload/route directly
3. rescan dashboard plugins if the live route still serves the old shape
4. if needed, restart dashboard processes
5. verify live HTTP API with dashboard session token
6. verify browser-rendered page shows the new Mnemosyne section

## Path / runtime nuance
On this system, `/root/.hermes` and `/mnt/tb/hermes` can be the same live Hermes home.
Always verify `samefile()` / resolved paths before assuming the dashboard is looking at a different config or memory tree.

## Good acceptance criteria
- `USER.md` unchanged
- `MEMORY.md` reduced to durable facts only
- live `/memory` dashboard shows cleaned built-in memory
- live dashboard exposes Mnemosyne provider block and Mnemosyne section
- browser snapshot confirms Mnemosyne cards/labels render, not just API JSON
