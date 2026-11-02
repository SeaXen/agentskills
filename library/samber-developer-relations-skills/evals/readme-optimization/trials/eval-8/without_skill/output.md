## README audit — petrichor-cli/haze

**Verdict: ❌ Does not pass.** All six lines are either unverifiable as written, missing the object of their claim, or make an assertion that needs supporting detail before it belongs in a README. None are actively self-contradictory, but none are shippable as-is either.

| Line | Status | Issue |
|---|---|---|
| `pip install haze` | ⚠️ | Package name is a single generic word — high collision risk on PyPI, and it doesn't match the repo namespace (`petrichor-cli/haze`). Confirm the PyPI project is actually this tool before publishing the line, not an unrelated squatted/abandoned package. |
| "handles 10k requests/sec on a laptop" | ❌ | Unscoped benchmark claim: no hardware spec, no methodology, no reproducible script, no definition of "request" (HTTP? bytes? what payload?). This is a marketing number dressed as a fact. Either link a `BENCHMARKS.md` with hardware + method, or cut it. |
| `--watch` re-runs on file change | ✅ | Fine as a one-liner. Minor: doesn't say which paths are watched or whether it's debounced — acceptable for a README, belongs in `--help`/flags reference if not already there. |
| "Works on Python 3.8+" | ⚠️ | Must match `python_requires` in packaging metadata and the CI test matrix, not just prose — otherwise it's an unverified claim. Also: Python 3.8 hit EOL in Oct 2024; asserting it as the floor in a 2026 README is likely stale and worth double-checking against current CI. |
| "Automatically reconnects when the upstream drops" | ❌ | No retry policy given — backoff strategy, max attempts/timeout, whether it's configurable, what happens to in-flight requests. For a networked tool this is exactly the detail that determines whether the feature is trustworthy; the claim alone is not enough. |
| "Case-insensitive by default" | ❌ | Missing the object. Case-insensitive about what — commands, config keys, flag names, pattern matching, headers? "By default" implies a way to opt out, but no flag for that is mentioned. As written this sentence is ambiguous, not just under-specified. |

**To pass:** name the missing object/scope on the case-insensitivity and reconnect lines, attach a reproducible benchmark or delete the throughput claim, and confirm the PyPI package identity and Python floor against actual packaging metadata rather than prose assertion.