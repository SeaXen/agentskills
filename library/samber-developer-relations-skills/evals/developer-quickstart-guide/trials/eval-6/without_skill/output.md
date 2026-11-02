# Northgate getting-started page — six-language tabs, TypeScript-sourced

Everything below is ready to drop into your Docusaurus repo. Design in one sentence: **TypeScript is the only hand-authored content; every other language is generated from small, structured code snippets (not whole-page prose) and gated behind that SDK owner's GitHub review before it ever reaches the live tab.**

## Why this shape, not "regenerate the whole page"

Translating a full MDX page's prose every run makes diffs huge and gives an LLM more room to drift or hallucinate a method that doesn't exist in that SDK. Splitting the page into **shared prose (templated, byte-identical across languages) + a handful of code snippets (the only thing actually generated)** shrinks the risk surface to what genuinely differs per language, and turns each owner's review into a 4-line JSON diff instead of a full page re-read.

## File layout

```
docs/
  getting-started.mdx                  # the tabbed page (hand-written, stable)
  _getting-started/
    template.mdx                       # shared prose skeleton, {{PLACEHOLDER}} slots
    api-refs/
      python.md  go.md  java.md  ruby.md  rust.md   # owner-maintained, grounds the LLM
    values/
      typescript.yaml                  # hand-authored — the real source of truth
      python.yaml   (generated, PR-reviewed)
      go.yaml        (generated, PR-reviewed)
      java.yaml      (generated, PR-reviewed)
      ruby.yaml      (generated, PR-reviewed)
      rust.yaml      (generated, PR-reviewed)
      *.meta.json                      # sourceHash + timestamp, one per generated language
scripts/
  generate-sdk-docs.ts                 # calls Claude, writes values/<lang>.yaml
  render-sdk-docs.ts                   # deterministic template + values -> <lang>.mdx, runs at build time
.github/
  CODEOWNERS
  workflows/
    sdk-docs-generate.yml
    sdk-docs-staleness.yml
```

`docs/_getting-started/*.mdx` files (except `template.mdx`) are **build output** — add them to `.gitignore`. Docusaurus ignores any file/folder starting with `_`, which is exactly why this directory doesn't turn into extra routed pages.

Because `<lang>.mdx` is only ever produced by the pre-build render step from an already-merged `values/<lang>.yaml`, nothing unreviewed can reach the live tab — there's no separate "publish" step to forget.

---

## `docs/getting-started.mdx`

```mdx
---
id: getting-started
title: Getting Started
---

import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

import TypeScriptGuide from './_getting-started/typescript.mdx';
import PythonGuide from './_getting-started/python.mdx';
import GoGuide from './_getting-started/go.mdx';
import JavaGuide from './_getting-started/java.mdx';
import RubyGuide from './_getting-started/ruby.mdx';
import RustGuide from './_getting-started/rust.mdx';

<Tabs groupId="sdk-language" queryString="lang">
  <TabItem value="typescript" label="TypeScript" default>
    <TypeScriptGuide />
  </TabItem>
  <TabItem value="python" label="Python">
    <PythonGuide />
  </TabItem>
  <TabItem value="go" label="Go">
    <GoGuide />
  </TabItem>
  <TabItem value="java" label="Java">
    <JavaGuide />
  </TabItem>
  <TabItem value="ruby" label="Ruby">
    <RubyGuide />
  </TabItem>
  <TabItem value="rust" label="Rust">
    <RustGuide />
  </TabItem>
</Tabs>
```

`groupId="sdk-language"` is Docusaurus's built-in mechanism — a reader's language choice syncs across every page that uses the same groupId, via localStorage, with no custom code. `queryString="lang"` gives shareable links like `?lang=go`.

---

## `docs/_getting-started/template.mdx` — shared prose, per-language slots

```mdx
## Install

{{INSTALL_CMD}}

## Initialize the client

Create a client once at startup and reuse it across your app.

{{INIT_CODE}}

## Send your first event

{{SEND_EVENT_CODE}}

## Verify it arrived

Open the [Northgate dashboard](https://app.northgate.dev) and confirm the event
shows up within a few seconds. If it doesn't, see [Troubleshooting](/docs/troubleshooting).

## Next steps

- [Configure sampling](/docs/config/sampling)
- [Add custom attributes](/docs/guides/custom-attributes)
- [Instrument background jobs](/docs/guides/background-jobs)
```

Every non-`{{...}}` line is identical across all six tabs by construction. Add a step later (e.g. `{{ASYNC_EXAMPLE}}`) and it flows to all six automatically — the generator picks up new keys from `values/typescript.yaml` without any code change.

## `docs/_getting-started/values/typescript.yaml` — the actual source of truth

