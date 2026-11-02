**Skip the badges. Fix the order first.** Cutting badges is the fastest edit, not the highest-leverage one — a demo-day reader never sees them if they bounce before scrolling past 8 sections of clutter to find `npm install`. Sequence below is ranked by what actually changes a judge's decision in the 30 seconds they spend on your README, not by edit speed.

## Fix order

1. **Reorder the file.** Install buried at the bottom is the actual landing-page bug — everything else is polish on top of a broken funnel.
2. **State maintained status.** A silent README reads as abandoned by default; judges actively screen for this.
3. **Add the Node version to install.** A failed `npm install` live on a demo floor is the one failure mode you can't recover from — worse than any README flaw.
4. **Rewrite "Why streamsmith."** "Simple and fast" answers nothing; a judge's next question is "why not `kcat`/`kafka-console-consumer`," and the README should pre-empt it.
5. **Trim badges to 4.** Correct instinct, wrong priority — do it last, it's cosmetic.

## Section order (top to bottom)

```
Logo (if any) + name + one-liner
Maintained-status line
Badges (max 4)
Hero example (terminal gif or snippet)
Why streamsmith
Install
Quick start / Usage
Documentation link
Contributing
License
```

## Ready-to-paste blocks

**Maintained-status line** — goes directly under the one-liner, above the badges:

```markdown
🟢 **Actively maintained** — new releases roughly every [X weeks], last release [YYYY-MM-DD].
```

Pair it with one badge instead of prose alone:

```markdown
[![Last commit](https://img.shields.io/github/last-commit/halyard-labs/streamsmith)](https://github.com/halyard-labs/streamsmith/commits/main)
```

**Badges — keep 4, cut the rest:**

```markdown
[![CI](https://github.com/halyard-labs/streamsmith/workflows/CI/badge.svg)](https://github.com/halyard-labs/streamsmith/actions)
[![npm version](https://img.shields.io/npm/v/streamsmith.svg)](https://www.npmjs.com/package/streamsmith)
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)
[![Last commit](https://img.shields.io/github/last-commit/halyard-labs/streamsmith)](https://github.com/halyard-labs/streamsmith/commits/main)
```

Drop the other 7 (stars/social, coverage, discord-if-quiet, etc.) — each additional badge past 4 reads as noise, not trust.

**Install block** — pull the exact minimum version from `package.json`'s `engines` field or your CI matrix before pasting; don't guess it, a wrong version claim breaks trust worse than an unstated one:

```markdown
## Install

Requires Node.js >= <FILL FROM package.json engines.node> (LTS).

\`\`\`bash
npm install -g streamsmith
\`\`\`

Or run without installing:

\`\`\`bash
npx streamsmith replay <topic>
\`\`\`
```

**"Why streamsmith" rewrite** — replace the one-liner with 3 concrete, true differentiators. Don't invent features you can't demo; fill the bracketed claims with what the tool actually does, keep only what survives:

```markdown
## Why streamsmith

- **[Timing-accurate replay]** — replays messages at original produce-time intervals, not just as fast as possible, so downstream consumers see realistic load.
- **[Time/offset range selection]** — replay a specific window (`--from`, `--to`) instead of an entire topic.
- **[Type-safe config]** — TypeScript-native config and plugin hooks, no YAML guessing.
```

If any of those three isn't real, swap it for whatever genuinely distinguishes streamsmith from `kcat`/`kafka-console-consumer` scripting — one true differentiator beats three vague ones.

**Hero example** — add right after the badges, before "Why." A terminal block is enough if you don't have time to record a gif before Friday:

```markdown
\`\`\`bash
$ streamsmith replay orders --from 2026-09-01T00:00:00Z --speed 1x
▸ replaying orders (14,203 messages) → localhost:9092
▸ [====================] 100% · 14,203/14,203 · 2m41s
\`\`\`
```

Do 1–4 this afternoon; 5 (badge trim) takes two minutes whenever you get to it.