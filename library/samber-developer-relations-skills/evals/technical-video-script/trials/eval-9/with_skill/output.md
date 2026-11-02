Using **technical-video-script** to rewrite this — full skill plus all four references read.

Two things up front, per the skill's "don't invent facts" rule:

- I don't have the contractor's literal file, only your seven beat descriptions — so config/resolver/CTA *wording* below is written to fix the named defect, not transcribed from an original I can't see. Swap in your real strings where marked.
- The 4x claim is **not** carried through as stated. Pass-threshold criterion 7 requires every on-screen/narrated claim to be reproducible on the recording machine — a number with no attached benchmark fails that gate before it fails a style note. It's flagged, not deleted, at the beat where it belongs.

---

## Promise

For an existing v2 user running a monorepo, this video shows exactly why their config broke and how v3's resolver fixes it — migration in under two minutes.

```
Shape:            Changelog / release clip, run long (single breaking-change fix off a real release)
Audience:         existing user hitting this exact error, primary; evaluator comparing v2→v3, secondary
Target runtime:   2:00        Estimated: 1:52 core / 2:14 with cuttable beats
Speaking rate:    [confirm — time a 200-word read on the actual recorder before trusting the estimate below; 150 wpm assumed]
Companion:        migration guide link [confirm URL]
Off-limits:       any real repo/package names visible in the demo monorepo, internal hostnames
```

## Beats

| #   | Visual                                                      | On-screen action                                                                  | Narration                                                                                                                                    | Starting state                                                                 | Est. s | Core/cut |
| --- | ------------------------------------------------------------ | ----------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------- | ------ | -------- |
| 1   | Terminal, split top/bottom                                  | Run the build in the top pane at repo root — passes. Run it in the bottom pane from `packages/api` — fails, error on screen. | "Same config, same command. From the repo root it builds. Two folders deeper, it can't find its own file." | Monorepo demo repo, v2 installed, both panes cleared, top pane at root, bottom pane at `packages/api`. | 12 | core |
| 2   | Terminal, error still on screen                             | Hold the frame on the error.                                                        | "The v2 loader resolved every path relative to the working directory. That's what just broke. v3 fixes it — this is the two-minute migration. You'll need v3.0 or later." [verbatim: version number] | Same as beat 1, no reset.                                                       | 14     | core     |
| —   | **Chapter: Why v2 broke in monorepos ends here**            |                                                                                     |                                                                                                                                                    |                                                                                     |        |          |
| 3   | Editor, `resolver.ts` (v3 source), split with the old v2 line dimmed above it | Zoom on the new resolution call.                                                    | "v3 resolves every path from the config file's own location, not from wherever you ran the command." | New branch/tag checked out, file open at the resolver function, v2 line shown as a code comment above for contrast. | 10 | core |
| 4   | Same terminal split as beat 1                               | Re-run the same two commands, root and `packages/api` — both pass, identical output. | "Same config, same two commands as before. Both pass now, because the result no longer depends on where you ran it. That's what deterministic means here." | v3 installed, same two panes, cleared.                                        | 14     | core     |
| 5   | Editor, `resolver.ts`                                       | Highlight the separator-normalization line.                                        | "One more fix riding along: v3 normalizes backslashes in `extends`, so the same config resolves the same way on Windows." | Same file, same scroll position.                                              | 8      | **cut**  |
| —   | **Chapter: How v3's resolver fixes it ends here**            |                                                                                     |                                                                                                                                                    |                                                                                     |        |          |
| 6   | Editor, `resolver.ts`, cache module highlighted              | Highlight the resolved-path cache.                                                  | "v3 also caches every path it resolves. The first build walks the filesystem. Every build after that reads the cache instead." | Same file, scrolled to the cache module.                                     | 10     | core     |
| 7   | Terminal, two build runs back to back with a timer overlay  | Run a cold build, then a cached build, timer visible on both.                       | `[UNCONFIRMED — contractor's script claims monorepo builds are 4x faster. Do not record a multiplier that hasn't been benchmarked on this machine. Replace with the real cold-vs-cached numbers from this take, e.g. "In this monorepo, that's the difference between an N-second cold build and an M-second cached one" — or cut to "noticeably faster" if a benchmark isn't ready by shoot day.]` | v3 installed, cache cleared for the cold run, warm for the second.           | 12     | **cut**  |
| —   | **Chapter: Migrate your config ends here**                   |                                                                                     |                                                                                                                                                    |                                                                                     |        |          |
| 8   | Editor, v2 config on the left, v3 config on the right (diff view) | Highlight the single changed line: `version` bumped to 3.                          | "Migrating is one line. Bump `version` to 3, and remove any relative-path workaround you'd added for the old bug." | v2 config open, v3 equivalent open in a second pane, both files real (not re-typed). | 11 | core |
| 9   | Terminal                                                    | Run `v3 doctor`, output shows a clean pass.                                         | "Run `v3 doctor` — it - kube control style, said out loud as 'vee-three doctor' — flags anything it can't fix automatically. The full migration guide is linked below." [verbatim: CTA + link] | Same repo, v3 installed, terminal cleared.                                    | 11     | core     |

