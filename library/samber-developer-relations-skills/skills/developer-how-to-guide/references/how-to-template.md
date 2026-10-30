# How-to page template

Fill this skeleton section by section. Delete a section only where the rule beside it says it may go. The page is the goal, the checks, the steps and the proof - everything else is a link.

Contents: skeleton · title and goal line · prerequisites · steps · variants · checkpoint and verification · roll back · clean up · next steps

The front matter keys are illustrative: use your docs platform's own fields (content type, owner, review date) where it has them. Where the docs set has its own section names or extra sections (a "Discussion" or "What's next" block, for example), follow the set.

## Skeleton

````markdown
---
title: <Verb> <object> [<qualifier that names the constraint>]
content_type: how-to
owner: <team, not a person>
tested_with: <product or SDK version; for an unversioned hosted product, the API version or the run date>
last_verified: <YYYY-MM-DD>
---

# <Verb> <object> [<constraint>]

<Goal line: when a reader wants this, in one or two sentences. Adds what the title lacks.>

## Prerequisites

- <Narrowest role or scope that works>, granted by <who>. Check: `<command>` shows `<expected>`.
- <Tool and version floor>. Check: `<command>` (expected: `<output>`).
- <Earlier task>: see [<title of the guide that does it>](<link>).
- <Billable resource this guide creates, if any.>
- <Production task: rehearse on staging or a test tenant first; change window and who to notify.>

## Steps

1. <Location>, <imperative action that states its purpose>:

   ```<lang>
   <one copyable command, no prompt, no secret pasted inline, placeholders as UPPER_SNAKE>
   ```

   Replace `PLACEHOLDER_NAME` with <what, and where to find it>.

   The output is similar to the following:

   ```text
   <real output from a real run>
   ```

2. If you <variant condition>, <action>. Otherwise, <action>. Safe to re-run.

3. Check the new state before you change anything irreversible:

   ```<lang>
   <independent read>
   ```

   Continue only when <expected result>.

4. <What this step changes.>

   > **Warning:** <consequence and its scope>. <Whether it can be undone, and from what.> Do not re-run this step; check state with `<command>` first.

   1. <Safeguard: dry run, diff, plan, snapshot, export.>
   2. <The action itself: interactive form, or applying the reviewed artefact from sub-step 1.>

5. Optional: <step the goal does not require>.

## Verify the result

<Independent check the reader runs. For a propagating change: the expected delay and a poll with a timeout.>

```<lang>
<command or request>
```

```text
<expected output>
```

If you see <failure signal> instead, see [<troubleshooting entry>](<link>).

## Roll back

Roll back if <signal that means the change failed>.

<Steps that return the system to its previous state through its own history or the safeguard's backup, or: "This change cannot be undone after step N.">

## Clean up

Clean up only once you have decided not to roll back.

<Delete the test resources this guide created, or delete this section.>

## Next steps

- <The most common next goal>: [<guide title>](<link>)
- <Reference for every option used above>: [<reference page>](<link>)
````

## Section rules

### Title and goal line

- Verb plus object plus, when needed, the constraint that makes this page different from its siblings: "Rotate an API key without downtime", "Deploy the worker on Kubernetes".
- Follow the collection's existing convention (bare imperative or "How to…"), never mixed in one navigation group.
- The goal line answers "when do I want this?" GitLab's example: "Create an issue when you want to track bugs or future work." Opening with the title's verb is fine; a goal line that only restates the title is not. Never start a sentence the steps finish.
- For a production task, add how long it takes and what it disrupts.

### Prerequisites

- Keep the docs set's existing heading ("Prerequisites", "Before you begin"). With no convention, use GitLab's plural "Prerequisites" even for one item.
- Roles and permissions first, at the narrowest scope that works; then software and versions; then earlier tasks.
- Each item carries a check command or a link. A prerequisite the reader cannot verify is discovered at step 4 instead.
- Name the version floor and the region or tenancy here, not in a step.
- No plan marketing; state the requirement plainly.
- Add a wrong-page cue where readers often land by mistake: "Running self-hosted? See <sibling page>."

### Steps

- One action per step. Combine two only when they happen on the same screen.
- Order inside a step (Google's): description of the action, command, placeholder explanations, explanation of the command, output.
- Use the exact UI label the reader clicks. Add a screenshot only where the screen is hard to find, give it alt text that states what it shows, and re-capture it when the UI changes. Prefer procedures a keyboard alone can complete.
- Describe what a command does, never "run the following command".
- One copyable block per action. Output in its own block, never inside the command block.
- Define each placeholder right after its block. Inside code, write placeholders as bare `UPPER_SNAKE` names or shell variables set once early, never `<NAME>`: pasted unfilled, angle brackets are shell redirection. Regional endpoints and tenant IDs are placeholders, not hard-coded values.
- Set non-secret environment variables once, early, so later blocks paste safely. Load secrets through the tool's own credential prompt, the secret manager's CLI, or a no-echo prompt (`read -rs VAR` in bash or zsh), never `export VAR=<secret>`, and pass them to tools through stdin or a config file where the tool allows.
- Use test-mode credentials and objects in every example; mark any step that needs live mode.
- A step in another vendor's UI names the screen, links that vendor's page, and lists only what the reader enters there.
- One-step procedures use a bullet, not a number.
- End an idempotent step with "Safe to re-run." and put "Do not re-run" in the warning of any step past the point of no return.
- Ten steps is the ceiling (Good Docs Project: "a maximum of 8-10 steps per task"); past it, split into sub-tasks with their own pages or headings.

### Variants

- Default to one recommended path. Write each remaining variant in the shape the SKILL.md variant table picks.
- An inline conditional names the condition first: "If your project is in the EU region, …".
- Tabs only when every tab holds the same steps in different syntax. A mandatory step never lives inside one tab.
- When procedures span sibling headings, restate the context in each first step (Google's rule), because readers land on headings from search.

### Checkpoint and verification

- A page with a point of no return carries two checks: the checkpoint before the irreversible step, and the verification step at the end. When the irreversible step is the last one, it follows the verification (Cloudflare's order) and gets a one-line check of its own.
- Each check is a command, request or screen with its expected output, never a statement.
- Verify through a path independent of the action (read after write; the dashboard after the CLI).
- For a propagating change, state the expected delay, poll with a timeout, and say what "still pending" looks like versus "failed".
- One line on what failure looks like and where to go.

### Roll back

- Required when any step is destructive, irreversible or outage-causing. Otherwise delete the section.
- Open with the decision signal: the error rate, status code or symptom that means "roll back now". Steps without a trigger get run too late.
- Roll back through the system's own history (previous secret version, previous revision, the still-active old credential) when one exists; otherwise restore from the safeguard's snapshot or export.
- When roll back is impossible, say so here and in the step's warning.

### Clean up

- Required when the guide creates test resources, temporary credentials or billable objects the reader does not keep. Otherwise delete the section.
- Sits after roll back: cleaning up first can delete the path back.

### Next steps

- Three links by default, or the docs set's own limit: the next goal, the reference for the options used, and help. Further reading that was not needed for the task goes here, never in the steps.
