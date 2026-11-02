**Yes, 14 is too long — but the fix is regrouping, not rewriting. Half a day, not a week.**

The list mixes five different jobs into one flat sequence: install, auth, team setup, editor tooling, and CI. Only one of those is the "does this thing work" path. Split them.

## Getting Started (5 steps — this is the only numbered list)

1. **Install Tessera** — `brew install tessera` (or link the curl/npm alternative for non-Homebrew users)
2. **Create a tokens file** — ship `tessera init` if you don't already, so this step produces a working example instead of a blank file
3. **Configure a build target**
4. **Run the build**
5. **Inspect the output** ← this is the aha moment. Label it as a checkpoint, show the expected output inline.

That's the Minimum Path to Value: signup-to-first-build with zero detours. Every step you cut here is a step people don't abandon on.

## Move these out, don't delete them

Turn them into separate linked sections/pages, reached from a "Next steps" block after step 5 — not pre-conditions to reach it:

- **Team setup** (create account, verify email, `tessera login`, create workspace, invite a teammate) — its own page. This is 5 of your 14 steps and none of them are required to see the tool work.
- **Editor integration** (install VS Code extension) — one line, own section.
- **CI/CD** (set up the CI action) — own page. Nobody wires CI before they've run the tool once locally.
- **Theming** — this isn't a step, it's a doc link. Put it under "Learn more," not in the numbered flow.

## One thing to check before you ship this

Does `tessera build` actually work locally without an account? If yes, account/login has no business gating step 1 — move it out as above. If the CLI phones home even for local compilation, that's a product question worth revisiting on its own, because it means nobody can hit the aha moment without first clearing signup + email verification + login — three steps of pure friction before value, which is the single biggest killer of activation rate in CLI tools.

**Effort estimate:** this is reordering and section-splitting of content you've already written, plus one new "Next steps" block. A few hours, not a week.