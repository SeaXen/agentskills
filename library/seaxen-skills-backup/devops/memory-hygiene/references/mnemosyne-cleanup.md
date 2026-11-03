# Mnemosyne cleanup workflow

Use when Hermes has Mnemosyne active and you need to remove low-signal test residue without disturbing durable memory.

## When to clean

Typical junk:
- smoke-test tokens
- dummy identifiers
- one-off validation prompts
- echoed assistant replies from memory-provider testing

Do not clean just because a memory is inconvenient. Clean only clear verification residue or stale low-signal noise.

## Fast audit

1. Query the suspected tokens/phrases with Mnemosyne recall.
2. Inspect exact hits with the Mnemosyne CLI.
3. Check whether the junk is in Mnemosyne, built-in memory, or both.

Important:
- built-in `MEMORY.md` noise does not imply Mnemosyne contains the same text
- Mnemosyne may store several rows for one smoke test

## Deletion pattern

If tool-level forgetting is available and works, use it.

If forget returns `not_found` or does not clear retrieval, use a DB-backed cleanup:

1. Back up the database first.
2. Inspect rows matching the token in:
   - `working_memory`
   - `episodic_memory`
   - `memories`
3. Delete all rows whose `content` contains the exact smoke-test token.
4. Commit.
5. Verify with both:
   - `hermes mnemosyne inspect '<token>'`
   - recall search for the same token(s)

## Concrete lesson from this case

Smoke-test residue was stored in `working_memory` as multiple rows per token, including:
- fact-style entries
- `[USER] ...` prompt echoes
- `[ASSISTANT] ...` reply echoes

Deleting only the fact row would have left residual recall noise. Full-token deletion across the memory tables cleaned it properly.

## Safety rules

- Always create a DB backup before direct edits.
- Prefer exact token matching for cleanup of validation residue.
- Re-run inspect/recall after deletion; do not assume success.
- Leave session transcripts alone unless the user explicitly wants history cleaned too.
