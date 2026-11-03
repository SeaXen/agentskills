---
name: yoinks-ink-tui-downloader
description: Use when building an Ink terminal TUI or wrapping yt-dlp.
---

# yoinks — Ink TUI video downloader

Repo: `pablostanley/yoinks` · MIT · TypeScript · v0.3.1 · 31 files · 1,943 LOC · 1.3k stars.
A full-screen **Ink** (React-for-terminal) TUI wrapping **yt-dlp**: paste a URL → format picker → download to `~/Downloads`. YouTube, X, Instagram, Threads, TikTok + 1,800 sites via yt-dlp's extractors. Node 18+, ESM, bundled with tsup into one 52 KB `dist/cli.js`. Deps: `ink@7`, `react@19`, `ink-select-input`, `ink-spinner`, `ffmpeg-static`.

Verified locally 2026-09-28: `npm test` 6/6 pass, `tsc --noEmit` clean, build 52.10 KB.

## Layout

```
src/cli.tsx              arg handling, alt-screen lifecycle, crash handlers
src/app.tsx (513)        phase state machine, all interaction
src/theme.ts (69)        auto/light/dark via unset colors
src/lib/ytdlp.ts (340)   binary resolution, probe, format building, download protocol
src/lib/click-map.ts (82) frame capture + hit-testing  ← the clever one
src/lib/use-mouse-click.ts  SGR mouse decoding + leak scrubbing
src/components/text-input.tsx (198)  readline-grade line editor
src/components/logo.tsx (110)  animated ASCII logo
src/components/{panel,fullscreen,progress-bar,framed-input,shortcuts}.tsx
src/lib/{args,format,history,clipboard,platforms}.ts
```

## The five techniques worth stealing

### 1. Mouse clicks in Ink with no position API

Ink exposes no absolute-position API. The author's first attempt re-derived each widget's cell rectangle from layout math and **broke every time the layout changed**. The fix: proxy `process.stdout.write`, keep a stripped copy of every frame, and hit-test by **searching for the label text**.

```ts
// wrap stdout so every frame ink writes is kept for hit-testing
export function captureFrames<T extends NodeJS.WriteStream>(stream: T): T {
  return new Proxy(stream, {
    get(target, prop) {
      if (prop === 'write') {
        return (chunk: unknown, ...rest: unknown[]) => {
          const lines = String(chunk).split('\n').map(stripAnsi)
          if (lines.some(l => l.trim() !== '')) frameLines = lines
          return (target.write as (...args: unknown[]) => boolean)(chunk, ...rest)
        }
      }
      const v = Reflect.get(target, prop)
      return typeof v === 'function' ? v.bind(target) : v
    },
  })
}

export type ClickTarget = {match: string; action: () => void; padX?: number; padY?: number}
export function clickTargetAt(x, y, targets) {
  for (const t of targets) {
    const {match, padX = 1, padY = 0} = t
    for (let row = y - 1 - padY; row <= y - 1 + padY; row++) {
      const line = frameLines[row]; if (!line) continue
      let i = line.indexOf(match)
      while (i !== -1) {
        if (x - 1 >= i - padX && x - 1 <= i + match.length - 1 + padX) return t
        i = line.indexOf(match, i + 1)
      }
    }
  }
  return undefined
}
```

Two invariants: frame line *i* maps to terminal row *i+1* (ink draws from the top of the alt screen and rewrites the whole frame), and cursor-only updates carry no printable text so they're ignored — the last real frame survives.

### 2. Terminal-native theming by LEAVING COLORS UNSET

The `auto` theme sets every color to `undefined`. ANSI defaults already follow the user's terminal theme — more reliable than detecting light vs dark.

```ts
auto: {mode: 'auto', primary: undefined, gray: undefined, dark: undefined, background: undefined,
       dimSecondary: true, inverseButton: true}
light: {primary: '#18181b', gray: '#52525b', dark: '#ffffff', background: '#ffffff', ...}
dark:  {primary: '#ffffff', gray: '#a1a1aa', dark: '#18181b', background: '#18181b', ...}
```

