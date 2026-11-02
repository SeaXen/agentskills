Yes. 14 steps, way past budget. CLI baseline: 5 min (per success moment: "command produces promised artefact"). This is a scope problem, not a wording problem — fixable in hours, not week.

**Real success moment for Tessera:** CLI compiles tokens file into platform-specific output, reader inspects it. That's it. Steps 9-12 only.

**Cut list, ranked by minutes saved (estimates — no cold run done yet):**

1. **Cut step 13 (CI action).** Est 5-15 min. Assumes CI provider, repo push access, wait-for-run. Move to separate "CI integration" how-to, link from Next steps.
2. **Cut/defer steps 3-7 (account, verify email, login, workspace, invite teammate).** Est 8-20 min combined. Biggest single lever. Question: does `tessera build` need auth at all? If no — delete all 5 steps from critical path, push signup after first success. If yes — collapse into one `tessera login` step (device-flow style, like `gh auth login`), and still cut "create workspace" + "invite teammate" — team features, not needed for one reader's first build.
3. **Cut step 8 (VS Code extension).** Est 2-4 min. Different product surface, not the CLI's job. Link in Next steps.
4. **Cut step 14 (theming overview).** Est 5-20 min reading, zero doing. Quickstarts drop concept explanations by definition. Link only.
5. **Merge steps 1+2 (Homebrew + install CLI).** Forcing Homebrew is a named-vendor-tool defect (mac-only, excludes Linux/Windows readers). One "install" step, per-OS one-liner, alternatives behind a link.

**Resulting core path, 5 steps:**
```
1. Install the CLI
2. Create a tokens file
3. Configure a build target
4. Run the build
5. Inspect the output   ← success moment
```
Matches the 3-6 step ceiling. Realistic at 5 min if no account is required first.

Everything cut still exists — just not blocking first success: workspace/teammate/CI/theming/VS Code all move to "Next steps" (cap 3 links) or their own pages.

Next: confirm whether `tessera build` can run before login. That single answer decides if steps 3-7 get deleted outright or just reordered after the win.