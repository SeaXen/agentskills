
# liarjs skills

**Agent Skills for browser fingerprint testing and automation-harness QA.**

Four skills that teach a coding agent to run [`liarjs`](https://www.npmjs.com/package/liarjs):
40 consistency checks over 19 fingerprint probes, cross-checked against what the TLS/HTTP layer
actually saw.

[liarjs.dev](https://liarjs.dev) - [what the checks mean](https://liarjs.dev/cli/) - [field notes](https://liarjs.dev/blog/)


```bash
npx skills add liarjs.dev                  # from the site's well-known endpoint
npx skills add liarjsdev/liarjs-skills     # from this repo
```

## The skills

| skill | use it when |
|---|---|
| [`browser-fingerprint-audit`](skills/browser-fingerprint-audit/) | run a browser fingerprint test and read the result: canvas, WebGL, WebGL2, WebGPU, audio, 220 fonts, WebRTC, timezone, TLS |
| [`playwright-stealth-verify`](skills/playwright-stealth-verify/) | check whether a Playwright, Puppeteer, Selenium or CDP-driven browser presents a coherent fingerprint, as an assertion in a test |
| [`fingerprint-ci-gate`](skills/fingerprint-ci-gate/) | fail a GitHub Actions or GitLab job on a fingerprint regression, with a baseline diff |
| [`fingerprint-failure-triage`](skills/fingerprint-failure-triage/) | turn a low score into a shortlist of things to change, by check id |

Each skill is a directory with a `SKILL.md` following the [Agent Skills](https://agentskills.io)
format, so it works in any client that supports the standard: Claude Code, Codex, Cursor,
GitHub Copilot, VS Code, Gemini CLI, OpenCode, Amp, Windsurf, Goose, Kiro and others.

## Install

With the cross-agent installer:

```bash
npx skills add liarjs.dev                                               # all four, from the site
npx skills add liarjsdev/liarjs-skills                                  # all four, from this repo
npx skills add liarjsdev/liarjs-skills/skills/browser-fingerprint-audit # just one
```

`liarjs.dev` works because the site publishes this same tree at
`/.well-known/agent-skills/index.json` (RFC 8615), so no directory site sits between you and the
skills. The generator lives in the site repo as `scripts/sync-skills.mjs` and takes this repo as its
source of truth.

Or copy a skill directory into the location your agent reads:

| agent | path |
|---|---|
| Claude Code | `~/.claude/skills/` (user) or `.claude/skills/` (project) |
| Codex | `~/.agents/skills/` |
| GitHub Copilot | `~/.copilot/skills/` (user) or `.github/skills/` (repo) |

## What the underlying tool does

A browser controls its own JavaScript. It does not control the network it connects over. `liarjs`
reads the fingerprint inside the browser, reads the TLS/HTTP/ASN view from the edge that served the
request, and reports every place the two stories disagree.

```
   18 / 100  Likely spoofed / bot

  x navigator.webdriver -40
    webdriver=true, the automation flag is set.
    id: webdriver

  x Worker <-> main-thread consistency -20
    A Web Worker reported different values than the main thread for userAgent, canvasHash.
    id: worker-consistency

  22 checks - 2 critical - 1 warnings - 18 clean
  edge: 203.0.113.7 - AS4058 - LAS - HTTP/2 - TLSv1.3
```

32 of the 40 checks need nothing but the browser (`--offline`). 8 compare the JavaScript story
against the wire. Full list with deductions:
[`checks.md`](skills/browser-fingerprint-audit/references/checks.md).

Requirements: Node 22 or newer, and a local Chrome, Chromium or Edge. `liarjs` has zero runtime
dependencies.

## Scope and safety

These skills are measurement and diagnostics. They ship no evasions, profiles or proxies.

- A scan launches its own Chrome with a fresh profile in a temp directory and deletes it when the
  run ends. It does not read the user's browser profile, history, cookies or saved credentials.
- No token, login or account is involved. The skills never ask an agent to handle secrets.
- Nothing is fetched at runtime that changes agent behaviour: the instructions and reference files
  are the whole content, and the npm package is version-pinned in every command.
- Probes run on `about:blank` by default. The skills do not direct an agent to browse third-party
  sites, and they state that scan output is data to relay rather than instructions to follow.
- Attaching to an already-running browser (`--cdp`) is documented as an explicit, user-requested
  path, not a default, because that drives a session the user owns.
- The one outbound request in the default path is the browser under test fetching
  `https://liarjs.dev/api/net.json`, which answers with what Cloudflare saw about that request.
  `--offline` makes no request at all; `--endpoint <url>` points at your own deployment of that
  Worker. liarjs.dev does not store scans.

## Related packages

| package | what it is |
|---|---|
| [`liarjs`](https://www.npmjs.com/package/liarjs) | the CLI and library API these skills drive |
| [`@liarjs/collect`](https://www.npmjs.com/package/@liarjs/collect) | the 19 browser-side probes, standalone |
| [`@liarjs/checks`](https://www.npmjs.com/package/@liarjs/checks) | the 40 consistency rules as pure functions |

Source for all three: [github.com/liarjsdev/liarjs](https://github.com/liarjsdev/liarjs).

## Limits worth stating up front

- A score is not a ban prediction. It measures internal coherence. Real sites also weigh IP
  reputation, account age and behaviour, none of which a local scan can see.
- Headless is detected on purpose. A stock headless run loses points, and that is the correct
  measurement.
- Checks drift with Chrome. The rules are versioned with the package and reviewed per Chrome major,
  which is why every command here pins a version.

MIT (c) liarjs.dev
