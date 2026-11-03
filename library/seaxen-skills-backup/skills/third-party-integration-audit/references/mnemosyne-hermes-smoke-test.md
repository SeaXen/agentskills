# Mnemosyne × Hermes smoke test reference

Condensed example for auditing a third-party Hermes memory integration.

## Context

Target repo: `AxDSan/mnemosyne`

Question:
- what is it?
- is it worth using with Hermes?
- does it actually work in a real install?

## Repo-level findings

Mnemosyne is a local/private memory system for agents, with Hermes integration via:
- memory provider
- plugin/tool surface
- CLI
- MCP server
- SQLite-backed storage with working/episodic concepts

Important code-level finding:
- provider skip contexts included `cron`, `flush`, `subagent`, `background`, `skill_loop`

That matters because a tool can look good in normal chat but still miss automation-heavy Hermes workflows.

## Practical install pattern that worked

1. Inspect local Hermes baseline first.
2. Create a throwaway profile rather than touching `default`.
3. Identify the Python interpreter used by the `hermes` launcher.
4. Install package into Hermes's own venv, not system Python.
5. Run the package installer with `HERMES_HOME` pointing at the throwaway profile.
6. Verify effective config after install.
7. Run a real memory write + recall probe.
8. If reporting is inconsistent, inspect the backing DB directly.

## What broke

### 1. Installer success was not enough

The installer reported success but the resulting profile config contained conflicting provider entries, leaving Hermes effectively on provider `none` until corrected.

Lesson:
- verify the effective config after install
- status command beats installer banner
- if needed, repair using Hermes config CLI

### 2. Stats/inspect did not match actual behavior

Observed:
- real recall worked across a fresh session
- CLI `stats` showed zero episodic memories
- CLI `inspect` returned zero results for the stored token
- direct SQLite inspection showed the fact present in `working_memory`

Lesson:
- when behavior and observability disagree, inspect storage directly before declaring failure
- distinguish working memory from consolidated/episodic storage

## Smoke-test token pattern

Use a unique token such as:
- `atlas-cobalt-731`

Good token properties:
- unique
- easy to grep/query
- easy to compare in exact-match answers

Test sequence:
1. store the token through the actual user-facing tool path
2. recall it in the same or resumed session if relevant
3. recall it again from a fresh session
4. inspect backing storage path and tables if the reporting layer looks wrong

## Practical verdict template

Use language like:
- core path works
- installer/config path is rough
- observability is misleading
- keep it in an isolated profile for now
- not ready as the default production memory backend if cron/subagent coverage matters

## Reusable lessons

- Never trust installer success text without post-install verification.
- For Hermes integrations, runtime venv identification is mandatory.
- Fresh-session recall is a much stronger proof than same-session recall.
- A reporting bug is different from a storage bug; direct DB inspection can separate them.
- Profile isolation needs explicit verification because shared/global storage paths can mask leakage.
