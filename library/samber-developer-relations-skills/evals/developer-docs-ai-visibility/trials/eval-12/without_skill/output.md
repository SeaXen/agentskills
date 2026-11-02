# Verdict: don't do any of the three

I haven't checked your repos, the npm page, or the blog post. This is based only on what you described.

## Why the plan fails

Deleting sources doesn't remove them from what the models know. Models cite from training data and from retrieval, and you can't edit either one. Retrieval will fall back to the next-best match, which may be a worse third-party copy. The root cause is that no fresh, authoritative page answers "oakspire session setup" for 3.x. Fix that first.

| Action | Problem | Do instead |
|---|---|---|
| Takedown to the blog | You have no legal basis. A 2021 tutorial that was correct for 2.x isn't infringing or defamatory. Independent bloggers often publicize takedown attempts, and a maintainer-turned-devrel asking for removal reads badly. | Email the author and ask for an "outdated since 3.0" banner linking to the current docs. Offer to send the updated snippet or a PR. Most will say yes. |
| Delete `oakspire-starter-express` | Stars, inbound links, and forks become 404s. Anyone following an old tutorial hits a dead end with no pointer to the fix. The repo is already archived, which is a clear signal. | Temporarily unarchive it. Either update it to 3.x (best) or put a deprecation banner at the top of the README. Then re-archive it. |
| Unpublish `oakspire-legacy` | npm only allows a full unpublish in narrow cases, such as no dependents and very low downloads. Otherwise it needs npm support. Unpublishing breaks installs and lockfiles for anyone depending on it. | Publish one final patch version whose README leads with the migration pointer. Run `npm deprecate` with a message. |

## Do this instead

1. **Write the canonical page.** Create one docs page titled "Session setup (3.x)" that covers:
   - what replaced `store: 'memory'`
   - a minimal working Express example
   - a short "coming from 2.x" section mapping the old call to the new one

   Put the old call string, `Oakspire.session({ store: 'memory' })`, on that page. Retrieval will then match the stale query to the correct answer.
2. **Add a migration entry** for the removed `store: 'memory'` option, with before/after code.
3. **Make the docs easy for models to read.** Publish `llms.txt` and make sure the page is crawlable, server-rendered, and linked from the docs nav and README.
4. **Update the three stale sources:**
   - **Blog:** a polite email asking for a banner. Draft below.
   - **Starter repo:** a README banner. Better, port it to 3.x so it becomes the canonical starter.
   - **`oakspire-legacy`:** a final version with a new README, plus the deprecate command below.
5. **Re-check in 4–8 weeks.** Ask the same "oakspire session setup" question in Claude and ChatGPT and see what they cite. Training-data lag is real, but retrieval-backed answers should shift sooner.

## Drafts

**Email to the blog author**

> Hi [name], I'm [you] from the Oakspire team. Your 2021 session tutorial is still the top result for "oakspire session setup" and it's been very helpful to many people. Since 3.0, `store: 'memory'` was removed, so new readers hit errors. Would you consider adding a note at the top linking to [canonical docs URL]? Happy to send an updated snippet or a PR if that's easier. Thank you for writing it.

**Banner for the starter repo and legacy README**

> ⚠️ This project targets Oakspire 2.x, which is no longer supported. `store: 'memory'` was removed in 3.0. For current session setup, see [canonical docs URL].

**npm deprecation** (this **writes to the registry**, so run it from a release-enabled account)

```
npm deprecate oakspire-legacy "Unsupported 2.x line. Use oakspire@3 — session setup: <canonical docs URL>"
```

Do this after publishing the final patch version so the new README is what npm displays.

## Questions

- What replaced `store: 'memory'` in 3.x? I need it to draft the canonical page and migration entry.
- Do you want me to draft the full "Session setup (3.x)" page next?