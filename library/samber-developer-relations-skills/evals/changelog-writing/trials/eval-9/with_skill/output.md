I read the skill and its `format-specifications.md` and `surface-templates.md` references. Before I can write anything I'm missing the one thing the skill calls non-negotiable: the raw material. I don't have Northgate's repo locally (searched — not found), so I can't pull the diff myself.

Given the 2-hour clock, fastest path — pick whichever is quicker for you:

1. **Paste the 22 auto-generated bullets** (PR titles are fine, dependabot ones included — I'll filter them), **or**
2. Give me `owner/repo` on GitHub and I'll try `gh pr list`/`gh api` for the `v3.1.x...v3.2.0` range myself.

Two quick calls to make the entry text right, multiple-choice:

- **Audience**: Northgate's CLI — is the release body read mainly by (a) people installing/upgrading the CLI as end users, (b) people scripting against it / depending on it as a library or in CI (integrators), or (c) both mixed?
- **Breaking/deprecated**: off the top of your head, do any of those 22 PRs change a flag, default, output format, or exit code in a way that could break someone's script — even if it "looks like a fix"? A yes/no per item once I see the list is fine too.

Paste the list and answer the audience question and I'll turn it around immediately — everything else (tiering, dependabot filtering, breaking-change formatting) I can do without further back-and-forth.