Cycle with `^t` or the footer control; start with `--theme auto|light|dark`. Two flags beyond color: `dimSecondary` and `inverseButton` switch between *dim ANSI* and *explicit hex*, because those render differently per terminal.

Test it by asserting the emitted escape codes, not the logic:
```ts
assert.match(renderPanel('light'), /\x1b\[48;2;255;255;255m/)   // forced → explicit bg
assert.doesNotMatch(renderPanel('auto'), /\x1b\[48;2;/)        // auto → terminal default
```

### 3. ASCII logo animation

`logo.tsx` draws "YOINKS" in `█▀▄▓░`, then: intro (900ms, each glyph flickers `░` → `▒` → solid, with a per-column delay), and a shimmer beam every 7s that leans right as it climbs (tilt 2 cols/row, half-width 2.4), thinning each glyph one density step.

The detail that matters: **full-cell blocks swap to a lighter shade char, but half-blocks (`▀ ▄`) only dim** — swapping a half-block would spill the effect outside the letterform.

```ts
const LIGHTER: Record<string,string> = {'█': '▒', '▓': '░'}
const HALF_BLOCKS = new Set(['▀', '▄'])
```
Rows are rendered as **grouped color segments** so each row is a few `<Text>` spans, not 24.

### 4. Drive yt-dlp as a line protocol

Don't scrape a progress bar. Ask for structured lines:

```
--progress-template "download:YOINK|%(progress.downloaded_bytes)s|%(progress.total_bytes)s|%(progress.total_bytes_estimate)s|%(progress.speed)s|%(progress.eta)s"
--print after_move:filepath        # final output path
--no-quiet --newline               # --print implies --quiet, which kills [Merger] lines
```

Then prefix-match stdout: `YOINK|` → progress (a *decrease* in downloaded bytes means a new part), `Downloading 1 format(s): 395+251` → count parts by splitting on `+`, `[Merger]`/`[ExtractAudio]` → processing phase + track destination paths, `[download] Destination:` → track more paths, a bare absolute path → the final file.

```ts
// pick one best format per height, prefer mp4 + avc
function scoreVideo(f: RawFormat): number {
  let s = f.tbr ?? 0
  if (f.ext === 'mp4') s += 10_000
  if (f.vcodec?.startsWith('avc')) s += 5_000
  return s
}
// video: `-f bv*[height=${h}]+ba/b[height=${h}]/bv*[height<=${h}]+ba/b --merge-output-format mp4`
// audio: `-f ba/b -x --audio-format mp3 --audio-quality 0`
```

**Cancel cleans up after itself** — every destination is collected during the run, then on abort:
```ts
function removePartials(dests: string[]) {
  return Promise.allSettled(dests.flatMap(d => [d, `${d}.part`, `${d}.ytdl`])
    .map(f => fs.rm(f, {force: true})))
}
```

Binary resolution, no Python required: system `yt-dlp` → `~/.yoinks/bin/yt-dlp` → download the standalone from GitHub releases (asset name switches on platform **and** `arch === 'arm64'`). Atomic: stream to `.download`, `chmod 0755`, `rename`. ffmpeg from PATH or `ffmpeg-static`; yt-dlp still works without it for single-file formats.

### 5. Yoga-layout hardening (the code comments are the lesson)

Every Ink layout trap this repo hit, with the fix:

