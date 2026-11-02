Cut beats 1-4 (0:00-1:20). Move first parse result to beat 1. Reshoot; don't re-edit — old footage can't fix a structure problem.

## Diagnosis

Retention data: 38% left by 0:30, curve flat after. Flat-after-30s means the bleed is concentrated in the intro, not scattered later — points straight at beats 1-4, not the parser content itself.

Beat table, current cut:

| # | Time | Content | Function | Status |
|---|------|---------|----------|--------|
| 1 | 0:00-0:07 | Logo + music | Ceremony | high risk |
| 2 | 0:07-0:20 | Greeting, "hope you're having a great week" | Ceremony | high risk |
| 3 | 0:20-0:35 | Topic announced, no proof | Setup | high risk |
| 4 | 0:35-1:20 | npm install, folder, editor, paste config | Dead time | high risk |
| 5 | 1:20 | First parse runs | Payoff | too late |

Three rule violations, all inside the measured window:

1. **Ceremony runs 20s** (logo + greeting). Perception threshold for ceremony reading as filler is ~5s. You're 4x over it before you've said what the video is.
2. **Opening beat's four required jobs — zero delivered by 0:30.** No problem named in the viewer's words, no result on screen, no prerequisites stated, no runtime stated. The platform's own retention metric is scored at exactly this boundary — you're handing it an empty beat.
3. **Payoff lands at 1:20**, outside the window entirely. Setup (install, folder, editor, config) is dead time with nothing proven — that's beat 4's whole 45s.

## Fix: new opening, 0:00-~0:20

Start on the result already running. Setup moves out of the intro — either a later segment or the companion repo, never typed live if it's boilerplate.

| # | Visual | On-screen action | Narration | Starting state | Est. s | Core/cut |
|---|--------|------|-----------|-----------------|--------|----------|
| 1 | Terminal, streaming parse mid-run against a large CSV | Row counter climbing live | "`[unconfirmed — real file size, e.g. '2GB CSV']` streaming through Parsel, no full-file load." | Parse job pre-started, terminal cleared, sample CSV already present | 6 | core |
| 2 | Same terminal, memory counter overlaid | Highlight memory line staying flat while row count climbs | "Memory stays flat because Parsel reads it as a stream, not all at once." | same | 9 | core |
| 3 | Terminal or small face cam | — | "You need `[unconfirmed — Node version]` and the sample CSV linked below. Next `[target runtime]` we wire this into your own project." | same | 8 | core |

Old beat 4 (install → paste config) becomes its own titled segment after the payoff, or gets replaced by a pre-supplied repo clone — per this skill's code-on-screen rule, boilerplate config is never typed live, only the one line that's the actual lesson.

`[unconfirmed]` tags: file size, Node version, target runtime — fill from what you actually shot, don't invent numbers for a public script.

## Chapters (once you have a full cut)

```
00:00 Stream a large CSV without loading it into memory
00:2x Set up Parsel in your project
0x:xx <next claim>
```

## Cut plan

Never cut beats 1-3 (new opening). If reshooting the whole thing is too much, the minimum fix is: kill the logo+greeting to ≤5s, and hard-cut straight from "welcome back" to the running parse — install/config moves after.

Next: reshoot beats 1-3 against your existing demo env, splice ahead of the old footage, re-check the 30s retention number against this baseline (38%).