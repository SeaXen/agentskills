# Large-tree index scaling

Session lesson: the user asked for an `INDEX.md` and initially meant **one root map that includes the folder/file structure**, not an `INDEX.md` file in every directory.

## What went wrong

Literal full-recursive generation created `INDEX.md` files in ~94k directories under `/mnt/tb`. That was technically compliant after clarification, but not the best design for Hermes navigation.

## Better default

For very large trees:
- keep **one root `INDEX.md`** as the main entry point
- add nested `INDEX.md` only for major subtrees that genuinely need deeper maps
- avoid per-directory `INDEX.md` generation unless the user explicitly wants that exact tradeoff

## Recommended explanation to the user

Explain the three shapes clearly before writing:

1. **One root index**
   - one file
   - summarized map of all major folders
   - best default for huge trees

2. **Root + selected nested indexes**
   - root file plus a few major subtree maps
   - best balance for Hermes

3. **Full recursive per-directory indexes**
   - one `INDEX.md` in nearly every directory
   - creates clutter and maintenance noise
   - only do this when the user explicitly insists

## Practical trigger

If the tree count is very large (for example tens of thousands of directories), actively recommend shape #1 or #2 and push back on #3 unless the user is certain.
