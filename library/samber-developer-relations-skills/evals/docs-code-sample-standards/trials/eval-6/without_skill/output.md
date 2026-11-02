**Short answer:** Not all 180 today. You can badge 124 now. The other 56 can earn it with a small fix.

## Why the 56 aren't verified

`go test` only runs an `ExampleXxx` function if it ends with an `// Output:` or `// Unordered output:` comment. Without one, Go compiles the function and never calls it.

So for those 56, a green CI run proves only that they compile against the current API. It says nothing about whether they run, return no error, or print what the docs claim. If one panics, hits a bad query, or sends a malformed request, CI stays green.

Putting "Verified" on them would be a false claim.

## What the 124 prove

They compile, run, and print exactly the documented output. That is real verification. Two caveats:
- The claim covers what the output comment checks. If an example prints only a count, that is all it verifies.
- If CI runs them against a real graph database, the claim holds for that DB version. If they use a mock, say so.

## Confirm the numbers first

Check that 124 is the number that actually executes, not just the number with a comment:

```
go test -run '^Example' -v ./... | grep -c '^--- PASS'
```

It should print 124. Anything lower means some examples have a malformed output comment. The comment must be the last comment in the function body.

## How to get the 56 to verified

Pick the cheapest option per sample:

1. **Inject determinism.** Give the SDK a clock and ID generator option and pin them in the example. This reads well in the docs only if the option is a public feature.
2. **Print stable facts, not volatile values.** Print `err == nil`, `len(id) > 0`, node labels, property keys, counts, or a timestamp's `IsZero()` result. Then add `// Output:`. This works for most of the 56.
3. **Assert, then print a marker.** Check the result inside the example with a plain `if` and `log.Fatal`, then `fmt.Println("ok")` with `// Output: ok`. Use this when there is nothing meaningful to print. It runs the code, though it adds noise to the docs sample.

Don't use `// Unordered output:` for timestamps or IDs. It only ignores line order, not line content.

## Make it stay true

- Add a CI check that fails when any `ExampleXxx` lacks an output comment. A small `go/ast` script does it. A new unverified sample then can't slip in.
- Generate the badge from the CI result per sample. Don't hand-place it.
- Embed the docs samples from `example_test.go` by build step. If the site copies the code, the badge describes code that may have drifted.
- Record the Ridgeline version and DB version in the badge tooltip.

## What to tell marketing

- **Now:** "Verified" on 124 samples, defined as "runs in CI, output checked."
- **Optional:** a weaker "Compiles" label for the 56. Don't use "Verified" for them.
- **After the fix:** all 180 with the same badge. How long that takes depends on how many of the 56 fit option 2, which is most of them.

Mixing the two meanings under one badge would hurt more than having no badge. The first user who finds a broken "Verified" sample will stop trusting all of them.