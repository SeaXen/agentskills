Using the readme-optimization skill's opening-lines guidance (Step 5) to draft this, but flagging one thing before the deliverable: I don't have repo access (no local clone, can't run oaklight/prismstore or its test suite), and the skill has a hard rule against exactly two of the phrases you asked for.

**"Production ready" and "battle-tested" are on the skill's explicit fabrication blacklist** — they're claims a reader disproves with one glance at the commit history, and unlike a real status statement they cost more trust than they buy. "Blazing-fast" and "developer-friendly" are flagged too, as the canonical example of unfalsifiable adjectives to replace with something checkable. The fix the skill prescribes: swap the vibe-claim for the one concrete, checkable fact you actually gave me — four months of internal production use — rather than a certification nobody issued.

Here's the rewritten top, keeping the punch:

---

# Prismstore

Prismstore is an embedded key-value store for Zig, built on an LSM tree. No server, no ops layer — it's a library you compile straight into your binary, and we've been running it in production internally for four months.

---

That second sentence still carries confidence and momentum, it just spends it on something a skeptical reader can't immediately poke a hole in. If you want, I can push further and swap "four months internally" for a harder number (write throughput, a p99, a dataset size) once I actually have repo access to verify it against a benchmark — right now that number doesn't exist in this conversation, so I didn't invent one.