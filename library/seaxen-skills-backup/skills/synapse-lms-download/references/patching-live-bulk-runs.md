# Patching a live bulk download — what does and does not work

You've been running `download_nested.py` for 5 hours. You discover a bug in `_dl()` (a NameError, a missing constant, an import that was never added). You fix it with `patch`. Nothing changes — the next segment that downloads still hits the same error.

**This is expected. Python imports modules once at startup.** The interpreter is still running the old bytecode. Your patch to the .py file only affects the **next** process invocation. The live bulk download is doomed to repeat its bug for every video it tries from now on.

## What to do (in order)

1. **Don't kill the live process to "fix" it.** Killing a 5-hour run to restart it from scratch is the wrong move. The live process is making real progress — 1-2 minutes of CDN downloads per video adds up fast, and killing it resets all the work to disk (which is fine) but burns the wall-clock time you've already spent.

2. **Verify the live process is still making progress.** Look at the log — are new "Downloaded N/M segments" or "✓ Lecture" lines still appearing? If yes, it's working through the bug one segment at a time. If no, it's stuck in a retry loop and should be killed. (For the `_dl()` NameError case, the script aborts that video but moves on, so progress continues.)

3. **Queue the fix for the next run.** Save the patch. Don't apply it then expect the live process to see it — the interpreter doesn't reload.

4. **Let the live process finish (or kill it if you have a better plan).** When it's done, re-run the script. The new process loads the patched code, skips the videos already in state, and only does real work for the ones that haven't been downloaded yet.

5. **If the fix is to a code path that the live process will hit again (e.g. a per-segment retry helper), wait it out.** The live process will accumulate more `⚠ N/M segments failed` warnings, but those are acceptable (see pitfall 20 in SKILL.md). The post-process at the end will re-download them with the new code.

## The "I'll patch it now and then explain the trick" trap

The user will sometimes ask "is the bug fixed?" right after you've patched. The right answer is **"the fix is on disk; the running process won't see it until it restarts. I can restart it cleanly, or let it finish and the fix applies to the re-download pass."** Don't claim the live process is fixed when it isn't.

## When you SHOULD kill the live process

- It's stuck in a tight retry loop and not making forward progress (no new "Downloaded N/M" lines for >5 min)
- It's deleting files it shouldn't (e.g. a bug in the success path that wipes the just-saved .mp4)
- It's about to OOM or hit some other resource limit
- The user explicitly says "kill it"

The cost of restarting is one "traverse the whole course again" pass, which is cheap (state skips) but still ~5-10 min of login + chapter enumeration.

## The delete-then-redownload hazard

`--fix-failures` mode does:
```python
for sid, info in to_fix:
    old_path = out_root / info["subpath"] / info["filename"]
    old_path.unlink(missing_ok=True)   # ← file is now GONE from disk
    del state["downloaded_videos"][sid]  # ← and from state
```

Then it falls through to the main download loop, which re-downloads them. **If the re-download fails (new code has a bug, network outage, etc.), the user is in a worse state than before:** the file is gone from disk AND from state, and the main loop won't re-attempt it until the next full run.

Mitigations to add before running `--fix-failures` against a new code version:

- **`--fix-failures-dry-run`** flag that just prints `would delete: <path> (<size MB>)` for each `to_fix` entry and exits. Lets you sanity-check the list before destruction.
- **Soft-delete fallback:** instead of `unlink()`, move the failed file to `<old_path>.quarantine/`. If the re-download succeeds, the quarantine copy is removed. If it fails, the quarantine copy is restored. Belt-and-braces insurance.
- **Single-item test mode:** `--fix-failures-one <stream_id>` to exercise the delete-redownload flow on ONE known-broken video before doing all of them at once.
- **Smoke test the new code first.** Before adding the `_dl()` retry helper, run it on a single known-good video and confirm it produces a valid MP4 with `ffprobe`. Then run post-process.

## Concrete example (Sharif 2026-06-19)

The main download accumulated 2 videos with 1-failed-segment each (GIT Physiology, Renal). Post-process ran `--fix-failures`, deleted both, started re-downloading them — and the new `_dl()` helper hit a `NameError: SEG_URL_TEMPLATE is not defined` (the constant was never created; the old code had the URL inline in the main download function). Both re-downloads aborted after 21+ NameError failures. Now both files were gone from disk AND from state.

Recovery: a fresh `download_nested.py sharif` re-ran the whole course. State was missing 2 entries (the just-deleted GIT + Renal), plus 2 brand-new videos that the original run never got to (Anatomy Previous Year's, Offline Class:Blood). All 4 re-downloaded with the FIXED `_dl()`. No data lost because the re-run picked up everything.

Lesson: the second pass saved the day, but only because state correctly reflected the missing videos. If state had been out of sync (e.g. the `del state[...]` line had been silently skipped due to a partial write), the second pass would have skipped those 4 videos and they'd be permanently lost.

**Always verify state consistency after a destructive operation.** `cat accounts/<name>.json | python3 -c "import json,sys; d=json.load(sys.stdin); v=d.get('downloaded_videos',{}); print(f'videos: {len(v)}')"` and `find <dest> -name "*.mp4" | wc -l` should match. If they differ, the state or the disk has drifted from the other.
