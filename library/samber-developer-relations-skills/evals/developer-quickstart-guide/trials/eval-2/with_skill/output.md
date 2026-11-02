# Halyard quickstart rewrite

## 1. Success moment + time budget

**Success moment:** the reader queries a brand-new Postgres branch from their terminal and sees it already contains real data — proof that branching is instant and the copy is real, not a promise.

**Time budget: 5 minutes**, page-load to that query returning rows. (Baseline for this product class is 10 min; committing to 5 because the redesign below removes a manual dashboard trip and a whole extra creation step — see the cut list.)

## 2. Defect table

I don't have the live page or a real terminal to cold-run against, so this table is a structural diagnosis from the six-step shape you described plus the one number you have (62% never reach the final call), not a verified cold run. Treat it as a hypothesis ranked by suspected cost — the verification plan in §5 is what turns it into fact. Ordered by estimated minutes/attrition lost:

| Step (as described)         | Suspected defect                                                                                                             | Cost                                                                                                                       |
| ---------------------------- | ------------------------------------------------------------------------------------------------------------------------------ | ---------------------------------------------------------------------------------------------------------------------------- |
| Auth                          | Almost certainly "find your API key in account settings" — a dashboard trip in the middle of a terminal flow                   | Highest-probability exit point. Leaving the page to hunt a key is the single most common quickstart death per the reference worked example, and it's a full context switch, not just lost seconds |
| Install CLI → Auth → Create project → Create branch | Four sequential gates before the one thing you promised. Every gate is a chance to bail, and you have no per-step data to tell you which one is bleeding people | Cumulative — this is very likely *why* 62% is measured only at the end and not attributed to a step |
| Create project *and* Create branch as separate steps | Two "create" nouns before the payoff, unclear if project is a real prerequisite or accidental ceremony                          | Re-reading, hesitation, "wait, do I need this?" — the kind of friction Hammerly's log exists to catch                        |
| Intro paragraph about branching | Concept explanation before any command — the exact shape of the negative example in this skill's own reference material       | Delays time-to-first-command; costs interest, not just minutes                                                               |
| (unstated) expected output   | You didn't mention output shown at any step, which usually means there isn't any                                              | A reader who can't tell "worked" from "silently didn't" abandons without you ever seeing an error — this is the failure mode that doesn't show up as a support ticket |
| (unstated) fail branches      | Same absence — no documented recovery for the most likely error at auth or CLI install                                        | Converts a 10-second fixable hiccup into a permanent drop                                                                    |

One thing worth naming directly: you and the two engineers running it cleanly isn't evidence the page is fine — it's evidence you're the wrong test. You already have accounts, cached CLI installs, and a cached API key. That's exactly the "author's machine always lies" trap — a SendGrid quickstart that read as finished to its authors was completed by 1 of 20 real workshop participants when someone finally tested it live. Your 62% is the same signal arriving a year later.

## 3. The quickstart page

```markdown
# Create your first Postgres branch in 5 minutes

You'll spin up a branch of a Postgres database and query it from your
terminal — a full, isolated copy, ready in seconds.

## Before you start

- macOS or Linux (Windows: use WSL — [setup guide](#))
- A GitHub account, used to sign in with one click. No password to create,
  no card required.

## 1. Install the CLI

    curl -fsSL https://cli.halyard.dev/install.sh | bash -s -- v2.4.0

You should see:

    halyard CLI v2.4.0 installed to /usr/local/bin/halyard
    Run `halyard login` to connect your account.

`command not found: halyard`? Restart your shell, or run
`export PATH=$PATH:/usr/local/bin` and try again.

## 2. Log in

    halyard login

You should see:

    Opening https://halyard.dev/device?code=WXYZ-1234 in your browser...
    Waiting for confirmation... done.
    Logged in as you@example.com.

Browser didn't open? Visit the printed URL manually and type in the code.

## 3. Create a branch

    halyard branch create dev

You should see:

    No project found in this account — created "quickstart" with sample data.
    Branching "quickstart/main" -> "quickstart/dev"... done (1.8s).
    Connection string saved to .halyard/dev.env

First run creates a starter project called `quickstart`, seeded with sample
rows, so there's something to see in the next step. If you already have a
project, pass `--project <name>` instead.

`branch name already exists`? Someone on your team already has `dev` —
pick another name, e.g. `halyard branch create dev-<yourname>`.

## 4. See it work

    halyard branch query dev "select count(*) from orders"

You should see:

     count
    -------
        50

Empty result or connection error? Wait a few seconds and retry — a branch
can take up to 10 seconds to finish attaching storage.

## What just happened

`dev` is a full, writable copy of `quickstart/main`, created by copying
storage pointers rather than the rows themselves — that's why it took under
two seconds. Writes in `dev` stay isolated until you merge or promote it.

## Next steps

- [Connect your app](#) using the connection string in `.halyard/dev.env`
- [CLI reference](#)
- [Community Discord](#)
```

