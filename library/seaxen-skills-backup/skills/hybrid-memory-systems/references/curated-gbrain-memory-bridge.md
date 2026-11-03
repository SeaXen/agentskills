# Curated Hermes-memory → GBrain bridge

## When to use
- The user wants Hermes/Mnemosyne to remain the canonical hot-memory layer, but also wants a small subset of durable facts visible inside GBrain.
- The user explicitly does **not** want raw transcript dumping or broad auto-mirroring into GBrain.
- You need a repeatable operator-facing sync path that survives sessions.

## Pattern
Use a **curated file-sync bridge**, not a live write-through of every memory event.

### Ownership
- **Mnemosyne** remains canonical for compact durable operator memory.
- **GBrain** receives only curated long-form pages that add structure and retrieval value.
- **MnemoSync** is orthogonal; do not touch it unless the user explicitly asks.

### Recommended shape
1. Create local markdown source files for the mirrored pages under a stable folder, e.g.:
   - `.../GBrain/mirrors/people--<name>.md`
   - `.../GBrain/mirrors/projects--<topic>.md`
2. Keep the mirrored set small:
   - operator profile / person page
   - memory-stack contract page
   - bridge-status page documenting local sources + sync command
3. Add a small rerunnable script under `~/.hermes/scripts/` that pushes those pages through the **verified shared-brain CLI path**.
4. Verify by reading the pages back from the live shared brain after sync.
5. If ongoing maintenance is wanted, schedule a **silent** cron sync (`no_agent=True`) that emits nothing on success.

## Why this pattern
This avoids the two bad extremes:
- losing stable operator context inside GBrain entirely
- polluting GBrain with raw session chatter, temporary state, and duplicated memory noise

## Verification
- Run the sync script once manually.
- Read back each mirrored slug from the shared brain.
- Confirm the pages describe the current ownership split correctly.
- Confirm the cron script path is **relative to `~/.hermes/scripts/`** if scheduled with `cronjob(..., script=..., no_agent=True)`.

## Notes
- Prefer the known-good repo CLI / wrapper path for the shared brain when the global binary and repo CLI disagree.
- The durable lesson is the **curated bridge pattern**, not any one transient install/path issue from a particular session.
