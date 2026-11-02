## Verdict: Ship the concept, not these two files as-is

Linking machine-readable docs from the footer is a good, low-risk move. But neither file is in shippable shape yet, and treating "generate + link" as done misses why these files exist.

### Problem 1: your llms.txt isn't an llms.txt

The llmstxt.org spec defines this as a **curated navigation index** — H1, one-line summary, then H2 sections with bullet links and short descriptions pointing to your real pages. Reference implementations (Anthropic, Stripe) run 2–20K characters. At 180,000 characters, yours isn't an index — it's a content dump wearing the index's file name. That's ~10x larger than anything the spec anticipates, and it defeats the file's purpose: an agent opening `llms.txt` wants a map, not the territory.

**Root cause is almost always the same:** whoever generated it inlined full page content or descriptions instead of linking out. Fix means re-curating, not re-running the generator — a content task, not a shipping task. Don't commit to "this week" for llms.txt specifically.

### Problem 2: llms-full.txt at 6.2MB is expected size, questionable utility

For 1,400 pages, 6.2MB isn't a generation bug — it's just what that much documentation weighs concatenated flat. The problem is consumption, not creation:

- No agent fetches 6.2MB before answering a query — cost and latency make that impractical even for large-context models.
- It's a flat concatenation with no chunking or per-product-line boundary, so an agent interested in Edge alone still has to pull (or ignore) Fleet, Historian, and Studio content.
- **No major AI engine has confirmed it prioritizes or even regularly fetches `llms-full.txt`.** This is a community convention, not an accepted crawler standard (same caveat as OKF) — treat it as a no-regret hygiene move, not a traffic lever.

### Recommended structure instead of one flat pair

- `/llms.txt` — root index, curated, ideally under ~10K characters. Links to four child indexes, one per product line.
- `/edge/llms.txt`, `/fleet/llms.txt`, `/historian/llms.txt`, `/studio/llms.txt` — per-line curated indexes, each linking to that line's key pages.
- `/llms-full.txt` — keep as a full-dump fallback if you want, but split it too (`/edge/llms-full.txt`, etc.) so it's actually retrievable in useful chunks.
- Serve clean markdown at predictable URLs (e.g., `page.html` → `page.md`) so every link in the index resolves to something an LLM can parse without HTML noise.

### Industrial IoT-specific risk — don't skip this

Vantage Grid docs likely include version-specific configuration, safety thresholds, and calibration steps across Edge/Fleet/Historian/Studio. A stale or flattened llms-full.txt that gets cited by an agent recommending a deprecated config isn't just a bad citation — it's a liability surface specific to industrial control systems. Before shipping:

- Stamp every generated file with a **version and last-updated date** at the top.
- If any product line has been through breaking changes, either exclude those sections from `llms-full.txt` or make the version boundary explicit inline.
- Regenerate on every docs release, not ad hoc — a wrong "current" flag is worse than no file.

### Before linking anything, verify AI crawlers can even reach it

Check `robots.txt` doesn't block `GPTBot`, `ClaudeBot`, `PerplexityBot`, or `Google-Extended` on these paths. Blocking them silently makes the whole exercise a no-op — nobody catches this until someone asks why citations never showed up.

### What to actually do this week

1. **Ship `llms-full.txt`** split per product line, with version/date headers. Mechanical, low-risk, do it now.
2. **Hold `llms.txt`** — rebuild it as a real curated index (root + 4 child indexes) rather than linking the 180K-character version. Budget this as a separate, slightly bigger task.
3. **Link the footer** once both are in their final shape, not before — a footer link to an oversized llms.txt just ships the same problem with a permalink.
4. **Set expectations with the team**: this is hygiene, not a guaranteed AI-citation win. Check back in a month with a manual spot-check (ask ChatGPT/Perplexity/Claude a handful of Vantage Grid setup questions) to see if anything changed before investing further here.