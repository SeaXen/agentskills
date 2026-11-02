## Big picture

You can't patch ChatGPT's training data — that channel is gone, permanently, for this specific mistake. 🎯 What you *can* do: make the wrong call fail with the fix baked into the error message, and make the correct answer the easiest thing on the internet to find for the literal string `new_with_config`. Do both. The first matters more — it works no matter where the bad code came from, and it needs zero infra beyond `cargo publish`.

## 1. Turn the dead API into a self-explaining compile error (do this first)

Right now a hallucinated call to `new_with_config` produces `error[E0599]: no function or associated item named 'new_with_config' found` — a real error, but one with zero guidance, which is exactly why three people gave up and filed issues instead of fixing it themselves.

Re-add the symbol as a tombstone. Two shapes, pick per-case:

**If the new API can satisfy the old call shape** — delegate for real, deprecate loudly:

```rust
#[deprecated(
    since = "0.9.0",
    note = "removed in 0.9; use `Engine::builder()...build()`. See https://<your-book>/migrating-0.9.html"
)]
pub fn new_with_config(config: LegacyConfig) -> Self {
    Engine::builder().apply_legacy(config).build()
}
```

This compiles with a **warning**, not silence — the migration note and URL print directly in `cargo build` output, in the user's own terminal, which they can paste straight back into ChatGPT to self-correct.

**If there's no safe equivalent** (the whole config concept is gone, not just renamed) — keep the deprecation attribute, panic with the fix on the rare path someone actually calls it:

```rust
#[deprecated(since = "0.9.0", note = "removed in 0.9; see https://<your-book>/migrating-0.9.html")]
pub fn new_with_config(_config: LegacyConfig) -> Self {
    panic!("Engine::new_with_config was removed in 0.9 — see https://<your-book>/migrating-0.9.html")
}
```

Either way: this is a purely additive, semver-safe change — ship it as a patch release. **`cargo publish`** once, and every future AI-hallucinated call self-corrects at the exact moment it happens, forever, with no further action from you.

## 2. Make the removal permanently greppable

Add one unambiguous entry that names the exact symbol verbatim (exact-match strings are what both humans searching and AI retrieval latch onto):

```markdown
## [0.9.0] - <date>
### Removed
- `Engine::new_with_config(Config)` — replaced by `Engine::builder()`.
  If an AI assistant suggested `new_with_config`, that's why it doesn't
  exist: it was removed here. Migration: https://<your-book>/migrating-0.9.html
```

Put the same callout, verbatim, at the top of `MIGRATING.md`/the mdbook's migration chapter. This is a plain markdown file in a repo you already own — no CDN, no headers needed.

## 3. Give the exact query a single canonical answer

Open one pinned GitHub issue or Discussion titled literally **"`Engine::new_with_config` was removed in 0.9 (AI assistants keep suggesting it)"**. Put the fix, the why, and the migration link in the first comment. Close the three open issues with a one-line reply pointing at it — GitHub issues are crawled and indexed, so this becomes the thing both search engines and browsing-capable AI tools (ChatGPT with search on, Perplexity, Claude with Brave search) surface for that query, distinct from your training-data problem.

## 4. Feed the tools that browse instead of recall

`docs.rs` and your mdbook/GitHub Pages are static files you already control — this needs nothing new:
- Drop an `llms.txt` at the book's root (see llmstxt.org) with a short "Removed / renamed APIs" section listing `new_with_config → Engine::builder()`.
- Add one prose sentence on the `Engine` doc comment itself (renders on docs.rs) noting the removal — docs.rs already banners old-version pages as outdated, so you don't need to touch that.

This only helps AI systems that fetch live pages, not ones answering from frozen training weights — worth doing because it's a five-minute static-file edit, not because it fixes the root cause.

## What not to spend time on

- Response headers, CDN rules, `Deprecation`/`Sunset` HTTP headers — none of this reaches ChatGPT's answer generation; skip it, you don't have the infra and it wouldn't help this specific problem anyway.
- Chasing each future hallucinated-API issue individually — once the tombstone ships, that's handled automatically; just point new issues at the pinned thread.
- Waiting for OpenAI to fix it — there's no retraining timeline you can influence. Individual affected users can thumbs-down the ChatGPT answer themselves; that's on them, not a maintainer task.