- **`<Box height={1}/>` spacers collapse.** Ink boxes default to `flexShrink: 1`, so spacers are the first thing yoga crushes on overflow. Use explicit `<Text> </Text>` lines inside a `flexShrink={0}` column.
- **Odd centering leftover** makes yoga give *every direct child* a `*.5` y-position and round each independently → spacers collapse into neighbors while extra blanks open elsewhere. Wrap all children in a single `<Box flexDirection="column" alignItems="center" flexShrink={0}>`.
- **Fixed-width numeric slots.** `5%` vs `100%` changes line width and the whole layout jumps on every progress tick. Use `padStart`/`padEnd` on every changing value (`${pct}%`.padStart(4), speed.padStart(10), eta.padEnd(12)).
- **Make every state branch the same height** (bar / gap / meta = 3 rows) so switching states doesn't reflow.
- **Native borders can't embed a title.** Draw the top border by hand, then `borderStyle="round"` with `borderTop={false}` for the rest.
- **Full-screen height** is `rows - 1`, and columns fall back to 80 when `stdout.columns` is 0/undefined.

## Gotchas

- **Mouse reports leak into text input.** SGR click reports also flow through ink's keypress parser, which strips the leading ESC and hands `<0;34;12M` to the input as typed text. Scrub every `onChange`:
  ```ts
  export const stripMouseReports = (v: string) => v.replace(/\u001B?\[?<\d+;\d+;\d+[Mm]/g, '')
  ```
- **Mouse needs SGR mode**: `ESC[?1000h` (report presses) + `ESC[?1006h`. While active the terminal's native text selection needs a modifier key — that's the tradeoff.
- **Restore the alt screen BEFORE a crash prints**, else the stack trace is wiped along with the screen and the app looks like it silently quit:
  ```ts
  const enterAltScreen = () => process.stdout.write('\x1b[?1049h\x1b[H')
  // also disable mouse tracking — a crash can skip React effect cleanup
  const leaveAltScreen = () => process.stdout.write('\x1b[?1006l\x1b[?1000l\x1b[?1049l')
  for (const ev of ['uncaughtException', 'unhandledRejection']) {
    process.on(ev, (e) => { leaveAltScreen(); console.error(e); process.exit(1) })
  }
  ```
- **`spawnSync` blocks ink mid-frame.** A synchronous spawn freezes rendering — the user hits enter and sees nothing until it returns. Use async `spawn`.
- **Read the version from `package.json`** at runtime (`createRequire(import.meta.url)('../package.json').version`) so npm bumps can't drift from a constant.
- **Reject multi-line clipboard content** — `new URL()` silently strips newlines, so a pasted block could produce a bogus URL.
- A bare `<Box height={n}/>` is not a spacer; a `<Text> </Text>` is.

## Patterns to reuse in other Ink TUIs

- Readline-grade line editing ink-text-input lacks: word jumps (⌥←/→, ⌥b/f), word delete (⌥⌫, ^w), kill line (^u/^k), home/end (^a/^e), shift+arrow selection, ↑/↓ history recall, paste auto-submit, horizontal scroll to keep the cursor in view.
- Phase as a **discriminated union** (`{name: 'input'|'probing'|'picking'|'downloading'|'done'|'error', ...}`) with a `HINTS: Record<Phase['name'], Array<[string,string]>>` map for the footer, so every state declares its own key hints.
- `AbortController` per long operation, threaded into `spawn` and `fetch`.
- Persist a deduped, capped (50) history to `~/.config/<app>/history.json`; never let a history write failure break the main flow.
- Platform detection by hostname match with `hostname === h || hostname.endsWith('.' + h)` — subdomain-safe.

## Build & dev

```sh
npm install
npm run dev          # tsup --watch
npm run typecheck    # tsc --noEmit
npm test             # tsx --test src/**/*.test.ts
node dist/cli.js <url>
npm link             # try as a global command without publishing
```
`prepublishOnly` = test → typecheck → build. tsup: single entry `src/cli.tsx`, ESM, `target: node18`, shebang banner, `files: ["dist"]`.

## Status

v0.3.1. Only 6 tests (args parsing + theme rendering) — **the TUI interaction is untested**, so don't trust its layout under unusual terminal sizes. Roadmap: `--best`/`--mp3` (scriptable mode), `-o` outdir, playlists, clipboard auto-suggest, self-update for the bundled binary.

Fair-use note from the author: personal-archiving tool; only download what you have the right to keep.