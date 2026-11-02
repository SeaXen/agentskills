**No, not all 180. Badge the 124 that carry `// Output:`, and only after two checks (below). Give the other 56 a different, weaker badge until they are made deterministic.**

I haven't seen the repo. This applies the docs-code-sample-standards tiers to the counts you gave.

## Why not 180

- **Green `go test ./...` proves less for the 56.** Go compiles every `ExampleXxx` function. It runs one only if it has an `// Output:` or `// Unordered output:` comment. Without that comment the example builds, never executes, and passes.
- **So the 56 are Compile-only tier.** That tier means "valid, not run for you". "Verified" tells a reader "this works as written", which is the Run tier.
- **Untiered samples default to Run**, so a "Verified" badge on the 56 would claim more than CI proves. A reader who pastes a 56-group sample and hits a runtime error will read "Verified" as a lie.

## Do now: ship by tier

1. **124 with `// Output:`:** badge "Verified". Check A and B below first.
2. **56 without:** badge "Compiles" or no badge. Keep the badge for the 56 honest, because it is a claim to the reader. Do not use the same word for both groups.
3. **Page copy for "Verified":** "Output asserted by CI against Ridgeline vX.Y". This states what was checked.

## Check before badging the 124 (about 1 hour)

**A. Does the `// Output:` comment actually count?**
- The comment must be the last comment in the function body. A misplaced one is silently ignored, so the example is Compile-only.
- An empty `// Output:` is valid. It passes whenever the example prints nothing, so it proves nothing.
- Run `go test -v -run Example ./... | grep -c '^--- PASS'`. Expect 124 passes. Fewer means some `// Output:` comments don't count.

**B. Do they run against a real Ridgeline server?**
- If they only hit a mock or fake, "Verified" is true only for the SDK's own logic, not for the database.
- A "Verified" claim needs one scheduled integration run against the real server. Service-side changes break samples without any repo change.
- Install the published module in that run, not the working tree. A working-tree build passes on code no reader can install yet.
- If the 124 run only on push, add a nightly run. Show the age of the last successful run on the page.

**C. Do the docs pages show the tested code?**
- If a page has hand-pasted copies of the `example_test.go` code, the badge describes the file and not the page.
- Pull the tested region into the page at build time. Hide setup with a region marker. Never publish a fragment with its imports cut.

## Fix the 56 (about 14 hours for one engineer, at ~15 minutes each)

Make the output deterministic, then add `// Output:`:

1. **Generated IDs:** print a derived fact, such as `len(id) > 0` or the node label. Do not print the ID.
2. **Timestamps:** inject a fixed clock, or print only whether `created.Before(now)` holds.
3. **Map or result ordering:** sort the results, or use `// Unordered output:`.
4. **Anything that can't be made deterministic** (a live server version, a random seed): keep it Compile-only, label it that on the page, and delete it if it is trivial.

Do the quickstart, auth and first-query samples first. The skill sets a baseline that 100% of samples on the adoption path are Run and green. Confirm all of them are in the 124. If any are in the 56, fix those before anything else.

## Measured against the skill's thresholds

| Gate | Status |
|---|---|
| Pass rate ≥90% (skill baseline, not an industry standard) | Met: 180/180 compile and CI is green. |
| ≥80% of the corpus Run or Compile-only in CI | Met: all 180 are covered. |
| 100% of adoption-path samples are Run | Unknown. Check which group they are in. |
| No sample's last successful run older than the freshness window | Unknown. Needs the scheduled run from B. |

## Next action

Run `go test -v -run Example ./... | grep -c '^--- PASS'` and tell me the number. That settles check A in a minute, and I'll turn the answer into the badge copy for marketing.

Separately: the repo has no sample owner yet. When a sample goes red on a Friday, whose queue does it land in? Want me to draft that rule next?