## 4. Cut list

| Removed from the page                          | Where it lives now                                          |
| ----------------------------------------------- | ------------------------------------------------------------- |
| Branching concept explanation (intro paragraph) | "What just happened" (2 sentences) + a linked concepts page   |
| Manual "copy your API key from account settings" | Deleted outright — replaced with `halyard login`'s OAuth device flow, no dashboard visit |
| Standalone "create project" step                | Folded into `branch create`'s first-run auto-provisioning; explicit project management moved to the CLI reference |
| Windows-specific install steps                  | Linked WSL setup page                                          |
| Region selection, branch expiry, role/permission flags | CLI reference                                            |

The auth and project cuts aren't edits — they're deletions of the two steps most likely responsible for the 62%. Everything else here is a rewording; those two are the actual fix.

## 5. Verification plan

This page has not been cold-run — the plan below is what has to happen before it ships, and it's non-negotiable per this skill's own gate ("never rewrite from reading alone").

- Clean container or VM, no cached `halyard` binary, no dotfiles, no existing Halyard account.
- Fresh GitHub-linked Halyard account created as part of the run, not beforehand.
- Timer starts at page load, not at the first command.
- Run every block verbatim. Any command you have to silently correct is a defect — log it.
- **Two reader profiles**, run separately: (a) someone fluent with Postgres and CLI tools generally but who has never touched Halyard, (b) someone newer to CLI-driven infra tools. Profile (b) is the one that catches assumed knowledge you and the two engineers who wrote this can no longer see.
- Log a defect table per run: step, elapsed, command ran verbatim (y/n), output matched (y/n), defect.
- Keep a friction log alongside it — green/yellow/red per Hammerly's convention. Three yellows in one step means split the step.
- Ship only when: every command succeeds as written, every output matches, zero prerequisites surface after step 1, elapsed time is ≤5 min, and both readers reach the query result without leaving the page.
- Once it passes, wire a CI job that runs the four command blocks against the published CLI and a throwaway project on a schedule — this catches the CLI or API drifting out from under the page, which is presumably part of how this got to a year old without anyone noticing it had rotted.

## 6. Instrumentation

Right now you have exactly one number — 62% never reach `create branch` — and no way to tell which of the four gates is actually failing. Fix that before you fix anything else:

- **Events to add**, one per step: `page_loaded`, `cli_install_confirmed`, `login_complete`, `branch_created`, `query_success` (the success event).
- **Step-level drop-off** — this is the one metric you're currently missing, and it's an hour of wiring against events you're about to add anyway. It'll tell you outright whether this is an auth problem, a CLI-install problem, or something else entirely, instead of guessing from structure the way this document had to.
- **Median page-load-to-`query_success` time** — your real number against the 5-minute commitment above.
- **Completion rate** — you already have this; keep tracking it as the check that the rewrite moved the number at all.
- **Support tickets/issues quoting a step number** — near-zero cost, and each one will point at a sentence, not a vague "setup is confusing."
- **Day-7 return of branch-creators vs. non-completers** — once completion is healthy, this is the metric that tells you whether "create branch" was even the right success moment to optimize for.

Measure four weeks post-launch as your baseline, then commit to a relative improvement (e.g., cut drop-off in half) — don't import a completion-rate target from somewhere else; nothing you'd import was measured against this page's actual audience.