```yaml
INSTALL_CMD: |
  ```bash
  npm install @northgate/sdk
  ```
INIT_CODE: |
  ```ts
  import { Northgate } from "@northgate/sdk";

  const northgate = new Northgate({ apiKey: process.env.NORTHGATE_API_KEY });
  ```
SEND_EVENT_CODE: |
  ```ts
  northgate.track("user.signed_up", { plan: "pro" });
  ```
```

This is the file your team edits directly, by hand. Nothing downstream of it is human-authored except review.

## `docs/_getting-started/api-refs/python.md` — owner-maintained grounding

```markdown
# Northgate Python SDK — public API

## Install
`pip install northgate-sdk`

## Client
```python
from northgate import Northgate

client = Northgate(api_key=os.environ["NORTHGATE_API_KEY"])
```

## Tracking
```python
client.track(event_name: str, properties: dict | None = None) -> None
```

Do not use `client.send()`, `client.emit()`, or `client.log_event()` — none exist.
```

One file per language, same pattern. This is what stops the model from inventing a plausible-but-fake method name — it's explicitly told what's real and, just as important, what *looks* real but isn't. **Each SDK owner keeps their own `api-refs/<lang>.md` current** — when a generated snippet is wrong, the fix that prevents recurrence usually belongs here, not in the prompt.

---

## `scripts/generate-sdk-docs.ts`

```typescript
import { readFileSync, writeFileSync, existsSync } from "node:fs";
import { createHash } from "node:crypto";
import { join } from "node:path";
import { parse as parseYaml, stringify as stringifyYaml } from "yaml";
import Anthropic from "@anthropic-ai/sdk";

const ROOT = join(__dirname, "..", "docs", "_getting-started");
const MODEL = "claude-sonnet-5";

const TARGET_LANGUAGES = [
  { id: "python", label: "Python" },
  { id: "go", label: "Go" },
  { id: "java", label: "Java" },
  { id: "ruby", label: "Ruby" },
  { id: "rust", label: "Rust" },
] as const;

const INSTRUCTIONS = `
You translate SDK code snippets for the Northgate observability SDK's
getting-started guide from TypeScript into another language.

Rules:
- Only use methods, classes, and config options that actually appear in the
  API reference you are given. Never invent a method name, even if a
  plausible-looking one would read naturally.
- Keep each snippet the same length and scope as the TypeScript original —
  same number of steps, same level of detail, no extra explanation added
  inside the code fence.
- Use that language's normal idioms (error handling, naming convention,
  package/import style) rather than a literal line-by-line port.
