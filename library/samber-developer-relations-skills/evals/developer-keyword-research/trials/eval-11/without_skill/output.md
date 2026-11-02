## Recommendation: kill the matrix, ship a 25-page pilot built from real signal

**Bottom line:** Don't generate the {8 languages × 8 features × 2 versions} grid. Three of your own inputs already tell you it will fail — an unsupported-language claim, an ambiguous demand signal, and a direct statement from the people who talk to customers that the taxonomy is invented, not observed. Build from what you actually know instead.

### Why the matrix fails

- ❌ **You'd be documenting clients you don't ship.** Java, Go, Python are official. Pages for Rust, Ruby, PHP, Elixir, .NET have no first-party code to test against — you'd be writing against community libraries you don't control, or making it up. Users who copy-paste and hit an untested code path file tickets against a page marketing generated, not engineering reviewed. That's a support-cost and trust problem, not a growth channel.
- ❌ **Most of the version axis is fake variation.** 6 of 47 error codes changed message text between v2/v3 — 41 didn't. Forking every page into v2/v3 doubles page count for content that's identical 87% of the time. That's the textbook thin/duplicate-content pattern search engines devalue, and a devaluation event on a doc subdomain can drag down pages that were already ranking.
- ❌ **The one demand signal you have is unreadable.** "antimatter timeout" at 290/90d with no way to tell error-message intent from config-key intent is not evidence a page matters — it's a prompt to go find out, not a green light to build 8 language variants of it.
- ❌ **The people closest to real user pain say this taxonomy doesn't match reality.** Solutions engineers see the actual question distribution. When they say "nothing like this list," that's not a caveat to note and proceed anyway — it's the single strongest piece of data in the brief, and it points away from the plan, not toward a footnote in it.
- ❌ **The whole grid is the weakest possible data source.** It's a combinatorial template with no proprietary or product-derived input — the bottom tier on the defensibility hierarchy (proprietary > product-derived > user-generated > licensed > public). Support tickets and SE call notes are product-derived — one tier up, and you're sitting on them unused.

### What to build instead

**1. Replace 47 × languages × versions of error content with one canonical error reference.**
A single filterable table: code, name, meaning, common cause, fix, and — only for the 6 codes where it's true — a v2-message / v3-message column. This is more useful than a scattered page-per-code-per-version (searchable, linkable, one place to keep correct) and collapses hundreds of near-duplicate pages into one page that's actually maintainable. Add `DefinedTerm`/`FAQPage` schema so individual codes can still surface in search and AI answers without needing separate URLs.

**2. Scope how-to content to what you actually ship: 3 languages × 8 features = 24 pages.**
Java, Go, Python only. Each page gets real code, tested against the actual broker, owned by an engineer, not fabricated for an unsupported runtime. That's a tractable, defensible content set — not "several hundred," 24.

**3. Don't fork by version unless content actually diverges.**
Default every page to version-agnostic. Add one "What changed in v3" migration page that calls out the real deltas (including the 6 error-message changes). Inline version callouts only where behavior genuinely differs — not a full page clone per version.

**4. Resolve "antimatter timeout" before writing anything for it.**
Check on-site search analytics: what do people click after that query — a config-key page or an error page? Cross-reference with support tickets mentioning "timeout." That tells you whether it's one page or two, and which one, in under a day — cheaper than guessing via 16 generated variants.

**5. Make the SE ticket/question corpus the actual content brief.**
Pull the real recurring questions from Zendesk/Intercom/Slack/call notes solutions engineers field. Cluster them. That cluster — not the combinatorial grid — is your roadmap for what to write next after the 24 pages above. This is literally the product-derived data your existing plan was skipping in favor of a synthetic template.

**6. Handle the unsupported languages as a signal, not a doc set.**
One honest "Community & unofficial clients" page listing what exists (Rust, Ruby, PHP, Elixir, .NET), clearly labeled as community-maintained, no fabricated examples. Track search and support demand for those languages separately and feed it to product as a build-vs-don't-build input — that's the correct use of "marketing wants to own the space," not a content op.

**7. Pilot, measure, then decide on scale.**
Ship the 24 + 1 (error reference) + 1 (migration) = 26 pages. Track organic traffic and support-ticket deflection for 60–90 days before generating anything further. If a specific combination proves out, expand it deliberately — don't pre-build the long tail on spec.

### Net effect
~26 pages instead of several hundred. Every page backed by code you actually ship and tested against the real broker. The two ambiguous/weak signals in the brief (the search query, the version fork) get resolved with data instead of guessed at with volume. The one strong signal in the brief (SE ticket reality) becomes the actual roadmap instead of a footnote you overrode.