*(Pronunciation note on beat 9: drop the stray "it - kube control style" aside before recording — that's a leftover reminder to spell out any acronym-like command name on first use, `v3 doctor` doesn't need it. Keeping the instruction here so it isn't silently lost.)*

## Chapters

```
00:00 Why v2 breaks in monorepos
00:26 How v3's resolver fixes it
00:58 Migrate your config
```

Each segment clears the platform's 10-second minimum; three timestamps, ascending, first at `00:00`.

## Cut plan

```
If long by ~15s:  drop beat 5 (Windows caveat) — bonus fix, not the core claim
If long by ~25s:  also drop beat 7 (benchmark) once a real number exists — or drop it outright if none does by shoot day
Never cut:        beats 1-2 (opening), 4 (the determinism proof), 8-9 (migration + CTA)
```
Cutting both cuttable beats still delivers the promise: the bug, the fix, and the migration step all survive.

## Recording brief

- **Starting states**: beats 1 and 4 use the identical two-pane layout — rehearse both from a cold shell, not immediately after each other, so a stale cache doesn't fake the "it works now" result.
- **Off-limits**: scrub the demo monorepo's package names before recording if they resemble anything internal.
- **Claims to re-verify before publish**: the v3 version number in beat 2, the cold/cached numbers in beat 7 (or its removal), the `v3 doctor` command name in beat 9.
- **Caption fix list**: `v3`, `extends`, `resolver.ts`, `v3 doctor`.
- **Clip-able beat**: beat 4 alone (the fail → fix re-run) works as a 15-second short-form clip.

## Runtime

Core beats only: 82 words of narration ÷ 150 wpm (~2.5 wps, **[confirm against the actual recorder's measured rate before locking]**) ≈ 33s of speech + 79s of budgeted dead time (build/command runs, the hold on the error frame, diff reveals) = **≈1:52**, against a 2:00 target. Adding both cuttable beats brings it to **≈2:14** — still inside a reasonable overrun, cut beat 5 first if the take runs long.

---

### Fixes mapped to your seven notes

1. Config file isn't a static opener anymore — it's the second half of a live before/after (beats 1, 8), which is a stronger hook than a file sitting on screen.
2. Kept, verbatim, as the one-sentence diagnosis (beat 2).
3. The three redundant sentences are gone — beat 2 states the cause once; nothing re-describes a file the viewer just watched fail.
4. The unearned jump is bridged: beat 3 states the actual mechanism (resolve from the config's own location), beat 4 *proves* determinism by re-running the exact same before/after demo instead of asserting it.
5. Cache sentence split into three short declaratives (beat 6) — no subordinate clauses left to die in the ear.
6. Windows note demoted to a one-line, explicitly cuttable beat (beat 5) instead of a side-quest — cut it first if runtime's tight.
7. CTA tightened to one concrete action plus a doctor-command safety net (beat 9), marked `[verbatim]`.

Unlisted but caught by the pass threshold: the 4x claim had no attached benchmark, so it's flagged rather than shipped — say the real number from the take, or cut the line.