- Preserve the markdown code fence and its language tag (e.g. \`\`\`python).
`.trim();

function sourceHash(templatePath: string, tsValuesPath: string): string {
  return createHash("sha256")
    .update(readFileSync(templatePath, "utf8"))
    .update(readFileSync(tsValuesPath, "utf8"))
    .digest("hex");
}

async function translateLanguage(
  client: Anthropic,
  systemBlocks: Anthropic.Messages.TextBlockParam[],
  language: { id: string; label: string },
  keys: string[],
) {
  const apiRefPath = join(ROOT, "api-refs", `${language.id}.md`);
  if (!existsSync(apiRefPath)) {
    throw new Error(`Missing API reference for ${language.label} at ${apiRefPath}`);
  }
  const apiRef = readFileSync(apiRefPath, "utf8");

  const tool: Anthropic.Messages.Tool = {
    name: "submit_translation",
    description: `Submit the ${language.label} translation for each code snippet key.`,
    input_schema: {
      type: "object",
      properties: Object.fromEntries(keys.map((key) => [key, { type: "string" }])),
      required: keys,
      additionalProperties: false,
    },
  };

  const response = await client.messages.create({
    model: MODEL,
    max_tokens: 4096,
    system: systemBlocks,
    tools: [tool],
    tool_choice: { type: "tool", name: "submit_translation" },
    messages: [
      {
        role: "user",
        content: [
          `Target language: ${language.label}.`,
          ``,
          `Authoritative ${language.label} SDK API reference (do not use anything outside this):`,
          apiRef,
        ].join("\n"),
      },
    ],
  });

  const toolUse = response.content.find(
    (block): block is Anthropic.Messages.ToolUseBlock => block.type === "tool_use",
  );
  if (!toolUse) {
    throw new Error(`${language.label}: model did not return a tool_use block`);
  }

  const translated = toolUse.input as Record<string, string>;
  for (const key of keys) {
    if (!translated[key]?.trim()) {
      throw new Error(`${language.label}: empty translation for "${key}"`);
    }
  }
  return translated;
}

async function main() {
  const checkOnly = process.argv.includes("--check");

  const templatePath = join(ROOT, "template.mdx");
  const tsValuesPath = join(ROOT, "values", "typescript.yaml");
  const currentHash = sourceHash(templatePath, tsValuesPath);
  const tsValues = parseYaml(readFileSync(tsValuesPath, "utf8")) as Record<string, string>;
  const keys = Object.keys(tsValues);

  if (checkOnly) {
    const stale = TARGET_LANGUAGES.filter(({ id }) => {
      const metaPath = join(ROOT, "values", `${id}.meta.json`);
      if (!existsSync(metaPath)) return true;
      const meta = JSON.parse(readFileSync(metaPath, "utf8")) as { sourceHash: string };
      return meta.sourceHash !== currentHash;
    });
    if (stale.length > 0) {
      console.log(stale.map((l) => l.id).join(","));
      process.exit(1);
    }
    process.exit(0);
  }

  const client = new Anthropic(); // reads ANTHROPIC_API_KEY from env

  const systemBlocks: Anthropic.Messages.TextBlockParam[] = [
    { type: "text", text: INSTRUCTIONS },
    {
      type: "text",
      text: `TypeScript source snippets (translate each key, keep the same keys):\n\n${JSON.stringify(tsValues, null, 2)}`,
      cache_control: { type: "ephemeral" },
    },
  ];

  // Fire the first call alone so the cache write lands before anything tries to
  // read it — two identical-prefix calls in flight at once both pay full price
  // instead of the second hitting cache. The remaining four share the now-warm
  // cache and can run concurrently.
  const [first, ...rest] = TARGET_LANGUAGES;
  const firstResult = await translateLanguage(client, systemBlocks, first, keys);
  const restResults = await Promise.all(
    rest.map((lang) => translateLanguage(client, systemBlocks, lang, keys)),
  );

  const allResults = [
    [first, firstResult] as const,
    ...rest.map((lang, i) => [lang, restResults[i]] as const),
  ];

  for (const [lang, values] of allResults) {
    writeFileSync(join(ROOT, "values", `${lang.id}.yaml`), stringifyYaml(values));
    writeFileSync(
      join(ROOT, "values", `${lang.id}.meta.json`),
      JSON.stringify(
        { sourceHash: currentHash, generatedAt: new Date().toISOString(), model: MODEL },
        null,
        2,
      ),
    );
    console.log(`Generated ${lang.label} translation.`);
  }
}

main().catch((err) => {
  console.error(err);
  process.exit(1);
});
```

`Anthropic.Messages.*` type names may need a small adjustment depending on your installed `@anthropic-ai/sdk` version — check `node_modules/@anthropic-ai/sdk/resources/messages.d.ts` if the compiler complains.

## `scripts/render-sdk-docs.ts` — deterministic, no LLM, runs on every build

```typescript
import { readFileSync, writeFileSync, existsSync } from "node:fs";
import { createHash } from "node:crypto";
import { join } from "node:path";
import { parse as parseYaml } from "yaml";

const ROOT = join(__dirname, "..", "docs", "_getting-started");
const LANGUAGES = ["typescript", "python", "go", "java", "ruby", "rust"] as const;

function sourceHash(): string {
  return createHash("sha256")
    .update(readFileSync(join(ROOT, "template.mdx"), "utf8"))
    .update(readFileSync(join(ROOT, "values", "typescript.yaml"), "utf8"))
    .digest("hex");
}

function render(lang: string, template: string): string {
  const valuesPath = join(ROOT, "values", `${lang}.yaml`);
  if (!existsSync(valuesPath)) {
    return `> **${lang} guide coming soon.** This SDK's getting-started guide is being drafted and reviewed by the ${lang} team.\n`;
  }

  const values = parseYaml(readFileSync(valuesPath, "utf8")) as Record<string, string>;
  let body = template;
  for (const [key, value] of Object.entries(values)) {
    body = body.replaceAll(`{{${key}}}`, value.trim());
  }

  if (lang !== "typescript") {
    const metaPath = join(ROOT, "values", `${lang}.meta.json`);
    const meta = JSON.parse(readFileSync(metaPath, "utf8")) as { sourceHash: string };
    if (meta.sourceHash !== sourceHash()) {
      body =
        `:::caution\nThis guide may be out of date. The TypeScript source guide changed ` +
        `since this translation was last reviewed. A refresh is pending ${lang} team sign-off.\n:::\n\n${body}`;
    }
  }

  return body;
}

const template = readFileSync(join(ROOT, "template.mdx"), "utf8");
for (const lang of LANGUAGES) {
  writeFileSync(join(ROOT, `${lang}.mdx`), render(lang, template));
}
```

This covers two edge cases without needing a UI component: a language with **no reviewed content yet** renders "coming soon" instead of breaking the build, and a language whose **source changed since last approval** renders a visible staleness banner instead of silently serving outdated instructions.

---

## `package.json` additions

```json
{
  "scripts": {
    "prebuild": "tsx scripts/render-sdk-docs.ts",
    "start": "npm run prebuild && docusaurus start",
    "build": "npm run prebuild && docusaurus build",
    "generate:sdk-docs": "tsx scripts/generate-sdk-docs.ts",
    "check:sdk-docs-staleness": "tsx scripts/generate-sdk-docs.ts --check"
  }
}
```

**Run** `npm install @anthropic-ai/sdk yaml tsx` **to add the dependencies.**
**Add** `docs/_getting-started/*.mdx` **minus** `template.mdx` **to `.gitignore`** (rendered output, not source).

---

## `.github/CODEOWNERS`

```
docs/_getting-started/values/python.yaml   @northgate/python-sdk-owners
docs/_getting-started/values/go.yaml       @northgate/go-sdk-owners
docs/_getting-started/values/java.yaml     @northgate/java-sdk-owners
docs/_getting-started/values/ruby.yaml     @northgate/ruby-sdk-owners
docs/_getting-started/values/rust.yaml     @northgate/rust-sdk-owners
```

## `.github/workflows/sdk-docs-generate.yml`

```yaml
name: Generate SDK getting-started translations

on:
  push:
    branches: [main]
    paths:
      - "docs/_getting-started/template.mdx"
      - "docs/_getting-started/values/typescript.yaml"
      - "docs/_getting-started/api-refs/**"

concurrency:
  group: sdk-docs-generate
  cancel-in-progress: true

jobs:
  generate:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-node@v4
        with:
          node-version: 20
      - run: npm ci
      - name: Generate translations
        env:
          ANTHROPIC_API_KEY: ${{ secrets.ANTHROPIC_API_KEY }}
        run: npm run generate:sdk-docs
      - name: Open PR with generated changes
        uses: peter-evans/create-pull-request@v6
        with:
          commit-message: "docs(sdk): regenerate translated getting-started guides"
          branch: sdk-docs/auto-update
          title: "docs(sdk): regenerate translated getting-started guides"
          body: |
            Auto-generated from `template.mdx` and `values/typescript.yaml`.
            Each changed language file needs sign-off from its owner (see
            CODEOWNERS) before this merges. Live docs are unaffected until then.
          labels: sdk-docs, needs-owner-review
```

**Add repo secret `ANTHROPIC_API_KEY`** (Settings → Secrets and variables → Actions).

## `.github/workflows/sdk-docs-staleness.yml`

```yaml
name: Check SDK docs staleness

on:
  schedule:
    - cron: "0 9 * * 1" # Monday 09:00 UTC
  workflow_dispatch:

jobs:
  check:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-node@v4
        with:
          node-version: 20
      - run: npm ci
      - id: check
        run: |
          if ! npm run check:sdk-docs-staleness; then
            echo "stale=true" >> "$GITHUB_OUTPUT"
          fi
      - if: steps.check.outputs.stale == 'true'
        uses: actions/github-script@v7
        with:
          script: |
            await github.rest.issues.create({
              owner: context.repo.owner,
              repo: context.repo.repo,
              title: "SDK getting-started translations are stale",
              body: "The TypeScript source guide changed since one or more translated guides were regenerated. Run the `Generate SDK getting-started translations` workflow.",
              labels: ["sdk-docs", "stale"],
            });
```

**Enable branch protection on `main`**: require a review from Code Owners for `docs/_getting-started/values/*.yaml` before merge. That single setting is the actual gate — nothing generated reaches `<lang>.mdx` without it, because `render-sdk-docs.ts` only ever reads from `main`.

---

## Nine-week rollout

| Weeks | Milestone |
|---|---|
| 1 | Real TypeScript content in `values/typescript.yaml`. All six tabs live, five showing "coming soon." Generation + render scripts working end to end for one language. |
| 2–3 | Fan out to remaining four languages, open first PRs, tighten each `api-refs/<lang>.md` against real owner feedback — expect first-pass code to need real fixes, not a rubber stamp. |
| 3–6 | Review cycles, regenerate on every TS edit, capture recurring mistakes as permanent additions to that language's `api-refs` file so they don't reappear next run. |
| 6–8 | Buffer for slow reviewers. Deliberately edit `typescript.yaml` once and confirm the staleness banner + re-review flow fires correctly. |
| 8–9 | Freeze TypeScript source before the conference. Final regen + review pass. Any language not signed off by freeze stays on its "coming soon"/stale state rather than shipping unapproved. |

**Flag now, not week 7:** five owners each reviewing generated content is real review time, and Go/Rust/Java are the languages most likely to need a second pass (checked exceptions, ownership/`Result` handling, idiomatic error wrapping) — confirm their bandwidth for weeks 2–6 this week.