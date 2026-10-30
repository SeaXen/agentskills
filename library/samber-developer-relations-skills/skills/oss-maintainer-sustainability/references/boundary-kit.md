# Boundary kit

Ready-to-adapt text for moves 1-3, 5 and 6. Adapt the numbers to the user's own budget; never copy a window they cannot keep.

## Contents

- README status block
- Response window wording
- Scope statement
- Saying-no replies
- Intake cuts
- Announced pause
- Backlog reset

## README status block

Template:

```markdown
## Project status

**<Active | Maintenance-only | Seeking maintainers | Paused until YYYY-MM-DD | Archived>**

<Optional one line on a transition under way, e.g. "A maintainer handover is under way; see the pinned announcement.">

- Maintained by <name(s)> in their spare time, about <N> hours a week.
- Expect a first reply to issues within <window>. Security reports: see SECURITY.md.
- In scope: <what gets fixed>. Not in scope: <what will be declined>.
- Questions go to <discussion space>, not the issue tracker.
```

Input: solo maintainer, 3 hours a week, wants to stop adding features.
Output:

```markdown
## Project status

**Maintenance-only**

- Maintained by one person in their spare time, about 3 hours a week.
- Expect a first reply to issues within 30 days; many will wait longer. Security reports: see SECURITY.md.
- In scope: security fixes and compatibility with new Python releases. Not in scope: new features or new optional backends.
- Questions go to GitHub Discussions, not the issue tracker.
```

## Response window wording

Worked capacity, using the formula in the skill: 3 hours a week x 60 x half on the tracker / 15 minutes per reply = 6 first replies a week, about 25 a month. With 40 new issues a month, cut intake first; with 20, a 30-day window holds.

```
// ✓ Good - window derived from the budget, no promise of a fix
"I read new issues about once a week. Expect a first reply within 30 days; a reply is not a promise of a fix."

// ✗ Bad - a window the budget cannot keep becomes a new source of guilt
"We aim to respond to all issues within 48 hours."
```

## Scope statement

Write what the project will not do, so a request closes by pointer:

```markdown
### Out of scope

- New output formats beyond JSON and YAML.
- Async variants of the public API.
- Support for runtimes past their end of life.
```

## Saying-no replies

Thank, explain, point, close. One or two sentences.

```
// ✓ Good - declines the contribution, not the person, and points at the rule
"Thanks for putting this together. Async support is out of scope (see 'Out of scope' in the README), so I'm closing this; a fork is welcome to carry it."

// ✓ Good - honest about capacity, no false hope
"I can't get to this, and I don't plan to in the future. Closing so it doesn't look like it's coming."

// ✗ Bad - leaves the request open as an implied promise
"Interesting idea, I'll think about it!"
```

## Intake cuts

- Issue forms with blank issues disabled, a bug form that requires a minimal reproduction and version, and a link to the discussion space for questions.
- A `SUPPORT.md` naming where questions go and that nobody owes an answer there.
- Pull requests restricted to collaborators when the inflow is mostly automated or unsolicited; say so in the README so contributors open an issue first.
- Full design of labels, routing and duty belongs to `samber/developer-relations-skills@oss-issue-triage`.

## Announced pause

```markdown
**Paused until 2026-12-01.** I'm taking a break from this project. Issues and PRs stay open but won't be read until then. Security reports go to SECURITY.md and are read by <name> during the pause. If the pause becomes permanent, this notice will say so.
```

Name who reads security reports, or write "security reports will not be read until <date>". Never imply someone reads a channel nobody watches.

The notice's last sentence matters: it commits to converting the pause into a status, never into silence.

## Backlog reset

A one-time sweep, announced first. Never a rolling bot on items waiting for the maintainer.

1. Post the announcement a week ahead, pinned:

   ```markdown
   **Backlog reset on <date>.** I can't work through <N> open issues with the time I have. On <date> I'll close issues older than <age> that have no reproduction and no activity in <period>, with the label `backlog-reset`. Confirmed bugs stay open. If one still matters to you, comment with a current reproduction and I'll reopen it. Security reports belong in SECURITY.md, not here.
   ```

2. Label first, close second, and post the same short comment on each closed item.
3. Keep confirmed bugs open or move them to a pinned "known issues" list; closing a confirmed bug tells reporters the project has no capacity, which is true but should come from a person.
4. Expect a notification wave and some angry replies; answer none individually beyond the reopen rule.

For automated staleness on items waiting for the reporter, use the rules from `samber/developer-relations-skills@oss-issue-triage`, not this sweep.
