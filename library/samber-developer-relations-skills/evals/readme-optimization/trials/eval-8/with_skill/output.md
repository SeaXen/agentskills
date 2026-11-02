## README audit — petrichor-cli/haze (audience: not established — see note)

I don't have the repository to read: there's no local checkout of `petrichor-cli/haze` I can find, and you've confirmed no shell/command execution is available either. That changes what this audit can honestly claim. Per the skill this audit follows, an install check or a behavioral claim can only be marked passed against its actual source of truth — never on inspection, never from memory of how a similar CLI "probably" works. With zero repo access, every one of the six lines you gave me stays unverified, not verified-by-me.

```
README audit ; petrichor-cli/haze   (audience: not established)
Band A: A1 not assessed · A2 UNRESOLVED (cannot execute; not run) · A3 FAIL (6/6 claims unverifiable, no source available) · A4 not assessed · A5 not assessed
Claim check: 6 unverifiable of 6 given
Band B: not scored — only 6 isolated lines supplied, not the full README
Verdict: does not pass ; A2 and A3 both blocking on their own
```

### Claim check — each line routed to the source it needs, none of which I have

| Line | Category | Source of truth required | Status |
|---|---|---|---|
| `pip install haze` | install command | run from clean state | **not run** — see A2 below |
| "handles 10k requests/sec on a laptop" | performance/scale claim | benchmark script, CI benchmark job, or changelog entry in the repo | unverifiable — no such artifact available to me. As phrased it's also under-specified (no hardware baseline, no definition of "request," no methodology), so even a real benchmark wouldn't fully cover this sentence as written |
| `--watch` re-runs on file change | documented flag | the CLI's argument parser | unverifiable — cannot confirm the flag is actually registered. A documented flag the parser doesn't define is a hallucination, not a typo, so this can't be waved through |
| "Works on Python 3.8+" | version requirement | `python_requires` in the package manifest, or the CI test matrix | unverifiable — also worth flagging independent of source-checking: Python 3.8 reached EOL in October 2024, so if this is genuinely the floor in a 2026 release, confirm it's intentional and not stale copy |
| "Automatically reconnects when the upstream drops" | behavioral assertion hidden in a verb | the reconnect/retry logic in the connection-handling code | unverifiable — and even once sourced, the line is missing the details a reader needs to trust it: backoff policy, retry limit, whether it's configurable |
| "Case-insensitive by default" | behavioral assertion hidden in a verb | whatever subsystem does the case handling | unverifiable — also missing its object: case-insensitive about what — commands, config keys, flag names, pattern matching? "By default" implies an opt-out that isn't named either |

### A2 — the install check specifically

I'm not marking this passed on inspection. To resolve it, please:

1. Start from a clean state — a fresh container or virtualenv, not your dev machine.
2. Run `pip install haze` exactly as documented.
3. Run the first usage example exactly as written (you didn't include this one — please send it too; I only have the six lines above, not the usage block).
4. Paste back the actual output, including the Python version used, and note anything the README didn't warn you about (a missing system package, a required env var, output that doesn't match what's documented).

### Verdict

**Does not pass.** Band A only needs one failure to sink the whole README, and this one has two: A2 is unresolved because nothing has been executed, and A3 fails outright because all six lines are unverifiable claims with no source behind them from where I'm sitting. I can't score A1, A4, A5, or any of Band B — you sent isolated claim lines, not the full file, so I have no opening two lines to check for identity, no status statement to judge, no licence section, and no sense of section ordering or badge count.

### What would actually move this forward

Sending me any of the following resolves the corresponding row above, not a substitute for it:

1. The install + first-usage output from a clean environment (A2).
2. The argument-parser source (confirms or kills `--watch`).
3. `pyproject.toml`/`setup.py` (confirms or corrects "Python 3.8+").
4. A benchmark script, CI job, or changelog entry behind "10k requests/sec" — absent that, cut the line rather than keep it unsourced.
5. The reconnect/retry code and the case-handling code for the two behavioral claims.
6. The rest of the README, so I can score A1/A4/A5 and Band B instead of leaving them blank.