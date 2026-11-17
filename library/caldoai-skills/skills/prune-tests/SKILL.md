---
name: prune-tests
description: Prune tests that guard no behavior from a codebase.
argument-hint: "[optional path]"
---

Prune every test that guards no behavior.

**1. Find what each test depends on**

Keep a test only if it depends on the intended behavior: it should change only when that behavior changes, and fail only when it regresses. Otherwise, it depends on one of three things:

**The past:** it guards code that no longer exists, so it has no reason of its own to change. For example:

- A feature was removed, and tests assert it's gone. Removed code never changes, so they can't catch a regression.
- A module was moved, and a test asserts it's absent from its old path.

**Nothing:** no change to the code can make it fail, so it has no reason of its own to change. For example:

- It tests the browser: a `<button>` renders, or a click event fires. The browser is already tested.
- It asserts what the type system already guarantees.

**The implementation:** it changes whenever the code does, even when behavior didn't. For example:

- The expected value is derived from the same logic as the code, so a wrong result still passes.
- It asserts private state, internal call order, or which helper was invoked.

**2. Prune**

Delete every test that isn't anchored to intended behavior. Where one also covers behavior something relies on, rewrite it against that behavior instead.

**What done looks like**

- Every test left is anchored to intended behavior.
- Each one would fail on a regression, and only on a regression.
- No test asserts code that no longer exists.
